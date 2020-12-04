from api.magna import Magna
from bs4 import BeautifulSoup
import httpx

# PMScans.com scraper, NOT SURE IF 100% WORKING
class PMScans(Magna):
    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "PMScans.com"

        # required for accessing the chapters of the manga
        self.ajax_url = "https://www.pmscans.com/wp-admin/admin-ajax.php"
        self.post_data = {"action": "manga_get_chapters", "manga": 0}

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text() == "Page not found - PMScans":
            return True

        return False

    # return the page title
    def page_title(self):
        return self.get_title().replace("– PMScans", "").strip()

    # return the description
    def manga_description(self):
        try:
            __desc = self.soup.find("div", class_="description-summary")
        except Exception:
            return ""

        return __desc.find("p").get_text()

    # return the manga image
    def manga_image(self):
        return self.soup.find("div", class_="summary_image").find("img")["data-src"]

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        self.post_data["manga"] = int(
            self.soup.find("div", id="manga-chapters-holder")["data-id"]
        )

        chapters = []
        raw = BeautifulSoup(
            httpx.post(url=self.ajax_url, data=self.post_data).text,
            "html.parser",
        )

        for chapter in raw.find_all("li", class_="wp-manga-chapter"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = chapter.find("a").get_text().strip()
            i["chapter_url"] = chapter.find("a")["href"].replace(
                "http://", "https://"
            )  # replace the http with https
            i["b64_hash"] = Magna.encode_base64(
                href=chapter.find("a")["href"].replace(
                    "http://", "https://"
                )  # replace the http with https
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - PMScans", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # THIS MIGHT BE UPDATED AND CHANGED IN THE FUTURE, FOR NOW, THIS IS THE CURRENT BEST SOLUTION
        test = str(self.soup.find("script", id="chapter_preloaded_images"))
        lister = (
            test.replace(
                '<script id="chapter_preloaded_images" type="text/javascript">', ""
            )  # remove the start script tag
            .replace("</script>", "")  # remove the end script tag
            .replace(
                "var chapter_preloaded_images =", ""
            )  # remove unnecessary js additionals
            .replace(
                ", chapter_images_per_page = 1;", ""
            )  # remove unnecessary js additionals
            .replace('"', "")  # remove the qoutations for easier converstion to list
            .replace("\\", "")  # remove the backslash from the urls
            .replace("[", "")  # remove the brackets
            .replace("]", "")  # remove the brackets
            .replace(
                "http://", "https://"
            )  # replace the http to https, since it is if I try to request
            .strip()
        )

        # get all images
        imgs = lister.split(",")  # split each

        return imgs

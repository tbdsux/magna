from api.magna import Magna
from bs4 import BeautifulSoup
import httpx

# Dark-scans.com scraper,
class DarkScans(Magna):
    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "Dark-scans.com"

        # required for accessing the chapters of the manga
        self.ajax_url = "https://dark-scans.com/wp-admin/admin-ajax.php"
        self.post_data = {"action": "manga_get_chapters", "manga": 0}

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text() == "Page not found - Dark Scans":
            return True

        return False

    # return the page title
    def page_title(self):
        return self.get_title().replace("– Dark Scans", "").strip()

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
            i["chapter_url"] = chapter.find("a")["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title()

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="reading-content")

        # get all images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["data-src"].strip())

        return imgs

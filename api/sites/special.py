########### SPECIAL WEBSITES FROM ORIGINAL SOURCE GIVERS

from api.magna import Magna
from api.magna import GenkanWP

# Leviatanscans.com scraper
class LeviatanScans(GenkanWP, Magna):
    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://leviatanscans.com"
        self.source = "Leviatanscans.com"
        self.title = "Leviatan Scans -"


# Reaperscans.com scraper
class ReaperScans(GenkanWP, Magna):
    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://reaperscans.com"
        self.source = "Reaperscans.com"
        self.title = "Reaper Scans -"


# SKScans.com scraper
class SKScans(GenkanWP, Magna):
    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://skscans.com"
        self.source = "SKscans.com"
        self.title = "SK Scans -"


# AsuraScans.com scraper
class AsuraScans(Magna):
    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "AsuraScans.com"

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text().startswith("Page not found"):
            return True

        return False

    # return the page title
    def page_title(self):
        return self.get_title().replace("- Asura Scans", "").strip()

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="entry-content entry-content-single")
        return __desc.get_text()

    # return the manga image
    def manga_image(self):
        # this might change in the future
        try:
            return self.soup.find("div", class_="thumb").find("img")["data-cfsrc"]
        except Exception:
            return self.soup.find("div", class_="thumb").find("img")["src"]

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("div", id="chapterlist")
        chapters = []

        for chapter in chapter_container.find_all("li"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = (
                chapter.find("a").find("span", class_="chapternum").get_text()
            )
            i["chapter_url"] = chapter.find("a")["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - Asura Scans", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", id="readerarea")

        credit_discord_ending = "https://asurascans.com/wp-content/uploads/2020/10/ENDING-PAGE.jpg"  ############# THIS MIGHT CHANGE IN THE FUTURE

        # get all of the images
        imgs = []
        for i in container.find_all("img", class_="aligncenter"):
            try:
                imgs.append(i["src"])  # append the source image file
            except Exception:
                pass

        # append last, for credits
        imgs.append(credit_discord_ending)

        return imgs
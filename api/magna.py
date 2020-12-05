import httpx
from bs4 import BeautifulSoup
import base64

## WORDPRESS SITES HANDLER
class WordpressSites:
    def __init__(self, soup):
        self.soup = soup
        self.ajax_url = None
        self.post_data = {"action": "manga_get_chapters", "manga": 0}

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text().startswith("Page not found"):
            return True

        return False

    # return the description
    def manga_description(self):
        try:
            __desc = self.soup.find("div", class_="description-summary")
        except Exception:
            return ""

        return __desc.find("p").get_text()

    # return the chapters from ajax response
    def ajax_get_chapters(self):
        # get the chapters
        self.post_data["manga"] = int(
            self.soup.find("div", id="manga-chapters-holder")["data-id"]
        )

        raw = BeautifulSoup(
            httpx.post(url=self.ajax_url, data=self.post_data).text,
            "html.parser",
        )

        return raw

    # return the chapters from the soup itself
    def built_get_chapters(self):
        return self.soup.find("ul", class_="main version-chap")

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        container = []
        if self.ajax_url:
            container = self.ajax_get_chapters()
        else:
            container = self.built_get_chapters()

        chapters = []

        for chapter in container.find_all("li", class_="wp-manga-chapter"):
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

    # return the description
    def manga_description(self):
        try:
            __desc = self.soup.find("div", class_="description-summary")
        except Exception:
            return ""

        return __desc.find("p").get_text()

    # return the manga image
    def manga_image(self):
        try:
            return self.soup.find("div", class_="summary_image").find("img")["data-src"]
        except Exception:
            return self.soup.find("div", class_="summary_image").find("img")["src"]

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="reading-content")

        # get all images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["data-src"].strip())

        return imgs


## >> Main CLASS Handler for all Websites to Scrape
class Magna:
    def __init__(self, soup, url):
        self.soup = soup
        self.request_url = url
        self.source = ""  # the source will be set in the subclass

    # CHECKS IF THERE WAS AN ERROR IN THE REQUESTED PAGE
    def validate_error(self):
        pass

    @classmethod
    async def initialize(cls, url):
        # get the source
        source = ""
        async with httpx.AsyncClient() as client:
            source = await client.get(url, timeout=None)

        await client.aclose()

        # return the scraped page
        return cls(BeautifulSoup(source.text, "html.parser"), url)

    # get the <title></title> tag from the soup
    def get_title(self):
        return self.soup.title.get_text()

    # >>------------------------------------------------------------------------------
    @staticmethod
    def encode_base64(href):
        return base64.b64encode(href.encode("ascii")).decode("ascii")

    @staticmethod
    def decode_base64(hash):
        return base64.b64decode(hash.encode("ascii")).decode("ascii")

    # >>------------------------------------------------------------------------------
    ### Main Manga Info - OVERRIDE THESE METHODS IN THE SUBCLASSES

    def page_title(self):
        return None

    def manga_description(self):
        return None

    def manga_image(self):
        return None

    def extract_chapters(self):
        return None

    ### Main Manga Info - OVERRIDE THESE METHODS IN THE SUBCLASSES

    # >>------------------------------------------------------------------------------
    ### Manga Chapter Images - OVERRIDE THESE METHODS IN THE SUBCLASSES

    def chapter_title(self):
        return None

    def chapter(self):
        return None

    ### Manga Chapter Images - OVERRIDE THESE METHODS IN THE SUBCLASSES

    # >>------------------------------------------------------------------------------
    # Return the BASIC Info and CHAPTERS of the Manga
    async def Extract(self):
        # get basic manga info
        manga = {
            "source": self.source,
            "request": self.request_url,
            "title": self.page_title(),
            "description": self.manga_description(),
            "image": self.manga_image(),
            "chapters": self.extract_chapters(),
        }

        return manga

    # >>------------------------------------------------------------------------------
    # Return the Images in the Manga CHAPTER
    async def ChapterImages(self):
        # get the images
        chapter = {
            "source": self.source,
            "request": self.request_url,
            "title": self.chapter_title(),
            "images": self.chapter(),
        }

        return chapter

import httpx
from bs4 import BeautifulSoup
import base64

# Main CLASS Handler for all Websites to Scrape
class Magna:
    def __init__(self, soup):
        self.soup = soup
        self.source = ""  # the source will be set in the subclass

    @classmethod
    async def initialize(cls, url):
        # get the source
        source = ""
        async with httpx.AsyncClient() as client:
            source = await client.get(url, timeout=None)

        await client.aclose()

        # return the scraped page
        return cls(BeautifulSoup(source.text, "html.parser"))

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
            "title": self.chapter_title(),
            "images": self.chapter(),
        }

        return chapter

"""
This is where all handlers all configured.
"""

import httpx
from bs4 import BeautifulSoup
import base64
import cfscrape

## MStream WP HANDLER
class MStreamWP:
    """
    Handler for websites that have MStream WP Theme.
    """

    def __init__(self, soup):
        self.soup = soup
        self.err_title = ""
        self.source = ""
        self.def_title = ""

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text().startswith(self.err_title):
            return True

        return False

    # return the page title
    def page_title(self):
        return self.get_title().replace(self.def_title, "").strip()

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="entry-content entry-content-single")
        return __desc.get_text()

    # return the manga image
    def manga_image(self):
        # this might change in the future
        try:
            return self.soup.find("div", class_="thumb").find("img")["data-src"]
        except Exception:
            return self.soup.find("div", class_="thumb").find("img")["src"]

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(self.def_title, "").strip()

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


## GENKAN WP HANLDER
class GenkanWP:
    """
    Main handler for websites that have Genkan WP Theme.
    """

    def __init__(self, soup):
        self.soup = soup
        self.base_url = ""
        self.title = ""

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text().strip().endswith("Not Found"):
            return True

        return False

    # return the page title
    def page_title(self):
        try:
            rtitle = self.soup.find_all("title")[1]  # get the second title
            title = rtitle.get_text()
        except Exception:
            title = (
                self.soup.title.get_text().replace(self.title, "").strip()
            )  # there might be a problem with other sites though, ..

        return title

    # return the description
    def manga_description(self):
        desc_container = self.soup.find(
            "div", class_="col-lg-9 col-md-8 col-xs-12 text-muted"
        )
        try:
            __desc = (
                desc_container.get_text()
                .replace(
                    desc_container.find("div", class_="heading").get_text(), ""
                )  # remove the `Description` text
                .replace(
                    desc_container.find("div", class_="row py-2").get_text(), ""
                )  # remove the chapters container texts
                .strip()  # remove leading and trailing spaces
            )
        except Exception:
            __desc = ""

        return __desc

    # return the manga image
    def manga_image(self):
        return self.base_url + (
            self.soup.find("div", class_="media media-comic-card")
            .find("a")["style"]  # img src is from the backround-image
            .replace("background-image:url(", "")
            .replace(")", "")
        )

    # return the manga available chapters
    def extract_chapters(self):
        # get each div chapter
        containers = self.soup.find_all("div", class_="list-item col-sm-3 no-border")

        chapters = []

        for chapter in containers:
            raw = chapter.find("a", class_="item-author text-color")
            # get the chapter page and title
            i = {}
            i["chapter_name"] = raw.get_text().strip()
            i["chapter_url"] = raw["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=raw["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # get the chapter title
    def chapter_title(self):
        return self.page_title()  # same with page title

    # RETURN THE MANGA CHAPTER IMAGES
    def chapter(self):
        # MANUAL COMPILATION, THERE MIGHT BE ERRORS IN THE FUTURE
        b_script = self.soup.find("div", class_="container py-5").find_all("script")
        script = ""

        # the script tag where the images are has a string 'window.chapterPages'
        for i in b_script:
            if "window.chapterPages" in str(i):
                script = str(i).split(";")[3]
                break

        raw = (
            script.split("]")[0]
            .replace("window.chapterPages = ", "")
            .replace("[", "")
            .replace("]", "")
            .replace("\\", "")
            .replace('"', "")
        )

        # fix each and convert to list, if i doesn't start with https://
        imgs = [
            self.base_url + i if not i.startswith("https://") else i
            for i in raw.split(",")
        ]

        return imgs


## WORDPRESS SITES HANDLER
class WordpressSites:
    """
    Main handles for websites that have Wordpress structure.
    Some complex websites, have overriden the methods below.
    """

    def __init__(self, soup):
        self.soup = soup
        self.replace = {}
        self.ajax_url = None
        self.post_data = {"action": "manga_get_chapters", "manga": 0}

    def page_title(self):
        return self.remove_other_strings(
            self.get_title().replace(self.replace["title"], "").strip()
        )

    def chapter_title(self):
        return self.remove_other_strings(
            self.get_title().replace(self.replace["chapter_title"], "").strip()
        )

    def remove_other_strings(self, title_string: str):
        try:
            for i in self.replace["others"]:
                title_string = title_string.replace(i, "")
        except KeyError:
            # do nothing if it is not set or defined in the subclasses
            pass

        # return the title
        return title_string.strip()

    def validate_error(self):
        if self.soup.title.get_text().startswith("Page not found"):
            return True

        return False

    def manga_description(self):
        try:
            __desc = self.soup.find("div", class_="description-summary")
        except Exception:
            return ""

        return __desc.find("p").get_text()

    def ajax_get_chapters(self):
        """
        It gets the chapters from the ajax api. Some websites use ajax for 'better performance'.
        """

        # get the chapters
        self.post_data["manga"] = int(
            self.soup.find("div", id="manga-chapters-holder")["data-id"]
        )

        raw = BeautifulSoup(
            httpx.post(url=self.ajax_url, data=self.post_data).text,
            "html.parser",
        )

        return raw

    def built_get_chapters(self):
        """
        It returns the chapters from the website source itself.
        """

        return self.soup.find("ul", class_="main version-chap")

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

    def manga_image(self):
        try:
            return self.soup.find("div", class_="summary_image").find("img")["data-src"]
        except Exception:
            return self.soup.find("div", class_="summary_image").find("img")["src"]

    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="reading-content")

        image = ""

        # get all images
        imgs = []
        for i in container.find_all("img"):
            try:
                image = i["data-src"].strip()
            except Exception:
                try:
                    image = i["data-lazy-src"].strip()
                except Exception:
                    image = i["src"].strip()

            if image.startswith("http"):
                imgs.append(image)

        return imgs


## >> Main CLASS Handler for all Websites to Scrape
class Magna:
    """
    Main class handler for all websites to scrape.
    """

    def __init__(self, soup, url):
        """
        **soup** : BeautifulSoup parsed html
        **url** : the requested url by client / user
        """

        self.soup = soup
        self.request_url = url
        self.source = ""  # the source will be set in the subclass

    # CHECKS IF THERE WAS AN ERROR IN THE REQUESTED PAGE
    def validate_error(self):
        """
        Check if page is an error page or not.
        Other websites do not send 404 status on error so, I think this is a better approach.
        """

        pass

    @classmethod
    async def initialize(cls, url):
        """
        Magna Initializer, it requests for the website's page source, then parses it with bs4.
        """

        # SPECIAL WEBSITE THAT USE CLOUDFLARE
        if url.startswith("https://leviatanscans.com/"):
            scraper = cfscrape.create_scraper()

            # return the scraper url src page
            return cls(BeautifulSoup(scraper.get(url).text, "html.parser"), url)

        # define user-agent header
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }

        # get the source
        source = ""

        async with httpx.AsyncClient() as client:
            source = await client.get(url, timeout=None, headers=headers)

        # return the scraped page
        return cls(BeautifulSoup(source.text, "html.parser"), url)

    # get the <title></title> tag from the soup
    def get_title(self):
        """
        It returns the title of the page.
        """

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
        """
        Replace page title. Example: 'Amazing Anime - Manga Website' == 'Amazing Anime'
        """

        return None

    def manga_description(self):
        """
        Returns the manga description from the website. It is overriden depending on how each websites work.
        """

        return None

    def manga_image(self):
        """
        Returns the manga image banner from the website.
        """

        return None

    def extract_chapters(self):
        """
        It extracts and parses the chapters from the given html soup (ajax api / web source).
        """

        return None

    ### Main Manga Info - OVERRIDE THESE METHODS IN THE SUBCLASSES

    # >>------------------------------------------------------------------------------
    ### Manga Chapter Images - OVERRIDE THESE METHODS IN THE SUBCLASSES

    def chapter_title(self):
        """
        Returns title of the manga chapter.
        """

        return None

    def chapter(self):
        """
        Extract all manga chapter imges from the website chapter.
        """

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

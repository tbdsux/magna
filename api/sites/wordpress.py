########### THESE SITES HAVE SIMILAR STRUCTURES, SO....

from api.magna import Magna, WordpressSites


class ManhwaTOP(WordpressSites, Magna):
    """
    ManhwaTOP.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {"title": "- MANHWATOP", "chapter_title": "- MANHWATOP"}
        # website source
        self.source = "Manhwatop.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://manhwatop.com/wp-admin/admin-ajax.php"


class DarkScans(WordpressSites, Magna):
    """
    Dark-scans.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {"title": "– Dark Scans", "chapter_title": ""}
        # website source
        self.source = "Dark-scans.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://dark-scans.com/wp-admin/admin-ajax.php"


class WebToon(WordpressSites, Magna):
    """
    Webtoon.xyz scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "Manhwa : Read Manhwa Free at WEBTOON XYZ",
            "chapter_title": " - WEBTOON XYZ",
        }
        # website source
        self.source = "Webtoon.xyz"

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="description-summary")
        temp = __desc.find_all("p")

        try:
            return temp[1].get_text()
        except Exception:
            return temp[0].get_text()


class IsekaiScan(WordpressSites, Magna):
    """
    IsekaiScan.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "- Read manga online in english, you can also read manhua, manhwa in english for free. Tons of Isekai manga, manhua and manhwa are available.",
            "chapter_title": " - WEBTOON XYZ",
        }
        # website source
        self.source = "IsekaiScan.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://isekaiscan.com/wp-admin/admin-ajax.php"


class Hiperdex(WordpressSites, Magna):
    """
    Hiperdex.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "» Hiperdex",
            "chapter_title": " - Hiperdex",
        }
        # website source
        self.source = "Hiperdex.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://hiperdex.com/wp-admin/admin-ajax.php"

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        raw_imgs = self.soup.find_all("img", class_="wp-manga-chapter-img")

        # get all images
        imgs = []
        for i in raw_imgs:
            imgs.append(i["src"].strip())

        return imgs


class Toonily(WordpressSites, Magna):
    """
    Toonily.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "- Toonily",
            "chapter_title": " - Toonily",
        }
        # website source
        self.source = "Toonily.com"


class MangaTX(WordpressSites, Magna):
    """
    Mangatx.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # website source
        self.source = "Mangatx.com"

    # return the page title
    def page_title(self):
        return self.soup.find("div", class_="post-title").find("h1").get_text().strip()

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="description-summary")
        try:
            return __desc.find("p").get_text()
        except Exception:
            return (
                __desc.find("div", class_="summary__content show-more")
                .get_text()
                .strip()
            )

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - Mangatx", "")


class PMScans(WordpressSites, Magna):
    """
    PMScans.com scraper, NOT SURE IF 100% WORKING
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "– PMScans",
            "chapter_title": " - PMScans",
        }
        # website source
        self.source = "PMScans.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://www.pmscans.com/wp-admin/admin-ajax.php"

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        container = self.ajax_get_chapters()

        chapters = []

        for chapter in container.find_all("li", class_="wp-manga-chapter"):
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


class AloAlivn(WordpressSites, Magna):
    """
    Aloalivn.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "- Aloalivn.com",
            "chapter_title": "- Aloalivn.com",
        }
        # website source
        self.source = "Aloalivn.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://aloalivn.com/wp-admin/admin-ajax.php"


class ManhuaFast(WordpressSites, Magna):
    """
    Manhuafast.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "- Manhuafast.com",
            "chapter_title": "- Manhuafast.com",
        }
        # website source
        self.source = "Manhuafast.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://manhuafast.com/wp-admin/admin-ajax.php"
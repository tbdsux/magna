########### SPECIAL WEBSITES FROM ORIGINAL SOURCE GIVERS

from api.magna import Magna, GenkanWP, MStreamWP, WordpressSites


class MMScans(WordpressSites, Magna):
    """
    MM-Scans.com scraper
    """

    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # stuff to be replaced
        self.replace = {
            "title": "– Mmscans",
            "chapter_title": "- Mmscans",
        }
        # website source
        self.source = "MM-Scans.com"
        # required for accessing the chapters of the manga
        self.ajax_url = "https://mm-scans.com/wp-admin/admin-ajax.php"

class MerakiScans(Magna):
    """
    Merakiscans.com scraper
    """

    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "Merakiscans.com"
        self.base_url = "https://merakiscans.com"

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text() == "404 Page Not Found - Meraki Scans":
            return True

        return False

    # return the page title
    def page_title(self):
        return self.get_title().replace("- Manga Detail Meraki Scans", "").strip()

    # return the description
    def manga_description(self):
        spans = self.soup.find("div", id="content2").find_all("span")[
            -1
        ]  # the last span contains the description
        return spans.get_text()

    # return the manga image
    def manga_image(self):
        return self.base_url + self.soup.find("img", id="cover_img")["src"]

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("table", id="chapter_table").find("tbody")
        chapters = []

        for chapter in chapter_container.find_all("tr"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = chapter.find(
                "td", id="chapter-part"
            ).get_text()  # get the first td
            i["chapter_url"] = self.base_url + chapter["data-href"]
            i["b64_hash"] = Magna.encode_base64(
                href=self.base_url + chapter["data-href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - Meraki Scans", "")

    # extract only the images variable from the script tag
    def manipulate_script(self, script_container):
        raw = script_container.split(";")
        for i in [j.strip() for j in raw]:
            if i.startswith("var images ="):
                return i

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # THIS MIGHT CHANGE IN THE FUTURE
        # get the main container
        try:
            container = self.manipulate_script(
                script_container=str(self.soup.find_all("script")[-3])
            )

            fnames = (
                container.replace("var images =", "")
                .replace("[", "")
                .replace("]", "")
                .replace('"', "")
            )

            # get all of the images
            imgs = []
            for i in fnames.split(","):
                if self.request_url.endswith("/"):
                    imgs.append(self.request_url + i.strip())
                else:
                    imgs.append(self.request_url + "/" + i.strip())

            return imgs

        except Exception:
            return []  # return a blank one if there is a problem


class ZeroScans(GenkanWP, Magna):
    """
    ZeroScans.com
    """

    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://zeroscans.com"
        self.source = "ZeroScans.com"
        self.title = "Zero Scans -"


class SecretScans(GenkanWP, Magna):
    """
    LynxScans.com
    """

    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://lynxscans.com/"
        self.source = "LynxScans.com"
        self.title = "Secret Scans -"


class MethodScans(GenkanWP, Magna):
    """
    MethodScans.com
    """

    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://methodscans.com"
        self.source = "Methodscans.com"
        self.title = "Method Scans -"


class LeviatanScans(GenkanWP, Magna):
    """
    Leviatanscans.com scraper
    """

    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://leviatanscans.com"
        self.source = "Leviatanscans.com"
        self.title = "Leviatan Scans -"


class ReaperScans(GenkanWP, Magna):
    """
    Reaperscans.com scraper
    """

    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://reaperscans.com"
        self.source = "Reaperscans.com"
        self.title = "Reaper Scans -"


class SKScans(GenkanWP, Magna):
    """
    SKScans.com scraper
    """

    def __init__(self, soup, url):
        GenkanWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.base_url = "https://skscans.com"
        self.source = "SKscans.com"
        self.title = "SK Scans -"


class FlameScans(MStreamWP, Magna):
    """
    Flame-Scans.com scraper
    """

    def __init__(self, soup, url):
        MStreamWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.source = "Flame-Scans.com"
        self.err_title = "Not Found, Error 404"
        self.def_title = "| FLAME-SCANS"

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="readercontent")

        scs = (
            str(container.find("script"))
            .split(':["')[1]
            .split("]}]")[0]
            .replace('"', "")
            .replace("\\", "")
        )  # parse the script tag => this is where the images are

        # get all of the images
        imgs = []
        for i in scs.split(","):
            imgs.append(i.strip())

        return imgs


class AsuraScans(MStreamWP, Magna):
    """
    AsuraScans.com scraper
    """

    def __init__(self, soup, url):
        MStreamWP.__init__(self, soup)
        Magna.__init__(self, soup, url)
        self.source = "AsuraScans.com"
        self.err_title = "Page not found"
        self.def_title = "- Asura Scans"

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", id="readerarea")

        # get all of the images
        imgs = []
        for i in container.find_all("img"):
            try:
                imgs.append(i["src"])  # append the source image file
            except Exception:
                pass

        return imgs
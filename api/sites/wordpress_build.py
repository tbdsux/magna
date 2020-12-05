########### THESE SITES HAVE SIMILAR STRUCTURES, SO....

from api.magna import Magna, WordpressSites

# Dark-scans.com scraper
class DarkScans(WordpressSites, Magna):
    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # parent class init

        self.source = "Dark-scans.com"

        # required for accessing the chapters of the manga
        self.ajax_url = "https://dark-scans.com/wp-admin/admin-ajax.php"

    # return the page title
    def page_title(self):
        return self.get_title().replace("– Dark Scans", "").strip()

    # return the chapter title
    def chapter_title(self):
        return self.get_title()


# Webtoon.xyz scraper
class WebToon(WordpressSites, Magna):
    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # parent class init

        self.source = "Webtoon.xyz"

    # return the page title
    def page_title(self):
        return (
            self.get_title()
            .replace("Manhwa : Read Manhwa Free at WEBTOON XYZ", "")
            .strip()
        )

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="description-summary")
        temp = __desc.find_all("p")

        try:
            return temp[1].get_text()
        except Exception:
            return temp[0].get_text()

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - WEBTOON XYZ", "")


# IsekaiScan.com scraper
class IsekaiScan(WordpressSites, Magna):
    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # parent class init

        self.source = "IsekaiScan.com"

        # required for accessing the chapters of the manga
        self.ajax_url = "https://isekaiscan.com/wp-admin/admin-ajax.php"

    # return the page title
    def page_title(self):
        return (
            self.get_title()
            .replace(
                "- Read manga online in english, you can also read manhua, manhwa in english for free. Tons of Isekai manga, manhua and manhwa are available.",
                "",
            )
            .strip()
        )

    # return the chapter title
    def chapter_title(self):
        return self.get_title()


# Hiperdex.com scraper,
class Hiperdex(WordpressSites, Magna):
    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # parent class init

        self.source = "Hiperdex.com"

        # required for accessing the chapters of the manga
        self.ajax_url = "https://hiperdex.com/wp-admin/admin-ajax.php"

    # return the page title
    def page_title(self):
        return self.get_title().replace("» Hiperdex", "").strip()

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - Hiperdex", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        raw_imgs = self.soup.find_all("img", class_="wp-manga-chapter-img")

        # get all images
        imgs = []
        for i in raw_imgs:
            imgs.append(i["src"].strip())

        return imgs


# Toonily.com scraper
class Toonily(WordpressSites, Magna):
    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # parent class init

        self.source = "Toonily.com"

    # return the page title
    def page_title(self):
        return self.get_title().replace("- Toonily", "").strip()

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - Toonily", "")


# Mangatx.com scraper
class MangaTX(WordpressSites, Magna):
    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # parent class init

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


# PMScans.com scraper, NOT SURE IF 100% WORKING
class PMScans(WordpressSites, Magna):
    def __init__(self, soup, url):
        # parent class init
        WordpressSites.__init__(self, soup)
        Magna.__init__(self, soup, url)
        # parent class init

        self.source = "PMScans.com"

        # required for accessing the chapters of the manga
        self.ajax_url = "https://www.pmscans.com/wp-admin/admin-ajax.php"

    # return the page title
    def page_title(self):
        return self.get_title().replace("– PMScans", "").strip()

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

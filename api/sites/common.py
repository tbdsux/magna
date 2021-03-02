########### THESE SITES HAVE DIFFERENT STRUCTURES AND SETUPS

from api.magna import Magna


class ManhwaManga(Magna):
    """
    ManhwaManga.net scraper
    """

    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "ManhwaManga.net"
        self.base_url = "https://manhwamanga.net"

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text().endswith(
            "Page not found - Manhwa Manga Releases, Read Webtoon Online"
        ):
            return True

        return False

    # return the page title
    def page_title(self):
        return (
            self.get_title()
            .replace(
                "- Manhwa Manga Releases, Read Webtoon Onlin",
                "",
            )
            .strip()
        )

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="desc-text").find("p")
        return __desc.get_text()

    # return the manga image
    def manga_image(self):
        return (
            self.soup.find("div", class_="books")
            .find("div", class_="book")
            .find("img")["src"]
        )

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("ul", class_="list-chapter")
        chapters = []

        for chapter in chapter_container.find_all("li"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = chapter.find("span", class_="chapter-text").get_text()
            i["chapter_url"] = chapter.find("a")["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters.reverse()

    # return the chapter title
    def chapter_title(self):
        return self.get_title()

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="chapter-content")

        # get all of the images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["src"])  # append the source image file

        return imgs


class MangaPark(Magna):
    """
    MangaPark.net scraper
    """

    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "MangaPark.net"
        self.base_url = "https://mangapark.net"

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text().endswith("Browse & Search manga at MangaPark"):
            return True

        return False

    # return the page title
    def page_title(self):
        return (
            self.get_title()
            .replace(
                "- All pages reading type, Fast loading speed, Fast update - MangaPark",
                "",
            )
            .strip()
        )

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="limit-html summary")
        return __desc.get_text()

    # return the manga image
    def manga_image(self):
        return (
            self.soup.find("section", class_="manga")
            .find("div", class_="cover")
            .find("img")["src"]
        )

    # return the manga available chapters
    def extract_chapters(self):
        # get all the chapter containers, . since the manga can contain volumes
        chapter_containers = self.soup.find_all("ul", class_="chapter")
        chapters = []

        for i in chapter_containers:
            for chapter in i.find_all("li"):
                # get the last link
                last_link = chapter.find_all("a")[-1]

                # get the chapter page and title
                i = {}
                i["chapter_name"] = chapter.find(
                    "a"
                ).get_text()  # this is the first link
                i["chapter_url"] = self.base_url + last_link["href"]
                i["b64_hash"] = Magna.encode_base64(
                    href=self.base_url + last_link["href"]
                )  # hash to base64 for url purposes

                # append to list
                chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - MangaPark - Read Online For Free", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        script_containers = [str(i) for i in self.soup.find_all("script")]

        ## get the script where the load_pages is
        main = ""
        for i in script_containers:
            if "_load_pages" in i:
                main = [
                    j.split('"')[0] for j in i.split('":"') if j.startswith("https:")
                ]
                break

        # get all of the images
        imgs = []
        for j in main:
            imgs.append(j.replace("\\", ""))

        return imgs


class MangaNelo(Magna):
    """
    Manganelo.com scraper
    """

    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "Manganelo.com"

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text() == "404 Not Found... - Manganelo":
            return True

        return False

    # return the page title
    def page_title(self):
        return self.get_title().replace("Manga Online Free - Manganelo", "").strip()

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", id="panel-story-info-description")
        return (
            __desc.get_text()
            .replace(__desc.find("h3").get_text(), "")  # remove `Description:` text
            .strip()  # remove unnecessary leading and trailing whitespaces
        )

    # return the manga image
    def manga_image(self):
        return self.soup.find("span", class_="info-image").find("img")["src"]

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("ul", class_="row-content-chapter")
        chapters = []

        for chapter in chapter_container.find_all("li"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = chapter.find("a").get_text()
            i["chapter_url"] = chapter.find("a")["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - Manganelo", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="container-chapter-reader")

        # get all of the images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["src"])  # append the source image file

        return imgs


class Mangakakalot(Magna):
    """
    Mangakakalot.com scraper
    """

    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "Mangakakalot.com"

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text() == "Error":
            return True

        return False

    # return the page title
    def page_title(self):
        return self.get_title().replace("Manga - Mangakakalot.com", "").strip()

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", id="noidungm")
        return (
            __desc.get_text()
            .replace(__desc.find("h2").find("p").get_text(), "")
            .strip()
        )

    # return the manga image
    def manga_image(self):
        return self.soup.find("div", class_="manga-info-pic").find("img")["src"]

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("div", class_="chapter-list")
        chapters = []

        for chapter in chapter_container.find_all("div", class_="row"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = chapter.find("a").get_text()
            i["chapter_url"] = chapter.find("a")["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - Mangakakalot.com", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="container-chapter-reader")

        # get all images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["src"])

        return imgs


class BuluManga(Magna):
    """
    Bulumanga.net scraper
    """

    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "Bulumanga.net"

    # check if the page is error or not
    def validate_error(self):
        if (
            self.soup.title.get_text() == ""
        ):  # there was no title returned if the page was not found on the website
            return True

        return False

    # return the page title
    def page_title(self):
        return (
            self.get_title()
            .replace(" latest update - Bulu Manga", "")
            .replace("Read", "")
            .strip()
        )

    # return the description
    def manga_description(self):
        __desc = self.soup.find("div", class_="comic-description")
        return __desc.find("p").get_text()  # return the paragraph description text

    # return the manga image
    def manga_image(self):
        return self.soup.find("div", class_="comic-info").find("img")["src"]

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("div", class_="chapters-wrapper")
        chapters = []

        for chapter in chapter_container.find_all("div", class_="r1"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = chapter.find("h2", class_="chap").find("a").get_text()
            i["chapter_url"] = chapter.find("h2", class_="chap").find("a")["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" English at Bulumanga.net", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find(
            "center"
        )  # the structure of the website is kind of weird, ..

        # get all of the images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["src"])  # append the source image file

        return imgs


class Manhwa18(Magna):
    """
    Manhwa18.com / Manhwa18.net (both sites are similar, just different domain name) scraper
    """

    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "Manhwa18.net"
        self.initial = "https://manhwa18.net/"  # this is required for compiling page links, since the links in the website didn't include it

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text() == "404 Not Found":
            return True

        return False

    # return the page title
    def page_title(self):
        return (
            self.soup.find("ul", class_="manga-info").find("h1").get_text()
        )  # the manga title cannot be found on the title tag

    # return the description
    def manga_description(self):
        # this will be updated in the future, since some mangas found doesn't have exact description
        __desc = self.soup.find("div", class_="well well-sm").find_all(
            "div", class_="row"
        )[1]

        __rr = __desc.find_all("p")[1]

        return __rr.get_text()

    # return the manga image
    def manga_image(self):
        return (
            self.initial
            + self.soup.find("div", class_="well info-cover").find("img")["src"]
        )

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("div", id="tab-chapper").find("table")
        chapters = []

        for chapter in chapter_container.find_all("tr"):
            # get the chapter page and title
            i = {}
            i["chapter_name"] = chapter.find("a").find("b").get_text()
            i["chapter_url"] = self.initial + chapter.find("a")["href"]
            i["b64_hash"] = Magna.encode_base64(
                href=self.initial + chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        temp = self.soup.find("div", class_="chapter-content-top").find_all("li")[-1]
        return temp.find("a")["title"]

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find_all("img", class_="_lazy chapter-img")

        # get all of the images
        imgs = []
        for i in container:
            imgs.append(i["src"].strip())  # append the source image file

        return imgs
from api.magna import Magna

# Manhwa18.com scraper
class Manhwa18(Magna):
    def __init__(self, soup):
        super().__init__(soup)
        self.source = "Manhwa18.com"
        self.initial = "https://manhwa18.com/"  # this is required for compiling page links, since the links in the website didn't include it

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
                href=chapter.find("a")["href"]
            )  # hash to base64 for url purposes

            # append to list
            chapters.append(i)

        return chapters

    # return the chapter title
    def chapter_title(self):
        return self.soup.find("div", class_="navbar-header").find("a").get_text()

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find_all("img", class_="_lazy chapter-img")

        # get all of the images
        imgs = []
        for i in container:
            imgs.append(i["src"].strip())  # append the source image file

        return imgs

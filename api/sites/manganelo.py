from api.magna import Magna

# Manganelo.com scraper
class MangaNelo(Magna):
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

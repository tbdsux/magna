from api.magna import Magna

# Bulumanga.net scraper
class BuluManga(Magna):
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

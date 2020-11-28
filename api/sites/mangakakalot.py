from api.magna import Magna

# Mangakakalot.com scraper,
class Mangakakalot(Magna):
    def __init__(self, soup):
        super().__init__(soup)
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
        container = self.soup.find("div", id="vungdoc")

        # get all images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["src"])

        return imgs

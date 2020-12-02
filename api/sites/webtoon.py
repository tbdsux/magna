from api.magna import Magna

# Webtoon.xyz scraper,
class WebToon(Magna):
    def __init__(self, soup, url):
        super().__init__(soup, url)
        self.source = "Webtoon.xyz"

    # check if the page is error or not
    def validate_error(self):
        if self.soup.title.get_text() == "Page not found » WEBTOON XYZ":
            return True

        return False

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

    # return the manga image
    def manga_image(self):
        return self.soup.find("div", class_="summary_image").find("img")["data-src"]

    # return the manga available chapters
    def extract_chapters(self):
        # get the chapters
        chapter_container = self.soup.find("ul", class_="main version-chap")
        chapters = []

        for chapter in chapter_container.find_all("li", class_="wp-manga-chapter"):
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

    # return the chapter title
    def chapter_title(self):
        return self.get_title().replace(" - WEBTOON XYZ", "")

    # RETURN THE CHAPTER MANGA IMAGES
    def chapter(self):
        # get the main container
        container = self.soup.find("div", class_="reading-content")

        # get all images
        imgs = []
        for i in container.find_all("img"):
            imgs.append(i["data-src"].strip())

        return imgs

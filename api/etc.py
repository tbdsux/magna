from api.sites.mangakakalot import Mangakakalot
from api.sites.manganelo import MangaNelo
from api.sites.bulumanga import BuluManga


# identifier function
async def grabber(url):
    x = ""

    try:
        if url.startswith("https://manganelo.com/manga/"):
            x = await MangaNelo.initialize(url)
        elif url.startswith("https://mangakakalot.com/manga/"):
            x = await Mangakakalot.initialize(url)
        elif url.startswith("https://ww5.bulumanga.net"):
            x = await BuluManga.initialize(url)

    except Exception:
        pass

    if not x.validate_error():
        # return the main method
        return await x.Extract()

    # if there was a problem during the scraping of the site, return NONE
    return None


# chapter image grabber
async def imiggger(url):
    x = ""

    try:
        if url.startswith("https://manganelo.com/chapter/"):
            x = await MangaNelo.initialize(url)
        elif url.startswith("https://mangakakalot.com/chapter/"):
            x = await Mangakakalot.initialize(url)
        elif url.startswith("https://ww5.bulumanga.net"):
            x = await BuluManga.initialize(url)

    except Exception:
        pass

    if not x.validate_error():
        # return the main method
        return await x.ChapterImages()

    # if there was a problem during the scraping of the site, return NONE
    return None
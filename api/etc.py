from api.sites.mangakakalot import Mangakakalot
from api.sites.manganelo import MangaNelo
from api.sites.bulumanga import BuluManga


# identifier function
async def grabber(url, method):
    x = ""

    try:
        if url.startswith("https://manganelo.com/manga/") or url.startswith(
            "https://manganelo.com/chapter/"
        ):
            x = await MangaNelo.initialize(url)
        elif url.startswith("https://mangakakalot.com/manga/") or url.startswith(
            "https://mangakakalot.com/chapter/"
        ):
            x = await Mangakakalot.initialize(url)
        elif url.startswith("https://ww5.bulumanga.net"):
            x = await BuluManga.initialize(url)

    except Exception:
        return None  # if there was a problem with the scraping, return null

    if not x.validate_error():
        # extract the manga
        if method == "manga":
            return await x.Extract()

        # get the chapter of the manga
        elif method == "chapter":
            return await x.ChapterImages()

    # return None
    return None
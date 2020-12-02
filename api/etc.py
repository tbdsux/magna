from api.sites.mangakakalot import Mangakakalot
from api.sites.manganelo import MangaNelo
from api.sites.bulumanga import BuluManga
from api.sites.manhwa18 import Manhwa18
from api.sites.hiperdex import Hiperdex
from api.sites.webtoon import WebToon
from api.sites.isekaiscan import IsekaiScan


# identifier function
async def grabber(url, method):
    x = ""

    try:
        # manganelo.com website
        if url.startswith("https://manganelo.com/manga/") or url.startswith(
            "https://manganelo.com/chapter/"
        ):
            x = await MangaNelo.initialize(url)

        # mangakakalot.com website
        elif url.startswith("https://mangakakalot.com/manga/") or url.startswith(
            "https://mangakakalot.com/chapter/"
        ):
            x = await Mangakakalot.initialize(url)

        # bulumanga.net website
        elif url.startswith("https://ww5.bulumanga.net"):
            x = await BuluManga.initialize(url)

        # manhwa18.com website
        elif url.startswith("https://manhwa18.com/") or url.startswith(
            "https://manhwa18.net/"
        ):
            x = await Manhwa18.initialize(url)

        # hiperdex.com website
        elif url.startswith("https://hiperdex.com/manga/"):
            x = await Hiperdex.initialize(url)

        # webtoon.xyz website
        elif url.startswith("https://www.webtoon.xyz/read/"):
            x = await WebToon.initialize(url)

        # isekaiscan.com
        elif url.startswith("https://isekaiscan.com/"):
            x = await IsekaiScan.initialize(url)

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
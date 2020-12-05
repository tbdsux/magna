## NEW SITES SHOULD BE CONFIGURED IN HERE

# IMPORT ALL WEBSITE SCRAPER SUBCLASSES
from api.sites.common import MangaNelo, Mangakakalot, BuluManga, Manhwa18

from api.sites.wordpress_build import (
    DarkScans,
    WebToon,
    IsekaiScan,
    Hiperdex,
    Toonily,
    MangaTX,
    PMScans,
)

# "<website-name/title>": {
#     "url": "<website-url>",
#     "class": <classname>,
# }
# -------> FORMAT FOR REGISTERING A SUBCLASS SITE SCRAPPER HANDLER
SITES = {
    "manganelo": {
        "urls": ["https://manganelo.com/manga", "https://manganelo.com/chapter"],
        "class": MangaNelo,
    },
    "mangakakalot": {
        "urls": ["https://mangakakalot.com/manga", "https://mangakakalot.com/chapter"],
        "class": Mangakakalot,
    },
    "bulumanga": {
        "urls": ["https://ww5.bulumanga.net"],
        "class": BuluManga,
    },
    "manhwa18": {
        "urls": ["https://manhwa18.com", "https://manhwa18.net"],
        "class": Manhwa18,
    },
    "hiperdex": {
        "urls": ["https://hiperdex.com/manga"],
        "class": Hiperdex,
    },
    "webtoon": {
        "urls": ["https://www.webtoon.xyz/read"],
        "class": WebToon,
    },
    "isekaiscan": {
        "urls": ["https://isekaiscan.com/manga", "https://isekaiscan.com"],
        "class": IsekaiScan,
    },
    "toonily": {
        "urls": ["https://toonily.com/webtoon", "https://toonily.com"],
        "class": Toonily,
    },
    "dark-scans": {
        "urls": ["https://dark-scans.com/manga", "https://dark-scans.com"],
        "class": DarkScans,
    },
    "mangatx": {
        "urls": ["https://mangatx.com/manga", "https://mangatx.com"],
        "class": MangaTX,
    },
    "pmscans": {
        "urls": ["https://www.pmscans.com/manga", "https://www.pmscans.com"],
        "class": PMScans,
    },
}


# verify if the requested url exists, the main purpose of this is for faster verification
def verifier(url):
    for _, info in SITES.items():
        for i in info["urls"]:
            # if the request starts with any of the registered sites, it will return true and it's class method
            if url.startswith(i):
                return True, info["class"]

    return False, None

## NEW SITES SHOULD BE CONFIGURED IN HERE

# IMPORT ALL WEBSITE SCRAPER SUBCLASSES
from api.sites.common import MangaNelo, Mangakakalot, BuluManga, Manhwa18, MangaPark
from api.sites.wordpress_build import (
    DarkScans,
    WebToon,
    IsekaiScan,
    Hiperdex,
    Toonily,
    MangaTX,
    PMScans,
    ManhwaTOP,
)
from api.sites.special import (
    AsuraScans,
    FlameScans,
    LeviatanScans,
    MethodScans,
    ReaperScans,
    SKScans,
    MerakiScans,
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
    "asurascans": {
        "urls": ["https://asurascans.com/manga", "https://asurascans.com"],
        "class": AsuraScans,
    },
    "leviatanscans": {
        "urls": ["https://leviatanscans.com/comics", "https://leviatanscans.com"],
        "class": LeviatanScans,
    },
    "reaperscans": {
        "urls": ["https://reaperscans.com/comics", "https://reaperscans.com"],
        "class": ReaperScans,
    },
    "skscans": {
        "urls": ["https://skscans.com/comics", "https://skscans.com"],
        "class": SKScans,
    },
    "merakiscans": {
        "urls": ["https://merakiscans.com/manga", "https://merakiscans.com"],
        "class": MerakiScans,
    },
    "manhwatop": {
        "urls": ["https://manhwatop.com/manga", "https://manhwatop.com"],
        "class": ManhwaTOP,
    },
    "mangapark": {
        "urls": ["https://mangapark.net/manga", "https://mangapark.net"],
        "class": MangaPark,
    },
    "methodscans": {
        "urls": ["https://methodscans.com/comics", "https://methodscans.com"],
        "class": MethodScans,
    },
    "flamescans": {
        "urls": ["https://www.flame-scans.com/manga", "https://www.flame-scans.com"],
        "class": FlameScans,
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


# return the SITES
def get_urls():
    us = SITES

    for i in SITES:
        # conver the classnames to string in order 
        # so that it will not return the __init__ method
        us[i]["class"] = str(SITES[i]["class"])

    # return the new dict
    return us
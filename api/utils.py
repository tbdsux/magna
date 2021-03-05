## NEW SITES SHOULD BE CONFIGURED IN HERE

# IMPORT ALL WEBSITE SCRAPER SUBCLASSES
from api.sites.common import (
    MangaNelo,
    Mangakakalot,
    BuluManga,
    Manhwa18,
    MangaPark,
    ManhwaManga,
)
from api.sites.wordpress import (
    AloAlivn,
    DarkScans,
    FirstKissManga,
    Manga68,
    MangaRockTeam,
    ManhuaFast,
    WebToon,
    IsekaiScan,
    Hiperdex,
    Toonily,
    MangaTX,
    PMScans,
    ManhwaTOP,
    S2Manga,
)
from api.sites.special import (
    AsuraScans,
    FlameScans,
    LeviatanScans,
    MethodScans,
    ReaperScans,
    SKScans,
    MerakiScans,
    SecretScans,
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
        "cache_chapter_images": True,
    },
    "mangakakalot": {
        "urls": ["https://mangakakalot.com", "https://mangakakalot.com/chapter"],
        "class": Mangakakalot,
        "cache_chapter_images": True,
    },
    "bulumanga": {
        "urls": [
            "https://ww5.bulumanga.net",
            "https://ww6.bulumanga.net",
            "https://ww4.bulumanga.net",
            "https://ww7.bulumanga.net",
        ],
        "class": BuluManga,
        "cache_chapter_images": True,
    },
    "manhwa18": {
        "urls": ["https://manhwa18.com", "https://manhwa18.net"],
        "class": Manhwa18,
        "cache_chapter_images": True,
    },
    "hiperdex": {
        "urls": ["https://hiperdex.com/manga", "https://hiperdex.com"],
        "class": Hiperdex,
        "cache_chapter_images": True,
    },
    "webtoon": {
        "urls": ["https://www.webtoon.xyz/read"],
        "class": WebToon,
        "cache_chapter_images": True,
    },
    "isekaiscan": {
        "urls": ["https://isekaiscan.com/manga", "https://isekaiscan.com"],
        "class": IsekaiScan,
        "cache_chapter_images": True,
    },
    # "toonily": {
    #     "urls": ["https://toonily.com/webtoon", "https://toonily.com"],
    #     "class": Toonily,
    # },
    # "dark-scans": {
    #     "urls": ["https://dark-scans.com/manga", "https://dark-scans.com"],
    #     "class": DarkScans,
    # },
    "mangatx": {
        "urls": ["https://mangatx.com/manga", "https://mangatx.com"],
        "class": MangaTX,
        "cache_chapter_images": True,
    },
    "pmscans": {
        "urls": ["https://www.pmscans.com/manga", "https://www.pmscans.com"],
        "class": PMScans,
        "cache_chapter_images": True,
    },
    "asurascans": {
        "urls": ["https://asurascans.com/manga", "https://asurascans.com"],
        "class": AsuraScans,
        "cache_chapter_images": True,
    },
    "leviatanscans": {
        "urls": ["https://leviatanscans.com/comics", "https://leviatanscans.com"],
        "class": LeviatanScans,
        "cache_chapter_images": True,
    },
    "reaperscans": {
        "urls": ["https://reaperscans.com/comics", "https://reaperscans.com"],
        "class": ReaperScans,
        "cache_chapter_images": True,
    },
    "skscans": {
        "urls": ["https://skscans.com/comics", "https://skscans.com"],
        "class": SKScans,
        "cache_chapter_images": True,
    },
    "merakiscans": {
        "urls": ["https://merakiscans.com/manga", "https://merakiscans.com"],
        "class": MerakiScans,
        "cache_chapter_images": True,
    },
    "manhwatop": {
        "urls": ["https://manhwatop.com/manga", "https://manhwatop.com"],
        "class": ManhwaTOP,
        "cache_chapter_images": True,
    },
    "mangapark": {
        "urls": ["https://mangapark.net/manga", "https://mangapark.net"],
        "class": MangaPark,
        "cache_chapter_images": False,
    },
    "methodscans": {
        "urls": ["https://methodscans.com/comics", "https://methodscans.com"],
        "class": MethodScans,
        "cache_chapter_images": True,
    },
    "flamescans": {
        "urls": ["https://www.flame-scans.com/manga", "https://www.flame-scans.com"],
        "class": FlameScans,
        "cache_chapter_images": True,
    },
    "aloalivn": {
        "urls": ["https://aloalivn.com/manga", "https://aloalivn.com"],
        "class": AloAlivn,
        "cache_chapter_images": True,
    },
    "manhuafast": {
        "urls": ["https://manhuafast.com/manga", "https://manhuafast.com"],
        "class": ManhuaFast,
        "cache_chapter_images": True,
    },
    # "s2manga": {
    #     "urls": ["https://s2manga.com/manga", "https://s2manga.com"],
    #     "class": S2Manga,
    #     "cache_chapter_images": True,
    # },
    "manga68": {
        "urls": ["https://manga68.com/manga", "https://manga68.com"],
        "class": Manga68,
        "cache_chapter_images": True,
    },
    "manhwamanga": {
        "urls": ["https://manhwamanga.net"],
        "class": ManhwaManga,
        "cache_chapter_images": True,
    },
    "1stkissmanga": {
        "urls": ["https://1stkissmanga.com/manga", "https://1stkissmanga.com"],
        "class": FirstKissManga,
        "cache_chapter_images": True,
    },
    "mangarockteam": {
        "urls": ["https://mangarockteam.com/manga", "https://mangarockteam.com"],
        "class": MangaRockTeam,
        "cache_chapter_images": True,
    },
    "secretscans": {
        "urls": ["https://secretscans.co/comics", "https://secretscans.co"],
        "class": SecretScans,
        "cache_chapter_images": True,
    },
}


# verify if the requested url exists, the main purpose of this is for faster verification
def verifier(url: str):
    for _, info in SITES.items():
        for i in info["urls"]:
            # if the request starts with any of the registered sites, it will return true and it's class method
            if url.startswith(i):
                return True, info["class"], info["cache_chapter_images"]

    return False, None, False


# return the SITES
def get_urls():
    us = SITES

    for i in SITES:
        # conver the classnames to string in order
        # so that it will not return the __init__ method
        us[i]["class"] = str(SITES[i]["class"])

    # return the new dict
    return us


# strips the trailing '/' from urls
# this is for consistency
def strip_slash(request_url: str):
    if request_url.endswith("/"):
        # re-cursive, .. user might add
        # extra slashes to the end of url
        return strip_slash(request_url[: len(request_url) - 1])

    # return request_url
    return request_url
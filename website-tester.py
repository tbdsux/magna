"""
Website tester utility for magna.
"""
import httpx

# API_URL is the online service of the api
#  Update this with your own.
#  [REMOVE TRAILING SLASH]
API_URL = "https://magna-sc.cf"

# set of sample website links to request
#  if the api returns OK
sample_requests = {
    "manganelo": {
        "manga": "https://manganelo.com/manga/pn918005",
        "chapter": "https://manganelo.com/chapter/pn918005/chapter_140",
    },
    "mangakakalot": {
        "manga": "https://mangakakalot.com/read-ce9by158524526578",
        "chapter": "https://mangakakalot.com/chapter/ke922068/chapter_116",
    },
    "bulumanga": {
        "manga": "https://ww6.bulumanga.net/solo-leveling",
        "chapter": "https://ww6.bulumanga.net/solo-leveling-chap-140",
    },
    "manhwa18": {
        "manga": "https://manhwa18.com/manga-that-mans-epilepsy.html",
        "chapter": "https://manhwa18.com/read-sex-exercise-chapter-46.html",
    },
    "hiperdex": {
        "manga": "https://hiperdex.com/manga/black-lagoon-engl/",
        "chapter": "https://hiperdex.com/manga/black-lagoon-engl/chapter-108/",
    },
    "webtoon": {
        "manga": "https://www.webtoon.xyz/read/terror-man/",
        "chapter": "https://www.webtoon.xyz/read/terror-man/chapter-176/",
    },
    "isekaiscan": {
        "manga": "https://isekaiscan.com/manga/drifters/",
        "chapter": "https://isekaiscan.com/manga/drifters/vol-07/ch-081/",
    },
    "toonily": {
        "manga": "https://toonily.com/webtoon/president-is-my-neighbor-cousin/",
        "chapter": "https://toonily.com/webtoon/president-is-my-neighbor-cousin/chapter-41/",
    },
    # "dark-scans": {
    #     "manga": "", "chapter": ""
    # },
    "mangatx": {
        "manga": "https://mangatx.com/manga/i-became-the-ugly-lady/",
        "chapter": "https://mangatx.com/manga/i-became-the-ugly-lady/chapter-21/",
    },
    "pmscans": {
        "manga": "https://www.pmscans.com/manga/shark/",
        "chapter": "https://www.pmscans.com/manga/shark/chapter-21/",
    },
    "asurascans": {
        "manga": "https://asurascans.com/comics/worn-and-torn-newbie/",
        "chapter": "https://asurascans.com/worn-and-torn-newbie-chapter-30/",
    },
    "leviatanscans": {
        "manga": "https://leviatanscans.com/comics/391190-max-level-returner",
        "chapter": "https://leviatanscans.com/comics/391190-max-level-returner/1/57",
    },
    "reaperscans": {
        "manga": "https://reaperscans.com/comics/371413-return-to-player",
        "chapter": "https://reaperscans.com/comics/371413-return-to-player/1/25",
    },
    "skscans": {
        "manga": "https://skscans.com/comics/495288-medical-return",
        "chapter": "https://skscans.com/comics/495288-medical-return/1/100",
    },
    "merakiscans": {
        "manga": "https://merakiscans.com/manga/the-last-human/",
        "chapter": "https://merakiscans.com/manga/the-last-human/300/",
    },
    "manhwatop": {
        "manga": "https://manhwatop.com/manga/the-evil-lady-will-change",
        "chapter": "https://manhwatop.com/manga/the-evil-lady-will-change/chapter-59/",
    },
    "mangapark": {
        "manga": "https://mangapark.net/manga/kaguya-sama-wa-kokurasetai-tensai-tachi-no-renai-zunousen-akasaka-aka",
        "chapter": "https://mangapark.net/manga/kaguya-sama-wa-kokurasetai-tensai-tachi-no-renai-zunousen-akasaka-aka/i2655523/c217/1",
    },
    "methodscans": {
        "manga": "https://methodscans.com/comics/741529-murim-login",
        "chapter": "https://methodscans.com/comics/741529-murim-login/1/58",
    },
    "flamescans": {
        "manga": "https://www.flame-scans.com/manga/mookhyang-dark-lady/",
        "chapter": "https://www.flame-scans.com/mookhyang-chapter-78/",
    },
    "aloalivn": {
        "manga": "https://aloalivn.com/manga/forced-to-become-the-villains-son-in-law/",
        "chapter": "https://aloalivn.com/manga/forced-to-become-the-villains-son-in-law/chapter-66/",
    },
    "manhuafast": {
        "manga": "https://manhuafast.com/manga/your-ancestor-is-online/",
        "chapter": "https://manhuafast.com/manga/your-ancestor-is-online/chapter-19/",
    },
}


def get_manga(website: str) -> bool:
    """
    API Manga website scraper checker.
    """

    check = True

    try:
        httpx.get(f"{API_URL}/manga?q={website}").json()
        # if len(res["chapters"]) < 1:
        #     check = False
    except Exception:
        # there was a problem with the function above
        check = False

    # return the status
    return check


def get_chapter(website: str) -> bool:
    """
    API Manga Chapter website scraper checker.
    """

    check = True

    try:
        httpx.get(f"{API_URL}/manga/chapters?q={website}").json()
        # if len(res["images"]) < 2:
        #     check = False
    except Exception:
        # there was a problem with the function above
        check = False

    # return the status
    return check


def test_website(name: str, samples: dict) -> bool:
    """
    Test if the API's website scraper works with different sample urls and links.
    """
    # check manga query
    manga = get_manga(samples["manga"])
    if manga:
        print(f"{name} =>\n\t\t ====> manga: \033[32m OK \033[00m")
    else:
        print(f"{name} =>\n\t\t ====> manga: \033[31m FAILED \033[00m")

    # check chapter query
    chapter = get_chapter(samples["chapter"])
    if chapter:
        print(f"{name} =>\n\t\t ====> chapter: \033[32m OK \033[00m")
    else:
        print(f"{name} =>\n\t\t ====> chapter: \033[31m FAILED \033[00m")

    if not manga or not chapter:
        return False

    return True


if __name__ == "__main__":
    """
    Run script once called.
    """
    fails = 0

    for i, k in sample_requests.items():
        print(f"\n\033[93mChecking:: {i.upper()}\033[00m\n")
        if not test_website(i, k):
            fails += 1

    # check if there are fails
    if fails > 0:
        raise ValueError("Some website scrapers have failed...")

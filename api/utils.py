## NEW SITES SHOULD BE CONFIGURED IN HERE
MANGA_SITES = [
    "https://manganelo.com/manga/",
    "https://mangakakalot.com/manga/",
    "https://ww5.bulumanga.net",
]
MANGA_SITES_CHAPTERS = [
    "https://manganelo.com/chapter/",
    "https://mangakakalot.com/chapter/",
    "https://ww5.bulumanga.net",
]


# verify if the requested url exists
def verifier(url, type):
    lst = []

    # set the type
    if type == "manga":
        lst = MANGA_SITES
    elif type == "chapter":
        lst = MANGA_SITES_CHAPTERS

    # check if it exists
    for i in lst:
        if url.startswith(i):
            return True

    return False

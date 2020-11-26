from api.sites.manganelo import MangaNelo

# identifier function
async def grabber(url):
    if url.startswith("https://manganelo.com/manga/"):
        x = await MangaNelo.initialize(url)

        return await x.Extract()

    # if there were no equivalent value, return the default
    return "Get the Chapters of the Manga"


# chapter image grbber
async def imiggger(url):
    if url.startswith("https://manganelo.com/chapter/"):
        x = await MangaNelo.initialize(url)

        return await x.ChapterImages()

    # if there were no equivalent value, return the default
    return "Get the Images from the Manga Chapter page"
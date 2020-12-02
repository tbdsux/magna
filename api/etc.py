### MAIN METHOD FUNCTIONS IN HERE

# identifier function
async def grabber(url, class_func, method):
    x = ""

    try:
        x = await class_func.initialize(url)

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
### MAIN METHOD FUNCTION HANDLERS IN HERE

from api.magna import Magna
from datetime import datetime
from typing import Type
from api.cache import Cache

## cacher function
async def cacher(type: str, data: dict, cache_chapter: bool):
    """
    cacher stores the parsed scraped data to the mongodb if defined
    """
    # cache it if it doesn't exist

    secs = 1
    if type == "manga":
        secs = 3600  # scraped manga will expire after 1 hour
    elif type == "chapter":
        secs = 86400  # scraped chapters will expire after 24 hrs / 1 day

    # append cache info to `data`
    if cache_chapter:
        data["cached"] = True
        data["cached_date"] = datetime.utcnow()
        data["cached_expires"] = secs
    else:
        data["cached"] = False

    to_insert = {
        "data": data,
        "request": data["request"],
        "cached_date": datetime.utcnow(),
    }

    # check if cache_chapter is defined in function
    if type == "chapter" and not cache_chapter:
        return data

    # insert to db
    session = await Cache.connect(type)
    insert = await session.insert(to_insert, "cached_date", secs)
    if insert:
        return data


# cache chacker
async def check_cache(request_item: str, type: str):
    """
    check_cache checks the cache if the request_item exists.
    """
    session = await Cache.connect(type)

    # if the data exists from the cache, return it
    data = await session.check(request_item)
    if data:
        return data["data"]

    return False


# identifier function
async def Grabber(
    url: str, class_func: Type[Magna], method: str, cache_chapter: bool = True
):
    """
    Grabber is the main function handler for the api and scraper.
    """
    # return the cache if it exists
    check = await check_cache(request_item=url, type=method)
    if check:
        return check

    # scrape it
    x = await class_func.initialize(url)

    if not x.validate_error():
        data = {}
        # extract the manga
        if method == "manga":
            data = await x.Extract()

        # get the chapter of the manga
        elif method == "chapter":
            data = await x.ChapterImages()

        # cache it
        return await cacher(type=method, data=data, cache_chapter=cache_chapter)

    # return None
    return None
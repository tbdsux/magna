### MAIN METHOD FUNCTION HANDLERS IN HERE

from datetime import datetime
from utils.cache import Cache

## cacher function
async def cacher(type, data):
    session = await Cache.connect(type)

    # cache it if it doesn't exist

    secs = 1
    if type == "manga":
        secs = 3600  # scraped manga will expire after 1 hour
    elif type == "chapter":
        secs = 86400  # scraped chapters will expire after 24 hrs / 1 day

    # append cache info to `data`
    data["cached"] = True
    data["cached_date"] = datetime.utcnow()
    data["cached_expires"] = secs

    to_insert = {
        "data": data,
        "request": data["request"],
        "cached_date": datetime.utcnow(),
    }

    # insert to db
    insert = await session.insert(to_insert, "cached_date", secs)
    if insert:
        return data


# cache chacker
async def check_cache(request_item, type):
    session = await Cache.connect(type)

    # if the data exists from the cache, return it
    data = await session.check(request_item)
    if data:
        return data["data"]

    return False


# identifier function
async def Grabber(url, class_func, method):
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
        ca = await cacher(type=method, data=data)
        if ca:
            return ca

    # return None
    return None
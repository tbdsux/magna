from fastapi import FastAPI, Response, status
from typing import Optional

from api.etc import Grabber
from api.utils import strip_slash, verifier, get_urls

### METADATA TAGS, FOR DOCUMENTATION PURPOSES
METADATA = [
    {"name": "index", "description": "Show API Info."},
    {
        "name": "manga",
        "description": "Scrape available chapters in a specific manga / manhwa from a specic and available website source.",
    },
    {
        "name": "chapter",
        "description": "Grab all the images from the chapter page of the manga / manhwa.",
    },
    {
        "name": "urls",
        "description": "Return the accepted and included websites in the API.",
    },
]
### METADATA TAGS


app = FastAPI(
    title="Magna SCRAPER",
    description="This is a manga, manhwa, manhuwa site scraper and grabber.",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url=None,
    openapi_tags=METADATA,
)


@app.get("/", tags=["index"])
async def index():
    return "MAGNA - Simple Manhwa, Manhua and Manga Scraper and Linker"


# Main Manga, Manhwa, Manhua Chapters Links
@app.get("/manga", tags=["manga"])
async def manga(response: Response, q: Optional[str] = None):
    # q should have a value
    if q:
        check, clsf = verifier(q)

        # continue if request is valid
        if check:
            # strip trailing slash to all urls for them
            # to be common with each request in cache
            url = strip_slash(q)

            resp = await Grabber(url=url, class_func=clsf, method="manga")

            # the Grabber function returns None if there was a problem,
            # but mainly if the scraper handler returns `404` ERROR
            if resp is None:
                # return 404 (not found)
                # if resp == None
                response.status_code = status.HTTP_404_NOT_FOUND
                return {"error": "404", "message": "Your request cannot be found!"}

            # else, return it
            return resp

    # return a 400 (bad request)
    # if q is not set / defined
    response.status_code = status.HTTP_400_BAD_REQUEST
    return "Get the Chapters of the Manga"


# Get the image content on specific chapters
@app.get("/manga/chapters", tags=["chapter"])
async def chapters(response: Response, q: Optional[str] = None):
    # q should have a value
    if q:
        check, clsf = verifier(q)

        # continue if request is valid
        if check:
            # strip trailing slash to all urls for them
            # to be common with each request in cache
            url = strip_slash(q)

            resp = await Grabber(url=url, class_func=clsf, method="chapter")

            # the Grabber function returns None if there was a problem,
            # but mainly if the scraper handler returns `404` ERROR
            if resp is None:
                # return 404 (not found)
                # if resp == None
                response.status_code = status.HTTP_404_NOT_FOUND
                return {"error": "404", "message": "Your request cannot be found!"}

            # else, return it
            return resp

    # return a 400 (bad request)
    # if q is not set / defined
    response.status_code = status.HTTP_400_BAD_REQUEST
    return "Get the Images from the Manga Chapter page"


# Return the accepted and included websites
@app.get("/urls", tags=["urls"])
async def urls():
    return get_urls()
from fastapi import FastAPI
from typing import Optional
from utils.etc import Grabber
from utils.utils import verifier, get_urls

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
async def manga(q: Optional[str] = None):
    # q should have a value
    if q:
        check, res = verifier(q)

        # continue if request is valid
        if check:
            # add trailing slash to all urls for them
            # to be common with each request in cache
            url = q
            if not q.endswith("/"):
                url = q + "/"

            return await Grabber(url=url, class_func=res, method="manga")

    return "Get the Chapters of the Manga"


# Get the image content on specific chapters
@app.get("/manga/chapters", tags=["chapter"])
async def chapters(q: Optional[str] = None):
    # q should have a value
    if q:
        check, res = verifier(q)

        # continue if request is valid
        if check:
            # add trailing slash to all urls for them
            # to be common with each request in cache
            url = q
            if not q.endswith("/"):
                url = q + "/"

            return await Grabber(url=url, class_func=res, method="chapter")

    return "Get the Images from the Manga Chapter page"


# Return the accepted and included websites
@app.get("/urls", tags=["urls"])
async def urls():
    return get_urls()
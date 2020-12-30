# load local .env
from dotenv import load_dotenv

load_dotenv()

import pymongo
import os

DB_NAME = "MagnaScrapes"
CHAPTER_COLLECTIONS = "MagnaChapters"
MANGA_COLLECTIONS = "MagnaManga"


class Cache:
    @classmethod
    async def connect(cls, scrape_type):
        # initialize the mongodb connection
        client = pymongo.MongoClient(os.getenv("MONGO_DB"))

        # set the db and collection
        db = client[DB_NAME]
        collection = None
        if scrape_type == "chapter":
            collection = db[CHAPTER_COLLECTIONS]
        elif scrape_type == "manga":
            collection = db[MANGA_COLLECTIONS]

        # if the scrape_type is different from the default ones, it will return false
        if not collection:
            return False

        # return the collection
        return cls(collection)

    def __init__(self, collection):
        self.collection = collection

    # check if the item was cached in the db
    async def check(self, item):
        res = self.collection.find_one({"request": item})
        if res:
            return res

        return False

    # insert the data to the db
    async def insert(self, data, field, seconds):
        self.collection.insert_one(data)

        try:
            # create ttl index
            self.collection.create_index(f"{field}", expireAfterSeconds=seconds)
        except pymongo.errors.OperationFailure:
            pass

        return True
## [!SERVICE IS CURRENTLY BEING FIXED, HELPS ARE WELCOME :smile:]

# magna
A Serverless MANGA, MANHUWA, MANHWA Scraper API.

**DON'T EXPECT THIS TO BE FAST SINCE IT IS A SCRAPER**

## Update:
- Complex websites or mangas with many chapters will fail to be scraped.
- There is a possiblity that this project will be moved to a full-api with `Heroku` for dev / testing mode.

#### URL:
**https://magna-sc.cf**

#### API Docs:
**https://magna-sc.cf/redoc**

## Currently Added Sites:
NOTE: **YOU SHOULD READ AND SUPPORT THE ORIGINAL SCANLATIONS PROVIDERS!**

- **Manganelo** *(https://manganelo.com)* [OK]
- **Mangakakalot** *(https://mangakakalot.com)* [OK]
- **BuluManga** *(https://ww5.bulumanga.net)* [OK]
- **Manhwa18** *(https://manhwa18.com)* or *(https://manhwa18.net)*  [OK]
- **Hiperdex** *(https://hiperdex.com)* [OK]
- **Webtoon** *(https://www.webtoon.xyz)* [OK]
- **IsekaiScan** *(https://isekaiscan.com)* [OK]
- ~~**Toonily** *(https://toonily.com)* [ERROR] [CLOUDFLARE IS PRESENT]~~
- ~~**DarkScans** *(https://dark-scans.com)* [WEBSITE IS DOWN]~~
- **MangaTX** *(https://mangatx.com)* [OK]
- **PMScans** *(https://www.pmscans.com)* [OK]
- **AsuraScans** *(https://asurascans.com)* [PROBLEM: CHAPTER QUERY]
- **LeviatanScans** *(https://leviatanscans.com)* [PROBLEM: CHAPTER QUERY]
- **ReaperScans** *(https://reaperscans.com)* [PROBLEM: CHAPTER QUERY]
- **SKScans** *(https://skscans.com)* [OK]
- **MerakiScans** *(https://merakiscans.com)* [OK]
- **ManhwaTOP** *(https://manhwatop.com)* [OK]
- **MangaPark** *(https://mangapark.net)* [!NOTE: Chapter Images are expiring returning `Error 410 Gone`, a fix will be committed soon.] [OK]
- **MethodScans** *(https://methodscans.com)* [OK]
- **Flame-Scans** *(https://www.flame-scans.com)* [OK]

## What is being scraped?
**Manga/Manhwa/Manhua**
- Title
- Description
- Image Banner
- Site Chapter Links
- Chapter Title
- Chapter Images - these are the main content being read by a user or a reader

#### Requests:
- **All sites added above are NOT 100% sure to do job done perfectly!**
- Scraped **mangas** are cached for **1 Hour**.
- Scraped **chapters** are cached for **1 Day**.
- Set your `.env` for development
```
MONGO_DB=[your mongo db here]
```

#### Info:
- All requests should have starting urls from any of the sites available above in order for it to work.
- The scrapers might not work 100%, report it if there was a problem.
- If there might be a problem in a scraping one of the websites above, it will be removed.
- *Some sites have compilicated structure so, adding them is kind of complicated and hard.*
- *Also, other sites have the same kind of setup, with just the name of the website as a difference.*

## Development
- Setup first with the Vercel CLI (install with `npm i -g vercel`)
```
vercel dev
```
*It will setup the app in the first run then, it will launch it after.*
- You can also first move the `main.py` to the outside or parent folder then run the app using `uvicorn`
```
uvicorn main:app --reload
```

## Note:
**This service is just made for fun and personal use. It is not meant to be for commercial or business purposes.**
- This is meant to be hosted on a serverless platform (Vercel). You can modify it at your own if you want to host it on your own server.
- **If I will have a server, I might re-configure and rewrite this API for better future updates and addition of websites.**

### All images and data being scraped are credits to the websites above.

### &copy; **TheBoringDude**


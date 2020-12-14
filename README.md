# magna
A Serverless MANGA, MANHUWA, MANHWA Scraper API.

**DON'T EXPECT THIS TO BE FAST SINCE IT IS A SCRAPER**

#### URL:
**https://magna-sc.cf**

#### API Docs:
**https://magna-sc.cf/redoc**

## Currently Added Sites:
NOTE: **YOU SHOULD READ AND SUPPORT THE ORIGINAL SCANLATIONS PROVIDERS!**

- **Manganelo** *(https://manganelo.com)*
- **Mangakakalot** *(https://mangakakalot.com)*
- **BuluManga** *(https://ww5.bulumanga.net)*
- **Manhwa18** *(https://manhwa18.com)* or *(https://manhwa18.net)*
- **Hiperdex** *(https://hiperdex.com)*
- **Webtoon** *(https://www.webtoon.xyz)*
- **IsekaiScan** *(https://isekaiscan.com)*
- **Toonily** *(https://toonily.com)*
- **DarkScans** *(https://dark-scans.com)*
- **MangaTX** *(https://mangatx.com)*
- **PMScans** *(https://www.pmscans.com)*
- **AsuraScans** *(https://asurascans.com)*
- **LeviatanScans** *(https://leviatanscans.com)*
- **ReaperScans** *(https://reaperscans.com)*
- **SKScans** *(https://skscans.com)*
- **MerakiScans** *(https://merakiscans.com)*
- **ManhwaTOP** *(https://manhwatop.com)*
- **MangaPark** *(https://mangapark.net)* [!NOTE: Chapter Images are expiring returning `Error 410 Gone`, a fix will be committed soon.]

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

#### Developed By:
##### :heart: TheBoringDude


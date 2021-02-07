# Dark-Web-Spiders
This repo has Dark Web scrapy spiders. These were actually used to get data.

## What differentiates this from normal scrapers?
In the dark web, CAPTCHAs pose a problem for spiders. This was taken care of by solving CAPTCHAs manually and then feeding the same to the spider.

## How to use these files?
To use these files:
1. Start a new scrapy project.
2. Overwrite the existing settings by referring to settings.py
3. First run the title scraper. For this, verify that the selectors work for your website or write your own selectors. Replace 'sample.website' and put proper cookies.
4. Now using data scraped, do the same for post scaper.

# Dark-Web-Spiders
This repository contains the web-crawlers used to mine dark-web. We had used Scapy to scrape data from the web. Although we have included some scripts that use BeautifulSoup as well,the major part was taken care by Scrapy itself. 

## What differentiates this from normal scrapers?
In the dark web, CAPTCHAs pose a problem for spiders. This was taken care of by solving CAPTCHAs manually and then feeding cookies to the spider.

## How to use these files?
To use these files:
1. Start a new scrapy project.
2. Overwrite the existing settings by referring to settings.py
3. First run the title scraper. For this, verify that the selectors work for your website or write your own selectors. Replace 'sample.website' and put proper cookies.
4. Now using data scraped, do the same for post scaper.


## Comparision of various Scapping frameworks

* **Scrapy** - Scrapy is a web crawling multithread framework with a large number of tools for web crawling. It is built on top Twisted which is an asynchronous networking framework that follows non-blocking I/O calls to servers. Because it is multithreaded and non-blocking, it is actually the best in terms of performance and actually very fast. 
It has been built to consume less memory and use CPU resources minimally. In fact, some benchmarks have stated that Scrapy is 20 times faster than the other tools in scraping. It is portable, and its functionality can be extended.

One advantage of Scrapy is that it comes with modules to send requests as well as to parse responses. The major problem associated with Scrapy is that it is not a beginner-centric tool.

* **BeautifulSoup** - It is an open-source tool and used for web scraping. However, unlike Scrapy, which is a web crawling and scraping framework, BeautifulSoup is not. BeautifulSoup is a module that can be used for pulling data out of HTML and XML documents. BeautifulSoup is a beginner-friendly tool that a newbie can hit the ground running with it. This is because it has very good documentation and a friendly user community. Most web scrapers must have used BeautifulSoup before heading over to Scrapy. The tool is not complex and makes it easier for you to transverse an HTML document and pick the required data.

* **Selenium** - Selenium can send web requests and also comes with a parser. With Selenium, you can pull out data from an HTML document as you do with Javascript DOM API. The major advantage Selenium has is that it loads Javascript and can help you access data behind JavaScript without necessarily going through the pain of sending additional requests yourself. This had made Selenium not only useful to itself but to the other tools. Web scrapers that use either Scrapy or BeautifulSoup make use of Selenium if they require data that can only be available when Javascript files are loaded.

## Scrapped files

The files that we have scrapped have been done in a controlled environment. Do not try to do the same without safety. Also, due to confidentiality, I have not uploaded the complete database file. Contact me at [jash.learn@gmail.com](mailto:jash.learn@gmail.com), for getting the access. The data is available for viewing purpose, press [this](https://drive.google.com/drive/folders/1rOh8ye3Al_ElR2mWTqXsBSnvMQJs0c52?usp=sharing) link for the same.

The drive folder also contains the softcopies of the book [Sion Retzkin - Hands-On Dark Web Analysis Learn wh…es on in the Dark Web, and how to work with it](https://drive.google.com/file/d/1ja0awlsqmHzuxJYFi5knpKH98MBA6CRK/view?usp=sharing) and [Dark Web_ Exploring and Data Mining the Dark Side of the Web](https://drive.google.com/file/d/1CkTUCLpVrSlBKil-hQTm5DxuSFZhkvo8/view?usp=sharing)

There are 4 different databse that we were able to scrap:
  * IronMarch Neo-Nazi Hackforum
  * Nulled.io hackforum
  * Indian Markets on darkweb
  * Agora database

Given below is a snapshot of the Agora database : 

![Agora](https://github.com/Jash-2000/Dark-Web-Spiders/blob/main/Agora.PNG)

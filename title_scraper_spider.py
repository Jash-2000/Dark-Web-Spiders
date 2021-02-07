import scrapy
from scrapy.utils.response import open_in_browser

class PostScraperSpider(scrapy.Spider):
	name = 'post_scraper'
	allowed_domains = ['sample.website']
	start_url = 'sample.website'
	cookies_ = {'keys':'values'}
	
	def start_requests(self):
		print('Entering Start reqs')
		yield scrapy.Request(self.start_url, cookies=self.cookies_)
	'''
	Scrapy shell help:
	req = scrapy.Request(start_url, cookies=cookies_)

	fetch(req)

	view(response)
	'''
	
	def parse(self, response):
		print('Showing response...')
		#open_in_browser(response)
		links_to_post= response.xpath('//*[@class="title "]/@href').extract()
		
		#Correct spaces in the output.
		err_corrected = response.xpath('//*[@class="title "]/text()').extract()
		comments_corr= response.xpath('//a[(contains(text(), "comments"))]/text()').extract()
		var=-1
		for i in range(len(err_corrected)):
			var+=1
			if err_corrected[var]==' ' or err_corrected[var]=='  ':
				err_corrected.pop(var)
				comments_corr.pop(var)
				var-=1

		for i in range(len(links_to_post)):
			title_of_posts = err_corrected[i]
			timestamp = response.xpath('//*[@class="author"]/span[not(contains(@title, "Edited"))]/@title').extract()[i]
			links_to_posts= response.xpath('//*[@class="title "]/@href').extract()[i]
			poster_name= response.xpath('//*[@class="author"]/a[(contains(text(), "/u/"))]/text()').extract()[i]
			forum_name= response.xpath('//*[@class="author"]/a[(contains(text(), "/d/"))]/text()').extract()[i]
			votes= response.xpath('//*[@class="voteCount"]/text()').extract()[i]
			comments= comments_corr[i]
			yield{
				'timestamp': timestamp,
				'title_of_posts': title_of_posts,
				'links_to_posts': links_to_posts,
				'poster_name': poster_name,
				'forum_name': forum_name,
				'votes': votes,
				'Comments':comments		
			}

		next_page_url= response.xpath('//*[@class="pagination"]/a[(contains(text(), "Next"))]/@href').extract()
		if next_page_url[0] is not None:
			print("Next Page URL Not NULL")
			print(next_page_url)
			absolute_next_page_url = response.urljoin(next_page_url[0])
			yield scrapy.Request(absolute_next_page_url, cookies=self.cookies_, callback=self.parse)

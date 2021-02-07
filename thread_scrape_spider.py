import scrapy #for scraping
import csv #for importing URLs from the scraped data.

#import data from csv(which was obtained by using title_scraper.py)
with open('data.csv', newline='') as f:
	reader = csv.reader(f)
	data = list(reader)

#keep URLs, drop rest.
for i in range(len(data)):
	data[i]=data[i][2]

data.pop(0) #remove the entry that has column name

class ThreadScraperSpider(scrapy.Spider):
	#default scrapy variables
	name = 'thread_scraper'
	allowed_domains = ['sample.website']

	number_of_posts=0

	#copied from the browser after solving the CAPTCHA. This is to bypass the CAPTCHA.
	cookies_ = {'keys':'values'}

	#scrape page from every URL in the post data that had been earlier scraped.
	def start_requests(self):
		print('Entering Start reqs. Correct file is.')

		for post_url in data:
			absolute_post_url = 'sample.website' + post_url
			yield scrapy.Request(absolute_post_url, cookies=self.cookies_, callback=self.parse)

	def parse(self, response):
		self.number_of_posts+=1
		comment_data=[]
		#TODO Scrape Post
		
		Post_content=response.xpath('//div[(contains(@class, "postTop"))]/a/text()')
		Post_content+=' : '
		for i in response.xpath('//div[(contains(@class, "postContent"))]/text()').extract():
			Post_content+=i
			Post_content+=' '

		author_name=response.xpath('//div[(contains(@class, "postTop"))]//div[(contains(@class, "author"))]/a[(contains(text(), "/u/"))]/text()')
		votes=response.xpath('//div[(contains(@class, "voteCount"))]/text()')
		timestamp=response.xpath('//div[(contains(@class, "postTop"))]//div[(contains(@class, "author"))]/span/@title')[0].extract()

		#for each comment, search for sub comments.
		root=response.xpath('//*[@class="postComments"]/div[(contains(@class, "comment"))]')
		for j in range(len(root)):
			self.scrape_comment(root[j],str(self.number_of_posts)+'.'+str(j+1),comment_data)
			self.hunt_comments(root[j],str(self.number_of_posts)+'.'+str(j+1),comment_data)

		for element in comment_data:
			yield{
				'timestamp': element['timestamp'],
				'comment_index': element['comment_index'],
				'comment_body': element['comment_body'],
				'poster_name': element['poster_name'],
				'votes': element['votes']
			}
		
		#TODO GOTO NEXT PAGE.

	#recursively look for comments and parse each using 'scrape_comment'
	def hunt_comments(self,comment_html,comment_index,comment_data):
		new_root=comment_html.xpath('./div[(contains(@id, "c-"))]')
		for i in range(len(new_root)):
			self.scrape_comment(new_root[i],comment_index+'.'+str(i+1), comment_data)
			self.hunt_comments(new_root[i],comment_index+'.'+str(i+1),comment_data)

	#parse a single comment
	def scrape_comment(self,comment_html,comment_index,comment_data):
		comment_body=comment_html.xpath('.//div[(contains(@class, "commentBody"))]').extract()[0][25:-6].replace('<br>\r\n',' ')
		poster_name=comment_html.xpath('.//div/a[(contains(@href, "/u/"))]/@href').extract()[0]
		# backup variable timestamp=response.xpath('//*[@class="postComments"]/div/div/div[(contains(@class, "commentContent"))]/div/div[(contains(@class, "timestamp"))]/span/@title').extract()
		timestamp=comment_html.xpath('.//div/div[(contains(@class, "timestamp"))]/span/@title').extract()[0]
		votes=comment_html.xpath('.//div/div[(contains(@class, "votes"))]/text()').extract()[0]
		retdict={
				'timestamp': timestamp,
				'comment_index': comment_index,
				'comment_body': comment_body,
				'poster_name': poster_name,
				'votes': votes,
			}
		comment_data.append(retdict)

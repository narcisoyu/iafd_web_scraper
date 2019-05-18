import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from iafd.items import IafdItem
from scrapy.exceptions import CloseSpider

class IafdSpider(CrawlSpider):
	name = 'iafd'
	#maybe need to change
	item_count = 0
	allowed_domain = ['iafd.com']
	start_urls = ['http://iafd.com/astrology.rme/sign=Aries',
				    'http://iafd.com/astrology.rme/sign=Taurus',
					'http://iafd.com/astrology.rme/sign=Gemini',
					'http://iafd.com/astrology.rme/sign=Cancer',
					'http://iafd.com/astrology.rme/sign=Leo',
					'http://iafd.com/astrology.rme/sign=Virgo',
					'http://iafd.com/astrology.rme/sign=Libra',
					'http://iafd.com/astrology.rme/sign=Scorpio',
					'http://iafd.com/astrology.rme/sign=Sagittarius',
					'http://iafd.com/astrology.rme/sign=Capricorn',
					'http://iafd.com/astrology.rme/sign=Aquarius',
					'http://iafd.com/astrology.rme/sign=Pisces']

	rules = {
		Rule(LinkExtractor(allow =(), restrict_xpaths =('//div[@class="perficon"]')), callback = 'parse_item', follow = False)
				}

	def parse_item(self, response):
		Iafditem_1 = IafdItem()

		#info actors profile
		#Iafditem_1['names'] = response.xpath('/html/body/div[1]/div[1]/div/h1/text()').extract() 
		#Iafditem_1['ethnicity'] = response.xpath('//*[@id="home"]/div/div[1]/p[2]/text()').extract() 
		#Iafditem_1['nationality'] = response.xpath('//*[@id="home"]/div/div[1]/p[4]/text()').extract() 
		#Iafditem_1['hair_colors'] = response.xpath('//*[@id="home"]/div/div[1]/p[6]/text()').extract() 
		#Iafditem_1['height'] = response.xpath('//*[@id="home"]/div/div[2]/p[2]/text()').extract() 
		#Iafditem_1['weight'] = response.xpath('//*[@id="home"]/div/div[2]/p[4]/text()').extract() 
		#Iafditem_1['measurements'] = response.xpath('//*[@id="home"]/div/div[2]/p[6]/text()').extract()
		#Iafditem_1['tattoos'] = response.xpath('//*[@id="home"]/div/div[3]/p[2]/text()').extract() 
		#Iafditem_1['piercings'] = response.xpath('//*[@id="home"]/div/div[3]/p[4]/text()').extract() 
		#Iafditem_1['performer_aka'] = response.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/text()').extract() 
		#Iafditem_1['birthday'] = response.xpath('/html/body/div[1]/div[2]/div[1]/p[4]/a/text()').extract() 
		#Iafditem_1['astrology'] = response.xpath('/html/body/div[1]/div[2]/div[1]/p[6]/a/text()').extract() 
		#Iafditem_1['birthplace'] = response.xpath('/html/body/div[1]/div[2]/div[1]/p[8]/text()').extract() 
		#Iafditem_1['years_active'] = response.xpath('/html/body/div[1]/div[2]/div[1]/p[10]/text()').extract() 

		#info actor's movie
		#HEAD
		names = response.xpath('/html/body/div[1]/div[1]/div/h1')

#		names = response.xpath('//div[@class = "perficon"]//span[@class = "perfname"]')
#>>>>>>> 7256e3180bda17391a612fe24ac52067deb234d2
		for name in names:
			Iafditem_1['names'] = name.xpath('//div[@class = "col-xs-12"]/h1/text()').extract() 
			Iafditem_1['movie_title'] = name.xpath('//*[@id="personal"]/tbody/tr/td[1]/a').extract() 
			Iafditem_1['movie_year'] = name.xpath('//*[@id="personal"]/tbody/tr/td[2]').extract() 
			Iafditem_1['distributor'] = name.xpath('//*[@id="personal"]/tbody/tr/td[3]/a').extract() 
			Iafditem_1['notes'] = name.xpath('//*[@id="personal"]/tbody/tr/td[4]/i').extract()
			Iafditem_1['Formats'] = name.xpath('//*[@id="personal"]/tbody/tr/td[6]/a').extract() 
			#print('*****************************************************')
			#print(Iafditem_1)
			#print(name)
			#print('*****************************************************')
		
		self.item_count += 1
		if self.item_count > 50:
			raise CloseSpider('item_exceeded')
		yield Iafditem_1


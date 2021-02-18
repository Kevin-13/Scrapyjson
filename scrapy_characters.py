import scrapy

class characterScrapy(scrapy.Spider):
    name = "character"
    start_urls = [
        'https://fr.wikipedia.org/wiki/Catégorie:Personnage_d%27animation'
    ]

    def parse(self, response):
        for link in response.css('div#mw-pages div.mw-content-ltr li'): #Dans la div mw-pages il va chercher la div mw-content-ltr et recupéré chaque li
            yield {'character': link.css('a ::text').extract_first()}


import csv
import time
import requests

from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, ChunkedEncodingError

class Scraper():

    def __init__(self):
        """
        Args:
        1) URL: Base url for concatenation.
        2) Years: Starts at 2006 - when PFR first starting tracking QBR.
        3) Categories: Fantasy football relevant only. No individual defensive stats. 
        """
        self.url        = 'https://www.pro-football-reference.com/'
        self.years      = list(range(2006,2019))
        self.categories = ['/passing.htm','/receiving.htm','/rushing.htm','/opp.htm']
    
    def scrape_sites(self):
        #list container for scrape_player_profiles
        href = []
        #iterate through instances
        for year in self.years:
            for cat in self.categories:
                print(str(year)+': '+cat.replace('/','').replace('.htm','').upper())
                url  = self.url+'years/'+str(year)+cat
                res  = requests.get(url)
                html = BeautifulSoup(res.content, 'html.parser')
                if html:
                    container  = html.find('div', {'id': 'content'})
                    if cat == '/passing.htm':
                        table = container.find('tbody')
                        rows  = table.find_all('tr')
                        for row in rows:
                            data = {}
                            for stat in row.find_all('td'):
                                data[stat['data-stat']] = stat.get_text().strip()
                            print(data)

                    else:
                        pass
    
    def scrape_player_profile(self,href):
        pass


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape_sites()
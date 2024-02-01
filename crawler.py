import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import time

def random_headers():
        '''
        Function: Randomize the headers to avoid detected by the websites.
        '''
        user_agent = UserAgent()
        return {'User-Agent': user_agent.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": "https://www.google.com/" 
                }

def crawl(url):
    with requests.Session() as s:
        s.headers = random_headers()
        ## randomly wait a few seconds
        delay = random.randint(1, 30)
        response = s.get(url)
        time.sleep(delay) 
        soup = BeautifulSoup(response.text, 'html5lib')
        
        print(find_question("theknot", soup))

def find_question(website, soup):
     if website == "theknot":
        li = soup.find_all("li", {"dir":"ltr"})
        questions = [i.find("p").text.strip() for i in li]
        return questions
          


if __name__ == "__main__":
    url = "https://www.theknot.com/content/conversation-starters-for-couples"
    crawl(url)
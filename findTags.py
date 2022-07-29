import requests

from bs4 import BeautifulSoup

class WebScraper:
  def __init__(self, ao3_url):
    self.url = ao3_url
    self.response = requests.get(self.url)
    self.html = self.response.text
    self.soup = BeautifulSoup(self.html, 'html.parser')

  def findFandomName(self):
    tags = self.soup.findAll('a', class_='tag')
    return tags
    
  def findNumberOfFic(self, tag):
    parent = tag.find_parent('li')
    parent.a.decompose()
    return parent

  def dataDictionary(self):
    tagList = []
    ficNumList = []
    
    # code
    tags = self.findFandomName();
    for tag in tags:
      tagText = tag.text.strip()
      tagList.append(tagText)
      
      ficNum = self.findNumberOfFic(tag)
      ficNumText = ficNum.text.replace('(', '').replace(')','').strip()

      if(ficNumText == ''):
        ficNumInt = 0
      else: 
        ficNumInt = int(ficNumText)
      ficNumList.append(ficNumInt)
    
    return dict(zip(tagList, ficNumList))

 
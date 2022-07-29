from findTags import *
from convertData import *

urls = [
  'https://archiveofourown.org/media/Anime%20*a*%20Manga/fandoms',
  'https://archiveofourown.org/media/Books%20*a*%20Literature/fandoms',
  'https://archiveofourown.org/media/Cartoons%20*a*%20Comics%20*a*%20Graphic%20Novels/fandoms',
  'https://archiveofourown.org/media/Celebrities%20*a*%20Real%20People/fandoms',
  'https://archiveofourown.org/media/Movies/fandoms',
  'https://archiveofourown.org/media/Music%20*a*%20Bands/fandoms',
  'https://archiveofourown.org/media/Other%20Media/fandoms',
  'https://archiveofourown.org/media/Theater/fandoms',
  'https://archiveofourown.org/media/TV%20Shows/fandoms',
  'https://archiveofourown.org/media/Video%20Games/fandoms',
  'https://archiveofourown.org/media/Uncategorized%20Fandoms/fandoms'
]

fileNames = [
  'ao3_anime',
  'ao3_books',
  'ao3_cartoons_comics',
  'ao3_celebrities',
  'ao3_movies',
  'ao3_music_bands',
  'ao3_other',
  'ao3_theatre',
  'ao3_tvShows',
  'ao3_videoGames',
  'ao3_8ncategorized'
]

for i in range(len(urls)):
  fandom = WebScraper(urls[i])
  fandomData = fandom.dataDictionary()

  dictToJson(fandomData, fileNames[i])




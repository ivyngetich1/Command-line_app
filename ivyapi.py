import urllib.request


url = 'https://holidayapi.com/v1/holidays?key=656a341b-c91a-4ef7-92a8-8ec4f4797296&country=US&year=2015&month=10'
content = urllib.request.urlopen(url)

print (content.read())

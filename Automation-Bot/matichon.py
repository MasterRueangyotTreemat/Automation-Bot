from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as req
from sendline import sendtext

def single():
	url = 'https://www.matichon.co.th/economy'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = Soup(page_html,'html.parser')
	#print(data)

	news = data.findAll('h3',{'class':'entry-title td-module-title'})
	print('COUNT: ',len(news))

	alltext = ''
	all_title = []
	all_link = []

	for i in news:
		title = i.a['title']
		link = i.a['href']

		text = "TITLE: {}\nLINK: {}\n\n".format(title,link)

		alltext = alltext + text
		all_title.append(title)
		all_link.append(link)

	#title = news[-1].a['title']
	#link = news[-1].a['href']
	
	return (alltext,all_title,all_link)

#allnews_economy = single()

#print(allnews_economy[0])

#sendtext(allnews_economy[0])

def multiple(pg):
	url = 'https://www.matichon.co.th/economy/page/' + pg

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = Soup(page_html,'html.parser')
	#print(data)

	news = data.findAll('h3',{'class':'entry-title td-module-title'})
	print('COUNT: ',len(news))

	alltext = ''
	all_title = []
	all_link = []

	for i in news[:10]:
		title = i.a['title']
		link = i.a['href']

		text = "TITLE: {}\nLINK: {}\n\n".format(title,link)

		alltext = alltext + text
		all_title.append(title)
		all_link.append(link)

	#title = news[-1].a['title']
	#link = news[-1].a['href']
	
	return (alltext,all_title,all_link)
'''
for i in range(2,10):
	x = multiple(str(i))
	print(x[0])
'''
#x = multiple('2')
#print(x[0])

'''

todaynews = single()

print(todaynews[2])

sendtext(todaynews[0])

'''
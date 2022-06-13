# step 0 :  import the requirements

from bs4 import BeautifulSoup
import requests
url='https://codewithharry.com'

# step 1 : get the HTML 
r=requests.get(url)
htmlContent=r.content


# step 2 : pass the HTML 
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())


# step 3 : tree traversal of the HTML 

#commonly used types of object 
# 1-Tag 
# title=soup.title
# print(title)
# print(type(title))
# # 2-NavigableString    
# print(title.string)
# print(type(title.string))
# # 3-BeautifulSoup    
# print(type(soup))
# # 3-Comments    
#

#get the title of the HTML page
title=soup.title

# get all the paragraphs from the page 
para=soup.find_all('p')
# print(para)

# get all the anchor tags from the page 
anchors=soup.find_all('a')
# print(anchor)

# get first element in the html page - in this case the first <p/>
firstP=soup.find('p')
# print(firstP)

# get classes of any element in the html page - in this case the first <p/>
firstPClass=soup.find('p')['class']
# print(firstPClass)

#findAll elements with class = lead
leadClass=soup.find_all('p',class_='mt-2')
# print(leadClass)

#get text from the element or soup
textP=soup.find('p').get_text()
# print(type(textP))

#get_text from the whole soup
soupText=soup.get_text()
print(soupText)

# get all the links on the page from anchor tag Element 
for i in anchors:
    link=i.get('href')
    print(link)

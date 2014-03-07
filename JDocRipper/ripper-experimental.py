

from bs4 import BeautifulSoup
import requests


#url = raw_input("Enter a website to extract the URL's from: ")
r = requests.get('http://www.cs.iastate.edu/~cs227/assignments/mini1/doc/mini1/TV.html')#'http://www.cs.iastate.edu/~cs227/assignments/mini3/doc/mini3/DNAStrand.html')

#http://www.cs.iastate.edu/~cs227/assignments/mini1/doc/mini1/TV.html')#

data = r.text
soup = BeautifulSoup(data)

sectionwrapper = soup.find('ul',{'class':'blockList'})
sections       = soup.findAll('li',{'class':'blockList'})

print sections.__len__()

print sections[0].text

if sections[0].text.split()[0] == 'Fields':
    #If there are some instance variables
    instances    = sections[0]
    constructors = sections[1]
    methods      = sections[2]
else:
    #If not, proceed as usual
    instances    = None
    constructors = sections[0]
    methods      = sections[1]

#Prints the package and class name
# print 'package '+soup.find('div',{'class':'subTitle'}).text+';\n'
# print 'public class'+soup.find('h2',{'class':'title'}).text[5:]+' {'





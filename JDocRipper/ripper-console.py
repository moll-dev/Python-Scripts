

from bs4 import BeautifulSoup
import requests

#url = raw_input("Enter a website to extract the URL's from: ")
#r = requests.get('http://www.cs.iastate.edu/~cs227/assignments/mini1/doc/mini1/TV.html')
r = requests.get('http://www.cs.iastate.edu/~cs227/assignments/mini3/doc/mini3/DNAStrand.html')

data = r.text
soup = BeautifulSoup(data)

sections = soup.findAll('table',{'class':'overviewSummary'})

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
print 'package '+soup.find('div',{'class':'subTitle'}).text+';\n'

classname = soup.find('h2',{'class':'title'}).text[5:]

print 'public class'+classname+' {'

#Prints the instance variables if any
if instances is not None:
    #Go ahead and do yo thang
    instances = iter(instances.findAll('tr'))
    next(instances)

    for instance in instances:
        first = True
        var  = ""
        line = ""
        for cols in instance.findAll('code'):
            line = (" ".join(cols.text.split()))
            if first:
                line = line.replace('java.lang.String','String')
                var += '\tpublic ' + line + ' '
                first = False
            else:
                line = line.replace('java.lang.String','String')
                var += line + '\t\t\t\n'

    print var #To file eventually
    #print "<<<>>>>>"

#Find the constructor summary and scrape that constructor
constructor = constructors.findAll('code')[0].text.replace('java.lang.String','String')
print '\tpublic '+constructor+'\t\t\t//TODO'
print '\t{\n\n\t}\n'

#Skip the first "method" which is the title of the table
methods = iter(methods.findAll('tr'))
next(methods)

for method in methods:
    first = True
    code  = ""
    line  = ""
    for cols in method.findAll('code')[0:2]:
        line = (" ".join(cols.text.split()))
        if first:
            line = line.replace('java.lang.String','String')
            code += '\tpublic ' + line + ' '
            first = False
        else:
            line = line.replace('java.lang.String','String')
            code += line + '\t\t\t//TODO'

    print code #To file eventually
    print '\t{\n\n\t}\n'

print '}'



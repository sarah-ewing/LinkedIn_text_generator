import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

os.chdir('D:\\linkedin\\description')
final = pd.DataFrame()

column = ['job_title', 'individual_url', 'end_date', 'date_posted', 
           'description', 'employmentType', 'experienceRequirements',
          'hiringOrganization','hiringOrganization', 'addressLocality',
          'addressRegion', 'postalCode','addressCountry']

print("now for the loop.")

final = pd.DataFrame()

column = ['job_title', 'individual_url', 'end_date', 'date_posted', 
           'description', 'employmentType', 'experienceRequirements',
          'hiringOrganization','hiringOrganization', 'addressLocality',
          'addressRegion', 'postalCode','addressCountry']


for ii in range(1110, 10001):
    
    if ii % 10 == 0:
        print(ii)

    i = ii * 25
    
    if i >= 50000:
        print("done!")
        break
        
    i = str(i)
    
    time.sleep(2)
    URL = 'https://www.linkedin.com/jobs/search/?keywords=data%20scientist&location=United%20States&start='
    page = requests.get(URL+i)

    soup = BeautifulSoup(page.content, 'html.parser')

    job_elems = soup.find_all(class_='result-card__full-card-link')

    count=0
    for job_elem in job_elems:
        count +=1
        
        new_url = job_elem.find('span', class_='screen-reader-text')
        result21 = str(job_elem).find('</span></a></a>')
    #     print("\n job_title:",str(new_url)[33:(result21-6)])

        result12 = str(job_elem).find('href=')
        result22 = str(job_elem).find('"><span class="')
    #     print("\n individual_url:", str(job_elem)[(result12+6):result22])

        Single_url = str(job_elem)[(result12+6):result22]
        page11 = requests.get(Single_url)
        soup_look = BeautifulSoup(page11.content, 'html.parser').prettify()

        soup_look = str(soup_look)
        
        result13 = str(soup_look).find('{"@context":')
        result23 = str(soup_look).find('","validThrough":"')
        long_desc = str(soup_look)[(result13+12):(result23)]
        long_desc = long_desc.replace(u'\\u003C/li\\u003E\\u003Cli\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003E\\u003Cul\\u003E\\u003Cli\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003Cbr\\u003E\\u003C/li\\u003E\\u003C/ul\\u003E\\u003Cem\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003Cbr\\u003E\\u003C/u\\u003E\\u003C/strong', " ")
        long_desc = long_desc.replace(u'\\u003Cbr\\u003E\\u003Cbr\\u003E\\u003Cstrong\\u003E\\u003Cu\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003Cbr\\u003E\\u003Cbr\\u003E\\u003C/li\\u003E\\u003C/ul\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003Cli\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003C/li\\u003E', " ")
        long_desc = long_desc.replace('\\u003C/li\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003Cbr\\u003E\\u003Cbr\\u003E', " ")
        long_desc = long_desc.replace(u'\\u003C', "")
        long_desc = long_desc.replace(u'\\u003E', "")
        long_desc = long_desc.replace(u'/li', "")
        long_desc = long_desc.replace(u'/pp&nbsp;', " ")
        long_desc = long_desc.replace(u'&nbsp;', " ")
        long_desc = long_desc.replace(u'/pp', " ")
        long_desc = long_desc.replace(u'/u/p', " ")
        long_desc = long_desc.replace(u'gobr/ul10%strong', "")
        long_desc = long_desc.replace(u'/strongstrong', "")
        long_desc = long_desc.replace(u'/ul/ulstrongu', "")
        long_desc = long_desc.replace(u'br/strongulli', "")
        long_desc = long_desc.replace(u'/u/strongu', "")
        long_desc = long_desc.replace(u'/ulstrongu', "")
        long_desc = long_desc.replace(u'br/strongli', "")
        long_desc = long_desc.replace(u'br/ulstrong', "")
        long_desc = long_desc.replace(u'/strongul', "")
        long_desc = long_desc.replace(u'listrong', "")
        long_desc = long_desc.replace(u'/strong', "")
        long_desc = long_desc.replace(u'strongu', "")
        long_desc = long_desc.replace(u'brstrong', "")
        long_desc = long_desc.replace(u' li ', "")
        long_desc = long_desc.replace(u'  ', " ")
        

        result14 = str(soup_look).find(',"validThrough":"')
    #     print("\n end_date:", str(soup_look)[(result14+17):(result14+41)])

        result15 = str(long_desc).find('","datePosted":"')
        result25 = str(long_desc).find('","description":')
    #     print("\n date_posted:", long_desc[(result15+16):result25])

        result26 = str(long_desc).find('","employmentType"')
    #     print("\n description:", long_desc[(result25+17):result26])

        result17 = str(long_desc).find('","employmentType"')
        result27 = str(long_desc).find('","experienceRequirements"')
    #     print("\n employmentType:", long_desc[(result17+20):result27])

        result18 = str(long_desc).find('","experienceRequirements":"')
        result28 = str(long_desc).find('","hiringOrganization"')
#         print("\n experienceRequirements:", long_desc[(result18+28):result28])

        result19 = str(long_desc).find('"hiringOrganization":{"@type":"Organization","name":"')
        result29 = str(long_desc).find('","sameAs":')
    #     print("\n hiringOrganization:", long_desc[(result19+53):result29])

        result110 = str(long_desc).find(',"industry":"')
        result210 = str(long_desc).find('","jobLocation":{"')
    #     print("\n hiringOrganization:", long_desc[(result110+13):result210])

        result111 = str(long_desc).find('"addressLocality":"')
        result211 = str(long_desc).find('","addressRegion":')
    #     print("\n addressLocality:", long_desc[(result111+19):result211])

        result112 = str(long_desc).find(',"addressRegion":')
        result212 = str(long_desc).find(',"postalCode":')
        addressRegion = long_desc[(result112+17):result212]
        addressRegion = addressRegion.replace('"', "")
        if len(addressRegion) >=3:
            addressRegion = None
    #     print("\n addressRegion:", long_desc[(result112+17):result212])

        result113 = str(long_desc).find('"postalCode":"')
        result213 = str(long_desc).find('","addressCountry":"')
    #     print("\n postalCode:", long_desc[(result113+14):result213])

        result114 = str(long_desc).find('","addressCountry":"')
        result214 = str(long_desc).find('"}},"')
    #     print("\n addressCountry:", long_desc[(result114+20):result214])
        filename = 'job_'+str(ii)+'_'+str(count)+'.txt'
        data = [[str(new_url)[33:(result21-6)], ## 'job_title',   
                str(job_elem)[(result12+6):result22], ## 'individual_url',
                str(soup_look)[(result14+17):(result14+41)], ## 'end_date',
                long_desc[(result15+16):result25], ## 'date_posted', 
                filename,
                long_desc[(result17+20):result27],
                long_desc[(result18+28):result28],
                long_desc[(result19+53):result29],
                long_desc[(result110+13):result210],
                long_desc[(result111+19):result211],
                addressRegion,
                long_desc[(result113+14):result213],
                long_desc[(result114+20):result214]]]
        description = [[ long_desc[(result25+17):result26] ]]
#         df = pd.DataFrame(data, columns = column)
        os.chdir('D:\\linkedin\\description')
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(description)+'\n')## 'description'

        os.chdir('D:\\linkedin')
        
        with open('meta_data.csv', "a+", encoding="utf-8") as f:
            f.write(str(data)+'\n')## 'description'
#iterate over these wiki webpages: https://en.m.wikipedia.org/wiki/List_of_municipalities_in_XYZ

#section that the table exists in....
#class: mf-section-1 collapsible-block collapsible-block-js open-block id: content-collapsible-block-0
#wikitable sortable jquery-tablesorter (class of table when name is first column...)
#go to tbody and iterate over rows... tr -> td -> get value of a and cut any of the cross stuff...

#class: class="mf-section-1 collapsible-block collapsible-block-js open-block" id 
#table class: class="wikitable sortable static-row-numbers jquery-tablesorter"
#wikitable sortable static-row-numbers jquery-tablesorter (class of table when municipality is second column, first column is ID)
#tr -> td -> a -> get value of <b>
from bs4 import BeautifulSoup
import json
import requests

WIKI_LINK_NORMAL = "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_"
WIKI_LINK_DC = "https://en.m.wikipedia.org/wiki/Neighborhoods_in_"

f = open('states_full.json')
f2 = open('alphabet.json')

states_data = json.load(f)
alphabet_data = json.load(f2)

for i in states_data['states']:
    print("state is: " + i)
    if i == "Washington,_D.C.":
        r = requests.get(WIKI_LINK_DC + i)
        soup = BeautifulSoup(r.content, 'html.parser')
        #section = soup.find("section", class_="mf-section-1")
        #table = section.table
        #table_body = table.tbody
        #table_row = table_body.tr
        #table_header = table_row.th
        #name = table_header.a
        #print(name)
        table_i_want = soup.find("table", class_="wikitable")
        #print(table_i_want)
        for name in table_i_want.tbody.contents:
            if name.a is None:
                print("no")
            else:
                print(name.a)
        '''for letter in alphabet_data['alphabet']:
            one_row = soup.find("tr", {"id": letter})
            if one_row is None:
                print("nothing found")
            else:
                if (one_row.contents[1].a) is None:
                    print("nothing found")
                else:
                    print(one_row.contents[1].a.contents)'''
    else:
        r = requests.get(WIKI_LINK_NORMAL + i)
        soup = BeautifulSoup(r.content, 'html.parser')
        #section = soup.find("section", class_="mf-section-1")
        #table = section.table
        #table_body = table.tbody
        #table_row = table_body.tr
        #table_header = table_row.th
        #name = table_header.a
        #print(name)
        table_i_want = soup.find("table", class_="wikitable")
        #print(table_i_want)
        for name in table_i_want.tbody.contents:
            if name.a is None:
                print("no")
            else:
                print(name.a)
        '''for letter in alphabet_data['alphabet']:
            one_row = soup.find("tr", {"id": letter})
            if one_row is None:
                print("nothing found")
            else:
                if (one_row.contents[1].a) is None:
                    print("nothing found")
                else:
                    print(one_row.contents[1].a.contents)'''

f.close()
f2.close()

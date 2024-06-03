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

#starting with Alabama
#find other states that follow the same setup?
#california - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_California
print("---ALABAMA---")
r = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Alabama")
soup = BeautifulSoup(r.content, 'html.parser')
cities_table_rows = soup.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
for row in cities_table_rows:
    city_name = row.find("th").find("a")
    if city_name is not None:
        print(city_name.text)
print("------")

#doing this for Iowa bc formatted differently
#Colorado - 
print("---IOWA---")
r2 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_in_Iowa")
soup2 = BeautifulSoup(r2.content, 'html.parser')
cities_table_rows_2 = soup2.find("section", class_="mf-section-2").find_all("table")[1].find("tbody").find_all("tr")
for row in cities_table_rows_2:
    city_name = row.find("th").find("a")
    if city_name is not None:
        print(city_name.text)
print("------")

#doing this for Maine bc formatted differently
print("---MAINE---")
r3 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Maine")
soup3 = BeautifulSoup(r3.content, 'html.parser')
cities_table_rows_3 = soup3.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_3:
    table_data = row.find_all("td")
    #first row does not have any td elements - need to skip that one
    #has to be a better way to check this lol
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a").find("b")
        if city_name is not None:
            print(city_name.text)
print("------")

#doing this for Nebraska bc formatted differently
#alaska
#hawaii - https://en.m.wikipedia.org/wiki/List_of_places_in_Hawaii
print("---NEBRASKA---")
r4 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Nebraska")
soup4 = BeautifulSoup(r4.content, 'html.parser')
cities_table_rows_4 = soup4.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_4:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...
    if not table_data:
        print("empty")
    else:
        city_name = table_data[1].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

#indiana - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Indiana
print("---ARIZONA---")
r5 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Arizona")
soup5 = BeautifulSoup(r5.content, 'html.parser')
cities_table_rows_5 = soup5.find("section", class_="mf-section-2").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_5:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

#kentucky - https://en.m.wikipedia.org/wiki/List_of_cities_in_Kentucky
print("---ARKANSAS---")
r6 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Arkansas")
soup6 = BeautifulSoup(r6.content, 'html.parser')
cities_table_rows_6 = soup6.find("section", class_="mf-section-2").find_all("table")[1].find("tbody").find_all("tr")
for row in cities_table_rows_6:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

#CT
#georgia - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Georgia_(U.S._state)
#louisiana - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Louisiana
#maryland - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Maryland
print("---CONNECTICUT---")
r7 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Connecticut")
soup7 = BeautifulSoup(r7.content, 'html.parser')
cities_table_rows_7 = soup7.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_7:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

#delaware
#florida -https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Florida
#illinois - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Illinois
print("---DELAWARE---")
r8 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Delaware")
soup8 = BeautifulSoup(r8.content, 'html.parser')
cities_table_rows_8 = soup8.find("section", class_="mf-section-1").find_all("table")[1].find("tbody").find_all("tr")
for row in cities_table_rows_8:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

print("---IDAHO---")
r9 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_in_Idaho")
soup9 = BeautifulSoup(r9.content, 'html.parser')
cities_table_rows_9 = soup9.find("section", class_="mf-section-0").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_9:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...        
    if not table_data:
        print("empty")
    else:
        city_name = table_data[1].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

print("---KANSAS---")
r10 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_in_Kansas")
soup10 = BeautifulSoup(r10.content, 'html.parser')
cities_table_rows_10 = soup10.find("section", class_="mf-section-2").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_10:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...        
    if not table_data:
        print("empty")
    else:
        city_name = table_data[1].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")


'''for i in states_data['states']:
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
        for letter in alphabet_data['alphabet']:
            one_row = soup.find("tr", {"id": letter})
            if one_row is None:
                print("nothing found")
            else:
                if (one_row.contents[1].a) is None:
                    print("nothing found")
                else:
                    print(one_row.contents[1].a.contents)
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
        for letter in alphabet_data['alphabet']:
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

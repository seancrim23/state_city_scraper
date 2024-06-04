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
state_link_arr = [
    ["AL", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Alabama"],
    ["CA", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_California"]
]
for state_link in state_link_arr:
    print(state_link[0])
    r = requests.get(state_link[1])
    soup = BeautifulSoup(r.content, 'html.parser')
    cities_table_rows = soup.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
    for row in cities_table_rows:
        city_name = row.find("th").find("a")
        if city_name is not None:
            print(city_name.text)
    print("------")

#doing this for Iowa bc formatted differently
#Colorado - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Colorado
state_link_arr_2 = [
    ["CO", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Colorado"],
    ["IA", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Iowa"]
]
for state_link in state_link_arr_2:
    print(state_link[0])
    r2 = requests.get(state_link[1])
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
#alaska - https://en.m.wikipedia.org/wiki/List_of_cities_in_Alaska
#hawaii - https://en.m.wikipedia.org/wiki/List_of_places_in_Hawaii
#minnesota - https://en.m.wikipedia.org/wiki/List_of_cities_in_Minnesota
#missouri - https://en.m.wikipedia.org/wiki/List_of_cities_in_Missouri
#north dakota - https://en.m.wikipedia.org/wiki/List_of_cities_in_North_Dakota
#oklahoma - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Oklahoma
#pennsylvnia - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Pennsylvania (figure out how to fix the names...)
#south dakota - https://en.m.wikipedia.org/wiki/List_of_cities_in_South_Dakota
#texas - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Texas
#wyoming - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Wyoming
state_link_arr_4 = [
    ["NE", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Nebraska"],
    ["AK", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Alaska"],
    ["HI", "https://en.m.wikipedia.org/wiki/List_of_places_in_Hawaii"],
    ["MN", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Minnesota"],
    ["MO", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Missouri"],
    ["ND", "https://en.m.wikipedia.org/wiki/List_of_cities_in_North_Dakota"],
    ["OK", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Oklahoma"],
    ["PA", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Pennsylvania"],
    ["SD", "https://en.m.wikipedia.org/wiki/List_of_cities_in_South_Dakota"],
    ["TX", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Texas"],
    ["WY", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Wyoming"],
]
for state_link in state_link_arr_4:
    print(state_link[0])
    r4 = requests.get(state_link[1])
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
#ohio - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Ohio
#tennessee - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Tennessee
state_link_arr_5 = [
    ["IN", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Indiana"],
    ["OH", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Ohio"],
    ["TN", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Tennessee"],
    ["AZ", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Arizona"],
]
for state_link in state_link_arr_5:
    print(state_link[0])
    r5 = requests.get(state_link[1])
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
#michigan - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Michigan
#mississippi - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Mississippi
#montana - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Montana
#nevada - https://en.m.wikipedia.org/wiki/List_of_cities_in_Nevada
#new jersey - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey
#new mexico - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_Mexico
#north carolina - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_North_Carolina
#rhode island - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Rhode_Island
#south carolina - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_South_Carolina
#utah - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Utah
#washington - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Washington
#wisconsin - https://en.m.wikipedia.org/wiki/List_of_cities_in_Wisconsin
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

#west virginia - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_West_Virginia
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

print("---MASSACHUSETTS---")
r11 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Massachusetts")
soup11 = BeautifulSoup(r11.content, 'html.parser')
cities_table_rows_11 = soup11.find("section", class_="mf-section-2").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_11:
    table_data = row.find_all("td")
    if not table_data:
        print("empty")
    else:
        city_name_td = table_data[0]
        #some of these data points are a link inside of a bold tag and vice versa
        bold_tag = city_name_td.find("b")
        #does it have a link inside? if no, print normal if yes, print link value
        city_link_tag = bold_tag.find("a")
        if city_link_tag is None:
            print(bold_tag.text)
        else:
            print(city_link_tag.text)
print("------")

#vermont - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Vermont
print("---NEW HAMPSHIRE---")
r12 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_Hampshire")
soup12 = BeautifulSoup(r12.content, 'html.parser')
cities_table_rows_12 = soup12.find("section", class_="mf-section-2").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_12:
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

print("---NEW YORK---")
r13 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_York")
soup13 = BeautifulSoup(r13.content, 'html.parser')
cities_table_rows_13 = soup13.find("section", class_="mf-section-0").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_13:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...        
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

print("---OREGON---")
r14 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_in_Oregon")
soup14 = BeautifulSoup(r14.content, 'html.parser')
cities_table_rows_14 = soup14.find("section", class_="mf-section-1").find("div").find("table").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_14:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...        
    if not table_data:
        print("empty")
    else:
        city_name = table_data[1].find("a")
        if city_name is not None:
            print(city_name.text)
print("------")

print("---VIRGINIA---")
r16 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_and_counties_in_Virginia")
soup16 = BeautifulSoup(r16.content, 'html.parser')
cities_table_rows_16 = soup16.find("section", class_="mf-section-3").find("table").find("tbody").find_all("tr")
for row in cities_table_rows_16:
    city_name = row.find("th").find("a")
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

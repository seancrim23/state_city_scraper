from bs4 import BeautifulSoup
import json
import requests

#need to remove the cross things from the city / town names
def format_city_name(city_name):
    if "††" in city_name:
        print(city_name)
        split_city_name = city_name.split()
        split_city_name.remove("††")
        return ' '.join(split_city_name)
    if "†" in city_name:
        print(city_name)
        split_city_name = city_name.split()
        split_city_name.remove("†")
        return ' '.join(split_city_name)
    return city_name

WIKI_LINK_NORMAL = "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_"
WIKI_LINK_DC = "https://en.m.wikipedia.org/wiki/Neighborhoods_in_"

f = open('states_full.json')
f2 = open('alphabet.json')

states_data = json.load(f)
alphabet_data = json.load(f2)

state_city_map = {}

#starting with Alabama
#find other states that follow the same setup?
state_link_arr = [
    ["AL", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Alabama"]
]
for state_link in state_link_arr:
    print(state_link[0])
    r = requests.get(state_link[1])
    soup = BeautifulSoup(r.content, 'html.parser')
    cities_table_rows = soup.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
    city_list = []
    for row in cities_table_rows:
        city_name = row.find("th").find("a")
        if city_name is not None:
            if format_city_name(city_name.text) not in city_list:
                city_list.append(format_city_name(city_name.text))
            #print(city_name.text)
    state_city_map[state_link[0]] = city_list
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
    index = 0
    city_list = []
    for row in cities_table_rows_2:
        #i dont like this but also find tbody should not return anything in thead imo
        if index > 1:
            table_head = row.find("th")
            if table_head is not None:
                city_name = table_head.find("a")
                if city_name is not None:
                    if format_city_name(city_name.text) not in city_list:
                        city_list.append(format_city_name(city_name.text))
                    #print(city_name.text)
        index+=1
    state_city_map[state_link[0]] = city_list
    print("------")

#doing this for Maine bc formatted differently
print("---MAINE---")
r3 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Maine")
soup3 = BeautifulSoup(r3.content, 'html.parser')
cities_table_rows_3 = soup3.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
city_list = []
for row in cities_table_rows_3:
    table_data = row.find_all("td")
    #first row does not have any td elements - need to skip that one
    #has to be a better way to check this lol
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a").find("b")
        if city_name is not None:
            if format_city_name(city_name.text) not in city_list:
                city_list.append(format_city_name(city_name.text))
            #print(city_name.text)
state_city_map["ME"] = city_list
print("------")

#doing this for Nebraska bc formatted differently
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
    city_list = []
    for row in cities_table_rows_4:
        table_data = row.find_all("td")
        #another situation where i should just skip over the first row...
        if not table_data:
            print("empty")
        else:
            city_name = table_data[1].find("a")
            if city_name is not None:
                if format_city_name(city_name.text) not in city_list:
                    city_list.append(format_city_name(city_name.text))
                #print(city_name.text)
    state_city_map[state_link[0]] = city_list
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
    city_list = []
    for row in cities_table_rows_5:
        table_data = row.find_all("td")
        #another situation where i should just skip over the first row...
        if not table_data:
            print("empty")
        else:
            city_name = table_data[0].find("a")
            if city_name is not None:
                if format_city_name(city_name.text) not in city_list:
                    city_list.append(format_city_name(city_name.text))
                #print(city_name.text)
    state_city_map[state_link[0]] = city_list
    print("------")

#kentucky - https://en.m.wikipedia.org/wiki/List_of_cities_in_Kentucky
state_link_arr_6 = [
    ["KY", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Kentucky"],
    ["AR", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Arkansas"]
]
for state_link in state_link_arr_6:
    print(state_link[0])
    r6 = requests.get(state_link[1])
    soup6 = BeautifulSoup(r6.content, 'html.parser')
    cities_table_rows_6 = soup6.find("section", class_="mf-section-2").find_all("table")[1].find("tbody").find_all("tr")
    city_list = []
    for row in cities_table_rows_6:
        table_data = row.find_all("td")
        #another situation where i should just skip over the first row...
        if not table_data:
            print("empty")
        else:
            city_name = table_data[0].find("a")
            if city_name is not None:
                if format_city_name(city_name.text) not in city_list:
                    city_list.append(format_city_name(city_name.text))
                #print(city_name.text)
    state_city_map[state_link[0]] = city_list
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
#alaska - https://en.m.wikipedia.org/wiki/List_of_cities_in_Alaska
state_link_arr_7 = [
    ["CT", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Connecticut"],
    ["GA", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Georgia_(U.S._state)"],
    ["LA", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Louisiana"],
    ["MD", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Maryland"],
    ["MI", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Michigan"],
    ["MS", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Mississippi"],
    ["MT", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Montana"],
    ["NV", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Nevada"],
    ["NJ", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey"],
    ["NM", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_Mexico"],
    ["NC", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_North_Carolina"],
    ["RI", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Rhode_Island"],
    ["SC", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_South_Carolina"],
    ["UT", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Utah"],
    ["WA", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Washington"],
    ["WI", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Wisconsin"],
    ["AK", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Alaska"]
]
for state_link in state_link_arr_7:
    print(state_link[0])
    r7 = requests.get(state_link[1])
    soup7 = BeautifulSoup(r7.content, 'html.parser')
    cities_table_rows_7 = soup7.find("section", class_="mf-section-1").find("table").find("tbody").find_all("tr")
    city_list = []
    for row in cities_table_rows_7:
        table_data = row.find_all("td")
        #another situation where i should just skip over the first row...
        if not table_data:
            print("empty")
        else:
            city_name = table_data[0].find("a")
            if city_name is not None:
                if format_city_name(city_name.text) not in city_list:
                    city_list.append(format_city_name(city_name.text))
                #print(city_name.text)
    state_city_map[state_link[0]] = city_list
    print("------")

#delaware
#florida -https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Florida
#illinois - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Illinois
state_link_arr_8 = [
    ["DE", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Delaware"],
    ["FL", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Florida"],
    ["IL", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Illinois"]
]
for state_link in state_link_arr_8:
    print(state_link[0])
    r8 = requests.get(state_link[1])
    soup8 = BeautifulSoup(r8.content, 'html.parser')
    cities_table_rows_8 = soup8.find("section", class_="mf-section-1").find_all("table")[1].find("tbody").find_all("tr")
    city_list = []
    for row in cities_table_rows_8:
        table_data = row.find_all("td")
        #another situation where i should just skip over the first row...
        if not table_data:
            print("empty")
        else:
            city_name = table_data[0].find("a")
            if city_name is not None:
                if format_city_name(city_name.text) not in city_list:
                    city_list.append(format_city_name(city_name.text))
                #print(city_name.text)
    state_city_map[state_link[0]] = city_list
    print("------")

print("---IDAHO---")
r9 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_in_Idaho")
soup9 = BeautifulSoup(r9.content, 'html.parser')
cities_table_rows_9 = soup9.find("section", class_="mf-section-0").find("table").find("tbody").find_all("tr")
city_list = []
for row in cities_table_rows_9:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...        
    if not table_data:
        print("empty")
    else:
        city_name = table_data[1].find("a")
        if city_name is not None:
            if format_city_name(city_name.text) not in city_list:
                city_list.append(format_city_name(city_name.text))
            #print(city_name.text)
state_city_map["ID"] = city_list
print("------")

#west virginia - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_West_Virginia
state_link_arr_10 = [
    ["WV", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_West_Virginia"],
    ["KS", "https://en.m.wikipedia.org/wiki/List_of_cities_in_Kansas"]
]
for state_link in state_link_arr_10:
    print(state_link[0])
    r10 = requests.get(state_link[1])
    soup10 = BeautifulSoup(r10.content, 'html.parser')
    cities_table_rows_10 = soup10.find("section", class_="mf-section-2").find("table").find("tbody").find_all("tr")
    city_list = []
    for row in cities_table_rows_10:
        table_data = row.find_all("td")
        #another situation where i should just skip over the first row...        
        if not table_data:
            print("empty")
        else:
            city_name = table_data[1].find("a")
            if city_name is not None:
                if format_city_name(city_name.text) not in city_list:
                    city_list.append(format_city_name(city_name.text))
                #print(city_name.text)
    state_city_map[state_link[0]] = city_list
    print("------")

print("---MASSACHUSETTS---")
r11 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Massachusetts")
soup11 = BeautifulSoup(r11.content, 'html.parser')
cities_table_rows_11 = soup11.find("section", class_="mf-section-2").find("table").find("tbody").find_all("tr")
city_list = []
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
            if format_city_name(bold_tag.text) not in city_list:
                city_list.append(format_city_name(bold_tag.text))
            #print(bold_tag.text)
        else:
            if format_city_name(city_link_tag.text) not in city_list:
                city_list.append(format_city_name(city_link_tag.text))
            #print(city_link_tag.text)
state_city_map["MA"] = city_list
print("------")

#vermont - https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Vermont
state_link_arr_12 = [
    ["VT", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_Vermont"],
    ["NH", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_Hampshire"]
]
for state_link in state_link_arr_12:
    print(state_link[0])
    r12 = requests.get(state_link[1])
    soup12 = BeautifulSoup(r12.content, 'html.parser')
    cities_table_rows_12 = soup12.find("section", class_="mf-section-2").find("table").find("tbody").find_all("tr")
    city_list = []
    for row in cities_table_rows_12:
        table_data = row.find_all("td")
        #first row does not have any td elements - need to skip that one
        #has to be a better way to check this lol
        if not table_data:
            print("empty")
        else:
            city_name = table_data[0].find("a").find("b")
            if city_name is not None:
                if format_city_name(city_name.text) not in city_list:
                    city_list.append(format_city_name(city_name.text))
                #print(city_name.text)
    state_city_map[state_link[0]] = city_list
    print("------")

print("---NEW YORK---")
r13 = requests.get("https://en.m.wikipedia.org/wiki/List_of_municipalities_in_New_York")
soup13 = BeautifulSoup(r13.content, 'html.parser')
cities_table_rows_13 = soup13.find("section", class_="mf-section-0").find("table").find("tbody").find_all("tr")
city_list = []
for row in cities_table_rows_13:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...        
    if not table_data:
        print("empty")
    else:
        city_name = table_data[0].find("a")
        if city_name is not None:
            if format_city_name(city_name.text) not in city_list:
                city_list.append(format_city_name(city_name.text))
            #print(city_name.text)
state_city_map["NY"] = city_list
print("------")

print("---OREGON---")
r14 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_in_Oregon")
soup14 = BeautifulSoup(r14.content, 'html.parser')
cities_table_rows_14 = soup14.find("section", class_="mf-section-1").find("div").find("table").find("table").find("tbody").find_all("tr")
city_list = []
for row in cities_table_rows_14:
    table_data = row.find_all("td")
    #another situation where i should just skip over the first row...        
    if not table_data:
        print("empty")
    else:
        city_name = table_data[1].find("a")
        if city_name is not None:
            if format_city_name(city_name.text) not in city_list:
                city_list.append(format_city_name(city_name.text))
            #print(city_name.text)
state_city_map["OR"] = city_list
print("------")

print("---VIRGINIA---")
r16 = requests.get("https://en.m.wikipedia.org/wiki/List_of_cities_and_counties_in_Virginia")
soup16 = BeautifulSoup(r16.content, 'html.parser')
cities_table_rows_16 = soup16.find("section", class_="mf-section-3").find("table").find("tbody").find_all("tr")
city_list = []
for row in cities_table_rows_16:
    city_name = row.find("th").find("a")
    if city_name is not None:
        if format_city_name(city_name.text) not in city_list:
            city_list.append(format_city_name(city_name.text))
        #print(city_name.text)
state_city_map["VA"] = city_list
print("------")


state_link_arr_17 = [
    ["CA", "https://en.m.wikipedia.org/wiki/List_of_municipalities_in_California"]
]
for state_link in state_link_arr_17:
    print(state_link[0])
    r17 = requests.get(state_link[1])
    soup17 = BeautifulSoup(r17.content, 'html.parser')
    cities_table_rows_17 = soup17.find("section", class_="mf-section-1").find_all("table")[1].find("tbody").find_all("tr")
    city_list = []
    for row in cities_table_rows_17:
        city_name = row.find("th").find("a")
        if city_name is not None:
            if format_city_name(city_name.text) not in city_list:
                city_list.append(format_city_name(city_name.text))
            #print(city_name.text)
    state_city_map[state_link[0]] = city_list
    print("------")

#DC
print("DC")
r18 = requests.get("https://en.m.wikipedia.org/wiki/Neighborhoods_in_Washington,_D.C.")
soup18 = BeautifulSoup(r18.content, 'html.parser')
cities_table_rows_18 = soup18.find("section", class_="mf-section-1").find_all("ul")
city_list = []
for row in cities_table_rows_18:
    list_elements = row.find_all("li")
    for list_element in list_elements:
        nbhd_name = list_element.find("a")
        if nbhd_name is not None:
            if format_city_name(nbhd_name.text) not in city_list:
                city_list.append(format_city_name(nbhd_name.text))
            #print(nbhd_name.text)
state_city_map["DC"] = city_list
print("--------------")


#print("---HOPEFULLY THIS LOOKS GOOD---")
#print(state_city_map)
#print("------")
print("state mapping size: ", len(state_city_map))

with open('state_city_mapping.json', 'w') as fp:
    json.dump(state_city_map, fp)

fp.close()
f.close()
f2.close()

import requests
from bs4 import BeautifulSoup as bs

bend_wind_url = 'http://www.usairnet.com/cgi-bin/Winds/Aloft.cgi?location=RDM&Submit=Get+Forecast&hour=12&course=azimuth'
wind_response = requests.get(bend_wind_url, headers={'user-agent':'Mozilla/5.0'})
soup = bs(wind_response.text, "html.parser")

tables = soup.findAll("table")
table = tables[8]
all_contents = table.contents[7].contents
filtered = all_contents[1::2]

print('Redmond OR Winds Aloft')
print("Altitude (ft), Wind Direction, Speed, Temperature, Wind Chill")
strings=[]
for foo in filtered[:-1]:
    text = foo.text.replace('\n',' ')
    strings.append(text)
    print(text)

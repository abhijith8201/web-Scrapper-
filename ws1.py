import csv
from email.policy import strict
import requests
from bs4 import BeautifulSoup

url_t20i = 'https://www.icc-cricket.com/rankings/mens/team-rankings/t20i'        # variable for url
#url_odi = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
#url_test = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'

r_t20i = requests.get(url_t20i)
soup = BeautifulSoup(r_t20i.text, 'html.parser')

rank_table = soup.find('table', class_='table')    # variable for table

file = open('t201.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Position', 'Team', 'Points'])

for team in rank_table.find_all('tbody'):
    init_rw = team.find_all('tr', class_='rankings-block__banner')           # rank one in sepearate class
    for rw in init_rw:
        team1_name = rw.find('span', class_='u-hide-phablet').text.strip()
        team1_rank = rw.find('td' , class_='rankings-block__banner--pos').text.strip()
        team1_points = rw.find('td', class_='rankings-block__banner--points').text.strip()
        print(team1_name,team1_rank,team1_points)
        writer.writerow([team1_rank, team1_name, team1_points])


    rows = team.find_all('tr', class_='table-body')
   
    for row in rows:

        cric_team = row.find('span', class_='u-hide-phablet').text.strip()
        cric_rank = row.find('td', class_='table-body__cell table-body__cell--position u-text-right').text.strip()
        cric_points = row.find_all('td', class_='table-body__cell u-center-text')[1].text.strip()
        print(cric_team, cric_rank,cric_points)
        writer.writerow([cric_rank, cric_team, cric_points])
    
file.close()


      

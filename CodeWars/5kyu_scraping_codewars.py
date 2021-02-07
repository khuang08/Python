from bs4 import BeautifulSoup
import requests

URL = 'https://www.codewars.com/users/leaderboard'

response = requests.get(URL)

data = response.content

def solution():
	soup = BeautifulSoup(data, 'html.parser')
	for link in soup.find_all('a'):
		print(link.get('href'))

leaderboard = solution()
print(leaderboard)

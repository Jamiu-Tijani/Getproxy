#importing required libraries
from bs4 import BeautifulSoup
import requests
print("Getting ip From Source ....")
try :
	url = "https://free-proxy-list.net/"
	dat = requests.get(url)
except Exception as e:
	print(e)
soup = BeautifulSoup(dat.text, 'html.parser')
tbody = soup.find_all("tbody")
ip = []
port = []
time = []
print("Parsing collected ips")
i = 0
while i < len(tbody[0].find_all("tr")):
    w = []
    for child in tbody[0].find_all("tr")[i].children:
        w.append(str(child).split('td')[1].split('<')[0].split('>')[1])
    ip.append(w[0])
    port.append(w[1])
    time.append(w[7])
    w.clear()
    i = i + 1
print("collected {} ips".format(len(ip)))
print("collected {} ports".format(len(port)))
print("Directory should be in this format : /home/user/someotherfolder")
Dir = input("Input directory to store data")

try:
	ips = open('{}/ip.txt'.format(Dir), 'w')
	ports = open('{}/ports.txt'.format(Dir), 'w')
except Exception as e:
	print(e)

w = 0
while w < len(ip):
     ips.write('{}\n'.format(ip[w]))
     ports.write('{}\n'.format(port[w]))
     w = w + 1 

ips.close()
ports.close()
open(Dir+'ip.txt','a')
print(ips.closed)
print(ports.closed)
print("Done")


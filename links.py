#usr/bin/python3

from bs4 import BeautifulSoup
import requests
import argparse
import time

logo = '''
                 ########################################
                 ------- Devloper by Yousef -----------
                         twitter : y0usef_11
                 ########################################
'''

print (logo)

def get_arags():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url' , dest ='url',help = 'url website ')
    options = parser.parse_args()

    if not options.url:
        parser.error('[-] Please Enter url website , use --help for more')

    return options.url

html_page = requests.get(get_arags(),verify=False).text

file = open("urls.txt","w")

soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    file.write(format(link.get('href')+"\n"))
    time.sleep(0.2)
    print(link.get('href'))
print("[+] Urls all saved file urls.txt")

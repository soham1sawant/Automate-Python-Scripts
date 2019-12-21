# download_comics_from_xkcd_com.py

# This program downloads all the comics from xkcd.com or downloads any new comics uploaded to the site

import bs4 , requests

def downloadAll(firstUrl , lastUrl):
    firstUrl = firstUrl.split('/')

    res = requests.get(lastUrl)        # downloads the page
    res.raise_for_status()              # checks if th epage has been dowloaded successfully

    soup = bs4.BeautifulSoup(res.text , 'html.parser')      # parser only the HTML of the page
    elems = str( soup.select('#middleContainer') ).split(' ')
    elems = elems[9].split('/')
    elems = elems[1]

    



def downloadNew(pageUrl):           # this function will download any new comics added to xkcd.com
    print(pageUrl)

print("Download comics from xkcd.com ")
print()

ans = input("Do you want to download all comics or new ones only ? (A/N) : ").strip().upper()

if ans == 'A':
    downloadAll('https://xkcd.com/1/' , 'https://xkcd.com')
elif ans == 'N':
    downloadAll('https://xkcd.com')


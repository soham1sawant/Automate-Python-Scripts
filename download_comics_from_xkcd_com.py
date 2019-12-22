# download_comics_from_xkcd_com.py

# This program downloads all the comics from xkcd.com or downloads any new comics uploaded to the site

import bs4 , requests

def downloadImages(start , end , firstUrl):
    savePath = input("Enter the path of folder to save images : ")

    for i in range( int(start) , end + 1 ):
        link = firstUrl[0] + '//' + firstUrl[2] + '/' + str(i) + '/'        # creates link page of each commic in site from start to finish
        res1 = requests.get(link)
        res1.raise_for_status()

        soup = bs4.BeautifulSoup(res1.text , 'html.parser')             # parses only the html content of the filr 'res1'
        Comicelem = soup.select("#comic > img")

        if Comicelem == []:
            print("Could not find Comic Image !!!")
        else:
            comicUrl = Comicelem[0].get('src').split('//')      # gets the URL of the image
            comicUrl = comicUrl[1]                          # gets the URL of the image
            comicUrl = 'https://' + comicUrl
            
            print("Downloading Image %s..." %(comicUrl))
            Img = requests.get(comicUrl)                # downloads the comic image
            Img.raise_for_status()

            # Save the File to User Entered Path
            imageFile = open(savePath + '/' + str(i) , 'wb')      # opens path to save the image file
            for chunk in Img.iter_content(100000):              # saves the image file in chunks
                imageFile.write(chunk)
            imageFile.close()                       # closes the image file

        dataFile = open(savePath + '/' + 'data' , 'w')
        dataFile.write(str(i))                                 # writes the number of the last number of the comic file
        
    print("Download Complete !!!")
    print()


def downloadAll(firstUrl , lastUrl):
    firstUrl = firstUrl.split('/')

    res = requests.get(lastUrl)        # downloads the page
    res.raise_for_status()              # checks if the page has been dowloaded successfully

    soup = bs4.BeautifulSoup(res.text , 'html.parser')      # parser only the HTML of the page
    end = str( soup.select('#middleContainer') ).split(' ')
    end = end[9].split('/')
    end = int(end[1])

    downloadImages(firstUrl[3] , end , firstUrl)
    

def downloadNew(firstUrl , lastUrl):           # this function will download any new comics added to xkcd.com
    firstUrl = firstUrl.split('/')

    res = requests.get(lastUrl)        # downloads the page
    res.raise_for_status()              # checks if the page has been dowloaded successfully

    soup = bs4.BeautifulSoup(res.text , 'html.parser')      # parser only the HTML of the page
    end = str( soup.select('#middleContainer') ).split(' ')
    end = end[9].split('/')
    end = int(end[1])

    dataPath = input("Enter the path of folder to save images : ")
    start = dataPath.read().strip()

    downloadImages(start , end , firstUrl)


print("Download comics from xkcd.com ")
print()

ans = input("Do you want to download all comics or new ones only ? (A/N) : ").strip().upper()

if ans == 'A':
    downloadAll('https://xkcd.com/1/' , 'https://xkcd.com')
elif ans == 'N':
    downloadAll('https://xkcd.com/1/' , 'https://xkcd.com')


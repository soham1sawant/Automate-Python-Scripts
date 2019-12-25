# download_google_images.py

# Program to download the 10 images on the topic specified by the user from google

# TODO : Take the path of the folder to save the images to from the user

# TODO : Download the images

# TODO : Inform the user that the images have finished downloading

import bs4 , requests , os
from selenium import webdriver

def download(topic , save):
    browser = webdriver.Firefox()
    browser.get('http://google.com')
    textBox = browser.find_element_by_css_selector('html body#gsr.hp.vasq.big div#viewport.ctr-p div#searchform.jhp.big form#tsf.tsf.nj div div.A8SBwf div.RNNXgb div.SDkEP div.a4bIc input.gLFyf.gsfi')
    textBox.send_keys(topic)
    textBox.submit()                        #Search the web for the images
    

print("Program to download images from google")
print()

topic = input("Enter the topic for downloading the images : ")      # Takes the topic from the topic
savePath = input("Enter the path of the folder to save the downloaded images : ")

if os.path.exists(savePath):
    def download(topic , savePath)
else:
    print("The path doe not exists !")
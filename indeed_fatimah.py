import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

cols = ['job_title','company','location','type','date','link', 'job_description']

titles=[]
companies=[]
locations=[]
types=[]
dates=[]
links=[]
descriptions=[]
# reviews=[]
# salaries=[]

#Fetch URLs
url = "https://eg.indeed.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81?q=data%20analyst&l=Cairo&start=50&vjk=0991a4e0e8bbfd88"
result = requests.get(url)
source= result.content
soup= BeautifulSoup(source, "html.parser")

#Fetch data markups
title = soup.find_all("h2", {"class":"jobTitle css-1h4a4n5 eu4oa1w0"})
# print(title)
company = soup.find_all("span", {"class":"companyName"})
# print(company)
location = soup.find_all("div", {"class":"companyLocation"})
# print(location)
type = soup.find_all("div", {"class":"attribute_snippet"})
# print(type)
date = soup.find_all("span", {"class":"date"})
# print(date)



for i in range(len(title)):
    titles.append(title[i].find("a").text)
    links.append("https://eg.indeed.com"+title[i].find("a", href=True)["href"])
    # print(title[i], "\n", "_____________________")
# print(links, "\n\n")

# Specify driver path
path = Service(r'/home/tima/selenium-firefox/drivers/geckodriver')
driver = webdriver.Firefox(service= path)

# driver.get(url)
# #Handle pop-ups
# close_popup = driver.find_element_by_id("popover-close-link")
# close_popup.click()
 

#Start navigating
for link in links:
    driver.get(link)
    driver.implicitly_wait(3)
    result = requests.get(link)
    source= result.content
    soup= BeautifulSoup(source, "html.parser")
    descriptions.append(soup.find("div", {"class":"jobsearch-jobDescriptionText"}).text)
# print(descriptions)
driver.quit()
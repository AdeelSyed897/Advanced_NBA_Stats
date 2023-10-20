import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import math
import random

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")


driver = webdriver.Chrome(options=options)

url = 'https://www.statmuse.com/nba'

driver.get(url)


print('\n')
name = input('What Player: ')
print('\n\n')

driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/textarea').send_keys(name+" 2023 regular season games stats") 
driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/input').click()
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

nums = soup.find_all("tr")

counter=0
ratingList = []

for num in nums:
    if counter==25:
        break
    row_content = num.find_all("td")
    if len(row_content)==0:
        continue
    pts = float(row_content[7].text.strip())
    reb = float(row_content[8].text.strip())
    ast = float(row_content[9].text.strip())
    stl = float(row_content[10].text.strip())
    blk = float(row_content[11].text.strip())
    tov = float(row_content[12].text.strip())
    fgMakes = float(row_content[13].text.strip())
    fga = float(row_content[14].text.strip())
    fgm = float(fga-fgMakes)
    ftMakes = float(row_content[19].text.strip())
    fta = float(row_content[20].text.strip())
    ftm = float(fta-ftMakes)
    rating = pts+reb+ast+stl+blk-fgm-ftm-tov
    ratingList.append(rating)
    counter+=1

post = input('Did the player play in the post season? (True/False) ')

if post:
    driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/a').click()
    driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/textarea').send_keys(name+" 2023 post season games stats") 
    driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/input').click()
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    nums = soup.find_all("tr")
    count = len(nums)-1
    for num in nums:
        row_content = num.find_all("td")
        if len(row_content)==0:
            continue
        pts = float(row_content[7].text.strip())
        reb = float(row_content[8].text.strip())
        ast = float(row_content[9].text.strip())
        stl = float(row_content[10].text.strip())
        blk = float(row_content[11].text.strip())
        tov = float(row_content[12].text.strip())
        fgMakes = float(row_content[13].text.strip())
        fga = float(row_content[14].text.strip())
        fgm = float(fga-fgMakes)
        ftMakes = float(row_content[19].text.strip())
        fta = float(row_content[20].text.strip())
        ftm = float(fta-ftMakes)
        rating = pts+reb+ast+stl+blk-fgm-ftm-tov
        ratingList.append(rating)

print(ratingList)



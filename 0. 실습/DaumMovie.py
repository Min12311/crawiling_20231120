import pandas as pd
import requests as req
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

def get_reviews() :
    res = req.get(url)
    movie_code = '149761585'
    count_url = f"https://comment.daum.net/apis/v1/comments/on/{movie_code}/flags"
    count_res = req.get(count_url)
    count_json = json.loads(count_res.text)
    print(f'1- count_json : {count_json}')


#driver_path = '/Driver/chromedriver.exe'
#driver = webdriver.Chrome(executable_path=driver_path)

try:
    url = "https://comment.daum.net/apis/v1/posts/149761585/comments?parentId=0&offset=0&limit=10&sort=LATEST&isInitial=true&hasNext=true"

    aa = get_reviews()
    print(f"{aa}")

#    driver.get(url)

#    for _ in range(1000):
#        soup = BeautifulSoup(driver.page_source, 'html.parser')

except Exception as e:
    print(f"{e}")

#finally:
    #driver.quit()

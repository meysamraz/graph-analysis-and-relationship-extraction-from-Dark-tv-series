"""
    @thour : Meysam Raz
"""


from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import pandas as pd
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="CHROME_PATH",options=options)
driver.maximize_window()
urls=[]
details_list = []

driver.get('https://dark-netflix.fandom.com/wiki/Dark_Wiki')

time.sleep(2)
print('Start scraping')
while True:
    for a in driver.find_elements_by_xpath('/html/body/div[4]/div[3]/div[2]/main/div[3]/div/div/div[1]/div/div[5]/div/div/div[2]/div/a'):
        url = a.get_attribute('href')
        url_dict = {"url":url}
        urls.append(url_dict)
        df_urls = pd.DataFrame(urls)
    print("Available Restaurants: ",len(df_urls))

    print('Start getting Bios')


    for url in df_urls['url'].to_list():
            driver.get(url)
            title = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div/aside/h2').text
            biography = [bio.text for bio in driver.find_elements_by_xpath('/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div/p')]
            new_title = title.replace("/", " ")

            filetitle =new_title+".text"
            with open(filetitle, "w", encoding='utf-8') as file:
                for bio in biography:
                    file.write(bio)
            file.close()
            time.sleep(2)
            
            

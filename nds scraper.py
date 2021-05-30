# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 23:14:03 2021

@author: Anne
"""
import time
import pandas as pd
import csv
import numpy as np
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException
from selenium.webdriver.common.by import By
import re
import os
from random import uniform



driver = webdriver.Chrome("C:\\Users\\Paul\\Documents\\NBA GOAT\\chromedriver.exe")

teamids = []

options = []
driver.get('https://draftscout.com/college.php?DSTeamId=122&DraftYear=2020&sortorder=TSXPos&order=ASC')
el = driver.find_element_by_xpath('//*[@id="School"]/select')
for option in el.find_elements_by_tag_name('option'):
    options.append(option.get_attribute("value"))
start = 'college.php?DSTeamId='
end = '&DraftYear=2020&sortorder=TSXPos&order=ASC'
for value in options[1:]:
    if value.endswith('&DraftYear=2020&sortorder=TSXPos&order=ASC'):
        value = int(value[21:-42])
        teamids.append(value)
print(teamids)
        
teamids = sorted(teamids)
print(teamids)        
        
   
for year in range(2022,2025):
    for team in teamids:
        print(team)
        try:
            driver.get('https://draftscout.com/college.php?DSTeamId=' + str(team) + '&DraftYear=' + str(year) + '&sortby=TSXPos&order=ASC&startspot=0')
            time.sleep(1.5)
            for player in range(1,16):
                try:
                    ds_rank = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[1]').text
                except NoSuchElementException:
                    continue
                try:
                    player_name = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[2]').text
                except NoSuchElementException:
                    continue
                try:
                    position = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[3]').text
                except NoSuchElementException:
                    continue
                try:
                    projected = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[4]').text
                except NoSuchElementException:
                    continue
                try:
                    height = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[5]').text
                except NoSuchElementException:
                    continue
                try:
                    weight = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[6]').text
                except NoSuchElementException:
                    continue
                try:
                    forty_time_range = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[7]').text
                except NoSuchElementException:
                    continue
                try:
                    hometown = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[8]').text
                except NoSuchElementException:
                    continue
                try:
                    high_school = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[9]').text
                except NoSuchElementException:
                    continue
                try:
                    college = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[1]/tbody/tr/td/div[1]/font/strong').text
                except NoSuchElementException:
                    continue
                try:
                    player_url = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[2]/a').get_attribute('href')
                except NoSuchElementException:
                    continue
                data = ds_rank + '~' + player_name + '~' + position + '~' + projected + '~' + height + '~' + weight + '~' + forty_time_range + '~' + hometown + '~' + high_school + '~' + college + '~' + player_url + '~' + str(team)
                print(data, file=open('nds_team_data_may2021.csv','a',encoding='UTF-8'))
                if player == 15:
                    driver.get('https://draftscout.com/college.php?DSTeamId=' + str(team) + '&DraftYear=' + str(year) + '&sortby=TSXPos&order=ASC&startspot=15')
                    for player2 in range(1,16):
                        try:
                            ds_rank = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[1]').text
                        except NoSuchElementException:
                            continue
                        try:
                            player_name = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[2]').text
                        except NoSuchElementException:
                            continue
                        try:
                            position = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[3]').text
                        except NoSuchElementException:
                            continue
                        try:
                            projected = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[4]').text
                        except NoSuchElementException:
                            continue
                        try:
                            height = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[5]').text
                        except NoSuchElementException:
                            continue
                        try:
                            weight = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[6]').text
                        except NoSuchElementException:
                            continue
                        try:
                            forty_time_range = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[7]').text
                        except NoSuchElementException:
                            continue
                        try:
                            hometown = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[8]').text
                        except NoSuchElementException:
                            continue
                        try:
                            high_school = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[9]').text
                        except NoSuchElementException:
                            continue
                        
                        try:
                            college = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[1]/tbody/tr/td/div[1]/font/strong').text
                        except NoSuchElementException:
                            continue
                        try:
                            player_url = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[2]/a').get_attribute('href')
                        except NoSuchElementException:
                            continue
                        data = ds_rank + '~' + player_name + '~' + position + '~' + projected + '~' + height + '~' + weight + '~' + forty_time_range + '~' + hometown + '~' + high_school + '~' + college + '~' + player_url + '~' + str(team)
    
                        print(data, file=open('nds_team_data_may2021.csv','a',encoding='UTF-8'))
        except:
            driver.get('https://draftscout.com/college.php?DSTeamId=' + str(team) + '&DraftYear=' + str(year) + '&sortby=TSXPos&order=ASC&startspot=0')
            time.sleep(1.5)
            for player in range(1,16):
                try:
                    ds_rank = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[1]').text
                except NoSuchElementException:
                    continue
                try:
                    player_name = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[2]').text
                except NoSuchElementException:
                    continue
                try:
                    position = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[3]').text
                except NoSuchElementException:
                    continue
                try:
                    projected = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[4]').text
                except NoSuchElementException:
                    continue
                try:
                    height = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[5]').text
                except NoSuchElementException:
                    continue
                try:
                    weight = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[6]').text
                except NoSuchElementException:
                    continue
                try:
                    forty_time_range = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[7]').text
                except NoSuchElementException:
                    continue
                try:
                    hometown = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[8]').text
                except NoSuchElementException:
                    continue
                try:
                    high_school = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[9]').text
                except NoSuchElementException:
                    continue
                try:
                    college = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[1]/tbody/tr/td/div[1]/font/strong').text
                except NoSuchElementException:
                    continue
                try:
                    player_url = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player) + ']/td[2]/a').get_attribute('href')
                except NoSuchElementException:
                    continue
                data = ds_rank + '~' + player_name + '~' + position + '~' + projected + '~' + height + '~' + weight + '~' + forty_time_range + '~' + hometown + '~' + high_school + '~' + college + '~' + player_url + '~' + str(team)
                print(data, file=open('nds_team_data_may2021.csv','a',encoding='UTF-8'))
                if player == 15:
                    driver.get('https://draftscout.com/college.php?DSTeamId=' + str(team) + '&DraftYear=' + str(year) + '&sortby=TSXPos&order=ASC&startspot=15')
                    for player2 in range(1,16):
                        try:
                            ds_rank = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[1]').text
                        except NoSuchElementException:
                            continue
                        try:
                            player_name = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[2]').text
                        except NoSuchElementException:
                            continue
                        try:
                            position = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[3]').text
                        except NoSuchElementException:
                            continue
                        try:
                            projected = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[4]').text
                        except NoSuchElementException:
                            continue
                        try:
                            height = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[5]').text
                        except NoSuchElementException:
                            continue
                        try:
                            weight = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[6]').text
                        except NoSuchElementException:
                            continue
                        try:
                            forty_time_range = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[7]').text
                        except NoSuchElementException:
                            continue
                        try:
                            hometown = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[8]').text
                        except NoSuchElementException:
                            continue
                        try:
                            high_school = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[9]').text
                        except NoSuchElementException:
                            continue
                        
                        try:
                            college = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[1]/tbody/tr/td/div[1]/font/strong').text
                        except NoSuchElementException:
                            continue
                        try:
                            player_url = driver.find_element_by_xpath('/html/body/font/div/div/b/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr[' + str(player2) + ']/td[2]/a').get_attribute('href')
                        except NoSuchElementException:
                            continue
                        data = ds_rank + '~' + player_name + '~' + position + '~' + projected + '~' + height + '~' + weight + '~' + forty_time_range + '~' + hometown + '~' + high_school + '~' + college + '~' + player_url + '~' + str(team)
    
                        print(data, file=open('nds_team_data_may2021.csv','a',encoding='UTF-8'))
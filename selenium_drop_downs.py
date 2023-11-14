from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
# path = r"C:\Users\varun\chromedriver-win64\chromedriver.exe"
driver = webdriver.Edge()
driver.get(website)
all_matches_button = driver.find_element(
    "xpath", '//label[@analytics-event = "All matches"]')
all_matches_button.click()

drop_down = Select(driver.find_element(By.ID, 'country'))
drop_down.select_by_visible_text('Japan')

time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)  # //tr/td[1]'
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

dict = {'date': date, 'home_team': home_team,
        'score': score, 'away_team': away_team}
df = pd.DataFrame(dict)
df.to_csv('football_data_japan.csv', index=False)
print(df)

# driver.quit()

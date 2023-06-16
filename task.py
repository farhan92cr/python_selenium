import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting')
driver.maximize_window()
driver.implicitly_wait(5)

start_range = '//*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr['
middle_range =']/td['
end_range = ']'

rows_data = driver.find_elements(By.XPATH,'//*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr')
total_rows_data = len(rows_data)


cols_data = driver.find_elements(By.XPATH,'//*[@id="top"]/div/div[5]/div[2]/div/table/tbody/tr[1]/td')
total_cols_data = len(cols_data)

for row in range(1,total_rows_data+1):
    for col in range(1,total_cols_data+1):
        print(driver.find_element(By.XPATH,start_range+str(row)+middle_range+str(col)+end_range).text,end = " ")
    print()
time.sleep(3)
driver.quit()
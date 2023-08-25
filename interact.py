from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://poki.com/en/g/crossy-road")

# select normal theme
theme_select = driver.find_element(by=By.XPATH ,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/button[1]")
theme_select.click()
sleep(2)

# drill down into correct html element
iframe = driver.find_element(by=By.XPATH, value='//*[@id="game-element"]')
driver.switch_to.frame(iframe)
inner_iframe = driver.find_element(by=By.XPATH, value='//*[@id="gameframe"]')
driver.switch_to.frame(inner_iframe)
game_window = driver.find_element(by=By.XPATH, value='/html/body')

# test
sleep(1)
game_window.send_keys(Keys.UP)
sleep(1)
game_window.send_keys(Keys.RIGHT)
sleep(1)
game_window.send_keys(Keys.DOWN)
sleep(1)
game_window.send_keys(Keys.LEFT)
sleep(1)

driver.quit()
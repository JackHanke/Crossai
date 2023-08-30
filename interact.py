from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from PIL import Image
from process import reward, feed_forward

driver = webdriver.Firefox()
driver.get("https://poki.com/en/g/crossy-road")

options = Options()
# options.set_preference()

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

move_dict = {0:None, 1:Keys.UP, 2:Keys.RIGHT, 3:Keys.DOWN, 4:Keys.LEFT}

# sleep(2)

move = 0
score = 0
while score >= 0:
    if move != 0:
        game_window.send_keys(move_dict[move])

    # screenshot game (needs optimizing)
    driver.switch_to.default_content()
    screenshot = driver.get_screenshot_as_file("image.png")
    screenshot_window = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div")
    screenshot_loc, screenshot_size = screenshot_window.location, screenshot_window.size
    x, y = screenshot_loc['x'], screenshot_loc['y']
    w, h = x + screenshot_size['width'], y + screenshot_size['height']
    screenshot = Image.open("./image.png")
    screenshot2 = screenshot.crop((x, y, w, h))
    screenshot2.save('./image.png')
    driver.switch_to.frame(iframe)
    driver.switch_to.frame(inner_iframe)

    score = reward(screenshot2)
    move = feed_forward(screenshot2, score)

driver.quit()
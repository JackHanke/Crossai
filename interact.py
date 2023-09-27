from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from PIL import Image, ImageOps, ImageChops
from process import reward
from random import randint

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

move = 0
score = 0
defecit=0
moves=[]
 
game_window.send_keys(move_dict[2])
sleep(1)

while score >= -10:
    if move != 0:
        game_window.send_keys(move_dict[move])

    # screenshot game (needs optimizing)
    driver.switch_to.default_content()
    screenshot = driver.get_screenshot_as_file("image.png")
    #screenshot = ImageOps.grayscale(color_screenshot)
    screenshot_window = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div")
    screenshot_loc, screenshot_size = screenshot_window.location, screenshot_window.size
    x, y = screenshot_loc['x'], screenshot_loc['y']
    w, h = x + screenshot_size['width'], y + screenshot_size['height']-64 # correction for white bar
    screenshot = Image.open(".\\image.png") #os path this
    screenshot2 = screenshot.crop((x, y, w, h))
    # screenshot2.save(f'.\\screenshots\\image{score}.png')
    driver.switch_to.frame(iframe)
    driver.switch_to.frame(inner_iframe)

    move = randint(0,4)
    if move == 1 and defecit > 0: defecit -= 1
    elif move == 3: defecit += 1
    elif move == 1 and defecit == 0: score += 1
    print(f"Move was: {move} Defecit is {defecit} Score is: {score}")
    sleep(0.25)
    

driver.quit()
import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    driver.close()
    driver.quit()

def test_koolio(driver):
    driver.get("https://development.app.koolio.ai/profile.html")

    username = driver.find_element(By.XPATH, "//input[@placeholder='User name or Email']")
    username.send_keys("Paykoolio")

    password = driver.find_element(By.XPATH, "//input[@id='lfpwd']")
    password.send_keys("123Abc!@")

    login_button = driver.find_element(By.XPATH, "//button[@class='line-height-input btn-padding text-l auth-button login-button']")
    login_button.click()

    add_file_button = WebDriverWait(driver, 75).until(EC.element_to_be_clickable((By.XPATH, "//img[@id='add-btn']")))
    add_file_button.click()

    file_upload = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@aria-label='Upload Project']")))
    file_upload.click()
    time.sleep(4)

    keyword = Controller()

    keyword.type("C:\\Users\\nabil\\Desktop\\pythonProject\\file\\1user_2.wav")
    keyword.press(Key.enter)
    keyword.release(Key.enter)

    confirm_upload = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']")))
    confirm_upload.click()

    confirm_upload2 = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']"))))
    confirm_upload2.click()
    time.sleep(60)

    view_button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(32) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
    action_chain = ActionChains(driver)
    action_chain.move_to_element(view_button).perform()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(32) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1) > span:nth-child(1)").click()

    play = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//img[@id='btn-play-icon']")))
    play.click()
    time.sleep(19)

    back = driver.find_element(By.XPATH, "//img[@id='btn-rewind']")
    back.click()

    edit = driver.find_element(By.XPATH, "//div[@id='control-opt-edit']")
    edit.click()

    spk_track = driver.find_element(By.XPATH, "//*[@id='playlist']/div/div/div[3]/div[1]")
    action_chain = ActionChains(driver)
    action_chain.click_and_hold(spk_track).move_by_offset(252.458328247073, 47.35416412353156).release().perform()

    copy = driver.find_element(By.XPATH, "//img[@id='btn-copy']")
    copy.click()

    past = driver.find_element(By.XPATH, "//img[@id='btn-insert-icon']")
    past.click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@id='insert-sub-menu']//img[@id='cm-insert-af-btn']").click()

    action_chain = ActionChains(driver)
    right_click = driver.find_element(By.XPATH, "//*[@id='playlist']/div/div/div[3]/div[2]")
    click_search = driver.find_element(By.XPATH, "//input[@id='sfxSearchBar']")
    action_chain.context_click(right_click).perform()
    time.sleep(1)
    click_search.click()
    time.sleep(1)
    click_search.send_keys("bird")

    sfx_sound = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[5]/a[1]")))
    sfx_sound.click()
    time.sleep(30)

    sfx_past = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='insert-sub-menu']//span[@id='cm-paste-btn']")))
    sfx_past.click()

    time.sleep(2)
    sfx_length = driver.find_element(By.XPATH, "//input[@id='sfx-min-length']")
    sfx_length.click()
    sfx_length.clear()
    sfx_length.send_keys(1.00)

    sfx_add = driver.find_element(By.XPATH, "//button[@id='sfx-length-button']")
    sfx_add.click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//*[@id='playlist']/div/div/div[3]/div[2]").click()
    time.sleep(3)

    sfx_track = driver.find_element(By.XPATH, "//*[@id='playlist']/div/div/div[3]/div[2]")
    action_chain = ActionChains(driver)

    action_chain.click_and_hold(sfx_track).move_by_offset(705.2083282470703, 42.666656494140625).release().perform()
    time.sleep(3)

    fade_button = driver.find_element(By.XPATH, "//img[@id='waveforms-selector']")
    fade_button.click()

    expo_button = driver.find_element(By.XPATH, "//img[@src='/static/img/workspace/controls/exponential.png']")
    expo_button.click()
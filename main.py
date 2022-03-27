from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver, By
from time import sleep
import webbrowser


def main(driver: WebDriver):
    with open("url.txt") as f:
        url = f.read().strip()
    driver.get(url)
    while True:
        sleep(30)
        try:
            driver.find_element(
            by=By.CLASS_NAME, value="shop-status-desc").text.strip()
            driver.refresh()
        except:
            webbrowser.open(url)
            break
    driver.quit()


if __name__ == "__main__":
    driver = webdriver.Safari()
    try:
        main(driver)
    except:
        driver.quit()

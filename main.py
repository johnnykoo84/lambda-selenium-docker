import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def handler(event=None, context=None):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--disable-application-cache')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.binary_location = '/opt/chrome/chrome'
    
    service = Service(executable_path='/opt/chromedriver')
    browser = webdriver.Chrome(service=service, options=chrome_options)

    print("browser", browser)

    browser.get("https://www.naver.com/")
    description = browser.find_element(By.NAME, "description").get_attribute("content")

    print(description)

    browser.close()

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": description,
            }
        ),
    }

if __name__ == '__main__':
    handler()
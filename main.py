import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from google.cloud import storage
from google.oauth2 import service_account

options = Options()
options.headless = True
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
url = "https://www.openrice.com/zh/hongkong"
driver.get(url)

elem = driver.find_element(By.ID,"header-searchbar-where-input")
elem.clear()
elem.send_keys('Central')
driver.find_element(By.CSS_SELECTOR, "div > button[type='submit']").click()
lis = driver.find_elements(By.CSS_SELECTOR,".sr1-listing-content-cell")

# ts = "2022-01-29"
temp = []
for li in lis:
    shop_name = li.find_element(By.CLASS_NAME,"title-name").text
    address = li.find_element(By.CLASS_NAME,"address").text
    temp.append([shop_name, address])
df = pd.DataFrame(temp,columns=['title','address'])
df.to_csv(f"data-{ts}.csv")
driver.close()

key_path = "vital-folder-331713-15f519e71cc2.json"
credentials = service_account.Credentials.from_service_account_file(key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
storage_client = storage.Client(credentials=credentials)
bucket = storage_client.bucket("storage_mika_csv")
blob = bucket.blob(f'data-{ts}.csv')
blob.upload_from_filename(f'data-{ts}.csv')

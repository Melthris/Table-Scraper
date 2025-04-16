from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Chromedriver needs to be added to the root directory of this script to work.
# You can get Chromedriver from the below link;
# https://developer.chrome.com/docs/chromedriver/downloads
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# First step is to get the login URL of the site you want to scrape
driver.get("YOURLOGINURLGOESHERE")
# We'll wait for 5 seconds to make sure the page is fully loaded
WebDriverWait(driver, 5).until (
    # After 5 seconds is up, we will proceed with our code once the
    # below ID is found on the page. Our code can safely continue to run
    # once it see's this as the whole page should now be loaded.
    # The element  that I'm using below is the sign-in email or username field ID
    EC.presence_of_element_located((By.ID, "SIGNINEMAILID"))
)
# Now we can start inputting our data 
input_element = driver.find_element(By.ID, "SIGNINEMAILID")
input_element.send_keys("user@website.com")
input_element = driver.find_element(By.ID, "SIGNINPASSWORDFIELD")
input_element.send_keys("Password123" + Keys.ENTER)

# After entering our login credentials, we now want to find the page that
# has the table data on it that we wish to scrape

driver.get("URLWITHTABLEDATATOSCRAPE")

# 15 seconds to wait is probably overkill so feel free to change
wait = WebDriverWait(driver, 15)
all_data = []
headers = []

# I'll explain what's happening below; First I am looking specifically for
# a dropdown menu to click, containing 'All time' as an option. My code then
# safely? assumes that this is a filter dropdown to find table data across all
# time instead of a smaller date window.
# Once this this done, we are going to start looking for all table data on the page,
# storing this in an array and then clicking onto the Next page to loop until Next
# is no longer selectable (last page).
# Once this is done, it will kill the loop, save the array into a CSV and terminate


try:
    # Step 1: Select "All time"
    dropdown = wait.until(EC.element_to_be_clickable((By.ID, "DATEFIELD-CONTROL")))
    dropdown.click()
    time.sleep(1.5)

    all_time_option = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='DATEDFIELD-DROPDOWNID']//div[text()='All time']")
    ))
    driver.execute_script("arguments[0].scrollIntoView(true);", all_time_option)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", all_time_option)
    print("📅 Selected 'All time'")
    time.sleep(3)

    # Step 2: Begin pagination loop
    while True:
        print("🔍 Scraping page...")
        table = wait.until(EC.presence_of_element_located((By.ID, "TABLEIDNAME")))
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            ths = row.find_elements(By.TAG_NAME, "th")
            tds = row.find_elements(By.TAG_NAME, "td")
            if ths and not headers:
                headers = [th.text.strip() for th in ths]
            elif tds:
                all_data.append([td.text.strip() for td in tds])

        # Try to find and click the "Next ›" button
        try:
            next_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Next')]")
            ))
            if 'disabled' in next_button.get_attribute("class").lower():
                print("⛔ 'Next' button is disabled. Done scraping.")
                break

            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(0.5)
            next_button.click()
            print("➡️ Going to next page...")
            time.sleep(3)  # Wait for next page to load

        except:
            print("🚫 No more pages or 'Next' button not found.")
            break

    # Step 3: Save to CSV
    if not headers and all_data:
        headers = [f"Column {i+1}" for i in range(len(all_data[0]))]

    df = pd.DataFrame(all_data, columns=headers)
    df.to_csv("all_tabledata.csv", index=False)
    print(f"✅ Finished scraping! Saved {len(all_data)} rows to all_tabledata.csv")

except Exception as e:
    print(f"❌ Error occurred: {e}")

finally:
    driver.quit()
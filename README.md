# 🕷️ Python Web Scraper for CRM Data Extraction

This was a small project I undertook while learning how to use **Python** and **Selenium**.

A client of mine was having issues with their old CRM supplier, who was not providing them with their client list or quote data to import into their new CRM of choice.

This presented them with significant issues. Their first solution was to manually copy and paste the information themselves — but given the sheer volume of quotes and clients, this would take **hours**.

💡 **This script takes a couple of minutes.**

---

## 📌 What This Script Does

- Automatically loads the legacy CRM system's web interface
- Selects the "All time" date filter to retrieve complete quote data
- Scrapes table data across **all available pages**
- Compiles all records into a clean, well-structured **CSV file**
- Saves you hours of manual work!

---

## 🧰 Technologies Used

- [Python 3](https://www.python.org/)
- [Selenium WebDriver](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/) for data processing
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) to control Chrome

---

## 🚀 How to Run This Script

### 1. Clone or Download the Repository
bash:
```
git clone https://github.com/melthris/table-scraper.git
cd table-scraper
```
### 2. Install Dependencies
Make sure you have Python installed, then install required packages:

bash:
```
pip install selenium pandas
```
### 3. Download ChromeDriver
Download the version of ChromeDriver that matches your installed version of Chrome (https://developer.chrome.com/docs/chromedriver/downloads) and place it in your project folder or system PATH.

### 4. Update the Target login URL, username & password and data URL
Open the Python file and update the url variables with the web address of your client’s login to the CRM, the login details and then the page where the data is that you wish to scrape. 

Python:
```
driver.get("YOURLOGINURLGOESHERE")  # Replace this with the actual login URL of the CRM
```
Python:
```
input_element = driver.find_element(By.ID, "SIGNINEMAILID") # the email address ID
input_element.send_keys("user@website.com")  # the email address you'll use to log into the CRM
input_element = driver.find_element(By.ID, "SIGNINPASSWORDFIELD") # the password ID
input_element.send_keys("Password123" + Keys.ENTER)  # the password you'll use to log into the CRM
```

Python:
```
driver.get("URLWITHTABLEDATATOSCRAPE"))  # Replace this with the Data page of the CRM once logged in
```
### 5. Run the Script
bash:
```
python main.py
```

The script will open Chrome, navigate the quote pages, collect data, and save everything into:

all_tabledata.csv
📁 Output
all_tabledata.csv – A single CSV file containing all scraped quote data from the legacy CRM

✍️ Author's Note
This project was part of my journey learning Python and automation using Selenium. What started as a helpful tool for a client became a great learning experience in web scraping, browser automation, and data handling.

⚠️ Legal Disclaimer
Ensure you have permission to scrape or extract data from any website. This script was developed for legitimate use in helping a client retrieve their own data.


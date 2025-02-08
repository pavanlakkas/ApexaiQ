from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import TimeoutException
import time
from webdriver_manager.chrome import ChromeDriverManager


# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--window-size=1920,1080")

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the Microsoft website
url = "https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info"
driver.get(url)
WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))

# Find all tables on the webpage
tables = driver.find_elements(By.TAG_NAME, "table")

# Dictionary to store all table data
all_tables_dict = {}

def extract_table_data(table_xpath):
    table = driver.find_element(By.XPATH, table_xpath)
    rows = table.find_elements(By.TAG_NAME, "tr")
    table_data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text.strip() for cell in cells if cell.text.strip()]
        if row_data:
            table_data.append(row_data)
    return table_data

# Loop through and reveal all dropdown tables
dropdowns = driver.find_elements(By.XPATH, "//*[@id='winrelinfo_container']//button[contains(@class, 'dropdown-btn')]")

for dropdown in dropdowns:
    dropdown.click()
    time.sleep(1)  # Wait to allow table visibility updates

# Example table extraction using dedicated functions
table_xpaths = [
    "//*[@id='winrelinfo_container']/div[2]/table[1]",
    "//*[@id='winrelinfo_container']/div[2]/table[2]",
    "//*[@id='winrelinfo_container']/div[2]/table[3]"
]

# Extract data for each table
for index, table_xpath in enumerate(table_xpaths):
    table_data = extract_table_data(table_xpath)
    if table_data:
        all_tables_dict[f"Table_{index+1}"] = table_data

    rows = driver.find_elements(By.XPATH, "//*[@id='winrelinfo_container']/div[2]/table/tbody/tr")
    for row in rows:
        cells = row.find_elements(By.XPATH, "//*[@id='winrelinfo_container']/div[2]/table/tbody/tr[1]/th[1]")  # Find all columns
        row_data = [cell.text.strip() for cell in cells]  # Extract text
        if row_data:  # Avoid empty rows
            table_data.append(row_data)

    rows = driver.find_elements(By.XPATH, "//*[@id='winrelinfo_container']/div[2]/table/tbody/tr")
    for row in rows:
        cells = row.find_elements(By.XPATH, "//*[@id='winrelinfo_container']/div[2]/table/tbody/tr[2]/td[1]")  # Find all columns
        row_data = [cell.text.strip() for cell in cells]  # Extract text
        if row_data:  # Avoid empty rows
            table_data.append(row_data)

    if table_data:
        all_tables_dict[f"Table_{index+1}"] = table_data

# Print the extracted data (Dictionary format)
print("Scraped Data in Dictionary Format:")
for table_name, data in all_tables_dict.items():
    print(f"\n{table_name}:")
    for row in data:
        print(row)

# Save combined data from all tables into a single CSV file
save_path = "D:/Apexaiq/programs/CSV"
combined_data = []

for table_name, table_data in all_tables_dict.items():
    combined_data.extend(table_data)  # Add table data without table labels

df = pd.DataFrame(combined_data)
df.to_csv(f"{save_path}\\combined_tables.csv", index=False, header=False)

# Close the browser
driver.quit()

print(f"\n Successfully saved {len(all_tables_dict)} tables to CSV files in {save_path}")


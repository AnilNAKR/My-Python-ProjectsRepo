from selenium import webdriver
from selenium.webdriver.common.by import By

#  To keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Samsung-Phantom-Storage-Additional-Exchange/dp/B09SH8JPCJ/?_encoding=UTF8&pd_rd_w=7BwZS&content-id=amzn1.sym.4f3c73a8-dac5-4181-8aa7-51fa268716c9%3Aamzn1.symc.cdb151ed-d8fe-485d-b383-800c8b0e3fd3&pf_rd_p=4f3c73a8-dac5-4181-8aa7-51fa268716c9&pf_rd_r=FBK7V1RG0AWM487JKRJD&pd_rd_wg=qj3hz&pd_rd_r=0989c159-482e-463a-9537-9f09beac1f04&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1")

price_symbol = driver.find_element(By.CLASS_NAME, value="a-price-symbol")
price_inr = driver.find_element(By.CLASS_NAME, value="a-price-whole")
print(f"The price is {price_symbol.text}.{price_inr.text}/-")

# Close() closes only a particular Tab
# driver.close()
# Quit() closes entire browser
driver.quit()


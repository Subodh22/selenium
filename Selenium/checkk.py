from selenium import webdriver
import os,time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(r"C:\Users\Subodh Maharjan\Desktop\projectEORBY8EEI.pdf")
time.sleep(2)
maine=driver.find_elements_by_tag_name("div")
print(maine)
try: 
     main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.find_elements_by_tag_name,"div"))
     )
     print(main)
    
    
    
except : 
        print("oops")
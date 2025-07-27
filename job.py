from selenium import webdriver
from selenium.webdriver.common.by import By


class Job:
    def __init__(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        job_details=driver.find_element(By.XPATH,'//*[@id="details_container"]/div[2]')
        self.info=job_details.text
        driver.quit()
    def get_info(self):
        return self.info


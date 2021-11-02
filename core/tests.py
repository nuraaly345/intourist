from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class SeleniumTest(TestCase):
    def test_one(self):
        driver = webdriver.Edge()
        driver.get("http://127.0.0.1:8000/places/create/")
        #elem = driver.driver.find_element_by_link_text('Создать место')
        #elem.click() 
     
        name = driver.find_element_by_name('name')
        name.send_keys('Test name')

        location = driver.find_element_by_name('location')
        location.send_keys('Test location')

        description = driver.find_element_by_name('description')
        description.send_keys('Test description')

        button = driver.find_element_by_xpath("//*[contains(text(), 'Сохранить')]")
        button.click()

        sleep(5)

        driver.close()


class ProfileTestCase(TestCase):
    def test_open_profile_edit(self):
        driver = webdriver.Edge()
        deriver.get("http://127.0.0.1:8000/profile/")

        element = driver.find_element_by_xpath("//*[contains(test(), Редактировать)]")
        element.click()



#title: Automate Testing For BITS
#Author: Tandin Wangchuk
#Discription : BITS Admin | PIT

import time
import HtmlTestRunner
import unittest

from setup import driver
cidNumber = "11905002029"
stagingurl = "http://10.11.1.13/bits/"
productionurl = "https://bits.drc.gov.bt/bits/"
uaturl = "https://bitsuat.drc.gov.bt/bits/"
url = uaturl

def guardian():
    # ID document
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").value = "11905001127"')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')

    # searchbutton
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-image").shadowRoot.querySelector("img").click()')

    # mobileNumber   
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = "17473422"')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')

    # nextButton
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(7) > wc-container:nth-child(2) > wc-container:nth-child(8) > wc-button:nth-child(2)").shadowRoot.querySelector("button").click()')


def spouseDetail():
    time.sleep(10)
    # title
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(8) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value =9')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(8) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
    # mobileNumber
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(8) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(5) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = 17478922')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(8) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(5) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
    time.sleep(5)
    # nextButton
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(8) > wc-container:nth-child(4) > wc-button:nth-child(2)").shadowRoot.querySelector("button").click()')


def contactDetail():
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(6) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = 17451312')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(6) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
    time.sleep(2)

    # nextButton
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(6) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-button:nth-child(2)").shadowRoot.querySelector("button").click()')

    file1 = open("result.log", "a")
    file1.write("provided contact detail) \n")
    file1.close()

def addressDetail():
    # select dzongkhag
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(11) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 1')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(11) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
    time.sleep(2)
    # select gewog/thromde
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(11) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 1')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(11) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
    time.sleep(2)
    # select village
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(11) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 1')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(11) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
    time.sleep(2)
    # nextButton
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(11) > wc-container:nth-child(3) > wc-button:nth-child(2)").shadowRoot.querySelector("button").click()')

def bankDetail():
    # select Bank
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").selectedIndex = 2')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
    time.sleep(2)
    # select branch
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").selectedIndex = 2')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
    time.sleep(2)
    # select account type
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").selectedIndex = 1')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
    time.sleep(2)
    # accountnumber
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(3) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = 200492017')
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(2) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(3) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
    time.sleep(2)
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(12) > wc-container:nth-child(3) > wc-button:nth-child(2)").shadowRoot.querySelector("button").click()')


def finalize():
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(15) > wc-container > wc-container:nth-child(1) > wc-checkbox-group").shadowRoot.querySelector("#checkbox-1").click()')
    time.sleep(2)
    driver.execute_script(
        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(17) > wc-container:nth-child(3) > wc-button").shadowRoot.querySelector("button").click()')

    time.sleep(10)



class TestBITS(unittest.TestCase):

    def test_A_admin_Login(self):
        time.sleep(5)
        # username
        userName = driver.find_elements_by_xpath(
            "/html/body/app-root/app-auth-layout/div/div[2]/div/app-auth-page/app-basic-login-page/app-auth-form/form/nz-form-item[1]/nz-form-control/div/span/input")[
            0]
        userName.send_keys('admin')
        time.sleep(1)
        # password
        password = driver.find_elements_by_xpath(
            "/html/body/app-root/app-auth-layout/div/div[2]/div/app-auth-page/app-basic-login-page/app-auth-form/form/nz-form-item[2]/nz-form-control/div/span/app-password-input/nz-input-group/input")[
            0]
        password.send_keys('admin')
        time.sleep(1)
        # submit
        submit = driver.find_elements_by_xpath(
            "/html/body/app-root/app-auth-layout/div/div[2]/div/app-auth-page/app-basic-login-page/app-auth-form/form/nz-form-item[3]/nz-form-control/div/span/button")[
            0]
        submit.click()
        time.sleep(5)
        self.assertEqual(driver.current_url, url+"1bca6d5c-7e79-4bcd-8558-159e3de95810")

    def test_B_create_New_Document(self):
        driver.get(url+"47143f65-4b69-401e-8f60-667a26dfdc94")
        time.sleep(10)
        driver.execute_script('document.querySelector("hatis-renderer").shadowRoot.children[2].querySelector("form-renderer").shadowRoot.querySelector("div").children[2].children[1].querySelector("wc-container").children[1].children[2].children[0].querySelector("wc-button").shadowRoot.querySelector("button").click()')

    def test_C_register_with_CID(self):
        time.sleep(15)
        # select cid
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(3) > wc-select").shadowRoot.querySelector("#container > select").selectedIndex = 1')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(3) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        time.sleep(2)
        # entercid
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(4) > wc-input").shadowRoot.querySelector("#container > input").value = '+cidNumber+'')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(4) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # click on button
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(7) > wc-container:nth-child(1) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(10)
        self.assertEqual(driver.current_url,url+"a7ea8e57-73df-43c9-8c4d-b8f586e374a0%3FdocType%3D7&cid%3D"+cidNumber+"","Enter Valid CID number / Entered CID is already Registered")

    def test_D_fetch_data_from_API(self):
        time.sleep(15)
        fetchName = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value')
        self.assertTrue(fetchName!="")
    def test_E_select_Their_title(self):
        # select title
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").selectedIndex = 4')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        time.sleep(2)

    def test_F_select_region_of_registration(self):
        # Region of Registration
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").selectedIndex = 4')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        time.sleep(2)

    def test_G_add_source_of_income(self):
        # source of income
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-multi-select").shadowRoot.querySelector("#itemList > div:nth-child(3) > input[type=checkbox]").click()')
        time.sleep(2)

    def test_H_add_contact_and_family_details(self):
        dob = driver.execute_script(
            'return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(2) > wc-date-picker").shadowRoot.querySelector("#inputContainer > input").value.substr(0,4)')
        age = 2021 - int(dob)
        if (age > 18):
            # next Button
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-button").shadowRoot.querySelector("button").click()')
            time.sleep(10)
            contactDetail()
            maritalStatus = driver.execute_script(
                'return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value')
            hasClid = driver.execute_script(
                'return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value')
            if maritalStatus == "1":
                # nextButton
                driver.execute_script(
                    'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-button").shadowRoot.querySelector("button")')
                spouseDetail()
                if hasClid == "yes":
                    time.sleep(10)
                    # number of children
                    children = driver.execute_script(
                        'return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(9) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-fractal").shadowRoot.querySelector("slot").children.length')
                    for i in range(children):
                        index = str(i + 1)
                        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(9) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-fractal").shadowRoot.querySelector("slot > wc-slot:nth-child('+index+') > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 9')
                        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(9) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-fractal").shadowRoot.querySelector("slot > wc-slot:nth-child('+index+') > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
                    # next
                    driver.execute_script(
                        'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(9) > wc-container:nth-child(3) > wc-button:nth-child(2)").shadowRoot.querySelector("button").click()')

        else:
            # nextButton
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-button").shadowRoot.querySelector("button").click()')
            time.sleep(10)
            contactDetail()
            driver.execute_script(
                'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(6) > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-button:nth-child(2)").shadowRoot.querySelector("button").click()')
            time.sleep(10)
            guardian()

    def test_I_permenant_address_api(self):
        permenantAddress = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(10) > wc-container:nth-child(2) > wc-container > wc-container:nth-child(4) > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value')
        self.assertTrue(permenantAddress!="")

    def test_J_add_present_address(self):
        addressDetail()

    def test_K_add_bank_detail(self):
        bankDetail()

    def test_L_register(self):
        finalize()
        drn = driver.execute_script(
            'return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        # ok button
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(15)
        # document nav bar
        driver.get(url+'47143f65-4b69-401e-8f60-667a26dfdc94')
        time.sleep(15)
        # enter drn
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = ' + '"' + drn + '"' + '')
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')

    def test_M_Amendment(self):
        time.sleep(10)
        tpn = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(3) > wc-container:nth-child(2) > wc-scroll-container > wc-container:nth-child(4) > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(6) > wc-input").shadowRoot.querySelector("#container > input").value')
        # navigate to taxpayer
        driver.get(url+'aee128cd-016f-4c8b-8049-f676dbbdd609')
        time.sleep(15)
        # enter TPN
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value=' +'"'+tpn+'"'+'')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        # search
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        # click on view
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-scroll-container > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(11) > wc-tooltip:nth-child(1) > wc-container > wc-image").shadowRoot.querySelector("img").click()')
        time.sleep(10)
        #click edit
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        #change title
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value = 4')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").dispatchEvent(new Event("change"))')
        # save
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(14) > wc-container > wc-container:nth-child(1) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(20)
        drn_aft = driver.execute_script(
            ' return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-text").shadowRoot.querySelector("div").innerText.split(".")[1].split(" ")[6]')
        # ok button
        driver.execute_script(
            'document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div.modal > div > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        #Taxpayer
        driver.get(url+'aee128cd-016f-4c8b-8049-f676dbbdd609')
        time.sleep(15)
        #cid number
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").value = '+'"'+cidNumber+'"'+'')
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(5) > wc-container:nth-child(2) > wc-input").shadowRoot.querySelector("#container > input").dispatchEvent(new Event("input"))')
        #search
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(3) > wc-container:nth-child(1) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(5)
        #view
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-container:nth-child(2) > wc-scroll-container > wc-fractal").shadowRoot.querySelector("slot > wc-slot > wc-container > wc-container:nth-child(1) > wc-container > wc-text").shadowRoot.querySelector("div").click()')
        time.sleep(15)
        #edit button
        driver.execute_script('document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(1) > wc-container > wc-container:nth-child(2) > wc-button").shadowRoot.querySelector("button").click()')
        time.sleep(2)
        # get title
        title = driver.execute_script('return document.querySelector("body > app-root > app-main-layout > nz-layout > nz-layout > nz-content > div > app-hatis-page > div > hatis-renderer").shadowRoot.querySelector("div:nth-child(3) > form-renderer").shadowRoot.querySelector("div > div.main-content > div.container > wc-container > wc-container:nth-child(2) > wc-container:nth-child(4) > wc-container:nth-child(2) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(1) > wc-container:nth-child(2) > wc-select").shadowRoot.querySelector("#container > select").value')
        self.assertEqual(title,'4')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        report_name= "PIT_Test_Result",
        report_title= "PIT_Test_Result | CID : "+ cidNumber,

    ))

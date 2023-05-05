# -*- coding: utf-8 -*-
# @Time  : 2023/3/13 19:12
# Author : Adan

from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class TestClass:
    def setup(self):
        # 創建⼀個字典,⽤於存儲設備和應用訊息
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "127.0.0.1:5556",
            "appPackage": "tw.com.icash.a.icashpay",
            "appActivity": "tw.net.pic.m.wallet.activity.WelcomeActivity",
            "disableAndroidWatchers": True,
            "automationName": "uiautomator2",
            "allowInsecure": True,
            "skipDeviceInitialization": True,
            "ignoreUnimportantViews": True,
            "noReset": True,
            "autoGrantPermissions": True,
            "allowTestPackages": True,
            "adbExecTimeout": "60000",
            "unlockType": "pin",
            "unlockKey": "135790",
            "autoAcceptAlerts": True,
            "settings": {
                "ignoreUnimportantViews": True,
                "enableNotificationListener": True,
                "waitForIdleTimeout": 0,
                "shouldUseCompactResponses": False,
                "eventTimings": True,
                "sendKeyStrategy": "grouped",
                "unicodeKeyboard": True,
                "resetKeyboard": True,
                "autoGrantPermissions": True,
                "password": "135790",
                "passwordStorage": "clear_text"
            }
        }

        # 與appium session之間建⽴聯繫，括號為appium服務地址
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        close_btn_locator = (MobileBy.ID, "tw.com.icash.a.icashpay:id/txt_right")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(close_btn_locator)).click()



        # 重複的程式碼可以將重複的程式碼抽出成函式，減少程式碼量和提高程式碼的可維護性。
        # 例如，以下程式碼中，點擊"首頁"
        # 按鈕和關閉"彈窗"的部分程式碼被多次使用

    # def go_to_home(self,driver):
    #     homep = (MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarHome"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep)).click()
    #
    # def close_popup(self,driver):
    #     popupclose = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose)).click()

    def enter_security_password(driver):
        inputpw = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入安全密碼")')
        if EC.visibility_of_element_located(inputpw):
            one = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")')
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(one)).click()

            three = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")')
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(three)).click()

            five = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("5")')
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(five)).click()

            seven = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("7")')
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(seven)).click()

            nine = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("9")')
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(nine)).click()

            zero = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0")')
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(zero)).click()

    def test_001(self):
        home_name_locator = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        home_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_name_locator))).text
        # inputpw = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入安全密碼")')
        # from uiautomator2.xpath import TimeoutException
        # try:
        #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(inputpw))
        #     driver.find_element_by_android_uiautomator('new UiSelector().text("1")').click()
        #     driver.find_element_by_android_uiautomator('new UiSelector().text("3")').click()
        #     driver.find_element_by_android_uiautomator('new UiSelector().text("5")').click()
        #     driver.find_element_by_android_uiautomator('new UiSelector().text("7")').click()
        #     driver.find_element_by_android_uiautomator('new UiSelector().text("9")').click()
        #     driver.find_element_by_android_uiautomator('new UiSelector().text("0")').click()
        # except TimeoutException:
        #     pass


        #self.enter_security_password(driver)
        print(home_name)
        contact_person = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_friend")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(contact_person)).click()
        personal = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_user")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(personal)).click()


    #     self.go_to_home(driver)
    #     self.close_popup(driver)
    #     homep = (MobileBy.XPATH,'//android.widget.FrameLayout[@content-desc="首頁"]')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep)).click()

    # 彈出關閉 截圖提醒
    # popupclose = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose)).click()

    def test_002(self):
        home2 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home2)).click()
        payment_instument = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("支付工具")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(payment_instument)).click()
        Creditcard = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="信用卡"]')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Creditcard)).click()
        BankAccount = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="銀行帳戶"]')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BankAccount)).click()
        # home_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home2))).click()
        # 開啟icash2.0

    def test_003(self):
        home3 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home3)).click()
        icash2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("icash2.0")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(icash2)).click()
        newcard = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新卡上市")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(newcard)).click()

        backpage = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(backpage)).click()

        eventnews = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("活動快訊")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(eventnews)).click()

    def test_004(self):
        home4 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home4)).click()
        paytaxes = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("繳費稅")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(paytaxes)).click()
        parkingfee = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("停車費")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(parkingfee)).click()
        Taipeiparkingfee = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("臺北市路邊臨時停車費")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Taipeiparkingfee)).click()
        Inputcarno = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇車種")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Inputcarno)).click()
        Setcar = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("汽車")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Setcar)).click()
        edit1 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/edit1")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(edit1)).send_keys("BFW")
        edit2 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/edit2")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(edit2)).send_keys("1060")
        Billing_inquiry = (MobileBy.ID, "tw.com.icash.a.icashpay:id/query")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Billing_inquiry)).click()

    def test_005(self):
        home5 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home5)).click()
        cupstored = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自帶杯儲值")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(cupstored)).click()
        TopUpAmout = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")')
        if driver.find_element(*TopUpAmout).text == "5":
            print("pass")
        else:
            print("fail")

    def test_006(self):
        home6 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home6)).click()
        Generaltax = (MobileBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout[1]')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Generaltax)).click()
        # time.sleep(2)

        # driver.quit()

    #     # time.sleep(5)
    #     # 彈出關閉
    #     self.close_popup(driver)
    #     #popupclose2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
    #     #WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose2)).click()
    #
    #     # 買二送二
    #     buyonegetpone_locator = (MobileBy.ID, 'com.nineyi.shop.s002131:id/cms_item_view_carousel_img_leftbb')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(buyonegetpone_locator)).click()
    #     #driver.find_element(MobileBy.ID, 'com.nineyi.shop.s002131:id/cms_item_view_carousel_img_leftbb').click()

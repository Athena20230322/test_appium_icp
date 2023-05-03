# -*- coding: utf-8 -*-
# @Time  : 2023/3/13 19:12
# Author : Adan

from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
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
            "unlockKey": "135790"
        }

        # 與appium session之間建⽴聯繫，括號為appium服務地址
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        close_btn_locator = (MobileBy.ID, "tw.com.icash.a.icashpay:id/txt_right")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(close_btn_locator)).click()

        # one = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(one)).click()
        #
        # three = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(three)).click()
        #
        # five = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("5")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(five)).click()
        #
        # seven = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text"7")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(seven)).click()
        # nine = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text"9")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(nine)).click()
        #
        # zero = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text"0")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(zero)).click()






        # account_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的帳戶")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(account_locator)).click()
        #
        # phone_locator = (MobileBy.ID, "com.nineyi.shop.s002131:id/id_et_input")
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(phone_locator)).send_keys("0919541317")
        #
        # login_btn_locator = (MobileBy.ID, "com.nineyi.shop.s002131:id/id_btn_login")
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_btn_locator)).click()
        #
        #
        # password_locator = (MobileBy.ID, "com.nineyi.shop.s002131:id/id_et_input")
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password_locator)).send_keys("dlink5229")
        #
        #
        # passwd_btn_locator = (MobileBy.ID, "com.nineyi.shop.s002131:id/id_btn_input_passwd")
       # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(passwd_btn_locator)).click()

        #重複的程式碼可以將重複的程式碼抽出成函式，減少程式碼量和提高程式碼的可維護性。
        #例如，以下程式碼中，點擊"首頁"
        #按鈕和關閉"彈窗"的部分程式碼被多次使用
    # def go_to_home(self,driver):
    #     homep = (MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarHome"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep)).click()
    #
    # def close_popup(self,driver):
    #     popupclose = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose)).click()


        # agree_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("同意")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(agree_locator)).click()
        # 点击我知道了按钮
        #driver.find_element(MobileBy.ACCESSIBILITY_ID,"关闭").click()
        # know_locator = (MobileBy.ACCESSIBILITY_ID, "关闭")
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(know_locator)).click()
        #time.sleep(10)

        # 滑动屏幕，露出新品tab
        # x = driver.get_window_size()['width']
        # y = driver.get_window_size()['height']
        # driver.swipe(int(x * 0.5), int(y * 0.5), int(x * 0.5), int(y * 0.1), duration=500)

        # 点击手机数码tab
        #driver.find_element(MobileBy.XPATH,'//android.widget.RelativeLayout[@content-desc="苏宁超市"]/android.widget.ImageView').click()
        # newcomm_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("手机数码")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(newcomm_locator)).click()

    def test_001(self):
    #     # 獲取登入後eshop會員卡
        home_name_locator = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        home_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_name_locator))).text
        print(home_name)

        contact_person = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_friend")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(contact_person)).click()
        time.sleep(2)

        personal = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_user")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(personal)).click()
        time.sleep(2)
    #     self.go_to_home(driver)
    #     self.close_popup(driver)
    #     homep = (MobileBy.XPATH,'//android.widget.FrameLayout[@content-desc="首頁"]')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(homep)).click()

        #彈出關閉 截圖提醒
        #popupclose = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose)).click()

        # 點選熱銷排行
        # hotInfo_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("活動訊息 - icash Pay")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(hotInfo_locator)).click()
       # time.sleep(2)
        # 獲取折扣活動
        # discountInfo_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("折扣活動")')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(discountInfo_locator)).click()


        # # 断言首页商品名称等于详情页商品名称
        # assert home_name == pageInfo_name, f"预期名称为{home_name}，实际结果为{pageInfo_name}"

    def test_002(self):
        home2 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home2)).click()
        payment_instument = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("支付工具")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(payment_instument)).click()
        Creditcard = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="信用卡"]')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Creditcard)).click()
        BankAccount = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="銀行帳戶"]')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BankAccount)).click()
        #home_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home2))).click()
        #開啟icash2.0



    def test_003(self):
        home3 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home3)).click()
        icash2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("icash2.0")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(icash2)).click()
        newcard = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新卡上市")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(newcard)).click()

        backpage = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(backpage)).click()

        eventnews = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("活動快訊")')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(eventnews)).click()

    #     #我的帳戶
    #    # driver.find_element(MobileBy.XPATH,'//android.view.ViewGroup[@content-desc="tabBarMember"]/android.view.ViewGroup/android.widget.TextView').click()
    #     # member = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="tabBarMember"]/android.view.ViewGroup/android.widget.TextView')
    #     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(member)).click()
    #    # time.sleep(5)
    #     # 修改密碼
    #     # changepw = (MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="memberChangePwBtn"]/android.widget.RelativeLayout/android.widget.TextView')
    #     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(changepw)).click()
    #
    #     # driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("原始密碼")').send_keys("dlink5229")
    #
    #     # driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入新密碼6-20碼英數字")').send_keys("icash1234")
    #     # time.sleep(3)
    #     # driver.find_element(MobileBy.ID, "com.nineyi.shop.s002131:id/id_btn_next").click()
    #     # time.sleep(3)
    #     # 領折價券
    #     # discountcoupon_locator = (MobileBy.ID, 'com.nineyi.shop.s002131:id/brand_link_btn2')
    #     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(discountcoupon_locator)).click()

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
        time.sleep(3)

    #    # time.sleep(5)
    #     # 彈出關閉
    #     self.close_popup(driver)
    #     #popupclose2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
    #     #WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose2)).click()
    #     #time.sleep(3)
    #
    #     # 買一送一
    #     buyonegetpone_locator = (MobileBy.ID,'com.nineyi.shop.s002131:id/cms_item_view_carousel_img_left')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(buyonegetpone_locator)).click()
    #    # driver.find_element(MobileBy.ID,'com.nineyi.shop.s002131:id/cms_item_view_carousel_img_left').click()
    #    # time.sleep(4)
    #
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

    #    # time.sleep(5)
    #     # 等待關閉按鈕出現
    #     self.close_popup(driver)
    #     #popupclose2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("關閉")')
    #     #WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popupclose2)).click()
    #     #點擊關閉按鈕
    #
    #
    #     #等待購物車按鈕出現
    #
    #     #driver.find_element(MobileBy.ID, 'com.nineyi.shop.s002131:id/cms_item_view_carousel_img_left').click()
    #     cart_locator = (MobileBy.ACCESSIBILITY_ID, 'tabBarCart')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(cart_locator))
    #     driver.find_element(*cart_locator).click() #進入購物車頁面
    #     #定位商品價格元素
    #
    #     item_price_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$420")')
    #     item_price_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(item_price_locator))
    #
    #     #獲取商品價格本文
    #     item_price_text = item_price_element.text
    #     # 定義期望價格
    #     expected_price = "NT$410"
    #
    #     # 判斷價格是否正確
    #     if item_price_text == expected_price:
    #         print("Item price is correct!")
    #     else:
    #         print(f"Item price is incorrect. Expected {expected_price}, but got {item_price_text}")
    #
    #
    #     #下一步
    #     driver.find_element(MobileBy.ID, "com.nineyi.shop.s002131:id/shoppingcart_next_step_button").click()

    def test_006(self):
        home6 = (MobileBy.ID, "tw.com.icash.a.icashpay:id/navigation_home")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home6)).click()
        Generaltax = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout[1]')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Generaltax)).click()
        #time.sleep(2)

        #driver.quit()

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
  


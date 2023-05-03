from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:5556',
    'appPackage': 'tw.com.icash.a.icashpay.debuging',
    'appActivity': 'tw.net.pic.m.wallet.activity.WelcomeActivity',
    'noReset': True
}

# 连接 Appium Server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 获取并保存屏幕截图
driver.save_screenshot('C:\\python_test\\test_appium\\testcases\\screenshot.png')

# 关闭连接
driver.quit()

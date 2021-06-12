from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
mname = "xx"
# input("Enter the middle name u want to set :")

dcs = []
dc = {}
dc['platformName'] = 'Android'
dc['deviceName'] = '16824257'
dc['noReset'] = 'true'
dc['appPackage'] = 'com.enstage.wibmo.hdfc'
dc['appActivity'] = 'com.enstage.wibmo.main.MainActivity'
dc['realDevice'] = 'true'
dcs.append(dc)

dc2={}
dc2['platformName'] = 'Android'
dc2['deviceName'] = '16824257'
dc2['noReset'] = 'true'
dc2['appPackage'] = 'com.excean.parallelspace'
dc2['appActivity'] = 'com.excelliance.kxqp.ui.MainActivity'
dc2['realDevice'] = 'true'
dcs.append(dc2)

# dc['isHeadless'] = 'true'
for i in [0,1]:
    dr = None
    if i == 0:
        dr = webdriver.Remote('http://localhost:4723/wd/hub', dcs[0])
    else :
        dr = webdriver.Remote('http://localhost:4723/wd/hub', dcs[1])
        time.sleep(1)
    if i == 1:
        el1 = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView[2]")
        el1.click()

    time.sleep(4)
    el1 = dr.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[1]")

    el2 = dr.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[2]")

    el3 = dr.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[3]")

    el4 = dr.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[1]")

    el5 = dr.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[2]")

    el6 = dr.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[3]")

    if i == 0:
        el1.click()
        el2.click()
        el3.click()
        el4.click()
        el5.click()
        el6.click()
    if i == 1:
        el5.click()
        el1.click()
        el2.click()
        el6.click()

    el6 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/login_button")
    el6.click()
    time.sleep(2.25)
    el2 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/buttonNegative")
    el2.click()
    el3 = dr.find_element_by_accessibility_id("Navigate up")
    el3.click()
    time.sleep(1)
    TouchAction(dr).tap(x=275, y=1554).perform()

    time.sleep(1)
    el5 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/button_manageprofile")
    el5.click()
    time.sleep(0.5)
    el6 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/main_mname_edit")
    el6.clear()
    el6.send_keys(mname)
    el7 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/main_btnSave")
    el7.click()
    el8 = dr.find_element_by_accessibility_id("Navigate up")
    el8.click()
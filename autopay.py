from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import csv

dcs = []
dc = {}
dc['platformName'] = 'android'
dc['deviceName'] = 'Vivo 1802'
dc['noReset'] = 'true'
dc['appPackage'] = 'multi.parallel.dualspace.cloner'
dc['appActivity'] = 'multi.parallel.dualspace.cloner.components.ui.MainActivity'
dc['realDevice'] = 'true'
dc['automationName'] = 'UiAutomator2'
dcs.append(dc)

passwords = ['5126','9389', '1234']


numbers={"1": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[1]",
         "2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[2]",
         "3": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.Button[3]",
         "4": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[1]",
         "5": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[2]",
         "6": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.Button[3]",
         "7": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.Button[1]",
         "8": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.Button[2]",
         "9": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.Button[3]",
         "0": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[4]/android.widget.Button[2]"}

apps = ["/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView",
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView[1]",
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView[2]"]

app_index=0

# data = pd.read_csv('SANJAY JI TESTING BILL 17.06.21.csv') 
data = pd.read_excel(r'01_04-05-21_40355_61_JDP.xlsx')
df = pd.DataFrame(data, columns=['Description', 'Biller Name', 'K Number', 'Amount'])
length = len(df.index)

file = open('Sheet1_updated.csv', 'w')
fieldnames = ['Sno', 'Due Date', 'Description', 'Biller Name', 'K Number', 'Amount', 'Status', 'File Name']
thewriter = csv.DictWriter(file, fieldnames=fieldnames)
thewriter.writeheader()


i=1
dr = webdriver.Remote('http://localhost:4723/wd/hub', dcs[0])

dr.implicitly_wait(30)

bill_pay_value = 0
elec_value = 0


def login(passw):
	el1 = dr.find_element_by_xpath(apps[i])
	el1.click()

	# dr.implicitly_wait(30)
	# time.sleep(20)
	
	for j in passw:
		el = dr.find_element_by_xpath(numbers[j])
		el.click()

	el6 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/login_button")
	el6.click()

def logout():
	option = dr.find_element_by_xpath('//android.widget.ImageView[@content-desc="More options"]')
	option.click()

	logout = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
	logout.click()

	time.sleep(5)
	dr.back()

def billPay():
	bill_pay_value = 0
	try:
		bill_pay = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView")
		bill_pay.click()
		elec()
		bill_pay_value = 1
	except:
		logout()
		bill_pay_value=0

	return bill_pay_value

def elec():
	elec_value = 0
	try:
		elec = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/image_electricity")
		elec.click()
		time.sleep(2)
		if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.EditText"):
			return
		else:
			back()
			x = billPay()
	except:
		dr.back()
		time.sleep(5)
		x = billPay()

def descr(k):
	description = df.iloc[k]['Description']
	string = description.split(" ")
	distributor = ""
	for i in range(0, len(string)-1):
		distributor+=string[i]+" "

	return distributor

def k_number(k):
	k_num = str(df.iloc[k]['K Number'])
	k_num = k_num.split('.')[0]
	return k_num


def distributor_func(k):
	dist_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.EditText")
	dist_name.send_keys(descr(k))
	dist_name.click()
	time.sleep(5)
	operator = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View[2]")
	operator.click()

def k_number_input(k):
	k_num_input = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[2]/android.widget.EditText")
	k_num_input.send_keys(k_number(k))

	confirm = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[3]/android.widget.Button")
	confirm.click()
	time.sleep(10)

def back():
	dr.back()
	time.sleep(0.5)
	dr.back()
	time.sleep(0.5)
	dr.back()
	

def pay_now_page(k):
	biller_name = df.iloc[k]['Biller Name']
	amount_csv = df.iloc[k]['Amount']
	print("Pay now page")
	time.sleep(5)
	customer_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[3]").text
	amount = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.widget.EditText").text
	print("touch action")
	amount=str(amount)
	amount = amount.split('.')[0]

	touch = TouchAction(dr)
	touch.press(x=486, y=765)   
	touch.move_to(x=486, y=396)
	touch.wait(0.01)
	touch.release()
	touch.perform()
	print("done sliding")

	# time.sleep(5)

	x = 0
	if biller_name == customer_name:
		print(amount)
		print(amount_csv)
		print(type(amount))
		print(type(amount_csv))
		print(int(amount))
		print(int(amount_csv))
		if str(amount) == str(amount_csv):
			pay_now = dr.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[7]/android.widget.Button")
			pay_now.click()
			print("passed pay button")
			time.sleep(10)
			x = 1
			return [1, customer_name, amount]

	if x == 0:
		return [0, customer_name, amount]


for k in range(1,4):
	print("Start")
	# description = df.iloc[k]['Description']
	# k_num = str(df.iloc[k]['K Number'])
	# string = description.split(" ")
	# distributor = ""
	# for i in range(0, len(string)-1):
	# 	distributor+=string[i]+" "

	passw = None
	passw = passwords[i]
	# el1 = dr.find_element_by_xpath(apps[i])
	# el1.click()

	# # dr.implicitly_wait(30)
	# # time.sleep(20)
	
	# for j in passw:
	# 	el = dr.find_element_by_xpath(numbers[j])
	# 	el.click()

	# el6 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/login_button")
	# el6.click()

	# time.sleep(10)

	# dr.implicitly_wait(30)
	x = 0
	while(1):
		login(passw)

		# try:
		# 	el2 = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/buttonNegative")
		# 	el2.click()
		# except:
		# 	pass
		time.sleep(5)

		x = billPay()
		if x==1:
			break

	distributor_loop = 1
	lis = []
	while(1):
		if x==0:
			elec()
		while(1):
		    distributor_func(k)
		    k_number_input(k)
		    break
		    # if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View/android.widget.TextView"):
		    # 	thewriter.writerow({'Sno':df.iloc[k]['Sno'], 'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Not paid", 'File Name':""})
		    # 	k=k+1
		    # else:
		    # 	break

		try:
			if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[1]"):
				lis = pay_now_page(k)
				if lis[0] == 0:
					distributor_loop = 0
				elif lis[0] == 1:
					distributor_loop = 1
				
				break

		except:
			oops = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]")
			cont = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.widget.Button")
			cont.click()
			time.sleep(5)
			back()
			x = billPay()
			continue

	if distributor_loop == 0:
		continue



	# time.sleep(5)
                                                       
	# try:
	# 	bill_pay = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView")
	# 	bill_pay.click()
	# except:
	# 	logout()
	# 	continue
	# time.sleep(5)

	# dr.implicitly_wait(45)

	# elec = dr.find_element_by_id("com.enstage.wibmo.hdfc:id/image_electricity")
	# elec.click()


	# time.sleep(20)

	# dr.implicitly_wait(30)

	# dist_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.EditText")
	# dist_name.send_keys(distributor)
	# dist_name.click()
	# time.sleep(5)
	
	# operator = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View[2]")
	# operator.click()

	# k_num_input = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[2]/android.widget.EditText")
	# k_num_input.send_keys(k_num)

	# confirm = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[3]/android.widget.Button")
	# confirm.click()

	# dr.implicitly_wait(30)

	# print("Pay now page")
	# time.sleep(5)

	# touch = TouchAction(dr)
	# touch.press(x=303, y=1302)
	# touch.move_to(x=282, y=444)
	# touch.release()
	# touch.perform()
	# print("done sliding")
	# time.sleep(5)


	# pay_now = dr.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[7]/android.widget.Button")
	# # actions = ActionChains(dr)
	# # actions.move_to_element(pay_now).perform()
	# # time.sleep(5)
	# pay_now.click()
	# print("passed pay button")
	# # time.sleep(20)

	card_no = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
	card_no.send_keys("5405-2900-0122-9019")

	ex_month = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText")
	ex_month.send_keys("05")

	ex_year = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
	ex_year.send_keys("2025")

	holder_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
	holder_name.send_keys("SANJAY JANGID")

	promocode = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[5]")
	promocode.click()
	time.sleep(1)
	enter_pcode = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
	enter_pcode.send_keys("billpay")

	apply_but = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[3]")
	apply_but.click()

	time.sleep(3)

	approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
	approve.click()

	# time.sleep(5)
	# approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
	# approve.click()

	time.sleep(15)

	# pin = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[5]/android.view.View/android.view.View[2]/android.widget.EditText")
	# pin.send_keys("982802")
	# time.sleep(3)
	# submit = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[7]/android.widget.Button[1]")
	# submit.click()







	# cross = dr.find_element_by_xpath('//android.widget.TextView[@content-desc="Close"]')
	# cross.click()

	# # time.sleep(5)

	# yes = dr.find_element_by_id("android:id/button1")
	# yes.click()

	# # time.sleep(5)

	# other = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[9]")
	# other.click()

	# dr.back()
	# print("driver is closed")
	print("options")

	# logout()

	i=i+1
	if i==3:
		i=1
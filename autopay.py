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
#                my     5        6      2       3
# passwords = ['5126','9389', '1234', '0616', '9828']
passwords = ['5126', '0616', '9828', '9389', '1234']


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

apps = ["/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView[1]",
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView",
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.ImageView[1]",
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageView[1]",
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageView"]

app_index=0

data = pd.read_csv('New_Bill.csv') 
# data = pd.read_excel(r'01_04-05-21_40355_61_JDP.xlsx')
# df = pd.DataFrame(data, columns=['Description', 'Biller Name', 'K Number', 'Amount'])
df = pd.DataFrame(data)
length = len(df.index)

file = open('Sheet1_updated.csv', 'w')
fieldnames = ['Sno', 'Due Date', 'Description', 'Biller Name', 'K Number', 'Amount', 'Status', 'Reason', 'Biller name on bill', 'Amount on bill','Reference no.','App no.']
thewriter = csv.DictWriter(file, fieldnames=fieldnames)
thewriter.writeheader()


i=1
dr = webdriver.Remote('http://localhost:4723/wd/hub', dcs[0])

dr.implicitly_wait(20)

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
	time.sleep(8)

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
	time.sleep(3)
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
		# print(amount)
		# print(amount_csv)
		# print(type(amount))
		# print(type(amount_csv))
		# print(int(amount))
		# print(int(amount_csv))
		if str(amount) == str(amount_csv):
			pay_now = dr.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[7]/android.widget.Button")
			pay_now.click()
			print("passed pay button")
			time.sleep(10)
			x = 1
			return [1, customer_name, amount]

	if x == 0:
		return [0, customer_name, amount]


for k in range(0,3):
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

	lis = []
	while(1):
		distributor_loop = 1
		kloop=1
		if x==0:
			elec()
		while(1):
			distributor_func(k)
			while(1):
				k_number_input(k)
				invalid = ""
				try:
					invalid = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View/android.widget.TextView")
				except:
					pass

				if invalid != "":
					print("invalid k number")
					k=k+1
					kloop=0
					thewriter.writerow({'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Not paid", 'Reason':"Wrong K number", 'Biller name on bill':"", 'Amount on bill':"", 'Reference no.':"",'App no.':""})
				break

			break

		if kloop==0:
			dr.back()
			time.sleep(0.3)
			dr.back()
			x=0
			continue

		try:
			if dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[1]"):
				lis = pay_now_page(k)
				if lis[0] == 0:
					distributor_loop = 0
				elif lis[0] == 1:
					distributor_loop = 1

		except:
			oops = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]")
			cont = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.widget.Button")
			cont.click()
			time.sleep(5)
			back()
			x = billPay()
			continue

		if distributor_loop == 0:
			thewriter.writerow({'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Not paid", 'Reason':"Either biller name or amount does not match", 'Biller name on bill':lis[1], 'Amount on bill':lis[2], 'Reference no.':"",'App no.':""})
			k=k+1
			x=0
			dr.back()
			time.sleep(0.3)
			dr.back()
			time.sleep(1)
			continue
		else:
			break



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

	# print(dr.page_source)

	# time.sleep(5)

	# dr.back()

	# promocode = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[5]")
	# promocode.click()
	# time.sleep(1)
	# enter_pcode = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
	# enter_pcode.send_keys("billpay")

	# apply_butt = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[3]")
	# apply_butt.click()

	# time.sleep(5)

	try:
		edit_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView")
		edit_card.click()

		time.sleep(3)


		card_alias = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
		card_alias.send_keys("SANJAY")

		card_no = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
		card_no.send_keys("4205-8060-0614-7016")

		ex_month = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText")
		ex_month.send_keys("06")

		ex_year = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[2]")	
		ex_year.send_keys("2025")

		holder_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText[3]")
		holder_name.send_keys("SANJAY JANGID")

		add_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
		add_card.click()

		# time.sleep(3)

		# approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
		# approve.click()

	except:
		card_no = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
		card_no.send_keys("4205-8060-0614-7016")

		ex_month = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText")
		ex_month.send_keys("06")

		ex_year = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
		ex_year.send_keys("2025")

		holder_name = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText[2]")
		holder_name.send_keys("SANJAY JANGID")

		# print(dr.page_source)

		# print("Approve")

		approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
		approve.click()

		time.sleep(5)
		approve = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[7]")
		approve.click() 


	print("Pin page")
	time.sleep(15)


	pin = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[5]/android.view.View/android.view.View[2]/android.widget.EditText")
	pin.send_keys("982802")
	time.sleep(3)
	submit = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[6]/android.view.View[7]/android.widget.Button[1]")
	submit.click()

	time.sleep(30)

	transac = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View").text

	thewriter.writerow({'Due Date':df.iloc[k]['Due Date'],	'Description':df.iloc[k]['Description'], 'Biller Name':df.iloc[k]['Biller Name'], 'K Number':df.iloc[k]['K Number'],'Amount':df.iloc[k]['Amount'],	'Status': "Paid", 'Reason':"", 'Biller name on bill':lis[1], 'Amount on bill':lis[2], 'Reference no.':str(transac),'App no.':i})
	dr.back()
	time.sleep(0.3)
	dr.back()

	# cancel = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[6]")
	# cancel.click()

	# edit_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView")
	# edit_card.click()

	# time.sleep(5)

	navigate_up = dr.find_element_by_accessibility_id("Navigate up")
	navigate_up.click()

	time.sleep(5)

	# print(dr.page_source)

	linked_cards = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.TextView")
	linked_cards.click()

	time.sleep(5)

	delete_card = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[3]")
	delete_card.click()

	time.sleep(5)

	yes = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
	yes.click()

	time.sleep(7)

	cross = dr.find_element_by_xpath('//android.widget.TextView[@content-desc="Close"]')
	cross.click()

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

	# i=i+1
	# if i==5:
	# 	i=1
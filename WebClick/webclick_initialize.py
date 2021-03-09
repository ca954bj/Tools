import time
# importing webdriver from selenium
from selenium import webdriver

# Here Firefox will be used
driver = webdriver.Firefox()

# URL of website
#url = "https://www.geeksforgeeks.org/"
url = "http://mir.com/setup/missions"

# class editbutton
# data-element-id missionsoverview
# data-guid 6fd1b64e-7d6f-11eb-9c5e-94c691a3e366
# xpath /html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div[68]/div[5]

# class settingsicon
# data-element-id missionview
# data-item-id missions_missionview_missionview_action_0

# Opening the website
driver.get(url)

# get the button by xpath
driver.find_element_by_xpath('''//*[@id="login_username"]''').send_keys("distributor")
driver.find_element_by_xpath('''//*[@id="login_password"]''').send_keys("distributor")
driver.find_element_by_xpath('''//*[@id="submit"]''').click()
time.sleep(2)

print("click setup")
driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[2]/div").click()
time.sleep(1)

print("click mission")
driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/ul/li[1]/a/span").click()
time.sleep(2)

print("edit trial")
driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div[68]/div[5]").click()
time.sleep(1)

print("begin editing data")
driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[3]/ul/li/div/div[5]").click()
time.sleep(1)

def edit_and_run(distancex, distancey, angle):
	# here is the mission panel
	t0 = time.clock()

	# edit x
	driver.find_element_by_name('''missionview_missionview_settingspanel_field_x''').clear()
	distancex = str(distancex)
	driver.find_element_by_name('''missionview_missionview_settingspanel_field_x''').send_keys(distancex)
	
	# edit y
	driver.find_element_by_name('''missionview_missionview_settingspanel_field_y''').clear()
	distancey = str(distancey)
	driver.find_element_by_name('''missionview_missionview_settingspanel_field_y''').send_keys(distancey)
	
	# edit orientation
	driver.find_element_by_name('''missionview_missionview_settingspanel_field_orientation''').clear()
	angle = str(angle)
	driver.find_element_by_name('''missionview_missionview_settingspanel_field_orientation''').send_keys(angle)
	
	# save
	driver.find_element_by_name("missionview_missionview_settingspanel_field_setbutton").click()
	time.sleep(0.5)
	driver.find_element_by_xpath('''/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div''').click()
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/a").click()
	time.sleep(2)

	# here is the mission panel
	print("Run")
	driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div[68]/div[3]").click()
	t1 = time.clock()
	print("Time: %f" % (t1 - t0))
	
	print("edit trial")
	driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div[68]/div[5]").click()
	time.sleep(1)

	print("begin editing data")
	driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[3]/ul/li/div/div[5]").click()
	time.sleep(1)

edit_and_run(0, 0, 10)
edit_and_run(0, 0, -20)
edit_and_run(0, 0, 20)
edit_and_run(0, 0, -10)
edit_and_run(0, 0, 5)
edit_and_run(0, 0, -5)

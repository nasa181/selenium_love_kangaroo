from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import numpy as np



proxy_index = 0
list_free_proxy = [
					
				]
proxy_index_length = len(list_free_proxy)

red_key = np.array([
				['MAZD10AA','MAZD14AF','MAZD16BJ'],
				['MAZD10AK','MAZD14AL','MAZD16AB'],
				['BMW 10AG','BMW 14AD','BMW 16BM'],
				['AUDI14AM','AUDI16AA'],
				['HOND10AE','HOND14AA','HOND16BS'],
				['NISS14AI','NISS16AU'],
				['TOYO10BY','TOYO14BB','TOYO16BS'],
				['HOND16CH'],
				['MERC14BT','MERC16AQ'],
				['TOYO10AA','TOYO14AU','TOYO16CD'],
				['HOND10AW','HOND14BA','HOND16AP'],
				['HOND10BC','HOND14BL','HOND16AJ'],
				['MAZD16AH'],
				['MAZD14AR','MAZD16AN'],
				['ISUZ10AA','ISUZ14BD','ISUZ16AB'],
				['ISUZ14BD','ISUZ16AB'],
				['TOYO10BE','TOYO14AB','TOYO16BF'],
				['TOYO16EH'],
				['HOND14CY','HOND16BZ'],
				['HOND10AL','HOND14BH','HOND16BH'],
				['MITS10AG','MITS14AP','MITS16AF']
		])

list_car_brand = ['Mazda','Mazda','BMW','Audi','Honda','Nissan','Toyota','Honda','Mercedes-Benz','Toyota','Honda','Honda','Mazda','Mazda','Isuzu','Toyota','Toyota','Honda','Honda','Mitsubishi']
list_car_model = ['2','3','320d','A3','Accord','Almera','Corolla Altis','BR-V','C300','Camry','Civic','CR-V','CX-3','CX-5','D-Max','Fortuner','Hilux Revo','HR-V','Jazz','Pajero Sport']
list_car_desc = np.array([
					['Auto / 1.5 / R','Auto / 1.5 / Elegance Groove','Auto / 1.3 / High'],
					['Auto / 1.6 / Groove','Auto / 1.6 / Groove','Auto / 2.0 / C'],
					['Auto / 2.0 / E90','Auto / 2.0 / F30','Auto / 2.0 / F30'],
					['Auto / 1.4 / Limousine','Auto / 1.4 / Limousine'],
					['Auto / 2.0 / MY08 E i-VTEC','Auto / 2.0 / MY13 EL i-VTEC','Auto / 2.0 / MY13 EL i-VTEC'],
					['Manual / 1.2 / S','Manual / 1.2 / S'],
					['Auto / 2.0 / V','Auto / 1.6 / G','Auto / 1.8 / E'],
					['Auto / 1.5 / V'],
					['Auto / 2.1 / W205 Blue TEC HYBRID AMG Dynamic / SEDAN','Auto / 2.1 / W205 Blue TEC HYBRID AMG Dynamic / WAGON'],
					['Auto / 2.0 / E','Auto / 2.0 / G','Auto / 2.0 / G'],
					['Auto / 1.8 / MY10 S i-VTEC','Auto / 1.8 / FB S i-VTEC','Auto / 1.8 / FB S i-VTEC'],
					['Auto / 2.0 / MY10 S','Auto / 2.0 / MY12 S','Auto / 2.0 / MY15 S'],
					['Auto / 2.0 / E'],
					['Auto / 2.0 / S','Auto / 2.0 / S'],
					['Auto / 3.0 / Hi-Lander Super Platinum','Manual / 2.5 / Chassis','Manual / 1.9 / S / 2 doors'],
					['Manual / 2.5 / Chassis','Manual / 1.9 / S / 2 doors'],
					['Manual / 3.0 / G','Manual / 2.5 / G','Manual / 2.4 / G'],
					['Auto / 2.4 / Prerunner E / 4 doors'],
					['Auto / 1.8 / E','Auto / 1.8 / S'],
					['Auto / 1.5 / S i-VTEC','Auto / 1.5 / S i-VTEC','Auto / 1.5 / S i-VTEC'],
					['Auto / 2.5 / GLS','Auto / 2.5 / GLS','Auto / 2.4 / GLS LTD']
				])
range_for_waiting = 300000
sleep_time = 2 #second
list_cm_sex = ['sex2d2ms','sex2d2fs']
list_sex = ['M','F']
list_car_make_year = np.array([
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2016 (2559)'],
						['2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2016 (2559)'],
						['2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2016 (2559)'],
						['2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)'],
						['2010 (2553)','2014 (2557)','2016 (2559)']
					])
list_cm_age = ['1982 (2525)','1972 (2515)','1962 (2505)']
list_age = ['35','45','55']
is_cm_man = True
birth_date = '1'
birth_month = 'มกราคม'
birth_month_abb = 'ม.ค.'
first_loop = True
# ====== create file to append data at the end of each loop ======
# f = open('roojai_data.csv','w')
# f.write('')
# f.close()
# ================================================================
# driver = webdriver.Chrome()
for i in range(len(list_car_brand)):
	for j in range(len(list_car_make_year[i])):
		for k in range(len(list_cm_age)):
			for x in range(len(list_cm_sex)):
				
				find_thing = ''
				chrome_options = ''
				driver = ''
				while len(find_thing) == 0:	
					chrome_options = webdriver.ChromeOptions()
					chrome_options.add_argument('--proxy-server=%s' % list_free_proxy[proxy_index])
					proxy_index = (proxy_index + 1)%proxy_index_length
					driver = webdriver.Chrome(chrome_options=chrome_options)
					driver.get("https://hide.me/en/check")
					find_thing = driver.find_elements_by_partial_link_text('Check again')
					if len(find_thing) == 0:
						driver.close()

				driver.get("https://insure.roojai.com/#/quotationInputB")

				# ==============================================================================================

				elem = driver.find_element_by_id('button-car-brand') # Select Car Brand (Car Make) 
				elem.click()
				time.sleep(sleep_time)
				make = driver.find_element_by_partial_link_text(list_car_brand[i]).click() # select element in drop down
				# if not first_loop:
				# 	time.sleep(sleep_time)
				# 	driver.execute_script("window.scrollTo(0,200);") # scroll up to nealy top
				# 	time.sleep(sleep_time)

				# ==============================================================================================
				
				elem = driver.find_element_by_id('button-car-model') # Select Car Model
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				model = driver.find_element_by_partial_link_text(list_car_model[i]).click() # select element in drop down
				# if not first_loop:
				# 	time.sleep(sleep_time)
				# 	driver.execute_script("window.scrollTo(0,200);") # scroll up to nealy top
				# 	time.sleep(sleep_time)

				# ==============================================================================================

				elem = driver.find_element_by_id('button-car-year') # Select Car Year
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				car_age = driver.find_element_by_partial_link_text(list_car_make_year[i][j]).click() # select element in drop down
				# if not first_loop:
				# 	time.sleep(sleep_time)
				# 	driver.execute_script("window.scrollTo(0,200);") # scroll up to nealy top
				# 	time.sleep(sleep_time)

				# ==============================================================================================

				elem = driver.find_element_by_id('button-car-desc') # Select Car Desc
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				car_desciption = driver.find_element_by_partial_link_text(list_car_desc[i][j]).click() # select element in drop down

				# ==============================================================================================

				time.sleep(sleep_time)
				elem = driver.find_element_by_id(list_cm_sex[x]) # Select CM_SEX
				time.sleep(sleep_time)
				elem.click()

				# ==============================================================================================

				elem = driver.find_element_by_id('D2date4select') # Select birth date
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				cm_date = driver.find_element_by_partial_link_text(birth_date).click() # select element in drop down

				# ==============================================================================================

				elem = driver.find_element_by_id('button-birth-month') # Select birth month
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				cm_month = driver.find_element_by_partial_link_text(birth_month) # select element in drop down
				if cm_month:
					cm_month.click()
				else:
					cm_month = driver.find_element_by_partial_link_text(birth_month_abb) # select element in drop down
					cm_month.click()
				# ==============================================================================================

				elem = driver.find_element_by_id('button-birth-year') # Select birth_year
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				cm_year = driver.find_element_by_partial_link_text(list_cm_age[k]).click() # select element in drop down
				
				# ==============================================================================================
				# if first_loop:
				elem = driver.find_element_by_id('exp2answer4v6') # Select DRV EXP
				time.sleep(sleep_time)
				elem.click()

				# ==============================================================================================

				
				elem = driver.find_element_by_id('acc2answer4zero') # Select Num Claim
				time.sleep(sleep_time)
				elem.click()

				# ==============================================================================================

				elem = driver.find_element_by_id('pk2drive2shop1') # Select Personal Drive
				time.sleep(sleep_time)
				elem.click()

				# ==============================================================================================

				elem = driver.find_element_by_id('ncb2answer4two') # Select NCB PCT
				time.sleep(sleep_time)
				elem.click()

				# ==============================================================================================

				elem = driver.find_element_by_id('camera02') # Select CCTV
				time.sleep(sleep_time)
				elem.click()
				# else:
				# 	time.sleep(sleep_time)
				# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to buttom
				# 	time.sleep(sleep_time)

				# ==============================================================================================

				elem = driver.find_element_by_id('rj-qp-buynow') # Select Commit
				time.sleep(sleep_time)
				elem.click()

				# ==============================================================================================

				# # ///////////// checking if mailing me pop up //////////////
				# elem = driver.find_element_by_id('cancelCallMe')
				# for i in range(range_for_waiting): # For waiting async
				# 	print('wainting for async')
				# if elem:
				# 	elem.click()
				# # //////////////////////////////////////////////////////////

				wait = WebDriverWait(driver, 10)
				try:
					wait.until(EC.visibility_of_element_located((By.ID, 'btnCustomizePlan'))) # wait until customize button exist
				except:
					driver.close()
				elem = driver.find_element_by_id('btnCustomizePlan') # Select Costomize plan
				elem.click()

				# ==============================================================================================
				
				# # ///////////// checking if mailing me pop up //////////////
				# elem = driver.find_element_by_id('cancelCallMe')
				# for i in range(range_for_waiting): # For waiting async
				# 	print('wainting for async')
				# if elem:
				# 	elem.click()
				# # //////////////////////////////////////////////////////////
				
				# ////////
				# V1 price
				# garage
				# ////////
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2excess0') # Select no excess
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2workshop1') # Select garage
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				driver.execute_script("window.scrollTo(0, 100);") # scroll down a bit
				time.sleep(sleep_time)

				elem = driver.find_element_by_id('pk2drive1') # Select not desc
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				
				elem = driver.find_element_by_xpath('//button[@id="pk2drive1no"]') # no driver younger than main driver
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)

				elem = driver.find_element_by_id('pkbuycom2') # Select not buy 'act of legislation'
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to buttom
				time.sleep(sleep_time)
				elem = driver.find_element_by_xpath("//button[@data-target='#table2display']") # Select show to table button
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				sum_insV1g = driver.find_element_by_id('sumInsured1')
				sum_insV1g = ''.join(re.findall(r'\d+',sum_insV1g.text))
				premiumV1g= driver.find_element_by_id('h3price4year') # find the price digit
				premiumV1g = (float(''.join(re.findall(r'\d+',premiumV1g.text))))/100
				print(sum_insV1g,',',premiumV1g)

				# ==============================================================================================
				# ////////
				# V1 price
				# Dealer
				# ////////
				if list_car_make_year[i][j] != '2010 (2553)':
					driver.execute_script("window.scrollTo(0,-1 * document.body.scrollHeight);") # scroll up to top
					time.sleep(sleep_time)
					elem = driver.find_element_by_id('pk2workshop2') # Select dealer
					time.sleep(sleep_time)
					elem.click()
					time.sleep(sleep_time)
					driver.execute_script("window.scrollTo(0, 200);") # scroll down a bit
					time.sleep(sleep_time)
					sum_insV1d = driver.find_element_by_id('sumInsured1')
					sum_insV1d = ''.join(re.findall(r'\d+',sum_insV1d.text))
					premiumV1d = driver.find_element_by_id('h3price4year') # find the price digit
					premiumV1d = (float(''.join(re.findall(r'\d+',premiumV1d.text))))/100
					print(sum_insV1d,',',premiumV1d)

				# ==============================================================================================
				# ////////
				# V52 price
				# garage
				# ////////

				# elem = driver.find_element_by_id('pkbuycom2') # Select not buy 'act of legislation'
				driver.execute_script("window.scrollTo(0,-1 * document.body.scrollHeight);") # scroll up to top
				elem = driver.find_element_by_id('pk-cover2plus') # Select V52
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2workshop1') # Select garage
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				driver.execute_script("window.scrollTo(0, 200);") # scroll down a bit
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2drive4') # Select not desc
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				driver.execute_script("window.scrollTo(0, 200);") # scroll down a bit
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pkbuycom2') # Select not buy 'act of legislation'
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				######################
				sum_insV52g = driver.find_element_by_id('sumInsured1')
				sum_insV52g = ''.join(re.findall(r'\d+',sum_insV52g.text))
				premiumV52g = driver.find_element_by_id('h3price4year') # find the price digit
				premiumV52g = (float(''.join(re.findall(r'\d+',premiumV52g.text))))/100
				print(sum_insV52g,',',premiumV52g)

				# ==============================================================================================

				# ////////
				# V52 price
				# Dealer
				# ////////
				driver.execute_script("window.scrollTo(0,-1 * document.body.scrollHeight);") # scroll up to top
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2workshop2') # Select Dealer
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				driver.execute_script("window.scrollTo(0, 300);") # scroll down a bit
				time.sleep(sleep_time)
				sum_insV52d = driver.find_element_by_id('sumInsured1')
				sum_insV52d = ''.join(re.findall(r'\d+',sum_insV52d.text))
				premiumV52d = driver.find_element_by_id('h3price4year') # find the price digit
				premiumV52d = (float(''.join(re.findall(r'\d+',premiumV52d.text))))/100
				print(sum_insV52d,',',premiumV52d)

				# ==============================================================================================

				# ////////
				# V53 price
				# garage
				# ////////
				elem = driver.find_element_by_id('pk-other') # Select another plan
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk-cover3plus') # Select V53
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2workshop1') # Select garage
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2drive4') # Select not desc
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pkbuycom2') # Select not buy 'act of legislation'
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				sum_insV53g = driver.find_element_by_id('sumInsured1')
				sum_insV53g = ''.join(re.findall(r'\d+',sum_insV53g.text))
				premiumV53g = driver.find_element_by_id('h3price4year') # find the price digit
				premiumV53g = (float(''.join(re.findall(r'\d+',premiumV53g.text))))/100
				print(sum_insV53g,',',premiumV53g)

				# ==============================================================================================

				# ////////
				# V53 price
				# Dealer
				# ////////
				driver.execute_script("window.scrollTo(0,-1 * document.body.scrollHeight);") # scroll up to top
				elem = driver.find_element_by_id('pk-other') # Select another plan
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				driver.execute_script("window.scrollTo(0,100);") # scroll down a bit
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk-cover3plus') # Select V53
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2workshop2') # Select dealer
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pk2drive4') # Select not desc
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				elem = driver.find_element_by_id('pkbuycom2') # Select not buy 'act of legislation'
				time.sleep(sleep_time)
				elem.click()
				time.sleep(sleep_time)
				sum_insV53d = driver.find_element_by_id('sumInsured1')
				sum_insV53d = ''.join(re.findall(r'\d+',sum_insV53d.text))
				premiumV53d = driver.find_element_by_id('h3price4year') # find the price digit
				premiumV53d = (float(''.join(re.findall(r'\d+',premiumV53d.text))))/100
				print(sum_insV53d,',',premiumV53d)

				# ========================================================================================================================================================================================================================================================================================================================================================================================
				print(list_car_brand[i],',',list_car_model[i],',',list_cm_age[k],',',list_cm_sex[x],',',sum_insV1g,',',premiumV1g,',',sum_insV52g,',',premiumV52g,',',sum_insV53g,',',premiumV53g)
				if list_car_make_year[i][j] != '2010 (2553)':
					print(list_car_brand[i],',',list_car_model[i],',',list_cm_age[k],',',list_cm_sex[x],',',sum_insV1d,',',premiumV1d,',',sum_insV52d,',',premiumV52d,',',sum_insV53d,',',premiumV53d)
				first_loop = False
				proxy_index = (proxy_index + 1)%proxy_index_length
				driver.close()

				# garage
				f = open('roojai_data_version2.csv','a')
				f.write(red_key[i][j] + ',' + list_car_brand[i] + ',' + list_car_model[i] + ',' + list_car_make_year[i][j] + ',' + 'GARAGE' + ',' + list_age[k] + ',' + list_sex[x] + ',' + 'Roojai' + ',' + str(sum_insV1g) + ',' + str(premiumV1g) + ',' + str(sum_insV52g) + ',' + str(premiumV52g) + ',' + str(sum_insV53g) + ',' + str(premiumV53g) + ',' + 'V52,V53 including deductable' + '\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				# dealer
				f.write(red_key[i][j] + ',' + list_car_brand[i] + ',' + list_car_model[i] + ',' + list_car_make_year[i][j] + ',' + 'DEALER' + ',' + list_age[k] + ',' + list_sex[x] + ',' + 'Roojai' + ',')
				if list_car_make_year[i][j] != '2010 (2553)':
					f.write(str(sum_insV1d) + ',' + str(premiumV1d) + ',')
				else:
					f.write(','+',')
				f.write(str(sum_insV52d) + ',' + str(premiumV52d) + ',' + str(sum_insV53d) + ',' + str(premiumV53d) + ',' + 'V52,V53 including deductable' + '\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				f.write('\n')
				# ========================================================================================================================================================================================================================================================================================================================================================================================
print('crawler task completed')
driver.close()

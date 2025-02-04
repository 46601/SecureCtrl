from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.by import By
import time
import os
desired_capabilities={
      "platformName": "Android",
      "appium:platformVersion": "13.0",
      "appium:deviceName": "Central's F14",
      "appium:app": "D:\\Secure_Controls.apk",
      "appium:GrantPermission": True,
      "appium:appWaitForLaunch": False,
      "appium:interactiveDebugging": True,
      "appium:autoGrantPermissions": True
}
#learning Git Commands

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
time.sleep(4)


ID = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/email")
ID.send_keys("harshil.jain@securemeters.com")
Pass= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/password")
Pass.send_keys("secure@123")
Show_Pass= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tvShowPassword")
Show_Pass.click()
Hide= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tvShowPassword")
Hide.click()
SignIn= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/btnSignIn")
SignIn.click()

print("login successful")

time.sleep(10)
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'Login'+".png")
user= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/signUp_user")
user.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'Userselection'+".png")
print("User selected")
time.sleep(30)
adddevice= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/floating_add_button")
adddevice.click()
time.sleep(30)
scan= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/btnContinue")
scan.click()
time.sleep(5)
details= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/lnk_enter_manually")
details.click()
time.sleep(5)
Sno= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/enter_serial_number")
Sno.send_keys("H0000354")
macAdd= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/enter_mac_id")
macAdd.send_keys("0C:EC:80:23:5F:10")
channel= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/four_channel")
channel.click()
channel.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'details'+".png")
print('device details entered successfully')
time.sleep(5)
Next= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/alert_done")
Next.click()
time.sleep(5)
contin= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/btnContinue")
contin.click()
time.sleep(7)
contini = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/btnContinue")
contini.click()
time.sleep(10)
retainuser= driver.find_element(by=AppiumBy.ID, value="android:id/button1")
retainuser.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'user retained'+".png")
print("user retained")
time.sleep(50)
print("commissioning successful")

driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'commissiomning done'+".png")
tempChange = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/current_temp")
tempChange.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'temperature changed'+".png")
print("temperature changed")
time.sleep(20)
hold = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/untill_textbox")
hold.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'hold success'+".png")
print("Hold success")
time.sleep(5)
untilCancell = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
untilCancell.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'hold untill cancell successful'+".png")
print("hold untill cancell successful")
time.sleep(30)
cancellHold= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/start_now")
cancellHold.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'cancell & hold'+".png")
print("cancell hold done")
time.sleep(25)
# Start= driver.find_element(by=AppiumBy.ID, value="c20om.secure.heatConnect:id/start_now")
# Start.click()
# time.sleep(5)
radiobtn = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]")
radiobtn.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'hot_water_action'+".png")
print("hot water actions working started")
time.sleep(10)
Boost1= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/boost_1_hr")
Boost1.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'hotwater boost'+".png")
print('hotwater boost for 1 hr on')
time.sleep(15)
Boost2= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/boost_2_hr")
Boost2.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'Booston'+".png")
print("boost for 2 hr on")
time.sleep(10)
CancelB= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/boost_cancel")
CancelB.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'cancelledBoost'+".png")
print("cancelled boost")
time.sleep(15)
editSchedule= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/edit_schedule_button")
editSchedule.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'edtschdule'+".png")
print("edit schedule started")
time.sleep(5)
exisingSchd= driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
exisingSchd.click()
time.sleep(5)
Cross= driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView")
Cross.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'scheduleDelete'+".png")
print("delete existing schedule")
time.sleep(5)
remove= driver.find_element(by=AppiumBy.ID, value="android:id/button1")
remove.click()
time.sleep(5)
addPeriod= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/add_slot")
addPeriod.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'add period'+".png")
print("add period done")
time.sleep(5)
timeSelect = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[1]/android.widget.Button[2]")
timeSelect.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'TimeChange'+".png")
print("time change")
time.sleep(5)
OffOn= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/hot_water_on_off")
OffOn.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'HotWaterOn/Off'+".png")
print("hot water Turned on/off")
time.sleep(5)
save= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/hide_dialog")
save.click()
time.sleep(5)
copyy= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/copy_schedule")
copyy.click()
time.sleep(5)
DaySelect= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tuesday_check")
DaySelect.click()
DaySelect.click()
time.sleep(5)
Save = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/hide_dialog")
Save.click()
time.sleep(5)
DaySelect2 = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/copy_schedule")
DaySelect2.click()
time.sleep(5)
friday= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/friday_check")
friday.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'CopyingShedule'+".png")
print("copying schedule successful")
time.sleep(5)
SSave = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/hide_dialog")
SSave.click()
time.sleep(10)
backk= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/activity_save")
backk.click()
time.sleep(35)
BackB= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
BackB.click()
time.sleep(40)
tempScreen= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
tempScreen.click()
time.sleep(30)
# Backkk= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
# Backkk.click()
# time.sleep(20)
HotWater= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/boost_text")
HotWater.click()
time.sleep(20)
Backbu= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
Backbu.click()
time.sleep(20)
Refresh= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/refresh")
Refresh.click()

print('refresh button for syncing done')
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'RefreshButton'+".png")
time.sleep(30)
notification= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Notification")
notification.click()
print("notification checked")
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'notifications'+".png")
time.sleep(5)
Beck= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
Beck.click()
time.sleep(5)
Settings= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Setting")
Settings.click()
time.sleep(5)
AwayTem= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/show_away_temp")
AwayTem.click()
time.sleep(5)
ChangeTemp= driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.NumberPicker/android.widget.Button[1]")
ChangeTemp.click()
time.sleep(5)
Savve= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/hide_dialog_away_temp")
Savve.click()
print("away temp hanged successfully")
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'AwayTemp'+".png")
time.sleep(30)
optStartStop= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/text_optimum_start")
optStartStop.click()
time.sleep(5)
uncheck = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/zone1")
uncheck.click()
time.sleep(10)
check = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/zone1")
check.click()
time.sleep(10)
uncheckk = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/zone5")
uncheckk.click()
print("optimum start /stop working fine ")
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'OptimumStartStop'+".png")
time.sleep(10)
Checkkk= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/zone5")
Checkkk.click()
time.sleep(15)
Backi= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
Backi.click()
time.sleep(10)
Summermode= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/switch_summer_mode")
Summermode.click()
time.sleep(10)
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'SummerModeOn'+".png")
SummerModeOff= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/switch_summer_mode")
SummerModeOff.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'SummeModeoff'+".png")
print("summer mode on/off")
time.sleep(10)
Frostprot= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/show_frost_temperature")
Frostprot.click()
time.sleep(5)
tempChange= driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.NumberPicker/android.widget.Button[1]")
tempChange.click()
time.sleep(5)
TempChange= driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.NumberPicker/android.widget.Button[2]")
TempChange.click()
time.sleep(5)
Savvy= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/hide_dialog")
Savvy.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'FrostProtection'+".png")
print("frost protecton temp changed")
time.sleep(10)
Ecomode= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/eco_btn")
Ecomode.click()
print("economy mode selected")
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'economyMode'+".png")
time.sleep(15)
ComfMode = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/comfort_btn")
ComfMode.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'Comfmode'+".png")
print("comfort mode selected")
time.sleep(15)
Deviceinfo= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/text_system_info")
Deviceinfo.click()
print("device info checked")
driver.save_screenshot("D:/mobileApps/SecureControlsLastSC/"+'deviceInfo'+".png")
time.sleep(5)
BACK= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
BACK.click()
time.sleep(5)
BaCK= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
BaCK.click()
time.sleep(5)
BurgerIcon= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation drawer")
BurgerIcon.click()
time.sleep(10)
editProf = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/edit_profile")
editProf.click()
time.sleep(10)
ChangePass = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_user_password")
ChangePass.click()
time.sleep(5)
oldPass = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/password")
oldPass.send_keys("secure@123")
Showhide = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tvShowPassword")
Showhide.click()
Showhide.click()
NewPass = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/password1")
NewPass.click()
NewPass.send_keys("secure@1234")
ShOW = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tvShowPassword1")
ShOW.click()
ShOW.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'ChangePasss'+".png")
print("change password initiated and checked")
time.sleep(5)
BeACK = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
BeACK.click()
time.sleep(5)
BACkkkk= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
BACkkkk.click()
time.sleep(5)
# el79= driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]")
# el79.click()
# el80 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
# el80.click()
# el81 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation drawer")
# el81.click()
# About = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/hot_water_title")
# About.click()
# time.sleep(5)
# TnC= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_terms_conditions")
# TnC.click()
# print("terms and condition opened")
# driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'T&C'+".png")
# time.sleep(15)
# Byck = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
# Byck.click()
# time.sleep(8)
# privacyP = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_privacy_policy")
# privacyP.click()
# print("Privacy Policy opened")
# time.sleep(10)
aBOUT = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[5]")
aBOUT.click()
time.sleep(5)
tNc = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_terms_conditions")
tNc.click()
time.sleep(5)
driver.back()
pRIVACYpOLICY= driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_privacy_policy")
pRIVACYpOLICY.click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.back()
time.sleep(5)
# Bwck = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
# Bwck.click()
# time.sleep(8)
# Bqck = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
# Bqck.click()
# time.sleep(5)
Burger = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation drawer")
Burger.click()
time.sleep(5)
helpandSupp = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[6]")
helpandSupp.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'Help&Supp'+".png")
print("help and support")
time.sleep(5)
Assistance = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_assistance")
Assistance.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'Assistedlvingchecked'+".png")
print("assistance calling checked")
time.sleep(5)
Bvck = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
Bvck.click()
time.sleep(5)
AppLog = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_email_logs")
AppLog.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'AppLogCreated'+".png")
print("app log file created")
time.sleep(10)
driver.back()
time.sleep(5)
AccDelete = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/tv_delete_account")
AccDelete.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'AccountDelInitiated'+".png")
print("account del initiated")
time.sleep(10)
cancell= driver.find_element(by=AppiumBy.ID, value="android:id/button2")
cancell.click()
time.sleep(4)
Blck = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
Blck.click()
time.sleep(4)
#driver.back()

BIcon = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation drawer")
BIcon.click()
time.sleep(4)
# Logout = driver.find_element(by=AppiumBy.ID, value="com.secure.heatConnect:id/lut")
# Logout.click()
# time.sleep(4)
# LogO = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
# LogO.click()
logout = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[7]")
logout.click()
time.sleep(5)
logoutsucees = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
logoutsucees.click()
driver.save_screenshot('D:/mobileApps/SecureControlsLastSC/'+'Logoff'+".png")
print("logout successful")
print("Secure Control Testing done!")
time.sleep(10)
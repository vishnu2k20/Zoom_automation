import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime,date
import keyboard
import calendar

def sign_in(meetingid,pswd):
    #Opens up the zoom app
    #change the path specific to your computer
    
    #If on windows use below line for opening zoom
    #subprocess.call('C:\\myprogram.exe')
    
    #If on mac / Linux use below line for opening zoom
    subprocess.call(r'C:\Users\Vishnu\AppData\Roaming\Zoom\bin_00\Zoom.exe')

    time.sleep(5)
    print("Zoom Opened")

    
    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('D:\Cloud\OneDrive\Desktop\Zoom-Automation-Python\join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    print("Join button clicked")
    time.sleep(5)

    # Type the meeting ID
    meeting_id_btn = pyautogui.locateCenterOnScreen('D:\Cloud\OneDrive\Desktop\Zoom-Automation-Python\meeting_id_button.png')
    pyautogui.moveTo(604,333)
    pyautogui.click()
    keyboard.write(meetingid)
    pyautogui.press('enter')
    print("Meeting_id entered")
    time.sleep(2)



    # Disables both the camera and the mic
    # media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    # for btn in media_btn:
    #     pyautogui.moveTo(btn)
    #     pyautogui.click()
    #     time.sleep(2)

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('D:\Cloud\OneDrive\Desktop\Zoom-Automation-Python\join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    print("Join meeting pressed")
    time.sleep(2)

    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('D:\Cloud\OneDrive\Desktop\Zoom-Automation-Python\meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    keyboard.write(pswd)
    pyautogui.press('enter')
    print("password entered")

# Reading the file

df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    my_date=date.today()
    day=calendar.day_name[my_date.weekday()].lower()
    if now in str(df["timings"]):
        a=df[df["days"]==day]
        print(a)
        row = a.loc[a['timings'] == now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])
        sign_in(m_id,m_pswd)
        time.sleep(40)
        print('signed in')

#!usr/bin/python3

#Serial imported for Serial communication
import serial 

#Required to use delay functions
import time 

#Required to to perform actions
import pyautogui   

#Create Serial port object called arduinoSerialData
ArduinoSerial = serial.Serial('com15',9600) 
time.sleep(2)					 #wait for 2 seconds for the communication to get established

#read the serial data and print it as line
while 1:
    incoming = str (ArduinoSerial.readline()) 
    print incoming
    
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)

    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right') 

    if 'Volume Incresaed' in incoming:
        pyautogui.hotkey('ctrl', 'down')
        

    if 'Volume Decreased' in incoming:
        pyautogui.hotkey('ctrl', 'up')

    incoming = "";

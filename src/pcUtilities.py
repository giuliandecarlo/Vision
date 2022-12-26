import os
import psutil

def batteryInfo(): #Provide information about battery (percentage and plugged/not-plugged)
    battery=psutil.sensors_battery()
    plugged=battery.power_plugged
    percent=battery.percent
    if plugged is True:
        return("La batteria è in carica, e al momento è al "+str(percent)+" %")
    else:
        return("La batteria non è in carica, e al momento è al "+str(percent)+" %")

def shutdownDevice(): #Shutdown the computer
    os.system("sudo shutdown -h now")

def restartDevice(): #Restart the computer
    os.system("sudo shutdown -r now")
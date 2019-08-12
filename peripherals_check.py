from escpos.printer import Usb
import escpos
import evdev
import temperature
import weight
import pygame
import time
import cv2
import os
import socket

barcodeScannerName = "HID 0581:020c Keyboard"


def printer_state():
    try:
        p = Usb(0x8866,0x0100,timeout=0, in_ep=0x81, out_ep=0x02)
        return 0
    except escpos.exceptions.USBNotFoundError:
        #print("printer not found")
        return -1
        
def scanner_state():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    for dev in devices:
        if dev.name == barcodeScannerName:
            device = evdev.InputDevice(dev.fn)
            return 0
    return -1

def weight_state():
    weight.init()
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/weight.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()
    weight_test = 0
    for i in range(5):
        weight_test = weight_test + weight.check_weight() 
        time.sleep(0.1)
    weight_test = weight_test/5
    if(weight_test<10):
        return -1
    else:
        return 0
    
def camera_state():
    try:
        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()
        cv2.imshow('frame',frame)
        cap.release()
        cv2.destroyAllWindows()
        return 0
    except:
        return -1
    
def device_name():
    try:
        f = open('/proc/device-tree/model','r')
        for line in f:
            device_name = line
        f.close()
        return device_name
    except:
        return -1
    #cmd = 'cat /proc/device-tree/model'
    #device_name = os.popen(cmd).readline()
    #return device_name
    
def serial_number():
    s = "0000000000000000"
    try:
        f  = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6] == "Serial":
                s = line[10:26]
        f.close()
    except:
        s = -1
    return s

def up_time():
    try:
        cmd = 'uptime -p'
        up_time = os.popen(cmd).readline()
        return up_time
    except:
        return -1
    
def ip_address():
    try:
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyname(hostname)
        return ipaddr
    except:
        return -1
    
def wifi_name():
    try:
        cmd = "iwconfig wlan0|grep ESSID|awk -F: '{print $2}'"
        wifi_name = os.popen(cmd).readline()
        return wifi_name
    except:
        return -1
    
def mac_address_eth():
    #cmd = "ifconfig -a|grep ether|awk -F ' ' '{print $2}'"
    cmd = 'cat /sys/class/net/eth0/address'
    eth = os.popen(cmd).readline()
    return eth

def mac_address_wlan():
    #cmd = "ifconfig -a|grep ether|awk -F ' ' '{print $2}'"
    cmd = 'cat /sys/class/net/wlan0/address' 
    wlan = os.popen(cmd).readline()
    return wlan

def cpu_load():
    cmd = "top -bn1 |grep load|awk '{printf \"%.2f%%\", $(NF-2)}'"
    cpu = os.popen(cmd).readline()
    return cpu

def memory_load():
    cmd = "free -m| awk 'NR == 2{printf \"%s/%sMB\",$3,$2}'"
    mem = os.popen(cmd).readline()
    return mem

def process_on():
    process = []
    cmd_node = "ps -ef|grep node |grep main"
    node = os.popen(cmd_node).readlines()
    for line in node:
        process.append(line)
    cmd_node = "ps -ef|grep python"
    py = os.popen(cmd_node).readlines()
    for line in py:
        process.append(line)
    return process


    
if __name__ == '__main__':
    #print(ip_address())
    #print(printer_state())
    #print(scanner_state())
    #print(temperature.get_temperature())
    #print(weight_state())
    #print(camera_state())
    #print(device_name())
    #print(up_time())
    #print(wifi_name())
    #print(mac_address_eth())
    #print(mac_address_wlan())
    #print(cpu_load())
    #print(memory_load())
    process_on()
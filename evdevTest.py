import evdev
import signal,sys
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
#devices = evdev.InputDevice('/dev/input/event1')
#print(devices)
scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

barcodeScannerName = "HID 0581:020c Keyboard"
for dev in devices:
    if dev.name == barcodeScannerName:
        device = evdev.InputDevice(dev.fn)
        
'''      
def signal_handler(signal,frame):
    print("stop")
    dev.ungrab()
    sys.exit(0)
'''
#signal.signal(signal.SIGINT,signal_handler)

device.grab()
barcode = ""
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        data = evdev.categorize(event)
        if data.keystate == 1 and data.scancode!=42:
            if data.scancode == 28:
                print(barcode,flush =True)
                sys.stdout.flush()
                sys.exit(0)
                barcode = ""
            else:
                barcode += scancodes[data.scancode]



'''
for event in devices.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
'''
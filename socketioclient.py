import socketio
import time
import peripherals_check
import temperature

sio = socketio.Client()
start_timer = None

'''
def send_ping():
    global start_timer
    start_timer = time.time()
    sio.emit('ping_from_client','sss',namespace = '/terminal')

''' 
@sio.event
def connect():
    print('connected')
    
    #sio.emit('terminal_check','aa', namespace = '/terminal')
    #sio.emit('check',{'response':"my response"}, namespace = '/terminal')

''' 
@sio.event
def pong_from_server(data):
    global start_timer
    latency = time.time()-start_timer
    print('latency : {0:.2f}ms'.format(latency*1000))
'''

@sio.event
def test(data):
    #print(sid)
    print(data)
'''
@sio.on(sid,namespace='/terminal' )
def test2(data):
    print(data)
'''
@sio.event
def terminal_check(sid,data):
    print(data)
    check_type = data['check_state']
    if(check_type == 'printer'):
        printer_state = peripherals_check.printer_state()
        print('the server is now checking the state of the printer')
        sio.emit('check',{'printer_state':printer_state})
    
    if(check_type == 'scanner'):
        scanner_state = peripherals_check.scanner_state()
        print('the server is now checking the state of the scanner')
        sio.emit('check',{'scanner_state':scanner_state})
        
    if(check_type == 'temperature' ):
        temper_state = temperature.get_temperature()
        print('the server is now checking the state of the cpu temperature')
        sio.emit('check',{'temper_state':temper_state})
        
    if(check_type == 'weight' ):
        weight_state = peripherals_check.weight_state()
        print('the server is now checking the state of the weighning machine')
        sio.emit('check',{'weight_state':weight_state})
        
    if(check_type == 'camera' ):
        camera_state = peripherals_check.camera_state()
        print('the server is now checking the state of the camera')
        sio.emit('check',{'camera_state':camera_state})
        
    if(check_type == 'wifi' ):
        wifi_name = peripherals_check.wifi_name()
        print('the server is now checking the name of the wifi')
        sio.emit('check',{'wifi_name':wifi_name})
        
    if(check_type == 'ipaddr' ):
        ip_address = peripherals_check.ip_address()
        print('the server is now checking the ip address')
        sio.emit('check',{'ip_address':ip_address})
    
    if(check_type == 'uptime' ):
        up_time = peripherals_check.up_time()
        print('the server is now checking the up time')
        sio.emit('check',{'up_time':up_time})
    
    if(check_type == 'serial' ):
        serial_number = peripherals_check.serial_number()
        print('the server is now checking the serial number')
        sio.emit('check',{'serial_number':serial_number})
        
    if(check_type == 'ether_mac' ):
        ethernet_mac_address =  peripherals_check.mac_address_eth()
        print('the server is now checking the mac address of ethernet')
        sio.emit('check',{'ethernet_mac_address':ethernet_mac_address})
        
    if(check_type == 'wlan_mac' ):
        wlan_mac_address = peripherals_check.mac_address_wlan()
        print('the server is now checking the mac address of wlan0')
        sio.emit('check',{'wlan_mac_address':wlan_mac_address})
        
    if(check_type == 'cpu' ):
        cpu_load = peripherals_check.cpu_load()
        print('the server is now checking the cpu load')
        sio.emit('check',{'cpu_load':cpu_load})
        
    if(check_type == 'memory' ):
        memory_load = peripherals_check.memory_load()
        print('the server is now checking the memory')
        sio.emit('check',{'memory_load':memory_load })
        
    if(check_type == 'process' ):
        process_on = peripherals_check.process_on()
        print('the server is now checking the process list')
        sio.emit('check',{'process_on':process_on })
        
    if(check_type == 'all'):
        printer_state = peripherals_check.printer_state()
        scanner_state = peripherals_check.scanner_state()
        temper_state = temperature.get_temperature()
        weight_state = peripherals_check.weight_state()
        camera_state = peripherals_check.camera_state()
        wifi_name = peripherals_check.wifi_name()
        ip_address = peripherals_check.ip_address()
        up_time = peripherals_check.up_time()
        serial_number = peripherals_check.serial_number()
        ethernet_mac_address =  peripherals_check.mac_address_eth()
        wlan_mac_address = peripherals_check.mac_address_wlan()
        cpu_load = peripherals_check.cpu_load()
        memory_load = peripherals_check.memory_load()
        process_on = peripherals_check.process_on()
        
        print('the server is checking the state of peripherals')
        sio.emit('check',{'printer_state':printer_state, \
            'scanner_state':scanner_state, \
            'temperature':temper_state, \
            'weight_state':weight_state, \
            'camera_state':camera_state, \
            'wifi_name':wifi_name, \
            'ip_address':ip_address, \
            'up_time':up_time, \
            'serial_number':serial_number,\
            'ethernet_mac_address':ethernet_mac_address,\
            'wlan_mac_address':wlan_mac_address,\
            'cpu_load':cpu_load,\
            'memory_load':memory_load,\
                                      })


@sio.event
def disconnect():
    print('disconnected from server')


    
if __name__ == '__main__':
    sio.connect('http://192.168.0.171:5001')
    #sio.emit('ping_from_client')
    #sio.on(str(sio.sid),handler=test2,namespace = '/termianl')
    #print('sid is',sio.sid)
    sid = sio.sid
    print(sid)
    
    @sio.event
    def (data):
        #print(sid)
        print(data)
        sio.emit(sid,'aa')
    sio.wait()
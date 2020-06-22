#!/usr/bin/python
from netmiko import ConnectHandler
import re

# here is list of cisco routers ip addresses
ip_list = ['192.168.174.101', '192.168.174.102', '192.168.174.103', '192.168.174.104', '192.168.174.105',
           '192.168.174.106']

# list where informations will be stored
devices = []

# loop all ip addresses in ip_list
for ip in ip_list:
    cisco = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'admin',  # ssh username
        'password': 'cisco123',  # ssh password
    }

    net_connect = ConnectHandler(**cisco)

    output = net_connect.send_command('show version')  # execute show version on router and save output to output object

    # finding hostname in output using regular expressions
    regex_hostname = re.compile(r'(\S+)\suptime')
    hostname = regex_hostname.findall(output)

    # finding uptime in output using regular expressions
    regex_uptime = re.compile(r'\S+\suptime\sis\s(.+)')
    uptime = regex_uptime.findall(output)

    # finding version in output using regular expressions
    regex_version = re.compile(r'Cisco\sIOS\sSoftware.+Version\s([^,]+)')
    version = regex_version.findall(output)

    # finding serial in output using regular expressions
    regex_serial = re.compile(r'Processor\sboard\sID\s(\S+)')
    serial = regex_serial.findall(output)

    # finding ios image in output using regular expressions
    regex_ios = re.compile(r'System\s\image\s\file\sis\s"([^ "]+)')
    ios = regex_ios.findall(output)

    # finding model in output using regular expressions
    regex_model = re.compile(r'[Cc]isco\s(\S+).*memory.')
    model = regex_model.findall(output)

    print(ip)  # print current ip address of router on screen

    # append results to table [hostname,uptime,version,serial,ios,model]
    devices.append([hostname[0], uptime[0], version[0], serial[0], ios[0], model[0]])

# print all results (for all routers) on screen
for i in devices:
    print(i)
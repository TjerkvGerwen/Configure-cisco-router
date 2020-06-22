import sys
import telnetlib
import getpass
import paramiko
import time

def telnet_connect():
    tn.read_until(b"Username: ")
    tn.write(tel_user.encode('ascii') + b"\n")
    if tel_password:
        tn.read_until(b"Password: ")
        tn.write(tel_password.encode('ascii') + b"\n")
    to_standardconf = input("Do u want to use the script for the standard config")
    if to_standardconf == "yes" or to_standardconf == "Yes" or to_standardconf == "Y" or to_standardconf == "y" or to_standardconf == "YES":
        print("-------------------------------------------------------------")
        print("You chose yes")
        telnet_standardconf()
    else:
        print("-------------------------------------------------------------")
        print("The end")


def telnet_standardconf():
    print("-------------------------------------------------------------")
    standard_config_password = input("What is the password you want to use? ")
    tn.write(b"enable secret " + standard_config_password)  # These commands are used to send command over
    tn.write(b"line vry 0 4")
    tn.write(b"password " + standard_config_password)
    tn.write(b"login")
    tn.write(b"line con 0")
    tn.write(b"password " + standard_config_password)
    tn.write(b"login")
    tn.write(b"exit")
    tn.write(b"service password-encryption")
    tn.write(b"copy run start")
    tn.write(b"end\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))  # This is to recieve any output that you get on the after Telnet
    tn.close()


def ssh_connect():
    ssh_name = input("Please enter UserName")
    ssh_password = input("Please enter Password")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=HOST, username=ssh_name,
                       password=ssh_password)  # This is used to establish a connection
    # remote_connection = ssh_client.invoke_shell()  # This helps you invoke the shell of the client machine
    # remote_connection.send("cli\n")  # These commands are used to send command over
    # time.sleep(5)
    # output = remote_connection.recv(10240)  # This is to recieve any output that you get on the after SSH
    # connection is established
    # ssh_client.close  # This closes your active SSH connection
    to_standardconf = input("Do u want to use the script for the standard config")
    if to_standardconf == "yes" or to_standardconf == "Yes" or to_standardconf == "Y" or to_standardconf == "y" or to_standardconf == "YES":
        print("-------------------------------------------------------------")
        print("You chose yes")
        ssh_standardconf()
    else:
        print("-------------------------------------------------------------")
        print("The end")



def ssh_standardconf():
    print("-------------------------------------------------------------")
    standard_config_password = input("What is the password you want to use? ")
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send("cli\n")
    remote_connection.send("enable secret " + standard_config_password)  # These commands are used to send command over
    remote_connection.send("line vry 0 4")
    remote_connection.send("password " + standard_config_password)
    remote_connection.send("login")
    remote_connection.send("line con 0")
    remote_connection.send("password " + standard_config_password)
    remote_connection.send("login")
    remote_connection.send("exit")
    remote_connection.send("service password-encryption")
    remote_connection.send("copy run start")
    remote_connection.send("end\n")
    remote_connection.send("end\n")
    remote_connection.send("exit\n")


def telnet_commands():
    tn.write(b"enable\n")
    tn.write(b"config t\n")
    hostname = input("What hostname do u want to assign? ")
    tn.write(b"hostname" + hostname + "\n")
    standard_config = input("Do u want to configure the standard config?(yes/no) ")
    if standard_config == "yes" or standard_config == "y" or standard_config == "Yes" or standard_config == "Y":
        telnet_standardconf()
    elif standard_config == "no" or standard_config == "No" or standard_config == "N" or standard_config == "NO":
        print("some other config options")

def help():
    print("-------------------------------------------------------------")
    print("You chose help")

HOST = input("What is the IP adress: ")
PORT = input("What is the port number: ")
CON_type = input("Wil je een SSH of Telnet verbinding opzetten?(Keuze: T/S) ")
helplist = ("OSPF","Interface","DHCP","setup ssh")

if CON_type == "T" or CON_type == "Telnet" or CON_type == "TELNET" or CON_type == "telnet":  # TELNET
    print("-------------------------------------------------------------")
    print("You chose Telnet")
    print("-------------------------------------------------------------")
    tel_user = input("Enter your remote account: ")
    tel_password = getpass.getpass()
    tn = telnetlib.Telnet(HOST, PORT)
    telnet_connect()

elif CON_type == "S" or CON_type == "SSH" or CON_type == "ssh" or CON_type == "Ssh":  # SSH
    print("-------------------------------------------------------------")
    print("You chose SSH")
    print("-------------------------------------------------------------")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect
else:
    print("-------------------------------------------------------------")
    print("u did not make a choice please restart this application")

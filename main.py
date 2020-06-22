import sys
import telnetlib
import getpass

HOST = input("What is the IP adress: ")
PORT = input("What is the port number: ")
CON_type = input("Wil je een SSH of Telnet verbinding opzetten?(Keuze: T/S) ")


def telnet_connect():
    tn.read_until(b"Username: ")
    tn.write(tel_user.encode('ascii') + b"\n")
    if tel_password:
        tn.read_until(b"Password: ")
        tn.write(tel_password.encode('ascii') + b"\n")


def telnet_standardconf():
    print("-------------------------------------------------------------")
    standard_config_password = input("What is the password you want to use? ")
    tn.write(b"enable secret " + standard_config_password)
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
    print(tn.read_all().decode('ascii'))


def ssh_connect():
    print("test")


def telnet_commands():
    tn.write(b"enable\n")
    tn.write(b"config t\n")
    hostname = input("What hostname do u want to assign? ")
    tn.write(b"hostname" + hostname + "\n")
    standard_config = input("Do u want to configure the standard config?(yes/no) ")
    if standard_config == "yes" or standard_config == "y" or standard_config == "Yes" or standard_config == "Y":
        telnet_standardconf()
    elif standard_config == "no" or standard_config == "No" or standard_config == "N" or standard_config == "NO":
        print("someother config options")


if CON_type == "T" or CON_type == "Telnet" or CON_type == "TELNET" or CON_type == "telnet":
    print("-------------------------------------------------------------")
    print("You chose Telnet")
    print("-------------------------------------------------------------")
    tel_user = input("Enter your remote account: ")
    tel_password = getpass.getpass()
    tn = telnetlib.Telnet(HOST, PORT)
    telnet_connect()

elif CON_type == "S" or CON_type == "SSH" or CON_type == "ssh" or CON_type == "Ssh":
    print("-------------------------------------------------------------")
    print("You chose SSH")
    print("-------------------------------------------------------------")

    ssh_connect

elif CON_type != "S" or CON_type != "T" or CON_type != "TELNET" or CON_type != "telnet" or CON_type != "ssh" or CON_type != "SSH":
    print("-------------------------------------------------------------")
    print("u did not make a choice please restart this application")

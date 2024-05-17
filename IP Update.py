"""
定时获取公网IP，更新对应文件
"""

import os
import requests
import datetime
import subprocess

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        response.raise_for_status()
        ip = response.json()['origin']
        return ip
    except requests.RequsetsException as e:
        print(f"Error:{e}")
        return None

def get_lastIp(fPath):
    try:
        f = open(fPath,"r")
        lastIp = f.read()
        f.close()
        return(lastIp)
    except:
        return None

def secret_ip(sip):
    sip_arr=sip.split('.')
    sip_arr[0]=str(int(sip_arr[0]))
    dip=sip_arr[0]+"."+sip_arr[1]+"."+sip_arr[2]+"."+sip_arr[3]
    return(dip)

def update_ipfile(newIp, fPath):
    f = open(fPath,"w")
    f.write(newIp)
    f.close()
    return None

def git_push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "update ip"])
    subprocess.run(["git", "push", "origin", "main"])

fPath = os.getcwd()+"\\IpRecord.txt"
#print(fPath)
oldIp = get_lastIp(fPath)
newIp = secret_ip(get_public_ip())
if oldIp != newIp:
    update_ipfile(newIp, fPath)
    git_push()

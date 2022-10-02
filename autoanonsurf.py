import os,sys,time

timetonodechange = int(input("Enter time in seconds between TOR node change :"))
os.system("clear")

os.system("anonsurf start") 
time.sleep(2.5)
os.system("anonsurf status")
time.sleep(2.5)
os.system("anonsurf myip")
time.sleep(2.5)
os.system("clear")

i = 0

def ipchange():
 os.system("anonsurf myip")
 time.sleep(2.5)  
 os.system("anonsurf change")
 time.sleep(2.5)  
 os.system("anonsurf myip") 
 time.sleep(2.5)  
 os.system("clear") 

while i == 0:
   time.sleep(timetonodechange)
   ipchange()
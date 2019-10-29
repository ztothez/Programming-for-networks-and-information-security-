#Toni Tuunainen 1.2.6.4: Activity – Create a Script to Allow User to Add Devices
devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)

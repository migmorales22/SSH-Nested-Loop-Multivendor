# SSH-Nested-Loop-Multivendor

An amazing tool to get the config of the Routers and Switches deployed around your Service Provider using Paramiko.

Here we would show how the script works with vendors like Cisco and Huawei.

##  Cisco

In the script for Cisco devices we start creating two .txt, one for the Commands and another one for the Devices. 

The formatting for the Command_List.txt in Cisco would be:

```js
!
show platform
!
show filesystem
!
show hw-module fpd location all
!
```
And the formatting for the Device_List.txt would be:
```js
10.192.35.105
10.192.35.108
```
Then put your SSH credentials in the username and password variables.
```js
username = "XXXXX"
password = "XXXXX" 
```

**Note:** In line 4 and 7, at the /path/ part, you have to put the directory path to the Command_List.txt and Device_List.txt, so the script find it and run it.

For example:
```js
c = open("/Volumes/Extreme SSD/HP/Py/ssh-multiple-sessions-paramiko/Command_List.txt" , "r")

d = open("/Volumes/Extreme SSD/HP/Py/ssh-multiple-sessions-paramiko/Device_List.txt", "r")
```

**Note:** In line 22, you might wanna put the command used by your vendor of choices that lets you runs a command and give you the whole output of this one. If you dont want it, just erase this line.

For example in Cisco:
```js
    comm.send("terminal length 0 \n")
```


Then you should be good to run the script as many times as you want!!. There's not limit on how many devices you can put in the Devices_List.txt.

##  Huawei

The script for Huawei devices, it's a little bit different, you don't need to create any .txt, because those inputs are in the script, so you just have to write it down into the script.

The formatting for the Command_List in Huawei would be:

```js
c =("display memory-usage\n"
    "display cpu-usage \n")
```
And the formatting for the Device_List in Huawei would be:
```js
d = ["10.39.152.151",
     "10.39.152.152"]
```
Then put your SSH credentials in the username and password variables.
```js
username = "XXXXX"
password = "XXXXX" 
```
**Note:** In line 24, you might wanna put the command used by your vendor of choices that lets you runs a command and give you the whole output of this one. If you don't want it, just erase this line.

For example in Huawei:
```js
    comm.send("screen-length 0 temporary\n")
```

Customize the script to whatever are your needs, and you should be good to go.!!

## Requirements

* Paramiko
* Time
* Python 3.9 =>

# SSH-Nested-Loop-Multivendor

An amazing tool to get the config of the Routers and Switches deployed around your Service Provider using Paramiko.

Here we would show how the script works with vendors like Cisco and Huawei.

##  Cisco:

In the script for Cisco we start creating two .txt, one for the Commands and another one for the Devices. 

The formatting for the Command_List.txt would be:

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
Then we put our credentials for the SSH connection,


##  Huawei:

In the script for Cisco we start creating two .txt, one for the Commands and another one for the Devices.


## Requirements

* Paramiko
* Time

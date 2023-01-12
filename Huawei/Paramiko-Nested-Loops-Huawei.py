import paramiko
import time

c =("display memory-usage\n"
    "display cpu-usage \n")
command_list = c.split("\n")              #Create a List from Command_List file

d = ["10.39.152.151",
     "10.39.152.152"]
hosts = d                    #Create a List from Device_List file

port = 22
username = "XXXXX"     #SSH-Username
password = "XXXXX"     #SSH-Password
logs = []
logs1= []

for ip in hosts:                                  #Loop each ip in hosts list
    print("Try to login..", ip)
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(ip, port, username, password)
    comm = conn.invoke_shell()
    comm.send("screen-length 0 temporary\n")
    for command in command_list:                   #Loop each commmand in command_list
        comm.send(' %s \n' %command)
        time.sleep(5)
        output = comm.recv(65535)
        output = output.decode("utf-8")
        logs = output.split("xxxxx")         #Convert string to List without any change
        print("logs",logs)
        logs1.extend(logs)                    #Extend list with new logs list in for loop
    logs1 = ''.join(map(str, logs1))               #Convert list to string
    with open("{}.txt".format(ip), "w") as f:             #Open txt file named by hosts(ip) in for loop
        f.write(logs1)                             #Write string to file
    logs1 = []                                     #Empty list after each for loop
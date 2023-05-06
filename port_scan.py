import socket

IP_Adress = input("Please enter your target ip Adress:\n")
with open("open_ports.txt","a") as file:
    file.write(IP_Adress+"\n")

for i in range(1,65536):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        try:
            s.connect((IP_Adress,i))
            print(f"port {i} is open")
            with open("open_ports.txt", "a") as file:
                file.write(f"port {i} is open\n")
        except:
            pass
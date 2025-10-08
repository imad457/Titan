import socket


def extract_ip():
    print('-------------------------')
    print('+        IP Address     +')
    print('-------------------------')
    url = input('entre ur domain : ')
    ip_address = socket.gethostbyname(url)
    print(f"your ip is : {ip_address}")


   
    
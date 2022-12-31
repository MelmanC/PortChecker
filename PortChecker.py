import socket

def scan():
    target = input("Entrez l'adresse IP de la cible : ")
    port = int(input("Entrez le port ou vous voulez commencer à scanner : "))
    end = int(input("Entrez le port ou vous voulez finir à scanner : "))
    L=[]
    while port <= end:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.04)
            conn = s.connect_ex((target, port))
            if conn == 0:
                print('\033[92mLe port', port, 'est ouvert !\033[0m')
                L.append(port)
                s.close()
            else:
                print('\033[91mLe port', port, 'est fermé !\033[0m')
                s.close()
            port = port + 1
        except KeyboardInterrupt:
            quit()
    print("Les ports ouverts sont : ", L)
scan()
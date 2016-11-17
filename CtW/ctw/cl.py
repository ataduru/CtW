import socket
import sys
import select
import os
import objects
import pickle


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    host = ''                         
    port = 9009

    s.settimeout(2)

    # connect to remote host
    try :
    	s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()

    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
     
        for sock in ready_to_read:        
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.flush() 

print("Menu")

    #MULTIPLAYER OPTION

flag = 1

while flag:
    print("Multiplayer: ")
    print("  1- Create Player:")
    print("  2- Join Game:\n")

    secim = input()

    if(secim == 1):     #CREATING NEW PLAYER
        flag = 0
        usernameFlag = 1

        while usernameFlag:
            print('Welcome!')
            print('Choose Your Username:\n')
            
            if(os.stat("usernames.txt").st_size != 0):
                f = open("usernames.txt", "r+")
                liste = ''.join(f.readlines())
                objects.usernames = pickle.loads(liste)
                f.close()


            username = raw_input()

            if username in objects.usernames:
                print "Unavailable"

            else:
                usernameFlag = 0
                objects.usernames.append(username)

                f = open("usernames.txt", "r+")
                f.truncate()
                f.write(pickle.dumps(objects.usernames))
                f.close()

                idFlag = 1
                while idFlag:
                    if(os.stat("users.txt").st_size != 0):
                        f = open("users.txt", "r+")
                        geciciListe = ''.join(f.readlines())
                        objects.users = pickle.loads(geciciListe)
                        f.close()

                    if(os.stat("id.txt").st_size != 0):
                        f = open("id.txt", "r+")
                        geciciListe = ''.join(f.readlines())
                        objects.mp_empire_id = pickle.loads(geciciListe)
                        f.close()

                    mp_empire_id = input("Choose your empire:\nPick a number between 1 and 256:\n")

                    if mp_empire_id not in objects.mp_empire_id:
                        print "It is already taken"

                    else:
                        idFlag = 0
                        objects.users[str(username)] = mp_empire_id

                        f = open("empireid.txt", "r+")
                        f.truncate()
                        f.write(str(mp_empire_id))
                        f.close()


                        f = open("users.txt", "r+")
                        f.truncate()
                        f.write(pickle.dumps(objects.users))
                        f.close()

                        objects.mp_empire_id.remove(mp_empire_id)
                        f = open("id.txt", "r+")
                        f.truncate()
                        f.write(pickle.dumps(objects.mp_empire_id))
                        f.close()


                        client()


    elif(secim == 2):       #JOIN GAME
        if(os.stat("mpdb.txt").st_size == 0):
            print "Not Found"
        else:
            flag = 0
            usernameFlag = 1

            while usernameFlag:
                print('Welcome!')
                print('Enter Your Username:\n')
                
                if(os.stat("usernames.txt").st_size != 0):
                    f = open("usernames.txt", "r+")
                    liste = ''.join(f.readlines())
                    objects.usernames = pickle.loads(liste)
                    f.close()
        
                username = raw_input()

                if username not in objects.usernames:
                    print "Wrong Username"

                else:
                    usernameFlag = 0
                    if(os.stat("users.txt").st_size != 0):
                                f = open("users.txt", "r+")
                                geciciListe = ''.join(f.readlines())
                                objects.users = pickle.loads(geciciListe)
                                f.close()

                    mp_empire_id = objects.users[username]

    else:
        "Invalid Input"

client()
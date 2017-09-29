# telnet program example
import socket, select, string, sys



class Main:

    def __init__(self):
        # if (len(sys.argv) < 4):
        #     print('Usage : python telnet.py hostname port username')
        #
        #     sys.exit()

        self.host = ""
        self.port = 0
        self.username = ""
        self.send = False
        self.message = ""

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(2)

        self.message_list = []

    def send_message(self, message):
        msg = message
        self.message_list.append([msg, True])
        msg += "///" + self.username
        self.s.send(msg.encode())


    def prompt(self):
        sys.stdout.write('<You> ')
        sys.stdout.flush()

    def get_messages(self):
        return self.message_list

    def set_username(self, username):
        self.username = username


    # main function
    def main_loop(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        # connect to remote host
        try:
            self.s.connect((self.host, int(self.port)))
        except:
            print('Unable to connect')
            sys.exit()

        print('Connected to remote host. Start sending messages')
        # self.prompt()

        while 1:
            socket_list = [sys.stdin, self.s]

            # Get the list sockets which are readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

            for sock in read_sockets:
                # incoming message from remote server
                if sock == self.s:
                    data = sock.recv(4096)
                    # if not data:
                    #     print('\nDisconnected from chat server')
                    #     sys.exit()
                    if data:
                        # print data
                        self.message_list.append([data, False])
                        sys.stdout.write(data.decode())
                        # self.prompt()
                #
                #
                # user entered a message
                else:
                    msg = sys.stdin.readline()
                    self.message_list.append([msg, True])
                    msg += "///" + self.username
                    self.s.send(msg.encode())
                    self.prompt()





# Debug commands

# Main = Main()
# Main.main_loop("localhost", 5000, "HPringles")
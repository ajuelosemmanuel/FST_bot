import socket

class osuIRC:
    """
    Kind of wrapper for my osu! IRC bot, designed to be easily used.
    """
    def __init__(self, username, password, server="irc.ppy.sh", port=6667):
        """     
        Args:
            username (str): osu!username
            password (str): osu!IRC password
            server (str, optional): irc server. Defaults to "irc.ppy.sh".
            port (int, optional): server port. Defaults to 6667.
        """
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        """
        Initiates the connection to the osu!IRC server.
        """
        self.irc.connect((self.server, self.port))
        self.irc.send(bytes("PASS " + self.password +"\n", "UTF-8"))
        self.irc.send(bytes("USER "+ self.username +" "+ self.username +" "+ self.username +" :python\n", "UTF-8"))
        self.irc.send(bytes("NICK "+ self.username +"\n", "UTF-8"))
        self.irc.send(bytes("NICKSERV IDENTIFY " + self.username + " " + self.password + "\n", "UTF-8"))
    
    def join_mp(self, mp_id):
        """
        Connects to the multiplayer lobby.

        Args:
            mp_id (int): multiplayer lobby id
        """
        self.irc.send(bytes("JOIN #mp_" + mp_id + "\n", "UTF-8"))
    
    def message_mp(self, mp_id, content):
        """
        Sends a message to a given multiplayer lobby.

        Args:
            mp_id (int): multiplayer lobby id
            content (str): content of your message
        """
        self.irc.send(bytes("PRIVMSG #mp_" + mp_id + " " + content + "\n", "UTF-8"))
    
    def message_player(self, name, content):
        """
        Sends a message to a given player.

        Args:
            name (player): player name
            content (str): content of your message
        """
        self.irc.send(bytes("PRIVMSG " + name + " " + content + "\n", "UTF-8"))
    
    def recv(self, bits):
        """
        Records the last <bits> bits, using the built in recv function.
        """
        return self.irc.recv(bits)
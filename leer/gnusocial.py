#!/bin/python
#Written by foo@gnusocial.net https://elbinario.net
#Under GNU GPL License
import sys
from sys import exit
import time
import socket
import threading
import ssl
import ConfigParser
import json
import pycurl
from StringIO import StringIO
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode


class GNUSocialIRCBot():

    def __init__(self):
	print("hola_mundo")
        self.cfg = ConfigParser.ConfigParser()
        self.cfg.read("gnusocialircbot.cfg")
        self.botnick = self.cfg.get("irc", "nickname")
        self.channel = self.cfg.get("irc", "channel")
        self.owner = self.cfg.get("irc", "owner")
        self.server = self.cfg.get("irc", "ip")
        self.port = int(self.cfg.get("irc", "port"))
        self.socialname = self.cfg.get("social" , "botname")
        self.socialpass = self.cfg.get("social" , "password")
        self.socialnode = self.cfg.get("social", "node")
        self.commands = [".quit", ".join", ".part", ".say", ".social"]
	print(self.botnick)
        self.olds = []
        self.ircmsg = ""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ircsock = ssl.wrap_socket(self.s)
        self.url_status = "https://" + self.socialnode + "/api/statuses/friends.json"
        self.url_update = "https://" + self.socialnode + "/api/statuses/update.xml"
        #init functions
        self.connect()
        self.joinchan(self.channel)
        self.sendowner("Im ready master")
        self.listen()
	print(self.botnick)
    def connect(self):
        self.ircsock.connect((self.server, self.port))
        self.ircsock.send("USER " + self.botnick + " " + self.botnick + " " + self.botnick + "  :\r\n")
        self.ircsock.send("NICK " + self.botnick + "\r\n")

    def ping(self):
        self.ircsock.send("PONG :pingis \n")
        self.news()

    def sendnews(self, list):
        try:
            for item in list:
                if item not in self.olds:
                    aux = '' + item['screen_name'] + "-> "
                    msg = item['status']['text']
                    aux = aux + msg
                    try:
                        self.olds.append(item)
                        self.sendmsg(aux)
                        time.sleep(1)
                    except:
                        pass
        except Exception as e:
            self.sendowner("error on send news", e)
            pass

    def sendmsg(self, msg):
        self.ircsock.send("PRIVMSG " + self.channel + " :" + msg.encode('utf-8') + "\r\n")

    def sendowner(self,msg):
        self.ircsock.send("PRIVMSG " + self.owner + " :" + msg + "\r\n")

    def joinchan(self, chan):
        self.ircsock.send("JOIN " + chan + "\n")

    def social_status(self, msg):
        try:
            curl = pycurl.Curl()
            curl.setopt(pycurl.SSL_VERIFYPEER, False)
            curl.setopt(pycurl.SSL_VERIFYHOST, False)
            curl.setopt(pycurl.USERPWD, self.socialname + ":" + self.socialpass)
            curl.setopt(pycurl.POST, 1)
            post_data = {"status" : msg}
            postfields = urlencode(post_data)
            curl.setopt(pycurl.POSTFIELDS, postfields)
            curl.setopt(curl.URL, self.url_update)
            curl.perform()
            curl.close()
        except:
            self.sendowner("error on status social")

    def news(self):
        try:
            buffer = StringIO()
            curl = pycurl.Curl()
            curl.setopt(pycurl.SSL_VERIFYPEER, False)
            curl.setopt(pycurl.SSL_VERIFYHOST, False)
            curl.setopt(pycurl.USERPWD, self.socialname + ":" + self.socialpass)
            curl.setopt(curl.URL, self.url_status)
            curl.setopt(pycurl.WRITEFUNCTION, buffer.write)
            curl.perform()
            curl.close()
            data = json.loads(buffer.getvalue())
            t = threading.Thread(target=self.sendnews, args=([data]))
            t.start()
        except:
            self.sendowner("error on news")


    def exitchat(self):
        self.sendowner("ByezzZzzZzz master")
        self.s.close()
        self.ircsock.close()
        exit()

    def analize_ircmsg(self):
        if self.ircmsg.find("PING :") != -1:
            self.ping()
        for com in self.commands:
            if self.ircmsg.find(com) != -1:
                if self.ircmsg.find(self.botnick) != -1:
                    message = self.ircmsg.split('!')
                    if message[0] == (":" + self.owner):
                        command = self.ircmsg.split(com)
                        param = command[1]
                        param = param.strip()
                        if com == ".quit":
                            self.exitchat()
                        if com == ".say":
                            self.sendmsg(param)
                        if com == ".join":
                            self.joinchan(param)
                        if com == ".social":
                            self.social_status(param)

    def listen(self):
        while 1:
            self.ircmsg = self.ircsock.recv(512)
            self.ircmsg = self.ircmsg.strip('\n\r')
            self.analize_ircmsg()

if __name__ == "__main__":
    ircbot = GNUSocialIRCBot()

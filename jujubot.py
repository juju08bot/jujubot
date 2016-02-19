import telepot
import csv
import random
import re
import time

class InsultHandler:
    def __init__(self):
        with open('insult.csv', 'rb') as f:
            reader = csv.reader(f)
            self.insultlist = list(reader)
            self.listlength = len(self.insultlist)
    def get(self):
        insultidx = random.randint(0, self.listlength-1)
        insult = self.insultlist[insultidx][0]
        return insult + "!"

class BierCounter:
    def __init__(self):
        self.idlist = list()
        self.namelist = list()
        self.countlist = list()
    def add(self, uid, uname):
        if uid in self.idlist:
            idx = self.idlist.index(uid)
            self.countlist[idx] = self.countlist[idx] + 1
        else:
            self.idlist.append(uid)
            self.namelist.append(uname)
            self.countlist.append(1)
    def get(self):
        outstring = "Bierstats:\n"
        for i in range(0, len(self.idlist)):
            outstring = outstring + self.namelist[i] + ": " + str(self.countlist[i]) + "\n"
        return outstring

def bierinize(text):
    btext = re.sub(r'(\S)ier', 'bier', text)
    if btext==text:
        out = None
    else:
        out = "Es heisst \n" + "'" + btext + "'\n" + "du " + insulthandler.get()
    return out

def handle(msg):
    chat_id = msg['chat']['id']
    from_id = msg['from']['id']
    from_name = msg['from']['first_name']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/zum':
        bot.sendMessage(chat_id, "Proscht!")
    elif command == '/jucker':
        bot.sendMessage(chat_id, "Schwul!")
    elif command == '/fluch':
        bot.sendMessage(chat_id, insulthandler.get())
    elif command == '/bierstats':
        bot.sendMessage(chat_id, biercounter.get())
    else:
        if "bier" in command:
            biercounter.add(from_id, from_name)
        if "ier" in command:
            btext = bierinize(command)
            if btext is not None:
               bot.sendMessage(chat_id, btext)


# Init insult
insulthandler = InsultHandler()

# Init biercounter
biercounter = BierCounter()

# Start listening
with open('token.txt', 'r') as f:
    token = f.readline()
bot = telepot.Bot(token)
bot.notifyOnMessage(handle)

# Keep the program running
while 1:
    time.sleep(10)
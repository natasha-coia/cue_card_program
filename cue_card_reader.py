import random


def rand_selector(num,thing):
    return thing[random.randint(0,num)]

def read_cue_card(line):
    front = ""
    x = 0
    is_front = True
    while is_front == True: #a.k.a before the separator "/" has appeared
        is_front = separator(line[x])
        front += line[x]
        x += 1
    print("Front of cue card: " + front)
    next = input("When ready to see back of cue card, press Enter: ")
    back = ""
    while x < len(line): #output the rest of the line
        back += line[x]
        x += 1
    print("Back of cue card is: " + back)
    next = input("When ready to see next cue card, press Enter")
    return

def already_read(alreadyread,x):
    if x in alreadyread:
        return True
    else:
        return False

def separator(char):
    if char == "/":
        return False
    return True

topic_name = input("Enter name (filename) of first set of cuecards: ")
topic = open(topic_name,'r') #opens the file of cue cards relating to topic to read
lines = topic.readlines()   #creates a list containing each line in the file
length = len(lines) #finds the length (number of lines) of the file
alreadyread=[]
while len(alreadyread) < length:    #while there is still lines to be read
    line = rand_selector(length,lines)  #randomly select a line
    if not already_read(alreadyread,line):  #if it hasn't already been read, read the cue card!
        read_cue_card(line)
        alreadyread.append(line)    #then add line to list of already read lines
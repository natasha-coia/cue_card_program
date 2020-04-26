import random

def read_cue_card(line):
    front = ""
    x = 0
    is_front = True
    while line[x] != "/": #a.k.a before the separator "/" has appeared
        front += line[x]
        x += 1
        #is_front = separator(line[x])
    print("Front of cue card: " + front)
    next = input("When ready to see back of cue card, press Enter")
    back = ""
    x += 1
    while x < len(line): #output the rest of the line
        back += line[x]
        x += 1
    print("Back of cue card is: " + back)
    next = input("When ready to see next cue card, press Enter")
    return


topic_name = input("Enter name (filename) of first set of cuecards: ")
topic = open(topic_name,'r') #opens the file of cue cards relating to topic to read
lines = topic.readlines()   #creates a list containing each line in the file
while len(lines) > 0:    #while there is still lines to be read
    line = lines[random.randint(0,len(lines)-1)]  #randomly select a line
    read_cue_card(line)
    lines.remove(line)
print("No more cue cards left on this topic")
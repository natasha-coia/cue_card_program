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
    next = input("When ready to see next cue card, press Enter, or to exit press 'X'")
    return True if next == "X" or next == "x" else False;


def first_menu_choice():
    topic_name = input("Enter name (filename) of first set of cuecards: ")
    topic = open(topic_name,'r') #opens the file of cue cards relating to topic to read
    lines = topic.readlines()   #creates a list containing each line in the file
    end = False
    while len(lines) > 0 and not end:    #while there is still lines to be read
        line = lines[random.randint(0,len(lines)-1)]  #randomly select a line
        end = read_cue_card(line)
        lines.remove(line)
    print("Cue Card Reading has Finished")
    return

def main_menu():
    print("Select command from following list by entering the associated number/letter:")
    print("     1. Read a set of cuecards")
    print("     2. Add a set of cuecards")
    print("     3. Edit a set of cuecards")
    print("     4. Delete a set of cuecards")
    print("     X. Exit program")
    menu_choice = input()
    if menu_choice == "1":
        first_menu_choice()
        main_menu()
    elif menu_choice == "2":
        print("Not a valid option at this time as program is still being developed. Please try again.")
        main_menu()
    elif menu_choice == "3":
        print("Not a valid option at this time as program is still being developed. Please try again.")
        main_menu()
    elif menu_choice == "4":
        print("Not a valid option at this time as program is still being developed. Please try again.")
        main_menu()
    elif menu_choice == "X" or menu_choice == "x":
        print("Thank you for using this program")
        return
    else:
        print("The option you entered was invalid, please try again:")
        main_menu()

main_menu()
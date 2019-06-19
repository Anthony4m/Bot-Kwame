
import os
import sys
import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# create a new bot kwame
chatbot = ChatBot("Kwame")
chatbot.storage.drop()

trainer = ListTrainer(chatbot)
trainer.train(open("KwameScript.txt", "r").readlines())


stuffs = ["saw", "hammer", "screw"]
initialise_words = ["open", "get", "search"]
terminate_words = ["close", "quit", "stop"]

# main loop
done = False
while done == False:
    # greetings function
    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            print('Good Morning!')

        if currentH >= 12 and currentH < 18:
            print('Good Afternoon!')

        if currentH >= 18 and currentH !=0:
            print('Good Evening!')
    greetMe()

    
    #Tracks whether a "bring" or "return" Keyword was used and whether a tool was mentioned
    _bring = False
    _return = False
    _tool = ""

    # Tracks if there was an error along the way
    conflict = False

    command = input("\nsay something \n")

#------------------------------------------------ANALYSE INPUT----------------------------------------------------#

    #check if tool was mentioned
    for tool in stuffs:
        if tool in command.lower():
            if _tool == "":
                 _tool = tool
                
            else:
    #Checks if one of the words is a subset of the other, and goes with the larger one
                if tool in _tool:
                    _tool = _tool
                elif _tool in tool:
                    _tool = tool
                else:
                    conflict = True
                    print("I can't multitask")
    
    #check for bribg synonyms
    for word in initialise_words:
        if word in command.lower():
            _bring = True


    # Check for terminate synonym
    for exit in terminate_words:
        if exit in command.lower():
            _return = True

    # #make sure a tool was mentioned and there is a bring or return word
    if (_tool == "" or (_bring == False and _return == False)):
        conflict = True

# -------------------------------------DECIDING RESPONSE----------------------------------------------------------------#
    if "shutdown" in command.lower():
        response = "shutting down......."
        done = True
    elif conflict == False and _bring == True:
        response = "OK I'll bring the " + _tool 
    elif conflict == False and _return == True:
        response = "Ok I'll put " + _tool + " away"
    else:
        response = str(chatbot.get_response(command))

    print(response)
  
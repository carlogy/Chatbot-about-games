print("Hello, My name is Carlo, and welcome to my chatbot! Let’s chat about games.")
answer = input("Are you excited to interact with me? ")
answer = answer.lower()
if (answer == "yes"):
  print ("I'm so excited too!")
elif (answer == "no"):
  print ("Aww, well I hope I can change your mind!")
else:
  print ("Hmm.. I seem to not comprehend your answer.") 
answer = input("Do you like video games?")
answer = answer.lower()
if (answer == "yes"):
    print("Cool! Same here!")
elif (answer == "no"):
    print ("Eh, they aren't for everyone")
elif (answer == "maybe"):
    print("On the fence, huh?")
else:
    print("Hmm.. I seem to not comprehend your answer.")
answer = input("What about board or card games?")
answer = answer.lower()
if (answer == "yes"):
    print("Nice, I like them too")
elif (answer == "no"):
    print("People like other things other than games.")
else:
    print("Hmm.. I seem to not comprehend your answer.")  
print("Thank you for chatting with me! Have a great day!")


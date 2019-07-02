import time,random,re

responses = {"Hi":["Hello","Goodday","Hi"],
             "Hello":["Hello","Goodday","Hi"],
             "Goodday":["Hello","Goodday","Hi"],
             "What is your name?":["My name is ALIE","ALIE","They call me ALIE"],
             "How are you?":["Fine","Worse than you","I am doing great"]} 

def respond(message):
  if message in responses:
    return random.choice(responses[message])
  else: 
    return"I don't know what to respond to: {}".format(message)

def send_message(message):
  print("USER: {}".format(message))
  time.sleep(random.randint(1,3))
  print("ECHOBOT: {}".format(respond(message)))
  
while True:
  send_message(input())


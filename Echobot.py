import time

def respond(message):
  return"Hello I am ALIE I am going to repeat everything you say: {}".format(message)

#respond("Hello I am a duck")

def send_message(message):
  print("USER: {}".format(message))
  time.sleep(0.4)
  print("ECHOBOT: {}".format(respond(message)))

import time,random,re

responses = {"Hi":["Hello","Goodday","Hi"],
             "Hello":["Hello","Goodday","Hi"],
             "Goodday":["Hello","Goodday","Hi"],
             "What is your name?":["My name is ALIE","ALIE","They call me ALIE"],
             "How are you?":["Fine","Worse than you","I am doing great"],
             "Koekjes":["Koekjes", "Awesome", "I like koekjes"]} 

pattern_responses = {"Do you remember (.*)": ["Of course I remember {}", "No I can't remember {}"],
                     "I feel (.*)": ["Why do you feel {}", "You feel {}, why?"]}



def check_pattern(message):
  pattern = "Do you remember (.*)"
  match = re.search(pattern, message)
  if match:
    answer = random.choice(pattern_responses[pattern])
    return answer.format(match.group(1))

def respond(message):
  if message in responses:
    return random.choice(responses[message])
  elif check_pattern(message):
    return "{}".format(check_pattern(message))
  else: 
    return random.choice(["Hmmm", "Anyway", "That is very interisting", "Whatever"])

def send_message(message):
  print("You: {}".format(message))
  time.sleep(random.randint(0,3))
  print("ALIE: {}".format(respond(message)))
  
while True:
  send_message(input())

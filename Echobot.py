import time,random,re



responses = {"hi":["Hello","Goodday","Hi"],
             "hello":["Hello","Goodday","Hi"],
             "goodday":["Hello","Goodday","Hi"],
             "what is your name?":["My name is ALIE","ALIE","They call me ALIE"],
             "how are you?":["Fine","Worse than you","I am doing great"],
             "koekjes":["Koekjes", "Awesome", "I like koekjes"],
             "where do you live?":["Nowhere", "I am not shure", "That is a good question", "I rather not talk about it"]} 

pattern_responses = {"do you remember (.*)": ["Of course I remember {}", "No I can't remember {}"],
                     "i feel (.*)": ["Why do you feel {}", "You feel {}, why?"],
                    "can i sit (.*)": ["Of course you can sit {}", "No you are not allowed to sit {}", "I don't know whether you can sit {} or not"],
                    "do you (.*)": ["No I don't {}", "I don't know if I {}", "Yes, I do {}"],
                    "if (.*)": ["{} already"],
                    "i am in (.*)": ["How is it in {}", "I heard {} is annoying", "I don't like to be in {}"]}


def swap_pronoun(phrase):
  if ' me' in phrase:
    return re.sub('me','you', phrase)
  elif ' you'in phrase:
    return re.sub('you', 'I', phrase)
  elif ' I' in phrase:
    return re.sub('I', 'you', phrase)
  else:
    return phrase

def check_pattern(message):
  for pattern in pattern_responses:
    match = re.search(pattern, message)
    if match:
      answer = random.choice(pattern_responses[pattern])
      return answer.format(swap_pronoun(match.group(1)))

def respond(message):
  message = message.lower()
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



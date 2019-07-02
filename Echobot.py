import time,random,re

responses = {"hi":["Hello","Goodday","Hi"],
             "hello":["Hello","Goodday","Hi"],
             "goodday":["Hello","Goodday","Hi"],
             "bye":["Goodbye","Bye","Have fun"],
             "goodbye":["Goodbye","Bye","Have fun"],
             "what is your name":["My name is ALIE","ALIE","They call me ALIE"],
             "how are you":["Fine","Worse than you","I am doing great"],
             "koekjes":["Koekjes", "Awesome", "I like koekjes"],
             "where do you live":["Nowhere", "I am not shure", "That is a good question", "I rather not talk about it"],
             "what are you doing":["Nothing... Why?","I am eating koekjes, and you?","Right now I am answering your question","I am solving a cube in my mind"],
             "why": ["Because I like it", "Doesn't matter", "What why?", "Because I tell you so"],
             "how old are you":["Infinity","I don't age","That is none of your business"],
             "how do you feel":["Awesome","Better than yesterday, and how do you feel?","I feel tired, and you?"],
             "what should I do":["Meyby you should get some more sleep","I think you should go outside more","Meyby you should drink some water"]} 

pattern_responses = {"do you remember (.*)": ["Of course I remember {}", "No I can't remember {}"],
                     "i feel (.*)": ["Why do you feel {}", "You feel {}, why?"],
                    "can i sit (.*)": ["Of course you can sit {}", "No you are not allowed to sit {}", "I don't know whether you can sit {} or not"],
                    "do you (.*)": ["No I don't {}", "I don't know if I {}", "Yes, I do {}"],
                    "if (.*)": ["{} already"],
                    "i am in (.*)": ["How is it in {}", "I heard {} is annoying", "I don't like to be in {}"],
                    "why (.*)": ["Because I like it", "Doesn't matter", "What why?", "Because I tell you so"],
                    "(.*)weather(.*)":["It is very very bad","Once in 2003 it was freezing.","It is going to rain someday"],
                    "(.*)happy(.*)":["I am glad that you feel happy","Did something happen?","Well that is good"],
                    "(.*)bad(.*)":["I am sorry that you feel sad","Can I help you with something?","That is too bad"],
                    "(.*)i don't know(.*)":["That is okay too","Alright","Can I help you with something"],
                    "can you help me(.*)":["Of course can I help you{}","Yes I can help you{} please tell me with wath","I would love to help you{}"],
                    "my name is(.*)":["{} is a nice name","I wish my name was{}","Hello{} my name is ALIE"],
                    "(.*)talk(.*)":["Tell me about it","What's up","Okay, begin"]}


def swap_pronoun(phrase):
  if ' me ' in phrase:
    return re.sub('me','you', phrase)
 # elif ' you 'in phrase:
    #return re.sub('you', 'I', phrase)
  elif ' I ' in phrase:
    return re.sub('I', 'you', phrase)
  elif ' am ' in phrase:
    return re.sub('am', 'are', phrase)
  elif ' my ' in phrase:
    return re.sub('my','your', phrase)
  elif ' your ' in phrase:
    return re.sub('your','mine', phrase)
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
  message = message.replace("?", "")
  if message in responses:
    return random.choice(responses[message])
  elif check_pattern(message):
    return "{}".format(check_pattern(message))
  else: 
    return random.choice(["Hmmm", "Anyway", "That is very interesting","I don't understand"])

def send_message(message):
  print("You: {}".format(message))
  time.sleep(random.randint(0,3))
  print("ALIE: {}".format(respond(message)))
  
while True:
  send_message(input())




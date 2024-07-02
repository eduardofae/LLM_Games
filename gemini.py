"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import os
import key

genai.configure(api_key=key.api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model_f = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

model_c = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

tool     = "Python"
template = f"In {tool}, create the following game:\n"
game     = "It's a game named jdv. In this game, 2 players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw."
task     = template + game
arquive  = "gemini.py"
outputs  = "test"

def get_critcs(codigo):
  feedback.send_message(f"Give a feedback about this game, made on {tool}:\n{codigo}\n\nWhich was developed to fullfill this task:\n{task}\nRemember it has to be in {tool} and it has to follow the stipulated rules")
  return feedback.last.text

def save_result(result, type):
  f = open(f"{outputs}/{type}.py", "w")
  f.write(result)
  f.close()
  print(f"{type} was generated with success!")

def make_dir(path):
  if not os.path.isdir(path): 
    os.makedirs(path) 

def start():
  print(f"Starting new generation!")
  coder    = model_c.start_chat(history=[])
  feedback = model_f.start_chat(history=[])
  return [coder, feedback]

try:
  os.system('cls')
  make_dir(outputs)
  [coder, feedback] = start()

  coder.send_message(task)
  save_result(coder.last.text, "first_out")

  print(f"Starting feedback loop:")
  for i in range(5):
    print(f"Starting feedback loop iteration {i}")
    code   = coder.last.text
    critcs = get_critcs(code)
    coder.send_message(f"Rectify this game, made on {tool}:\n{code}\n\nFollowing the criticism:\n{critcs}\n\nThe game has to be in {tool}")
  
  save_result(coder.last.text, "last_out")
except Exception as e:
  os.system(f"python {arquive}")
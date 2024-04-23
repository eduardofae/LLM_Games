"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyC9VobGRKnbPZ0EUvsoPNm965J-VjqjOQk")

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
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model_f = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

model_c = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

coder = model_c.start_chat(history=[])
feedback = model_f.start_chat(history=[])

tool     = "Python"
template = "In " + tool + " , create the following game:\n"
# game     = "It's a game named jdv. In this game, 2 players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw."
game     = "It's a game named pong. In this game, 2 players take turns placing their pieces at the lowest free space of any collumn of a 10x10 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw."
task     = template + game
coder.send_message(task)

import os
if not os.path.isdir("outputs"): 
    os.makedirs("outputs") 

f = open("outputs/first_out.py", "w")
f.write(coder.last.text[coder.last.text.find('\n')+1:coder.last.text.rfind('\n')])
f.close()

def get_critcs(codigo):
  feedback.send_message("Give a feedback about this game, made on " + tool + ":\n" + codigo + "\n\nWhich was developed to fullfill this task:\n" + task + "\nRemember it has to be in " + tool + " and it has to follow the stipulated rules")
  return feedback.last.text

iter = 10
while iter > 0:
  codigo = coder.last.text
  critcs = get_critcs(codigo)
  coder.send_message("Rectify this game, made on " + tool + ":\n" + codigo + "\n\nFollowing the criticism:\n" + critcs + "\n\nThe game has to be in " + tool)
  iter -= 1

f = open("outputs/final_out.py", "w")
f.write(coder.last.text[coder.last.text.find('\n')+1:coder.last.text.rfind('\n')])
f.close()
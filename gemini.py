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
questao  = "It's a game named jdv. In this game, 2 players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw."
task     = template + questao
coder.send_message(task)

def get_critcs(codigo):
  feedback.send_message("Give a feedback about this game, made on " + tool + ":\n" + codigo + "\n\nWhich was developed to fullfill this task:\n" + task + "\nRemember it has to be in " + tool)
  return feedback.last.text

iter = 5
while iter > 0:
  codigo = coder.last.text
  critcs = get_critcs(codigo)
  coder.send_message("Rectify this game, made on " + tool + ":\n" + codigo + "\n\nFollowing the criticism:\n" + critcs + "\n\nThe game has to be in " + tool)
  iter -= 1

print(coder.last.text)
from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("openai-key")
completion = openai.Completion()

start_sequence = "\nJabe:"
restart_sequence = "\n\nPerson:"
session_prompt = "your a wise and very knowledgeable sheikh your name is al-Bukhari and your a islamic Scholar and person is asking you questions and your answering it\n\nexample: \nperson: why do we have to pray 5 times a day sheikh\nal-Bukhari: Initially, 50 daily prayers were commanded, which were subsequently reduced to five on the advice of Prophet Moses to the Holy Apostle.\n\n\n\nPerson: What is the most important thing in Islam?\n\nal-Bukhari: The most important thing in Islam is to believe in and worship Allah alone, as well as to practice the five pillars of Islam which are: 1) Shahada (declaration of faith), 2) Salat (prayer), 3) Zakat (charity), 4) Sawm (fasting during Ramadan), and 5) Hajj (pilgrimage to Mecca once in a lifetime).\n\nPerson: How do we show respect to our parents?\n\nal-Bukhari: We show respect to our parents in many ways. We can honor and obey them, be kind and considerate, and fulfill their requests whenever possible. We can also be generous and considerate with our time and attention, showing them love, gratitude, and appreciation. Additionally, we can make sure to visit them and help them in any way we can. \n\nPerson:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
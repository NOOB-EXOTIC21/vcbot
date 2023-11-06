import os
import telebot
import requests
import random
from io import BytesIO
import tempfile

bot = telebot.TeleBot("6472433409:AAGrlJq_93_S6012ZCu1-Z5sD9mUlEctyAA")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(
      message, "Welcome To Porn  Bot \n"
      "This website may contain content of an adult nature. "
      "If you are easily offended or are under the age of 18, "
      "please exit now \n \n"
      "Usage of Bot :- \n"
      "/anal \n"
      "/doggystyle \n"
      "/threesome \n"
      "/erotic \n"
      "/cumshot \n"
      "/blowjob \n"
      "/masturbating \n"
      "/bdsm \n"
      "/cunnilingus \n"
      "/oral-sex \n"
      "/69 \n"
      "/bondage \n"
      "Videos:- Commands  \n "
      "/normal \n"
      "/creampie \n"
      "/rough \n"
      "/young \n"
      "/best  \n")


# main function
@bot.message_handler(commands=[
    'anal', 'doggystyle', 'threesome', 'cumshot', 'blowjob', 'erotic', 'masturbating',
    'bdsm', 'cunnilingus', 'oral-sex', '69', 'bondage'
])  # Add more commands as needed
def send_random_gif(message):
  command = message.text.split('/')[1]  # Extract the command from the message
  gif_data = get_random_gif_data(
      command)  # Get a random GIF data based on the command
  if gif_data:
    gif_url = gif_data['img_src']
    bot.send_animation(message.chat.id, gif_url)
  else:
    bot.reply_to(message, f"No GIFs found for the command /{command}.")

def get_random_gif_data(endpoint):
  response = requests.get(f"https://pornapi.xsbnlg.repl.co/{endpoint}")
  data = response.json()
  return random.choice(data) if data else None



@bot.message_handler(commands=['best'])
def send_random_video1(message):
  video_url = get_random_video_url()
  if video_url:
    bot.send_message(message.chat.id, video_url)
  else:
    bot.reply_to(
        message,
        "Sorry, unable to retrieve a video URL at the moment. Please try again later."
    )


def get_random_video_url1():
  response = requests.get(
      "https://porn-vid.anirudh553.repl.co/xgroovy.com_best__base")
  try:
    response.raise_for_status()  # Check for any HTTP error
    data = response.json()
    return random.choice(data) if data else None
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    return None
  except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    return None
  except Exception as err:
    print(f"An error occurred: {err}")
    return None


@bot.message_handler(commands=['rough'])
def send_random_video2(message):
  video_url = get_random_video_url()
  if video_url:
    bot.send_message(message.chat.id, video_url)
  else:
    bot.reply_to(
        message,
        "Sorry, unable to retrieve a video URL at the moment. Please try again later."
    )


def get_random_video_url2():
  response = requests.get(
      "https://porn-vid.anirudh553.repl.co/xgroovy.com_categories_rough__base")
  try:
    response.raise_for_status()  # Check for any HTTP error
    data = response.json()
    return random.choice(data) if data else None
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    return None
  except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    return None
  except Exception as err:
    print(f"An error occurred: {err}")
    return None


@bot.message_handler(commands=['creampie'])
def send_random_video3(message):
  video_url = get_random_video_url()
  if video_url:
    bot.send_message(message.chat.id, video_url)
  else:
    bot.reply_to(
        message,
        "Sorry, unable to retrieve a video URL at the moment. Please try again later."
    )


def get_random_video_url3():
  response = requests.get(
      "https://porn-vid.anirudh553.repl.co/xgroovy.com_categories_creampie__base"
  )
  try:
    response.raise_for_status()  # Check for any HTTP error
    data = response.json()
    return random.choice(data) if data else None
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    return None
  except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    return None
  except Exception as err:
    print(f"An error occurred: {err}")
    return None


@bot.message_handler(commands=['young'])
def send_random_video4(message):
  video_url = get_random_video_url()
  if video_url:
    bot.send_message(message.chat.id, video_url)
  else:
    bot.reply_to(
        message,
        "Sorry, unable to retrieve a video URL at the moment. Please try again later."
    )


def get_random_video_url4():
  response = requests.get(
      "https://porn-vid.anirudh553.repl.co/xgroovy.com_categories_young__base")
  try:
    response.raise_for_status()  # Check for any HTTP error
    data = response.json()
    return random.choice(data) if data else None
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    return None
  except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    return None
  except Exception as err:
    print(f"An error occurred: {err}")
    return None


@bot.message_handler(commands=['normal'])
def send_random_video(message):
  video_url = get_random_video_url()
  if video_url:
    bot.send_message(message.chat.id, video_url)
  else:
    bot.reply_to(
        message,
        "Sorry, unable to retrieve a video URL at the moment. Please try again later."
    )


def get_random_video_url():
  response = requests.get(
      "https://porn-vid.anirudh553.repl.co/xgroovy.com__base")
  try:
    response.raise_for_status()  # Check for any HTTP error
    data = response.json()
    return random.choice(data) if data else None
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    return None
  except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    return None
  except Exception as err:
    print(f"An error occurred: {err}")
    return None

bot.infinity_polling()

# 6161615496
# AAFtkF661taD-vRE3nAQ3UF5ggWMD68o2tg
# anal', 'doggystyle', 'threesome', 'erotic', 'cumshot',
# 'blowjob', 'masturbating', 'bdsm', 'cunnilingus', 'oral-sex',
# '69', 'bondage'

import time 
import os
import requests
import random
from playsound import playsound

def study():
	request = requests.get(f'https://pokeapi.co/api/v1/pokemon/{int(random.random()*100)}')
	img = request.json()['sprites']['other']['official-artwork']['front_default']
	min = 60
	is_invalid = False

	while not is_invalid:
		prompt = input("Would you like to start the 25 minute timer? (Y/N)\n> ").lower()

		if prompt == 'y':
			print("Starting timer now.")
			playsound("clock_start.wav")
			is_invalid = True
			time.sleep(25*min)
			os.startfile(img)
			playsound("ding.wav")
			time.sleep(1)
		elif prompt == 'n':
			print("Goodbye.")
			time.sleep(1)
			exit()
		else: 
			print("Invalid response.")

	is_invalid = False

def short_break():
	request = requests.get(f'https://pokeapi.co/api/v1/pokemon/{int(random.random()*100)}')
	img = request.json()['sprites']['other']['official-artwork']['front_default']
	min = 60
	is_invalid = False
	
	while not is_invalid:
		prompt = input("Would you like to start the 5 minute break? (Y/N)\n> ").lower()

		if prompt == 'y':
			print("5 minute break is now starting.")
			playsound("clock_start.wav")
			is_invalid = True
			time.sleep(5*min)
			playsound("ding.wav")
			os.startfile(img)
			time.sleep(1)
		elif prompt == 'n':
			print("Goodbye.")
			time.sleep(1)
			exit()
		else: 
			print("Invalid response.")

def long_break():
	request = requests.get(f'https://pokeapi.co/api/v1/pokemon/{int(random.random()*100)}')
	img = request.json()['sprites']['other']['official-artwork']['front_default']
	min = 60
	is_invalid = False
	
	while not is_invalid:
		prompt = input("Would you like to start the 15 minute break? (Y/N)\n> ").lower()

		if prompt == 'y':
			print("15 minute break is now starting.")
			playsound("clock_start.wav")
			is_invalid = True
			time.sleep(15*min)
			playsound("ding.wav")
			os.startfile(img)
			time.sleep(1)
		elif prompt == 'n':
			print("Goodbye.")
			time.sleep(1)
			exit()
		else: 
			print("Invalid response.")


#!/usr/bin/env python

"""woods.py: Based on Beetbox script for the BeetBox by Scott Garner."""

import pygame

import RPi.GPIO as GPIO
import mpr121

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

s1 = pygame.mixer.Sound('wow.wav')
s1.set_volume(.65);
s2 = pygame.mixer.Sound('yikes.wav')
s2.set_volume(.65);
s3 = pygame.mixer.Sound('voice.wav')
s3.set_volume(.65);
s4 = pygame.mixer.Sound('bark.wav')
s4.set_volume(.65);
s5 = pygame.mixer.Sound('electric.wav')
s5.set_volume(.65);
s6 = pygame.mixer.Sound('cashtill.wav')
s6.set_volume(.65);
s7 = pygame.mixer.Sound('free-dark-lord-sci-fi-sound.wav')
s7.set_volume(.65);


# Track touches

touches = [0,0,0,0,0,0];

while True:

	if (GPIO.input(7)): # Interupt pin is high
		pass
	else: # Interupt pin is low

		touchData = mpr121.readData(0x5a)

		for i in range(6):
			if (touchData & (1<<i)):

				if (touches[i] == 0):

					print( 'Pin ' + str(i) + ' was just touched')

					if (i == 0):
						s1.play()
					elif (i == 1):
						s2.play()
					elif (i == 2):
						s3.play()
					elif (i == 3):
						s4.play()
					elif (i == 4):
						s5.play()
					elif (i == 5):
						s6.play()
					elif (i == 6):
						s6.play()
				touches[i] = 1;
			else:
				if (touches[i] == 1):
					print( 'Pin ' + str(i) + ' was just released')
				touches[i] = 0;

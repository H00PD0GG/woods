#!/usr/bin/env python

#Python script based on Scott Garners Beetbox and SKpang Ledchaser

import pygame
import RPi.GPIO as GPIO
import mpr121
import smbus
import sys
import getopt
import time

bus = smbus.SMBus(1)
address = 0x20
bus.write_byte_data(0x20,0x00,0x00) #Bank A as Outputs
bus.write_byte_data(0x20,0x01,0x00) #Bank B as Outputs

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x10
mpr121.REL_THRESH = 0x13
mpr121.setup(0x5a)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

s1 = pygame.mixer.Sound('bird_caw2.wav')
s1.set_volume(.05);
s2 = pygame.mixer.Sound('bird_chirp.wav')
s2.set_volume(.05);
s3 = pygame.mixer.Sound('kick_01.wav')
s3.set_volume(.05);
s4 = pygame.mixer.Sound('owl1.wav')
s4.set_volume(.05);
s5 = pygame.mixer.Sound('peacock.wav')
s5.set_volume(.05);
s6 = pygame.mixer.Sound('snare_01.wav')
s6.set_volume(.05);
s7 = pygame.mixer.Sound('H_closedhat_01.wav')
s7.set_volume(.05);


# Track touches

touches = [0,0,0,0,0,0,0,0];

def set_led(data,bank):
	if bank == 1:
		bus.write_byte_data(address,0x12,data)
        else:
                bus.write_byte_data(address,0x13,data)
        return

delay = 0.2


while True:

	if (GPIO.input(7)): # Interupt pin is high
		pass
	else: # Interupt pin is low

		touchData = mpr121.readData(0x5a)

		for i in range(8):
			if (touchData & (1<<i)):

				if (touches[i] == 0):

					print( 'Pin ' + str(i) + ' was just touched')

					if (i == 0):
						s1.play()
						set_led(1,0)
						time.sleep(delay)
						set_led(0,0)
					elif (i == 1):
						s2.play()
						set_led(2,0)
						time.sleep(delay)
						set_led(0,0)
					elif (i == 2):
						s3.play()
						set_led(4,0)
						time.sleep(delay)
						set_led(0,0)
					elif (i == 3):
						s4.play()
						set_led(8,0)
						time.sleep(delay)
						set_led(0,0)
					elif (i == 4):
						s5.play()
						set_led(16,0)
						time.sleep(delay)
						set_led(0,0)
					elif (i == 5):
						s6.play()
						set_led(32,0)
						time.sleep(delay)
						set_led(0,0)
					elif (i == 6):
						s6.play()
						set_led(64,0)
						time.sleep(delay)
						set_led(0,0)
					elif (i == 7):
						s7.play()
						set_led(128,0)
						time.sleep(delay)
						set_led(0,0)
					
				touches[i] = 1;
			else:
				if (touches[i] == 1):
					print( 'Pin ' + str(i) + ' was just released')
				touches[i] = 0;

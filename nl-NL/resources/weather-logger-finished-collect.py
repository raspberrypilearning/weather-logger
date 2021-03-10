from sense_hat import *
from time import sleep

sense = SenseHat()

while True:
  mijnbestand = open('weather.txt', 'a')
  mijnbestand.write(sense.temp)
  mijnbestand.write('\n')
  mijnbestand.close()
  sleep(5)


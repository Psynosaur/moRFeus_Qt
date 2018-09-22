from moRFeusQt import mrf
from time import sleep


# morse code source : https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/resources/morse_code.py
class MorseCode(object):
    def __init__(self, device):
        self.device = device
        self.moRFeus = mrf.MoRFeus(self.device)

    # added some additional morse code characters '@','!' and '&'
    MORSE = {' ': ' ', "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-',
             '/': '-..-.', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..', '9': '----.', ':': '---...', ';': '-.-.-.', '?': '..--..',
             'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
             'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
             'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--.-', '+': '.-.-.',
             '=': '-...-', '@': '.--.-.', '!': '-.-.--', '&': '.-...'}

    def switch(self, state):
        self.moRFeus.message(self.moRFeus.SET, self.moRFeus.funcCurrent, state)

    def dot(self):
        self.switch(1)
        sleep(0.2)
        self.switch(0)
        sleep(0.2)

    def dash(self):
        self.switch(1)
        sleep(0.5)
        self.switch(0)
        sleep(0.2)

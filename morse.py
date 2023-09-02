import pyaudio
import numpy as np
import keyboard
import random
import time


class Morse:
    def __init__(self) -> None:
        self.morses = {"a":"._",
                       "b":"_...",
                       "c":"_._.",
                       "d":"_..",
                       "e":".",
                       "f":".._.",
                       "g":"__.",
                       "h":"....",
                       "i":"..",
                       "j":".___",
                       "k":"_._",
                       "l":"._..",
                       "m":"__",
                       "n":"_.",
                       "o":"___",
                       "p":".__.",
                       "q":"__._",
                       "r":"._.",
                       "s":"...",
                       "t":"_",
                       "u":".._",
                       "v":"..._",
                       "w":".__",
                       "x":"_.._",
                       "y":"_.__",
                       "z":"__..",
                       "1":".____",
                       "2":"..___",
                       "3":"...__",
                       "4":"...._",
                       "5":".....",
                       "6":"_....",
                       "7":"__...",
                       "8":"___..",
                       "9":"____.",
                       "0":"_____"}
        
        self.p = pyaudio.PyAudio()
        self.frequency = 440 * 4/3
        self.speed = 10
        self.fs = 44100
        self.lives = 3
        self.morse_characters = list("abcdefghijklmnopqrstuvwxyz1234567890")
    
    
    def play(self, char:str, vol:float=0.5):
        for m in self.morses[char]:
            if m == ".":
                dur = 1 / self.speed
            else:
                dur = 3 / self.speed
            
            samples = (np.sin(2 * np.pi * np.arange(self.fs * dur) * self.frequency / self.fs)).astype(np.float32)
            output_bytes = (vol * samples).tobytes()
            
            stream = self.p.open(format=pyaudio.paFloat32,
                                 channels=1,
                                 rate=self.fs,
                                 output=True)
    
            stream.write(output_bytes)


    def train_morse(self):
        while len(self.morse_characters) > 0:
            char = random.choice(self.morse_characters)
            
            time.sleep(0.4)
            self.play(char)
            
            while True:
                key = keyboard.read_key().lower()
                print(key)
                if key == "esc":
                    return 0
                    
                elif key == char:
                    print("\033[32mcorrect\033[0m")
                    self.morse_characters.remove(char)
                    break
                
                elif not key in self.morse_characters:
                    continue
                
                else:
                    print(f"\033[31mincorrect\033[0m it was {char}")
                    break
    
    
    def write_to_morse(self):
        while True:
            key = keyboard.read_key().lower()
            if key == "esc":
                return 0
            
            word = input("write something to hear it in morse code: ").lower()

            for letter in word:
                if letter == " ":
                    time.sleep(7 / self.speed)
                if not letter in self.morse_characters:
                    break
                else:
                    self.play(letter)
                    time.sleep(3 / self.speed)
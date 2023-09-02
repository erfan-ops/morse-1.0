from morse import Morse
from sys import exit
import threading
import keyboard


def volume_control (m: Morse):
    while True:
        k = keyboard.read_key()
        if k == "=":
            m.speed += 1
        elif k == "-":
            m.speed -= 1
        elif k == "esc":
            m.p.terminate()
            exit()


def main (m: Morse):
    while True:
        game_mode = input("1.training\n2.playing\n3.quit\n> ")
        
        if game_mode == "3":
            m.p.terminate()
            exit()
        
        elif game_mode == "1":
            m.train_morse()
        elif game_mode == "2":
            m.write_to_morse()
        
        else:
            print(f"{game_mode} is not a valid option")


if __name__ == '__main__':
    m = Morse()
    x = threading.Thread(target=volume_control, args=(m,))
    x.start()
    main(m)
    
import pygame.mixer as mixer
import pygame
import threading
from datetime import datetime
from time import time


def play_music(file, stopper):
    try:
        pygame.init()
        mixer.init()
        mixer.music.load(file)

        # Start playing the music in a loop
        mixer.music.play(-1)

        # Create an event to signal when the user types "Drank" and presses Enter
        user_input_event = threading.Event()

        def wait_for_user_input():
            user_input = input(
                "Enter 'drank' (case-insensitive) to stop the music: ")
            if user_input.lower() == stopper:
                user_input_event.set()

        # Start a separate thread to wait for the user's input
        user_input_thread = threading.Thread(target=wait_for_user_input)
        user_input_thread.start()

        # Wait for the user to type "Drank" and press Enter
        user_input_thread.join()
        print("User input thread completed.")  # Debug statement

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        mixer.music.stop()
        mixer.quit()
        print("Music stopped and mixer quit.")  # Debug statement


def my_log(msg):
    with open('mylog.txt', 'a') as f:
        f.write(f"{msg}   {datetime.now()} \n")


if __name__ == '__main__':
    water = 'water.mp3'
    eye = 'eyes.mp3'
    phy = 'phy.mp3'
    watersec = 5
    init_water = time()
    while True:
        if time() - init_water == watersec:
            play_music(phy, 'drank')
            my_log('Drank water at')
        if time() - 
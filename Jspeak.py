import asyncio
import threading
import os
import edge_tts
import pygame

VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024

def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path, 'wb'):
                pass  # Try to close the file handle
            os.remove(file_path)
            break  # If successful, break out of the loop
        except Exception as e:
            print(f"Error removing file: {e}")
            attempts += 1

async def amain(TEXT, output_file) -> None:
    try:
        # Main function
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(output_file)

        # Use threading to run audio playback in a separate thread
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()  # Wait for the audio playback thread to finish

    except Exception as e:
        print(f"Error: {e}")

    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        # Initialize pygame
        pygame.init()

        # Open the audio file
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)

        # Play the audio
        sound.play()

        # Wait for the audio to finish playing
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

        # Quit pygame
        pygame.quit()

    except Exception as e:
        print(f"Error during audio playback: {e}")

def jspeak(TEXT, output_file=None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"
    asyncio.run(amain(TEXT, output_file))



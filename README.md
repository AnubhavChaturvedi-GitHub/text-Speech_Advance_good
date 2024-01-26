# Text-to-Speech Code Readme

## Overview
This Python code provides a simple interface for converting text to speech using the Microsoft Azure Speech Service through the `edge_tts` library. It utilizes asyncio for asynchronous operations and includes functionality for audio playback using Pygame.

## Prerequisites
Before using this code, make sure you have the following installed:

- Python 3.7 or later
- The `edge_tts` library
- Pygame library

Install the required libraries using the following commands:
```bash
pip install edge-tts pygame
```

## Usage

### Setting up the Voice and Buffer Size
Adjust the `VOICE` and `BUFFER_SIZE` constants at the beginning of the script to customize the voice and buffer size for audio playback.

```python
VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024
```

### Functionality

#### `amain(TEXT, output_file) -> None`
This asynchronous function takes text input (`TEXT`) and an optional output file path (`output_file`) as arguments. It utilizes the `edge_tts` library to convert the text to speech and plays the resulting audio using Pygame in a separate thread.

#### `play_audio(file_path)`
This function initializes Pygame, opens the specified audio file, plays the audio, and waits for the playback to finish. It then quits Pygame.

#### `remove_file(file_path)`
A utility function that attempts to remove a file with error handling.

#### `jspeak(TEXT, output_file=None)`
This is the main entry point for using the code. It calls `amain` using the provided text and output file path. If no output file path is provided, a default path (`speak.mp3`) within the current working directory is used.

## Example
```python
from tts_code import jspeak

text_to_speak = "Hello, how are you today?"
jspeak(text_to_speak)
```

## Notes
- Ensure your system has audio support and speakers connected for audio playback.
- Handle exceptions appropriately, especially when dealing with the removal of temporary files and audio playback.

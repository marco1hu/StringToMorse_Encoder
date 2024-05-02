Features
Converts text to Morse code based on a predefined dictionary.
Generates audio signals for dots, dashes, and spaces using sine waves.
Plays the Morse code representation of the phrase using PyAudio.
Allows users to adjust sound parameters (volume, frequency) to some extent (modifications needed in the code).


Usage
Install Required Libraries:
You might need to install the pyaudio library using pip install pyaudio before running the script.

Run the Script:
Save the code as a Python file (e.g., morse_code_player.py).
Open a terminal or command prompt and navigate to the directory where you saved the file.
Run the script using python morse_code_player.py.

Enter a Phrase:
The script will prompt you to enter a phrase.
Type your desired phrase and press Enter.

Listen to the Morse Code:
The script will convert the phrase to Morse code and play the corresponding audio signals for each letter, symbol, and space.

How it Works
The script defines a Morse code dictionary mapping characters to their Morse code representations (dots and dashes). When you enter a phrase, it iterates through each character and looks up the corresponding Morse code in the dictionary. For each Morse code symbol (dot or dash), it generates audio samples using a sine wave with a specific frequency and duration. Finally, it plays the generated audio data through your speakers using PyAudio, creating a sequence of beeps representing the Morse code of your phrase.

Limitations
The script currently uses fixed timings for dots, dashes, and pauses. You cannot adjust these timings directly.
Error handling is not implemented. Entering characters not present in the dictionary might cause errors. 

Contributing
Feel free to fork this repository and make improvements! You can add functionalities like:
User-configurable sound parameters (volume, frequency, timing)
Error handling for invalid user input
Support for additional symbols or languages using Morse code

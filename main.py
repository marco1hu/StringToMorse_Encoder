import numpy as np
import pyaudio     # You might need to install pyaudio (e.g., pip install pyaudio)
import time


# Morse code dictionary mapping characters to their Morse code representation
morse_code = {
  'A': '.-', 'B': '-...',
  'C': '-.-.', 'D': '-..', 'E': '.',
  'F': '..-.', 'G': '--.', 'H': '....',
  'I': '..', 'J': '.---', 'K': '-.-',
  'L': '.-..', 'M': '--', 'N': '-.',
  'O': '---', 'P': '.--.', 'Q': '--.-',
  'R': '.-.', 'S': '...', 'T': '-',
  'U': '..-', 'V': '...-', 'W': '.--',
  'X': '-..-', 'Y': '-.--', 'Z': '--..',
  ' ': '/', '.': '.-.-.-', ',': '--..--',
  '?': '..--..', '-': '-....-', '/': '-..-.',
  '(': '-.--.', ')': '-.--.-'
}

# Get user input for the phrase and convert it to uppercase for easier dictionary lookup
phrase = input("Insert a phrase: ").upper()

# Initialize PyAudio object
p = pyaudio.PyAudio()

# Define sound parameters:
volume = 0.1  # Adjust for desired intensity (0 to 1)
fs = 44100     # Sample rate (common audio format)
f = 600        # Frequency of the generated tone (Hz)

# Open an audio stream for playback
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# Loop through each character in the phrase
for letter in phrase:
  duration = 0  # Initialize total sound duration for the letter

  # Loop through each Morse code symbol for the current letter
  for char in morse_code[letter]:
    if char == ".":
      duration = 0.1  # Set duration for a dot (1 time unit)
    elif char == "-":
      duration = 0.3  # Set duration for a dash (3 times a dot's duration)

    # Generate audio samples for the symbol using sine wave (explained below)
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs) * volume).astype(np.float32).tobytes()

    # Write the generated sound data to the audio stream
    stream.write(samples)

    # Add a short pause between symbols
    time.sleep(0.1)

  # Add a pause between letters (longer than symbol pause)
  time.sleep(0.2)  # 0.1 + 0.2 = total 3 time units

  # Handle spaces with a longer pause (7 times a dot's duration)
  if letter == " ":
    time.sleep(0.4)

# Close the audio stream and terminate PyAudio object
stream.close()
p.terminate()

# **Explanation of sound generation with numpy.sin:**
# This part creates a sine wave with the desired frequency (`f`) and duration (`duration`).
# - np.sin generates an array of sine wave values.
# - 2 * np.pi: mathematical constant pi used in the sine wave formula.
# - np.arange(fs * duration) creates an array of time steps within the symbol duration.
# - f / fs: scales the frequency to the sample rate.
# - The result is multiplied by the volume and converted to a byte array suitable for audio output.
import winsound
import time

user_message = input("What is your message? ")
user_message = user_message.lower()
new_message = []

for letter in user_message:

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", ".", ",", "?", "'", "!", "/", "(", ")", "&", ":", ";", "=", "+", "-", '"', "$"]

    morse = ["•- ", "-••• ", "-•-• ", "-•• ", "• ", "••-• ", "--• ", "•••• ", "•• ", "•--- ", "-•- ", "•-•• ", "-- ", "-• ", "--- ", "•--• ", "-••- ", "•-• ", "••• ", "- ", "••- ", "•••- ", "•-- ", "-••- ", "-•-- ", "--•• ", "/ ", "•---- ", "••--- ", "•••-- ", "••••- ", "••••• ", "-•••• ", "--••• ", "---•• ", "----• ", "----- ", "•--•-• ", "•-•-•- ", "--••-- ", "••--•• ", "•---• ", "-•-•-- ", "-••-• ", "-•--• ", "••--•- ", "•-••• ", "---••• ", "-•-•-• ", "-•••- ", "•-•-• ", "-••••- ", "••--•- ", "•-••-• ", "•••-••- "]

    if letter in alphabet:
        old = alphabet.index(letter)
        morse_letter = morse[old]
        new_message.append(morse_letter)
    else:
        pass

print("".join(new_message))

audio_prompt = input("Would you like to hear your message in morse code? ")
audio_prompt = audio_prompt.lower()

if audio_prompt == "yes":
    for word in new_message:
        for char in word:
            if char == "•":
                winsound.Beep(600, 100)
                time.sleep(0.1)
            elif char == "-":
                winsound.Beep(600, 300)
                time.sleep(0.1)
            elif char == "/":
                time.sleep(0.7)
            elif char == " ":
                time.sleep(0.3)
            else:
                time.sleep(0.1)
else:
    pass
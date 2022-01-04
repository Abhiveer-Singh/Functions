import gtts
from playsound import playsound
text = input("Type Something: ")
t1 = gtts.gTTS(f"{text}")
t1.save("welcome.mp3")
playsound("welcome.mp3")
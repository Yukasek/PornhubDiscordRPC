from pypresence import *
from time import time
from os import system

system("title PornhubDiscordRPC")

activity_list = ["Gorące mamuśki",
                 "Step sister",
                 "Gwiazdy porno",
                 "Porno w HD"]

print("Wybierz aktywność z listy\n")

for i in activity_list:
    print(f"{activity_list.index(i) + 1} - {i}")

while True:
    try:
        activity_input = int(input("\n>>> "))
        activity = activity_list[activity_input - 1]
        break
    except ValueError or IndexError:
        print("Wprowadź poprawny numer")

timestamp = int(time())
CLIENT_ID = 782680726121611266
RPC = Presence(CLIENT_ID)
RPC.connect()

RPC.update(start=timestamp,
           large_image="logo",
           large_text="Pornhub",
           details="Ogląda",
           state=activity)

input("Aby zamknąć program naciśnij Enter...")

# importing the module
import wikipedia
import webbrowser
import pyjokes
import datetime

def he_function():
    try:
        a = input("ask me any question you want:")
        result = wikipedia.summary(a, sentences=2)
        print(result)
    except wikipedia.exceptions.PageError:
        print("No ans found")
m = input("should i continue,yes,no:")
while m == "yes":
    print("i am jarvis your assistant")
    print("what can i do for you")
    print("a. play a game")
    print("b.play a music")
    print("c.ask a doubt")
    print("d.jokes")
    print("type any letter you want")
    c = input("what can i do for you:")
    if c == "a":
        webbrowser.open('https://www.roblox.com/home')

    if c == "b":
        webbrowser.open('https://music.youtube.com')

    if c == "c":
        he_function()

    if c == "d":
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        print(My_joke)
    if "hi" in c:
        print("hello sir")
    if "play music" in c:
        webbrowser.open('https://music.youtube.com')
    if "play" in c:
        webbrowser.open('https://www.roblox.com/home')
    if "doubt" in c:
        he_function()
    if "open google" in c:
        webbrowser.open('https://www.google.co.in/?client=safari')
    if "bad" in c:
        print("sorry i will do my best next time")
    if "my friend" in c:
        print("yes sure")
    if "help" in c:
        print("sure sir")
    if "thank" in c:
        print("thank you sir")
    if "lets chat" in c:
        name=input("what is your name:")
        if name == "quit":
            quit()
        print("saving your name...")
        birth=input("when is your birthday:")
        print("saving your birthday...")


    if "time" in c:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)





    if c == "what is your name":
        print("my name is python")
    m = input("should i continue,yes,no:")
else:
    quit()

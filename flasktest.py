from flask import Flask
from flask_ask import Ask,statement,question,session, audio
import json
import requests
import time
import unidecode
import cv2
import os
import subprocess, sys
import scripts.label_image

app = Flask(__name__)

ask = Ask(app,"/do_the_magic")

@app.route('/')
def homepage():
    return "You are on homepage"

@ask.launch
def start_skill():
    welcome_message = "Welcome to Hogwarts. Do you want to see some magic?"
    return question(welcome_message)

@ask.intent("YesIntent")
def yes_intent():
    camera = cv2.VideoCapture(0)
    return_value,image = camera.read()
    cv2.imwrite("C:/Users/punitbawal/Desktop/tensorflowpoet/opencv.png", image)
    camera.release()
    #cv2.destroyAllWindows
    scripts.label_image.load_main()
    f = open("C:/Users/punitbawal/Desktop/tensorflowpoet/myresult.txt","r")
    scor = f.readlines()
    f.close()
    #print("Scor",scor)
    if scor[0] == 'gryffindor':
        return statement("Hmmm....Bravery, Daring, Nerve and Chivalry. You are like a lion. But you also hold intelligence and wit. Are you a Ravenclaw? Naaaa, I see fire in you. Just like Harry, I choose GRYFFINDOR!!!")
    if scor[0] == 'hufflepuff':
        return statement("Oh wow, Helga would have liked you! Hard work, dedication and patience. Dumbledore likes you, but you are not as daring as you should have been. I see you know your way around herbs!!! Hmmm, I choose HUFFLEPUFF!!!!")
    if scor[0] == 'ravenclaw':
        return statement("Winds are blowing!!! Ohh I see you are solving puzzles in your head? So intelligent and witty!!! I have no doubt, you are a RAVENCLAW!!!!")
    if scor[0] == 'slytherin':
        return statement("Dark Dark Dark!!! Cunning as a snake and ambitious like your ancestors. Professor snape looks happy. But will you be more succesfull at Gryffindor? I choose......SLYTHERIN!!!!")
    return statement(scor[0])

@ask.intent("NoIntent")
def no_intent():
    return statement("Get out of Hogwarts!!! You are a Muggle!")

if __name__ == '__main__':
    app.run(debug=True)

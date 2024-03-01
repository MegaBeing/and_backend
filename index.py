from flask import Flask
from firebase import firebase
import os
from os.path import join, dirname
from dotenv import load_dotenv
from openai import OpenAI
app = Flask(__name__)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv()
FIREBASE_URL = os.environ['FIREBASE_URL']
firebase = firebase.FirebaseApplication(FIREBASE_URL, None)


# @app.route("/auth/<user>",methods = ['GET'])
# def get_user(user):
#     # call to firebase to get user
#     # authenticate the user
#     # pass true/false inside json
#     pass

@app.route("/auth-create/<user>",methods = ['POST'])
def create_user(user):
    # call to firebase to search for existing user
    # if present 
        # return user-exists to json
    # else
        # create the user and pass successful to json
    pass

@app.route("/<user>/all",methods = ["GET"])
def get_all_section_and_task(user):
    # call to FireBase to fetch all the sections related to that user
    # if present 
        # send the json response
    # else 
        # send empty json
    pass

@app.route("/prompt/")
def prompt_gpt():
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    print(completion.choices[0].message)
    pass

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)

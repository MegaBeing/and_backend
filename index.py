# Requirements 
# -----------------------------------------------------------------------
from flask import Flask,request,jsonify,redirect
from firebase import firebase
import os
from os.path import join, dirname
from dotenv import load_dotenv
from openai import OpenAI

# initializations
# -----------------------------------------------------------------------
app = Flask(__name__)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv()
FIREBASE_URL = os.environ['FIREBASE_URL']
firebase = firebase.FirebaseApplication(FIREBASE_URL, None)

# Requests
# -----------------------------------------------------------------------

@app.route("/user/",methods = ['GET'])
def get_users():
    """ 
    Get all users
    """
    response = firebase.get('user/',None)
    return response

@app.route("/user/<id>",methods = ['GET','POST'])
def get_specific_user(id):
    """
    Get specific user
    """
    if request.method == 'GET':
        response = firebase.get(f'user/{id}',None)
        return response
    else:
        data = request.data
        firebase.patch(f'users/{id}',data)
        return jsonify({"message":"Operation Completed"})

@app.route("/prompt/",methods = ['GET','POST'])
def prompt_gpt():
    """
    POST: Generate Prompt according to User Requests
    GET: List of Prompts Generated by the user
    """
    if request.method == 'POST':
        req = request.form
        user = req['user_id']
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are an to-do list creator which takes the prompt as user requirements for creating the list of tasks which are given priority as low, medium and high and you have to divide it into 4 categories given by the user"},
                    {"role": "user", "content": req['message']}
            ]
        )
        data = firebase.get(f'/users/{user}',None)
        count = data['prompt']['count']
        data['prompt'][count+1]={"generated_value":completion.choices[0].message.content,
                                    "Prompt":data['message'],
                                }
        data['prompt']['count']+=1
        firebase.patch(f'/users/{user}/prompt/',data)
        return jsonify({"Response":completion.choices[0].message.content})
    else:
        user = request.args.getlist('user_id')
        user = int(user[0])
        data = firebase.get(f'users/{user}/prompt',None)
        return jsonify(data)

# Server Configs
# -----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)

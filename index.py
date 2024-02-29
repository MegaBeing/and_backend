from Flask import flask

app = flask(__name__)

@app.route("/auth/<user>",methods = ['GET'])
def get_user(user):
    # call to firebase to get user
    # authenticate the user
    # pass true/false inside json
    pass

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

@app.route("/prompt/<user>/create",method = ['POST'])
def prompt_gpt(user):
    # call firebase for user information
    # openAI api key
    # generate a prompt using string 
    # Send request to openAi api
    # get the request answer
    # return response as json 
    pass

if '__main__'==__name__:
    app.run(host = '0.0.0.0',debug = True)

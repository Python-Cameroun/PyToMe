# i create this file because i wanted to separate the 
# main workflow of the application and his differents modules
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def start():
    if request.args.get("email") != "None":
        f=open("data/suscribers.ptm", "a+")
        if f.mode == 'a+':
            f.write(request.args.get("email") + "\n")
            f.close()
            return '{message: "Email saved successfully!"}'
        else:
            return '{message: "Something went wrong with the file!"}'
    else:
        return '{message: "Error, Email not found!"}'
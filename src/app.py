import os
from flask import Flask, request, render_template
from application import app

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
    return render_template('index.html')

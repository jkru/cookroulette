from flask import Flask, request, session, render_template, g, redirect, url_for, flash
import jinja2
import os
import random
#import recipe_classes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/whee")
def whee():
    recipe_kinds = {"Quiche" : recipe_classes.Quiche(),"Gratin" : recipe_classes.Gratin(),"Risotto" : recipe_classes.Risotto()}
    recipe_struct = random.choice(["Quiche","Gratin","Risotto"])
    
    this_recipe = recipe_kinds[recipe_struct]
    

    html = render_template("whee.html", recipe = recipe_struct )
    return html

def populate_recipe(recipe_struct):
    recipe_dict = {}

    return recipe_dict

if __name__ == "__main__":
    app.run(debug=True)


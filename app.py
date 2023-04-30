#Import required libraries
import os
from flask import Flask,render_template

#set the static and template folder path 
template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'DIS')
template_dir = os.path.join(template_dir, 'DIS')
template_dir = os.path.join(template_dir, 'Project')
template_dir = os.path.join(template_dir, 'html')
STATIC_DIR = os.path.abspath('../DIS/Project/static')
app= Flask(__name__,template_folder=template_dir,static_folder=STATIC_DIR)

# Main page load
@app.route("/",methods=['post','get'])
def index():
    return  render_template("index.html")
#Html page page redirect
@app.route("/home")
def home():
    return render_template("home.html")
#AI maker page redirect
@app.route("/AI_Maker")
def AIMaker():
    return render_template("AI Maker.html")
#Upcoming 
@app.route("/upcoming")
def upcoming():
    return render_template("Upcoming.html")

#About page redirect
@app.route("/About")
def uAbout():
    return render_template("About.html")
#contact page redirect
@app.route("/Contact")
def Contact():
    return render_template("Feedback.html")
# graph page redirect
@app.route("/Graph")
def graph():
    return render_template("graph.html")

     
 
# main flask run 
if __name__ == "__main__":
    app.run(debug=True)

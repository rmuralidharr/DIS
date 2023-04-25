import os
from flask import Flask,render_template
template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(template_dir)
template_dir = os.path.join(template_dir, 'DIS')
print(template_dir)
template_dir = os.path.join(template_dir, 'DIS')
print(template_dir)
template_dir = os.path.join(template_dir, 'Project')

print(template_dir)
template_dir = os.path.join(template_dir, 'html')
print(template_dir)
STATIC_DIR = os.path.abspath('../DIS/Project/static')
print(STATIC_DIR)
app= Flask(__name__,template_folder=template_dir,static_folder=STATIC_DIR)





@app.route("/wow")
def home1():
    return "wow"

@app.route("/",methods=['post','get'])
def index():
    return  render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/AI_Maker")
def AIMaker():
    return render_template("AI Maker.html")

@app.route("/upcoming")
def upcoming():
    return render_template("Upcoming.html")


@app.route("/About")
def uAbout():
    return render_template("About.html")

@app.route("/Contact")
def Contact():
    return render_template("Feedback.html")

@app.route("/Graph")
def graph():
    return render_template("graph.html")



# @app.route("/hello/<name>")
# def hello_there(name): 
#     now=datetime.now()
#     formatted_now =now.strftime("%A,%d %B, %Y at %x" )
#     match_object =re.match("[a-zA-Z]+",name)
#     if match_object:
#         clean_name=match_object.group()
#     else:
#         clean_name="Friend"
#     return "hello ther0ed'e, "+name+"! It's"+formatted_now
    
# @app.route("/html1/<name>")
# def hello(name):
#     return render_template("hello_there.html",name=name,date=datetime.now())

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("static.json")
     
 

if __name__ == "__main__":
    app.run(debug=True)


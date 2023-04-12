from flask import Flask,render_template
app= Flask(__name__)

@app.route("/")
def home():
    return  "hello world"

@app.route("/hello/<name>")
def hello_there(name): 
    now=datetime.now()
    formatted_now =now.strftime("%A,%d %B, %Y at %x" )
    match_object =re.match("[a-zA-Z]+",name)
    if match_object:
        clean_name=match_object.group()
    else:
        clean_name="Friend"
    return "hello ther0ed'e, "+name+"! It's"+formatted_now
    
@app.route("/html1/<name>")
def hello(name):
    return render_template("hello_there.html",name=name,date=datetime.now())

@app.route("/api/data")
def get_data():
    return app.send_static_file("static.json")
     
 

if __name__ == "__main__":
    app.run()


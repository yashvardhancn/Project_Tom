from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("newindex.html")

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    img=request.files['img']
    img.save("img.jpg")
    return "welcome into predict"

if __name__=="__main__":
    app.run(debug=True)



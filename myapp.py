# https://blog.paperspace.com/deploying-deep-learning-models-flask-web-python/


from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", var1="yash")



@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/uploader",methods=['GET','POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        filename=secure_filename(f.filename)

        f.save(filename)
        #   showmyImage(f.filename)
        #   return f"{f.filename}"
        #   https://stackoverflow.com/questions/46785507/python-flask-display-image-on-a-html-page
               
        return render_template("showimage.html",userimage=filename)
        

    # return "<h1>entered upload file"




if __name__=="__main__":
    app.run(debug=True)




# @app.route("/<name>")
# def user(name):
#     return f'hello {name}'

# @app.route("/admin")
# def admin():
#     # return redirect(url_for("home"))
#     return redirect(url_for("user",name="yash"))



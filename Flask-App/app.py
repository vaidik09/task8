from flask import Flask, render_template, request
import os 
from deeplearning import OCR
from numberplate import user_details
# webserver gateway interface
app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')

text=""
@app.route('/',methods=['POST','GET'])
def index():
    global text
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text = OCR(path_save,filename)
        print(type(text))
        

        return render_template('index.html',upload=True,upload_image=filename,text=text)

    return render_template('index.html',upload=False)

@app.route("/get_details")
def get_details():
   print(len(text))
   print(type(text))
   final = text
   details = user_details(final)

   return render_template(
                 "details.html", 
                 model = details[0],
                 regyear = details[1],
                 engsize = details[2],
                 sea = details[3],
                 idfi = details[4],
                 engnum = details[5],
                 fuelt = details[6],
                 regdate = details[7],
                 loc = details[8]
         )
if __name__ =="__main__":
    app.run(debug=True)
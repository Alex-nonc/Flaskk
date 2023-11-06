import os
from queue import Empty
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

upload_folder = 'uploads/'
finally_uploads = 'finally_uploads/'

if not os.path.exists(upload_folder):
   os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder
allowed_extensions = ['mp3', 'wav', 'ogg', 'wma']

def check_file_extension(filename):
    return filename.split('.')[-1] in allowed_extensions

@app.route('/') 
def upload(): 
    return render_template("upload.html", word="absolutely")

@app.route('/success', methods=['GET','POST']) 
def success(): 
    if request.method == 'POST': 
        f = request.files['file']
        if check_file_extension(f.filename):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)))
            f.save(os.path.join(finally_uploads ,secure_filename(f.filename)))
        return render_template("success.html", name=f.filename)
    return send_file(finally_uploads + "8.docx", as_attachment=True)
          		
if __name__ == '__main__':
   app.run()
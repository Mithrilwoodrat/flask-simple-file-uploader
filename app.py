# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename

__basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(__basedir, 'uploads')
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['py', 'txt', 'jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        fileobj = request.files['file']
        filename = fileobj.filename
        print filename
        if fileobj and allowed_file(filename):
            filename = secure_filename(filename)
            FILE_URI = os.path.join(UPLOAD_FOLDER, filename)
            fileobj.save(FILE_URI)
            return jsonify(status='SUCCESS',filename=filename,origin=filename)
        else:
            return jsonify(status='FAILED',error='UNSUPPORTED FILE TYPE')

if __name__ == "__main__":
    app.run(debug=True)
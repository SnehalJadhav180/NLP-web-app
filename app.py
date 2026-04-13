from flask import Flask, request, redirect, url_for, send_file, render_template
import os
from werkzeug.utils import secure_filename
from utils import process_text_file
import json

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        pos_tags = process_text_file(file_path)
        result_filename = filename.rsplit('.', 1)[0] + '_pos.json'
        result_filepath = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)
        with open(result_filepath, 'w') as result_file:
            json.dump(pos_tags, result_file)
        return send_file(result_filepath, as_attachment=True)
    else:
        return redirect(request.url)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

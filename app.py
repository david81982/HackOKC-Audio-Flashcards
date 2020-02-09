import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from forms import KeyWordForm
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = "yeet4321"
db = SQLAlchemy(app)



AUDIO_UPLOAD_FOLDER = 'uploads/audio'
TEXT_UPLOAD_FOLDER = 'uploads/text'
ALLOWED_EXTENSIONS = {'txt','mp3'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Get files from user 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(AUDIO_UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_audio_file', filename=filename))
    return render_template('home.html')

@app.route('/uploads/audio/<filename>')
def uploaded_audio_file(filename):
    return send_from_directory(AUDIO_UPLOAD_FOLDER, filename)


@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    form = KeyWordForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('keywords.html', form=form)

   
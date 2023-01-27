from flask import Flask, request, url_for, flash, \
    redirect, render_template;
from werkzeug.utils import secure_filename;
import runmodel;
import os;

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000;
app.secret_key = '655d15c18354e0e34d31c48d55fba78e19c44492a88d69e856fc3f302e0dbb14';

# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg',}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/image", methods=['Get'])
def downloadImage():
    print('in downloadImage', request.method);
    args = request.args;
    print(type(args));
    args = args.to_dict();
    print(type(args))
    imagepath = args.get("imagepath")
    # imagepath = request.form['imagepath'];
    # imagepath = '0a4f38c94dd63cd8e5b9209dc9892146.jpg';
    print(imagepath);
    return "<p> yarab 9!</p>"

@app.route("/detectroadimage", methods=['Get','Post'])
def detectRoadImage():
    if request.method == 'POST':
        print('in uploadImage', request.method);
        UPLOAD_FOLDER = './uploads'
        # imagepath = request.form['imagepath'];
        # imagepath = '0a4f38c94dd63cd8e5b9209dc9892146.jpg';
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # filename = file.filename
            filePath = os.path.join(UPLOAD_FOLDER, filename);
            file.save(filePath);
            # return redirect(url_for('download_file', name=filename))
            print(filePath);
            detectionLabels = runmodel.roadBalzerDetect(filePath, filename);
            flash('detection succes');
            flash(detectionLabels);
            return redirect(url_for('detectRoadImage'))
    else:
        return render_template('index.html')

# @app.route('/', methods=['GET'])
# def uploadForm():
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

with app.test_request_context():
    print(url_for('detectRoadImage', imagepath='000ed1547634a24f09f22530065d46c9.jpg'))

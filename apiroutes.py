from flask import Flask;
from flask import request;
from flask import url_for;
import runmodel;

app = Flask(__name__)

@app.route("/image", methods=['Get'])
def image():
    print('in api', request.method);
    args = request.args;
    print(type(args));
    args = args.to_dict();
    print(type(args))
    imagepath = args.get("imagepath")
    # imagepath = request.form['imagepath'];
    # imagepath = '0a4f38c94dd63cd8e5b9209dc9892146.jpg';
    print(imagepath);
    runmodel.downloadImage(imagepath);
    return "<p> yarab 9!</p>"

with app.test_request_context():
    print(url_for('image', imagepath='000ed1547634a24f09f22530065d46c9.jpg'))

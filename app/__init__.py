import os
from app.src.document import Document
from app.src.document import document_from_file
from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask import flash
from flask import jsonify
from flask import request
from flask import render_template
from flask import abort, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['xml'])

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine()
db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)

@app.route('/')
def index():
    app.logger.info('HomePage requested')
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_errors_in_uploaded_document(request):
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if not allowed_file(file.filename):
        return 'Not a valid file, make sure its an XML Word file'
    return None


def save_file(file):
    upload_folder = app.config['UPLOAD_FOLDER']
    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    return [filepath, filename]

def create_document(request):
    filepath,filename = save_file(request.files['file'])
    document = document_from_file(filepath)
    document.save()
    print(document.id)
    return redirect(url_for('document',id=document.id))

def index_documents(request):
    documents = Document.objects
    return render_template("documents.html", documents=documents)

def get_document(request,id):
    document = Document.objects.get(id=id)
    return render_template("document.html", document=document)

@app.route('/documents', methods=['GET','POST'])
def documents():
    if request.method == 'POST':
        errors = get_errors_in_uploaded_document(request)
        if errors is None:
            return create_document(request)
        else:
            flash(errors)
            return redirect(url_for('documents'))
    if request.method == 'GET':
        return index_documents(request)

@app.route('/documents/<id>', methods=['GET'])
def document(id):
    return get_document(request,id)

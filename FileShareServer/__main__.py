from flask import Flask, send_from_directory, render_template, abort, request, redirect, url_for
from PathContainer import PathContainer
from werkzeug import secure_filename
import os


app = Flask(__name__)

def handle_get(path):
    pc = PathContainer(path)
    if pc.isfile: 
        return send_from_directory('/',pc.real_path[1:], as_attachment=True)
    elif pc.isdir:
        return render_template('dirlist.html', all_children=pc.get_dir_contents())
    return abort(400)

def handle_post(path, request):
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join(path,filename))
    return redirect(url_for('home_test', path=path))

@app.route('/', defaults={'path': ''}, methods=["GET", "POST"])
@app.route('/<path:path>', methods=["GET", "POST"])
def home_test(path):
    if request.method == "POST":
        return handle_post(path, request)
    else:
        return handle_get(path)
    
if __name__ == "__main__":
    app.run(debug=True)

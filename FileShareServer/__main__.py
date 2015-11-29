from flask import Flask, send_from_directory, render_template
from PathContainer import PathContainer

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=["GET"])
@app.route('/<path:path>', methods=["GET"])
def home_test(path):
    pc = PathContainer(path)
    if pc.isfile: 
        return send_from_directory('/',pc.real_path[1:], as_attachment=True)
    elif pc.isdir:
        return render_template('dirlist.html', all_children=pc.get_dir_contents())
    return pc.real_path, 200

if __name__ == "__main__":
    app.run(debug=True)

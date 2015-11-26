from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

def get_dir_info(real_dir_path):
    all_contents = os.listdir(real_dir_path)
    return {'all_contents' : all_contents, 'dir_path':real_dir_path}

@app.route('/', defaults={'path': ''}, methods=["GET"])
@app.route('/<path:path>', methods=["GET"])
def home_test(path):
    realPath = os.path.realpath(path)
    if os.path.isfile(realPath):
        return send_from_directory('/',realPath[1:])
    elif os.path.isdir(realPath):
        return render_template('dirlist.html', **get_dir_info(realPath))
    return realPath, 200

if __name__ == "__main__":
    app.run(debug=True)

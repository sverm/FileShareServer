from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

def get_dir_info(realPath, path):
    all_paths = os.listdir(realPath) # get all the directory contents' names
    all_paths = [os.path.join(path,child_path) for child_path in all_paths] #get the full relative path
    all_paths = [os.path.join(child_path,'') #add a '/' after the directories
            if os.path.isdir(child_path)
            else child_path
            for child_path in all_paths]
    return {'all_paths' : all_paths}

@app.route('/', defaults={'path': ''}, methods=["GET"])
@app.route('/<path:path>', methods=["GET"])
def home_test(path):
    realPath = os.path.realpath(path)
    if os.path.isfile(realPath):
        return send_from_directory('/',realPath[1:], as_attachment=True)
    elif os.path.isdir(realPath):
        return render_template('dirlist.html', **get_dir_info(realPath, path))
    return realPath, 200

if __name__ == "__main__":
    app.run(debug=True)

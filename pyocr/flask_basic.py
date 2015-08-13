from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/index.html')

@app.route('/')

def webprint():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run()

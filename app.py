
from flask import Flask, render_template, request

app=Flask(__name__, template_folder='template')

@app.route('/',methods =["POST", "GET"])
def get_artist():
    artist = request.form.get("artist")
    return render_template("index.html", artist=artist)

if __name__ == '__main__':
    app.run(debug=True)

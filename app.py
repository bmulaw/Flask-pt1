
from flask import Flask, render_template, request

app=Flask(__name__, template_folder='template')

@app.route('/',methods =["POST", "GET"])
def get_artist():
    name = str(request.form.get("name"))
    artist = request.form.get("artist")
    return render_template("index.html", name=name, artist=artist)

if __name__ == '__main__':
    app.run(debug=True)
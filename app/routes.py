from app import app

@app.route("/")
def index():
    return '<h1>Hello docker</h1>'
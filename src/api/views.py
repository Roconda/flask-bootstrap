from api import app


@app.route("/", methods=['GET'])
def get_method():
    return "Hello world!"

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/setcookie')
def set_cookie():
    resp = make_response("Cookie is set")
    resp.set_cookie('username', 'JohnDoe')
    return resp

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username')
    return f"Hello {username}" if username else "No cookie found!"

@app.route('/deletecookie')
def delete_cookie():
    resp = make_response("Cookie deleted")
    resp.set_cookie('username', '', expires=0)
    return resp

if __name__ == "__main__":
    app.run(debug=True)

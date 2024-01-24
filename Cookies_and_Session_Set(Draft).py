import os

from flask import Flask, make_response, request, session
import datetime

app = Flask(__name__)

# start Session
app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机数种子，用于生成sessionid


@app.route("/")  # Decorator, "/" -> root path
def hello_world():
    return "<p> Hello World!</p>"


# set_cookies
@app.route('/cookie')
def cookie():
    response = make_response("Set Cookies Successfully")
    response.set_cookie()
    return response


# get_cookies
@app.route("/get_cookie")
def get_cookie():
    cookies = request.cookies
    cookies_dict = request.cookies.to_dict()



# delete_cookies
@app.route("/del_cookie")
def delete_cookie():
    response = make_response("Delete Cookies Successfully")
    response.delete_cookie()
    return response

# add_session
@app.route("/add_session")
def add_session():
    session['username'] = None
    return "Set Session successfully"
# get_session
@app.route("/get_session")
def get_session():
    print(session)
    return "Get Session Successfully"
#delete_session
@app.route("/del_session")
def del_session():
    session.clear()
    return "Clear Session Successfully"








if __name__ == '__main__':
    app.run(debug=True)

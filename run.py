from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My name is Conan!<br>This domain is for sale.<br>Contact me by mail:whhxf@126.com<br>Thank you!'

if __name__ == '__main__':
    app.run()

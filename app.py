from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome to RoyalWings Flight Booking</h1>
    <p>Flight search and booking coming soon!</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

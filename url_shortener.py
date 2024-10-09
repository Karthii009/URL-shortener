from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)

# Dictionary to store shortened URLs
url_mapping = {}

def generate_short_id(length=6):
    """Generate a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_id = generate_short_id()
    url_mapping[short_id] = long_url
    return f"Shortened URL: <a href='/{short_id}'>http://127.0.0.1:5000/{short_id}</a>"

@app.route('/<short_id>')
def redirect_url(short_id):
    long_url = url_mapping.get(short_id)
    if long_url:
        return redirect(long_url)
    return "URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)

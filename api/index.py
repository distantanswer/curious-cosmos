from flask import Flask

app = Flask(__name__)

@app.route('/api/')
def hello_world():
    return 'Hello, world!', 200, {'Content-Type': 'text/plain'}


# If using Vercel, you need to expose the `app` object as `app` for it to recognize it.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


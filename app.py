from flask import Flask, render_template
from boto.s3.connection import S3Connection
import os

s3 = S3Connection(os.environ['API_KEY'], os.environ['API_KEY2'])

app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

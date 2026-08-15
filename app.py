from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>AI Video Pro MAX</h1>
    <p>✅ Website Live hai</p>
    <p>Ab AI Video + Voice + Payment add hoga</p>
    """

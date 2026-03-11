from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "DevSecOps Pipeline Running"


if __name__ == "__main__":
    # Binding to all interfaces is required for container runtime.
    app.run(host="0.0.0.0", port=5000)  # nosec B104

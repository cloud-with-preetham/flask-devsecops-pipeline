from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    # Binding to all interfaces is required for container runtime.
    app.run(host="0.0.0.0", port=80)  # nosec B104

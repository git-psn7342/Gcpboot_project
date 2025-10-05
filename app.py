from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from Cloud Run! This is our customer-facing website."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
# temp test for Cloud Build trigger
print("Trigger testing for prod pipeline")

from flask import Flask, render_template

# Cria o aplicativo
app = Flask(__name__)

# Rota principal do site (quando acessa /)
@app.route("/")
def home():
    return render_template("index.html")

# Roda o site
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
#Gera

app = Flask(__name__)

@app.get("/")
def main_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

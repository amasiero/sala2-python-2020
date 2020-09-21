from flask import Flask, render_template

app = Flask('Meu aplicativo Flask')


@app.route('/')
def index():
    return render_template('index.html', nome='Andrey Masiero')


app.run()

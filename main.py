from flask import Flask
import random

facts_list = [
    'Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
    'Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati',
    'Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja']

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1>Did You Know?</h1>'
            '<a href="/randomfact">View a random fact!</a><br>'
            '<a href="/catpic">Want a random cat?</a>')

@app.route("/randomfact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/catpic")
def cat_picture():
    return f'<img src="https://cataas.com/cat" alt="Meow!">'

app.run(debug=True)
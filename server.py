from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
   return render_template('./index.html')


@app.route('/register')
def blog():
   return render_template('./register.html')



from flask import Flask, render_template, request, url_for
import psycopg2
from werkzeug.utils import redirect

app = Flask(__name__)

con = psycopg2.connect(
    host="localhost",
    port="5432",
    database="j-com",
    user="postgres",
    password="admin"
    )


@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('index.html')


@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        Username = request.form['Username']
        email = request.form['email']
        password = request.form['password']
        cur = con.cursor()
        cur.execute("insert into register (username,email,password) values (%s,%s,%s)", (Username, email, password))
        con.commit()
        cur.close()

        return redirect(url_for('register'))
    else:
        return render_template("register.html")
#con.close( )
#Last line
if __name__ == '__main__':
    app.run(debug=True)




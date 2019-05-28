from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super secret key"
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return "Logged in as " + username + "<br><b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href ='/login'></b>click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      session['email'] = request.form['email']
      return redirect('/foi')
   return render_template(<nome_html>,<dados>)
   """
	
   <form action="/login" method="post">
        Nome:
        <input type="text" name="username"></input>
        E-mail:
        <input type="text" name="email"></input>
        <input type="submit" value="dale" >
    </form>
	
    """
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   #session.clear()
   session.pop('username', None)
   return redirect('/')

@app.route("/foi", methods=["GET", "POST"])
def tabela():
    dados = []
    n = session['username']
    e = session['email']
    dados.append(n)
    dados.append(e)
    return render_template("table.html", dados=dados)

@app.route("/a", methods=["GET", "POST"])
def formulario():
    
    return render_template("form.html")
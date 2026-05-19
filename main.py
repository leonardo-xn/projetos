# pip install Flask
# pip install flask-socketio

from flask import Flask, render_template, request, session, redirect, url_for
import banco
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "bola"

socketio = SocketIO(app)

rooms = {}

# =========================
# GERAR CÓDIGO DA SALA
# =========================

def generate_unique_code(length):

    while True:

        code = ""

        for _ in range(length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            break

    return code


# =========================
# LOGIN
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    session.clear()

    if request.method == "POST":

        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        # verifica login
        if not banco.login(usuario, senha):

            return render_template(
                "APS.html",
                error="Usuário ou senha inválidos"
            )

        # verifica se digitou usuário
        if not usuario:

            return render_template(
                "APS.html",
                error="Digite seu usuário!"
            )

        # cria sala padrão
        room = "KBTG"

        # cria a sala se não existir
        if room not in rooms:

            rooms[room] = {
                "members": 0,
                "messages": []
            }

        # salva sessão
        session["room"] = room
        session["name"] = usuario

        # vai para o chat
        return redirect(url_for("biomas"))

    return render_template("APS.html")


# =========================
# CADASTRO
# =========================

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        # salva no banco
        if banco.cadastrar(usuario, senha):

            return redirect(url_for("home"))

        return render_template(
            "Cadastro.html",
            error="Usuário já existe"
        )

    return render_template("Cadastro.html")


# =========================
# CHAT
# =========================

@app.route("/biomas")
def biomas():

    room = session.get("room")

    if room not in rooms:
        return redirect(url_for("home"))

    return render_template(
        "biomas.html",
        messages=rooms[room]["messages"]
    )


# =========================
# SOCKET.IO
# =========================

@socketio.on("message")
def message(data):

    room = session.get("room")

    if room not in rooms:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }

    send(content, to=room)

    rooms[room]["messages"].append(content)

    print(f"{session.get('name')} disse: {data['data']}")


# =========================
# CONECTAR
# =========================

@socketio.on("connect")
def connect(auth):

    room = session.get("room")
    name = session.get("name")

    if not room or not name:
        return

    if room not in rooms:

        leave_room(room)

        return

    join_room(room)

    send(
        {
            "name": name,
            "message": "Entrou na sala"
        },
        to=room
    )

    rooms[room]["members"] += 1

    print(f"{name} entrou na sala {room}")


# =========================
# DESCONECTAR
# =========================

@socketio.on("disconnect")
def disconnect():

    room = session.get("room")
    name = session.get("name")

    leave_room(room)

    if room in rooms:

        rooms[room]["members"] -= 1

        if rooms[room]["members"] <= 0:
            del rooms[room]

    send(
        {
            "name": name,
            "message": "Saiu da sala"
        },
        to=room
    )

    print(f"{name} saiu da sala {room}")


# =========================
# RODAR
# =========================

if __name__ == "__main__":

    socketio.run(app, debug=True)
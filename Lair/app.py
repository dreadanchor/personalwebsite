from flask import Flask, render_template, redirect, request, abort
from markdown import markdown
from data.missions import missions
from datetime import datetime
from static.tools.csv import load_quests, save_quests
from docs.stack import stack

app = Flask(__name__)

USERNAME = "ANCHOR!"

# Parte que decide a saudação do site, colocar em uma função em tools depois
horario = datetime.now().hour # Isso devolve o horário atual em hora
if horario < 12:
    mensagem = f"Bom dia, {USERNAME}"
elif horario < 18:
    mensagem = f"Boa tarde, {USERNAME}"
else:
    mensagem = f"Boa noite, {USERNAME}"

@app.route("/")
def main():
    dia = datetime.now().weekday() # Isso devolve um número de 0-6, de segunda a domingo

    todays_missions = missions[-1][dia] # Uma lista com as missões de hoje, de acordo com a rotina mais nova

    # Agora as quests

    quests = load_quests()

    return render_template(
    "main.html",
    mensagem = mensagem,
    todays_missions = todays_missions,
    quests = quests
    )

@app.post("/add")
def add():

    quests = load_quests()

    quests.append({
        "titulo": request.form["titulo"],
        "descricao": request.form["descricao"]
    })

    save_quests(quests)

    return redirect("/")

@app.post("/delete/<int:index>")
def delete(index):

    quests = load_quests()

    quests.pop(index)

    save_quests(quests)

    return redirect("/")

@app.route("/mydocs")
def docpage():

    return render_template(
    "mydocs.html",
    mensagem = mensagem,
    stack = stack
    )

@app.route("/mydocs/<string:skill>")
def docs(skill):

    if skill not in stack:
        abort(404)

    with open(stack[skill]["doc"], "r", encoding="utf-8") as file:
        texto = file.read()

    html = markdown(
        texto,
        extensions=[
            "fenced_code",
            "tables",
            "toc",
            "codehilite"
        ]
    )

    return render_template(
        "doc.html",
        mensagem = mensagem,
        conteudo=html
    )

# Isso aqui sempre fica no final do app.py
if __name__ == "__main__":
    app.run(debug=True)

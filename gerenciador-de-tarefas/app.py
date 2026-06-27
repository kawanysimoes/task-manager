from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":
        nova_tarefa = request.form.get("tarefa")

        if nova_tarefa:
            tarefas.append(nova_tarefa)

    return render_template("index.html", tarefas=tarefas)


@app.route("/excluir/<int:id>")
def excluir(id):

    if 0 <= id < len(tarefas):
        tarefas.pop(id)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


tarefas = []

def criar_tarefa(nome):
    tarefas.append(nome)

def listar_tarefas():
    return tarefas

def excluir_tarefa(nome):
    if nome in tarefas:
        tarefas.remove(nome)

if __name__ == "__main__":
    criar_tarefa("Estudar ADS")
    print(listar_tarefas())

from src.app import criar_tarefa, listar_tarefas

def test_criar_tarefa():
    criar_tarefa("Teste")
    assert "Teste" in listar_tarefas()

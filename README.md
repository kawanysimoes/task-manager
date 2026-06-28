# Gerenciador de Tarefas

## Descrição

O Gerenciador de Tarefas é uma aplicação web desenvolvida em Python utilizando o framework Flask. O sistema permite o gerenciamento de tarefas por meio de uma interface simples e intuitiva, possibilitando adicionar, visualizar e organizar tarefas.

Este projeto foi desenvolvido como trabalho da disciplina do curso de Análise e Desenvolvimento de Sistemas (ADS).

---

##  Tecnologias Utilizadas

* Python 3.11
* Flask
* HTML5
* Git
* GitHub
* GitHub Actions
* Pytest

---

##  Estrutura do Projeto

```
gerenciador-de-tarefas/
│
├── app.py
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
└── README.md
```

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/kawanysimoes/task-manager.git
```

2. Entre na pasta do projeto:

```bash
cd gerenciador-de-tarefas
```

3. Instale as dependências:

```bash
pip install flask pytest
```

4. Execute a aplicação:

```bash
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## Executando os testes

Execute o seguinte comando:

```bash
python -m pytest
```

---

##  Integração Contínua

O projeto utiliza **GitHub Actions** para executar automaticamente os testes sempre que alterações são enviadas para o repositório.

---

## Autor

**Kawany Simões**

Projeto desenvolvido como atividade acadêmica do curso de Análise e Desenvolvimento de Sistemas (ADS).

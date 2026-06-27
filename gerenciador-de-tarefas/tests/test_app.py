from app import app

def test_pagina_inicial():

    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
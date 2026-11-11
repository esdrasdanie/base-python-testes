import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user

def test_serialize_user_completo():
    # Create a mock user object
    user = {
        "email": "teste@exemplo.com",
        "name": "Fulano",
        "address": "Rua A, 123",
        "role": "admin"
    }

    resultado = serialize_user(user)
    esperado = {
        "email": "teste@exemplo.com",
        "name": "Fulano",
        "address": "Rua A, 123",
        "role": "admin"
    }

    assert resultado == esperado

def test_serialize_user_campos_ausentes():
    user = {
        "email": "teste@exemplo.com",
    }
    resultado = serialize_user(user)
    esperado = {
        "email": "teste@exemplo.com",
        "name": "",
        "address": "",
        "role": "cliente" 
    }

    assert resultado == esperado

def test_serialize_user_email_ausente():
    user = {}
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente" 
    }
    assert resultado == esperado

def test_serialize_user_nome():
    with pytest.raises(AttributeError):
        serialize_user(None)

def test_serialize_user_valores_none():
    """Campos presentes mas com valor: None deve ser mantido"""
    user = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    assert resultado == esperado
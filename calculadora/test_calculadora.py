import allure
import pytest
from app import soma, divisao

def test_soma_positiva():
    with allure.step("Testando soma de dois números positivos"):
        resultado = soma(2, 3)
    allure.attach(str(resultado), name="Resultado de soma positiva", attachment_type=allure.attachment_type.TEXT)
    assert resultado == 5

def test_subtracao_negativa():
    with allure.step("Testando subtração de dois números negativos"):
        resultado = soma(-2, -3)
    allure.attach(str(resultado), name="Resultado de subtração negativa", attachment_type=allure.attachment_type.TEXT)
    assert resultado == -5

def test_divisão_zero():
    with allure.step("Testando divisão com zero"):
        with pytest.raises(
            ValueError, match="Não é possível dividir por zero"
        ) as erro:
            divisao(4, 0)
    allure.attach(str(erro.value), name="Erro de divisão com zero",attachment_type=allure.attachment_type.TEXT)

def test_soma_valor_alto():
    with allure.step("Testando soma de dois números positivos"):
            resultado = soma(123123, 1232312)
    allure.attach(str(resultado), name="Resultado de soma positiva", attachment_type=allure.attachment_type.TEXT)
    assert resultado == 13
    
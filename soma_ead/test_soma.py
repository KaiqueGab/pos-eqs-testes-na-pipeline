import allure
from app import soma

def test_soma_positiva():
    with allure.step("Testando soma de dois números positivos"):
        resultado = soma(2, 3)
    allure.attach(str(resultado), name="Resultado de soma positiva", attachment_type=allure.attachment_type.TEXT)
    assert resultado == 5

def test_soma_negativa():
    with allure.step("Testando soma de dois números positivos"):
        resultado = soma(-2, -3)
    allure.attach(str(resultado), name="Resultado de soma negativa", attachment_type=allure.attachment_type.TEXT)
    assert resultado == -5

def test_soma_zero():
    assert soma(0, 0) == 0

def test_soma_valor_alto():
    assert soma(23233, 23233) == 46466
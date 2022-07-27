"""
Exemplos de testes.

    - Criar função add
    - Testar função add
"""
import pytest


def add(num1, num2):
    """Add function."""
    return num1 + num2


@pytest.mark.parametrize("num1,num2, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (10000, 10000, 20000)
])
def test_add(num1, num2, expected):
    """Test add function."""
    assert add(num1, num2) == expected


def test_wrong_add():
    """Test add function."""
    assert add(2, 1) != 2


def nao_testa():
    """Nao testa devido ao nome da função estar fora dos padrões."""
    assert 1 == 1


class SaldoInsuficienteException(Exception):
    pass


class ContaCorrente:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException("Saldo insuficiente")
        self.saldo -= valor


@pytest.fixture
def nova_conta() -> ContaCorrente:
    return ContaCorrente()


@pytest.fixture
def nova_conta_100() -> ContaCorrente:
    return ContaCorrente(100)


def test_Conta_init(nova_conta):
    assert nova_conta.saldo == 0


def test_Conta_depositar(nova_conta_100):
    nova_conta_100.depositar(100)
    assert nova_conta_100.saldo == 200


def test_Conta_sacar(nova_conta_100):
    nova_conta_100.sacar(100)
    assert nova_conta_100.saldo == 0


@pytest.mark.parametrize("deposito, saque, saldo",
    [
        (100, 100, 0),
        (200, 100, 100),
        (200, 0, 200),
    ]
)
def test_Conta_transacoes(nova_conta, deposito, saque, saldo):
    nova_conta.depositar(deposito)
    nova_conta.sacar(saque)
    assert nova_conta.saldo == saldo


def test_saldo_insuficiente(nova_conta_100):
    with pytest.raises(SaldoInsuficienteException):
        nova_conta_100.sacar(200)

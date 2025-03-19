"""
Instruções
Seu amigo Chandler pretende visitar países exóticos em todo o mundo. Infelizmente, as habilidades matemáticas dele não são muito boas. Ele está bastante preocupado em ser enganado em casas de câmbio durante a viagem – e quer que você crie uma calculadora de câmbio para ele. Aqui estão as especificações que ele passou para o aplicativo:

Tarefa 1: Estimar o valor após a troca

Crie a função exchange_money(), que recebe 2 parâmetros:

budget: a quantia de dinheiro que você planeja trocar.
exchange_rate: a quantidade de moeda local equivalente a uma unidade da moeda estrangeira.
Essa função deve retornar o valor da moeda após a troca.

Observação: Se sua moeda for USD e você quiser trocar USD por EUR com uma taxa de câmbio de 1.20, isso significa que 1.20 USD == 1 EUR.

>>> exchange_money(127.5, 1.2)
106.25

Tarefa 2: Calcular quanto dinheiro sobra após a troca
Crie a função get_change(), que recebe 2 parâmetros:

budget: quantia de dinheiro antes da troca.
exchanging_value: quantia de dinheiro que será retirada do orçamento para a troca.
Essa função deve retornar a quantia de dinheiro que sobra do orçamento.

>>> get_change(127.5, 120)
7.5

Tarefa 3: Calcular o valor das notas
Crie a função get_value_of_bills(), que recebe 2 parâmetros:

denomination: o valor de uma única nota.
number_of_bills: a quantidade total de notas.
Este guichê de câmbio só trabalha com dinheiro em certos incrementos. O total que você recebe precisa ser divisível pelo valor de uma “nota” ou unidade, o que pode deixar uma fração ou resto. Sua função deve retornar apenas o valor total das notas (excluindo valores fracionados) que o guichê devolveria. Infelizmente, o guichê fica com o restante/troco como um bônus extra.

>>> get_value_of_bills(5, 128)
640

Tarefa 4: Calcular o número de notas
Crie a função get_number_of_bills(), que recebe amount e denomination.
Esta função deve retornar a quantidade de notas que você consegue receber com base no valor inicial. Em outras palavras, quantas notas inteiras cabem nesse valor? Lembre-se de que você só pode receber notas inteiras, não frações, então é preciso dividir adequadamente. Na prática, você estará arredondando para baixo até o número inteiro mais próximo.

>>> get_number_of_bills(127.5, 5)
25

Tarefa 5: Calcular o valor restante após trocar em notas
Crie a função get_leftover_of_bills(), que recebe amount e denomination.
Essa função deve retornar o valor que sobra e não pode ser convertido em notas, considerando o valor inicial e a denominação informada. É muito importante saber exatamente quanto o guichê fica para si.

>>> get_leftover_of_bills(127.5, 20)
7.5

Tarefa 6: Calcular o valor após a troca
Crie a função exchangeable_value(), que recebe os parâmetros budget, exchange_rate, spread e denomination.

O spread é a porcentagem cobrada como taxa de câmbio, representada por um inteiro. Você precisa convertê-lo em decimal dividindo por 100. Se 1.00 EUR = 1.20 USD e o spread for 10, a taxa de câmbio efetiva será 1.00 EUR = 1.32 USD, pois 10% de 1.20 (ou seja, 0.12) é somado à taxa original, resultando em 1.32.

Esta função deve retornar o valor máximo que você consegue obter na nova moeda depois de aplicar a taxa de câmbio com o spread. Lembre-se de que a denominação da moeda é um número inteiro e não pode ser fracionada.

Observação: O valor retornado deve ser do tipo int.

>>> exchangeable_value(127.25, 1.20, 10, 20)
80
>>> exchangeable_value(127.25, 1.20, 5, 20)
95
"""

def exchange_money(budget, exchange_rate):
    """
    Calcula o valor da moeda estrangeira após a troca, sem considerar taxas adicionais.

    :param budget: float - o montante de dinheiro que você planeja trocar.
    :param exchange_rate: float - a taxa de câmbio, que indica quantos unidades da moeda local equivalem a 1 unidade da moeda estrangeira.
    :return: float - o valor obtido na nova moeda.
    """
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """
    Calcula a quantia de dinheiro que sobra após retirar um determinado valor para a troca.

    :param budget: float - a quantia de dinheiro disponível antes da troca.
    :param exchanging_value: float - o valor que será retirado do orçamento para a troca.
    :return: float - o valor restante após a troca.
    """
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """
    Calcula o valor total das notas que podem ser obtidas, com base no valor de cada cédula e na quantidade disponível.

    :param denomination: int - o valor de uma única cédula.
    :param number_of_bills: int - a quantidade de cédulas.
    :return: int - o valor total obtido multiplicando a denominação pelo número de cédulas.
    """
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    """
    Calcula quantas notas inteiras podem ser obtidas com uma quantia de dinheiro, dado o valor de cada cédula.

    :param amount: float - o montante total disponível.
    :param denomination: int - o valor de uma única cédula.
    :return: int - o número de cédulas inteiras que podem ser obtidas.
    """
    return int(amount // denomination)

def get_leftover_of_bills(amount, denomination):
    """
    Calcula o valor restante que não pode ser convertido em notas inteiras, com base na quantia total e na denominação.

    :param amount: float - o montante total disponível.
    :param denomination: int - o valor de uma única cédula.
    :return: float - o valor restante após converter para notas inteiras.
    """
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calcula o valor máximo que você pode obter na nova moeda após aplicar a taxa de câmbio com o spread.

    :param budget: float - o montante de dinheiro que você planeja trocar.
    :param exchange_rate: float - a taxa de câmbio original (valor da moeda estrangeira em relação à moeda local).
    :param spread: int - a porcentagem cobrada como taxa de câmbio.
    :param denomination: int - o valor de uma única cédula na nova moeda (não pode ser fracionada).
    :return: int - o valor máximo que pode ser obtido, em múltiplos da denominação.

    A função realiza os seguintes passos:
      1. Calcula a taxa de câmbio efetiva, somando o spread à taxa original:
           effective_rate = exchange_rate * (1 + spread/100)
      2. Converte o orçamento para a moeda estrangeira:
           converted_value = budget / effective_rate
      3. Calcula o maior valor que pode ser obtido usando apenas cédulas inteiras,
         isto é, o maior múltiplo de 'denomination' que não excede o valor convertido.
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    converted_value = budget / effective_rate
    exchangeable_amount = int(converted_value // denomination) * denomination
    return exchangeable_amount

def run_tests():
    """
    Executa uma série de testes simples para validar as funções da calculadora de câmbio.

    A função realiza as seguintes verificações:
      - Testa a função exchange_money com um orçamento de 127.5 e uma taxa de 1.2, 
        esperando o valor 106.25 (pois 127.5 / 1.2 = 106.25).
      - Testa a função get_change com um orçamento de 127.5 e um valor de troca de 120, 
        esperando o valor 7.5 (pois 127.5 - 120 = 7.5).
      - Testa a função get_value_of_bills com denominação 5 e 128 notas, 
        esperando o valor 640 (pois 5 * 128 = 640).
      - Testa a função get_number_of_bills com um montante de 127.5 e denominação 5, 
        esperando o valor 25 (pois 127.5 // 5 = 25).
      - Testa a função get_leftover_of_bills com um montante de 127.5 e denominação 20, 
        esperando o valor 7.5 (pois 127.5 % 20 = 7.5).
      - Testa a função exchangeable_value com um orçamento de 127.25, taxa de câmbio 1.20, 
        spread de 10 e denominação 20, esperando o valor 80.
    
    Se os resultados impressos corresponderem aos valores esperados, as funções estão funcionando corretamente.
    """
    print("exchange_money(127.5, 1.2):", exchange_money(127.5, 1.2))  # Esperado: 106.25
    print("get_change(127.5, 120):", get_change(127.5, 120))          # Esperado: 7.5
    print("get_value_of_bills(5, 128):", get_value_of_bills(5, 128))    # Esperado: 640
    print("get_number_of_bills(127.5, 5):", get_number_of_bills(127.5, 5))  # Esperado: 25
    print("get_leftover_of_bills(127.5, 20):", get_leftover_of_bills(127.5, 20))  # Esperado: 7.5
    print("exchangeable_value(127.25, 1.20, 10, 20):", exchangeable_value(127.25, 1.20, 10, 20))  # Esperado: 80

if __name__ == '__main__':
    run_tests()


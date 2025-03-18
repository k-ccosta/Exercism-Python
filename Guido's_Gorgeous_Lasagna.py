"""
Instruções:
Você irá escrever um código para ajudar a preparar uma lasanha maravilhosa, baseada no seu livro de receitas favorito.

1. Defina o tempo de cozimento esperado (em minutos) como uma constante:
Defina a constante EXPECTED_BAKE_TIME que representa quantos minutos a lasanha deve ficar no forno. Segundo seu livro de receitas, a lasanha deve assar por 40 minutos:

>>> print(EXPECTED_BAKE_TIME)
40

2. Calcule o tempo restante de cozimento (em minutos):
Complete a função bake_time_remaining() que recebe como argumento os minutos reais que a lasanha já está no forno e retorna quantos minutos ainda faltam para que ela termine de assar, com base na constante EXPECTED_BAKE_TIME.

>>> bake_time_remaining(30)
10

3. Calcule o tempo de preparo (em minutos):
Defina a função preparation_time_in_minutes() que recebe o número de camadas que você deseja adicionar à lasanha como argumento e retorna quantos minutos você gastará para prepará-las. Considere que cada camada leva 2 minutos para ser preparada.

>>> preparation_time_in_minutes(2)
4

4. Calcule o tempo total decorrido de cozimento (preparo + assar) em minutos:
Defina a função elapsed_time_in_minutes() que recebe dois parâmetros: number_of_layers (o número de camadas adicionadas à lasanha) e elapsed_bake_time (o número de minutos que a lasanha já está assando no forno). Esta função deve retornar o tempo total (em minutos) que você gastou no preparo e cozimento da lasanha.

>>> elapsed_time_in_minutes(3, 20)
26

5. Atualize a receita com observações:
Revise a receita, adicionando "notas" na forma de docstrings nas funções.

Exemplo:

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    \"\"\"Calcula o tempo total decorrido de cozimento.

    :param number_of_layers: int - o número de camadas na lasanha.
    :param elapsed_bake_time: int - o tempo já decorrido no cozimento.
    :return: int - o tempo total decorrido (em minutos) de preparo e cozimento.

    Esta função recebe dois inteiros representando o número de camadas da lasanha e o tempo já gasto no forno, calculando a soma do tempo de preparo e do tempo que a lasanha já passou assando.
    \"\"\" 
"""

# Constante que define o tempo de cozimento esperado (em minutos)
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """
    Calcula o tempo restante de cozimento da lasanha.

    :param elapsed_bake_time: int - o tempo (em minutos) que a lasanha já está assando.
    :return: int - o tempo restante (em minutos) para que a lasanha atinja o tempo de cozimento esperado.

    Esta função subtrai o tempo que a lasanha já passou no forno do tempo total de cozimento esperado.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Calcula o tempo total de preparo baseado no número de camadas da lasanha.

    :param number_of_layers: int - o número de camadas da lasanha.
    :return: int - o tempo total de preparo (em minutos), considerando que cada camada leva 2 minutos para ser preparada.

    Esta função multiplica o número de camadas pelo tempo de preparo por camada (2 minutos).
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calcula o tempo total decorrido de preparo e cozimento da lasanha.

    :param number_of_layers: int - o número de camadas da lasanha.
    :param elapsed_bake_time: int - o tempo (em minutos) que a lasanha já está assando.
    :return: int - a soma do tempo de preparo e do tempo de cozimento já decorrido.

    Esta função combina o tempo gasto para preparar as camadas com o tempo que a lasanha já passou assando.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

def run_tests():
    """
    Executa uma série de testes simples para validar as funções da receita de lasanha.

    A função realiza as seguintes verificações:
      - Imprime o valor da constante EXPECTED_BAKE_TIME (esperado: 40).
      - Testa a função bake_time_remaining com 30 minutos já assados (esperado: 10).
      - Testa a função preparation_time_in_minutes com 2 camadas (esperado: 4).
      - Testa a função elapsed_time_in_minutes com 3 camadas e 20 minutos de cozimento (esperado: 26).

    Se os resultados impressos corresponderem aos valores esperados, as funções estão funcionando corretamente.
    """
    print("EXPECTED_BAKE_TIME:", EXPECTED_BAKE_TIME)  # Deve exibir 40
    
    # Teste da função bake_time_remaining
    result = bake_time_remaining(30)
    print("bake_time_remaining(30):", result)  # Esperado: 10
    
    # Teste da função preparation_time_in_minutes
    result = preparation_time_in_minutes(2)
    print("preparation_time_in_minutes(2):", result)  # Esperado: 4
    
    # Teste da função elapsed_time_in_minutes
    result = elapsed_time_in_minutes(3, 20)
    print("elapsed_time_in_minutes(3, 20):", result)  # Esperado: 26

if __name__ == '__main__':
    run_tests()
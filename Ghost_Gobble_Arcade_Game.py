"""
Instruções
Neste exercício, você precisa implementar algumas regras do jogo clássico Pac-Man, lançado nos anos 1980.

Há quatro regras para implementar, todas relacionadas ao mesmo jogo. Não se preocupe em como os argumentos são obtidos; basta se concentrar em combinar os argumentos para retornar o resultado pretendido.

Tarefa 1: Definir se Pac-Man come um fantasma
Defina a função eat_ghost() que recebe dois parâmetros (se Pac-Man tem uma “power pellet” ativa e se Pac-Man está tocando um fantasma) e retorna um valor booleano indicando se Pac-Man consegue comer o fantasma. A função deve retornar True somente se Pac-Man tiver uma “power pellet” ativa e estiver tocando um fantasma.

>>> eat_ghost(False, True)
False
Tarefa 2: Definir se Pac-Man pontua
Defina a função score() que recebe dois parâmetros (se Pac-Man está tocando uma “power pellet” e se Pac-Man está tocando um “dot”) e retorna um valor booleano indicando se Pac-Man pontuou. A função deve retornar True se Pac-Man estiver tocando uma “power pellet” ou um “dot”.

>>> score(True, True)
True
Tarefa 3: Definir se Pac-Man perde
Defina a função lose() que recebe dois parâmetros (se Pac-Man tem uma “power pellet” ativa e se Pac-Man está tocando um fantasma) e retorna um valor booleano indicando se Pac-Man perde. A função deve retornar True se Pac-Man estiver tocando um fantasma e não tiver uma “power pellet” ativa.

>>> lose(False, True)
True
Tarefa 4: Definir se Pac-Man vence
Defina a função win() que recebe três parâmetros (se Pac-Man comeu todos os “dots”, se Pac-Man tem uma “power pellet” ativa e se Pac-Man está tocando um fantasma) e retorna um valor booleano indicando se Pac-Man vence. A função deve retornar True se Pac-Man tiver comido todos os “dots” e não tiver perdido de acordo com os parâmetros definidos na parte 3.

>>> win(False, True, False)
False
"""
def eat_ghost(power_pellet_active, touching_ghost):
    """
    Determina se Pac-Man pode comer um fantasma.

    :param power_pellet_active: bool - True se Pac-Man está com a power pellet ativa, False caso contrário.
    :param touching_ghost: bool - True se Pac-Man está tocando um fantasma, False caso contrário.
    :return: bool - True se Pac-Man pode comer o fantasma (ou seja, se ambos os parâmetros forem True); False caso contrário.

    A função retorna True somente quando Pac-Man possui uma power pellet ativa e está tocando um fantasma.
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """
    Determina se Pac-Man pontuou ao consumir uma power pellet ou um dot.

    :param touching_power_pellet: bool - True se Pac-Man está tocando uma power pellet, False caso contrário.
    :param touching_dot: bool - True se Pac-Man está tocando um dot, False caso contrário.
    :return: bool - True se Pac-Man pontuou (ou seja, se pelo menos um dos parâmetros for True); False caso contrário.

    A função retorna True se Pac-Man estiver tocando uma power pellet ou um dot.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """
    Determina se Pac-Man perde o jogo.

    :param power_pellet_active: bool - True se Pac-Man está com a power pellet ativa, False caso contrário.
    :param touching_ghost: bool - True se Pac-Man está tocando um fantasma, False caso contrário.
    :return: bool - True se Pac-Man perde (ou seja, se estiver tocando um fantasma sem ter a power pellet ativa); False caso contrário.

    A função retorna True somente quando Pac-Man toca um fantasma sem estar protegido por uma power pellet.
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    Determina se Pac-Man vence o jogo.

    :param has_eaten_all_dots: bool - True se Pac-Man comeu todos os dots, False caso contrário.
    :param power_pellet_active: bool - True se Pac-Man está com a power pellet ativa, False caso contrário.
    :param touching_ghost: bool - True se Pac-Man está tocando um fantasma, False caso contrário.
    :return: bool - True se Pac-Man vence (ou seja, se comeu todos os dots e não perdeu de acordo com a função lose); False caso contrário.

    A função retorna True somente quando Pac-Man comeu todos os dots e não perde, ou seja, não toca um fantasma sem a power pellet ativa.
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)


def run_tests():
    """
    Executa uma série de testes simples para validar as funções que implementam as regras do jogo Pac-Man.

    A função realiza as seguintes verificações:
      - Testa a função eat_ghost com diferentes combinações de power pellet ativa e toque em fantasma.
      - Testa a função score para verificar se Pac-Man pontua ao tocar uma power pellet ou um dot.
      - Testa a função lose para confirmar que o jogo é perdido quando Pac-Man toca um fantasma sem estar protegido.
      - Testa a função win para assegurar que Pac-Man vence somente se tiver comido todos os dots e não perder conforme as regras estabelecidas.

    Se os resultados impressos corresponderem aos valores esperados, as funções estão funcionando corretamente.
    """
    print("Teste da função eat_ghost:")
    print("eat_ghost(False, True) =", eat_ghost(False, True), " | Esperado: False")
    print("eat_ghost(True, True) =", eat_ghost(True, True), " | Esperado: True")
    print("eat_ghost(False, False) =", eat_ghost(False, False), " | Esperado: False")
    
    print("\nTeste da função score:")
    print("score(True, True) =", score(True, True), " | Esperado: True")
    print("score(True, False) =", score(True, False), " | Esperado: True")
    print("score(False, False) =", score(False, False), " | Esperado: False")
    
    print("\nTeste da função lose:")
    print("lose(False, True) =", lose(False, True), " | Esperado: True")
    print("lose(True, True) =", lose(True, True), " | Esperado: False")
    print("lose(True, False) =", lose(True, False), " | Esperado: False")
    
    print("\nTeste da função win:")
    print("win(False, True, False) =", win(False, True, False), " | Esperado: False")
    print("win(True, True, False) =", win(True, True, False), " | Esperado: True")
    print("win(True, False, True) =", win(True, False, True), " | Esperado: False")


if __name__ == '__main__':
    run_tests()
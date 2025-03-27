"""
Instruções
Neste exercício, vamos desenvolver um sistema de controle simples para um reator nuclear.
Para que um reator produza energia, ele precisa permanecer em um estado de criticidade. Se o reator estiver em um estado que não seja mais crítico, pode superaquecer e resultar em fusão nuclear. Se o reator ultrapassar a criticidade, pode sobrecarregar e também resultar em fusão. As três tarefas a seguir estão todas relacionadas à escrita de código para manter o estado ideal do reator.

Tarefa 1: Verificar a criticidade

A primeira coisa que um sistema de controle deve fazer é checar se o reator está equilibrado em criticidade. Um reator é considerado crítico se satisfizer as seguintes condições:

A temperatura está abaixo de 800 K.

O número de nêutrons emitidos por segundo é maior que 500.

O produto de temperatura e nêutrons emitidos por segundo é menor que 500000.

Tarefa 2: Determinar a faixa de saída de energia
Assim que o reator começa a produzir energia, é preciso determinar sua eficiência. A eficiência pode ser agrupada em 4 faixas:

green -> eficiência de 80% ou mais,

orange -> eficiência menor que 80%, mas de pelo menos 60%,

red -> eficiência abaixo de 60%, mas ainda de 30% ou mais,

black -> eficiência menor que 30%.

O valor da porcentagem pode ser calculado como:

(potência gerada / potência máxima teórica)*100

onde potência gerada = voltage * current. Note que o valor de porcentagem normalmente não é um número inteiro, então tome cuidado ao usar os operadores < e <=.

Tarefa 3: Mecanismo de segurança (Fail Safe)

Sua última tarefa envolve criar um mecanismo de segurança para evitar sobrecarga e fusão nuclear. Esse mecanismo vai determinar se o reator está abaixo, acima ou no limite ideal de criticidade. A criticidade pode ser aumentada, reduzida ou mantida (inserindo ou removendo barras de controle) no reator.

Se temperature * neutrons_produced_per_second < 90% de threshold, o código de status é 'LOW' e a injeção de barras de controle deve ser removida para produzir mais energia.

Se temperature * neutrons_produced_per_second estiver dentro de +/- 10% de threshold (ou seja, entre 90% e 110% do valor de threshold), o reator está em criticidade e o código de status é 'NORMAL', indicando que o reator está em operação ideal e as barras de controle não são inseridas.

Se temperature * neutrons_produced_per_second não estiver na faixa acima mencionada, o código de status é 'DANGER' e deve-se parar o reator imediatamente para evitar fusão.
"""

def is_criticality_balanced(temperature, neutrons_emitted):
    """
    Verifica se o reator está em equilíbrio de criticidade.

    :param temperature: int or float - temperatura do reator em kelvin.
    :param neutrons_emitted: int or float - número de nêutrons emitidos por segundo.
    :return: bool - True se o reator estiver em criticidade, False caso contrário.

    O reator é crítico se:
    - A temperatura for inferior a 800 K
    - O número de nêutrons emitidos for superior a 500
    - O produto de ambos for inferior a 500000
    """
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """
    Avalia a faixa de eficiência do reator.

    :param voltage: int or float - valor da tensão (voltage).
    :param current: int or float - valor da corrente (current).
    :param theoretical_max_power: int or float - potência máxima teórica.
    :return: str - uma das faixas de eficiência: 'green', 'orange', 'red' ou 'black'.

    A eficiência é calculada como:
    (potência gerada / potência máxima) * 100
    Faixas:
    - green: >= 80%
    - orange: >= 60% e < 80%
    - red: >= 30% e < 60%
    - black: < 30%
    """
    percentage = ((voltage * current) / theoretical_max_power) * 100

    if percentage >= 80:
        return "green"
    if percentage >= 60:
        return "orange"
    if percentage >= 30:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
    Determina o código de status do reator com base na criticidade.

    :param temperature: int or float - temperatura do reator.
    :param neutrons_produced_per_second: int or float - número de nêutrons por segundo.
    :param threshold: int or float - limite ideal de criticidade.
    :return: str - status do reator: 'LOW', 'NORMAL' ou 'DANGER'.

    - LOW: abaixo de 90% do limite
    - NORMAL: entre 90% e 110% do limite
    - DANGER: fora dessas faixas
    """
    product = temperature * neutrons_produced_per_second

    if product < threshold * 0.9:
        return "LOW"
    if threshold * 0.9 <= product <= threshold * 1.1:
        return "NORMAL"
    return "DANGER"

def run_tests():
    """
    Executa testes simples para validar o comportamento das funções do controle do reator.
    """

    # Testes is_criticality_balanced
    print("Testando is_criticality_balanced...")
    assert is_criticality_balanced(750, 600) == True
    assert is_criticality_balanced(750, 700) == False
    assert is_criticality_balanced(800, 600) == False
    print("✓ Passou")

    # Testes reactor_efficiency
    print("Testando reactor_efficiency...")
    assert reactor_efficiency(200, 400, 80000) == "green"
    assert reactor_efficiency(200, 300, 80000) == "orange"
    assert reactor_efficiency(200, 150, 80000) == "red"
    assert reactor_efficiency(200, 50, 80000) == "black"
    print("✓ Passou")

    # Testes fail_safe
    print("Testando fail_safe...")
    assert fail_safe(80, 100, 10000) == "LOW"
    assert fail_safe(95, 100, 10000) == "NORMAL"
    assert fail_safe(120, 100, 10000) == "DANGER"
    print("✓ Passou")

    print("\nTodos os testes foram concluídos com sucesso.")

if __name__ == "__main__":
    run_tests()

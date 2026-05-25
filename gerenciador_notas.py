# --- gerenciador_notas.py ---
"""Sistema de Gerenciamento Acadêmico - Motor de Lógica e Relatórios.

Este script contém as funções centrais para manipulação de notas, cálculo
de médias aritméticas, validação de critérios de aprovação institucional
e geração de relatórios de desempenho formatados.
"""

import random


def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas escolares.

    Garante que o cálculo seja feito de forma segura, tratando cenários em que
    o estudante ainda não possui avaliações registradas no período letivo.

    Args:
        notas (list): Uma lista contendo as notas do estudante, onde cada
            elemento deve ser um número de ponto flutuante (float).

    Returns:
        float: O valor da média aritmética calculada. Retorna 0.0 se a lista
        estiver vazia para evitar erros de divisão por zero.
    """
    if not notas:
        return 0.0

    media_resultante = sum(notas) / len(notas)
    return media_resultante


def verificar_aprovacao(media_final, media_minima=7.0):
    """Verifica se o rendimento do estudante atende ao critério de aprovação.

    Utiliza uma estrutura de decisão simples para comparar a nota obtida com a
    linha de corte estabelecida pela instituição de ensino.

    Args:
        media_final (float): A média ponderada ou aritmética final do aluno.
        media_minima (float, opcional): A nota mínima exigida para passar de
            ano. O valor padrão é 7.0.

    Returns:
        str: Retorna 'Aprovado' caso a media_final seja maior ou igual à
        media_minima. Caso contrário, retorna 'Reprovado'.
    """
    if media_final >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorio(alunos):
    """Percorre a lista de estudantes, processa suas médias e situações, e exibe

    um relatório consolidado no terminal de forma organizada.

    Args:
        alunos (list): Uma lista de dicionários, onde cada dicionário representa
            um estudante e contém obrigatoriamente as chaves "nome" e "notas".
    """
    print("\n" + "=" * 55)
    print("         RELATÓRIO DE DESEMPENHO ACADÊMICO")
    print("=" * 55)
    print(f"{'Estudante':<20} | {'Média Final':<12} | {'Situação':<12}")
    print("-" * 55)

    if not alunos:
        print("⚠️ Nenhum estudante cadastrado no sistema até o momento.")
        print("=" * 55)
        return

    for aluno in alunos:
        nome_estudante = aluno["nome"]
        lista_notas = aluno["notas"]

        # Reutilização das funções modulares de cálculo
        media_calculada = calcular_media(lista_notas)
        situacao_final = verificar_aprovacao(media_calculada)

        emoji_status = "✨" if situacao_final == "Aprovado" else "❌"

        # Formatação com alinhamento à esquerda (<) e duas casas decimais (.2f)
        print(
            f"{nome_estudante:<20} | {media_calculada:<12.2f} | {emoji_status} {situacao_final:<10}"
        )

    print("=" * 55 + "\n")


# --- Bloco de Execução Principal para Demonstração ---
if __name__ == "__main__":
    # Inicialização da estrutura de dados planejada (Lista de Dicionários)
    turma_estudantes = [
        {"nome": "Ana Silva", "notas": [8.5, 7.0, 9.0]},
        {"nome": "Bruno Santos", "notas": [5.5, 6.0, 4.5]},
        {"nome": "Carla Oliveira", "notas": [9.5, 10.0, 8.8]},
        {"nome": "Diego Souza", "notas": [7.0, 6.5, 7.2]},
        {
            "nome": "Beatriz Mendes",
            "notas": [],
        },  # Teste de Edge Case controlado
    ]

    # Execução do relatório gerencial
    gerar_relatorio(turma_estudantes)
    
    
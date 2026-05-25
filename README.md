# Academic Performance Management System (APMS) 📊

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange)
![Environment](https://img.shields.io/badge/Environment-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

Este projeto consiste em um sistema em linha de comando (CLI) focado no registro, processamento e monitoramento do desempenho acadêmico de estudantes. A aplicação foi projetada sob os princípios da engenharia de software moderna, priorizando a modularidade, legibilidade e manutenibilidade do código.

---

## 🎯 Arquitetura & Padrões de Projeto

A aplicação foi estruturada seguindo rigorosamente os seguintes pilares técnicos:

* **Princípio da Responsabilidade Única (SRP):** Cada componente e função do sistema possui uma única razão para mudar. As rotinas de cálculo matemático estão completamente isoladas da camada de apresentação (I/O).
* **Guia de Estilo PEP 8:** Todo o ecossistema de código adota as convenções oficiais do Python, incluindo nomenclatura em `snake_case` para funções/variáveis, espaçamento vertical padronizado e documentação interna por meio de docstrings estruturadas (padrão Google/Docstring).
* **Defesa contra Falhas (*Edge Cases*):** Implementação de travas lógicas preventivas para mitigar erros em tempo de execução, como o tratamento de listas vazias para evitar exceções de divisão por zero (`ZeroDivisionError`).

---

## 🏗️ Estrutura de Dados na Memória

Para garantir a acessibilidade e flexibilidade das informações sem a necessidade de persistência em banco de dados nesta etapa, o sistema utiliza uma coleção acoplada de **listas e dicionários (`List[Dict[str, Any]]`)**:

```python
[
    {
        "nome": "Nome do Estudante",
        "notas": [float, float, float]
    }
]

---

## 📁 Módulos e Funções do Core

O motor lógico do sistema é composto pelas seguintes rotinas independentes:

| Função | Parâmetros | Retorno | Descrição |
| :--- | :--- | :--- | :--- |
| `calcular_media` | `notas` (list) | `float` | Calcula a média aritmética. Retorna `0.0` se a lista estiver vazia. |
| `verificar_aprovacao` | `media` (float), `media_minima` (float) | `str` | Compara a média com a nota de corte. Retorna 'Aprovado' ou 'Reprovado'. |
| `gerar_relatorio` | `alunos` (list) | `None` | Varre a lista, consome as funções acima e renderiza a tabela gerencial. |

---

💻 Pré-requisitos e Ambiente
A aplicação foi desenvolvida de forma nativa, eliminando a necessidade de gerenciadores de pacotes externos (pip).

Interpretador: Python 3.8 ou superior instalado.

Dependências: Apenas módulos nativos do ecossistema Python (unittest, random).

---

🚀 Instruções de Execução
1. Clonar o Repositório
Abra o seu terminal e clone este projeto para a sua máquina local:

git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

2. Executar a Aplicação Principal
Para rodar o motor do sistema e visualizar a renderização do relatório gerencial no terminal, execute:

python3 gerenciador_notas.py

---

🧪 Ambiente de Testes Unitários e Validação
A confiabilidade das regras de negócio foi blindada utilizando a biblioteca nativa unittest. A matriz de testes cobre fluxos principais (Happy Paths) e cenários de exceção (Edge Cases).

Para disparar os ensaios automatizados de validação de código, execute o comando:

python3 -m unittest test_notas.py

Cenários Cobertos na Suite de Testes:
test_calcular_media_comum: Garante a precisão do cálculo matemático com floats tradicionais.

test_verificar_aprovacao_comum / test_verificar_reprovacao_comum: Valida a assertividade da tomada de decisão na linha de corte (7.0).

test_calcular_media_lista_vazia: Teste limite (Edge Case) que valida a resiliência do sistema ao processar alunos sem avaliações cadastradas.

test_verificar_aprovacao_corte_zero: Valida a estabilidade do parâmetro padrão dinâmico da função diante de configurações extremas de negócio.

---

👩‍💻 Autora
Desenvolvido por [Erica Serpa] como evidência técnica de engenharia de software e boas práticas de programação.

LinkedIn: Seu Nome no LinkedIn
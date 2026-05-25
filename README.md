# Sistema de Gerenciamento de Notas Acadêmicas 📊

Sistema desenvolvido em Python para gerenciamento e processamento de notas acadêmicas via terminal (CLI). O projeto foi estruturado seguindo boas práticas de engenharia de software, modularização de código e validação automatizada com testes unitários.

---

# 📌 Objetivo do Projeto

O sistema permite:

- Cadastro estruturado de estudantes e notas;
- Cálculo automático de médias;
- Verificação de aprovação ou reprovação;
- Geração de relatórios formatados;
- Execução de testes automatizados para validação das regras de negócio.

O projeto foi desenvolvido com foco em:

- Legibilidade;
- Organização modular;
- Tratamento de casos extremos (*edge cases*);
- Confiabilidade do sistema.

---

# 🛠️ Tecnologias Utilizadas

- Python 3.8+
- Biblioteca nativa `unittest`
- Programação estruturada
- Terminal/CLI

---

# 📂 Estrutura do Projeto

```bash
📦 sistema-gerenciamento-notas
 ┣ 📜 gerenciador_notas.py
 ┣ 📜 test_notas.py
 ┗ 📜 README.md
```

---

# ⚙️ Funcionalidades

## ✅ Cálculo de Média

A função `calcular_media()` realiza o cálculo da média aritmética das notas do estudante.

### Exemplo:

```python
notas = [8.0, 7.0, 9.0]
media = calcular_media(notas)
print(media)
```

### Saída:

```bash
8.0
```

---

## ✅ Verificação de Aprovação

A função `verificar_aprovacao()` valida a situação final do aluno com base na média mínima institucional.

### Regra padrão:

- Média maior ou igual a `7.0` → **Aprovado**
- Média menor que `7.0` → **Reprovado**

### Exemplo:

```python
resultado = verificar_aprovacao(7.5)
print(resultado)
```

### Saída:

```bash
Aprovado
```

---

## ✅ Relatório Acadêmico

O sistema gera um relatório formatado no terminal contendo:

- Nome do estudante;
- Média final;
- Situação acadêmica.

### Exemplo de saída:

```bash
=======================================================
         RELATÓRIO DE DESEMPENHO ACADÊMICO
=======================================================
Estudante           | Média Final | Situação
-------------------------------------------------------
Ana Silva           | 8.17        | ✨ Aprovado
Bruno Santos        | 5.33        | ❌ Reprovado
=======================================================
```

---

# 🧪 Testes Automatizados

O projeto utiliza o framework nativo `unittest` para garantir estabilidade e confiabilidade das regras de negócio.

## Casos testados

### Happy Paths

- Cálculo de média padrão;
- Aprovação com média acima da nota mínima;
- Reprovação abaixo da média exigida.

### Edge Cases

- Lista de notas vazia;
- Média mínima configurada como `0.0`.

---

# ▶️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/sistema-gerenciamento-notas.git
```

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd sistema-gerenciamento-notas
```

---

## 3️⃣ Execute o sistema

```bash
python gerenciador_notas.py
```

ou

```bash
python3 gerenciador_notas.py
```

---

# 🧪 Como Executar os Testes

```bash
python -m unittest test_notas.py
```

ou

```bash
python3 -m unittest test_notas.py
```

---

# ✅ Resultado Esperado dos Testes

```bash
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

# 🧠 Conceitos Aplicados

- Modularização de código;
- Single Responsibility Principle (SRP);
- Tratamento de exceções;
- Programação defensiva;
- Testes unitários;
- Estruturas de dados com listas e dicionários;
- Boas práticas da PEP 8;
- Documentação com Docstrings.

---

# 📖 Aprendizados

Durante o desenvolvimento deste projeto foi possível aplicar conceitos fundamentais de engenharia de software, incluindo:

- Organização lógica de sistemas;
- Separação de responsabilidades;
- Criação de testes automatizados;
- Desenvolvimento orientado à confiabilidade;
- Estruturação profissional de documentação técnica.

---

# 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos na disciplina de Engenharia de Software / Programação em Python.

---

# 📜 Licença

Este projeto possui finalidade educacional e acadêmica.



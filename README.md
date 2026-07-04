# Simplex — Otimização Linear com PuLP

Projeto desenvolvido para a disciplina de **Métodos Quantitativos** do curso de **Ciência da Computação**, com o objetivo de implementar o **Método Simplex** para resolução de problemas de Programação Linear (PL), utilizando a biblioteca [PuLP](https://coin-or.github.io/pulp/) para modelagem e resolução, e a biblioteca **`re`** (Regex) para o parsing e formatação das entradas fornecidas pelo usuário.

O sistema permite modelar problemas com:

- **Mais de 2 variáveis de decisão**;
- **Mais de 2 restrições**;
- Escolha entre **maximização** ou **minimização** da função objetivo.

---

## 📁 Estrutura do Projeto

```
simplex/
├── app/
│   ├── models/
│   │   ├── data_format.py       # Parsing e formatação dos inputs (usa regex)
│   │   └── problem_builder.py   # Construção do problema com PuLP (variáveis, restrições, FO)
│   └── quantitative/
│       ├── optimizer.py         # Orquestra a resolução do problema
│       └── exceptions.py        # Exceções customizadas do domínio
├── main.py                      # Ponto de entrada da aplicação
└── requirements.txt              # Dependências do projeto (usadas no ambiente virtual .venv)
```

---

## 🔗 Arquitetura e Relacionamentos

O projeto segue uma arquitetura em camadas, onde cada módulo possui uma responsabilidade bem definida:

```
main.py
  │
  ├──> data_format.py   (formata os inputs em um dict, usando re)
  │
  └──> optimizer.py     (recebe o dict e resolve o problema)
          │
          └──> problem_builder.py   (monta o problema com PuLP)
```

### Descrição das camadas

- **`main.py`** — Camada superior da aplicação. Responsável por coletar os dados de entrada do usuário (função objetivo, restrições e tipo de otimização) e orquestrar o fluxo, chamando `data_format` para formatar os dados e `optimizer` para resolver o problema.

- **`app/models/data_format.py`** — Recebe os inputs brutos (strings) informados pelo usuário e utiliza expressões regulares (**`re`**) para interpretar e extrair coeficientes, variáveis e operadores das restrições e da função objetivo. Retorna um **dicionário estruturado** para o `main.py`, contendo todas as informações necessárias para a montagem do problema.

- **`app/quantitative/optimizer.py`** — Camada de orquestração da resolução. Recebe o dicionário formatado através da função `optimize_problem`, instancia a classe `BuildProblem` (de `problem_builder.py`) para montar o problema, executa a resolução utilizando o **PuLP** e imprime os resultados no console (status da solução, valor ótimo da função objetivo e valores das variáveis). Também trata exceções específicas definidas em `exceptions.py`.

- **`app/quantitative/exceptions.py`** — Define exceções customizadas utilizadas para tratar erros de validação e de resolução do problema (ex.: problema inviável, dados inconsistentes, restrições mal formatadas).

- **`app/models/problem_builder.py`** — Contém a classe `BuildProblem`, responsável por organizar as variáveis de decisão, restrições e coeficientes da função objetivo, criando as instâncias base do **PuLP** (`LpVariable`, `LpProblem`), prontas para serem resolvidas pelo `optimizer.py`.

---

## 🧩 Fluxo de Execução

1. O usuário informa, via `main.py`, a função objetivo, o tipo de otimização (max/min) e as restrições do problema;
2. `data_format.py` interpreta essas strings utilizando **regex**, convertendo-as em um dicionário estruturado (coeficientes, sinais, valores, tipo de otimização);
3. `main.py` chama `optimize_problem(dados)` em `optimizer.py`;
4. `optimizer.py` instancia `BuildProblem`, passando o dicionário formatado;
5. `problem_builder.py` cria as variáveis (`LpVariable`) e o problema (`LpProblem`), define a função objetivo e adiciona as restrições;
6. `optimizer.py` resolve o problema utilizando o solver do **PuLP** (`problem.solve()`);
7. O resultado (status, valor ótimo e valores das variáveis) é impresso no console.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python 3** | Linguagem principal do projeto |
| **PuLP** | Modelagem e resolução do problema de Programação Linear (Método Simplex) |
| **re (Regex)** | Extração e formatação dos dados de entrada (função objetivo e restrições) |
| **requirements.txt** | Lista as dependências do projeto para instalação no ambiente virtual (`.venv`) |

---

## 📦 Dependências (`requirements.txt`)

Na raiz do projeto há um arquivo **`requirements.txt`**, utilizado para instalar todas as dependências necessárias dentro do ambiente virtual (`.venv`):

```
pulp
```

> Caso novas bibliotecas sejam adicionadas ao projeto, elas devem ser incluídas neste arquivo para manter o ambiente virtual sempre atualizado.

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd simplex
   ```

2. Crie o ambiente virtual `.venv`:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Instale as dependências a partir do `requirements.txt` (localizado na raiz do projeto):
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa:
   ```bash
   python main.py
   ```

5. Siga as instruções no console para informar:
   - A função objetivo (ex.: `2x1 + 3x2 - x3`);
   - O tipo de otimização (`max` ou `min`);
   - As restrições (ex.: `x1 + x2 <= 40`, `2x1 + x3 >= 10`).

---

## 📌 Exemplo de Entrada

```
Função objetivo: max 3x1 + 5x2 + 4x3
Restrições:
  2x1 + 3x2 <= 8
  2x2 + 5x3 <= 10
  3x1 + 2x2 + 4x3 <= 15
```

## 📌 Exemplo de Saída

```
Status: Optimal
Valor ótimo da função objetivo: 36.13
x1 = 0.0
x2 = 2.67
x3 = 0.93
```

---

## ⚠️ Tratamento de Erros

Erros comuns (problema inviável, ilimitado, ou entrada mal formatada) são tratados por meio de exceções customizadas definidas em `exceptions.py`, garantindo mensagens claras ao usuário sem interromper abruptamente a execução do programa.

---

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como trabalho prático da disciplina de **Métodos Quantitativos**, com foco na aplicação de conceitos de **Pesquisa Operacional**, mais especificamente o **Método Simplex**, utilizando ferramentas de programação para automatizar a modelagem e resolução de problemas de otimização linear.
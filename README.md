# EXPA02 — Ciclos: While e For

**Disciplina:** Programação e Sistemas de Informação (PSI) — Módulo 3
**Exercício Prático:** 02
**Turma:** 1.º I — N.º 14785
**Ano Letivo:** 2025/2026

10 exercícios em três níveis de dificuldade sobre ciclos de repetição `while` e `for`. Inclui um programa introdutório de demonstração dos dois ciclos em conjunto.

---

## Ficheiros

| Ficheiro | Descrição |
|---|---|
| `Ciclos de While e For.py` | Programa introdutório — tabuada com `while` externo e `for` interno |
| `Exercicio Pratico 02 - Modulo 3 - Ciclos de while e for.py` | Programa completo com menu e todos os 10 exercícios |
| `README.md` | Este ficheiro |

---

## Programa Introdutório

Demonstração da combinação `while` (controlo externo) com `for` (iteração fixa) para criar uma tabuada repetível:

```python
# Ciclos: While e For
resposta = "sim"
while resposta == "sim":
    numero = int(input("Numero: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    resposta = input("Deseja repetir? (Sim/Nao): ").lower()

    if resposta != "sim" and resposta != "nao":
        print("Operacao Invalida!")
        resposta = input("Deseja repetir? (Sim/Nao): ").lower()
```

---

## Exercícios

### Nível Básico

| Código | Título | Descrição |
|---|---|---|
| B1 | Contagem Simples (`while`) | Mostra números de 1 a 10 |
| B2 | Contagem Decrescente (`while`) | Mostra números de 10 a 1 |
| B3 | Contagem com `for` | Mostra números de 1 a 20 |
| B4 | Números Pares | Mostra pares entre 1 e 20 com `range(2, 21, 2)` |

### Nível Intermédio

| Código | Título | Descrição |
|---|---|---|
| I1 | Soma de 1 a 100 | Acumulador manual — resultado: 5050 |
| I2 | Tabuada | Repete enquanto número >= 0; número negativo termina |
| I3 | Contador de Pares | Conta números pares entre 1 e 50 |

### Nível Avançado

| Código | Título | Descrição |
|---|---|---|
| A1 | Soma Personalizada | Pede N números e calcula a soma |
| A2 | Menu Repetitivo | Menu com 3 opções — repete até escolher `0` |
| A3 | Fatorial | Calcula N! com `for`; valida negativos |

---

## Conceitos Abordados

```python
# while — repetição controlada por condição
i = 1
while i <= 10:
    print(i)
    i += 1

# for com range — iteração numérica
for i in range(1, 21):         # 1 a 20
    print(i)
for i in range(2, 21, 2):     # pares: 2, 4, 6 ... 20
    print(i)

# Acumulador (I1)
soma = 0
for i in range(1, 101):
    soma += i                   # resultado: 5050

# break — saída controlada (I2)
while True:
    num = int(input("Numero (negativo para sair): "))
    if num < 0:
        break

# Fatorial (A3)
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
```

---

## Compatibilidade

O ficheiro EXPA02 usa `os.system("cls")` para limpar a consola.

- Windows — funciona nativamente
- macOS / Linux — substituir por `os.system("clear")`

O programa introdutório já usa a versão multiplataforma: `"cls" if os.name == "nt" else "clear"`.

---

## Como Executar

```bash
git clone https://github.com/a14785-oficina/ciclos-while-e-for.git
cd ciclos-while-e-for

# Programa introdutório
python3 "Ciclos de While e For.py"

# Exercícios completos
python3 "Exercicio Pratico 02 - Modulo 3 - Ciclos de while e for.py"
```

---

## Navegação — Módulo 3

| Posição | Repositório |
|---|---|
| Anterior | [EXPA01 — Exercícios de Estruturas Condicionais](https://github.com/a14785-oficina/exercicios-estruturas-condicionais) |
| Seguinte | [EXPA03 — Sistema de Gestão de Notas](https://github.com/a14785-oficina/sistema-gestao-notas) |
| Portfólio | [oficina-jpc](https://github.com/a14785-oficina/oficina-jpc) |

---

*PSI — Módulo 3 — Programação Estruturada — OFICINA — 2025/2026*

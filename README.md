#  Biblioteca Interativa com Tkinter

Bem-vindo ao sistema de **Biblioteca**!
Aqui você pode cadastrar livros, usuários, funcionários, emprestar e devolver livros — tudo com uma interface gráfica simples e prática feita em Python com Tkinter.

---

##  O que dá pra fazer?

✅ Cadastrar livros  
✅ Cadastrar usuários  
✅ Cadastrar funcionários  
✅ Listar tudo bonitinho  
✅ Emprestar e devolver livros  
✅ Salvar tudo automaticamente 

---

## Como rodar

1. Tenha o Python 3 instalado.
2. No terminal, rode:

```bash
python interface.py
```

3. A janela da biblioteca vai abrir, aí é só usar os botões!

---

## Organização dos arquivos

| Arquivo         | O que faz                                   |
|------------------|----------------------------------------------|
| `interface.py`   | Interface gráfica com os botões e janelas   |
| `biblioteca.py`  | Regras e operações da biblioteca            |
| `livro.py`       | Define a classe `Livro`                     |
| `pessoa.py`      | Define `Usuario` e `Funcionario`            |
| `emprestimo.py`  | Gerencia os empréstimos                    |
| `historico.py`   | Guarda o histórico de ações                 |
| `dados.py`       | Salva e carrega os dados com pickle         |
| `biblioteca.pkl` | Arquivo onde os dados ficam salvos          |

---

## Importante

- Os dados são salvos sempre que você clica em **"Sair e Salvar"**.
- Quando abrir o programa de novo, tudo estará lá de onde parou!

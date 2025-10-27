# 🧠 Tradutor com Avatar em Libras (PoC)

Este projeto é uma **prova de conceito** (PoC) para mapeamento de palavras em português para *comandos de sinais* em Libras.  
Inclui testes automatizados com `pytest` e pipeline de CI/CD com **GitHub Actions**.

## 🚀 Como rodar localmente

```bash
# Instale as dependências
pip install pytest

# Execute diretamente
python teste_mapeamento_completo.py

# Ou via pytest
pytest -v
```

## 🧩 Estrutura
```
tradutor-com-avatar-em-libras/
├── teste_mapeamento_completo.py
├── README.md
├── .gitignore
└── .github/workflows/python-tests.yml
```

## ✅ CI Automático
A cada push ou pull request, os testes são executados automaticamente no GitHub Actions.

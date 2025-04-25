# 📁 Extrator de Metadados

**Ferramenta para extração automatizada de metadados de documentos**

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Licença](https://img.shields.io/badge/Licença-MIT-green)

## 📦 Instalação

```bash
git clone https://github.com/fribeiro1986/extrator-metadados.git
cd extrator-metadados
pip install -r requirements.txt
```

## 🚀 Como Usar

```python
python extrair_metadados.py caminho/do/arquivo.pdf
```

### Formatos Suportados:
- PDF
- DOCX
- JPEG/PNG (em desenvolvimento)

## 🛠 Funcionalidades

| Função          | Descrição                          |
|-----------------|-----------------------------------|
| `extrair_pdf`   | Extrai metadados de arquivos PDF   |
| `extrair_docx`  | Extrai metadados de arquivos Word  |
| `gerar_relatorio` | Gera relatório em JSON           |

## 📝 Exemplo de Saída

```json
{
  "arquivo": "documento.pdf",
  "autor": "João Silva",
  "criado_em": "2023-10-15T08:30:00",
  "tamanho": "2.4 MB"
}
```

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie um branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para o branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request



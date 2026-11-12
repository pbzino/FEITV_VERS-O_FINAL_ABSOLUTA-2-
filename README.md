# FEItv

Catálogo de vídeos em Python com interface de terminal. O projeto usa arquivos de texto para armazenar o catálogo e as interações dos usuários.

## O que dá para fazer

- Criar uma conta e entrar no sistema.
- Buscar vídeos e consultar informações como gênero, ano e sinopse.
- Curtir vídeos e criar listas de favoritos.

## Como executar

Com o Python 3 instalado, abra o terminal na pasta do repositório e execute:

```bash
python main.py
```

No Windows, você também pode usar `py main.py`. Para testar o cadastro, use um usuário e uma senha fictícios. Os dados de login deste projeto didático são gravados em arquivo de texto.

## Estrutura

| Arquivo | Responsabilidade |
| --- | --- |
| [`main.py`](main.py) | Menus e ponto de entrada |
| [`auth.py`](auth.py) | Cadastro e login |
| [`usuario.py`](usuario.py) | Busca, curtidas e favoritos |
| [`arquivo_utils.py`](arquivo_utils.py) | Leitura e escrita dos dados |

# FubaKake 🍜

FubaKake é uma rede social colaborativa de receitas (um "GitHub para receitas") onde usuários podem postar, comentar e salvar receitas de outros perfis.

## Stack

- Python + Django REST Framework
- PostgreSQL (produção) / SQLite (desenvolvimento)
- JWT Authentication (djangorestframework-simplejwt)
- Deploy: Railway (em breve)

## Endpoints

### Autenticação
| Método | URL | Descrição |
|--------|-----|-----------|
| POST | `/token/` | Login — retorna access e refresh token |
| POST | `/token/refresh/` | Renova o access token |

### Receitas
| Método | URL | Descrição |
|--------|-----|-----------|
| GET | `/recipes/` | Feed com todas as receitas |
| POST | `/recipes/criar_receita` | Cria uma receita |

### Comentários
| Método | URL | Descrição |
|--------|-----|-----------|
| POST | `/comments/create_comments/<receita_id>/` | Comenta em uma receita |
| GET | `/comments/comments` | Lista todos os comentários |

> Todos os endpoints exigem autenticação via Bearer Token no header.

## Como rodar localmente
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fubakake.git

# Instale as dependências
pip install -r requirements.txt

# Rode as migrations
python manage.py migrate

# Suba o servidor
python manage.py runserver
```

## Status do projeto

Em desenvolvimento ativo.

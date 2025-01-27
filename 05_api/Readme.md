# Atividade 05

## Como rodar o projeto (API)

Para rodar a API é necessário está dentro da pasta server, após isso, basta entrar no ambiente venv rodando o comando 

```source venv/bin/activate``` 

Após isso, executar o comando para instalação das dependências

```pip install -r requirements.txt```

E para rodar a API, executar o comando

```uvicorn server:app --reload```

Após isso, a API estará rodando. O endereço será mostrado na tela, por padrão será http://127.0.0.1:8000, esse mesmo endereço está configurado no arquivo client_controller.py, caso seja necessário alterar, basta alterar o valor da variável BASE_URL, adicionando um "/cursos" após a porta, para acessar a rota de cursos, como mostrado a seguir:

```python
BASE_URL = "http://127.0.0.1:8000/cursos"
```

## Como rodar o projeto (Frontend)

Para executar o frontend é necessário está dentro da pasta client, após isso, é necessário apenas rodar o comando

```python3 client.py```

Após isso será exibido um menu com as opções disponíveis para interação com a API, como mostrado a seguir:

```
Opções:
1. Listar todos os cursos
2. Obter detalhes de um curso
3. Criar um novo curso
4. Atualizar um curso existente
5. Excluir um curso
6. Sair
Escolha uma opção: 
```

Depois disso, basta escolher a opção desejada e seguir as instruções que serão exibidas no terminal.

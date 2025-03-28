<h1 style="text-align:center"> Projeto BlockBuster </h1> 

> Esse projeto foi feito como uma API com o intuito de gestão de vendas de filmes (como um Blockbuster). Portanto ele consegue:
* Criar usuário
* Buscar filmes
* Criar pedidos
* E muitas outras funções

## Tecnologias

* Django Rest Framework

## Rotas da API

| Rotas | Verbo HTTP | Objetivo|
| ------- |:-----------:|--------:|
|/api/users/ | POST | Criação de usuário
|/api/users/login/ | POST | Autenticação do usuário
|/api/users/int:user_id/ | GET | Busca de usuário por id
|/api/users/user_id/ | PATCH | Atualizar usuário
|/api/movies/ | POST | Criação de filme
|/api/movies/ | GET | Listagem de filme
|/api/movies/movie_id/ | GET | Busca de filme por id
|/api/movies/movie_id/ | DELETE | Deleção de filme
|/api/movies/movie_id/orders/ | POST | Criação de pedido

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate

# git bash:
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```

5. Vá até o arquivo `pytest.ini` e modifique o nome do projeto `my_project_name.settings` para o nome do **seu_projeto**.settings (onde se encontra o settings.py)

4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```



## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

- Rodando testes da Tarefa 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Rodando testes da Tarefa 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Rodando testes da Tarefa 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Rodando testes da Tarefa 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```
## Dockerização da aplicação

### Configuração do Docker

- Crie um arquivo chamado Dockerfile dentro do diretório app para configurar o ambiente Python.

- Crie um arquivo chamado docker-compose.yml no diretório raiz do projeto para definir os serviços Docker.

- Inicie a imagem utilizando o comando com as configurações da Dockerfile

````bash
docker build -t nome_da_image .
````
- Inicie o container

````bash
docker-compose up app -d
````

- a flag '-d' fara com que não apareça o servidor do FastAPI no terminal;

- O mesmo para os containers do pgadmin e do postgresql 
 
````bash
docker-compose up pgadmin -d
````

````bash
docker-compose up postgresql -d
````

- No terminal, navegue até o diretório raiz do seu projeto e execute docker-compose up.
- Isso irá construir e iniciar todos os serviços definidos no arquivo docker-compose.yml.
- Sua aplicação FastAPI estará disponível em http://localhost:8000, o PGAdmin4 em http://localhost:5050, e o PostgreSQL em localhost:5432.
- Você pode acessar o PGAdmin4 com o e-mail e senha definidos nas variáveis de ambiente. (.env)


## Subindo PostgreSQL com docker-compose


- Com o Alembic configurado, você pode criar uma migração inicial para o seu esquema de banco de dados. Para isso, execute o seguinte comando:

````bash
docker-compose run --user 1000 app sh -c 'alembic init migrations'
````
- Isso criará um arquivo de migração na pasta alembic/versions com o nome no formato {timestamp}_initial_migration.py.

- Agora, você pode aplicar as migrações ao banco de dados. Isso é feito com o seguinte comando:


````bash
docker-compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add categories table"'
````

````bash
docker-compose run --user 1000 app sh -c 'alembic upgrade head'
````


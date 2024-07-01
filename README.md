# Trees Everywhere

## Introdução

**Trees Everywhere** é um projeto que visa criar um banco de dados global de árvores plantadas por voluntários ao redor do mundo. Utilizamos Django para o backend, e Leaflet.js para exibir as localizações das árvores em um mapa interativo.

## Funcionalidades

- Registro e login de usuários
- Criação e gerenciamento de perfis de usuários
- Registro de novas árvores plantadas
- Visualização de árvores plantadas em um mapa interativo

## Requisitos

- Python 3.8+
- Django 3.2+

## Instalação

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/VasconcelosVictor/Trees-Everywhere.git
    cd Trees-Everywhere
    ```

2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências do backend:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados:**
    Modifique as configurações de Banco de Dados pra sua Base.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'SEU DATABASE',
            'USER': 'SEU USUARIO',
            'PASSWORD': 'SUA SENHA',
            'HOST': 'localhost',
            'PORT': '5432',
        }

    }
    
     ```

    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

8. **Acesse a aplicação:**
    Abra o navegador e vá para `http://localhost:8000`

## Uso

- **Usuario Adm**
- **Registro de Usuário:** Vá para a página de Admin e as  contas do seu sistema e adcione os usuários a conta que ele pertencer.
- **Login:** Faça login com suas credenciais.
- **Todas as Contas:** Em todas as contas voce pode Vizualiar as contas do sistema, la voce também pode adcionar editar ou excluir uma conta.
- **Todos os Usuários:** Em todos os usuário voce pode adcionar editar ou excluir um usuario .

- **Usuario**
- **Cadastro de Plantas:** Com seu Usuário administrador Logado clique em Cadastrar Plantas pra adicionar plantas a sua base de dados.
- **Adicionar Árvore:** Navegue até a página de adicionar árvore, clique no mapa para definir a localização, preencha os detalhes e salve.
- **Visualizar Detalhes:** Clique em cima de uma arvore que você plantou e visualize as informações sobre ela.
- **Perfil:** Em perfil você pode visuzualizar suas informações e também edita-las.
- 

## Contribuição

Se você deseja contribuir para o projeto, siga estas etapas:

1. **Fork o repositório**
2. **Crie um branch para sua feature/bugfix**
    ```bash
    git checkout -b feature/nova-feature
    ```
3. **Faça commit das suas alterações**
    ```bash
    git commit -m "Adiciona nova feature"
    ```
4. **Envie para o branch remoto**
    ```bash
    git push origin feature/nova-feature
    ```
5. **Abra um Pull Request**

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

- **Nome:** Victor Vasconcelos
- **Email:** [seu-email@example.com](mailto:victorvasoncelos6x@hmail.com)
- **LinkedIn:** [Seu Perfil LinkedIn](https://www.linkedin.com/in/victor-vasconcelos-barbosa/)


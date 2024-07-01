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
    ```bash
    python manage.py migrate
    ```

5. **Crie um superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7. **Acesse a aplicação:**
    Abra o navegador e vá para `http://localhost:8000`

## Uso

- **Registro de Usuário:** Vá para a página de registro e crie uma conta.
- **Login:** Faça login com suas credenciais.
- **Adicionar Árvore:** Navegue até a página de adicionar árvore, clique no mapa para definir a localização, preencha os detalhes e salve.
- **Visualizar Mapa:** Vá para a página do mapa para visualizar todas as árvores plantadas.

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
- **Email:** [seu-email@example.com](mailto:seu-email@example.com)
- **LinkedIn:** [Seu Perfil LinkedIn](https://www.linkedin.com/in/seu-perfil-linkedin/)


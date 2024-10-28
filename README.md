# 🌐 Integração com Modelos de Linguagem para Sugestões Personalizadas

Este repositório contém scripts em Python que utilizam a tecnologia de **Modelos de Linguagem de Grande Escala (LLMs)** para fornecer recomendações personalizadas em diferentes contextos. Os scripts usam a biblioteca [LangChain](https://python.langchain.com/) para facilitar o acesso e manipulação das respostas do modelo LLM [llama3.2]([https://ollama.com/](https://ollama.com/library/llama3.2)).

## 📚 O que são LLMs?

LLMs (Large Language Models) são modelos de inteligência artificial projetados para processar e gerar linguagem natural. Eles conseguem interpretar e responder a uma variedade de solicitações complexas, como responder perguntas, traduzir idiomas, sugerir recomendações e muito mais. No contexto deste repositório, estamos utilizando um LLM para responder a perguntas com base em inputs (prompts) específicos fornecidos pelo usuário.

## 📋 Sobre os Scripts

Este repositório possui duas funcionalidades principais:

1. **Sugestões de vestimenta e alimentação** com base nas condições climáticas de uma cidade (usando a API OpenWeather).
2. **Sugestões de receitas** com base nas preferências alimentares e nível de experiência do usuário.

Cada script aproveita o poder dos LLMs da para criar respostas personalizadas e contextuais em português.

## 📦 Bibliotecas Utilizadas

- **LangChain**: Biblioteca para criação de fluxos e integração com modelos de linguagem.
- **Requests**: Utilizada para chamadas HTTP, como a API OpenWeather.
- **Python-dotenv**: Para carregar variáveis de ambiente de forma segura.
- **LLM da Ollama**: Modelo de linguagem utilizado para gerar as respostas baseadas em prompts e contexto fornecido.

### Instalação das Dependências

Para instalar todas as bibliotecas necessárias, execute:

```bash
pip install langchain_ollama requests python-dotenv
```

## 🚀 Configuração Inicial

1. **Clone este repositório** e navegue até a pasta do projeto:
   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
   cd nome_do_repositorio
   ```

2. **Configure o arquivo `.env`**:

   Para a funcionalidade de sugestões baseadas no clima, é necessário configurar a chave de API da OpenWeather. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo, substituindo `"YOUR_WEATHER_API_KEY"` pela sua chave da OpenWeather:

   ```plaintext
   WEATHER_API_KEY="YOUR_WEATHER_API_KEY"
   ```

## 🧑‍💻 Utilização dos Scripts

### 1. Sugestão de Vestimenta e Alimentação com Base no Clima

O script `weather.py` consulta a API OpenWeather e utiliza a LLM para fornecer recomendações de vestimenta e alimentação com base nas condições climáticas atuais de uma cidade.

Para executar o script:

```bash
python weather.py
```

Durante a execução, o usuário será solicitado a informar o nome de uma cidade. O script então buscará os dados climáticos e retornará sugestões personalizadas, como no exemplo:

```plaintext
Welcome suggestion bot!
Which city do you want to check? São Paulo
Thinking wait...

Bot:
Para a temperatura de 25.00°C, com um clima que está nublado na cidade de São Paulo, você deve considerar usar roupas leves e comer pratos refrescantes como saladas e frutas.
```

### 2. Sugestão de Receitas com Base em Preferências Alimentares

O script `recipes.py` gera sugestões de receitas com base em preferências alimentares, ingredientes favoritos e o nível de experiência culinária do usuário.

Para executar o script:

```bash
python recipes.py
```

O script solicitará detalhes sobre as preferências e restrições alimentares do usuário, como nível de experiência na cozinha, ingredientes disponíveis e restrições. Em seguida, ele gera uma sugestão de receita que atende a essas preferências:

```plaintext
Welcome to the recipe suggestion bot!
Dietary restrictions: Vegan
Ingredients: tofu, spinach, rice
Experience level: beginner
Spice level: 3
Processing...

Bot:
Sugiro um prato simples de tofu com espinafre refogado e arroz. Esse prato vegano é leve, nutritivo e fácil de preparar.
```

## 🔧 Estrutura do Projeto

- `weather.py`: Script para recomendações de vestimenta e alimentação com base nas condições climáticas.
- `recipes.py`: Script para sugestões de receitas baseadas em preferências alimentares e nível de experiência.
- `.env`: Arquivo para armazenar a chave de API da OpenWeather de forma segura.


## 🔗 Recursos Adicionais

- [Documentação LangChain](https://python.langchain.com/)
- [API da Ollama](https://ollama.com/api)
- [API OpenWeather](https://openweathermap.org/api)

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar PRs ou sugerir melhorias.

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.


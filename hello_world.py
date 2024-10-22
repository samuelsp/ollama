from langchain_ollama import OllamaLLM
model = OllamaLLM(model="llama3")
result = model.invoke(input='Hello, world!')
print(result)

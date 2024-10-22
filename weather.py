import os
import requests
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3")
load_dotenv('.env', override=True)
api_key = os.getenv('WEATHER_API_KEY')


def call_model(template, chain):
    return chain.invoke({"context": template, "question": 'Suggest clothing and food based on the weather conditions'})

def handle_conversation():    
    print('Welcome suggestion bot!\n')
    
    while True:       
        city = input('Which city do you want to check? ')
        data = get_weather(city=city)
        
        if data is not None:
            temperature = data['temperature']
            description = data['description']
            weather     = data['weather']
            city        = data['city']
        
            template = f'''
                        The temperature is {temperature:.2f} currently, 
                        the weather is {weather} and the climate is {description} 
                        in the city of {city}.
                        
                        Output example:
                        Para a temperatura de {temperature:.2f}°C, com um clima que está ... na cidade de {city}, você deve considerar usar roupas... e comer ...
    
                        Respond only in Portuguese of Brazil and make sure your answer is clear, concise and correct.
                    '''
        
            print('Thinking wait...')
            prompt = ChatPromptTemplate.from_template(template)
            chain  = prompt | model    
            result = call_model(template, chain)
        
            context = f"\nBot: \n{result}"
            print(context)
            context = ''
        
        else:
            print(data)
        
        user_input = input('\nWant more suggestions? ')        
        if user_input in ['exit', 'quit', 'no']:
            break
                            

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == '404':
        return 'City not found'    
    
    return {
                'temperature' : data['main']['temp'],
                'weather'     : data['weather'][0]['main'],
                'description' : data['weather'][0]['description'],
                'city'        : data['name'],
                'country'     : data['sys']['country'],
                'latitude'    : data['coord']['lat'],
                'longitude'   : data['coord']['lon'],
                'cod'         : data['cod']
        }  
    

if __name__ == '__main__':
    handle_conversation()
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3")
    
def call_model(template, chain):
    return chain.invoke({"context": template, "question": 'Suggest recipes with my preferences'})

def handle_conversation():    
    print('Welcome to the recipe suggestion bot!\n')
    
    while True:  
        restrictions = input('Dietary restrictions: ')
        ingredients  = input('Ingredients: ').strip().lower().split(',')
        experience   = input('Experience level: ')
        spice_level  = input('Spice level: ')
        
        food_preferences = {
            "dietary_restrictions": restrictions,
            "favorite_ingredients": ingredients,
            "experience_level": experience,
            "maximum_spice_level": spice_level
        }
        
        template = f'''
            Please suggest a recipe that tries to include the following ingredients:
            {food_preferences['favorite_ingredients']}.
            The recipe should adhere to the following dietary restrictions:
            {food_preferences['dietary_restrictions']}.
            The difficulty of the recipe should be: 
            {food_preferences['experience_level']}
            The maximum spice level on a scale of 10 should be: 
            {food_preferences['maximum_spice_level']} 
            Provide a two sentence description.'''           
          
        print('Processing...')
        prompt = ChatPromptTemplate.from_template(template)
        chain  = prompt | model    
        result = call_model(template, chain)
        
        context = f"\nBot: \n{result}"
        print(context)
        context = ''
        
        user_input = input('\nWant more recipe suggestions? ')        
        if user_input in ['exit', 'quit', 'no']:
            break
                            
if __name__ == '__main__':
    handle_conversation()
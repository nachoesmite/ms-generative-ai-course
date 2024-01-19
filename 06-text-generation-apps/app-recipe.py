import openai
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 

# enable below if you use Azure Open AI
# openai.api_type = 'azure' 
# openai.api_version = '2023-05-15'
# openai.api_base = os.getenv("API_BASE")


no_recipes = 10

ingredients = "carne roja, pescado, pollo, garbanzos, lentejas, porotos negros, vegetales, arroz, cuscus"

# interpolate the number of recipes into the prompt an ingredients
prompt = f"""Listame {no_recipes} recetas por su nombre. Voy a buscar estos platos para cocinarlos en una thermomix(cookidoo). 
  Dentro de esos platos quiero que sean 3 con carne roja, 3 con pescado o pollo y 4 con legumbres: {ingredients}, idealmente me gustaria la lista mezclando las restricciones y ordenados de lunes a viernes(almuerzo y cena).
"""
print(prompt)
# engine

# deployment_id
# deployment_name = os.getenv("DEPLOYMENT_NAME")

completion = openai.chat.completions.create(model="gpt-3.5-turbo",messages = [{"role": "user", "content": prompt}], max_tokens=600, temperature=0.1)

# print response
print("Recipes:")
print(completion.choices[0].message.content)

# old_prompt_result = completion.choices[0].text
# prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "

# new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
# completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=600)

# # print response
# print("\n=====Shopping list ======= \n")
# print(completion.choices[0].text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.


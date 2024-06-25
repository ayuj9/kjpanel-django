from .models import Names  # Adjust the import based on your project structure
import json



def run(n):
    with open('text.json', 'r') as f:
        data = json.load(f)
        
        for i in range(1,n):  # Assuming your JSON has 830+ entries
            try:
                id = data[str(i)]['ID']  # Accessing data with str(i) as key
                name = data[str(i)]['Name']
                recipe_link = data[str(i)]['RecipeLink']  # Adjust for correct key name
           
                Names.objects.create(
                    id=id,
                    name=name,
                    recipeLink=recipe_link
                )
                
                
            except KeyError:
                print(f"KeyError: Entry with index {i} not found in JSON.")
                continue
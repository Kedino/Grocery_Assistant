Project Grocery Assistant for Hackathon. 
The aim of this project is to convince my wife that coding can have useful application in everyday life. It serves as a repository for recipes, and generates a shopping list based on the selected recipes. 

The program generates both a recipe list json file and a shopping list txt file so data can persist through sessions and for easy printing. 

Other than importing os and json, it has no dependencies, and runs on python version 3.12 or greater. 
Create environment with uv and run with "uv run main.py"


Future improvements: 
- interface. I would like to create a web interface for this, so my wife can add recipes at home, and I can print a shopping list before I leave the office. 
- recipe data. with an improved interface, it would be prudent to add more information about each recipe. I would have to change the format they are stored in, so both a description and instructions could be added to each recipe. 
- to be decided...
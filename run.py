import json
from script import executeScript

# Import input.json file
with open('./input.json') as file:
    input_data = json.load(file)

variables = {}
for variable in input_data['variables']:
    variables[variable['name']] = variable['value']

# Execute the script and print the JSON output with indentation for readability
result = executeScript(variables)
formatted_result = json.dumps(result, indent=2)
print("\033[1;32;40m" + formatted_result + "\033[0m")


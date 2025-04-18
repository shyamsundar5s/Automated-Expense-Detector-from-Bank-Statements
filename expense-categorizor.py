import json

def load_rules():
    with open("src/categorizer/rules.json", "r") as f:
        return json.load(f)

def categorize_expenses(data):
    rules = load_rules()
    categorized = []
    for line in data:
        category = "Uncategorized"
        for rule, cat in rules.items():
            if rule in line:
                category = cat
                break
        categorized.append({"line": line, "category": category})
    return categorized
  

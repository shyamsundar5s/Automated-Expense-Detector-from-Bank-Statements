import matplotlib.pyplot as plt

def generate_visuals(categorized_data):
    categories = {}
    for item in categorized_data:
        category = item['category']
        categories[category] = categories.get(category, 0) + 1
    
    plt.bar(categories.keys(), categories.values())
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()

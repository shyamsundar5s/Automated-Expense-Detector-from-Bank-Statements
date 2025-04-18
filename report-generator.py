import pandas as pd

def export_to_excel(categorized_data, output_path):
    df = pd.DataFrame(categorized_data)
    df.to_excel(output_path, index=False)

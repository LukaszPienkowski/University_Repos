import pandas as pd
from tabulate import tabulate

# Define a custom DataFrame class
class CustomDataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        column_names = self.columns.tolist()
        column_types = self.dtypes.tolist()
        null_counts = self.isnull().sum().tolist()
        total_counts = len(self)
        null_percentages = [f"{(count/total_counts)*100:.1f}%" for count in null_counts]
        
        null_all = [f"{count} ({perc})" for count, perc in zip(null_counts, null_percentages)]

        info_df = pd.DataFrame({'Column Name': column_names, 'Data Type': column_types, 'Null Count': null_all})
        
        shape_info = f"Rows: {total_counts}, Columns: {len(column_names)}"
        table = tabulate(info_df, headers='keys', showindex=False, tablefmt='psql')
        
        return shape_info + '\n\n' + table
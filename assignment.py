# Import the pandas library for data manipulation
import pandas as pd
# Read data from a CSV file into a pandas DataFrame
data = pd.read_csv("brca_cnvs_tcga.csv")
# Add a new column 'length' which is calculated as loc.end - loc.start
# This represents the length of the gene
data['length'] = data['loc.end'] - data['loc.start']
# Write the output to a new file
output_file = 'output.csv'
data.to_csv(output_file, index=False)
print(f"Output written to {output_file}")

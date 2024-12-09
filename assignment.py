# Import the pandas library for data manipulation
import pandas as pd
# Read data from a CSV file into a pandas DataFrame
data = pd.read_csv("brca_cnvs_tcga.csv")
# Add a new column 'length' which is calculated as loc.end - loc.start
# This represents the length of the gene
data['length'] = data['loc.end'] - data['loc.start']
new_data = data

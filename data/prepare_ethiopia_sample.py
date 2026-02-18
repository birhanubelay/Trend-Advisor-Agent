import pandas as pd

# Load primary CORGIS file (adjust filename if yours is different)
corgis = pd.read_csv('data/coffee.csv', low_memory=False)

# Load Kaggle export and production (select only Ethiopia)
export = pd.read_csv('data/Coffee_export.csv', low_memory=False)
production = pd.read_csv('data/Coffee_production.csv', low_memory=False)

# Filter Ethiopia from Kaggle files
eth_export = export[export['Country'] == 'Ethiopia'].copy()
eth_production = production[production['Country'] == 'Ethiopia'].copy()

# Filter Ethiopia from CORGIS (case insensitive)
eth_corgis = corgis[corgis['Location.Country'].str.contains('Ethiopia', case=False, na=False)].copy()

# Save small samples
eth_corgis.to_csv('data/ethiopia_corgis_sample.csv', index=False)
eth_export.to_csv('data/ethiopia_export_sample.csv', index=False)
eth_production.to_csv('data/ethiopia_production_sample.csv', index=False)

print("Created samples:")
print("- ethiopia_corgis_sample.csv :", len(eth_corgis), "rows")
print("- ethiopia_export_sample.csv :", len(eth_export), "rows")
print("- ethiopia_production_sample.csv :", len(eth_production), "rows")
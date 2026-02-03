import pandas as pd
import psycopg2 as ps

##Ensuring all kept fields are non-null
df_ingest = df_ingest.dropna(subset=['Book Name', 'Publishing Year', 'Author', 'Publisher ', 'sale price', 'genre', 'publisher revenue'])

df_ingest[['units sold', 'gross sales']].fillna(0)
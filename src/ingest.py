import pandas as pd
import psycopg2 as ps
import datetime as dt

source_file = 'raw/data/Books_Data.csv'

df_ingest = pd.read_csv(source_file)

rows_in = len(df_ingest)
##Removing unneccessary columns and columns we should be creating ourselves later
df_ingest.drop(columns=['language_code', 'index', 'sales rank', 'Author_rating'], inplace=True)

print(df_ingest.shape)

##Ensuring columns are in the correct name convention for later work
df_ingest.rename(columns={'Publisher ':'publisher', 'Book Name': 'title', 'Publishing Year':'publishing_year', 'Author':'author',
                          'Book_average_rating':'book_average_rating', 'Book_ratings_count':'book_ratings_count', 'sale price':'sale_price',
                          'gross sales':'gross_sales', 'publisher revenue': 'publisher_revenue', 'units sold':'units_sold'}, inplace=True)
 
rows_out = len(df_ingest)

log_df = pd.DataFrame({'rows_in': [rows_in], 'rows_out': [rows_out], 'source_file': [source_file], 'ingestion_timestamp':[dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]})

print(log_df.head())
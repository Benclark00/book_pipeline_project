import pandas as pd
import psycopg2 as ps


def load_data(source_file):
    df_ingest = pd.read_csv(source_file)

    ##Removing unneccessary columns and columns we should be creating ourselves later
    df_ingest.drop(columns=['language_code', 'index', 'sales rank', 'Author_Rating'], inplace=True)


    ##Ensuring columns are in the correct name convention for later work
    df_ingest.rename(columns={'Publisher ':'publisher', 'Book Name': 'title', 'Publishing Year':'publishing_year', 'Author':'author',
                            'Book_average_rating':'book_average_rating', 'Book_ratings_count':'book_ratings_count', 'sale price':'sale_price',
                            'gross sales':'gross_sales', 'publisher revenue': 'publisher_revenue', 'units sold':'units_sold'}, inplace=True)
    
    return df_ingest
    

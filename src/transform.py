import pandas as pd
import psycopg2 as ps
import datetime as dt

def transform(ingestion_df, source_file):
    transform_df = ingestion_df.copy()

    ##Rows upon ingestion for logging purposes
    rows_in = len(transform_df)

    ##Ensuring all kept fields are non-null
    transform_df = transform_df.dropna(subset=['title', 'publishing_year', 'author', 'publisher', 'sale_price', 'genre', 'publisher_revenue'])
    transform_df[['units_sold', 'gross_sales']].fillna(0)

    ##Ensuring all rows have proper typing
    transform_df['publishing_year'] = transform_df['publishing_year'].astype(int)

    ##Generating some needed columns
    transform_df.insert(0, 'book_id', range(1, len(transform_df) + 1))
    transform_df['sales_rank'] = transform_df['units_sold'].rank(method='dense', ascending=False).astype(int)
    transform_df['company_revenue'] = round(((transform_df['sale_price'] * transform_df['units_sold']) - transform_df['publisher_revenue']),2)

    ##Generating month for sales, will be ingesting data from the previous month
    current_month = dt.datetime.now().month
    if (current_month == 1):
        transform_df['sales_month'] = 12
    else:
        transform_df['sales_month'] = current_month - 1

    ##Rows left after transformations for logging purposes
    rows_out = len(transform_df)

    ##Creating Logs for Database table
    log_df = pd.DataFrame({'rows_in': [rows_in], 'rows_out': [rows_out], 'source_file': [source_file], 'ingestion_timestamp':[dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]})

    transform_df.to_csv(r'raw\data\books_transformed.csv', index=False)
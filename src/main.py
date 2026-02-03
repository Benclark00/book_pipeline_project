from ingest import load_data
from transform import transform

source_file = 'raw\data\Books_Data.csv'

ingested_data = load_data(source_file)

transformed_data = transform(ingested_data, source_file)
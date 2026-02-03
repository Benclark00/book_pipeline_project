# Book Sales Pipeline Project
In this repository I have created a pipeline to help aid a bookseller with daily sales data ingestion. This pipeline serves to help clean, validate, enrich the data with calculated and load it into a postgreSQL analytical warehouse. This process is set up to ensure that the data will go through the transformations and validations in a safe and replicable manner.
<br>
## Final Table Structure
- book_id (generated) PK int
- book_name string
- author string
- genre string
- publishing_year int
- book_avg_rating real
- book_ratings_count int
- units_sold int
- gross_sales real
- publisher_revenue real
- sales_rank int (generated)
- net_sales (generated)
- ingestion_date (generated) timestamp
<br>
The original dataset is from Kaggle here is a link to the [dataset](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings?resource) if you are interested in utilizing it in your own projects.

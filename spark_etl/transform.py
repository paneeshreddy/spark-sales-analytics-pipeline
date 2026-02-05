from scripts.create_spark_session import create_spark_session
from pyspark.sql.functions import col

def transform_data(df):
    # Cast columns to numeric types
    df = df.withColumn("quantity", col("quantity").cast("int")) \
           .withColumn("price", col("price").cast("float")) \
           .withColumn("total_price", col("quantity") * col("price"))

    # Total revenue per country
    total_revenue = df.groupBy("country").sum("total_price").withColumnRenamed("sum(total_price)", "total_revenue")

    # Total quantity per country
    total_quantity = df.groupBy("country").sum("quantity").withColumnRenamed("sum(quantity)", "quantity")

    # Top 5 products by revenue
    top_products = df.groupBy("product_id").sum("total_price").withColumnRenamed("sum(total_price)", "total_price")
    top_products = top_products.orderBy("total_price", ascending=False).limit(5)

    return total_revenue, total_quantity, top_products

if __name__ == "__main__":
    spark = create_spark_session()
    df = spark.read.option("header", True).csv("data/raw/sales.csv")
    total_revenue, total_quantity, top_products = transform_data(df)

    print("--- Total Revenue by Country ---")
    total_revenue.show()

    print("--- Total Quantity by Country ---")
    total_quantity.show()

    print("--- Top 5 Products by Revenue ---")
    top_products.show()

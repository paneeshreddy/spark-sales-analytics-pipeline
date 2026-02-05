from scripts.create_spark_session import create_spark_session
from transform import transform_data

def load_data(df, file_path):
    df.coalesce(1).write.mode("overwrite").option("header", True).csv(file_path)

if __name__ == "__main__":
    spark = create_spark_session()
    
    # Read raw data
    df = spark.read.option("header", True).csv("data/raw/sales.csv")
    
    # Transform data
    total_revenue, total_quantity, top_products = transform_data(df)
    
    # Save aggregated analytics
    load_data(total_revenue, "data/processed/total_revenue")
    load_data(total_quantity, "data/processed/total_quantity")
    load_data(top_products, "data/processed/top_products")
    
    # Save full transformed dataset
    load_data(df, "data/processed/sales_transformed")
    
    # Save daily revenue trends
    daily_revenue = df.groupBy("order_date").sum("price").withColumnRenamed("sum(price)", "total_price")
    load_data(daily_revenue, "data/processed/daily_revenue")
    
    print("Data saved to data/processed/")

from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == "__main__":
    # Step 1: Extract
    df = extract_data("data/raw/sales.csv")
    
    # Step 2: Transform
    total_revenue, total_quantity, top_products = transform_data(df)
    
    # Step 3: Load
    load_data(total_revenue, "data/processed/total_revenue")
    load_data(total_quantity, "data/processed/total_quantity")
    load_data(top_products, "data/processed/top_products")
    
    print("ETL pipeline completed successfully!")

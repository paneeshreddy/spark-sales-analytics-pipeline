from scripts.create_spark_session import create_spark_session

def extract_data(file_path):
    spark = create_spark_session()
    df = spark.read.option("header", True).csv(file_path)
    return df

if __name__ == "__main__":
    df = extract_data("data/raw/sales.csv")
    df.show(5)

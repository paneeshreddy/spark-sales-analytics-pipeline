from pyspark.sql import SparkSession


def create_spark_session(app_name="SparkSalesAnalytics"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .getOrCreate()

    return spark


if __name__ == "__main__":
    spark = create_spark_session()
    print("Spark Session Created Successfully")
    spark.stop()

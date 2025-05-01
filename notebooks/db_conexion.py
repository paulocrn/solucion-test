from pyspark.sql import SparkSession
import os

def get_spark_session():
    jar_path = os.path.abspath("postgresql-42.7.5.jar")

    return SparkSession.builder \
        .appName("MP3") \
        .config("spark.jars", jar_path) \
        .config("spark.driver.extraClassPath", jar_path) \
        .getOrCreate()



def get_postgres_connection():
    url = "jdbc:postgresql://localhost:5432/postgres"
    properties = {
        "user": "postgres",
        "password": "postgres",
        "driver": "org.postgresql.Driver"
    }
    return url, properties


def load_table(spark, table_name):
    url, properties = get_postgres_connection()
    return spark.read.jdbc(url=url, table=table_name, properties=properties)


def write_table(df, table_name, mode="append"):
    url, properties = get_postgres_connection()
    df.write.jdbc(url=url, table=table_name, mode=mode, properties=properties)


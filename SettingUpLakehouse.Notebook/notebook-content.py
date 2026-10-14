# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1554b255-456e-462f-9df7-9004bfa6f6f7",
# META       "default_lakehouse_name": "MultipleSchemaLakehouse",
# META       "default_lakehouse_workspace_id": "c475b9ff-eabc-4800-8af9-8e54579414ec",
# META       "known_lakehouses": [
# META         {
# META           "id": "1554b255-456e-462f-9df7-9004bfa6f6f7"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df_public = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("Files/public_data.csv")
)

df_public.write.mode("overwrite").saveAsTable(
    "dbo.public_data"
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""
    CREATE SCHEMA IF NOT EXISTS restricted_schema
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_customer = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("Files/customer_data.csv")
)

df_customer.write.mode("overwrite").saveAsTable(
    "restricted_schema.customer_data"
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("SHOW SCHEMAS").show(truncate=False)

display(spark.sql("SHOW TABLES IN dbo"))
display(spark.sql("SHOW TABLES IN restricted_schema"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

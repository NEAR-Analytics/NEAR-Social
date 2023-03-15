# Databricks notebook source
# MAGIC %sql
# MAGIC select
# MAGIC 	collected_for_day,
# MAGIC 	mau as mau_30_trailing
# MAGIC from mainnet_analytics.daily_accounts_stickiness
# MAGIC where collected_for_day between current_date()::date - interval '12' month AND current_date()::date - interval '1' day
# MAGIC order by 1 desc

# COMMAND ----------

_sqldf.toPandas().to_csv('https://github.com/NEAR-Analytics/NEAR-Social/data/mau_test.csv')

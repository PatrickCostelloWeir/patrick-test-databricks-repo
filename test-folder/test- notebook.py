# Databricks notebook source
# MAGIC %md #Test Repo Notebook

# COMMAND ----------

x=1
print(x)

# COMMAND ----------

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100,2),columns=["a","b"])

df.plot()



# COMMAND ----------



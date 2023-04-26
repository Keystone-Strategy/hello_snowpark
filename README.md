# Getting started with Snowpark
This repository contains resources to help set up the Snowpark environment and learn basic data transofomartions.

To get started, first make download all the packages needed for Snowpark in a virtual environment by running the followign commands in your terminal once your in the correct respository.  <br>
<code>conda env create -f conda_env.yml <br>
conda activate pysnowpark </code> <br> 

Once you are in the file you're coding in, add the following import statements. 
from snowflake.snowpark.session import Session

<code>import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T
import getpass
import pandas as pd </code>

Then enter your connection parameters and run the code block.
    
<code>connection_parameters = {
    "account": "<your snowflake account>",
    "user": "<your snowflake user>",
    "password": "<your snowflake password>",
    "role": "<your snowflake role>",  # optional
    "warehouse": "<your snowflake warehouse>",  # optional
    "database": "<your snowflake database>",  # optional
    "schema": "<your snowflake schema>",  # optional
  }  </code>

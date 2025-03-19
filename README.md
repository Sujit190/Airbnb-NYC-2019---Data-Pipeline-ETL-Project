# Airbnb-NYC-2019---Data-Pipeline-ETL-Project

# Overview

This project implements an ETL (Extract, Transform, Load) pipeline for processing Airbnb NYC 2019 dataset. The pipeline extracts data from a CSV file, applies preprocessing transformations (handling missing values, encoding categorical variables, and scaling numerical data), and saves the processed data for further analysis.

# Features

  Extract: Reads raw data from AB_NYC_2019.csv.

# Transform:

  - Handles missing values.
  
  - Encodes categorical variables using One-Hot Encoding.
  
  - Scales numerical features using StandardScaler.
  
  - Removes high-cardinality columns (name, host_name).
  
  - Load: Saves the transformed dataset as processed_data.csv.

# Dependencies

  - This project requires Python 3.12+ and the following libraries:

        pip install pandas scikit-learn

# Usage

  - Run the ETL pipeline using the following command:
  
        python DataPipeline.py
  
  - Make sure the input file (AB_NYC_2019.csv) is present in the same directory.

# Project Structure

-       AB_NYC_2019.csv           # Raw dataset
-       DataPipeline.py           # ETL script
-       processed_data.csv        # Processed dataset (output)
-       README.md                 # Project documentation

# Error Handling

 - File Not Found: Ensures the input file exists before processing.
 - Empty DataFrame: Checks if the dataset is empty before transformation.
 - Column Validation: Verifies the presence of valid numerical and categorical columns.
 - Transformation Errors: Handles errors during scaling and encoding.
  
# License
  This project is licensed under the MIT License.

# Author
  Sujit Dinkar

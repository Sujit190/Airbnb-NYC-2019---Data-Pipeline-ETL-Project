import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os
import traceback

def extract_data(file_path):
    """Loads data from a CSV file with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file '{file_path}' does not exist.")
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")

def transform_data(df):
    """Preprocesses the data by handling missing values, encoding categorical features, and scaling numerical features."""
    if df.empty:
        raise ValueError("Error: The input DataFrame is empty.")
    
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    # Remove high-cardinality categorical features
    categorical_features = df.select_dtypes(include=['object']).columns.tolist()
    high_cardinality_cols = ["name", "host_name"]  # Dropping these from encoding
    categorical_features = [col for col in categorical_features if col not in high_cardinality_cols]
    
    print("Numerical Features:", numerical_features)
    print("Categorical Features (Processed):", categorical_features)

    if not numerical_features and not categorical_features:
        raise ValueError("Error: No valid numerical or categorical columns found.")

    # Define transformations
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # Combine transformations
    preprocessor = ColumnTransformer([
        ('num', num_pipeline, numerical_features),
        ('cat', cat_pipeline, categorical_features)
    ])

    try:
        print("Applying transformations...")
        transformed_data = preprocessor.fit_transform(df)
        print(f"Transformation successful! Output shape: {transformed_data.shape}")
        
        cat_feature_names = preprocessor.named_transformers_['cat'].named_steps['encoder'].get_feature_names_out(categorical_features)
        transformed_df = pd.DataFrame(
            transformed_data, 
            columns=numerical_features + list(cat_feature_names)
        )
        return transformed_df
    except Exception as e:
        print(f"Error during transformation: {e}")
        import traceback
        traceback.print_exc()
        raise
    
def load_data(df, output_path):
    """Saves the processed data to a CSV file with error handling."""
    try:
        df.to_csv(output_path, index=False)
    except Exception as e:
        raise IOError(f"Error saving data: {e}")

def main():
    input_file = 'AB_NYC_2019.csv'  # Ensure correct file path
    output_file = 'processed_data.csv'

    try:
        print("Extracting data...")
        data = extract_data(input_file)
        print("Data extracted successfully. Shape:", data.shape)
        
        print("Transforming data...")
        processed_data = transform_data(data)
        print("Data transformed successfully. Shape:", processed_data.shape)

        print("Loading data...")
        load_data(processed_data, output_file)
        print("ETL process completed successfully!")

    except Exception as e:
        print(f"Pipeline Error: {e}")
        traceback.print_exc()  # Print full error details

if __name__ == "__main__":
    main()
from data_ingestion import DataIngestion
import os
import pandas as pd

# Initialize the DataIngestion object
data_ingestion = DataIngestion()

# Run the data ingestion process
try:
    train_path, test_path = data_ingestion.initiate_data_ingestion()

    # Check if the files are created
    if os.path.exists(train_path) and os.path.exists(test_path):
        print(f"Train and test files created successfully:")
        print(f"Train data path: {train_path}")
        print(f"Test data path: {test_path}")
        print('length of train_set ',len(train_path))
        print('length of test_set ',len(test_path))

        # Optionally, load the data to verify contents
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        print("\nSample Train Data:")
        print(train_df.head())

        print("\nSample Test Data:")
        print(test_df.head())
    else:
        print("Error: Train and test files were not created.")
except Exception as e:
    print(f"An error occurred during testing: {e}")

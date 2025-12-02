import pandas as pd
import numpy as np
import os

def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"Original dataset shape: {df.shape}")
    return df

def handle_missing_values(df):
    print(f"\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    df = df.dropna(subset=['OBS_VALUE'])
    df['REF_AREA_LABEL'] = df['REF_AREA_LABEL'].fillna('Unknown')
    
    print(f"\nMissing values after cleaning:")
    print(df.isnull().sum())
    
    return df

def clean_data(df):
    df['TIME_PERIOD'] = pd.to_datetime(df['TIME_PERIOD'])
    df = df.sort_values(['REF_AREA', 'TIME_PERIOD'])
    df = df.reset_index(drop=True)
    
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved to: {output_path}")
    print(f"Final dataset shape: {df.shape}")

def main():
    input_file = '../data/food_price_inflation.csv'
    output_file = '../data/clean_food_price_inflation.csv'
    
    df = load_data(input_file)
    df = handle_missing_values(df)
    df = clean_data(df)
    save_cleaned_data(df, output_file)
    
    print("\nData cleaning completed successfully!")

if __name__ == "__main__":
    main()

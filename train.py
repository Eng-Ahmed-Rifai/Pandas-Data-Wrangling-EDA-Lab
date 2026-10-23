"""
Pandas Data Wrangling & Feature Engineering Lab: WHO Life Expectancy Pipeline
Handling Missing Data, Outlier Winsorization, and Correlation Analysis
Author: Eng. Ahmed Rifai
"""

import numpy as np
import pandas as pd

def generate_raw_who_data(n_countries=193, n_years=16, random_state=42):
    np.random.seed(random_state)
    records = []
    
    statuses = ['Developed'] * 32 + ['Developing'] * (n_countries - 32)
    
    for i in range(n_countries):
        country_name = f"Country_{i+1:03d}"
        status = statuses[i]
        base_gdp = np.random.uniform(25000, 85000) if status == 'Developed' else np.random.uniform(800, 15000)
        base_life = np.random.uniform(78, 84) if status == 'Developed' else np.random.uniform(52, 74)
        
        for y in range(2000, 2000 + n_years):
            gdp = base_gdp * (1 + 0.02 * (y - 2000)) + np.random.normal(0, 1000)
            life = base_life + 0.15 * (y - 2000) + np.random.normal(0, 1.2)
            mortality = max(10, int(350 - 3.2 * life + np.random.normal(0, 15)))
            schooling = np.clip(16 + np.random.normal(0, 1) if status == 'Developed' else 11 + np.random.normal(0, 2), 2, 21)
            
            # Inject realistic missing values (NaN)
            if np.random.rand() < 0.15: gdp = np.nan
            if np.random.rand() < 0.05: schooling = np.nan
            if np.random.rand() < 0.08: mortality = np.nan
            
            records.append({
                'Country': country_name,
                'Year': y,
                'Status': status,
                'LifeExpectancy': life,
                'AdultMortality': mortality,
                'GDP': gdp,
                'Schooling': schooling
            })
            
    return pd.DataFrame(records)

def run_wrangling_pipeline():
    df = generate_raw_who_data()
    print("--- 1. Raw Ingestion Overview ---")
    print(f"Shape: {df.shape}")
    print("Missing values per column:\n", df.isnull().sum())
    
    print("\n--- 2. Missing Value Imputation ---")
    # Impute numeric columns grouped by Economic Status
    numeric_cols = ['LifeExpectancy', 'AdultMortality', 'GDP', 'Schooling']
    for col in numeric_cols:
        df[col] = df.groupby('Status')[col].transform(lambda x: x.fillna(x.median()))
    print("Missing values post-imputation:\n", df.isnull().sum())
    
    print("\n--- 3. Outlier Handling via IQR Winsorization ---")
    for col in ['AdultMortality', 'GDP']:
        q25 = df[col].quantile(0.25)
        q75 = df[col].quantile(0.75)
        iqr = q75 - q25
        lower_bound = q25 - 1.5 * iqr
        upper_bound = q75 + 1.5 * iqr
        outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
        df[col] = np.clip(df[col], lower_bound, upper_bound)
        print(f"Column [{col}] clipped {outliers} outliers.")
        
    print("\n--- 4. Summary Correlation Matrix ---")
    corr = df[numeric_cols].corr()
    print(corr.round(3))
    
    return df

if __name__ == "__main__":
    run_wrangling_pipeline()

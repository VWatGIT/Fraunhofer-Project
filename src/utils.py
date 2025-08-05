"""
Utility functions for the Fraunhofer project.

This module contains helper functions that can be imported and used
across different notebooks in the project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def setup_plotting_style():
    """Set up a consistent plotting style across notebooks."""
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12


def load_data(filename, data_dir="../data"):
    """
    Load data from the data directory.
    
    Args:
        filename (str): Name of the file to load
        data_dir (str): Path to the data directory
        
    Returns:
        pd.DataFrame or None: Loaded data or None if file not found
    """
    data_path = Path(data_dir) / filename
    
    if not data_path.exists():
        print(f"File {data_path} not found.")
        return None
    
    file_extension = data_path.suffix.lower()
    
    try:
        if file_extension == '.csv':
            return pd.read_csv(data_path)
        elif file_extension in ['.xlsx', '.xls']:
            return pd.read_excel(data_path)
        elif file_extension == '.json':
            return pd.read_json(data_path)
        elif file_extension == '.parquet':
            return pd.read_parquet(data_path)
        else:
            print(f"Unsupported file format: {file_extension}")
            return None
    except Exception as e:
        print(f"Error loading file {filename}: {e}")
        return None


def save_figure(fig, filename, output_dir="../outputs", dpi=300):
    """
    Save a matplotlib figure to the outputs directory.
    
    Args:
        fig: Matplotlib figure object
        filename (str): Name of the output file
        output_dir (str): Path to the outputs directory
        dpi (int): Resolution for the saved figure
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    full_path = output_path / filename
    fig.savefig(full_path, dpi=dpi, bbox_inches='tight')
    print(f"Figure saved to {full_path}")


def describe_dataframe(df):
    """
    Provide a comprehensive description of a DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame to describe
    """
    print("=== DataFrame Info ===")
    print(f"Shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print("\n=== Column Info ===")
    print(df.dtypes)
    print("\n=== Missing Values ===")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("No missing values found.")
    print("\n=== Summary Statistics ===")
    print(df.describe())

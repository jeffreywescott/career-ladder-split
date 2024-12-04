#!/usr/bin/env python3

import argparse
import sys
import os
import re

import pandas as pd

def split_data_into_job_levels(input_file, output_folder):
    """
    Splits the input Excel file into separate spreadsheets for each job level.

    Args:
        input_file (str): Path to the input Excel or CSV file.
        output_folder (str): Folder to save the output Excel files.

    Returns:
        None
    """
    # Load the data
    if input_file.endswith('.csv'):
        df_raw = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        df_raw = pd.read_excel(input_file)
    else:
        raise ValueError("Input file must be a .csv or .xlsx")

    # Extract job levels
    job_levels = df_raw.columns[1:]  # Job levels are in the second column onwards

    # Process and save files for each job level
    for level in job_levels:
        rows = []
        for index, row in df_raw.iterrows():
            competency = row['Levels']
            behaviors = re.split(r'\n|\.\s', str(row[level]))
            for behavior in behaviors:
                if behavior.strip():
                    rows.append({'Competency Area': competency, 'Competency at Level': behavior.strip()})

        # Create a DataFrame for the level
        level_df = pd.DataFrame(rows)
        # Save the DataFrame to an Excel file
        output_file = f"{output_folder}/{level.replace(' ', '_').replace('/', '_')}_Behaviors.csv"
        level_df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")

def main():
    parser = argparse.ArgumentParser(
        description='Split career ladder assessment data into separate spreadsheets for each job level.',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input_file', 
                        help='Path to the input Excel (.xlsx) or CSV (.csv) file')
    parser.add_argument('output_folder', 
                        help='Path to the folder where output files will be saved')

    args = parser.parse_args()

    # Validate input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist")
        sys.exit(1)

    # Create output folder if it doesn't exist
    os.makedirs(args.output_folder, exist_ok=True)

    try:
        split_data_into_job_levels(args.input_file, args.output_folder)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()

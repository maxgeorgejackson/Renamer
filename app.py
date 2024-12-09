import os
import pandas as pd
import argparse

def search_in_excel(excel_path, search_column, rename_column, hospital_number):
    """
    Search for a value in the specified column across all sheets of an Excel file.
    Return the value from the rename column if a match is found.
    """
    try:
        excel_data = pd.ExcelFile(excel_path)
        for sheet_name in excel_data.sheet_names:
            sheet = excel_data.parse(sheet_name)
            if search_column in sheet.columns and rename_column in sheet.columns:
                match = sheet[sheet[search_column] == hospital_number]
                if not match.empty:
                    return match.iloc[0][rename_column]
    except Exception as e:
        print(f"Error processing Excel file: {e}")
    return None

def rename_files(folder_path, excel_path, search_column, rename_column):
    """
    Rename `.tif` files in the specified folder based on Excel mappings.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".tif"):
            file_path = os.path.join(folder_path, filename)
            
            # Extract text before the first space
            first_part = filename.split(" ", 1)[0]
            rest_of_name = filename.split(" ", 1)[1] if " " in filename else ""
            
            # Search for the hospital number in the Excel file
            biobank_number = search_in_excel(excel_path, search_column, rename_column, first_part)
            
            if biobank_number:
                # Construct new filename and rename file
                new_filename = f"{biobank_number} {rest_of_name}"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
            else:
                print(f"No match found for: {filename}")

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Rename .tif files based on Excel mappings.")
    parser.add_argument("--path_excel", required=True, help="Path to the Excel file")
    parser.add_argument("--path_folder", required=True, help="Path to the folder containing .tif files")
    parser.add_argument("--search_column", required=True, help="Column in Excel to search for (e.g., HOSPITAL NUMBER)")
    parser.add_argument("--rename_column", required=True, help="Column in Excel with new name (e.g., Biobank Number)")

    args = parser.parse_args()

    # Validate paths
    if not os.path.exists(args.path_excel):
        print(f"Error: Excel file does not exist at {args.path_excel}")
        exit(1)

    if not os.path.exists(args.path_folder):
        print(f"Error: Folder does not exist at {args.path_folder}")
        exit(1)

    # Call the rename function with arguments
    rename_files(args.path_folder, args.path_excel, args.search_column, args.rename_column)

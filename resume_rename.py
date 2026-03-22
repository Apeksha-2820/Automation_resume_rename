import os
import pandas as pd
import shutil

# Load data
data = pd.read_csv("data.csv")   # or read_excel

# Source folder (original resumes)
source_folder = "resume_raw"

# Destination folder (renamed resumes)
destination_folder = "resume_renamed"

# Create destination folder if not exists
os.makedirs(destination_folder, exist_ok=True)

files = os.listdir(source_folder)

print("Files found:", files)

# Copy + Rename
for i, file in enumerate(files):
    if file.endswith(".pdf"):
        try:
            name = data.loc[i, "Firstname"]   # adjust column name if needed
            new_name = f"{name}.pdf"

            source_path = os.path.join(source_folder, file)
            dest_path = os.path.join(destination_folder, new_name)

            shutil.copy(source_path, dest_path)

            print(f"Copied: {file} → {new_name}")

        except Exception as e:
            print(f"Error with file {file}: {e}")
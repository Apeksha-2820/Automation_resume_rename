import os
import PyPDF2
import shutil

source_folder = "resume_raw"
destination_folder = "resume_renamed"

os.makedirs(destination_folder, exist_ok=True)

files = os.listdir(source_folder)

def extract_name_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()

    lines = text.split("\n")
    lines = [line.strip() for line in lines if line.strip() != ""]

    # Common unwanted words
    ignore_words = ["resume", "cv", "profile", "objective", "skills", "experience"]

    for line in lines[:10]:  # check first 10 lines
        words = line.split()

        # Conditions for a valid name
        if (
            1 < len(words) <= 3 and  # 2-3 words
            all(word[0].isupper() for word in words if word) and
            not any(char.isdigit() for char in line) and
            "@" not in line and
            not any(ig in line.lower() for ig in ignore_words)
        ):
            return line

    return "Unknown"


for file in files:
    if file.endswith(".pdf"):
        try:
            file_path = os.path.join(source_folder, file)

            extracted_name = extract_name_from_pdf(file_path)

            new_name = f"{extracted_name}.pdf"
            dest_path = os.path.join(destination_folder, new_name)

            shutil.copy(file_path, dest_path)

            print(f"Extracted: {extracted_name} → {file}")

        except Exception as e:
            print(f"Error with file {file}: {e}")
# Resume Automation Project

## 📌 Overview

This project automates the process of renaming resume PDF files by extracting candidate names directly from the content of the resumes.

## 🚀 Features

* Extracts text from PDF resumes
* Identifies candidate names using smart filtering
* Renames files automatically
* Handles duplicate names safely
* Preserves original files

## 🛠️ Tech Stack

* Python
* PyPDF2
* OS module
* shutil

Project Structure
resume_raw/ → contains original resumes
resume_renamed/ → contains renamed resumes
pdf_rename.py → main script

## ▶️ How to Run

1. Install dependencies:
   pip install PyPDF2

2. Place resumes in `resume_raw` folder

3. Run the script:
   python pdf_rename.py

4. Get renamed files in `resume_renamed`

## 💡 Future Improvements

* Use NLP for better name detection
* Build a UI for non-technical users
* Integrate with job portals

## 👤 Author

Apeksha Sarode

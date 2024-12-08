Phone Number Extractor from CSV
Description
This project is a tool to extract phone numbers from multiple CSV files. It supports handling CSV files with both "Telefono" and "Telefono (consigliato)" column names, ensuring that phone numbers are extracted regardless of column name variations. The extracted phone numbers are consolidated into a single Excel file with the current date and time in its name, making it easy to manage and track the data.

Features
Select multiple CSV files from different folders.
Automatically detects and extracts phone numbers from files containing "Telefono" or "Telefono (consigliato)" columns.
Saves the extracted phone numbers into a single Excel file formatted as "phone_numbers_day-month-year_time.xlsx".
Displays errors related to missing or incorrect columns directly in the file list with red text for clear visibility.
Uses try-except blocks for error handling during file loading and processing.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/phone-number-extractor.git
cd phone-number-extractor
Install the required dependencies:

bash
Copy code
pip install pandas
pip install openpyxl
Usage
Run the script to launch the GUI.
Click "Select Files" to choose the CSV files containing phone numbers.
Click "Extract" to extract the phone numbers and save them to an Excel file.
Configuration
No specific configuration is required. The script handles all required settings internally.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
Inspired by client requirements for data management and extraction.
Uses the pandas library for data manipulation and the QFileDialog for file selection.

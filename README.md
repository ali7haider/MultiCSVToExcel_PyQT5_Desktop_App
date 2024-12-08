# Phone Number Extractor from CSV

**Description**

This project is a tool to extract phone numbers from multiple CSV files. It supports handling CSV files with both **"Telefono"** and **"Telefono (consigliato)"** column names, ensuring that phone numbers are extracted regardless of column name variations. The extracted phone numbers are consolidated into a single **Excel** file with the current date and time in its name, making it easy to manage and track the data.

---

## Features

- **Select multiple CSV files** from different folders.
- **Automatically detects and extracts phone numbers** from files containing **"Telefono"** or **"Telefono (consigliato)"** columns.
- **Saves the extracted phone numbers** into a single Excel file formatted as **"phone_numbers_day-month-year_time.xlsx"**.
- **Displays errors** related to missing or incorrect columns directly in the file list with **red text** for clear visibility.
- **Uses try-except blocks** for error handling during file loading and processing.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ali7haider/MultiCSVToExcel_PyQT5_Desktop_App.git
   cd MultiCSVToExcel_PyQT5_Desktop_App
   ```

2. **Install the required dependencies**:
   ```bash
   pip install pandas
   pip install openpyxl
   ```

---

## Usage

1. **Run the script** to launch the GUI.
2. **Click "Select Files"** to choose the CSV files containing phone numbers.
3. **Click "Extract"** to extract the phone numbers and save them into an Excel file.

---

## Configuration

No specific configuration is required. The script handles all necessary settings internally.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](https://opensource.org/licenses/MIT) file for more information.

---

## Acknowledgments

- **Inspired by** client requirements for efficient data management and extraction.
- **Libraries Used**:
  - **pandas**: For data manipulation.
  - **QFileDialog**: For file selection.

---

This format should be more readable and properly formatted for GitHub.

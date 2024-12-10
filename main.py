import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import os
from datetime import datetime
from main_ui import Ui_MainWindow


class PhoneNumberExtractor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PhoneNumberExtractor, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Phone Number Extractor")
        # self.setGeometry(100, 100, 600, 400)

        self.selected_files = []

        # Button to select files
        self.select_button.clicked.connect(self.select_files)

        
        self.extract_button.clicked.connect(self.extract_phone_numbers)

        

    def select_files(self):
        # Open file dialog to select multiple CSV files
        files, _ = QFileDialog.getOpenFileNames(self, "Select CSV Files", "", "CSV Files (*.csv)")
        if files:
            # Add new files to the existing list, avoiding duplicates
            new_files = [file for file in files if file not in self.selected_files]
            self.selected_files.extend(new_files)

            # Update the file display
            if new_files:
                self.file_list_display.append("\n".join(new_files))
            else:
                QMessageBox.information(self, "No New Files", "All selected files are already added.")

    def extract_phone_numbers(self):
        if not self.selected_files:
            QMessageBox.warning(self, "No Files Selected", "Please select at least one CSV file to extract phone numbers.")
            return

        extracted_numbers = []

        self.file_list_display.clear()  # Clear previous logs in the display
        for file in self.selected_files:
            try:
                # Load CSV file into a DataFrame with string data type
                df = pd.read_csv(file, dtype=str)

                # Check if either "Telefono" or "Telefono (consigliato)" exists
                telefono_column = None
                if "Telefono" in df.columns:
                    telefono_column = "Telefono"
                elif "Telefono (consigliato)" in df.columns:
                    telefono_column = "Telefono (consigliato)"

                if telefono_column:
                    # Extract phone numbers and clean data
                    phone_numbers = df[telefono_column].dropna().str.strip()
                    phone_numbers = phone_numbers.str.replace(r'[^\+\d]', '', regex=True)

                    # Filter valid numbers
                    valid_numbers = [num for num in phone_numbers if num.startswith('+') and num[1:].isdigit()]
                    extracted_numbers.extend(valid_numbers)

                    self.file_list_display.append(f"<span style='color:green;'>Processed: {os.path.basename(file)}</span>")
                else:
                    raise ValueError(
                        f"The file '{os.path.basename(file)}' does not contain a valid phone number column ('Telefono' or 'Telefono (consigliato)')."
                    )

            except ValueError as ve:
                # Log error in red color
                self.file_list_display.append(f"<span style='color:red;'>{ve}</span>")
            except Exception as e:
                # Log unexpected error in red color
                self.file_list_display.append(f"<span style='color:red;'>Error in '{os.path.basename(file)}': {e}</span>")

        try:
            if extracted_numbers:
                # Convert extracted numbers to a DataFrame
                final_data = pd.DataFrame(extracted_numbers, columns=["Phone Number"])

                # Get current datetime
                current_datetime = datetime.now()

                # Format datetime as "day-month-year_time" (e.g., "08-12-2024_15-30-45")
                formatted_datetime = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")

                # Use it in the filename
                output_file = f"phone_numbers_{formatted_datetime}.xlsx"

                # Save to Excel file
                final_data.to_excel(output_file, index=False)

                QMessageBox.information(self, "Success", f"Phone numbers extracted successfully to '{output_file}'.")
            else:
                self.file_list_display.append("<span style='color:red;'>No phone numbers were extracted from the selected files.</span>")

        except Exception as e:
            # Log save error in red color
            self.file_list_display.append(f"<span style='color:red;'>An error occurred while saving the Excel file: {e}</span>")

if __name__ == "__main__":
    app = QApplication([])
    window = PhoneNumberExtractor()
    window.show()
    app.exec()

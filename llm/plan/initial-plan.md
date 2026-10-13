# Plan for building the health tracker script

1.  **Read the data:** Read the data from the "Symptom Tracker" worksheet in the "Jami Symptom Tracker" Google Sheet using the existing `process_symptom_data.py` script as a starting point.
2.  **Process the data:**
    *   Create a pandas DataFrame from the raw data.
    *   Split the 'Symptom' column by the "|" delimiter to create a new DataFrame where each symptom is on its own row, while keeping the corresponding 'Date'.
    *   Create a second DataFrame for the other measures ('Mobility' and 'Notes') along with the 'Date'.
3.  **Write the data:**
    *   Clear the "Data Symptoms Table" and "Data Measures Table" worksheets before writing new data.
    *   Write the processed symptom data to the "Data Symptoms Table" worksheet.
    *   Write the other measures data to the "Data Measures Table" worksheet.
4.  **Structure the script:** Organize the code into a Python script that can be run from the command line, ensuring it handles authentication and spreadsheet access correctly.
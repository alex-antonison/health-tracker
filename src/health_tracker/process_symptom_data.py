import argparse
import os

import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


def authenticate_google_sheets():
    """Authenticate with Google Sheets API and return the client."""
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    creds = Credentials.from_service_account_file(
        os.getenv("GOOGLE_CREDENTIAL_LOCATION"), scopes=SCOPES
    )

    return gspread.authorize(creds)


def read_symptom_data(client):
    """Read data from the 'Symptom Tracker' worksheet."""
    sheet_name = os.getenv("SYMPTOM_GOOGLE_SHEET", "Symptom Tracker")
    sheet = client.open(sheet_name).worksheet("Symptom Tracker")
    rows = sheet.get_all_records()
    return pd.DataFrame(rows)


def process_symptoms(df):
    """
    Process the symptom data by splitting the 'Symptom' column by '|' delimiter.
    Each symptom will be on its own row with the corresponding 'Date'.
    """
    # Create a copy of the original dataframe
    symptom_df = df[["Date", "Symptom"]].copy()

    # Split the 'Symptom' column by '|' and explode it to separate rows
    symptom_df["Symptom"] = symptom_df["Symptom"].str.split(" *\\| *")
    symptom_df = symptom_df.explode("Symptom").reset_index(drop=True)

    # Remove any leading/trailing whitespace from symptoms
    symptom_df["Symptom"] = symptom_df["Symptom"].str.strip()

    # Remove any empty rows
    symptom_df = symptom_df[symptom_df["Symptom"] != ""]

    return symptom_df


def process_measures(df):
    """
    Create a DataFrame for the other measures ('Mobility' and 'Notes') along with the 'Date'.
    """
    measures_df = df[["Date", "Mobility", "Notes"]].copy()
    return measures_df


def write_to_worksheet(sheet, worksheet_name, df):
    """Write DataFrame to a specific worksheet, clearing it first."""
    worksheet = sheet.worksheet(worksheet_name)

    # Clear the worksheet
    worksheet.clear()

    # Convert DataFrame to list of lists for writing
    data = [df.columns.tolist()] + df.values.tolist()

    # Write data to worksheet
    worksheet.update("A1", data)


def create_sample_data():
    """Create sample data similar to what would be read from Google Sheets."""
    sample_data = [
        {
            "Date": "10/9/2026",
            "Symptom": "Headache | Fatigue | Nausea",
            "Mobility": "No Assist",
            "Notes": "A bit anxious",
        },
        {
            "Date": "10/10/2026",
            "Symptom": "Headache | Dizziness",
            "Mobility": "No Assist",
            "Notes": "Ate late on the night of the 9th.",
        },
        {
            "Date": "10/11/2026",
            "Symptom": "Fatigue | Nausea | Back Pain | Joint Pain",
            "Mobility": "Minimal Assist",
            "Notes": "Slept well",
        },
    ]
    return pd.DataFrame(sample_data)


def process_health_data(use_test_data=False):
    """Main function to process health data and write to Google Sheets."""
    try:
        if use_test_data:
            # Use sample data instead of reading from Google Sheets
            print("Using sample data for testing...")
            raw_df = create_sample_data()
            print(f"Created {len(raw_df)} rows of sample data.")
        else:
            # Authenticate with Google Sheets and read real data
            client = authenticate_google_sheets()

            # Read data from the "Symptom Tracker" worksheet
            print("Reading data from Google Sheet...")
            raw_df = read_symptom_data(client)
            print(f"Read {len(raw_df)} rows of data.")

        # Process the data
        print("Processing symptom data...")
        symptom_df = process_symptoms(raw_df)
        print(f"Processed {len(symptom_df)} symptom entries.")

        print("Processing measures data...")
        measures_df = process_measures(raw_df)
        print(f"Processed {len(measures_df)} measures entries.")

        if use_test_data:
            # For test data, we'll just print what would be written
            print("\n=== Sample Data Test Results ===")
            print("\nSymptoms that would be written to 'Data Symptoms Table':")
            print(symptom_df.to_string(index=False))
            print("\nMeasures that would be written to 'Data Measures Table':")
            print(measures_df.to_string(index=False))
            print("\nIn a real run, these would be written to the Google Sheets.")
        else:
            # Open the spreadsheet for writing
            sheet_name = os.getenv("SYMPTOM_GOOGLE_SHEET", "Symptom Tracker")
            sheet = client.open(sheet_name)

            # Write processed data to respective worksheets
            print("Writing symptom data to 'Data Symptoms Table'...")
            write_to_worksheet(sheet, "Data Symptoms Table", symptom_df)

            print("Writing measures data to 'Data Measures Table'...")
            write_to_worksheet(sheet, "Data Measures Table", measures_df)

            print("Data processing completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process health data from Google Sheets"
    )
    parser.add_argument(
        "--test-data",
        action="store_true",
        help="Use sample data instead of reading from Google Sheets",
    )

    args = parser.parse_args()
    process_health_data(use_test_data=args.test_data)

def main():
    """Main entry point for the health tracker script."""
    import argparse

    from .process_symptom_data import process_health_data

    parser = argparse.ArgumentParser(
        description="Process health data from Google Sheets"
    )
    parser.add_argument(
        "--test-data",
        action="store_true",
        help="Use sample data instead of reading from Google Sheets",
    )

    # Parse arguments, but ignore the script name
    args = parser.parse_args()
    process_health_data(use_test_data=args.test_data)


if __name__ == "__main__":
    main()

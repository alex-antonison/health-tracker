"""
Simple test to verify the main script can be imported and run.
"""

import sys
import os
import argparse

# Add the src directory to the path so we can import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_import_main():
    """Test that we can import the main module."""
    try:
        import health_tracker
        assert True
    except ImportError:
        assert False, "Could not import health_tracker module"


def test_import_process_symptom_data():
    """Test that we can import the process_symptom_data module."""
    try:
        from health_tracker.process_symptom_data import process_health_data
        assert True
    except ImportError:
        assert False, "Could not import process_symptom_data module"


def test_sample_data_creation():
    """Test that we can create sample data."""
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
        from health_tracker.process_symptom_data import create_sample_data
        sample_df = create_sample_data()
        assert len(sample_df) == 3, "Sample data should have 3 rows"
        assert list(sample_df.columns) == ['Date', 'Symptom', 'Mobility', 'Notes'], "Sample data should have correct columns"
    except Exception as e:
        assert False, f"Could not create sample data: {e}"
#!/usr/bin/env python3
"""
Setup script for Text Analyzer project.
Downloads required NLTK data automatically.
"""

import nltk
import sys

def download_nltk_data():
    """Download required NLTK data packages."""
    required_packages = [
        'punkt',
        'averaged_perceptron_tagger'
    ]
    
    print("Downloading required NLTK data...")
    
    for package in required_packages:
        try:
            print(f"Downloading {package}...")
            nltk.download(package, quiet=True)
            print(f"✓ {package} downloaded successfully")
        except Exception as e:
            print(f"✗ Error downloading {package}: {e}")
            return False
    
    print("\n✓ All NLTK data downloaded successfully!")
    print("You can now run the text analyzer.")
    return True

if __name__ == "__main__":
    print("Text Analyzer Setup")
    print("===================")
    
    try:
        success = download_nltk_data()
        if success:
            print("\nSetup complete! You can now:")
            print("- Run 'jupyter notebook script.ipynb' to start the analysis")
            print("- Or import the modules in your own Python scripts")
        else:
            print("\nSetup failed. Please check your internet connection and try again.")
            sys.exit(1)
    except ImportError:
        print("Error: NLTK not found. Please install requirements first:")
        print("pip install -r requirements.txt")
        sys.exit(1) 
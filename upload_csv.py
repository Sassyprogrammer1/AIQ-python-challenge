# upload_csv.py

import os
from image_service import ImageService

def main():
    # Initialize the ImageService
    image_service = ImageService()
    # Get the current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # Relative path to the CSV file
    csv_file_relative_path = "csv_file.csv"
    # Construct the absolute path to the CSV file
    csv_file_path = os.path.join(current_dir, csv_file_relative_path)
    # Upload CSV data to MongoDB
    image_service.upload_csv_and_store_images(csv_file_path)

if __name__ == "__main__":
    main()

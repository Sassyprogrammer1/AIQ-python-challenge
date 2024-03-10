# service.py
from PIL import Image
from io import BytesIO
import io
import numpy as np
import pandas as pd
from connection import client

class ImageService:
    def __init__(self):
        self.client = client  # Get the MongoDB client instance
        self.db = self.client['mydb']

    def _read_csv(self, file_path):
        df = pd.read_csv(file_path, skiprows=1)  # Skip the first row (headers)
        data = [(row[0], list(row[1:])) for row in df.itertuples(index=False)]
        return data


    def _resize_and_store_image(self, depth, pixel_values):
        # Convert pixel values to image
        image = Image.new("L", (200, 1))
        image.putdata(pixel_values)
        
        # Resize image
        resized_image = image.resize((150, 1))
        print("Resized image dimensions:", resized_image.size)

        # Save resized image to CSV file
        # Store resized image in MongoDB
        with BytesIO() as output:
            resized_image.save(output, format='JPEG')
            image_data = output.getvalue()
            result = self.db.images.insert_one({"depth": depth, "image_data": image_data})
            print("result %s" % repr(result.inserted_id))

    def upload_csv_and_store_images(self, file_path):
        # Read CSV file
        csv_data = self._read_csv(file_path)
        # Resize and store images
        for depth, pixel_values in csv_data:
            self._resize_and_store_image(depth, pixel_values)

    def get_image_frames(self, depth_min, depth_max):
        frames = []
        result = self.db.images.find({'depth': {'$gte': depth_min, '$lte': depth_max}})
        for frame in result:
            image_data = frame['image_data']
            depth_value = frame['depth']
            # Assuming 'image_bytes' is your bytes object
            image = Image.open(io.BytesIO(image_data))
            frames.append({'depth': depth_value, 'image_data': image})
        return frames

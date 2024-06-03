import os  # Import the os module for interacting with the operating system
import requests  # Import the requests module for making HTTP requests

# Define the output directory where images will be saved
output_dir = "output"

# Create the output directory if it does not exist, if exists do not create
os.makedirs(output_dir, exist_ok=True)

# Open the file 'image_urls.txt' in read mode
with open('image_urls.txt', 'r') as file:
    # Iterate over each line in the file
    for i, line in enumerate(file, start=1):
        # Strip whitespace characters from the beginning and end of the line
        line_data = line.strip()

        # Check if the line is not empty
        if line_data:
            try:
                # Make an HTTP GET request to download the image content from the web
                img_bytes = requests.get(line_data).content

                # Define the base name for the image file; customize this as needed
                name = f"photo-{i}"

                # Create the full image file name with the .jpg extension
                img_name = f'{name}.jpg'

                # Create the full path for saving the image file
                full_path = os.path.join(output_dir, img_name)

                # Open the image file in write-binary mode and save the image content to your local disk
                with open(full_path, 'wb') as img_file:
                    img_file.write(img_bytes)
                    print(f'{img_name} was downloaded and saved in {output_dir}...')

            except Exception as e:
                print(f"Failed to download {line_data}: {e}")

print("All images have been processed.")



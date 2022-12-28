from PIL import Image
import argparse
import os

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='the input file')
parser.add_argument('output_file', help='the output file')
args = parser.parse_args()

# Check if the input file exists
if not os.path.exists(args.input_file):
  raise FileNotFoundError(f"File not found: {args.input_file}")

try:
    # Open the PNG image
    im = Image.open(args.input_file)

    # Convert the image to the RGB mode
    im = im.convert('RGB')

    # Save the image as a JPEG
    im.save(args.output_file, 'JPEG')
except Exception as e:
    print(f"[Error] str(e)")
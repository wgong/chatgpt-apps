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

# Get the output file extension
_, extension = os.path.splitext(args.output_file)

# Convert the extension to upper case
output_img_fmt = extension.upper()[1:]

SUPPORTED_IMG_FMT = ('GIF', 'JPEG', 'PNG')
# Check if the extension is supported
if output_img_fmt not in SUPPORTED_IMG_FMT:
  raise ValueError(f"Supported output formats are {SUPPORTED_IMG_FMT} \nbut you specified {extension}")

try:
    # Open the PNG image
    im = Image.open(args.input_file)

    # Save the image as a JPEG
    im.save(args.output_file, output_img_fmt)
    
except Exception as e:
    print(f"[Error] str(e)")
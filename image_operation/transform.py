import cv2
from pathlib import Path

def png_to_jpg(input_path, output_path):
    assert Path(input_path).suffix == ".png" and Path(input_path).is_file(), \
        "Please make sure the input file is png and exists."
    assert Path(output_path).suffix == ".jpg"
    image_array = cv2.imread(input_path)
    cv2.imwrite(output_path, image_array, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


import os 
import pydicom
import numpy as np

def normalize_dicom(pixel_array):
    """Convert raw high-bit DICOM pixel data to standard 8-bit grayscale."""
    img = pixel_array.astype(float)
    
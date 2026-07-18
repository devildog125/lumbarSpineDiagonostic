import os
import pydicom
import numpy as np
import cv2
import pandas as pd

def normalize_dicom(pixel_array):
    """Convert raw high-bit DICOM pixel data to standard 8-bit grayscale."""
    img = pixel_array.astype(float)
    # Min-max normalization to handle varying scanner contrast windows
    img = (img - np.min(img)) / (np.max(img) - np.min(img)) * 255.0
    img = np.uint8(img)
    
    # Apply CLAHE to sharpen bone/soft tissue boundaries for the vision model
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    return clahe.apply(img)

def crop_roi(image, x, y, crop_size=128):
    """Crop a bounding box around the target coordinates for localized analysis."""
    h, w = image.shape
    
    # Calculate crop boundaries while staying within image edges
    x_min = max(0, int(x - crop_size // 2))
    y_min = max(0, int(y - crop_size // 2))
    x_max = min(w, int(x + crop_size // 2))
    y_max = min(h, int(y + crop_size // 2))
    
    return image[y_min:y_max, x_min:x_max]

def process_pipeline(csv_path, dicom_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(csv_path)
    
    print(f"Parsing {len(df)} coordinate points...")
    for idx, row in df.iterrows():
        # Build path to the specific MRI slice
        # Kaggle structure usually matches: study_id / series_id / instance_number.dcm
        dicom_path = os.path.join(dicom_dir, str(row['study_id']), str(row['series_id']), f"{int(row['instance_number'])}.dcm")
        
        if not os.path.exists(dicom_path):
            continue
            
        # Read and extract raw image frame
        ds = pydicom.dcmread(dicom_path)
        normalized_img = normalize_dicom(ds.pixel_array)
        
        # Pull coordinates
        x, y = row['x'], row['y']
        condition = row['condition'].replace(" ", "_").lower()
        level = row['level'].replace("/", "_").lower()
        
        # Generate target filename
        filename = f"{row['study_id']}_{row['series_id']}_{level}_{condition}.jpg"
        
        # For YOLO training: Save the full processed frame
        cv2.imwrite(os.path.join(output_dir, "full_" + filename), normalized_img)
        
        # For VLM validation: Save a direct crop of the pathology area
        cropped_img = crop_roi(normalized_img, x, y)
        cv2.imwrite(os.path.join(output_dir, "crop_" + filename), cropped_img)

if __name__ == "__main__":
    # Point these to your local data locations
    process_pipeline(
        csv_path="data/train_coordinates.csv",
        dicom_dir="data/raw_dicoms",
        output_dir="data/processed_images"
    )
    print("Data extraction complete.")
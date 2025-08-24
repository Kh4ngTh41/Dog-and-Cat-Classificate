# Requirements and Environment Setup

## My Folder Struct

- Submit: my final submit - you can evaluate 
- Training Process: my training process

## Required Libraries

- torch
- torchvision
- scikit-learn
- numpy
- matplotlib
- pillow

You can install all required libraries using pip:

```
pip install torch torchvision scikit-learn numpy matplotlib pillow
```

## Environment
- Python 3.8 or newer
- CUDA-enabled GPU recommended (optional)

# How to Run Final_Submit.ipynb

## 1. Manual Test
- Step 1: Load and display an image in the notebook (see the cell with `plt.imshow(img)`)
- Step 2: Use the prediction function to classify the image (see the cell with `predict_image(img_path, ...)`)

## 2. Automatic Test
- Step 1: Ensure the test images are in `YourPrivateTestSetPath/` with subfolders `Cat` and `Dog`
- Step 2: Run the cell that loads `test_loader` and `test_dataset`
- Step 3: Run the cell that evaluates the model and prints confusion matrix, precision, and recall

## Notes
- The model weights file `best_model.pth` must be present in the workspace
- The code will automatically use GPU if available, otherwise CPU
- All paths are relative to the workspace root

# Troubleshooting
- If you get missing library errors, install them using pip as above
- If you get CUDA errors, set device to CPU by changing `torch.device("cuda" if torch.cuda.is_available() else "cpu")`

# File Structure
- Final_Submit.ipynb: Main notebook for evaluation
- best_model.pth: Trained model weights
- PetImages_split/: Dataset folder

# Contact
Contact me if you need assist

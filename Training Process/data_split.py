import os
import shutil
import random

# Data Path
data_dir = "PetImages"
output_dir = "PetImages_split"

# Split ratio
train_ratio = 0.7
val_ratio   = 0.15  # test_ratio = 0.15 

# Tạo thư mục output
for split in ["train", "val", "test"]:
    for cls in ["Cat", "Dog"]:
        os.makedirs(os.path.join(output_dir, split, cls), exist_ok=True)

# Split data
def split_data(class_name):
    src_dir = os.path.join(data_dir, class_name)
    images = os.listdir(src_dir)
    random.shuffle(images)

    n_total = len(images)
    n_train = int(n_total * train_ratio)
    n_val   = int(n_total * val_ratio)

    train_files = images[:n_train]
    val_files   = images[n_train:n_train+n_val]
    test_files  = images[n_train+n_val:]

    # Copy images to new folder
    for f in train_files:
        shutil.copy(os.path.join(src_dir, f), os.path.join(output_dir, "train", class_name, f))
    for f in val_files:
        shutil.copy(os.path.join(src_dir, f), os.path.join(output_dir, "val", class_name, f))
    for f in test_files:
        shutil.copy(os.path.join(src_dir, f), os.path.join(output_dir, "test", class_name, f))

# Cat and Dog split
split_data("Cat")
split_data("Dog")

print("Done! Dataset:", output_dir)

import os
import shutil
import random

# Đường dẫn dataset gốc
data_dir = "PetImages"
output_dir = "PetImages_split"

# Tỉ lệ chia
train_ratio = 0.7
val_ratio   = 0.15  # test_ratio = 0.15 còn lại

# Tạo thư mục output
for split in ["train", "val", "test"]:
    for cls in ["Cat", "Dog"]:
        os.makedirs(os.path.join(output_dir, split, cls), exist_ok=True)

# Hàm chia dữ liệu
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

    # Copy ảnh vào thư mục mới
    for f in train_files:
        shutil.copy(os.path.join(src_dir, f), os.path.join(output_dir, "train", class_name, f))
    for f in val_files:
        shutil.copy(os.path.join(src_dir, f), os.path.join(output_dir, "val", class_name, f))
    for f in test_files:
        shutil.copy(os.path.join(src_dir, f), os.path.join(output_dir, "test", class_name, f))

# Chia cho cat và dog
split_data("Cat")
split_data("Dog")

print("Done! Dataset đã được chia vào thư mục:", output_dir)

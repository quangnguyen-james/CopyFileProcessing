import os
import random
import shutil

# Thực hiện chuyển 1 số hình ảnh từ thư mục con của root_folder sang thư mục con tương ứng của destination_folder

# Đường dẫn gốc
root_folder = r"D:\Chương trình thạc sĩ\HK2-Máy học nâng cao\Bài kiểm tra\Solution Double Check\German_Traffic_Sign_Mix\Train"
destination_folder = r"D:\Chương trình thạc sĩ\HK2-Máy học nâng cao\Bài kiểm tra\Solution Double Check\German_Traffic_Sign_Mix\Test"

imgNumber = 32

# Duyệt qua từng thư mục con trong Train
for subfolder in os.listdir(root_folder):
    train_subfolder = os.path.join(root_folder, subfolder)
    test_subfolder = os.path.join(destination_folder, subfolder)

    # Bỏ qua nếu không phải thư mục
    if not os.path.isdir(train_subfolder):
        continue

    # Tạo thư mục Test tương ứng nếu chưa tồn tại
    os.makedirs(test_subfolder, exist_ok=True)

    # Lấy danh sách ảnh và chọn ngẫu nhiên imgNumber ảnh
    all_images = [f for f in os.listdir(train_subfolder) if os.path.isfile(os.path.join(train_subfolder, f))]
    selected_images = random.sample(all_images, imgNumber)

    # Di chuyển từng ảnh sang thư mục Test tương ứng
    for image in selected_images:
        src_path = os.path.join(train_subfolder, image)
        dst_path = os.path.join(test_subfolder, image)
        shutil.move(src_path, dst_path)  # move = copy + delete

print("Đã hoàn tất việc move ảnh từ mỗi thư mục ROOT sang DESTINATION.")

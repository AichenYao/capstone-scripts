import shutil, random, os

# Images_of_Waste/rawimgs/AluCan: 560 -> 56
# Images_of_Waste/rawimgs/Glass: 732 -> 73
# Images_of_Waste/rawimgs/HDPEM: 528 -> 53
# Images_of_Waste/rawimgs/PET: 1008 -> 100
# AluCan's original dataset has 560 images in total, picking ~10% for test and validation separately
# Delete the selected images from the train dataset

src_path = 'Images_of_Waste/rawimgs/'
subdirs_lst = ['AluCan', 'Glass', 'HDPEM', 'PET']
subdirs_num_lst = [56, 73, 53, 100]
test_path = 'Test/rawimgs'
val_path = 'Val/rawimgs'
# number of files in test and validation datasets

jpg_suffix = ".jpg"
txt_suffix = ".txt"
ALUCAN = "AluCan"
GLASS = "Glass"
HDPEM = "HDPEM"
PET = "PET"
IMAGES_DIR = "images/"
TEST_DIR = "test/"
TRAIN_DIR = "train/"
VAL_DIR = "validation/"
LABELS_DIR = "labels/"
ALUCAN_DIR = "AluCan/"
GLASS_DIR = "Glass/"
HDPEM_DIR = "HDPEM/"
PET_DIR = "PET/"

# for dir_name in [ALUCAN, GLASS, HDPEM, PET]:
#     os.mkdir("labels/test/" + dir_name)
    # os.mkdir("labels/train/" + dir_name)
    # os.mkdir("labels/validation/" + dir_name)

# move labels files (.txt) according to the images folder 
for file in os.listdir("YOLO_imgs/"):
    if (file.endswith(".txt")):
        txt_name = file
        orig_name = file[0:file.index('.')]
        jpg_name = orig_name + jpg_suffix
        if orig_name.startswith(ALUCAN):
            # if (os.path.exists(IMAGES_DIR + TEST_DIR + ALUCAN_DIR +  jpg_name)):
            #     shutil.copyfile("YOLO_imgs/" + txt_name, 
            #     LABELS_DIR + TEST_DIR + ALUCAN_DIR + txt_name)
            if (os.path.exists(IMAGES_DIR + VAL_DIR + ALUCAN_DIR +  jpg_name)):
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + VAL_DIR + ALUCAN_DIR + txt_name)
            else:
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + TRAIN_DIR + ALUCAN_DIR + txt_name)

        elif orig_name.startswith(GLASS):
            # if (os.path.exists(IMAGES_DIR + TEST_DIR + GLASS_DIR +  jpg_name)):
            #     shutil.copyfile("YOLO_imgs/" + txt_name, 
            #     LABELS_DIR + TEST_DIR + GLASS_DIR + txt_name)
            if (os.path.exists(IMAGES_DIR + VAL_DIR + GLASS_DIR +  jpg_name)):
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + VAL_DIR + GLASS_DIR + txt_name)
            else:
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + TRAIN_DIR + GLASS_DIR + txt_name)

        elif orig_name.startswith(HDPEM):
            # if (os.path.exists(IMAGES_DIR + TEST_DIR + HDPEM_DIR +  jpg_name)):
            #     shutil.copyfile("YOLO_imgs/" + txt_name, 
            #     LABELS_DIR + TEST_DIR + HDPEM_DIR + txt_name)
            if (os.path.exists(IMAGES_DIR + VAL_DIR + HDPEM_DIR +  jpg_name)):
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + VAL_DIR + HDPEM_DIR + txt_name)
            else:
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + TRAIN_DIR + HDPEM_DIR + txt_name)

        elif orig_name.startswith(PET):
            # if (os.path.exists(IMAGES_DIR + TEST_DIR + PET_DIR +  jpg_name)):
            #     shutil.copyfile("YOLO_imgs/" + txt_name, 
            #     LABELS_DIR + TEST_DIR + PET_DIR + txt_name)
            if (os.path.exists(IMAGES_DIR + VAL_DIR + PET_DIR +  jpg_name)):
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + VAL_DIR + PET_DIR + txt_name)
            else:
                shutil.copyfile("YOLO_imgs/" + txt_name, 
                LABELS_DIR + TRAIN_DIR + PET_DIR + txt_name)


# # select files for test dataset
# for i in range(len(subdirs_lst)):
#     subdir = subdirs_lst[i]
#     subdir_num = subdirs_num_lst[i]
#     tmp_src = os.path.join(src_path, subdir)
#     tmp_dest = os.path.join(test_path, subdir)
#     count = 0
#     if (not os.path.exists(tmp_dest)): os.mkdir(tmp_dest)
#     filenames = random.sample(os.listdir(tmp_src), subdir_num)
#     for fname in filenames:
#         src_file = os.path.join(tmp_src, fname)
#         dest_file = os.path.join(tmp_dest, fname)
#         shutil.copyfile(src_file, dest_file)
#         os.remove(src_file) # remove the selected file from the train dataset

# # select files for validation dataset
# for i in range(len(subdirs_lst)):
#     subdir = subdirs_lst[i]
#     subdir_num = subdirs_num_lst[i]
#     tmp_src = os.path.join(src_path, subdir)
#     tmp_dest = os.path.join(val_path, subdir)
#     count = 0
#     if (not os.path.exists(tmp_dest)): os.mkdir(tmp_dest)
#     filenames = random.sample(os.listdir(tmp_src), subdir_num)
#     for fname in filenames:
#         src_file = os.path.join(tmp_src, fname)
#         dest_file = os.path.join(tmp_dest, fname)
#         shutil.copyfile(src_file, dest_file)
#         os.remove(src_file) # remove the selected file from the train dataset


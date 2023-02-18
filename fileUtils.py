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
test_num = 500
val_num = 500


# select files for test dataset
for i in range(len(subdirs_lst)):
    subdir = subdirs_lst[i]
    subdir_num = subdirs_num_lst[i]
    tmp_src = os.path.join(src_path, subdir)
    tmp_dest = os.path.join(test_path, subdir)
    count = 0
    if (not os.path.exists(tmp_dest)): os.mkdir(tmp_dest)
    filenames = random.sample(os.listdir(tmp_src), subdir_num)
    for fname in filenames:
        src_file = os.path.join(tmp_src, fname)
        dest_file = os.path.join(tmp_dest, fname)
        shutil.copyfile(src_file, dest_file)
        os.remove(src_file) # remove the selected file from the train dataset

# select files for validation dataset
for i in range(len(subdirs_lst)):
    subdir = subdirs_lst[i]
    subdir_num = subdirs_num_lst[i]
    tmp_src = os.path.join(src_path, subdir)
    tmp_dest = os.path.join(val_path, subdir)
    count = 0
    if (not os.path.exists(tmp_dest)): os.mkdir(tmp_dest)
    filenames = random.sample(os.listdir(tmp_src), subdir_num)
    for fname in filenames:
        src_file = os.path.join(tmp_src, fname)
        dest_file = os.path.join(tmp_dest, fname)
        shutil.copyfile(src_file, dest_file)
        os.remove(src_file) # remove the selected file from the train dataset

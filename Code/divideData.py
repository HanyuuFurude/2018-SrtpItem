import shutil
import os

train_number = 15
validation_number = 1
test_number = 1
original_dataset_dir = "C:\\Users\\28172\\Desktop\\Srtp\\Code\\unet\\data\\brain\\IBSR18_Data"
train_dir = os.path.join(original_dataset_dir,'train')
os.mkdir(train_dir)
validation_dir = os.path.join(original_dataset_dir,'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(original_dataset_dir,'test')
os.mkdir(test_dir)

#把前面文件的path记录一下
undivide_dataset_dir = []
for i in range(2,19):
    undivide_dataset_dir.append(os.path.join(original_dataset_dir,'IBSR_{}'.format(i)))
imagenames = ['{}.jpg'.format(i) for i in range(0,256)]
truthnames = ['truth{}.jpg'.format(i) for i in range(0,256)]

for i in range(0,15):
    for j in range(0,256):
        src_image = os.path.join(undivide_dataset_dir[i],imagenames[j])
        src_truth = os.path.join(undivide_dataset_dir[i],truthnames[j])
        dst_image_name = str(i)+'_'+imagenames[j]
        dst_truth_name = str(i)+'_'+truthnames[j]
        dst_image = os.path.join(train_dir,dst_image_name)
        dst_truth = os.path.join(train_dir,dst_truth_name)
        shutil.copy(src_image,dst_image)
        shutil.copy(src_truth,dst_truth)
for j in range(0,256):
    src_image = os.path.join(undivide_dataset_dir[15],imagenames[j])
    src_truth = os.path.join(undivide_dataset_dir[15],truthnames[j])
    dst_image = os.path.join(validation_dir,imagenames[j])
    dst_truth = os.path.join(validation_dir,truthnames[j])
    shutil.copy(src_image,dst_image)
    shutil.copy(src_truth,dst_truth)
for j in range(0,256):
    src_image = os.path.join(undivide_dataset_dir[16],imagenames[j])
    src_truth = os.path.join(undivide_dataset_dir[16],truthnames[j])
    dst_image = os.path.join(test_dir,imagenames[j])
    dst_truth = os.path.join(test_dir,truthnames[j])
    shutil.copy(src_image,dst_image)
    shutil.copy(src_truth,dst_truth)
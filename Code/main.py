from model import *
from data import *
import nibabel as nib
import matplotlib.pyplot as plt

#os.environ["CUDA_VISIBLE_DEVICES"] = "0"
train_number = 15
validation_number = 1
test_number = 1
original_dataset_dir = "data\\brain\\IBSR18_Data"
train_dir = os.path.join(original_dataset_dir,'train')
validation_dir = os.path.join(original_dataset_dir,'validation')
test_dir = os.path.join(original_dataset_dir,'test')
undivide_dataset_dir = []



model = unet()
train_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')

train_generator= trainGenerator(8,train_dir,'image','truth',train_gen_args,save_to_dir = None)
validation_generator = testGenerator(8,validation_dir,'image','truth',save_to_dir = None)
# 看一下生成，因为后面没有shape属性，没看懂
for data_batch, labels_batch in train_generator:
    print('data batch shape' , data_batch.shape)
    print('labels batch shape:', labels_batch.shape)
    break
#每个epoch 训练数量 = 所有数据数量 = step_per_epoch * batch_size
#model_checkpoint = ModelCheckpoint('unet_membrane.hdf5', monitor='loss',verbose=1, save_best_only=True)
history = model.fit_generator(train_generator,steps_per_epoch = 320, epochs = 10, validation_data = validation_generator, validation_steps = 32)
model.save("third_fit.h5")

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1,len(acc)+1)

plt.plot(epochs,acc, 'r', label = 'Training acc')
plt.plot(epochs,val_acc, 'b',label ='Validation acc')
plt.title('Training and validation accuracy')

plt.figure()

plt.plot(epochs,loss, 'r', label = 'Training loss')
plt.plot(epochs,val_loss, 'b',label ='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
'''
results = model.predict_generator(testGene,30,verbose=1)
saveResult("data/membrane/test",results)
'''
'''
path = "E:/Oanakiaja/Srtp/Code/unet/data/niiBrain/train/image/0.nii"
brain_img = nib.load(path).get_data()
print('brain_img.shape: ', brain_img.shape)
print('type', type(brain_img))
print(brain_img)
'''
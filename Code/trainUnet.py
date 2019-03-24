#!/usr/bin/env python
# coding: utf-8

# In[1]:


from model import *
from data import *


# ## Train your Unet with membrane data
# membrane data is in folder membrane/, it is a binary classification task.
#
# The input shape of image and mask are the same :(batch_size,rows,cols,channel = 1)

# ### Train with data generator

# In[3]:

#训练数据增强
data_gen_args = dict(rotation_range=0.2,              #旋转角度值0~180
                    width_shift_range=0.05,           #水平方向向上平移
                    height_shift_range=0.05,          #高度方向向上平移
                    shear_range=0.05,                 #随机错切变换的角度(图片错位)
                    zoom_range=0.05,                  #图像随机缩放的范围
                    horizontal_flip=True,             #随机将一半图像水平翻转
                    fill_mode='nearest')              #新像素由附近像素补充
myGene = trainGenerator(2,'data/membrane/train','image','label',data_gen_args,save_to_dir = None) #批次，训练根目录，图像，标签，字典参数，数据增强后的位置

#unet()初始化
model = unet()

#读取已经训练好的权重
model_checkpoint = ModelCheckpoint('unet_membrane.hdf5', monitor='loss',verbose=1, save_best_only=True)
#利用数据增强生成器训练卷积，（如果我们不用数据增强的话就直接model.fit()，主要这样利用了内存里面的myGene,callbacks。？)
model.fit_generator(myGene,steps_per_epoch=2000,epochs=5,callbacks=[model_checkpoint])


# ### Train with npy file

# In[ ]:


#imgs_train,imgs_mask_train = geneTrainNpy("data/membrane/train/aug/","data/membrane/train/aug/")
#model.fit(imgs_train, imgs_mask_train, batch_size=2, nb_epoch=10, verbose=1,validation_split=0.2, shuffle=True, callbacks=[model_checkpoint])


# ### test your model and save predicted results

# In[ ]:

#不能增强验证集，这里应该做归一化处理
testGene = testGenerator("data/membrane/test")
model = unet()
#加载权重
model.load_weights("unet_membrane.hdf5")
#评估模型
results = model.predict_generator(testGene,30,verbose=1)
#save 啥？
saveResult("data/membrane/test",results)


# import nibabel as nib
# import numpy as np
# # nii读取
# brain_img = nib.load(nii_dir).get_data()


# # nii保存
# affine = nib.load(nii_dir).affine  # 对应的nii图像的affine
# save_nii = nib.Nifti1Image(save_img, affine)
# nib.save(save_nii, save_dir)

# def dice_similarity_coef(pred, label, argmax=True, num_classes=4):
#     if argmax:
#         pred = np.argmax(pred, axis=-1)
#         label = np.argmax(label, axis=-1)
#     shape = np.shape(pred)

#     pred_o = np.reshape(pred, [shape[0], shape[1] * shape[2]])
#     label_o = np.reshape(label, [shape[0], shape[1] * shape[2]])

#     dscs = []
#     for i in range(1, num_classes):
#         seg = copy.copy(pred_o)
#         gt = copy.copy(label_o)
#         seg[seg != i] = 0
#         gt[gt != i] = 0
#         seg[seg == i] = 1
#         gt[gt == i] = 1

#         insection = sum(np.sum(seg * gt, axis=-1))
#         sum1 = sum(np.sum(seg, axis=-1) + np.sum(gt, axis=-1))
#         dsc_i = 2 * insection / sum1
#         dscs.append(dsc_i)
#     return dscs


# def absolute_volume_difference(pred, label, num_classes=4):
#     avds = []
#     for i in range(1, num_classes):
#         count_i = np.sum(pred == i)
#         length_i = np.sum(label == i)
#         avds.append(abs(count_i - length_i) / length_i)
#     return avds

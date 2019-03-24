import nibabel as nib
import os
import re
brain = []
truth = []
for folder,subsolders,files in os.walk('.\\'):
    for f in files:
        if re.search('(.*).nii$', f):
            if re.search('brain', f):
                brain.append(nib.load(os.path.join(folder, f)))
            elif re.search('truth', f):
                truth.append(nib.load(os.path.join(folder, f)))
            else:
                print('uncongrized!')


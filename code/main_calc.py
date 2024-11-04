
import numpy as np
import math
from glob import glob
import natsort
import scipy.misc
from psnr import PSNR


input_files = glob('../data/input/*.png')

input_files = natsort.natsorted(input_files)

denoised_files = glob('../data/denoised/*.png')
denoised_files = natsort.natsorted(denoised_files)

target_files = glob('../data/target/*.png')
target_files = natsort.natsorted(target_files)

file_num = len(input_files)

for i in range(file_num):
    input_img = scipy.misc.imread(input_files[i], flatten=True).astype(np.float32)
    denoised_img = scipy.misc.imread(denoised_files[i], flatten=True).astype(np.float32)
    target_img = scipy.misc.imread(target_files[i], flatten=True).astype(np.float32)

    psnr_input_and_target = PSNR(input_img, target_img).cal_psnr()
    psnr_denoised_and_target = PSNR(denoised_img, target_img).cal_psnr()




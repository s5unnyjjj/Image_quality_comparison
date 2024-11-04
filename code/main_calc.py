
import numpy as np
from glob import glob
import natsort
import scipy.misc
from psnr import PSNR
from ssim import SSIM
from vifp import VIFP

input_files = glob('../data/input/*.png')
input_files = natsort.natsorted(input_files)

denoised_files = glob('../data/pred/*.png')
denoised_files = natsort.natsorted(denoised_files)

target_files = glob('../data/target/*.png')
target_files = natsort.natsorted(target_files)

file_num = len(input_files)

psnr_all = []
ssim_all = []
vif_all = []
for i in range(file_num):
    input_img = scipy.misc.imread(input_files[i], flatten=True).astype(np.float32)
    denoised_img = scipy.misc.imread(denoised_files[i], flatten=True).astype(np.float32)
    target_img = scipy.misc.imread(target_files[i], flatten=True).astype(np.float32)

    psnr_input_and_target = PSNR(input_img, target_img).cal_psnr()
    psnr_denoised_and_target = PSNR(denoised_img, target_img).cal_psnr()

    ssim_input_and_target = SSIM(input_img, target_img).cal_ssim()
    ssim_denoised_and_target = SSIM(denoised_img, target_img).cal_ssim()

    vifp_input_and_target = VIFP(input_img, target_img).cal_vifp()
    vifp_denoised_and_target = VIFP(denoised_img, target_img).cal_vifp()

    print('\n******* Dataset # %d *******' %(i+1))
    print('### Image quality comparison between input image and target image')
    print(' - psnr: %.5f\n - ssim: %.5f\n - vif: %.5f\n' %(psnr_input_and_target, ssim_input_and_target, vifp_input_and_target))

    print('### Image quality comparison between denoised image and target image')
    print(' - psnr: %.5f\n - ssim: %.5f\n - vif: %.5f' %(psnr_denoised_and_target, ssim_denoised_and_target, vifp_denoised_and_target))
    print('****************************************************************')

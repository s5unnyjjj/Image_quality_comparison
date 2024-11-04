
import numpy as np
from scipy.ndimage import gaussian_filter

class SSIM:
    def __init__(self, img1, img2, param_c1=0.01**2, param_c2=0.03**2, param_sigma=1.5):
        self.img1 = img1
        self.img2 = img2
        self.param_c1 = param_c1
        self.param_c2 = param_c2

        self.param_sigma = param_sigma

    def cal_ssim(self):
        img1_gf = gaussian_filter(input=self.img1, sigma=self.param_sigma)
        img2_gf = gaussian_filter(input=self.img2, sigma=self.param_sigma)

        img1_mul = img1_gf * img1_gf
        img2_mul = img2_gf * img2_gf
        img1_img2_mul = img1_gf * img2_gf

        img1_gf = gaussian_filter(input=self.img1*self.img1, sigma=self.param_sigma) - img1_mul
        img2_gf = gaussian_filter(input=self.img2 * self.img2, sigma=self.param_sigma) - img2_mul
        img1_img2_gf = gaussian_filter(input=self.img1 * self.img2, sigma=self.param_sigma) - img1_img2_mul

        ssim1 = ((2 * img1_img2_mul + self.param_c1) * (2 * img1_img2_gf + self.param_c2))

        ssim2 = ((img1_mul + img2_mul + self.param_c1) * (img1_gf + img2_gf + self.param_c2))

        ssim = ssim1 / ssim2
        return np.mean(ssim)

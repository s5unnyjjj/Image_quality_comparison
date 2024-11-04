import numpy as np
from scipy.ndimage import gaussian_filter

class VIFP:
    def __init__(self, img1, img2, param_sigma1=2, param_eps = 1e-10):
        self.img1 = img1
        self.img2 = img2
        self.param_sigma1 = param_sigma1
        self.param_eps = param_eps

    def cal_vifp(self):
        num = 0.0
        den = 0.0

        for scale in range(1, 5):
            sigma = (2 ** (4 - scale + 1) + 1) / 5.0

            if (scale > 1):
                self.img1 = gaussian_filter(input=self.img1, sigma=sigma)[::2, ::2]
                self.img2 = gaussian_filter(input=self.img2, sigma=sigma)[::2, ::2]

            img1_gf = gaussian_filter(input=self.img1, sigma=sigma)
            img2_gf = gaussian_filter(input=self.img2, sigma=sigma)

            img1_mul = img1_gf * img1_gf
            img2_mul = img2_gf * img2_gf
            img1_img2_mul = img1_gf * img2_gf

            img1_gf = gaussian_filter(input=self.img1 * self.img1, sigma=sigma) - img1_mul
            img2_gf = gaussian_filter(input=self.img2 * self.img2, sigma=sigma) - img2_mul
            img1_img2_gf = gaussian_filter(input=self.img1 * self.img2, sigma=sigma) - img1_img2_mul

            img1_gf[img1_gf < 0] = 0
            img2_gf[img2_gf < 0] = 0

            g = img1_img2_gf / (img1_gf + self.param_eps)
            sv_sq = img2_gf - g * img1_img2_gf

            g[img1_gf < self.param_eps] = 0
            sv_sq[img1_gf < self.param_eps] = img2_gf[img1_gf < self.param_eps]
            img1_gf[img1_gf < self.param_eps] = 0

            g[img2_gf < self.param_eps] = 0
            sv_sq[img2_gf < self.param_eps] = 0

            sv_sq[g < 0] = img2_gf[g < 0]
            g[g < 0] = 0
            sv_sq[sv_sq <= self.param_eps] = self.param_eps

            num += np.sum(np.log10(1 + g * g * img1_gf / (sv_sq + self.param_sigma1)))
            den += np.sum(np.log10(1 + img1_gf / self.param_sigma1))

        vifp = num / den

        if np.isnan(vifp):
            return 1.0
        else:
            return vifp
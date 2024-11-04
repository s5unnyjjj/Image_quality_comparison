

import numpy as np
import math

class PSNR:
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2
        self.max_pixel = 255.0

    def cal_psnr(self):
        mse = np.mean((self.img1 - self.img2) ** 2)
        if mse == 0:
            return 100

        return 20 * math.log10(self.max_pixel / math.sqrt(mse))

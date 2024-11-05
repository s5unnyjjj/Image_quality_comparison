import numpy as np
import cv2
import phasepack.phasecong as pc

class FSIM:
    def __init__(self, img1, img2, param_t1=0.85, param_t2 = 160):
        self.img1 = cv2.imread(img1)
        self.img2 = cv2.imread(img2)
        self.param_t1 = param_t1
        self.param_t2 = param_t2
        self.param_alpha = 1
        self.param_beta = 1


    def cal_fsim(self):
        fsim_list = []
        for i in range(self.img1.shape[2]):
            # Calculate the PC for original and predicted images
            pc1_2dim = pc(self.img1[:, :, i], nscale=4, minWaveLength=6, mult=2, sigmaOnf=0.5978)
            pc2_2dim = pc(self.img2[:, :, i], nscale=4, minWaveLength=6, mult=2, sigmaOnf=0.5978)

            pc1_2dim_sum = np.zeros((self.img1.shape[0], self.img1.shape[1]), dtype=np.float64)
            pc2_2dim_sum = np.zeros((self.img2.shape[0], self.img2.shape[1]), dtype=np.float64)

            for orientation in range(6):
                pc1_2dim_sum += pc1_2dim[4][orientation]
                pc2_2dim_sum += pc2_2dim[4][orientation]

            img1_scharr_x = cv2.Scharr(self.img1[:, :, i], cv2.CV_16U, 1, 0)
            img1_scharr_y = cv2.Scharr(self.img1[:, :, i], cv2.CV_16U, 0, 1)
            img1_gradient_magnitude = np.sqrt(img1_scharr_x ** 2 + img1_scharr_y ** 2)

            img2_scharr_x = cv2.Scharr(self.img2[:, :, i], cv2.CV_16U, 1, 0)
            img2_scharr_y = cv2.Scharr(self.img2[:, :, i], cv2.CV_16U, 0, 1)
            img2_gradient_magnitude = np.sqrt(img2_scharr_x ** 2 + img2_scharr_y ** 2)

            pc_numerator = 2 * pc1_2dim_sum * pc2_2dim_sum + self.param_t1
            pc_denominator = pc1_2dim_sum ** 2 + pc2_2dim_sum ** 2 + self.param_t1
            pc_similarity_measure = pc_numerator / pc_denominator

            gm_numerator = 2 * img1_gradient_magnitude * img2_gradient_magnitude + self.param_t2
            gm_denominator = img1_gradient_magnitude ** 2 + img2_gradient_magnitude ** 2 + self.param_t2
            gm_similarity_measure = gm_numerator / gm_denominator

            final_similarity_measure = ((pc_similarity_measure ** self.param_alpha)
                                        * (gm_similarity_measure ** self.param_beta))

            numerator = np.sum(final_similarity_measure * np.maximum(pc1_2dim_sum, pc2_2dim_sum))
            denominator = np.sum(np.maximum(pc1_2dim_sum, pc2_2dim_sum))
            fsim_list.append(numerator / denominator)

        return np.mean(fsim_list)
# Image quality comparison </br>
Image quality comparison: psnr, ssim, vif, fsim
</br></br>

## Project Structure </br>
 * code/main_calc.py: Code to calculate with the image quality metrics
 * code/psnr.py: Code to calculate with the PSNR(Peak Signal-to-noise ratio)
 * code/ssim.py: Code to calculate with the SSIM(Structural similarity index measureo)
 * code/vifp.py: Code toe calculate with the VIF(Variance inflation factor)
</br>

## Dataset </br>
#### Dataset #1 </br>
|Input|Denoised|Target|
|:---:|:---:|:---:| 
|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/input/88.png" width="300" height="150">|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/pred/88.png" width="300" height="150">|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/target/88.png" width="300" height="150">|

#### Dataset #2 </br>
|Input|Denoised|Target|
|:---:|:---:|:---:| 
|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/input/89.png" width="300" height="150">|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/pred/89.png" width="300" height="150">|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/target/89.png" width="300" height="150">|

#### Dataset #3 </br>
|Input|Denoised|Target|
|:---:|:---:|:---:| 
|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/input/535.png" width="300" height="150">|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/pred/535.png" width="300" height="150">|<img src="https://github.com/s5unnyjjj/Image_quality_comparison/blob/master/data/target/535.png" width="300" height="150">|
</br>

## Results </br>
#### Image quality comparison between input image and target image </br>
||Dataset #1|Dataset #2|Dataset #3|
|:---:|:---:|:---:|:---:|
|PSNR|20.09831|23.90398|18.13228|
|SSIM|0.45760|0.77630|0.40929|
|VIFP|0.21355|0.32840|0.30385|
</br>

#### Image quality comparison between denoised image and target image </br>
||Dataset #1|Dataset #2|Dataset #3|
|:---:|:---:|:---:|:---:|
|PSNR|25.52061|27.02996|28.92660|
|SSIM|0.55099|0.81606|0.52800|
|VIFP|0.35648|0.41545|0.50229|


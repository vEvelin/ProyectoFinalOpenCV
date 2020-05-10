import cv2


class ImageSobelx:
    @classmethod
    def imag_to_sobelx(self,img):
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        return sobelx
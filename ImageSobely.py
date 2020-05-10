import cv2


class ImageSobely:
    @classmethod
    def imag_to_sobely(self,img):
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
        return sobely
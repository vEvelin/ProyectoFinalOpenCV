import cv2


class ImageLaplacian:
    @classmethod
    def imag_to_laplacian(self,img):
        laplacia = cv2.Laplacian(img, cv2.CV_64F)
        return laplacia
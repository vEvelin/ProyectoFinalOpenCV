import cv2


class ImageGray:

    @classmethod
    def img_to_gray_scale(self,img):
        """Recibe un objeto imagen y devuleve la imagen en blanco y negro"""
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img
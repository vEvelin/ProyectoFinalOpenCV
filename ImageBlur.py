import cv2


class ImageBlur:

    @classmethod
    def img_to_blur(self,img):
        blur_image = cv2.GaussianBlur(img, (5, 5), 0)
        return blur_image

import cv2


class ImageSize:


    @classmethod
    def img_change_size(self,img):

        size_img = cv2.resize(img,(int(220),int(100)))
        return size_img




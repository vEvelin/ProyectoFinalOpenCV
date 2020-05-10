
from ImageStorage import ImageStorage
from ImageGray import ImageGray
from ImageSize import ImageSize
from ImageDetection import ImageDetection
from ImageBlur import ImageBlur
from ImageLaplacian import ImageLaplacian
from ImageSobelx import ImageSobelx
from ImageSobely import ImageSobely


if __name__ == '__main__':
    # print(img.shape)
    img = ImageStorage.read_image("images/animas.jpg")
    img_gray = ImageGray.img_to_gray_scale(img)
    ImageStorage.save_img(img=img_gray,name_img="animasblack")
    print("<<<<<<<<<  La imagen se guardó exitosamente  >>>>>>>>>>>")
    img2 = ImageStorage.read_image("images/animas.jpg")
    img_size = ImageSize.img_change_size(img_gray)
    ImageStorage.save_img(img= img_size, name_img="animassize")
    print("<<<<<<<<<  La imagen se guardó exitosamente  >>>>>>>>>>>")
    img3 = ImageStorage.read_image("images/animas.jpg")
    img_detect = ImageDetection.detection(img)
    ImageStorage.save_img(img=img_detect, name_img="animadetect")
    print("<<<<<<<<<  La imagen se guardó exitosamente  >>>>>>>>>>>")
    img4 = ImageStorage.read_image("images/animas.jpg")
    img_blur = ImageBlur.img_to_blur(img)
    ImageStorage.save_img(img=img_blur, name_img="animablur")
    print("<<<<<<<<<  La imagen se guardó exitosamente  >>>>>>>>>>>")
    img5 = ImageStorage.read_image("images/animas.jpg")
    imag_laplac =ImageLaplacian.imag_to_laplacian(img)
    ImageStorage.save_img(img=imag_laplac, name_img="animalap")
    print("<<<<<<<<<  La imagen se guardó exitosamente  >>>>>>>>>>>")
    img6 = ImageStorage.read_image("images/animas.jpg")
    imag_sobelx = ImageSobelx.imag_to_sobelx(img)
    ImageStorage.save_img(img=imag_sobelx, name_img="animasobelx")
    print("<<<<<<<<<  La imagen se guardó exitosamente  >>>>>>>>>>>")
    img7 = ImageStorage.read_image("images/animas.jpg")
    imag_sobely = ImageSobely.imag_to_sobely(img)
    ImageStorage.save_img(img=imag_sobely, name_img="animasobely")
    print("<<<<<<<<<  La imagen se guardó exitosamente  >>>>>>>>>>>")



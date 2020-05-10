import numpy as np
import argparse
import glob
import cv2


class ImageDetection:
	@classmethod
	def valor_Inf(self):
		sigma = 0.30
		infe = int(max(0, (1.0 - sigma)))
		return infe

	@classmethod
	def valor_Sup(self):
		sigma = 0.30
		sup = int(min(255, (1.0 + sigma)))
		return sup

	@classmethod
	def detection(self,imag):
		sigma = 0.30
		mediana_intensidades_pixls = np.median(imag)
		inferior = self.valor_Inf() * (mediana_intensidades_pixls)
		superior = self.valor_Sup() * (mediana_intensidades_pixls)
		imag_detect = cv2.Canny(imag, inferior, superior)
		return imag_detect
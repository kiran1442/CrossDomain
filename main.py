import numpy as np
import cv2
from os.path import splitext, basename, join

class Colorizer:
    def __init__(self, height=480, width=640):
        (self.height, self.width) = height, width

        self.Colormodel = cv2.dnn.readNetFromCaffe('models/colorization_deploy_v2.prototxt',
                                              caffeModel='models/colorization_release_v2.caffemodel')
        
        culsterCenters = np.load('models/pts_in_hull.npy')
        culsterCenters = culsterCenters.transpose().reshape(2, 313, 1, 1)

        self.Colormodel.getLayer(self.Colormodel.getLayerId('class8_ab')).blobs = [culsterCenters.astype(np.float32)]
        self.Colormodel.getLayer(self.Colormodel.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]

    def processImage(self, imgName):
        self.img = cv2.imread(imgName)
        self.img = cv2.resize(self.img, (self.height, self.width))

        self.processFrame()
        cv2.imwrite(join("output", imgName), self.finalImg)
        cv2.imshow('Output', self.finalImg)
        cv2.waitKey(0)

    # colorize image
    def processFrame(self):
        imgNormalize = (self.img[:, :, [2,1,0]] * 1.0/255).astype(np.float32)

        imgLab = cv2.cvtColor(imgNormalize, cv2.COLOR_RGB2Lab)
        channelL = imgLab[:, :, 0]

        imgLabResized = cv2.cvtColor(cv2.resize(imgNormalize, (224, 224)), cv2.COLOR_RGB2Lab)
        channelResized = imgLabResized[:, :, 0]
        channelResized -= 50

        self.Colormodel.setInput(cv2.dnn.blobFromImage(channelResized))
        result = self.Colormodel.forward()[0,:,:,:].transpose((1,2,0))

        resultResized = cv2.resize(result, (self.height, self.width))

        self.imgOut = np.concatenate((channelL[:, :, np.newaxis], resultResized), axis = 2)
        self.imgOut = np.clip(cv2.cvtColor(self.imgOut, cv2.COLOR_LAB2BGR), 0, 1)
        self.imgOut = np.array((self.imgOut)*255, dtype=np.uint8)

        self.finalImg = np.hstack((self.img, self.imgOut))



        

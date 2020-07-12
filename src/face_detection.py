# coding: utf-8

import numpy as np
import sys
import cv2
import ssl
import os


class FaceDetection:

    def face_detection(self,imagepath,feature='haar',filename=None):
        project_dir = os.path.dirname(os.path.abspath(__file__))

        xml_file = 'hogcascades/hogcascade_pedestrians.xml'

        if filename is not None:
            xml_file = feature+'cascades/'+filename+'.xml'
        elif feature == 'hog':
            xml_file = 'hogcascades/hogcascade_pedestrians.xml'
        elif feature == 'lbp':
            xml_file = 'lbpcascades/lbpcascade_frontalface_improved.xml'
        elif feature == 'haar':
            xml_file = 'haarcascades/haarcascade_frontalface_default.xml'

        full_path =  '%s/data/%s' % (project_dir,xml_file)

        if os.path.isfile(full_path) == False:
            raise ValueError('Parameter value error')

        return self.do_count(imagepath,full_path)

    def do_count(self,imagepath,full_path):
        image = self.url_to_image(imagepath)

        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(full_path)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (30,30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        return faces


    def url_to_image(self,url):
        context = ssl._create_unverified_context()

        if sys.version_info[0] == 3:
            from urllib.request import urlopen
        else:
            from urllib import urlopen

        with urlopen(url,context=context) as url:
            s = url.read()

        image = np.asarray(bytearray(s), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image






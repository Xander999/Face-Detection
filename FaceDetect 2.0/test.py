import os
import cv2
import cv2.face
import numpy as np
from PIL import Image

recognizer=cv2.face.createLBPHFaceRecognizer()
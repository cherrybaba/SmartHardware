import time
import datetime
import spidev as SPI
import SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import numpy as np

RST = 19
DC = 16
bus = 0
device = 0
disp = SSD1306.SSD1306(rst=RST,dc=DC,spi=SPI.SpiDev(bus,device))
disp.begin()
disp.clear()
disp.display()

digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
  plt.subplot(2, 4, index + 1)
  plt.axis('off')
  plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
  plt.title('Training: %i' % label)
# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(C=1.0,gamma=0.01)
# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])
# Now predict the value of the digit on the second half:
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])
images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for kk,prediction in images_and_predictions:
    digit=Image.fromarray((kk*8).astype(np.uint8),mode='L').resize((48,48)).convert('1')
    img=Image.new('1',(disp.width,disp.height),'black')
    img.paste(digit,(0,16,digit.size[0],digit.size[1]+16))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((0,0),'Prediction: %i' % prediction,font=font,fill=255)
    disp.clear()
    disp.image(img)
    disp.display()
    time.sleep(1)
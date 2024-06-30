
import imageio.v3 as iio
import cv2
import os
images = [ ]
image_files=os.listdir('Input')
image_files=sorted(image_files)
for file in image_files:
    repo = os.path.join('Input/{}'.format(file))
    images.append(iio.imread(repo))
gif= iio.imwrite('team.gif', images, duration = 500, loop = 0)

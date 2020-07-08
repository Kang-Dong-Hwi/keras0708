import numpy as np
import PIL.Image
import os

PATH = 'C:/Projects/keras_talk/keras/handwriting_shape2/'
arr_PATH = 'C:/Projects/keras_talk/keras/handwriting_shape2_array'
file_list = os.listdir(PATH)



x_train = []
y_train = []

x_test = []
y_test = []

Shape_dict = {'c':0, 'r':1, 't':2}
for png in file_list:
    
    image = PIL.Image.open(PATH + png)
    image = image.convert('L')
    Shape = png[0]
    Num = int( png[-6:-4] )

    pixel = np.array(image).reshape(24,24)
        
    if Num <= 15:
        x_train.append( pixel )
        y_train.append( Shape_dict[Shape] )
    else:
        x_test.append(pixel)
        y_test.append( Shape_dict[Shape] )


np.save(arr_PATH+'/x_train.npy', np.array(x_train))
np.save(arr_PATH+'/y_train.npy', np.array(y_train))
np.save(arr_PATH+'/x_test.npy', np.array(x_test))
np.save(arr_PATH+'/y_test.npy', np.array(y_test))
print('t')

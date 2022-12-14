# ๐ฆ TIL

[TF CNN ๊ณต์ ๋ฌธ์](https://www.tensorflow.org/tutorials/images/cnn) <br>
[์์ด์ฐ ์ถ์ฒ ์๋ฃ](https://untitledtblog.tistory.com/150)

## โ Convolutional Neural Network, CNN
### - ํฉ์ฑ๊ณฑ ์ธต ๋ง๋ค๊ธฐ

* CNN์ ๋ฐฐ์น(batch) ํฌ๊ธฐ๋ฅผ ์ ์ธํ๊ณ  `(์ด๋ฏธ์ง ๋์ด, ์ด๋ฏธ์ง ๋๋น, ์ปฌ๋ฌ ์ฑ๋)` ํฌ๊ธฐ์ ํ์(tensor)๋ฅผ ์๋ ฅ
* ๋ณดํต ์ปฌ๋ฌ ์ด๋ฏธ์ง๋ ์ปฌ๋ฌ ์ฑ๋์ด 3 == R, G, B
* ํ๋ฐฑ ์ด๋ฏธ์ง๋ 1

```python
model = models.Sequential()

# Convolution layer, input_shape = (๋์ด, ๋๋น, ์ฑ๋)
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), 
                        activation='relu', input_shape=(32, 32, 3)))

# Max Pooling ์ฐ์ฐ์ ์ํํ๋ layer
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))

# 3D ์ถ๋ ฅ์ 1D๋ก ํผ์นจ
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

# 10๊ฐ์ ํด๋์ค
model.add(layers.Dense(10))
```
* `filters`
  * ํํฐ์ ๊ฐ์
* `kernel_size`
  * ์ปค๋์ ํฌ๊ธฐ๊ฐ ์์์๋ก ๋ ์ด์ด ํฌ๊ธฐ๊ฐ ๋ ์์์ง๋ฏ๋ก ๋ ๊น์ ์ํคํ์ฒ ๊ฐ๋ฅ
  * ํฐ ํฌ๊ธฐ์ ์ปค๋์ ๋ ์ ์ ์ ๋ถ ์ถ์ถ โก๏ธ ์ฐจ์์ด ๋ ๋นจ๋ฆฌ ์ค์ด๋ค๊ณ  ๊ณผ์์ ํฉ ๊ฐ๋ฅ์ฑ
  * ๋ณดํต ํ ์๋ก ์ฌ์ฉํ๋ ํธ
* `pool_size`
  * pooling ์ฐ์ฐ์ ์ํ ์ปค๋ ํฌ๊ธฐ

<br>

### - Padding
[CNN explainer](https://poloclub.github.io/cnn-explainer/)

![](../../img/padding.png)

* padding ์ ์ญํ 
  * ์ด๋ฏธ์ง๊ฐ ์ค์ด๋๋ ๊ฒ์ ๋ฐฉ์ง
  * ๊ฐ์ฅ์๋ฆฌ ๋ถ๋ถ์ ํน์ง์ ์ข ๋ ํ์ตํ๊ธฐ ์ํด
* `padding = 1`, `kernel_size = 3` ์ ๋ง์ด ์ฌ์ฉ โก๏ธ ์ด๋ฏธ์ง๊ฐ ์ค์ด๋ค์ง ์์

<br>

### - ํผ์ฒ๋งต
  * Convolution ์ฐ์ฐ ํ ๊ฒฐ๊ณผ๋ฌผ
  * ํผ์ฒ๋งต์ ๋ง๋๋ ์ด์ 
    * ์ด๋ฏธ์ง์ ๊ณต๊ฐ์ ์ธ ํน์ง์ ์ถ์ถํ๊ธฐ ์ํด

![](../../img/conv.png)
[์ด๋ฏธ์ง ์ถ์ฒ](https://poloclub.github.io/cnn-explainer/)

* CNN, DNN์ ๊ฐ์ฅ ํฐ ์ฐจ์ด
* 1์ฐจ์์ผ๋ก flatten ํด์ ๋ฃ์ด์ฃผ๋๊ฒ ์๋๋ผ Conv, Pooling ์ฐ์ฐ์ ํตํด ํน์ง์ ํ์ตํ๊ณ  ์์ถํ ๊ฒฐ๊ณผ๋ฅผ flatten ํด์ DNN ์ ๋ฃ์ด์ค๋๋ค.
* DNN์ ์ด๋ฏธ์ง ๋ฐ์ดํฐ์ ์ฌ์ฉํ์ ๋ ๋จ์ 
  * `flatten()` ์ผ๋ก 1์ฐจ์ ๋ฒกํฐ ํํ๋ก ์ฃผ์์ ํด์ ์ธ์  ๊ณต๊ฐ์ ๋ํ ์ ๋ณด๋ฅผ ์์ด๋ฒ๋ฆผ
  * 1์ฐจ์ ํํ๋ก ์ฃผ์ํ๋ฉด ์๋ ฅ๊ฐ์ด ๋๋ฌด ์ปค์ ์ค๋ ์๊ฐ ์์
  * Conv๊ณผ Pooling ์ฐ์ฐ์ ํ๊ฒ ๋๋ฉด ๋ฐ์ดํฐ์ ๊ณต๊ฐ์ ์ธ ํน์ง์ ํ์ต
  * Pooling์ ํตํด ๋ฐ์ดํฐ๋ฅผ ์์ถํ์ฌ ์ฉ๋์ด ์ค๊ณ , ์ถ์ํ๋ฅผ ํ๊ธฐ ๋๋ฌธ์ ๋๋ฌด ์์ธํ๊ฒ ํ์ตํ์ง ์์ โก๏ธ ๊ณผ์ ํฉ ๋ฐฉ์ง

<br>

### - ์กํฐ๋ฒ ์ด์๋งต
  * ํ์ฑํ ํจ์๋ฅผ ํต๊ณผํ ๊ฒฐ๊ณผ๋ฌผ

![](../../img/afcnn.png)
[์ด๋ฏธ์ง ์ถ์ฒ](https://poloclub.github.io/cnn-explainer/)

<br>

### - pooling layer ์ ์ญํ 
* ๋์ฒด์ ์ผ๋ก ์ปฌ๋ฌ ์ด๋ฏธ์ง์์๋ `MaxPooling` ์ ๊ฐ์ฅ ๋ง์ด ์ฌ์ฉ
* ํ๋ฐฑ ์ด๋ฏธ์ง์์๋ `MinPooling` ์ ์ฌ์ฉํ๊ธฐ๋ ํจ
* MaxPooling ์ ๊ฐ์ฅ ํฐ ๊ฐ ๋ฐํ 
* AveragePooling ์ ํ๊ท  ๊ฐ ๋ฐํ 
* MinPooling ์ ์ต์๊ฐ ๋ฐํ
* Stride ์กฐ์  ๊ฐ๋ฅ
* ์ด๋ฏธ์ง์ ํฌ๊ธฐ๋ฅผ ์ค์ด๊ณ  ๋ฐ์ดํฐ๋ฅผ ์์ถ
  * ๊ณผ๋์ ํฉ ๋ฐฉ์ง โก๏ธ ์ด๋ฏธ์ง๋ฅผ ์ถ์ํ ํด์ฃผ๊ธฐ ๋๋ฌธ์ ์์ธํ ํ์ต๋์ง ์๋๋ก ํจ
  * ์ฉ๋ ๊ฐ์
  * ๊ณ์ฐ ํจ์จ์ฑ ์ฆ๊ฐ

![](../../img/pool.png)
[์ด๋ฏธ์ง ์ถ์ฒ](https://poloclub.github.io/cnn-explainer/)

> * CNN ๊ด๋ จ ๋ผ๋ฌธ์ ๋ณด๋ฉด ์ด ์ธต์ ์ผ๋ง๋ ๊น๊ฒ ์๋์ง์ ๋ํ ๋ผ๋ฌธ์ด ์์ 
> * VGG16, VGG19 ๋ฑ์ ์ธต์ 16๊ฐ, 19๊ฐ ๋งํผ ๊น๊ฒ ๋ง๋  ๊ฒ์ ์๋ฏธ
> * 30~50์ธต๊น์ง ์๊ธฐ๋ ํ๊ณ  100์ธต ์ ๋ ์๊ธฐ๋ ํจ 
> * ์ธต์ ์๋ฅผ ๋ชจ๋ธ์ ์ด๋ฆ์ ๋ถ์ด๊ธฐ๋ ํจ
> * ๊ณผ๊ฑฐ์ ๋นํด GPU ๋ฑ์ ์ฐ์ฐ์ ๋ ๋ง์ด ์ง์ํ๊ธฐ ๋๋ฌธ์ ์ฐ์ฐ์ด ๋นจ๋ผ์ง ๋๋ถ

<br> 


## โ Classification
[PIL ๋ผ์ด๋ธ๋ฌ๋ฆฌ ๊ธฐ๋ฅ](https://ddolcat.tistory.com/690)

### - ๋ฐ์ดํฐ ๋ถ๋ฌ์ค๊ธฐ
* `wget` ์ ์ด์ฉํ์ฌ URL์ ์๋ ๋ฐ์ดํฐ ๋ถ๋ฌ์ค๊ธฐ 
```python
!wget https://data.lhncbc.nlm.nih.gov/public/Malaria/cell_images.zip
!unzip cell_images.zip
```

### - ๋ฐ์ดํฐ ์ ์ฒ๋ฆฌ
* ์ด๋ฏธ์ง ์ฌ์ด์ฆ๊ฐ ๋ค ๋ค๋ฅด๋ฉด ๊ณ์ฐ ๋ถ๊ฐ๋ฅ
* ์ด๋ฏธ์ง ์ฌ์ด์ฆ๋ฅผ ํต์ผํด์ฃผ๋ ๋จ๊ณ ํ์
* `PIL`, `OpenCV` ๋ฑ์ ํ์ฉ
* ์ด๋ค ์ฌ์ด์ฆ๊ฐ ์ข์๊น?
  * ๊ณ์ฐ ํธ์๋ฅผ ์ํด ๋ณดํต ์ ์ฌ๊ฐํ ํํ๋ก ๋ง๋ค์ด ์ค
  * ์๋ ์ด๋ฏธ์ง๊ฐ ์๊ณก๋  ์ ์์
  * ์ฌ์ด์ฆ๋ฅผ ์๊ฒ ํ๋ฉด ๊ณ์ฐ ์๋๊ฐ ๋นจ๋ผ์ง
  * ์ฌ์ด์ฆ๋ฅผ ํฌ๊ฒ ํ๋ฉด ์ฑ๋ฅ์ด ์ข์์ง
  * ํ์ดํผ ํ๋ผ๋ฏธํฐ์ฒ๋ผ ์กฐ์ 
  * layer ๊ตฌ์ฑ์ ๋ฐ๋ผ ๋ณด์์ด ๊ฐ๋ฅํ๊ธฐ๋ ํจ

```python
train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
  
    # ์ด๋ฏธ์ง ์ฌ์ด์ฆ ๊ณ ์  
    image_size=(img_height, img_width),

    # ๊ฐ์ ธ์ฌ ์ด๋ฏธ์ง ๊ฐ์, ์ผ๋ถ ์ด๋ฏธ์ง๋ง ๋ถ๋ฌ์ ํ์ต
    batch_size=batch_size)
```

```python
model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),

  layers.Conv2D(filters=16, kernel_size=3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
```

* `padding`
  * `โvalidโ`
    * conv2d ์ธต์ padding ๋งค๊ฐ๋ณ์์ ๊ธฐ๋ณธ๊ฐ
    * ์ปค๋์ด ์ธํ ์ด๋ฏธ์ง ๋ฐ์ผ๋ก ์ฌ๋ผ์ด๋ฉ ํ์ง ์์
    * ์ ํจํ ์์ญ๋ง ์ถ๋ ฅ, ๋ฐ๋ผ์ ์ถ๋ ฅ ์ด๋ฏธ์ง ์ฌ์ด์ฆ๋ ์๋ ฅ ์ฌ์ด์ฆ๋ณด๋ค ์์์ง
  * `โsameโ`
    * ์ถ๋ ฅ ํฌ๊ธฐ๊ฐ ์๋ ฅ๊ฐ๊ณผ ๋์ผํด์ง๋๋ก ์๋ ฅ ์ด๋ฏธ์ง ์ฃผ์์ 0 ํฝ์ ํจ๋ฉ
    * ์ถ๋ ฅ ์ด๋ฏธ์ง ์ฌ์ด์ฆ๊ฐ ์๋ ฅ ์ด๋ฏธ์ง ์ฌ์ด์ฆ์ ๋์ผ

<br>

### - ๋ฐ์ดํฐ ์ฆ๊ฐ
* ๋ฐ์ดํฐ๋ฅผ ์ฆ๊ฐํ๊ธฐ ์ํด
  * ์ด๋ฏธ์ง ๋ฐ์ 
  * ํ์ 
  * ๋ฐฐ์จ ์กฐ์ 
```python
data_augmentation = keras.Sequential(
  [
    layers.RandomFlip("horizontal",
                      input_shape=(img_height,
                                  img_width,
                                  3)),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
  ]
)
```

* ์ฆ๊ฐ์ ํ๋ฉด ์๋๋ ๊ฒฝ์ฐ
  * ํฌ๋กญ์ด๋ ํ๋ โก๏ธ ์ฅ๋น ์ฌ์ง์ ํ๋์ ๋ธ์ด์ฆ๋ฅผ ํ๋ํ๊ฑฐ๋ ํฌ๋กญํ๋ฉด ๋ฌธ์ ๊ฐ ๋  ์ ์์
  * ํ์ ์ด๋ ๋ฐ์  โก๏ธ 6์ 180๋ ๋๋ฆฌ๋ฉด 9๊ฐ ๋๊ธฐ ๋๋ฌธ์ ์ซ์ ์ด๋ฏธ์ง๋ฅผ ํ์ ํ์ง ์์
  * ์์ ๋ณ๊ฒฝ โก๏ธ ๊ฝ์ ๊ฒฝ์ฐ ๋ค์ํ ์์์ด ์๊ธฐ์ ์๊ด์์ง๋ง ์ ํธ๋ฑ ๊ฐ์ด ์์ ๊ณผ ์ง๊ฒฐ๋๋ ๊ฒฝ์ฐ ๋ณ๊ฒฝ X
  * ์ฆ๊ฐ์ train ์๋ง ์ ์ฉ
  * ์ฆ๊ฐ์ ํ  ๋๋ ํ์ค ์ธ๊ณ ๋ฌธ์ ์ ์ฐ๊ดํด์ ๊ณ ๋ฏผํด๋ด์ผ ํจ

<br> 

## โ Malaria image load 1001
### - ์ด๋ฏธ์ง ๋ก๋ ๋ฐฉ๋ฒ
* matplotlib.pyplot ์ imread()๋ฅผ ์ฌ์ฉํ๋ ๋ฐฉ๋ฒ
```python
import matplotlib.pyplot as plt
img = plt.imread(paths[0])
img.shape
```

<br>

* PIL(Pillow) ๋ก ๋ถ๋ฌ์ค๋ ๋ฐฉ๋ฒ
* PIL ๋ก augmentation ๊ฐ๋ฅ
* TF ๋ด๋ถ์์๋ PIL ์ด๋ OpenCV๋ฅผ ์ฌ์ฉํด์ augmentation ๊ฐ๋ฅ
* ์ด๋ฏธ์ง ํธ์ง๊ธฐ๋ฅผ ๋ง๋ค ์๋ ์์
```python
from PIL import Image, ImageFilter
original = Image.open(cell_img)
original
```

<br>  

* OpenCV๋ก ๋ถ๋ฌ์ค๋ ๋ฐฉ๋ฒ
* Computer Vision์ ์ฃผ๋ก ์ฌ์ฉํ๋ ๋๊ตฌ๋ก ๋์์์ฒ๋ฆฌ ๋ฑ์ ์ฃผ๋ก ์ฌ์ฉ
```python
import cv2

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img.shape
```

<br> 

## โ Malaria CNN 1002
### - ImageDataGenerator, ์ด๋ฏธ์ง ๋ฐ์ดํฐ ์ ์ฒ๋ฆฌ
```python
# ImageDataGenerator ๋ฅผ ํตํด ์ด๋ฏธ์ง๋ฅผ ๋ก๋ํ๊ณ  ์ ์ฒ๋ฆฌ
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# validation_split ๊ฐ์ ํตํด ํ์ต:๊ฒ์ฆ ๋น์จ์ 8:2 ๋ก ๋๋
datagen = ImageDataGenerator(rescale=1/255.0, validation_split=0.2)
```
* ๊ณต๊ฐ ๋ ๋ฒจ ๋ณํ
  - Flip : ์ํ, ์ข์ฐ ๋ฐ์ 
  - Rotation : ํ์ 
  - Shift : ์ด๋
  - Zoom : ํ๋, ์ถ์
  - Shear : ๋ํ๊ธฐ

<br>

* ํฝ์ ๋ ๋ฒจ ๋ณํ
  - Bright : ๋ฐ๊ธฐ ์กฐ์ 
  - Channel Shift : RGB ๊ฐ ๋ณ๊ฒฝ
  - ZCA Whitening : Whitening ํจ๊ณผ

<br>

### - ํ์ต & ๊ฒ์ฆ ๋ฐ์ดํฐ ์ ๋ถ๋ฆฌ
* label์ ํด๋๋ช์ผ๋ก ์ ์
* class_mode : ์ด์ง๋ถ๋ฅ์ด๊ธฐ ๋๋ฌธ์ binary
* class_mode : One of "categorical", "binary", "sparse", "input", or None. Default: "categorical".
* subset: Subset of data ("training" or "validation")
```python
height = 32 
width = 32

trainDatagen = datagen.flow_from_directory(directory = 'cell_images/',
                                           target_size = (height, width),
                                           class_mode = 'binary',
                                           batch_size = 64,
                                           subset='training')
```
```python
valDatagen = datagen.flow_from_directory(directory = 'cell_images/',
                                         target_size =(height, width),
                                         class_mode = 'binary',
                                         batch_size = 64,
                                         subset='validation')
```


<br>

### - ๋ฐ์ดํฐ ํ์๋ณ ๋ ์ด์ด ๊ตฌ์ฑ
|๋ฐ์ดํฐ|layer|
|:----:|:----:|
|๋ฒกํฐ ๋ฐ์ดํฐ(์๊ฐ์ด๋ ์์๊ฐ ์๊ด ์์)|MLP (๋ฐ์ง์ธต)|
|์ด๋ฏธ์ง ๋ฐ์ดํฐ(ํ๋ฐฑ ๋๋ ์ปฌ๋ฌ)| 2D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง|
|์คํํธ๋ก๊ทธ๋จ ์ค๋์ค ๋ฐ์ดํฐ| 2D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง์ด๋ ์ํ ์ ๊ฒฝ๋ง|
|ํ์คํธ ๋ฐ์ดํฐ| 1D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง์ด๋ ์ํ ์ ๊ฒฝ๋ง|
|์๊ณ์ด ๋ฐ์ดํฐ(์๊ฐ์ด๋ ์์๊ฐ ์ค์ํจ)| 1D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง์ด๋ ์ํ ์ ๊ฒฝ๋ง|
|๋ณผ๋ฅจ ๋ฐ์ดํฐ(์: 3D ์๋ฃ ์ด๋ฏธ์ง)| 3D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง|
|๋น๋์ค ๋ฐ์ดํฐ(์ด๋ฏธ์ง์ ์ํ์ค)| 3D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง(๋ชจ์ ํจ๊ณผ๋ฅผ ๊ฐ์งํด์ผ ํ๋ ๊ฒฝ์ฐ) <br> ํน์ฑ ์ถ์ถ์ ์ํด ํ๋ ์ ๋ณ๋ก ์ ์ฉํ 2D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง ์กฐํฉ <br> ํน์ฑ ์ํ์ค๋ฅผ ์ฒ๋ฆฌํ๊ธฐ ์ํด RNN์ด๋ 1D ํฉ์ฑ๊ณฑ ์ ๊ฒฝ๋ง ์กฐํฉ

<br>

> ์ฑ๋ฏผ๋ <br>
> ์ฐธ๊ณ ๋ก tensorflow.js ๋ฅผ ๋ง๋๋ ๊ตฌ๊ธ ๋ธ๋ ์ธ ํ์ ์ํ๋ฉด conv2d ๋ณด๋ค tf.layers.separableConv2d(๊น์ด๋ณ ๋ถ๋ฆฌ ํฉ์ฑ๊ณฑ) ์ธต์ด ๊ฐ์ ์์์ ๋์ผ ํ๊ฑฐ๋ ํจ์ฌ ์ ์ํํ๋ ๋ ์๊ณ  ๋น ๋ฅธ ์ ๊ฒฝ๋ง์ ๋ง๋ค ์ ์๊ธฐ ๋๋ฌธ์ ์ฒ์๋ถํฐ ์ ๊ฒฝ๋ง์ ์๋ ๊ฒฝ์ฐ๋ผ๋ฉด conv2d๋ฅผ ๋์ฒดํด์ ์ฌ์ฉํ๋ ๊ฑธ ์ถ์ฒํ๋ค๊ณ  ํจ


<br> 

* CNN ๋ชจ๋ธ์ ํ์ต์ํค๋๋ฐ ๋ด ์ปดํจํฐ๋ก ๋๋ ธ๋๋ ๋ฉ๋ชจ๋ฆฌ ์ค๋ฅ๊ฐ ๋ฌ๋ค๋ฉด?
* ์ผ๋จ ์ฑ๋ฅ๊ณผ ๊ด๊ณ ์์ด ๋๋ฆฌ๊ณ  ์ถ๋ค! ์ด๋ป๊ฒ ํด๊ฒฐํ๋ฉด ์ข์๊น?
* ๋์ ์ฐ์ง ์๊ณ  ํด๊ฒฐํ๋ ๋ฐฉ๋ฒ!
  * ์ด๋ฏธ์ง ์ฌ์ด์ฆ๋ฅผ ์ค์ธ๋ค.
  * ๋ ์ด์ด๋ฅผ ์ค์ธ๋ค.
  * ํํฐ์๋ฅผ ์ค์ธ๋ค.
  * ๋ฐฐ์น(ํ๋ฒ์ ๋ค ๋ถ๋ฌ์ค์ง ์๊ณ  ๋๋ ์ ๋ถ๋ฌ์ค๊ฒ) ์ฌ์ด์ฆ๋ฅผ ์ค์ธ๋ค. โก๏ธ ๋ชจ๋  ์ฌ์ง์ ๋๋ ์ ์กฐ๊ธ์ฉ ํ์ต 

<br>

## โ Transfer learning
[์ฐธ๊ณ  ์๋ฃ](https://newindow.tistory.com/254) <br>
[tf.keras.applications link](https://www.tensorflow.org/api_docs/python/tf/keras/applications) <br> 
Keras Applications are premade architectures with pre-trained weights. <br>
[keras ์ ์ดํ์ต ๊ฐ์ด๋](https://keras.io/guides/transfer_learning/) <br>
[VGG16 API ๊ณต์ ๋ฌธ์](https://www.tensorflow.org/api_docs/python/tf/keras/applications/vgg16/VGG16)
### - Transfer learning์ด๋
* ํน์  ๋ถ์ผ์์ ํ์ต๋ ์ ๊ฒฝ๋ง(pre-trained)์ ์ผ๋ถ ๋ฅ๋ ฅ์ ์ ์ฌํ๊ฑฐ๋ ์ ํ ์๋ก์ด ๋ถ์ผ์์ ์ฌ์ฉ๋๋ ์ ๊ฒฝ๋ง์ ํ์ต์ ์ด์ฉํ๋ ๋ฐฉ๋ฒ
* ํ์ต ๋ฐ์ดํฐ์ ์๊ฐ ์ ์ ๋ ํจ๊ณผ์ 
* ์ ์ดํ์ต ์์ด ํ์ตํ  ๋๋ณด๋ค ํจ์ฌ ๋์ ์ ํ๋์ ๋น ๋ฅธ ํ์ต ์๋ ์ ๊ณต
* ์ ์ด ํ์ต์ ์ด์ฉ๋๋ pre-trained model
  * ImageNet
  * ResNet
  * GoogLeNet
  * VGGNet

```python
from tensorflow.keras.applications.vgg16 import VGG16

vgg = VGG16(include_top=False, weights='imagenet', input_shape=(height, width, 3))

model = Sequential()
model.add(vgg)
model.add(Flatten())

# ์ด์ง ๋ถ๋ฅ๋ฅผ ์ํ ์ถ๋ ฅ์ธต
model.add(Dense(1, activation='sigmoid'))
```
> input_shape    optional shape tuple, only to be specified if include_top is False (otherwise the input shape has to be (224, 224, 3) (with channels_last data format) or (3, 224, 224) (with channels_first data format). It should have exactly 3 input channels, and width and height should be no smaller than 32. E.g. (200, 200, 3) would be one valid value.

<br>

### - include_top
[์ถ์ฒ](https://www.learndatasci.com/tutorials/hands-on-transfer-learning-keras/) <br>
* ๊ฐ์ฅ ์๋จ์ fully connected layer๋ค์ ํฌํจ ์ํฌ์ง์ ์ฌ๋ถ
* True

![](../../img/ict.png)

* False

![](../../img/icf.png)

<br>

### - ๋ชจ๋ธ ์๊ฐํ
```python
from tensorflow.keras.utils import plot_model

plot_model(model)
```

<br>

### - Fine Tuning
* ๋ชจ๋ธ์ ํ๋ผ๋ฏธํฐ๋ฅผ ๋ฏธ์ธํ๊ฒ ์กฐ์ ํ๋ ํ์
* ์ ์ด ํ์ต ์ดํ ๋์ Task์ ๋ง๊ฒ ๋ชจ๋ธ ํ๋ผ๋ฏธํฐ๋ฅผ ์๋ฐ์ดํธํ๋ ๊ฒ

<br>

## โ weather classification
```python
def img_read_resize(img_path):
    img = cv2.imread(img_path)

    # cv์์ฌ๋ BGR ์ฌ์ฉ, RGB๋ก ๋ณ๊ฒฝ
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ์ด๋ฏธ์ง ์ฌ์ด์ฆ ํต์ผ
    img = cv2.resize(img, (120, 120))
    return img
```

```python
def img_folder_read(img_label):
    """
    ํน์  ์ด๋ฏธ์ง ํด๋์ ์๋ ์ด๋ฏธ์ง๋ฅผ array ํํ๋ก ๋ฆฌ์คํธ์ ๋ด์์ฃผ๋ ํจ์
    """
    # ์ด๋ฏธ์ง์ ๋ ์ด๋ธ์ ๋ด์์ค ๋ฆฌ์คํธ
    img_files = []
    labels = []

    # ์ด๋ฏธ์ง ๋ ์ด๋ธ(ํด๋๋ช)์ ๋ฐ์ ์ด๋ฏธ์ง ๊ฒฝ๋ก ํ์ธ
    wfiles = glob.glob(f"{root_dir}/{img_label}/*")

    # ์ด๋ฏธ์ง ๋ฒํธ๋๋ก ๊ฒฝ๋ก ์ ๋ ฌ
    wfiles = sorted(wfiles)

    # ๊ฒฝ๋ก ๋ฆฌ์คํธ๋ฅผ ์ํํ๋ฉด์ ์ด๋ฏธ์ง ๊ฒฝ๋ก ํ๋์ฉ ํ์ธ
    for w_img in wfiles:
        try:
            # ์ด๋ฏธ์ง ์ฌ์ด์ฆ ์กฐ์ ํด์ ๋ฆฌ์คํธ์ ์ถ๊ฐ
            # ํ์์ ๋ง์ง ์๋ ์ด๋ฏธ์ง๊ฐ ๋ค์ด์ฌ ๊ฒฝ์ฐ ์๋ฌ
            img_files.append(img_read_resize(w_img))
            labels.append(img_label)
        except:
            continue

    return img_files, labels
```

<br>

### - train_test_split
* `fit(validation_split)`์ผ๋ก ๋๋ ๋ ๋จ
  * class๊ฐ ๊ท ์ผํ๊ฒ ๋๋ ์ง์ง ์๋ ๋จ์  ์์


> RGB ์ 255? <br>
> ํ๋์ ๋๋ถ๋ถ ๋ชจ๋ํฐ์ ์ต๋ ์ง์ ์ ์ฌ๋๋ 24๋นํธ์๋๋ค. (๋ฌผ๋ก  ๋ ๋ง์ด ์ง์ํ๋ ๋ชจ๋ํฐ ๋ค๋ ๋ง์ด ๋์์ต๋๋ค)
์ฆ ๊ฐ ํฝ์์ 2^24(~16.7M)์ ์์์ ํ์ํ  ์ ์๊ฒ ๋์ด์๊ณ 
24๋นํธ ๊ฐ์ ๊ฐ๊ฐ R G B  ์ธ๊ฐ์ ์์์ผ๋ก ๋๋์๋ฉด 24๋นํธ / 3์ด๋ฏ๋ก
๊ฐ ์ฑ๋์ ํญ์ 8๋นํธ๋ฅผ ๊ฐ์ง๊ฒ ๋๊ฒ ๋์์ต๋๋ค.
์ฑ๋๋น 8๋นํธ๋ผ๋๊ฒ์ ๊ณ ๋ คํ ๋ 0 ~ 255 (256๊ฐ)์ ์ซ์ ๊ฐ๋ง ์ธ์ฝ๋ฉ ํ  ์ ์๊ฒ ๋๋ ๊ฒ์ด ์ด์น์ ๋ง์ต๋๋ค.


<br>

### - from_logits
[์ฐธ๊ณ  ์๋ฃ](https://hwiyong.tistory.com/335)
 
* ๋ชจ๋ธ์ ์ถ๋ ฅ๊ฐ์ด ๋ฌธ์ ์ ๋ง๊ฒ normalize ๋์๋๋์ ์ฌ๋ถ 
* ์๋ฅผ ๋ค์ด, 10๊ฐ์ ์ด๋ฏธ์ง๋ฅผ ๋ถ๋ฅํ๋ ๋ฌธ์ ์์๋ ์ฃผ๋ก softmax ํจ์๋ฅผ ์ฌ์ฉ
* ์ด๋, ๋ชจ๋ธ์ด ์ถ๋ ฅ๊ฐ์ผ๋ก ํด๋น ํด๋์ค์ ๋ฒ์์์์ ํ๋ฅ ์ ์ถ๋ ฅํ๋ค๋ฉด, ์ด๋ฅผ logit=False๋ผ๊ณ  ํํ
* logit์ด ์๋๋ผ ํ๋ฅ ๊ฐ
* ๋ฐ๋๋ก ๋ชจ๋ธ์ ์ถ๋ ฅ๊ฐ์ด sigmoid ๋๋ linear๋ฅผ ๊ฑฐ์ณ์ ํ๋ฅ ์ด ์๋ ๊ฐ์ด ๋์ค๊ฒ ๋๋ค๋ฉด, logit=True๋ผ๊ณ  ํํ
* ๋ง ๊ทธ๋๋ก ํ๋ฅ ์ด ์๋๋ผ logit

>ํด๋์ค ๋ถ๋ฅ ๋ฌธ์ ์์ softmax ํจ์๋ฅผ ๊ฑฐ์น๋ฉด from_logits = False(default),
๊ทธ๋ ์ง ์์ผ๋ฉด from_logits = True.

```python
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
```

<br>

* `history` ์๊ฐํ๋ฅผ ํด๋ดค์ ๋ ๋ ์ด์ val_loss ๊ฐ์ด ๊ฐ์ํ์ง ์๋๋ฐ, loss ๊ฐ์ ์ค์ด๋ ๋ค๋ฉด ์ค๋ฒํผํ ๋์๋ค๊ณ  ํ๋จ
* ๋ฑ ์์น๊ฐ ์ผ๋ง๊ฐ ์ฐจ์ด๊ฐ ๋๋ฉด ์ค๋ฒํผํ์ด๋ค ์ด๋ ๊ฒ ๊ณต์์ผ๋ก ์๊ธฐ๋ ์ ํ์ง ์๋ ํธ
* val_loss ๊ฐ์ด ๋์์ง์ง ์๋๋ฐ loss ๊ฐ๋ง ๋์์ง๋ค๋ฉด ํ์คํ๊ฒ ์ค๋ฒํผํ์ด๋ผ๊ณ  ๋ณผ ์ ์์


<br>

### - Tensorflow callback function
[์ฐธ๊ณ  ์๋ฃ](restore_best_weights)


|parameter|์ค๋ช|
|:---:|:---:|
|`monitor`|EarlyStopping์ ๊ธฐ์ค์ด ๋๋ ๊ฐ|
|`min_delta`|๊ฐ์ ๋ ๊ฒ์ผ๋ก ๊ฐ์ฃผํ๊ธฐ ์ํ ์ต์ํ์ ๋ณํ๋|
|`patience`|monitor๋๋ ๊ฐ์ ๊ฐ์ ์ด ์์ ๊ฒฝ์ฐ, ๋ฌด์ํ๊ณ  ํ์ต์ ๊ณ์ํ๋ ํ์|
|`verbose`|0 or 1 <br> 0์ผ ๊ฒฝ์ฐ, ํ๋ฉด์ ๋ํ๋ ์์ด ์ข๋ฃ <br> 1์ผ ๊ฒฝ์ฐ ํ๋ฉด์ ์ถ๋ ฅ|
|`mode`|`auto` or `min` or `max` <br> monitor ๊ฐ์ด ์ต์๊ฐ ๋์ด์ผ ํ๋์ง ์ต๋๊ฐ ๋์ด์ผ ํ๋์ง ์ค์  <br> `auto` ๋ ๋ชจ๋ธ์ด ์์์ ํ๋จ|
|`baseline`|๋ชจ๋ธ์ด ๋ฌ์ฑํด์ผํ๋ ์ต์ํ์ ๊ธฐ์ค๊ฐ|
|`restore_best_weights`|๊ฐ์ฅ ์ข์ ์ฑ๋ฅ์ผ๋ก ๋๋๋ฆด ์ ํ๋ผ๋ฏธํฐ <br> True๋ผ๋ฉด monitor ๊ฐ์ด ๊ฐ์ฅ ์ข์์ ๋์ weight๋ก ๋ณต์|


<br>

### - FC์ธต์ ์ฒซ layer๋ถํฐ ์ฌ์ฉํ์ง ์๊ณ  ํฉ์ฑ๊ณฑ ์ฐ์ฐ์ ์ฌ์ฉํ ์ด์ 
[์ฐธ๊ณ  ์๋ฃ](https://excelsior-cjh.tistory.com/180)
* FC Layer๋ flatten์ด ํ์ํ๊ธฐ ๋๋ฌธ์ ์ง๋์น๊ฒ ๊ณ์ฐ์ด ๋ณต์กํด์ง๊ณ , ๊ณต๊ฐ์ ๋ณด๊ฐ ๋ง์ด ์์ค
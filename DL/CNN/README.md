# 🦁 TIL

[TF CNN 공식 문서](https://www.tensorflow.org/tutorials/images/cnn) <br>
[영운쓰 추천 자료](https://untitledtblog.tistory.com/150)

## ✅ Convolutional Neural Network, CNN
### - 합성곱 층 만들기

* CNN은 배치(batch) 크기를 제외하고 `(이미지 높이, 이미지 너비, 컬러 채널)` 크기의 텐서(tensor)를 입력
* 보통 컬러 이미지는 컬러 채널이 3 == R, G, B
* 흑백 이미지는 1

```python
model = models.Sequential()

# Convolution layer, input_shape = (높이, 너비, 채널)
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), 
                        activation='relu', input_shape=(32, 32, 3)))

# Max Pooling 연산을 수행하는 layer
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))

# 3D 출력을 1D로 펼침
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

# 10개의 클래스
model.add(layers.Dense(10))
```
* `filters`
  * 필터의 개수
* `kernel_size`
  * 커널의 크기가 작을수록 레이어 크기가 더 작아지므로 더 깊은 아키텍처 가능
  * 큰 크기의 커널은 더 적은 정부 추출 ➡️ 차원이 더 빨리 줄어들고 과소적합 가능성
  * 보통 홀 수로 사용하는 편
* `pool_size`
  * pooling 연산을 위한 커널 크기

<br>

### - Padding
[CNN explainer](https://poloclub.github.io/cnn-explainer/)

![](../../img/padding.png)

* padding 의 역할
  * 이미지가 줄어드는 것을 방지
  * 가장자리 부분의 특징을 좀 더 학습하기 위해
* `padding = 1`, `kernel_size = 3` 을 많이 사용 ➡️ 이미지가 줄어들지 않음

<br>

### - 피처맵
  * Convolution 연산 후 결과물
  * 피처맵을 만드는 이유
    * 이미지의 공간적인 특징을 추출하기 위해

![](../../img/conv.png)
[이미지 출처](https://poloclub.github.io/cnn-explainer/)

* CNN, DNN의 가장 큰 차이
* 1차원으로 flatten 해서 넣어주는게 아니라 Conv, Pooling 연산을 통해 특징을 학습하고 압축한 결과를 flatten 해서 DNN 에 넣어줍니다.
* DNN을 이미지 데이터에 사용했을 때 단점
  * `flatten()` 으로 1차원 벡터 형태로 주입을 해서 인접 공간에 대한 정보를 잃어버림
  * 1차원 형태로 주입하면 입력값이 너무 커서 오랜 시간 소요
  * Conv과 Pooling 연산을 하게 되면 데이터의 공간적인 특징을 학습
  * Pooling을 통해 데이터를 압축하여 용량이 줄고, 추상화를 하기 때문에 너무 자세하게 학습하지 않음 ➡️ 과적합 방지

<br>

### - 액티베이션맵
  * 활성화 함수를 통과한 결과물

![](../../img/afcnn.png)
[이미지 출처](https://poloclub.github.io/cnn-explainer/)

<br>

### - pooling layer 의 역할
* 대체적으로 컬러 이미지에서는 `MaxPooling` 을 가장 많이 사용
* 흑백 이미지에서는 `MinPooling` 을 사용하기도 함
* MaxPooling 은 가장 큰 값 반환 
* AveragePooling 은 평균 값 반환 
* MinPooling 은 최솟값 반환
* Stride 조정 가능
* 이미지의 크기를 줄이고 데이터를 압축
  * 과대적합 방지 ➡️ 이미지를 추상화 해주기 때문에 자세히 학습되지 않도록 함
  * 용량 감소
  * 계산 효율성 증가

![](../../img/pool.png)
[이미지 출처](https://poloclub.github.io/cnn-explainer/)

> * CNN 관련 논문을 보면 이 층을 얼마나 깊게 쌓는지에 대한 논문이 있음 
> * VGG16, VGG19 등은 층을 16개, 19개 만큼 깊게 만든 것을 의미
> * 30~50층까지 쌓기도 하고 100층 정도 쌓기도 함 
> * 층의 수를 모델의 이름에 붙이기도 함
> * 과거에 비해 GPU 등의 연산을 더 많이 지원하기 때문에 연산이 빨라진 덕분

<br> 


## ✅ Classification
[PIL 라이브러리 기능](https://ddolcat.tistory.com/690)

### - 데이터 불러오기
* `wget` 을 이용하여 URL에 있는 데이터 불러오기 
```python
!wget https://data.lhncbc.nlm.nih.gov/public/Malaria/cell_images.zip
!unzip cell_images.zip
```

### - 데이터 전처리
* 이미지 사이즈가 다 다르면 계산 불가능
* 이미지 사이즈를 통일해주는 단계 필요
* `PIL`, `OpenCV` 등을 활용
* 어떤 사이즈가 좋을까?
  * 계산 편의를 위해 보통 정사각형 형태로 만들어 줌
  * 원래 이미지가 왜곡될 수 있음
  * 사이즈를 작게 하면 계산 속도가 빨라짐
  * 사이즈를 크게 하면 성능이 좋아짐
  * 하이퍼 파라미터처럼 조정
  * layer 구성에 따라 보완이 가능하기도 함

```python
train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
  
    # 이미지 사이즈 고정 
    image_size=(img_height, img_width),

    # 가져올 이미지 개수, 일부 이미지만 불러와 학습
    batch_size=batch_size)
```

```python
model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),

  layers.Conv2D(filters=16, kernel_size=3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
```

* `padding`
  * `‘valid’`
    * conv2d 층의 padding 매개변수의 기본값
    * 커널이 인풋 이미지 밖으로 슬라이딩 하지 않음
    * 유효한 영역만 출력, 따라서 출력 이미지 사이즈는 입력 사이즈보다 작아짐
  * `‘same’`
    * 출력 크기가 입력값과 동일해지도록 입력 이미지 주위에 0 픽셀 패딩
    * 출력 이미지 사이즈가 입력 이미지 사이즈와 동일

<br>

### - 데이터 증강
* 데이터를 증강하기 위해
  * 이미지 반전
  * 회전
  * 배율 조정
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

<br> 

## ✅ Malaria image load 1001
### - 이미지 로드 방법
* matplotlib.pyplot 의 imread()를 사용하는 방법
```python
import matplotlib.pyplot as plt
img = plt.imread(paths[0])
img.shape
```

<br>

* PIL(Pillow) 로 불러오는 방법
* PIL 로 augmentation 가능
* TF 내부에서도 PIL 이나 OpenCV를 사용해서 augmentation 가능
* 이미지 편집기를 만들 수도 있음
```python
from PIL import Image, ImageFilter
original = Image.open(cell_img)
original
```

<br>  

* OpenCV로 불러오는 방법
* Computer Vision에 주로 사용하는 도구로 동영상처리 등에 주로 사용
```python
import cv2

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img.shape
```

<br> 

## ✅ Malaria CNN 1002
### - ImageDataGenerator, 이미지 데이터 전처리
```python
# ImageDataGenerator 를 통해 이미지를 로드하고 전처리
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# validation_split 값을 통해 학습:검증 비율을 8:2 로 나눔
datagen = ImageDataGenerator(rescale=1/255.0, validation_split=0.2)
```
* 공간 레벨 변형
  - Flip : 상하, 좌우 반전
  - Rotation : 회전
  - Shift : 이동
  - Zoom : 확대, 축소
  - Shear : 눕히기

<br>

* 픽셀 레벨 변형
  - Bright : 밝기 조정
  - Channel Shift : RGB 값 변경
  - ZCA Whitening : Whitening 효과

<br>

### - 학습 & 검증 데이터 셋 분리
* label은 폴더명으로 정의
* class_mode : 이진분류이기 때문에 binary
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

### - 데이터 타입별 레이어 구성
|데이터|layer|
|:----:|:----:|
|벡터 데이터(시간이나 순서가 상관 없음)|MLP (밀집층)|
|이미지 데이터(흑백 또는 컬러)| 2D 합성곱 신경망|
|스펙트로그램 오디오 데이터| 2D 합성곱 신경망이나 순환 신경망|
|텍스트 데이터| 1D 합성곱 신경망이나 순환 신경망|
|시계열 데이터(시간이나 순서가 중요함)| 1D 합성곱 신경망이나 순환 신경망|
|볼륨 데이터(예: 3D 의료 이미지)| 3D 합성곱 신경망|
|비디오 데이터(이미지의 시퀀스)| 3D 합성곱 신경망(모션 효과를 감지해야 하는 경우) <br> 특성 추출을 위해 프레임 별로 적용한 2D 합성곱 신경망 조합 <br> 특성 시퀀스를 처리하기 위해 RNN이나 1D 합성곱 신경망 조합

<br>

> 성민님 <br>
> 참고로 tensorflow.js 를 만드는 구글 브레인 팀에 의하면 conv2d 보다 tf.layers.separableConv2d(깊이별 분리 합성곱) 층이 같은 작업을 동일 하거나 훨씬 잘 수행하는 더 작고 빠른 신경망을 만들 수 있기 때문에 처음부터 신경망을 쌓는 경우라면 conv2d를 대체해서 사용하는 걸 추천한다고 함

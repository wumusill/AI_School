# 🦁 TIL

## ✅ Benz

[데이터 출처](https://www.kaggle.com/competitions/mercedes-benz-greener-manufacturing/data)

### - 선형 회귀 특징
[선형 회귀 공식 문서](https://scikit-learn.org/stable/modules/linear_model.html)
* 다른 모델들에 비해 간단한 작동 원리
* 매우 빠른 학습 속도
* 조정해줄 파라미터가 적음
* 이상치에 영향을 크게 받음
* 데이터가 수치형 변수로만 이루어져 있을 경우, 경향성이 뚜렷할 경우 사용하기 좋음

<br>

### - 선형 회귀 모델의 단점 보완 모델
* `Ridge`
* `Lasso`
* `ElasticNet`


<br>

### - OneHotEncoder
* `handle_unknown="ignore"`
  * test에는 등장하지만 train에 존재하지 않는 것은 무시
  * feature의 기준은 train
  * test에 train에 없는 값이 있다면 그 값은 feature로 만들지 않음
  * test 컬럼에 있으나 train 컬럼에 없는 경우 train 에 없는 컬럼에 대해 인코딩 진행하지 않고 무시
* fit은 train에만 진행
* test는 transform만 진행
* `OneHotEncoder` 는 수치 데이터까지 인코딩 하므로 이를 제외하는 전처리 필요
* `pd.get_dummies()` 의 경우 이런 전처리 없어도 범주 데이터만 알아서 인코딩 진행
* `drop="first"`
  * 모든 변수의 첫 번째 feature drop
  * 카테고리가 하나만 있는 경우 완전히 삭제됨
* `drop="if_binary"`
  * 두 개의 범주가 있는 각 기능의 첫 번째 범주를 삭제, 1개 or 3개 이상의 범주가 있는 기능은 그대로 유지
```python
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(handle_unknown="ignore")
```



8️⃣8️⃣ 하조🐯

🐯박혜정
사실(Fact): 피처스케일링을 통해 예측모델을 만들고 kaggle에 제출해보았고, 선형회귀의 특징에 대해 배웠다.
느낌(Feeling): 회귀분석에 대해 더 알아봐야겠다.
교훈(Finding): 복습..!

🐯구자현
사실(Fact): house price 전처리 마무리 & 제출과 benz 실습 시작하였다
느낌(Feeling): 메서드가 늘어날수록 새로운 에러를 만나게 되고 어렵다
교훈(Finding): 메서드가 무슨 작업을 하는지, 어떤 것을 return하는지 확실히 하자

🐯김영민
사실(Fact): 피처엔지니어링을 실습하였고, 벤츠 데이터셋을 사용하여 간단한 EDA를 해보았다.
느낌(Feeling):  아직 스스로 바로바로 실습을 못할 것 같다.
교훈(Finding): 복습이 답이다 !

🐯이영빈
사실(Fact): 피쳐엔지니어링 부트캠프에 들어온 것같이 자세하게 알아보았다
느낌(Feeling):  세상엔 똑똑한 사람들이 많고 나는 아직 경험치가 너무 부족하다
교훈(Finding): 참고자료를 많이 접하고 컨디션 관리를 잘하자

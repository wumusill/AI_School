# 🦁 TIL

## ✅ Support Vector Machine
### - SVM
* `Support Vector` : 각 클래스에서 분류 경계선을 지지하는 관측치들
* 두 클래스 사이 가장 넓이가 큰 분류 경계선을 찾기 때문에 `Large margin classification` 이라고도 함
* 선형이나 비선형 분류, 회귀, 이상치 탐색에 사용할 수 있는 ML 방법론
* 딥러닝 이전 시대까지 널리 사용
* 복잡한 분류 문제를 잘 해결
* 상대적으로 작거나 중간 크기를 가진 데이터에 적합
* 최적화 모형으로 모델링 후 최적의 분류 경계 탐색

<br>

* SVM은 스케일에 민감 ➡️ 변수들 간의 스케일을 잘 맞춰주는 것이 중요
* 스케일이 크면 상대적으로 좁은 margin을 가짐 ➡️ 일반화에 어려움 
* `sklearn`의 `StandardScaler`를 사용하면 잘 맞출 수 있음

<br>

### - `Hard Margin` vs `Soft Margin`
* `Hard Margin`
  * 두 클래스가 하나의 선으로 완벽하게 나눠지는 경우에만 적용 가능 ➡️ 강력한 제약조건
  * 적용할 수 있는 경우가 많지 않음
* `Soft Margin`
  * 일부 샘플들이 분류 경계선의 분류 결과에 반하는 경우를 일정 수준 허용하는 방법
  * C 패널티 파라미터로 조정, `Trade-off`
    * `C = 1` : 패널티가 작음 ➡️ `Soft Margin`, 경계선의 margin이 넓어짐<br>➡️ training error는 증가, 언더피팅 가능성
    * `C = 100` : 패널티가 큼 ➡️ `Hard Margin`, 경계선의 margin이 좁아짐<br>➡️ training error는 감소, 오버피팅 가능성
  * 벽의 탄성이 강할 때가 좋은 경우가 있고 반대의 경우가 있다
    * 어떻게 판단하는가?
    * validation set으로 error를 최소화하는 파라미터 설정 

<br>

## ✅ Nonlinear SVM
* 다항식 변수들을 추가함으로써 직선으로 분류할 수 있는 형태로 데이터 만듦

### - Nonlinear SVM Classification
* Polynomial Kernel
  * 다항식의 차수를 조절할 수 있는 효율적인 계산 방법
* Gaussian RBF Kernel
  * 무한대 차수를 갖는 다항식으로 차원을 확장시키는 효과
  * gamma : 고차항 차수에 대한 가중 정도, 복잡도를 조정하는 하이퍼 파라미터
    * 커지면 결정 경계가 비선형에 가까워지고 복잡한 모델이 됨
    * 작아지면 결정 경계가 선형에 가까워지며 일반적인 모델이 됨


<br>

## ✅ SVM Regression
* 선형 회귀식을 중심으로 이와 평행한 오차 한계선을 가정
* 오차 한계선 너비가 최대가 되면서 오차 한계선을 넘어가는 관측치들에 패널티 부여
* Classification 모델과 같이 다항식 변수항을 추가함으로써 비선형적인 회귀 모형 적합
# 🦁 TIL
[딥러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)
[AI 142가지 데이터셋](https://needleworm.github.io/dataset/)
[BLSTM 정은쓰 추천 자료](https://blog.naver.com/ssj860520/222820930221)

## ✅ Natural Language Processing, NLP
* 자연어 의미를 분석하여 컴퓨터가 처리할 수 있도록 하는 일
* 자연어(natural language) : 우리가 일상 생활에서 사용하는 언어
* 기계에게 인간의 언어를 이해시키는 인공지능의 한 분야

<br>

### - 자연어 처리로 할 수 있는 일
* 음성 인식, 내용 요약, 번역
* 사용자의 감성 분석
* 텍스트 분류 작업(스팸 메일 분류, 뉴스 기사 카테고리 분류)
* 질의 응답 시스템, 챗봇 등 

> 네이버 영화리뷰의 저작권 ➡️ 네이버는 데이터베이스권, 리뷰 작성자에게는 저작권

<br>

### - 자연어 분류 과정
* 데이터 나누기와 벡터화 과정은 바뀔 수 있음
* 데이터 로드 ➡️ 텍스트 데이터 전처리 ➡️ 텍스트 데이터 벡터화 ➡️ 데이터 나누기 ➡️ 학습
* 데이터 로드 ➡️ 텍스트 데이터 전처리 ➡️ 데이터 나누기 ➡️ 텍스트 데이터 벡터화 ➡️ 학습

<br>

### - 데이터 정제 및 전처리
* 이상치 과적합 방지
* 텍스트 정제 ➡️ 신호와 소음을 구분
1. HTML 태그, 특수문자, 이모티콘
2. 정규 표현식
   * 문자, 숫자, 특수문자를 제외할 때 주로 사용
   * 특정 패턴으로 텍스트 전처리 시 사용
   * 그 자체로 프로그래밍 언어 
3. 불용어, Stopword
   * 문장에 자주 등장하지만 "우리, 그, 그리고, 그래서" 등 관사, 전치사, 조사, 접속사 등의 단어로 문장 내에서 큰 의미를 갖지 않는 단어
   * 영어는 불용어 사전을 사용하나 한국어는 주제나 프로젝트에 맞게 만들어 사용
   * 데이터에서 유의미한 단어 토큰을 선별하기 위해 큰 의미가 없는 단어 토큰 제거 작업 필요
   * 언어 분류, 스팸 필터링, 감정 분석과 관련된 작업 중 하나인 경우 불용어 제거 추천
   * 기계 번역, 질문 답변, 텍스트 요약, 언어 모델링의 경우 불용거 제거하지 않는 것을 추천
   * 장점
     * 데이터셋의 크기가 줄고 모델의 정확도에 영향을 미치지 않으면서 학습 시간 감소
     * 성능 향상에 잠재적으로 도움
   * 단점
     * 부적절한 불용어 선태은 텍스트의 의미 변경 가능성
4. 어간 추출, Stemming
5. 음소표기법, Lemmatizing

* `NLTK`, `Spacy`
  * 대표적인 텍스트 전처리 도구 
  * 토큰화, steming, lematization, 불용어 등의 기능 제공
  * 잘 사용하지 않을 예정 ➡️ 한글 미지원

<br>

* `stemming` vs `lematization`

![](../../img/Stemming_and_lemmatization.webp) <br>
[출처](https://www.turing.com/kb/stemming-vs-lemmatization-in-python)

<br>

### - 토큰화, Tokenization
* 패턴을 찾는 것에 유용, 형태소 분석 및 표제어를 위한 기본 단계
* 토큰, token : 문자열을 분석을 위한 문자열 단위로 단어, 문자 또는 하위 단어
* 토큰 생성, tokenizing : 문자열을 토큰으로 나누는 작업

<br>

## ✅ Frequency based Word Embedding

### - Bag of Words, BOW
* `Bag Of Words`, `TF-IDF` : 단어를 숫자로 인코딩 하는 방법
* 단어들의 순서를 전혀 고려하지 않고 단어들의 출현 빈도에만 집중
* 가장 간단하고 효과적이라 널리 쓰이는 방법
* 단어의 순서가 완전히 무시된다는 단점
  * 이를 보완하기 위해 `n-gram` 사용
  * [n-gram 참고 자료](https://heytech.tistory.com/343)
    * 모든 단어를 고려하는 것이 아니라 일부 단어만 고려하는 접근 방법
    * 일부 단어를 묶어서 사용
    * 앞뒤 맥락 고려 
  * BOW는 하나의 토큰 사용, n-gram은 n개의 토큰 사용


<br>

### - 문서 단어 행렬, DTM, Document-Term Matrix
* 다수의 문서에서 등장하는 각 단어들의 빈도를 하나의 행렬로 표현
* 각 문서에 대한 BOW를 하나의 행렬로 만든 것 

<br>

### - 단어 빈도, TF, Term Frequency
* 특정 단어가 문서 내에 얼마나 자주 등장하는지 나타내는 값
* 이 값이 높을수록 문서에서 얼마나 중요하다고 생각할 수 있음
* 단어 자체가 문서군 내에서 자주 사용되는 경우, 그 단어가 흔하게 등장한다는 의미

<br>

### - TF-IDF
* 전체 문서에서는 자주 등장하지 않지만 특정 문서에서 자주 등장한다면 가중치 값이 높게 나옴
* 모든 문서에 자주 등장하는 값은 가중치가 낮게 나옴
* TF와 IDF를 곱한 값
* IDF 값은 문서군의 성격에 따라 결정
  * 예를 들어 '원자'라는 낱말은 일반적인 문서들 사이에서는 잘 나오지 않기 때문에 높은 IDF 값 
  * 문서의 핵심어가 될 수 있지만, 원자에 대한 문서를 모아놓은 문서군의 경우 이 낱말은 상투어
  * 각 문서들을 세분화하여 구분할 수 있는 다른 낱말들이 높은 가중치를 얻게 된다.
* scikit-learn API를 통해 계산 가능

<br>

|구분|내용|
|:---:|:---:|
|TF|단어 빈도 <br> 특정한 단어가 문서 내 얼마나 자주 등장하는지 나타내는 값 <br> 이 값이 높을수록 문서에서 중요하다고 생각할 수 있음|
|DF|문서 빈도 <br> 특정 단어가 등장한 문서의 수 <br> 단어 자체가 문서군 내 자주 사용되는 경우 <br> 그 단어가 흔하게 등장한다는 것을 의미|
|IDF|역문서 빈도, DF의 역수로 DF에 반비례하는 수|
|TF-IDF|`TF * IDF` <br> 모든 문서에 자주 등장하는 단어는 중요도가 낮다고 판단 <br> 특정 문서에서만 등장하는 단어는 중요도가 높다고 판단 <br> TF-IDF 값이 낮으면 중요도가 낮은 것 <br> TF-IDF 값이 높으면 중요도가 높은 것 <br> 불용어의 TF-IDF의 값은 다른 단어의 TF-IDF에 비해 낮음|

<br>

## ✅ scikit-learn feature_extraction API

|API|기능|
|:---:|:---:|
|`feature_extraction.DictVectorizer()`|특성-값 매핑 목록을 벡터로 변환|
|`feature_extraction.text.CountVectorizer()`|텍스트 문서 모음을 토큰 수의 행렬로 변환|
|`feature_extraction.text.HashingVectorizer()`|텍스트 문서 모음을 토큰 발생 매트릭스로 변환|
|`feature_extraction.text.TfidTransformer()`|카운트 행렬을 정규화된 tf 또는 tf-idf 로 변환|
|`feature_extraction.text.TfidVectorizer()`|문서 모음을 tf-idf 매트릭스로 변환|

<br>

### - DictVectorizer
* [공식 문서](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer)
* 각 단어의 수가 기록된 사전을 가지고 BOW 인코딩 백터를 생성
* Parameters
  * dtype
    * 특성 값의 유형
    * Numpy 배열/scipy.sparse 행렬 생성자에 dtype 인수로 전달
  * separator
    * 원핫 인코딩을 위한 새로운 기능을 구성할 때 사용되는 구분자 문자열
  * sparse
    * 변환이 scipy.sparse 행렬을 생성해야 하는지 여부
  * sort
    * feature_names_와 vocabulary_를 학습할 때 정렬 여부
```python
from sklearn.feature_extraction import DictVectorizer

dvect = DictVectorizer(sparse=False)
d = [{"foo":1, "baz":2}, {"foo":3, "baz":1}]

dvect.fit_transform(d)

>>> array([[2., 1.],
>>>        [1., 3.]])
```

<br>

### - CountVectorizer
* sklearn에서 제공하는 bag of words 를 만들 수 있는 API
* 텍스트 문서 모음을 토큰 수의 행렬로 변환
* 단어들의 카운트(출현 빈도)로 여러 문서들을 벡터화
* 문서목록에서 각 문서의 feature(문장의 특징) 노출수를 가중치로 설정한 BOW 벡터를 생성
* 카운트 행렬, 단어 문서 행렬 (Term-Document Matrix, TDM))
* max_df, min_df 인수를 사용하여 문서에서 토큰이 나타난 횟수를 기준으로 단어장을 구성 
* 토큰의 빈도가 max_df로 지정한 값을 초과 하거나 min_df로 지정한 값보다 작은 경우에는 무시하며 인자 값은 정수인 경우 횟수, 부동소수점인 경우 비율을 의미
* [API documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)

### - 사용법
1. 문서를 토큰 리스트로 변환
2. 각 문서에서 토큰의 출현 빈도를 셈
3. 각 문서를 BOW 인코딩 벡터로 변환
4. 매개 변수
    * `analyzer` : 단어, 문자 단위의 벡터화 방법 정의
    * `ngram_range` : BOW 단위 수 (1, 3) 이라면 1개~3개까지 토큰을 묶어서 벡터화
    * `max_df` : 어휘를 작성할 때 문서 빈도가 주어진 임계값보다 높은 용어(말뭉치 관련 불용어)는 제외 (기본값=1.0)
        * 너무 많이 등장하는 단어를 제외하는 효과
        * `max_df=0.9` : 문서의 90% 이상에 나타나는 단어 제외
        * `max_df=10` : 문서에 10개 이상 나타나는 단어 제외
    * `min_df` : 어휘를 작성할 때 문서 빈도가 주어진 임계값보다 낮은 용어는 제외합니다. 컷오프라고도 합니다.(기본값=1.0)
        * 너무 적게 등장하는 단어를 제외하는 효과 
        * `min_df=0.01` : 문서의 1% 미만으로 나타나는 단어 제외
        * `min_df=10` : 문서에 10개 미만으로 나타나는 단어 제외
    * `stop_words` : 불용어 정의
    * `max_features` : 어휘의 양을 제한
      * `max_features=10` : 10개의 단어만 추출
      * 단어를 너무 많이 사용해서 dtm 이 커지는 것을 방지하기 위함

> * 이미지를 다룰 때는 돈을 쓰지 않고 모델을 내 컴퓨터에서 돌리기 위해 이미지 사이즈, 레이어 개수 등을 조정
> * 텍스트 데이터에서 내 컴퓨터가 힘들어 한다면 여러 방법을 사용 
> * 가장 간단한 방법이 max_features 를 작게 조정하는 것
> * 비지도학습의 차원축소를 사용하게 되면 데이터를 압축해서 사용 가능
> * 그런데 차원축소 과정에서도 메모리 오류가 발생할 수도 있음 
> * 그럴 때 max_features 를 내 컴퓨터가 계산할 사이즈로 적당하게 조정해 주면 로컬 PC로도 돌려볼 수 있음
> * 여기에서 조금 더 조정한다면 min_df, max_df, stop_words 등을 조정

<br>

### - HashingVectorizer
* [공식 문서](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer)
* 텍스트 문서 모음을 토큰 발생 매트릭스로 변환
* 해시 함수를 사용하여 단어에 대한 인덱스 번호를 생성하기 때문에 메모리 및 실행 시간 감소
* CountVectorizer는 모든 작업을 메모리 상에서 수행해 문서가 너무 크다면 실행이 불가능

<br>

### - TfidTransformer
* [공식 문서](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer)
* 카운트 행렬을 정규화된 tf 또는 tf-idf 표현으로 변환

<br>

### - TfidVectorizer
* [공식 문서](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer)
* 단어를 개수 그대로 카운트하지 않고 모든 문서에 공통적으로 들어있는 단어의 경우 가중치를 축소하는 방법

```python
from sklearn.feature_extraction.text import TfidVectorizer

tfidf = TfidVectorizer(analyzer="word", max_df=1.0, min_df=1, ngram_range=(1, 1))
tf_wv = tfidf.fit_transform(document)
pd.DataFrame(tf_wv.toarray(), columns=tfidf.get_feature_names_out())
```

<br>

```python
# topic을 입력받아 출력
def display_word_cloud_topic(topic, width=1200, height=500):
    word_draw = WordCloud(
        font_path=r"/Library/Fonts/NanumBarunGothic.ttf",
        width=width, height=height,
        stopwords=["합니다", "입니다"], 
        background_color="white",
        random_state=42
    )

    # 올바른 topic
    try:
        data = ' '.join(df.loc[df["topic"] == topic, :]["title"])
        word_draw.generate(data)
        plt.figure(figsize=(15, 7))
        plt.imshow(word_draw)
        plt.axis("off")
        plt.show()

    # 이상한 topic
    except:
        topic_list = df["topic"].unique().tolist()
        print("존재하지 않는 topic 입니다.")
        print(f"topic list : {topic_list}")
```


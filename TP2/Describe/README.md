# 🦁 TIL

## ✅ 추상화된 도구를 통한 기술 통계 구하기
>python0105

## 🔗 Link
> pandas-profiling : https://github.com/ydataai/pandas-profiling <br>
sweetviz : https://github.com/fbdesignpro/sweetviz <br>
> sweetviz : https://pypi.org/project/sweetviz/

### - 장점

* 기본적인 EDA 빠르게 수행
* 편리

### - 단점
* 대용량 데이터에 사용하기 어려움
* 놓칠 수 있는 부분이 발생
* 미세한 컨트롤 불가능


<br>

## ✅ 추상화된 도구를 사용하지 않고 직접 기술 통계 구하기
>python0106




* `pandas-profiling`
* `sweetviz`
* `autoviz`
* `df.isnull().sum()`
* `df.isnull().mean()`
* `비대칭도 = .skew`
* `첨도 = .kurt`
* `표준화 = standardization`
* `정규화 = normalization`
* `np.triu`
* `np.ones_like`
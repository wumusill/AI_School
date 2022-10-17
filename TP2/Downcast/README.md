# 🦁 TIL

## 🔗 Link
> [data type](https://github.com/rougier/numpy-tutorial#quick-references)

## ✅ 용량이 큰 데이터 다루기
* 메모리 절약 : 절약을 통해 더 많은 데이터를 불러와서 더 많이 분석 
* 스토리지 절약 : 파일 크기를 줄여 더 많은 파일 저장

### 메모리 절약 ➡️ `downcast` 
> python0308

### - downcast

* `downcast` 하기 전 최솟값, 최댓값을 조회하여 타입 결정
```python
downcast : {'integer', 'signed', 'unsigned', 'float'}, default None
    If not None, and if the data has been successfully cast to a
    numerical dtype (or if the data was numeric to begin with),
    downcast that resulting data to the smallest numerical dtype
    possible according to the following rules:
```
* `df[col].dtypes.name.startswith("int")`
* `df[col] = pd.to_numeric(df[col], downcast='unsigned')`


* 범주형 형태일 때 category로 지정하면 메모리를 좀 더 효율적으로 사용 가능
* 이 때 범주의 수가 너무 많다면 적합하지 않을 수 있음


<br>


### 스토리지 절약 (디스크 공간) ➡️ `parquet`
> python0309

* `parquet`가 `csv`보다 훨씬 용량이 작음


* `csv`는 행 단위로 데이터 구분
* `parquet`은 열 단위로 데이터 구분
> 열 단위 압축은 동일한 데이터 타입으로 압축에 유리


<br>

* 데이터가 너무 작으면 `csv`가 더 작은 용량
  * `csv`는 메타 데이터를 포함하고 있지 않음
  * `parquet`는 메타 데이터를 포함하고 있음
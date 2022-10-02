# 🦁 TIL

* DB의 4가지 기능
    * 검색과 갱신
    * 동시성 제어
    * 장애 대응
    * 보안


## ✅ 데이터 검색 : SELECT

> 실습 환경 : https://solvesql.com/   <br>
> DB : 따릉이 자전거 이용 현황


### - TABLE 출력
* `*` : 모든 column 출력
* `LIMIT` : 출력 data 개수 제한
```sql
SELECT *
FROM station
LIMIT 10;
```
<br>

### - 조건문 : `WHERE`
* `WHERE vs HAVING`
  * `WHERE` : `GROUP BY` 전 데이터 필터링
  * `HAVING` : `GROUP BY` 후 요약 정보 필터링 
  * 가능하면 `WHERE` 구문에서 필터링 하는 것이 좋음 ➡️ 그룹화 과정에서 연산량이 더 적이지기 때문
```sql
-- local이 "마포구" 인 row들만 출력
SELECT *
FROM station
WHERE local = "마포구"
LIMIT 10;
```
* 쿼리문이 조건으로 들어갈 수도 있음 : 서브 쿼리
```sql
SELECT *
FROM station
WHERE lat > (SELECT lat FROM station WHERE name="서울북부지방법원");
```

<br>


### - 별칭 사용 : `AS`
* 별칭에 띄어쓰기를 하고 싶다면 `" "` 로 감싸준다.
```sql
SELECT name AS station_name
     , address AS 'station address'
FROM station
WHERE local = "마포구";
```
> 아래와 같이 AS는 생략이 가능 <br>
> 하지만 **가독성**을 위해 생략하지 않는걸 권장
```sql
SELECT name station_name
     , address station_address
FROM station
WHERE local = "마포구";
```


<br>


### - 여러 조건 : `OR`, `AND`, `IN`
```sql
SELECT *
FROM station
WHERE local = "마포구" OR local = "광진구";
```
```sql
SELECT *
FROM station
WHERE local IN ("마포구", "광진구");
```

<br>

### - 정렬 : `ORDER BY`
* 오름차순 설정 : `ASC`, 기본값으로 생략 가능
* 내림차순 설정 : `DESC`
```sql
SELECT *
FROM station
WHERE local = "광진구"
ORDER BY updated_at DESC;
```
> 정렬 조건이 두 개 이상이면?

```sql
SELECT *
FROM station
WHERE local = "광진구"
ORDER BY updated_at DESC, station_id DESC;
```

<br>

### - 부분 조건문 : `LIKE`
* `WHERE`절 안에서 문자열 일부분을 비교
* `_` : 한 글자만을 의미
* `%` : 0글자부터 그 이상을 의미
```sql
SELECT *
FROM table
-- "a"를 포함한 데이터 출력
WHERE col LIKE "%a%"
```



<br>

### - `IS NULL`/`IS NOT NULL`
* 테이블 내 **입력되지 않은 데이터**는 `NULL`로 저장
* `NULL` 값을 검색할 때 `IS NULL` 사용
* `NULL` 값이 아닌 행을 검색할 경우, `IS NOT NULL` 사용

```sql
SELECT *
FROM table
WHERE name IS NOT NULL; 
```

<br>

### - 유일값 출력 : `DISTINCT`

```sql
SELECT DISTINCT col
FROM TABLE;
```

<br><br>

## ✅ SQL 함수
### - `LEFT(str, len)`



### - `RIGHT(str, len)`



### - `SUBSTR(str, start, len)`
### - `CEIL()` : 올림 
### - `FLOOR()` : 내림
### - `ROUND()` : 반올림

<br><br>

## ✅ 데이터 변경/갱신
### - `UPDATE`
```sql
UPDATE table SET col1 = 'new_content' WHERE col2 = 'condition';
```

### - `DELETE`
```sql
DELETE FROM table WHERE col1 = 'condition';
```

### - `INSERT`
```sql
INSERT INTO table VALUES(col1, col2, col3...);
```

<br><br>

## ✅ 집계 함수

> 실습 환경 : https://solvesql.com/   <br>
> DB : Waiter's Tips

>`Null` 값이 있다면 집계 함수 사용 시 유의해야 함 

### - `COUNT()`
* `Null` 값이 있다면
  * `COUNT(*)` : 다른 셀을 참조하여 개수에 포함
  * `COUNT(Null이 있는 col)` : `Null`은 개수에 포함 X


* 테이블의 데이터 총 개수
```sql
SELECT COUNT(*)
FROM tips;
```
* 10불 이상 결제한 테이블 수
```sql
SELECT COUNT(*)
FROM tips
WHERE total_bill >= 10;
```

<br>

### - `SUM()`
* `Null` 값은 포함하지 않음
```sql
SELECT SUM(total_bill)
FROM tips;
```

### - `AVG()`
```sql
SELECT AVG(total_bill)
FROM tips;
```

### - `MIN(), MAX()`
```sql
SELECT MIN(total_bill)
FROM tips;

SELECT MAX(total_bill)
FROM tips;
```


<br><br>

## ✅ 그룹별로 요약
### - `GROUP BY`
* 그룹화 기준을 반드시 `SELECT`에 넣어줘야 함 
* 날짜별 매출액의 합계
```sql
SELECT day, SUM(total_bill)
FROM tips
GROUP BY day;
```

* 요일, 시간대별로 매출액의 합계 
```sql
SELECT day, time, SUM(total_bill)
FROM tips
GROUP BY day, time; 
```

<br>

### - `HAVING` : 요약 정보 필터링
* `HAVING` : `GROUP BY` 연산 결과물을 필터링
* `WHERE` : `GROUP BY` 하기 전 필터링 


* 요일별로 여성의 매출액 합계 출력, 매출액이 200불 미만인 날은 출력에서 제외


```sql
SELECT day, SUM(total_bill)
FROM tips
WHERE sex = 'Female'
GROUP BY day
HAVING SUM(total_bill) >= 200;
```

* 요일별로 여성의 매출액 합계를 출력, 매출액 200불 미만은 제외하고 내림차순으로 출력
```sql
SELECT day
     , SUM(total_bill) AS revenue_daily
FROM tips
WHERE sex = 'Female'
GROUP BY day
HAVING revenue_daily >= 200
ORDER BY revenue_daily DESC
```
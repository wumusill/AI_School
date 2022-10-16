# 🦁 TIL



## ✅ SQL 조건문 : `CASE & IF`
### - CASE
* `CASE`로 시작해서 `END`로 끝남
```sql
/* CASE
    WHEN (A조건) THEN (A조건이 True 일 때)
    WHEN (B조건) THEN (B조건이 True 일 때)
    ELSE (위의 조건이 모두 False 일 때)
END */
```

* [문제 링크](https://www.hackerrank.com/challenges/what-type-of-triangle/problem?h_r=internal-search)

```sql
SELECT 
    CASE
        WHEN A = B AND B = C THEN "Eqilateral"
        WHEN A = B THEN "Isosceles"
    END
FROM 
    triangles;
```
* `WHEN`의 순서 중요 ‼ <br>
* 순서에 따라 결과가 달라짐
> `WHEN A = B AND B = C THEN "Eqilateral"` 에서 결정된 데이터는 그 다음 코드로 넘어가지 않음

<br>


### - IF
```sql
-- IF(조건, 조건이 True일 때, False일 때)
```

<br>



### - Pivot 
* 결과 값을 가로로 보고 싶을 때 사용
* 행으로 나열되어 있던 데이터를 열 방향으로 변환해서 한 눈에 보고 싶을 때 사용
> [문제 링크](https://leetcode.com/problems/reformat-department-table/submissions/)

```sql
SELECT
    id, 
    SUM(CASE WHEN month = "Jan" THEN revenue ELSE Null END) AS Jan_Revenue,
    SUM(CASE WHEN month = "Feb" THEN revenue ELSE Null END) AS Feb_Revenue,
    SUM(CASE WHEN month = "Mar" THEN revenue ELSE Null END) AS Mar_Revenue,
    SUM(CASE WHEN month = "Apr" THEN revenue ELSE Null END) AS Apr_Revenue,
    SUM(CASE WHEN month = "May" THEN revenue ELSE Null END) AS May_Revenue,
    SUM(CASE WHEN month = "Jun" THEN revenue ELSE Null END) AS Jun_Revenue,
    SUM(CASE WHEN month = "Jul" THEN revenue ELSE Null END) AS Jul_Revenue,
    SUM(CASE WHEN month = "Aug" THEN revenue ELSE Null END) AS Aug_Revenue,
    SUM(CASE WHEN month = "Sep" THEN revenue ELSE Null END) AS Sep_Revenue,
    SUM(CASE WHEN month = "Oct" THEN revenue ELSE Null END) AS Oct_Revenue,
    SUM(CASE WHEN month = "Nov" THEN revenue ELSE Null END) AS Nov_Revenue,
    SUM(CASE WHEN month = "Dec" THEN revenue ELSE Null END) AS Dec_Revenue
FROM department
GROUP BY id
```
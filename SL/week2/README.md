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

<br>

## ✅ SQL : `Join`
> [SQL Joins Visualizer](https://sql-joins.leopard.in.ua/) <br>
> [실습 링크](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) <br>
> [문제 링크](https://www.hackerrank.com/challenges/african-cities/problem?h_r=internal-search)

### - `INNER JOIN`
* A와 B의 교집합
```sql
# Old
SELECT *
FROM Users, Orders
WHERE Users.Id = Orders.userId

# New
SELECT *
FROM Users
    INNER JOIN Orders ON Users.Id = Orders.userId
```



<br>

### - `LEFT JOIN`
* A와 B의 왼쪽 기준 합집합
```sql
SELECT * 
FROM Customers
	LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
```

> `RIGHT JOIN` 은 반대로 오른쪽 기준 합집합 <br>
> 보통 순서를 바꿔 `LEFT JOIN`을 많이 씀




<br>

### - `SELF JOIN`

* 자기 자신을 `JOIN`
> [문제 링크](https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/)

```sql
SELECT Employee.name as Employee
FROM Employee
    INNER JOIN Employee as Manager ON Employee.managerId = Manager.id
WHERE Employee.Salary > Manager.Salary
```
<br>

> [문제 링크](https://leetcode.com/problems/rising-temperature/submissions/)
```sql
SELECT today.id as Id
FROM Weather AS today
    INNER JOIN Weather as yesterday ON today.recordDate = DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY)
WHERE yesterday.temperature < today.temperature
```



<br>

## ✅ SQL : `UNION`
> [실습 링크](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_where) <br>
> [문제 링크](https://www.hackerrank.com/challenges/symmetric-pairs/problem?h_r=internal-search)


### - `UNION` 
* 두 테이블을 위아래로 `중복 데이터를 제거하고` 연결

```sql
-- Products 테이블에서 Price가 5 이하 또는 200 이상인 상품들만 출력
SELECT *
FROM Products
WHERE price <= 5

UNION

SELECT *
FROM Products
WHERE price >= 200
```

> * `MySQL` 의 경우 `FULL OUTER JOIN`을 지원하지 않음
> * `LEFT JOIN`과 `RIGHT JOIN`을 `UNION`함으로써 구현


<br>

### - `UNION ALL`
* 두 테이블을 위아래로 `중복 데이터를 제거하지 않고` 연결



```sql
SELECT x, y
FROM Functions
WHERE x = y
GROUP BY x, y
HAVING COUNT(*) = 2

UNION

SELECT f1.x, f1.y
FROM Functions as f1
    INNER JOIN Functions AS f2 ON f1.x = f2.y AND f1.y = f2.x 
WHERE f1.x < f1.y
ORDER BY x
```



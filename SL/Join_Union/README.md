# 🦁 TIL

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


<br>


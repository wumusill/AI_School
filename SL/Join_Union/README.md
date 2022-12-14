# ๐ฆ TIL

## โ SQL : `Join`
> [SQL Joins Visualizer](https://sql-joins.leopard.in.ua/) <br>
> [์ค์ต ๋งํฌ](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) <br>
> [๋ฌธ์  ๋งํฌ](https://www.hackerrank.com/challenges/african-cities/problem?h_r=internal-search)

### - `INNER JOIN`
* A์ B์ ๊ต์งํฉ
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
* A์ B์ ์ผ์ชฝ ๊ธฐ์ค ํฉ์งํฉ
```sql
SELECT * 
FROM Customers
	LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
```

> `RIGHT JOIN` ์ ๋ฐ๋๋ก ์ค๋ฅธ์ชฝ ๊ธฐ์ค ํฉ์งํฉ <br>
> ๋ณดํต ์์๋ฅผ ๋ฐ๊ฟ `LEFT JOIN`์ ๋ง์ด ์




<br>

### - `SELF JOIN`

* ์๊ธฐ ์์ ์ `JOIN`
> [๋ฌธ์  ๋งํฌ](https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/)

```sql
SELECT Employee.name as Employee
FROM Employee
    INNER JOIN Employee as Manager ON Employee.managerId = Manager.id
WHERE Employee.Salary > Manager.Salary
```
<br>

> [๋ฌธ์  ๋งํฌ](https://leetcode.com/problems/rising-temperature/submissions/)
```sql
SELECT today.id as Id
FROM Weather AS today
    INNER JOIN Weather as yesterday ON today.recordDate = DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY)
WHERE yesterday.temperature < today.temperature
```



<br>

## โ SQL : `UNION`
> [์ค์ต ๋งํฌ](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_where) <br>
> [๋ฌธ์  ๋งํฌ](https://www.hackerrank.com/challenges/symmetric-pairs/problem?h_r=internal-search)


### - `UNION` 
* ๋ ํ์ด๋ธ์ ์์๋๋ก `์ค๋ณต ๋ฐ์ดํฐ๋ฅผ ์ ๊ฑฐํ๊ณ ` ์ฐ๊ฒฐ

```sql
-- Products ํ์ด๋ธ์์ Price๊ฐ 5 ์ดํ ๋๋ 200 ์ด์์ธ ์ํ๋ค๋ง ์ถ๋ ฅ
SELECT *
FROM Products
WHERE price <= 5

UNION

SELECT *
FROM Products
WHERE price >= 200
```

> * `MySQL` ์ ๊ฒฝ์ฐ `FULL OUTER JOIN`์ ์ง์ํ์ง ์์
> * `LEFT JOIN`๊ณผ `RIGHT JOIN`์ `UNION`ํจ์ผ๋ก์จ ๊ตฌํ


<br>

### - `UNION ALL`
* ๋ ํ์ด๋ธ์ ์์๋๋ก `์ค๋ณต ๋ฐ์ดํฐ๋ฅผ ์ ๊ฑฐํ์ง ์๊ณ ` ์ฐ๊ฒฐ



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


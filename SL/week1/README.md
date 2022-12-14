# ๐ฆ TIL

* DB์ 4๊ฐ์ง ๊ธฐ๋ฅ
    * ๊ฒ์๊ณผ ๊ฐฑ์ 
    * ๋์์ฑ ์ ์ด
    * ์ฅ์  ๋์
    * ๋ณด์


## โ ๋ฐ์ดํฐ ๊ฒ์ : SELECT

> ์ค์ต ํ๊ฒฝ : https://solvesql.com/   <br>
> DB : ๋ฐ๋ฆ์ด ์์ ๊ฑฐ ์ด์ฉ ํํฉ


### - TABLE ์ถ๋ ฅ
* `*` : ๋ชจ๋  column ์ถ๋ ฅ
* `LIMIT` : ์ถ๋ ฅ data ๊ฐ์ ์ ํ
```sql
SELECT *
FROM station
LIMIT 10;
```
<br>

### - ์กฐ๊ฑด๋ฌธ : `WHERE`
* `WHERE vs HAVING`
  * `WHERE` : `GROUP BY` ์  ๋ฐ์ดํฐ ํํฐ๋ง
  * `HAVING` : `GROUP BY` ํ ์์ฝ ์ ๋ณด ํํฐ๋ง 
  * ๊ฐ๋ฅํ๋ฉด `WHERE` ๊ตฌ๋ฌธ์์ ํํฐ๋ง ํ๋ ๊ฒ์ด ์ข์ โก๏ธ ๊ทธ๋ฃนํ ๊ณผ์ ์์ ์ฐ์ฐ๋์ด ๋ ์ ์ด์ง๊ธฐ ๋๋ฌธ
```sql
-- local์ด "๋งํฌ๊ตฌ" ์ธ row๋ค๋ง ์ถ๋ ฅ
SELECT *
FROM station
WHERE local = "๋งํฌ๊ตฌ"
LIMIT 10;
```
* ์ฟผ๋ฆฌ๋ฌธ์ด ์กฐ๊ฑด์ผ๋ก ๋ค์ด๊ฐ ์๋ ์์ : ์๋ธ ์ฟผ๋ฆฌ
```sql
SELECT *
FROM station
WHERE lat > (SELECT lat FROM station WHERE name="์์ธ๋ถ๋ถ์ง๋ฐฉ๋ฒ์");
```

<br>


### - ๋ณ์นญ ์ฌ์ฉ : `AS`
* ๋ณ์นญ์ ๋์ด์ฐ๊ธฐ๋ฅผ ํ๊ณ  ์ถ๋ค๋ฉด `" "` ๋ก ๊ฐ์ธ์ค๋ค.
```sql
SELECT name AS station_name
     , address AS 'station address'
FROM station
WHERE local = "๋งํฌ๊ตฌ";
```
> ์๋์ ๊ฐ์ด AS๋ ์๋ต์ด ๊ฐ๋ฅ <br>
> ํ์ง๋ง **๊ฐ๋์ฑ**์ ์ํด ์๋ตํ์ง ์๋๊ฑธ ๊ถ์ฅ
```sql
SELECT name station_name
     , address station_address
FROM station
WHERE local = "๋งํฌ๊ตฌ";
```


<br>


### - ์ฌ๋ฌ ์กฐ๊ฑด : `OR`, `AND`, `IN`
```sql
SELECT *
FROM station
WHERE local = "๋งํฌ๊ตฌ" OR local = "๊ด์ง๊ตฌ";
```
```sql
SELECT *
FROM station
WHERE local IN ("๋งํฌ๊ตฌ", "๊ด์ง๊ตฌ");
```

<br>

### - ์ ๋ ฌ : `ORDER BY`
* ์ค๋ฆ์ฐจ์ ์ค์  : `ASC`, ๊ธฐ๋ณธ๊ฐ์ผ๋ก ์๋ต ๊ฐ๋ฅ
* ๋ด๋ฆผ์ฐจ์ ์ค์  : `DESC`
```sql
SELECT *
FROM station
WHERE local = "๊ด์ง๊ตฌ"
ORDER BY updated_at DESC;
```
> ์ ๋ ฌ ์กฐ๊ฑด์ด ๋ ๊ฐ ์ด์์ด๋ฉด?

```sql
SELECT *
FROM station
WHERE local = "๊ด์ง๊ตฌ"
ORDER BY updated_at DESC, station_id DESC;
```

<br>

### - ๋ถ๋ถ ์กฐ๊ฑด๋ฌธ : `LIKE`
* `WHERE`์  ์์์ ๋ฌธ์์ด ์ผ๋ถ๋ถ์ ๋น๊ต
* `_` : ํ ๊ธ์๋ง์ ์๋ฏธ
* `%` : 0๊ธ์๋ถํฐ ๊ทธ ์ด์์ ์๋ฏธ
```sql
SELECT *
FROM table
-- "a"๋ฅผ ํฌํจํ ๋ฐ์ดํฐ ์ถ๋ ฅ
WHERE col LIKE "%a%"
```



<br>

### - `IS NULL`/`IS NOT NULL`
* ํ์ด๋ธ ๋ด **์๋ ฅ๋์ง ์์ ๋ฐ์ดํฐ**๋ `NULL`๋ก ์ ์ฅ
* `NULL` ๊ฐ์ ๊ฒ์ํ  ๋ `IS NULL` ์ฌ์ฉ
* `NULL` ๊ฐ์ด ์๋ ํ์ ๊ฒ์ํ  ๊ฒฝ์ฐ, `IS NOT NULL` ์ฌ์ฉ

```sql
SELECT *
FROM table
WHERE name IS NOT NULL; 
```

<br>

### - ์ ์ผ๊ฐ ์ถ๋ ฅ : `DISTINCT`

```sql
SELECT DISTINCT col
FROM TABLE;
```

<br><br>

## โ SQL ํจ์
### - `LEFT(str, len)`



### - `RIGHT(str, len)`



### - `SUBSTR(str, start, len)`
### - `CEIL()` : ์ฌ๋ฆผ 
### - `FLOOR()` : ๋ด๋ฆผ
### - `ROUND()` : ๋ฐ์ฌ๋ฆผ

<br><br>

## โ ๋ฐ์ดํฐ ๋ณ๊ฒฝ/๊ฐฑ์ 
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

## โ ์ง๊ณ ํจ์

> ์ค์ต ํ๊ฒฝ : https://solvesql.com/   <br>
> DB : Waiter's Tips

>`Null` ๊ฐ์ด ์๋ค๋ฉด ์ง๊ณ ํจ์ ์ฌ์ฉ ์ ์ ์ํด์ผ ํจ 

### - `COUNT()`
* `Null` ๊ฐ์ด ์๋ค๋ฉด
  * `COUNT(*)` : ๋ค๋ฅธ ์์ ์ฐธ์กฐํ์ฌ ๊ฐ์์ ํฌํจ
  * `COUNT(Null์ด ์๋ col)` : `Null`์ ๊ฐ์์ ํฌํจ X


* ํ์ด๋ธ์ ๋ฐ์ดํฐ ์ด ๊ฐ์
```sql
SELECT COUNT(*)
FROM tips;
```
* 10๋ถ ์ด์ ๊ฒฐ์ ํ ํ์ด๋ธ ์
```sql
SELECT COUNT(*)
FROM tips
WHERE total_bill >= 10;
```

<br>

### - `SUM()`
* `Null` ๊ฐ์ ํฌํจํ์ง ์์
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

## โ ๊ทธ๋ฃน๋ณ๋ก ์์ฝ
### - `GROUP BY`
* ๊ทธ๋ฃนํ ๊ธฐ์ค์ ๋ฐ๋์ `SELECT`์ ๋ฃ์ด์ค์ผ ํจ 
* ๋ ์ง๋ณ ๋งค์ถ์ก์ ํฉ๊ณ
```sql
SELECT day, SUM(total_bill)
FROM tips
GROUP BY day;
```

* ์์ผ, ์๊ฐ๋๋ณ๋ก ๋งค์ถ์ก์ ํฉ๊ณ 
```sql
SELECT day, time, SUM(total_bill)
FROM tips
GROUP BY day, time; 
```

<br>

### - `HAVING` : ์์ฝ ์ ๋ณด ํํฐ๋ง
* `HAVING` : `GROUP BY` ์ฐ์ฐ ๊ฒฐ๊ณผ๋ฌผ์ ํํฐ๋ง
* `WHERE` : `GROUP BY` ํ๊ธฐ ์  ํํฐ๋ง 


* ์์ผ๋ณ๋ก ์ฌ์ฑ์ ๋งค์ถ์ก ํฉ๊ณ ์ถ๋ ฅ, ๋งค์ถ์ก์ด 200๋ถ ๋ฏธ๋ง์ธ ๋ ์ ์ถ๋ ฅ์์ ์ ์ธ


```sql
SELECT day, SUM(total_bill)
FROM tips
WHERE sex = 'Female'
GROUP BY day
HAVING SUM(total_bill) >= 200;
```

* ์์ผ๋ณ๋ก ์ฌ์ฑ์ ๋งค์ถ์ก ํฉ๊ณ๋ฅผ ์ถ๋ ฅ, ๋งค์ถ์ก 200๋ถ ๋ฏธ๋ง์ ์ ์ธํ๊ณ  ๋ด๋ฆผ์ฐจ์์ผ๋ก ์ถ๋ ฅ
```sql
SELECT day
     , SUM(total_bill) AS revenue_daily
FROM tips
WHERE sex = 'Female'
GROUP BY day
HAVING revenue_daily >= 200
ORDER BY revenue_daily DESC
```
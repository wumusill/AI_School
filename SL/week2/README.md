# ๐ฆ TIL



## โ SQL ์กฐ๊ฑด๋ฌธ : `CASE & IF`
### - CASE
* `CASE`๋ก ์์ํด์ `END`๋ก ๋๋จ
```sql
/* CASE
    WHEN (A์กฐ๊ฑด) THEN (A์กฐ๊ฑด์ด True ์ผ ๋)
    WHEN (B์กฐ๊ฑด) THEN (B์กฐ๊ฑด์ด True ์ผ ๋)
    ELSE (์์ ์กฐ๊ฑด์ด ๋ชจ๋ False ์ผ ๋)
END */
```

* [๋ฌธ์  ๋งํฌ](https://www.hackerrank.com/challenges/what-type-of-triangle/problem?h_r=internal-search)

```sql
SELECT 
    CASE
        WHEN A = B AND B = C THEN "Eqilateral"
        WHEN A = B THEN "Isosceles"
    END
FROM 
    triangles;
```
* `WHEN`์ ์์ ์ค์ โผ <br>
* ์์์ ๋ฐ๋ผ ๊ฒฐ๊ณผ๊ฐ ๋ฌ๋ผ์ง
> `WHEN A = B AND B = C THEN "Eqilateral"` ์์ ๊ฒฐ์ ๋ ๋ฐ์ดํฐ๋ ๊ทธ ๋ค์ ์ฝ๋๋ก ๋์ด๊ฐ์ง ์์

<br>


### - IF
```sql
-- IF(์กฐ๊ฑด, ์กฐ๊ฑด์ด True์ผ ๋, False์ผ ๋)
```

<br>



### - Pivot 
* ๊ฒฐ๊ณผ ๊ฐ์ ๊ฐ๋ก๋ก ๋ณด๊ณ  ์ถ์ ๋ ์ฌ์ฉ
* ํ์ผ๋ก ๋์ด๋์ด ์๋ ๋ฐ์ดํฐ๋ฅผ ์ด ๋ฐฉํฅ์ผ๋ก ๋ณํํด์ ํ ๋์ ๋ณด๊ณ  ์ถ์ ๋ ์ฌ์ฉ
> [๋ฌธ์  ๋งํฌ](https://leetcode.com/problems/reformat-department-table/submissions/)

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
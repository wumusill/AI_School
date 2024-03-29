# 🦁 TIL

## ✅ `Tableau`
### - Data Literacy
* 데이터를 보고, 활용할 수 있는 능력
* 보는 것에 그치지 않고, 탐색을 통해 본인이 이해
* 다른 사람과 대화와 협업을 통해 인사이트를 공유하는 일련의 능력

### - Data Type
* 불연속형
  * 파란색 필드
  * 불연속형
  * 개별적으로 구분
  * 유한한 범위
  * 뷰에 추가하면 머리글을 추가
* 연속형
  * 초록색 필드
  * 연속형
  * 단절이 없고 끊어지지 않는 무한대 범위
  * 뷰에 추가하면 축을 추가


### - 계산된 필드
* 데이터 원본에 없는 새로운 필드를 만드는 것
* 겉으로 드러나지 않은 인사이트를 발굴하는 요소

#### 기본 계산
* 데이터 원본 세부 수준 또는 Viz 세부 수준에서 값 또는 멤버를 변환
* 수익률
```xml
SUM([수익])/SUM([매출])
```

#### LOD 식
* 계산할 세부 수준을 세부적으로 제어
* Viz의 세부 수준을 기준으로 더 세분화된 수준(INCLUDE), 덜 세분화된 수준(EXCLUDE)
* 완전히 독립적인 수준(FIXED)에서 LOD 계산
* 고객별 첫 구매일 
```xml
{FIXED [고객명] : MIN([주문 일자])}
```

#### 테이블 계산
* 테이블 계산을 사용하면 Viz 전용 세부 수준에서 값을 변환할 수 있음
* 구성 비율 
```xml
SUM([매출])/TOTAL(SUM([매출]))
```




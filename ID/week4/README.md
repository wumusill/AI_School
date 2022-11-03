# 🦁 TIL

## ✅ `parameter` vs `hyper parameter`
### - `parameter`
* 한국어로 매개변수
* 모델 내부에서 결정되는 변수
* 데이터로부터 결정됨
* 사용자에 의해서 조정되지 않음

>A model parameter is a configuration variable that is internal to the model and whose value can be estimated from data.
>
>- They are required by the model when making predictions.
>- They values define the skill of the model on your problem.
>- They are estimated or learned from data.
>- They are often not set manually by the practitioner.
>- They are often saved as part of the learned model.


### - `hyper parameter`
* 머신러닝 모델링할 때 사용자가 직접 세팅해주는 값

>A model hyperparameter is a configuration that is external to the model and whose value cannot be estimated from data.
>
>- They are often used in processes to help estimate model parameters.
>- They are often specified by the practitioner.
>- They can often be set using heuristics.
>- They are often tuned for a given predictive modeling problem.


> 가장 뚜렷한 차이점은 사용자가 직접 설정하느냐 아니냐의 차이


### - reference
* [참고 자료](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-13-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0Parameter%EC%99%80-%ED%95%98%EC%9D%B4%ED%8D%BC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0Hyper-parameter)


<br>

## ✅ FIFA 선수 이적료 예측
[데이콘 링크](https://dacon.io/competitions/open/235538/data)
* 데이터 재밌어 보여서 실습해보면서 이번 주 내용 정리 & 제출

<br>

### - 데이터 구조
* id : 선수 고유의 아이디
* name : 이름
* age : 나이
* continent : 선수들의 국적이 포함되어 있는 대륙
* contract_until : 선수의 계약기간이 언제까지인지 나타냄
* position : 선수가 선호하는 포지션 ex) 공격수, 수비수 등
* prefer_foot : 선수가 선호하는 발 ex) 오른발
* reputation : 선수가 유명한 정도 ex) 높은 수치일 수록 유명한 선수
* stat_overall : 선수의 현재 능력치
* stat_potential : 선수가 경험 및 노력을 통해 발전할 수 있는 정도
* stat_skill_moves : 선수의 개인기 능력치
* value : FIFA가 선정한 선수의 이적 시장 가격 (단위 : 유로)


### - 전처리 전 column에 대한 의견

* age
  * 일반적으로 나이가 많아질수록 이적료 하락
  * 이적료에 큰 영향을 미친다고 판단
* continent
  * 유럽 리그는 일반적으로 자국 선수 보호를 위해 쿼터제 실시
  * 하지만 이적료에 큰 영향을 미치지 않는다고 판단
* contract_until 
  * 일반적으로 남아있는 계약기간이 길수록 높은 이적료 
  * `파생변수 = 계약기간 - 현재 연도` 를 추가하고 싶었으나 데이터 작성 연도 부재, 계약기간 최신화 X
  * 현재 연도를 임의로 2019년으로 설정 
* position : 선수가 선호하는 포지션 ex) 공격수, 수비수 등
  * 일반적으로 DF, GK는 FW, MF에 비해 낮은 이적료 기록 ➡️ groupby로 확인해볼 것
  * 확인 결과, 이적료에 영향 미침
* prefer_foot : 선수가 선호하는 발 ex) 오른발
  * 이적료에 큰 영향을 미치지 않는다고 판단
* reputation : 선수가 유명한 정도 ex) 높은 수치일 수록 유명한 선수
  * 이적료에 큰 영향을 미친다고 판단
* stat_overall : 선수의 현재 능력치
* stat_potential : 선수가 경험 및 노력을 통해 발전할 수 있는 정도
  * 위 두 스탯은 파생 변수로 활용
* stat_skill_moves : 선수의 개인기 능력치
  * 영향을 미치지 않는다고 판단
  * stat_overall에 반영되어있을거라는 판단


[제출완료](https://dacon.io/competitions/open/235538/leaderboard)

* 배울 때마다 develop
# π¦ TIL

## β `parameter` vs `hyper parameter`
### - `parameter`
* νκ΅­μ΄λ‘ λ§€κ°λ³μ
* λͺ¨λΈ λ΄λΆμμ κ²°μ λλ λ³μ
* λ°μ΄ν°λ‘λΆν° κ²°μ λ¨
* μ¬μ©μμ μν΄μ μ‘°μ λμ§ μμ

>A model parameter is a configuration variable that is internal to the model and whose value can be estimated from data.
>
>- They are required by the model when making predictions.
>- They values define the skill of the model on your problem.
>- They are estimated or learned from data.
>- They are often not set manually by the practitioner.
>- They are often saved as part of the learned model.


### - `hyper parameter`
* λ¨Έμ λ¬λ λͺ¨λΈλ§ν  λ μ¬μ©μκ° μ§μ  μΈνν΄μ£Όλ κ°

>A model hyperparameter is a configuration that is external to the model and whose value cannot be estimated from data.
>
>- They are often used in processes to help estimate model parameters.
>- They are often specified by the practitioner.
>- They can often be set using heuristics.
>- They are often tuned for a given predictive modeling problem.


> κ°μ₯ λλ ·ν μ°¨μ΄μ μ μ¬μ©μκ° μ§μ  μ€μ νλλ μλλμ μ°¨μ΄


### - reference
* [μ°Έκ³  μλ£](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-13-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0Parameter%EC%99%80-%ED%95%98%EC%9D%B4%ED%8D%BC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0Hyper-parameter)


<br>

## β FIFA μ μ μ΄μ λ£ μμΈ‘
[λ°μ΄μ½ λ§ν¬](https://dacon.io/competitions/open/235538/data)
* λ°μ΄ν° μ¬λ°μ΄ λ³΄μ¬μ μ€μ΅ν΄λ³΄λ©΄μ μ΄λ² μ£Ό λ΄μ© μ λ¦¬ & μ μΆ

<br>

### - λ°μ΄ν° κ΅¬μ‘°
* id : μ μ κ³ μ μ μμ΄λ
* name : μ΄λ¦
* age : λμ΄
* continent : μ μλ€μ κ΅­μ μ΄ ν¬ν¨λμ΄ μλ λλ₯
* contract_until : μ μμ κ³μ½κΈ°κ°μ΄ μΈμ κΉμ§μΈμ§ λνλ
* position : μ μκ° μ νΈνλ ν¬μ§μ ex) κ³΅κ²©μ, μλΉμ λ±
* prefer_foot : μ μκ° μ νΈνλ λ° ex) μ€λ₯Έλ°
* reputation : μ μκ° μ λͺν μ λ ex) λμ μμΉμΌ μλ‘ μ λͺν μ μ
* stat_overall : μ μμ νμ¬ λ₯λ ₯μΉ
* stat_potential : μ μκ° κ²½ν λ° λΈλ ₯μ ν΅ν΄ λ°μ ν  μ μλ μ λ
* stat_skill_moves : μ μμ κ°μΈκΈ° λ₯λ ₯μΉ
* value : FIFAκ° μ μ ν μ μμ μ΄μ  μμ₯ κ°κ²© (λ¨μ : μ λ‘)


### - μ μ²λ¦¬ μ  columnμ λν μκ²¬

* age
  * μΌλ°μ μΌλ‘ λμ΄κ° λ§μμ§μλ‘ μ΄μ λ£ νλ½
  * μ΄μ λ£μ ν° μν₯μ λ―ΈμΉλ€κ³  νλ¨
* continent
  * μ λ½ λ¦¬κ·Έλ μΌλ°μ μΌλ‘ μκ΅­ μ μ λ³΄νΈλ₯Ό μν΄ μΏΌν°μ  μ€μ
  * νμ§λ§ μ΄μ λ£μ ν° μν₯μ λ―ΈμΉμ§ μλλ€κ³  νλ¨
* contract_until 
  * μΌλ°μ μΌλ‘ λ¨μμλ κ³μ½κΈ°κ°μ΄ κΈΈμλ‘ λμ μ΄μ λ£ 
  * `νμλ³μ = κ³μ½κΈ°κ° - νμ¬ μ°λ` λ₯Ό μΆκ°νκ³  μΆμμΌλ λ°μ΄ν° μμ± μ°λ λΆμ¬, κ³μ½κΈ°κ° μ΅μ ν X
  * νμ¬ μ°λλ₯Ό μμλ‘ 2019λμΌλ‘ μ€μ  
* position : μ μκ° μ νΈνλ ν¬μ§μ ex) κ³΅κ²©μ, μλΉμ λ±
  * μΌλ°μ μΌλ‘ DF, GKλ FW, MFμ λΉν΄ λ?μ μ΄μ λ£ κΈ°λ‘ β‘οΈ groupbyλ‘ νμΈν΄λ³Ό κ²
  * νμΈ κ²°κ³Ό, μ΄μ λ£μ μν₯ λ―ΈμΉ¨
* prefer_foot : μ μκ° μ νΈνλ λ° ex) μ€λ₯Έλ°
  * μ΄μ λ£μ ν° μν₯μ λ―ΈμΉμ§ μλλ€κ³  νλ¨
* reputation : μ μκ° μ λͺν μ λ ex) λμ μμΉμΌ μλ‘ μ λͺν μ μ
  * μ΄μ λ£μ ν° μν₯μ λ―ΈμΉλ€κ³  νλ¨
* stat_overall : μ μμ νμ¬ λ₯λ ₯μΉ
* stat_potential : μ μκ° κ²½ν λ° λΈλ ₯μ ν΅ν΄ λ°μ ν  μ μλ μ λ
  * μ λ μ€ν―μ νμ λ³μλ‘ νμ©
* stat_skill_moves : μ μμ κ°μΈκΈ° λ₯λ ₯μΉ
  * μν₯μ λ―ΈμΉμ§ μλλ€κ³  νλ¨
  * stat_overallμ λ°μλμ΄μμκ±°λΌλ νλ¨


[μ μΆμλ£](https://dacon.io/competitions/open/235538/leaderboard)

* λ°°μΈ λλ§λ€ develop
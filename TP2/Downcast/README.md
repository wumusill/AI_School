# π¦ TIL

## π Link
> [data type](https://github.com/rougier/numpy-tutorial#quick-references)

## β μ©λμ΄ ν° λ°μ΄ν° λ€λ£¨κΈ°
* λ©λͺ¨λ¦¬ μ μ½ : μ μ½μ ν΅ν΄ λ λ§μ λ°μ΄ν°λ₯Ό λΆλ¬μμ λ λ§μ΄ λΆμ 
* μ€ν λ¦¬μ§ μ μ½ : νμΌ ν¬κΈ°λ₯Ό μ€μ¬ λ λ§μ νμΌ μ μ₯

### λ©λͺ¨λ¦¬ μ μ½ β‘οΈ `downcast` 
> python0308

### - downcast

* `downcast` νκΈ° μ  μ΅μκ°, μ΅λκ°μ μ‘°ννμ¬ νμ κ²°μ 
```python
downcast : {'integer', 'signed', 'unsigned', 'float'}, default None
    If not None, and if the data has been successfully cast to a
    numerical dtype (or if the data was numeric to begin with),
    downcast that resulting data to the smallest numerical dtype
    possible according to the following rules:
```
* `df[col].dtypes.name.startswith("int")`
* `df[col] = pd.to_numeric(df[col], downcast='unsigned')`


* λ²μ£Όν ννμΌ λ categoryλ‘ μ§μ νλ©΄ λ©λͺ¨λ¦¬λ₯Ό μ’ λ ν¨μ¨μ μΌλ‘ μ¬μ© κ°λ₯
* μ΄ λ λ²μ£Όμ μκ° λλ¬΄ λ§λ€λ©΄ μ ν©νμ§ μμ μ μμ


<br>


### μ€ν λ¦¬μ§ μ μ½ (λμ€ν¬ κ³΅κ°) β‘οΈ `parquet`
> python0309

* `parquet`κ° `csv`λ³΄λ€ ν¨μ¬ μ©λμ΄ μμ


* `csv`λ ν λ¨μλ‘ λ°μ΄ν° κ΅¬λΆ
* `parquet`μ μ΄ λ¨μλ‘ λ°μ΄ν° κ΅¬λΆ
> μ΄ λ¨μ μμΆμ λμΌν λ°μ΄ν° νμμΌλ‘ μμΆμ μ λ¦¬


<br>

* λ°μ΄ν°κ° λλ¬΄ μμΌλ©΄ `csv`κ° λ μμ μ©λ
  * `csv`λ λ©ν λ°μ΄ν°λ₯Ό ν¬ν¨νκ³  μμ§ μμ
  * `parquet`λ λ©ν λ°μ΄ν°λ₯Ό ν¬ν¨νκ³  μμ
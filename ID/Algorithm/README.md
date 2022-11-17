# 🦁 Algorithm

[참고 자료](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/answers/8-algorithm.md#2-6)

## ✅ Time Complexity
* 시간 복잡도(Time Complexity) : 알고리즘에 사용되는 `연산 횟수`의 총량
* 공간 복잡도(Space Complexity) : 알고리즘에 사용되는 `메모리 공간`의 총량

<br>

* 알고리즘의 복잡도는 `점근적 표기법`으로 나타냄
  * [점근 표기법 위키백과](https://ko.wikipedia.org/wiki/%EC%A0%90%EA%B7%BC_%ED%91%9C%EA%B8%B0%EB%B2%95)
  * 어떤 함수의 증가 양상을 다른 함수와의 비교로 표현하는 수론과 해석학의 방법
  * 알고리즘의 복잡도를 단순화할 때나 무한급수의 뒷부분을 간소화할 때 쓰인다.
* 점근적 표기법에는 대표적으로 O(빅오), Ω(오메가), Θ(세타)가 있다.

<br>

* `O Notation (빅오 표기법)` : 점근적 상한선 / 최악의 경우
* `Ω Notation (오메가 표기법)` : 점근적 하한선 / 최상의 경우
* `θ Notation (세타 표기법)` : 점근적 상한선과 점근적 하한선의 교집합 / 평균의 경우
> 일반적으로 최악의 경우의 성능을 측정하는 빅오 표기법을 많이 사용


<br>


## ✅ Sorting Algorithm
[정렬 참고 영상](https://www.youtube.com/watch?v=EdIKIf9mHk0&list=PLOmdoKois7_FK-ySGwHBkltzB11snW7KQ&ab_channel=megaovermoc) <br>

### - Insert Sort
* 배열의 시작부터 끝까지 비교해가면서 적절한 위치에 삽입하는 정렬 알고리즘
* 시간 복잡도
  * 최악 : $O(N^2)$
  * 평균 : $O(N^2)$
  * 최선 : $O(N)$
1. 0번 부터 n번까지 확인
2. 왼쪽에 있는 원소가 확인 중인 원소보다 작을 때까지 왼쪽으로 이동

![](img/insert.png) <br>
[사진 출처](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheInsertionSort.html)


<br>

### - Bubble Sort 
* 시간 복잡도
  * $O(N^2)$  
1. n, (n+1) 원소 확인
2. (n+1)이 작다면 swap 하고 (n+1), (n+2) 확인
3. 정렬될 때까지 반복


![](img/bubble.png) <br>
[사진 출처](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheBubbleSort.html)

<br>


### - Merge Sort
* 리스트를 잘게 쪼갠 뒤 두 개씩 크기 비교 후 정렬
* 분리된 리스트를 재귀적으로 합쳐서 정렬 완성
* 분할된 리스트를 저장해둘 공간 때문에 메모리 소모량이 큰 편
* 시간 복잡도
  * 최악, 평균, 최선 가리지 않고 항상 일정한 속도
  * $O(N\log N)$
1. 리스트를 반으로 나눔
2. 왼쪽 리스트와 오른쪽 리스트를 각각 정렬
3. 정렬된 두 리스트를 하나의 정렬된 리스트로 합병 


![](img/merge.png) <br>
[사진 출처](https://wonjayk.tistory.com/221)


<br>


### - Quick Sort
* 대개 효율적이지만 Pivot이 잘못 선택되면(내림차순 정렬 되어 있는 경우) 시간 복잡도가 $O(N^2)$
* 파이썬 sort 메서드가 quick sort로 구현되어 있고 $O(N^2)$을 방지하고자 정렬 전 리스트를 한 번 섞어주는 것으로 알고 있음
* 시간 복잡도 
  * 최악 : $O(N^2)$
  * 평균 : $O(N\log N)$
  * 최선 : $O(N\log N)$
1. Pivot을 정한다
2. Pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽에 둔다.
3. Pivot 기준으로 Pivot은 제외하고 리스트 분할
4. 1 ~ 3 반복



<br>


### - Select Sort
* 주어진 배열 중에 최댓값을 찾아 정렬되지 않은 배열의 맨 뒤의 값과 자리를 바꿈
* 배열의 맨 뒤부터 차례로 정렬
* 시간 복잡도
  * $O(N^2)$

![](img/select.png) <br>
[사진 출처](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheSelectionSort.html)

<br>


### - Heap Sort
* `Heap` : 아래 두 조건을 만족하는 트리
  1. 완전 이진 트리, 노드의 개수가 $n$개일 때 높이 $O(lg(n))$
  2. 모든 노드는 자식 노드보다 크거나 같음 ➡️ `root node는 항상 max 값`

* `Heapify`
  * 부모, 자식 노드들을 비교 후 가장 큰 노드가 부모가 되도록 자리 변경
  * 최악은 가장 큰 노드가 leaf node인 경우
  * root node 까지 가기 위해 트리 높이만큼 비교 & 재배치 ➡️ 최악 시간 복잡도 : $O(lg(n))$

* 정렬 단계
  1. `Heapify` 로 힙 생성
  2. root node == max
  3. root node를 떼어내고 나머지 노드들로 다시 `Heapify`
  4. 노드 개수만큼 반복

* 시간 복잡도 
  * 최악 : $O(N\log N)$
  * 평균 : $O(N\log N)$
  * 최선 : $O(N\log N)$

![](img/heap.png) <br>
[사진 출처](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/answers/8-algorithm.md#2-6)
<!-- <br>

## ✅ Graph -->



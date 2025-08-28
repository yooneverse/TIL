# Display 속성
= 박스의 화면 배치

## 종류
1. Block 타입
2. Inline 타입

---

## Block 타입

### 하나의 독립된 덩어리처럼 동작하는 요소로서, 웹 페이지의 큰 구조와 단락을 만듦

## 📌 Block vs Inline 요소 정리

## 1. Block 타입

- **항상 새로운 행으로 나뉨**  
  → 한 줄 전체를 차지하며, 너비는 100%  

- **크기와 여백 관련 속성 사용 가능**  
  → `width`, `height`, `margin`, `padding` 속성을 모두 적용할 수 있음  

- **여백과 테두리에 따른 밀어냄 효과**  
  → `padding`, `margin`, `border` 값 때문에 다른 요소들이 상자로부터 떨어져 배치됨  

- **width를 지정하지 않은 경우**  
  → 자동으로 **inline 방향에서 가능한 공간 전체**를 차지  
  → 즉, 상위 컨테이너의 너비를 **100%로 채우는 것과 동일**

- **대표적인 block 타입 태그**
  - 제목 태그: `<h1>` ~ `<h6>`
  - 문단: `<p>`
  - 구역: `<div>` **대표
  - 목록: `<ul>`, `<li>`

---

## 2. Inline 타입

- **줄 바꿈 없이 한 줄 안에 배치됨**  
  → 콘텐츠 크기만큼만 차지하고, 옆 요소와 같은 줄에 나란히 배치됨

  → 텍스트의 일부에만 적용되며 문장 안 단어처럼 흐름에 따라 자연스럽게 배치됨  

- **크기 지정 불가**  
  → `width`, `height` 속성은 사용할 수 없음  
  → 대신 `margin`, `padding`은 **좌우 방향**에는 적용 가능하지만, **상하 방향**에는 레이아웃에 큰 영향을 주지 않음  

- **여백과 테두리**  
  → `padding`, `margin`, `border`를 사용할 수 있지만 block 요소처럼 상자(다른 텍스트)를 밀어내지는 않음  

- **대표적인 inline 타입 태그**
  - 글자 스타일: `<span>`, `<strong>`, `<em>`, `<b>`, `<i>`  
  - 링크: `<a>`  
  - 줄 바꿈 없는 이미지: `<img>` (단, 이미지는 자체 크기를 가짐)

## 3. Inline 타입의 대표: `<span>`

- **자체적으로 시각적 변화 없음**  
  → 스타일을 적용하기 전까지 특별한 변화가 없음  

- **텍스트 일부 조작에 유용**  
  → 문장 내 특정 단어나 구문에만 스타일을 적용할 때 사용  

- **구조에 영향 없음**  
  → block 요소처럼 줄바꿈을 일으키지 않으므로, 문서의 구조에 큰 변화를 주지 않음  

---

## 📖 개념 보충

### 🔹 block vs inline 비교
- **block 요소**: 한 줄 전체 차지, 항상 줄바꿈 발생  
- **inline 요소**: 텍스트 흐름 안에서 배치, 줄바꿈 없음  

### 🔹 실무 예시
```html
<div style="border: 1px solid black;">
  <p>나는 block 요소입니다.</p>
  <span>나는 inline 요소입니다.</span>
  <span>옆에 붙어서 나와요.</span>
</div>

<p>
  나는 <span style="color:red;">빨간 글씨</span>이고,  
  <strong>강조된 글씨</strong>는 굵게 표시돼요.  
  <a href="#">링크</a>도 inline 요소예요.
</p>
```

### Normal flow
: 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식

## 4. Inline-block 타입

- **block + inline의 혼합 특성**
  - block 요소처럼 `width`, `height`, `margin`, `padding` 속성 모두 사용 가능  
  - inline 요소처럼 옆에 나란히 배치 가능  

- **줄 바꿈 발생 안 함**

  → 여러 개의 요소가 한 줄에 나란히 놓일 수 있음  

- **다른 요소가 상자에서 밀려남**
 
  → `margin`, `padding` 및 `border`로 인하여 다른 요소가 밀려남  

- **레이아웃 구성에 유리**

  → 수평으로 나열하면서 각 항목의 크기를 직접 제어할 수 있기에,버튼, 네비게이션 메뉴, 카드 형태 UI 등에 자주 활용됨  

- **대표적인 inline-block 활용 태그**
  - `<button>`, `<input>`, `<select>`  
  - CSS에서 `display: inline-block;`을 직접 지정한 요소  

---

## 📖 개념 보충

### 🔹 Block vs Inline vs Inline-block 비교

| 구분 | Block | Inline | Inline-block |
|------|-------|--------|--------------|
| 줄바꿈 | 항상 발생 | 발생하지 않음 | 발생하지 않음 |
| width/height | 지정 가능 | 지정 불가 | 지정 가능 |
| margin/padding | 모두 적용 | 좌우만 의미 있음 | 모두 적용 |
| 차지 공간 | 부모 컨테이너 100% | 콘텐츠 크기만큼 | 콘텐츠 크기만큼 (단, 크기 지정 가능) |
| 대표 태그 | `<div>`, `<p>`, `<ul>` | `<span>`, `<a>`, `<strong>` | `<button>`, `<input>`, CSS 지정 |

---

### 🔹 실무 예시
```html
<div style="border: 1px solid black; padding:10px;">
  <p>나는 block 요소입니다.</p>

  <span style="color:red;">나는 inline 요소</span>
  <span>옆에 붙어서 나와요.</span>

  <div>
    <button style="display:inline-block; width:100px; height:30px; margin:5px;">
      버튼1
    </button>
    <button style="display:inline-block; width:100px; height:30px; margin:5px;">
      버튼2
    </button>
  </div>
</div>
```

---
## 5. None 타입

- **화면에 표시되지 않음**  
  → 요소 자체가 렌더링되지 않아 **보이지도 않고 공간도 차지하지 않음**  

- **특징**
  - `display: none;`으로 설정하면 해당 요소는 마치 DOM에서 제거된 것처럼 동작  
  - 화면에서 완전히 사라지며, 다른 요소가 그 자리를 차지  

- **활용 예시**
  - 특정 조건에서만 나타나야 하는 UI 요소 숨기기  
  - 탭 메뉴, 드롭다운, 모달 창 등에서 초기 상태를 숨길 때 사용  

```html
<p>나는 항상 보여요.</p>
<p style="display:none;">나는 None 타입이라 보이지 않아요.</p>
<p>위의 요소는 공간조차 차지하지 않음.</p>
```

---

# CSS Position

### 📌 CSS Layout과 Position 정리

## 1. CSS Layout

# 📌 CSS Layout & CSS Position 개념 정리

## 🔹 CSS Layout
- 각 요소의 **위치와 크기를 조정**하여 웹 페이지의 디자인을 결정하는 것  
- 요소들을 상하좌우로 정렬하고, 간격을 맞추고, 전체적인 페이지의 뼈대를 구성  
- **핵심 속성**: `display`  
  - block, inline, flex, grid, …  

---

## 🔹 CSS Position
- 요소를 **Normal Flow에서 제거**하여 **다른 위치로 배치**하는 것  
- 다른 요소 위에 올리거나, 화면의 특정 위치에 고정시키기 등에 사용  
- **핵심 속성**: `position`  
  - static, relative, absolute, fixed, sticky, …  

---

## 📖 Layout vs Position 비교

| 구분 | CSS Layout | CSS Position |
|------|------------|--------------|
| 정의 | 페이지의 뼈대를 만들고 요소들을 정렬하는 방식 | 요소를 Normal Flow에서 빼서 원하는 위치로 배치하는 방식 |
| 초점 | **전체 구조** | **개별 요소의 위치 제어** |
| 주요 속성 | `display` (block, inline, flex, grid 등) | `position` (static, relative, absolute, fixed, sticky 등) |
| 사용 목적 | 레이아웃을 구성 (정렬, 크기, 간격 설정) | 특정 요소를 고정, 이동, 겹치게 배치 |
| 예시 | Flexbox로 카드 레이아웃 정렬, Grid로 2차원 레이아웃 | 네비게이션 바 고정, 버튼을 화면 구석에 고정 |


## 📝 정리
- **Layout** → 페이지의 **전체 구조(틀)**  
- **Position** → 요소의 **정밀한 위치 제어(세부 조정)**  

---


# 📌 CSS Position 전체 정리

## 1. static
- 기본값으로 모든 요소는 Normal Flow(문서 흐름)에 따라 배치된다.
- `top`, `left`, `right`, `bottom` 값은 적용되지 않는다.

---

## 2. relative

- 요소는 Normal Flow에 따라 배치된다.  
- **자신의 원래 위치(static)를 기준으로 이동한다.**  
- `top`, `right`, `bottom`, `left` 속성으로 위치를 조정할 수 있다.  
- 다른 요소의 레이아웃에는 영향을 주지 않는다.  
- 요소가 차지하는 공간은 `static`일 때와 동일하다.


---

## 3. absolute
- '절대 위치'
- **가장 가까운 relative 부모 요소를 기준으로 이동**
- 만족하는 부모 요소가 없다면 body 태그를 기준으로 함
- 문서에서 요소가 차지하는 공간이 없어짐
- top, right, bottom, left 속성으로 위치 조정
- 뱃지로 쓰고 싶으면 잘라내서, 부모 속성으로 일단 기준 잡아주고 원하는 자리에 붙이기의 흐름

---
## 📌 relative vs absolute 공간 특성 비교

| 구분       | relative                                | absolute                                      |
|------------|-----------------------------------------|-----------------------------------------------|
| 공간 유지  | 원래 공간을 그대로 차지함               | 공간이 제거되어 다른 요소가 메꿔 올라감        |
| 문서 흐름  | Normal Flow에 포함됨                    | Normal Flow에서 제거됨                        |
| 시각 효과  | 시각적으로만 이동                       | 공간을 뜯어내고, 겹쳐서 자유롭게 배치 가능     |

---

## 🔎 부가 설명: "공간을 뜯어낸다"는 의미
- `absolute`는 문서의 Normal Flow에서 빠지기 때문에 **자신이 차지하던 레이아웃 상의 자리가 완전히 사라진다.**  
- 따라서 다른 요소들이 그 빈자리를 채워 올라가며, 결과적으로 해당 요소가 **시각적으로는 보이지만, 공간적 흔적은 남지 않는 상태**가 된다.  
- 즉, 요소를 "보여주되, 문서 흐름 안에서는 없는 것처럼 취급"하기 때문에 **공간을 뜯어낸다**고 표현한다.

---

## 4. fixed
- 브라우저 뷰포트(화면 전체)를 기준으로 위치가 고정된다.
- 스크롤을 내려도 요소가 항상 같은 자리에 유지된다.
- 상단 네비게이션 바, 하단 고정 버튼 등에 활용된다.

---

## 5. sticky
- relative와 fixed의 혼합 속성이다.
- 스크롤 기준점에 도달하기 전에는 relative처럼 동작하고,
- 기준점에 도달하면 fixed처럼 고정된다.
- 주로 헤더, 사이드바, 목차 등에 사용된다.

Q. 요소의 자리를 대체한다면 뒤에 있는 sticky는 자리가 이동하나요? 아니면 그대로 남아있나요?

A: 남아있되, 화면에서는 사라집니다.

---

## 📖 Position 유형 비교 요약

| 유형     | 기준                           | 특징                                   |
|----------|--------------------------------|----------------------------------------|
| static   | Normal Flow                   | 기본값, 위치 이동 불가                 |
| relative | 자기 자신                     | 원래 자리 유지 + 이동                  |
| absolute | 가장 가까운 position 지정 조상 | flow에서 제거, 겹칠 수 있음            |
| fixed    | 브라우저 뷰포트               | 스크롤에도 고정                        |
| sticky   | 스크롤 위치                   | relative ↔ fixed 혼합, 스크롤 고정 가능 |


# 📌 z-index 정리

- 정수 값을 사용해 Z축 순서를 지정한다.  
- 값이 클수록 요소가 위에 쌓이게 된다.  
- `static`이 아닌 요소에만 적용된다.  
- 기본값은 `auto`로, 부모 요소의 z-index 값에 영향을 받는다.  
- 같은 부모 내에서는 z-index 값을 비교하고, 값이 같으면 HTML 문서 순서대로 쌓인다.  
- 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없다.  

---

## 💡 TIP
- `position` 속성이 `static`(기본값)이 아닌 요소에만 z-index가 적용된다.  
- 음수 z-index 값은 요소를 부모 요소의 뒤(배경)로 보낼 때 사용할 수 있다.  

- 뱃지처럼 반드시 위에 올라와야 하는 경우에는 z-index 값을 확실한 큰 수로 부여함

---
# CSS Flexbox

- Inner display 타입
  - 박스 내부의 요소들이 어떻게 배치될지 결정
  - 속성 flex인 CSS Flexbox


- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
- 책장의 책 정리와 같음
- 공간의 배분에 따라 움직이게 되는 것

## 📌 Flexbox 구성 요소

## 🔹 main axis
- flex item들이 배치되는 Flexbox의 **주 축**(main axis)  
- 기본값은 **가로 방향**이며, `flex-direction` 속성으로 바꿀 수 있다.  
- `row` → 가로, `column` → 세로  
- main start에서 시작하여 main end 방향으로 배치하는 것이 기본값

---

## 🔹 cross axis
- main axis와 **수직을 이루는 축**  
- main axis가 가로면 cross axis는 세로,  
  main axis가 세로면 cross axis는 가로  

---

## 🔹 flex container
- Flexbox 레이아웃을 적용하는 **부모 요소**  
- `display: flex;` 또는 `display: inline-flex;`로 지정  
- flex 속성 값을 사용하여 자식 요소 Flex Item들을 배치하는 주체
- 이 컨테이너의 1차 자식 요소들이 Flex Item이 됨 

---

## 🔹 flex item
- flex container 안에 포함된 **자식 요소**  
- container의 속성(`justify-content`, `align-items`, `align-content`)에 따라 배치  
- 개별 item은 `flex` 속성(`flex-grow`, `flex-shrink`, `flex-basis`)을 가질 수 있다.  

---
# 📘 Flexbox 속성

## 1. 컨테이너 지정
- 부모 요소에 `display:flex` 또는 `display:inline-flex` 선언.
- 모든 직계 자식 요소는 자동으로 flex item이 됨.

```css
.container {
  display: flex;       /* block-level flex 컨테이너 */
  /* display: inline-flex; → inline-level flex 컨테이너 */
}

2. 방향 설정 (flex-direction)

- 아이템이 배치되는 주 축(main axis) 방향 결정.

- cross axis는 자동으로 반대축이 됨.

.container {
  flex-direction: row;           /* 기본값, 좌→우 */
  flex-direction: row-reverse;   /* 우→좌 */
  flex-direction: column;        /* 위→아래 */
  flex-direction: column-reverse;/* 아래→위 */
}

3. 줄 바꿈 설정 (flex-wrap)

아이템이 컨테이너 크기를 넘어갈 때 줄바꿈 여부 결정.
.container {
  flex-wrap: nowrap;      /* 기본값, 한 줄에 압축 */
  flex-wrap: wrap;        /* 공간 부족 시 줄 바꿈 */
  flex-wrap: wrap-reverse;/* 줄 바꿈, 반대 방향 */
}

4. 주 축 정렬 (justify-content)

- main axis 기준 아이템 정렬.
- 주축을 따라서 아이템을 정렬하고 간격 조정함
.container {
  justify-content: flex-start;   /* 기본값, 시작점으로 정렬 */
  justify-content: flex-end;     /* 끝점으로 정렬 */
  justify-content: center;       /* 주 축의 중앙으로 정렬 */
}

# 📘 Flexbox 속성 정리

## 📌 목적에 따른 속성 분류
- **배치**
  - `flex-direction` : 주 축 방향 설정
  - `flex-wrap` : 줄 바꿈 여부 설정

- **공간 분배**
  - `justify-content` : 주 축 기준 아이템 정렬
  - `align-content` : 여러 줄 간격 정렬 (wrap 시)

- **정렬**
  - `align-items` : 교차 축 기준 정렬 (한 줄)
  - `align-self` : 개별 아이템 교차 축 정렬

---

## 📌 속성 쉽게 이해하는 방법
- **justify → 주 축(main axis)**
- **align → 교차 축(cross axis)**

---

## 📌 전체 흐름 요약
1. **컨테이너 지정** → `display:flex`
2. **배치**
   - `flex-direction`
   - `flex-wrap`
3. **공간 분배**
   - `justify-content`
   - `align-content`
4. **정렬**
   - `align-items`
   - `align-self`

+ 콘텐트는 여러 줄, items는 한줄, self는 한 개
+ 움직이는 데에 교차축의 세 가지 정렬은 중요하게 생각하기
7.
flex-grow를 준만큼 균등하게 나눠서 배분, 배율은 아님!

8. flex-basis
- flex item 초기 크기 값을 지정
- width 값과 동시에 적용한 경우 flex-basis가 우선

---
# 📘 CSS Margin Collapsing (마진 상쇄)

## ✅ 개념
- 두 block 요소의 **수직 방향 margin(top/bottom)** 이 만날 때,  
  단순히 더해지는 것이 아니라 **더 큰 margin 값만 적용**되는 현상.
- 예: `20px + 20px = 40px` 이 아님 → 실제 적용 = `20px`

---

## 📌 예시
```css
.box1 {
  margin-bottom: 20px;
}
.box2 {
  margin-top: 20px;
}
```
📌 실제 두 요소 간 간격 = 20px
(마진이 겹쳐져 더 큰 값 하나만 반영됨)

📌 특징

수직 방향(block flow)에서만 발생.

수평 방향(left/right margin)에서는 발생하지 않음.

부모-자식 관계에서도 발생 가능.
→ 부모의 margin-top 과 자식의 margin-top 이 상쇄될 수 있음.

📌 상쇄 이유

일관성: 복잡한 레이아웃에서도 요소 간 간격을 단순하게 유지 가능.

단순성: 요소 간 간격을 예측하기 쉽게 만들어 관리가 용이.

📌 해결 방법

padding 또는 border 로 요소 사이에 경계 추가.

부모 요소에 overflow:hidden, display:flex, display:grid 등을 적용하면 상쇄 방지 가능.


align_items는 각 줄 안에서 몇 개건 이동
align_content 줄이 여러 개 있어야 이동이 보임


---
채팅 웹 서비스 구현
HTML, CSS, JS
React, TS(타입스크립트)


---
정확하게 어디다 쓰는지 알기
flex는 '배치를 다시 하고 싶은 영역'에 써주기
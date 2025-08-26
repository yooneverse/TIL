# 📘 CSS Display, Position, Flexbox, Margin Collapsing 정리

---

# 1. Display 속성

## 🔹 Block 타입
- 하나의 독립된 덩어리처럼 동작, 웹 페이지의 큰 구조와 단락 형성.
- **특징**
  - 항상 새로운 행으로 나뉨 → 한 줄 전체 차지, 너비 100%.
  - `width`, `height`, `margin`, `padding` 모두 적용 가능.
  - 지정하지 않으면 상위 컨테이너 너비 100% 차지.
- **대표 태그**: `<div>`, `<p>`, `<h1> ~ <h6>`, `<ul>`, `<li>`

## 🔹 Inline 타입
- 줄 바꿈 없이 한 줄 안에서 콘텐츠 크기만큼 배치.
- **특징**
  - `width`, `height` 지정 불가.
  - `margin`, `padding`은 좌우만 적용, 상하는 큰 영향 없음.
- **대표 태그**: `<span>`, `<strong>`, `<em>`, `<a>`, `<img>`

## 🔹 Inline-block 타입
- Block + Inline 혼합 특성.
  - 크기 지정 가능, 옆으로 나란히 배치.
  - 버튼, 네비게이션 메뉴, 카드 UI 등에 활용.
- **대표 태그**: `<button>`, `<input>`, `<select>`

## 🔹 None 타입
- `display:none;` → 화면에 표시되지 않고 공간도 차지하지 않음.
- UI 초기 상태 숨김 등에 활용.

---

# 2. CSS Layout vs Position

## 🔹 Layout
- 페이지의 뼈대를 구성, 요소 정렬과 크기 결정.
- **핵심 속성**: `display`

## 🔹 Position
- 요소를 Normal Flow에서 제거해 원하는 위치에 배치.
- **핵심 속성**: `position`

| 구분 | CSS Layout | CSS Position |
|------|------------|--------------|
| 정의 | 전체 페이지 뼈대 | 요소를 흐름에서 제거해 위치 지정 |
| 초점 | 전체 구조 | 개별 요소 위치 |
| 속성 | display | position |
| 예시 | flex, grid | fixed nav, 배지, 모달 |

---

# 3. CSS Position

## static
- 기본값, Normal Flow에 따라 배치.
- `top`, `left` 등 위치 속성 적용 불가.

## relative
- 자신의 원래 위치를 기준으로 이동.
- 원래 자리 유지 + 이동.

## absolute
- 가장 가까운 `position` 지정 부모 기준으로 이동.
- 문서 흐름에서 제거 → "공간을 뜯어낸다".

## fixed
- 브라우저 뷰포트 기준 고정.
- 스크롤에도 위치 유지.

## sticky
- relative + fixed 혼합.
- 스크롤 기준점 전까지는 relative, 이후 fixed처럼 동작.

| 유형 | 기준 | 특징 |
|------|------|------|
| static | Normal Flow | 기본값, 이동 불가 |
| relative | 자기 자신 | 자리 유지 + 이동 |
| absolute | 가까운 조상 | 흐름에서 제거, 겹침 가능 |
| fixed | 뷰포트 | 스크롤 고정 |
| sticky | 스크롤 | 상대적 → 고정 |

---

# 4. z-index
- Z축 순서 지정, 값이 클수록 위에 쌓임.
- `static`이 아닌 요소에만 적용.
- 부모 z-index보다 높을 수 없음.
- 음수 값 → 부모 뒤로 배치 가능.

---

# 5. CSS Flexbox

## 🔹 기본 개념
- 1차원 레이아웃 (행 또는 열).
- `display:flex` → flex container 지정.
- 자식 요소는 flex item.

## 🔹 구성 요소
- **main axis**: 주 축 (기본 가로).
- **cross axis**: 주 축에 수직.
- **flex container**: 부모 요소.
- **flex item**: 자식 요소.

---

## 📘 Flexbox 속성

### 1. 컨테이너 지정
```css
.container { display:flex; }
```

### 2. 방향 설정 (flex-direction)
```css
.container {
  flex-direction: row;        /* 기본 */
  flex-direction: row-reverse;
  flex-direction: column;
  flex-direction: column-reverse;
}
```

### 3. 줄 바꿈 (flex-wrap)
```css
.container {
  flex-wrap: nowrap;   /* 기본 */
  flex-wrap: wrap;
  flex-wrap: wrap-reverse;
}
```

### 4. 주 축 정렬 (justify-content)
```css
.container {
  justify-content: flex-start; /* 기본 */
  justify-content: flex-end;
  justify-content: center;
  justify-content: space-between;
  justify-content: space-around;
  justify-content: space-evenly;
}
```

### 5. 여러 줄 정렬 (align-content)
```css
.container {
  align-content: stretch; /* 기본 */
  align-content: flex-start;
  align-content: flex-end;
  align-content: center;
  align-content: space-between;
  align-content: space-around;
  align-content: space-evenly;
}
```

### 6. 교차 축 정렬 (align-items)
```css
.container {
  align-items: stretch; /* 기본 */
  align-items: flex-start;
  align-items: flex-end;
  align-items: center;
  align-items: baseline;
}
```

### 7. 개별 아이템 정렬 (align-self)
```css
.item {
  align-self: auto; /* 기본 */
  align-self: flex-start;
  align-self: flex-end;
  align-self: center;
  align-self: baseline;
  align-self: stretch;
}
```

---

## 📌 속성 분류 & 이해
- **배치**: `flex-direction`, `flex-wrap`
- **공간 분배**: `justify-content`, `align-content`
- **정렬**: `align-items`, `align-self`

👉 `justify` → 주 축, `align` → 교차 축.

---

# 6. CSS Margin Collapsing (마진 상쇄)

## 개념
- 수직 margin이 만날 때 합산되지 않고 **더 큰 값만 적용**.

예: `20px + 20px` → 실제 간격 `20px`

## 예시
```css
.box1 { margin-bottom:20px; }
.box2 { margin-top:20px; }
```
📌 실제 간격 = `20px`

## 특징
- 수직 방향에서만 발생.
- 수평 margin에는 적용되지 않음.
- 부모-자식 관계에서도 발생 가능.

## 이유
- **일관성**: 간격을 단순하게 유지.
- **단순성**: 예측·관리 용이.

## 해결 방법
- `padding`이나 `border`로 분리.
- 부모에 `overflow:hidden`, `display:flex`, `display:grid` 적용.


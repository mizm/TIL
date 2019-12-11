# Android Studio 기본 구조

####   "안드로이드 프로젝트는 "application"위에 "activity"가 실행되는 구조이다."

- manifests : "AndroidManifest.xml" 안드로이드 어플리케이션을 구돟하는데 필요한 설정값을 관리
  - package = 패키지 표시
  - icon = 앱 아이콘 설정
  - label = 앱 이름
- java : 클래스 관리 `Activity 파일과 Xml파일은 언제나 한쌍이다.`
  - MainActivity.java
- res : Resource 폴더
  - XML :   xml 파일은 우리가 눈에 보이는 UI를 구현하는 파일입니다. 디자이너로 부터 받은 디자인을 구현할때 xml파일을 만들면 됨
- 단축키
  1. **Search everything(including code and menus)(Press Shift twice)** : 정말이지 유용한 기능이다. IDE가 인덱싱이 얼마나 잘되어 있는지 알 수 있다. 원하는 모든 것을 찾을 수 있고 Shift 키를 두번 누르면 되기 때문에 접근성도 뛰어나고 정말 강추하는 단축키.
  2. **Find(Control + F)** : 현재 파일 내에서 검색을 제공한다.
  3. **Find next(F3)** : 현재 파일 내에서 검색을 제공하고 F3을 계속 누르면 매칭 되는 위치를 위에서 아래로 하나씩 이동된다.
  4. **Find previous(Shift + F3)** : Find next의 반대라고 생각하면 된다. 아래에서 위로 이동된다.
  5. **Replace(Control + R)** : 예를 들어 ‘Text’라고 검색을 하고 ‘Text’ → ‘Text2’ 로 변경하고자 할 때 사용된다. find and replace로 이해하면 된다.
  6. **Find action(Control + Shift + A)** : IDE에서 제공하는 다양한 Action 들에 대한 단축키.
  7. **Search by symbol name(Control + Alt + Shift + N)** : Android에서 R로 생성되는 symbol만 검색하는 단축키.
  8. **Find class(Control + N)** : 이름에서 유추가 되겠지만 현재 프로젝트내에서 Class파일만 검색하는 단축키.
  9. **Find file(instead of class)(Control + Shift + N)** : 현재 프로젝트의 라이브러리에 있는 class까지 검색하는 단축키.
  10. **Find in path(Control + Shift + F)** : 검색 조건, 검색 범위, 검색 결과 등을 설정할수 있는 검색 단축키.
  11. **Open file structure pop-up(Control + F12)** : 현재 파일에 대한 Structure를 작은 팝업에 보여주는 단축키다. Structure 탭을 끄고 개발한다면 유용한 단축키.
  12. **Navigate between open editor tabs(Alt + Right/Left Arrow)** : Editor창과는 무관하고 Project, Packages, Android 등의 탭 등을 빠르게 변환해주는 단축키.
  13. **Jump to source(F4 / Control + Enter)** : 자주 사용되는 단축키 중 하나다. 소스를 분석할 때 유용.
  14. **Open current editor tab in new window(Shift + F4)** : 현재 파일을 새로운 에디터창에 로드한다. 별다른 기능 없는 아주 심플한 에디터 창이다.
  15. **Recently opened files pop-up(Control + E)** : 최근 이용한 파일들의 목록을 제공하는 단축키다.
  16. **Recently edited files pop-up(Control + Shift + E)** : 최근 편집했던 파일들의 목록을 제공하는 단축키다. 최근에 어떤 파일들을 수정했는지 히스토리를 알기 쉽다.
  17. **Go to last edit location(Control + Shift + Backspace)** : 마지막으로 코드를 수정했던 위치로 이동한다.
  18. **Close active editor tab(Control + F4)** : 현재 열려있는 파일을 닫는다. 이부분은 상당히 불만족스럽다. 자주 사용되어야 하는 기능임에도 불구하고 사용성 및 접근성이 전혀 고려가 안된 단축키다. Control + W가 아니라니.. Eclipse나 브라우저 등도 기본적으로 탭을 닫을때 Control + W 를 이용한다.
  19. **Return to editor window from a tool window(ESC)** : 이 기능은 editor창이 아닌 다른 window영역에 포커싱을 하면 editor창의 커서가 없어지는데 이 단축키를 이용하면 다시 editor창에 포커싱이 가고 커서가 나타난다.
  20. **Hide active or last active tool window(Shift + ESC)** : 별 쓸모도 없고 사용하기 불편하다. 그냥 활성화 되있거나 마지막에 사용한 tool window를 닫아주는 단축키.
  21. **Go to line(Control + G)** : Editor창에 line number를 보이게 하고 쓰면 가끔 유용하다. 입력된 창에 line number를 입력하고 엔터치면 소스코드의 해당 line으로 이동한다.
  22. **Open type hierarchy(Control + H)** : 선택된 class 등의 계층구조를 펼쳐서 보여주는 단축키.
  23. **Open method hierarchy(Control + Shift + H)** : 선택된 method의 계층구조를 펼쳐서 보여주는 단축키. 소스 분석이나 흐름등을 파악할 때 유용하다.
  24. **Open call hierarchy(Control + Alt + H)** : 선택된 method의 호출구조를 파악할때 유용하다. 어디서 호출되는지 펼쳐서 보여주는 단축키.
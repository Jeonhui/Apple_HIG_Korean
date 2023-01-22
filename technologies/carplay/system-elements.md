# **[technologies-carplay] system-elements**

## **Action sheets**

An action sheet is a specific style of alert that slides up from the bottom of the screen in response to a control or action, and presents a set of two or more choices related to the current context.
> 작업 시트는 컨트롤 또는 액션에 응답하여 화면 하단에서 위로 이동하고 현재 컨텍스트와 관련된 두 개 이상의 선택 항목 집합을 표시하는 특정 유형의 경고입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ActionSheet_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ActionSheet_2x.png)

**Avoid displaying action sheets in CarPlay.** Action sheets disrupt the user experience and increase the complexity of your app. It's fine to offer action sheets on iPhone, but avoid displaying them in CarPlay.
> CarPlay에 작업 시트를 표시하지 마십시오. 작업 시트는 사용자 경험을 방해하고 앱의 복잡성을 증가시킵니다. iPhone에서 액션 시트를 제공하는 것은 좋지만, CarPlay에 표시하는 것은 피하세요.
>




For related design guidance, see [Alerts](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#alerts).

# **Activity indicators**

Don’t show a static or an empty screen while your app loads content. Use an activity indicator to let people know your app isn’t stalled.
> 앱이 콘텐츠를 로드하는 동안 정적 또는 빈 화면을 표시하지 마십시오. 활동 표시기를 사용하여 앱이 중지되지 않았음을 사람들에게 알립니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Activity_Spinner_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Activity_Spinner_2x.png)

**If it’s helpful, provide useful information while waiting for a task to complete.** Include a label above an activity indicator to give extra context. Avoid vague terms like loading because they don’t usually add any value.
> 도움이 될 경우 작업이 완료될 때까지 기다리는 동안 유용한 정보를 제공하십시오. 추가 컨텍스트를 제공하려면 작업 표시기 위에 레이블을 포함하십시오. 일반적으로 값을 추가하지 않으므로 로드와 같은 모호한 용어는 사용하지 마십시오.
>




For developer guidance, see [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview).

# **Alerts**

Alerts convey important information related to the state of your app. An alert consists of a title, an optional message, and one or more buttons. Aside from these configurable elements, the visual appearance of an alert is static and can’t be customized.
> 알림은 앱 상태와 관련된 중요한 정보를 전달합니다. 알림은 제목, 선택적 메시지 및 하나 이상의 단추로 구성됩니다. 이러한 구성 가능한 요소 외에도 경고의 시각적 모양은 정적이므로 사용자 지정할 수 없습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Alert_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Alert_2x.png)

**Minimize alerts.** Alerts disrupt the user experience. Use alerts only for important situations like notifying people about problems. The infrequency of alerts helps ensure that people take them seriously.
> 경고를 최소화합니다. 경고는 사용자 환경을 방해합니다. 문제에 대해 사람들에게 알리는 것과 같은 중요한 상황에만 경고를 사용합니다. 경고의 빈도가 적다는 것은 사람들이 경고를 심각하게 받아들이도록 하는 데 도움이 됩니다.
>




For developer guidance, see [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller).

### **Alert titles and messages**

**Write short, descriptive, multiword alert titles.** The less text people have to read onscreen, the better. Try to craft a title that avoids adding extra text as a message. Because single-word titles rarely provide useful information, consider asking a question or using short sentences. Whenever possible, keep titles to a single line. Use sentence-style capitalization and appropriate punctuation for complete sentences. Don’t use ending punctuation for sentence fragments.
> 짧고 설명적인 다중 단어 경고 제목을 작성합니다. 화면에서 사람들이 읽어야 할 텍스트가 적을수록 좋습니다. 메시지에 추가 텍스트를 추가하지 않도록 제목을 만드십시오. 단일 단어 제목은 유용한 정보를 제공하는 경우가 거의 없기 때문에 질문을 하거나 짧은 문장을 사용하는 것을 고려하십시오. 가능할 때마다 제목을 한 줄로 유지하십시오. 완전한 문장을 위해 문장 스타일의 대문자와 적절한 구두점을 사용하세요. 문장 조각에는 끝 문장 부호를 사용하지 마십시오.
>




**If you must provide a message, write short, complete sentences.** Try to keep messages short enough to fit on one or two lines to prevent scrolling. Use sentence-style capitalization and appropriate punctuation.
> 만약 당신이 메시지를 제공해야 한다면, 짧고 완전한 문장을 써라. 스크롤을 방지하기 위해 메시지를 한 줄 또는 두 줄에 맞게 충분히 짧게 유지하도록 노력하라. 문장 형식의 대문자와 적절한 구두점을 사용하십시오.
>




**Avoid sounding accusatory, judgmental, or insulting.** People know that alerts notify them about problems and dangerous situations. As long as you use a friendly tone, it’s better to be negative and direct than positive and oblique. Avoid pronouns such as *you*, *your*, *me*, and *my*, which are sometimes interpreted as insulting or patronizing.
> 비난적이거나, 판단적이거나, 모욕적으로 들리는 것을 피하라. 사람들은 경보가 문제와 위험한 상황에 대해 그들에게 알려준다는 것을 안다. 친근한 어조를 사용하는 한 긍정적이고 비스듬한 것보다는 부정적이고 직접적인 것이 좋다. 당신, 당신, 나, 그리고 나와 같은 대명사들은 때때로 모욕적이거나 잘난 체하는 것으로 해석되는 것을 피하세요.
>




**Avoid explaining the alert buttons.** If your alert text and button titles are clear, you don't need to explain what the buttons do. In rare cases where you must provide guidance, use the word *tap*, preserve capitalization when referencing buttons, and don’t enclose button titles in quotes.
> 경고 단추에 대해 설명하지 마십시오. 경고 텍스트와 단추 제목이 명확하면 단추의 기능을 설명할 필요가 없습니다. 지침을 제공해야 하는 드문 경우에는 탭이라는 단어를 사용하고, 단추를 참조할 때 대문자를 유지하며, 단추 제목을 따옴표로 묶지 마십시오.
>




### **Alert buttons**

**Generally, use two-button alerts.** Two-button alerts provide an easy choice between two alternatives. Single-button alerts inform, but give no control over the situation. Alerts with three or more buttons create complexity and can require scrolling, which is a bad user experience. If you need more than two choices, consider using an action sheet instead. See [Action sheets](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#action-sheets).
> 일반적으로 두 버튼 경보를 사용합니다. 두 버튼 경보는 두 가지 대안 중에서 쉽게 선택할 수 있습니다. 버튼 하나로 알림을 표시하지만 상황을 제어할 수는 없습니다. 세 개 이상의 단추가 있는 알림은 복잡성을 유발하고 스크롤이 필요할 수 있으며, 이는 좋지 않은 사용자 환경입니다. 세 가지 이상의 옵션이 필요한 경우 대신 수행 시트를 사용하는 것을 고려하십시오. 작업 시트를 참조하십시오.
>




**Give alert buttons succinct, logical titles.** The best button titles consist of one or two words that describe the result of selecting the button. Use title-style capitalization and no ending punctuation. To the extent possible, use verbs and verb phrases that relate directly to the alert title and message. Use *OK* for simple acceptance. Avoid using *Yes* and *No*.
> 경고 단추에 간결하고 논리적인 제목을 지정합니다. 최상의 단추 제목은 단추를 선택한 결과를 설명하는 한 두 단어로 구성됩니다. 제목 스타일의 대소문자를 사용하고 끝맺음 구두점을 사용하지 마십시오. 가능한 한 경고 제목 및 메시지와 직접 관련된 동사 및 동사 구를 사용하십시오. 단순 승인의 경우 확인을 사용합니다. 예 및 아니요를 사용하지 마십시오.
>




**Place commonly used buttons on the right and Cancel buttons on the left.** Typically, buttons people are most likely to tap are on the right. Cancel buttons should always be on the left.
> 일반적으로 사용되는 단추는 오른쪽에, 취소 단추는 왼쪽에 배치합니다. 일반적으로 사람들이 가장 많이 누르는 단추는 오른쪽에 있습니다. 취소 버튼은 항상 왼쪽에 있어야 합니다.
>




**Label cancellation buttons appropriately.** A button that cancels an alert’s action should always be labeled Cancel.
> 경고의 작업을 취소하는 단추에는 항상 취소라는 레이블을 붙여야 합니다.
>




**Identify destructive buttons.** If an alert button results in a destructive action, such as deleting content, set the button’s style to Destructive so that it gets appropriate formatting by the system. For developer guidance, see the [UIAlertActionStyleDestructive](https://developer.apple.com/documentation/uikit/uialertactionstyle/uialertactionstyledestructive) constant of [UIAlertAction](https://developer.apple.com/documentation/uikit/uialertaction). Additionally, provide a Cancel button so people can safely opt out of the destructive action. Make the Cancel button bold by marking it as the default button.
> 파괴 단추를 식별합니다. 경고 단추를 누르면 내용 삭제와 같은 파괴 작업이 발생할 경우 단추의 스타일을 파괴로 설정하여 시스템에서 적절한 형식으로 지정합니다. 개발자 지침은 UIAlertAction의 UIAlertActionStyle파괴 상수를 참조하십시오. 또한 사용자가 안전하게 파괴 작업에서 벗어날 수 있도록 취소 버튼을 제공하십시오. 취소 단추를 기본 단추로 표시하여 굵게 표시합니다.
>




**Allow the Home button to cancel alerts.** Tapping Home while an alert is visible exits the app. It should also produce the same effect as tapping the Cancel button—that is, the alert is dismissed without performing any action. If your alert doesn’t have a Cancel button, consider implementing a cancel action in your code that runs when the Home button is tapped.
> 홈 버튼을 사용하여 알림을 취소할 수 있습니다. 알림이 표시된 상태에서 홈을 누르면 앱이 종료됩니다. 또한 Cancel(취소) 버튼을 누르는 것과 동일한 효과가 나타나야 합니다. 즉, 작업을 수행하지 않고 경고가 무시됩니다. 경고에 취소 단추가 없는 경우 홈 단추를 누를 때 실행되는 코드에서 취소 작업을 구현하는 것이 좋습니다.
>




# **Buttons**

Buttons initiate app-specific actions when tapped, have customizable backgrounds, and can include a title or an icon. Although iOS provides a number of predefined button styles, CarPlay supports only the system button style.
> 버튼을 누르면 앱별 작업이 시작되고 사용자 지정 가능한 배경이 있으며 제목이나 아이콘을 포함할 수 있습니다. iOS는 여러 가지 미리 정의된 버튼 스타일을 제공하지만, CarPlay는 시스템 버튼 스타일만 지원합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Button_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Button_2x.png)

### **System buttons**

System buttons often appear in navigation bars, but may be used anywhere.
> 시스템 버튼은 탐색 모음에 나타나는 경우가 많지만 어디서나 사용할 수 있습니다.
>




**Use verbs in titles.** An action-specific title, such as Add Favorite, shows that a button is interactive and says what happens when you tap it.
> 제목에 동사를 사용합니다. 즐겨찾기 추가와 같은 동작별 제목은 단추가 대화형임을 보여주고 단추를 누르면 어떻게 되는지 알려줍니다.
>




**Use title-case for titles.** Capitalize every word except articles, coordinating conjunctions, and prepositions of four or fewer letters.
> 제목에는 제목 대소문자를 사용합니다. 기사, 조정 접속사 및 4자 이하의 전치사를 제외한 모든 단어를 대문자로 표시합니다.
>




**Keep titles short.** Overly long text can crowd your interface and may get truncated on smaller screens.
> 제목을 짧게 유지합니다. 너무 긴 텍스트는 인터페이스를 혼잡하게 만들 수 있으며 작은 화면에서 잘릴 수 있습니다.
>




**Consider adding a border or a background only when necessary.** By default, a button has no border or background. In some content areas, however, a border or background is necessary to denote interactivity. In the Phone app, bordered number keys reinforce the traditional model of making a call, and the background of the Call button provides an eye-catching target that’s easy to hit.
> 필요한 경우에만 테두리나 배경을 추가하십시오. 기본적으로 단추에는 테두리나 배경이 없습니다. 그러나 일부 콘텐츠 영역에서는 상호작용성을 나타내기 위해 테두리 또는 배경이 필요합니다. 전화 앱에서 테두리가 있는 숫자 키는 통화를 하는 전통적인 모델을 강화하고, 통화 버튼의 배경은 치기 쉬운 눈길을 끄는 표적을 제공한다.
>




For developer guidance, see the [UIButtonTypeSystem](https://developer.apple.com/documentation/uikit/uibuttontype/uibuttontypesystem) button type of [UIButton](https://developer.apple.com/documentation/uikit/uibutton).
> 개발자 지침은 UIButton의 UIButtonTypeSystem 버튼 유형을 참조하십시오.
>




# **Collections**

A collection manages an ordered set of content, such as a set of Internet radio station logos, and presents it in a highly visual layout. Because a collection doesn’t enforce a strictly linear format, it’s particularly well-suited to displaying items that vary in size. Generally speaking, collections are ideal for showing off image-based content. Optionally, implement backgrounds and other decorative views to visually distinguish subsets of items.
> 컬렉션은 인터넷 라디오 방송국 로고 세트와 같은 순서가 지정된 콘텐츠 세트를 관리하고 시각적인 레이아웃으로 표시합니다. 컬렉션은 엄격하게 선형 형식을 적용하지 않기 때문에 크기가 다양한 항목을 표시하는 데 특히 적합합니다. 일반적으로, 컬렉션은 이미지 기반 콘텐츠를 보여주기에 이상적입니다. 또는 배경 및 기타 장식 보기를 구현하여 항목의 하위 집합을 시각적으로 구분할 수 있습니다.
>




Collections support both interactivity and animation. By default, you can tap to select, touch and hold to edit, and swipe to scroll. If your app requires it, you can add more gestures for custom actions. Within a collection, animations can be enabled whenever items are inserted, deleted, or reordered, and custom animations are also supported.
> 컬렉션은 상호작용과 애니메이션을 모두 지원합니다. 기본적으로 탭하여 선택하고 길게 눌러 편집하고 스와이프하여 스크롤할 수 있습니다. 앱에 필요한 경우 사용자 지정 작업에 대한 제스처를 추가할 수 있습니다. 컬렉션 내에서 항목을 삽입, 삭제 또는 재정렬할 때마다 애니메이션을 활성화할 수 있으며 사용자 지정 애니메이션도 지원됩니다.
>




**Avoid creating radical new designs when a standard row or grid layout is sufficient.** A collection should enhance the user experience, not become the center of attention. Make it easy to select an item. If it’s hard to tap an item in your collection, people will get frustrated and lose interest before reaching the content they want. Use adequate padding around content to keep the layout clean and prevent overlapping.
> 표준 행 또는 그리드 레이아웃이 충분할 때는 급진적인 새 설계를 작성하지 마십시오. 컬렉션은 사용자 경험을 향상시켜야 하며 관심의 대상이 되어서는 안 됩니다. 항목을 쉽게 선택할 수 있도록 합니다. 컬렉션의 항목을 탭하는 것이 어렵다면, 사람들은 원하는 콘텐츠에 도달하기 전에 좌절하고 흥미를 잃을 것입니다. 내용 주위에 적절한 패딩을 사용하여 레이아웃을 깨끗하게 유지하고 겹치지 않도록 합니다.
>




**Consider using a table instead of a collection for text.** It’s generally simpler and more efficient to view and digest textual information when it’s displayed in a scrollable list.
> 일반적으로 텍스트 정보가 스크롤 가능한 목록에 표시될 때 텍스트 정보를 보고 요약하는 것이 더 간단하고 효율적입니다.
>




**Use caution when making dynamic layout changes.** The layout of a collection can be changed at any time. If you dynamically change the layout while people are viewing and interacting with it, be sure the change makes sense and is easy to track. Unmotivated layout changes can make your app seem unpredictable and difficult to use. If context is lost due to a layout change, people are likely to feel like they’re no longer in control.
> 동적 레이아웃을 변경할 때는 주의하십시오. 컬렉션의 레이아웃은 언제든지 변경할 수 있습니다. 사용자가 레이아웃을 보고 상호 작용하는 동안 레이아웃을 동적으로 변경할 경우 변경 내용이 타당하고 추적하기 쉽도록 하십시오. 의도하지 않은 레이아웃 변경은 앱을 예측할 수 없고 사용하기 어렵게 만들 수 있습니다. 레이아웃 변경으로 인해 컨텍스트가 손실되면 사람들은 더 이상 제어할 수 없다고 느낄 가능성이 있습니다.
>




For developer guidance, see [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview).

# **Labels**

A label describes an onscreen interface element or provides a short message. Labels can display any amount of static text, but are best kept short.
> 레이블은 화면 인터페이스 요소를 설명하거나 짧은 메시지를 제공합니다. 레이블은 정적 텍스트를 얼마든지 표시할 수 있지만 짧게 유지하는 것이 가장 좋습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Label_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Label_2x.png)

**Keep labels legible.** Labels can include plain or styled text. If you adjust the style of a label or use custom fonts, be sure not to sacrifice legibility.
> 레이블을 읽기 쉽게 유지합니다. 레이블에는 일반 텍스트 또는 스타일 텍스트가 포함될 수 있습니다. 레이블의 스타일을 조정하거나 사용자 지정 글꼴을 사용하는 경우 가독성이 저하되지 않도록 하십시오.
>




For developer guidance, see [UILabel](https://developer.apple.com/documentation/uikit/uilabel).

# **Navigation bars**

A navigation bar appears at the top of an app screen, and enables navigation through a series of hierarchical app screens. When a new screen is displayed, a back button, preceded by a chevron and often labeled with the title of the previous screen, appears on the left side of the bar. Sometimes, the right side of a navigation bar contains a control, such as a Search button, for interacting with the active view.
> 탐색 모음은 앱 화면 상단에 나타나며, 일련의 계층적 앱 화면을 통해 탐색할 수 있습니다. 새 화면이 표시되면 뒤로 단추가 표시되고 이전 화면의 제목이 레이블로 표시되는 경우가 많습니다. 탐색 모음의 오른쪽에 활성 보기와 상호 작용하기 위한 검색 단추와 같은 컨트롤이 있는 경우도 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Navigation_Bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Navigation_Bar_2x.png)

**Consider showing the title of the current view in the navigation bar.** In most cases, a title provides context by letting people know what they’re looking at. However, if titling a navigation bar seems redundant, you can leave the title empty. For example, the Now Playing screen in the Music app doesn’t include a title in the navigation bar because the rest of the screen provides sufficient context.
> 대부분의 경우 제목은 사용자가 보고 있는 내용을 알려줌으로써 컨텍스트를 제공합니다. 그러나 탐색 모음 제목이 중복되는 경우 제목을 비워 둘 수 있습니다. 예를 들어 음악 앱의 지금 재생 화면은 화면의 나머지 부분이 충분한 컨텍스트를 제공하기 때문에 탐색 모음에 제목을 포함하지 않습니다.
>




**Avoid crowding a navigation bar with too many controls.** In general, a navigation bar should contain no more than the view’s current title, a back button, and one or two controls for interacting with the view’s contents.
> 일반적으로 네비게이션 바는 보기의 현재 제목, 뒤로 단추 및 보기 내용과 상호 작용하는 하나 또는 두 개의 컨트롤만 포함해야 합니다.
>




**Don’t include multisegment breadcrumb paths.** The back button always performs a single action—returning to the previous screen. If you think people might get lost without the full path to the current screen, consider flattening your app’s hierarchy.
> 다중 세그먼트 빵 부스러기 경로를 포함하지 마십시오. 뒤로 단추를 누르면 항상 이전 화면으로 돌아갑니다. 만약 당신이 사람들이 현재 화면으로 가는 전체 경로 없이 길을 잃을 수 있다고 생각한다면, 당신의 앱의 계층을 평평하게 하는 것을 고려해보라.
>




**Give text-titled buttons enough room.** If your navigation bar includes multiple text buttons, the text of those buttons may appear to run together, making the buttons indistinguishable. Add separation by inserting a fixed space item between the buttons. For developer guidance, see the [UIBarButtonSystemItemFixedSpace](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace) constant value in [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem).
> 탐색 모음에 여러 개의 텍스트 단추가 있는 경우 해당 단추의 텍스트가 함께 실행되어 단추를 구분할 수 없는 것처럼 보일 수 있습니다. 버튼 사이에 고정 공간 항목을 삽입하여 분리를 추가합니다. 개발자 지침은 UIButtonItem의 UIBarButtonSystemItemFixedSpace 상수 값을 참조하십시오.
>




**Use the standard back button.** People know that the standard back button lets them retrace steps through a hierarchy of information.
> 표준 뒤로 버튼을 사용하십시오. 사람들은 표준 뒤로 버튼을 사용하여 정보 계층을 통해 단계를 추적할 수 있다는 것을 알고 있습니다.
>




For developer guidance, see [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar).

# **Scroll views**

A scroll view lets users browse content that’s larger than the visible area. As a user swipes, flicks, drags, and taps, a scroll view follows the gesture, revealing or zooming content in a way that feels natural. A scroll view itself has no appearance, but does display transient scrolling indicators as people interact with it. A scroll view can also be configured to operate in paging mode, where scrolling reveals an entirely new page of content rather than moving around the current page.
> 스크롤 보기를 사용하여 표시되는 영역보다 큰 내용을 찾아볼 수 있습니다. 사용자가 스와이프하고, 긋고, 드래그하고, 탭하면 스크롤 뷰가 제스처를 따라 자연스러운 느낌으로 콘텐츠를 표시하거나 확대합니다. 스크롤 보기 자체는 모양이 없지만 사용자가 화면과 상호 작용할 때 일시적인 스크롤 표시기를 표시합니다. 스크롤 보기는 페이징 모드에서 작동하도록 구성할 수도 있습니다. 여기서 스크롤은 현재 페이지를 이동하는 대신 완전히 새로운 콘텐츠 페이지를 표시합니다.
>




**Don’t place a scroll view inside another scroll view.** Doing so creates an unpredictable interface that’s difficult to control.
> 스크롤 보기를 다른 스크롤 보기 안에 넣지 마십시오. 이렇게 하면 제어하기 어려운 예측 불가능한 인터페이스가 생성됩니다.
>




**In general, display one scroll view at a time.** People often make large swipe gestures when scrolling, and it can be hard to avoid interacting with a neighboring scroll view on the same screen. If you need to put two scroll views on one screen, consider allowing them to scroll in different directions so one gesture is less likely to affect both views.
> 일반적으로 스크롤 뷰를 한 번에 하나씩 표시하며, 스크롤할 때 큰 스와이프 제스처를 취하는 경우가 많으며, 같은 화면에서 인접한 스크롤 뷰와 상호 작용하는 것을 피하기 어려울 수 있다. 한 화면에 두 개의 스크롤 보기를 배치해야 하는 경우 한 가지 제스처가 두 보기 모두에 영향을 미치지 않도록 다른 방향으로 스크롤할 수 있도록 허용하는 것이 좋습니다.
>




For developer guidance, see [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview).

# **Tab bars**

A tab bar appears at the top of an app screen, enabling users to quickly switch between different sections of an app. A tab bar may contain any number of tabs, but the number of visible tabs varies based on the display size. If some tabs can’t be displayed due to limited horizontal space, the final visible tab becomes a More tab, which lists additional tabs on a separate screen.
> 앱 화면 상단에 탭 바가 나타나 사용자가 앱의 다른 섹션을 빠르게 전환할 수 있습니다. 탭 표시줄에는 여러 개의 탭이 포함될 수 있지만 표시되는 탭의 수는 디스플레이 크기에 따라 다릅니다. 수평 공간이 제한되어 일부 탭을 표시할 수 없는 경우 최종적으로 표시되는 탭은 별도의 화면에 추가 탭을 나열하는 추가 탭이 됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Tab_Bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Tab_Bar_2x.png)

**In general, use a tab bar to flatten your information hierarchy.** A tab bar provides access to several peer information categories or modes at once.
> 일반적으로 정보 계층을 평평하게 하려면 탭 표시줄을 사용합니다. 탭 표시줄은 여러 피어 정보 범주 또는 모드에 한 번에 액세스할 수 있도록 제공합니다.
>




**Don’t remove or disable a tab when its function is unavailable.** If tabs are available in some cases but not in others, your app’s interface appears unstable and unpredictable. Ensure that all tabs are always enabled. Explain why a tab’s content is unavailable in the body of the tab.
> 탭을 사용할 수 없는 경우 탭을 제거하거나 사용하지 않도록 설정하지 마십시오. 탭을 사용할 수 있는 경우가 있지만 다른 경우에는 사용할 수 없는 경우 앱의 인터페이스가 불안정하고 예측할 수 없는 것으로 나타납니다. 모든 탭이 항상 활성화되어 있는지 확인합니다. 탭의 내용을 탭 본문에서 사용할 수 없는 이유를 설명합니다.
>




**Use a tab bar strictly for navigation.** Tab bar buttons should not be used to perform actions.
> 네비게이션에는 탭 바를 사용하십시오. 탭 바 단추를 사용하여 작업을 수행하면 안 됩니다.
>




**In general, use between three and five tabs.** Each additional tab reduces the tappable area for selecting a tab and increases the complexity of your app, making it harder to locate information. Although a More tab can display extra tabs, this requires additional taps and is a poor use of space. Include essential tabs only, and use the minimum tabs necessary for your information hierarchy. Too few tabs can be a problem too, as it can make your interface appear disconnected.
> 일반적으로 3개에서 5개의 탭을 사용합니다. 각 탭이 추가되면 탭을 선택하기 위한 탭 영역이 줄어들고 앱의 복잡성이 증가하여 정보를 찾기가 더 어려워집니다. 추가 탭에는 추가 탭이 표시될 수 있지만, 이 경우 추가 탭이 필요하고 공간을 제대로 사용하지 못합니다. 필수 탭만 포함하고 정보 계층에 필요한 최소 탭을 사용하십시오. 탭 수가 너무 적으면 인터페이스가 연결되지 않은 것처럼 보일 수 있기 때문에 문제가 될 수도 있습니다.
>




**Use badging to communicate unobtrusively.** You can display a badge—a red oval containing white text and either a number or an exclamation point—on a tab to indicate that new information is associated with that view or mode.
> 배지를 사용하여 눈에 띄지 않게 통신합니다. 흰색 텍스트와 숫자 또는 느낌표가 포함된 빨간색 타원형 배지를 탭에 표시하여 새 정보가 해당 보기 또는 모드와 연결되었음을 나타낼 수 있습니다.
>




For developer guidance, see [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar).

# **Tables**

A table presents data as a scrolling, single-column list of rows. Use a table to display large or small amounts of information cleanly and efficiently in the form of a list.
> 테이블은 데이터를 스크롤하는 단일 열 행 목록으로 표시합니다. 표를 사용하여 대량 또는 소량의 정보를 목록 형태로 깨끗하고 효율적으로 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Index_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Index_2x.png)

**Consider table width.** Thin tables can cause truncation and wrapping, making them hard to read and scan quickly at a distance.
> 테이블 너비를 고려하십시오. 테이블이 얇으면 잘라내기와 래핑이 발생하여 먼 거리에서 빠르게 읽고 스캔하기 어려울 수 있습니다.
>




**Begin showing table content quickly.** Don’t wait for extensive table content to load before showing something. Fill onscreen rows with textual data immediately and show more complex data—such as images—as it becomes available. This technique gives people useful information right away and increases the perceived responsiveness of your app. In some cases, showing stale, older data may make sense until fresh, new data arrives.
> 표 내용을 빨리 표시하기 시작합니다. 자세한 표 내용이 로드될 때까지 기다리지 말고 내용을 표시하십시오. 화면의 행을 텍스트 데이터로 즉시 채우고 사용할 수 있게 되면 이미지와 같은 더 복잡한 데이터를 표시합니다. 이 기술은 사람들에게 유용한 정보를 즉시 제공하고 당신의 앱의 인식된 응답성을 증가시킨다. 경우에 따라 새로운 데이터가 도착할 때까지 오래되고 오래된 데이터를 표시하는 것이 타당할 수 있습니다.
>




**Communicate progress as content loads.** If a table’s data takes time to load, show a spinning activity indicator to reassure people that your app is still running.
> 콘텐츠가 로드될 때 진행 상황을 전달합니다. 테이블의 데이터가 로드되는 데 시간이 걸리는 경우 회전 작업 표시기를 표시하여 앱이 아직 실행 중임을 사람들에게 확신시킵니다.
>




**Update table content regularly to reflect newer data, but don’t change the scrolling position.** Add new content to the beginning or end of the table, and let people scroll to it when they’re ready. Some apps display an indicator when new data has been added, and provide a control for jumping right to it.
> 테이블 콘텐츠를 정기적으로 업데이트하여 새 데이터를 반영하되 스크롤 위치는 변경하지 마십시오. 테이블의 처음이나 끝에 새 콘텐츠를 추가하고 사용자가 준비되면 스크롤할 수 있습니다. 일부 앱은 새 데이터가 추가되었을 때 표시기를 표시하고 바로 이동할 수 있는 컨트롤을 제공합니다.
>




For developer guidance, see [UITableView](https://developer.apple.com/documentation/uikit/uitableview).

### **Table rows**

You use standard table cell styles to define how content appears in table rows.
> 표준 표 셀 스타일을 사용하여 표 행에 내용이 표시되는 방식을 정의할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-default_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-default_2x.png)

**Default.** An optional image on the left side of the row, followed by a left-aligned title. It’s a good option for displaying items that don’t require supplementary information. For developer guidance, see the [UITableViewCellStyleDefault](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstyledefault) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).
> 기본값. 행 왼쪽에 있는 선택적 이미지와 왼쪽으로 정렬된 제목입니다. 보충 정보가 필요 없는 항목을 표시할 때 좋은 옵션입니다. 개발자 지침은 UITableViewCell의 UITableViewCellStyle 기본 상수를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row_sub_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row_sub_2x.png)

**Subtitle.** A left-aligned title on one line and a left-aligned subtitle on the next. This style works well in a table where rows are visually similar. The additional subtitle helps distinguish rows from one another. For developer guidance, see the [UITableViewCellStyleSubtitle](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstylesubtitle) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).
> 부제. 한 줄에 왼쪽으로 정렬된 제목과 다음 줄에 왼쪽으로 정렬된 부제. 이 스타일은 행이 시각적으로 유사한 표에서 잘 작동합니다. 추가 부제는 행을 서로 구별하는 데 도움이 됩니다. 개발자 지침은 UITableViewCell의 UITableViewCellStyle 부제 상수를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V1_2x.png)

**Value 1.** A left-aligned title with a right-aligned subtitle in a lighter font on the same line. For developer guidance, see the [UITableViewCellStyleValue1](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstylevalue1) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).
> 값 1. 같은 줄에 더 가벼운 글꼴로 오른쪽으로 정렬된 부제가 있는 왼쪽으로 정렬된 제목. 개발자 지침은 UITableViewCell의 UITableViewCellStyleValue1 상수를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V2_2x.png)

**Value 2.** A right-aligned title, followed by a left-aligned subtitle in a lighter font on the same line. For developer guidance, see [UITableViewCellStyleValue2](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstylevalue2) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).
> 값 2. 오른쪽으로 정렬된 제목 다음에 같은 줄에 더 가벼운 글꼴로 왼쪽으로 정렬된 부제가 표시됩니다. 개발자 지침은 UITableViewCell의 UITableViewCellStyleValue2 상수를 참조하십시오.
>




**Keep text succinct to avoid clipping.** Truncated words and phrases are hard to scan and decipher. Text truncation is automatic in all table cell styles, but it can present more or less of a problem depending on which cell style you use and where truncation occurs.
> 잘라내기를 방지하려면 텍스트를 간결하게 유지하십시오. 잘린 단어와 구문은 스캔하고 해독하기 어렵습니다. 텍스트 잘라내기는 모든 테이블 셀 스타일에서 자동으로 수행되지만, 사용하는 셀 스타일과 잘라내기가 발생하는 위치에 따라 다소 문제가 발생할 수 있습니다.
>




**Provide feedback when a selection is made.** People expect a row to highlight briefly when its content is tapped. Then, people expect a new view to appear or something to change, such as a checkmark appearing, that indicates a selection has been made.
> 선택할 때 피드백을 제공합니다. 사용자는 해당 내용을 누르면 행이 짧게 강조 표시됩니다. 그런 다음, 사람들은 새로운 보기가 나타나거나 선택이 이루어졌음을 나타내는 확인 표시가 나타나는 것과 같은 변경 사항을 기대합니다.
>




**Design a custom table cell style for nonstandard table rows.** Standard styles are great for use in a variety of common scenarios, but some content or your overall app design may call for a heavily customized table appearance.
> 표준이 아닌 테이블 행에 대한 사용자 지정 테이블 셀 스타일을 설계하십시오. 표준 스타일은 다양한 일반적인 시나리오에서 사용하기에 좋지만 일부 콘텐츠 또는 전체 앱 디자인은 사용자 지정된 테이블 모양을 요구할 수 있습니다.
>




For developer guidance, see [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).

# **Text views**

A text view displays multiline, styled text content. Text views can be any height and enable scrolling when the content extends outside of the view. By default, content within a text view is left-aligned and uses the system typeface in white. CarPlay doesn’t support text editing and selection.
> 텍스트 보기는 여러 줄의 스타일이 지정된 텍스트 내용을 표시합니다. 텍스트 보기는 높이와 상관없이 내용이 보기 외부로 확장될 때 스크롤을 사용할 수 있습니다. 기본적으로 텍스트 보기의 내용은 왼쪽으로 정렬되며 흰색으로 표시된 시스템 글꼴을 사용합니다. CarPlay는 텍스트 편집 및 선택을 지원하지 않습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Textview_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Textview_2x.png)

**Keep text legible.** Although you can use multiple fonts, colors, and alignments in creative ways, it’s essential to maintain the readability of your content. Be sure to test your text legibility at different times of day.
> 텍스트를 읽기 쉽게 유지합니다. 여러 글꼴, 색 및 정렬을 창의적인 방법으로 사용할 수 있지만 콘텐츠의 가독성을 유지하는 것이 중요합니다. 하루 중 다른 시간에 텍스트 가독성을 테스트하십시오.
>




For developer guidance, see [UITextView](https://developer.apple.com/documentation/uikit/uitextview).

# **Web views**

A web view loads and displays rich, static content, such as HTML embedded within your app.
> 웹 보기는 앱에 내장된 HTML과 같은 풍부한 정적 콘텐츠를 로드하고 표시합니다.
>




**Use a web view to present static content only.** Do not use a web view to display dynamic content or to offer web browsing capabilities.
> 정적 내용만 표시하려면 웹 보기를 사용하십시오. 동적 내용을 표시하거나 웹 검색 기능을 제공하려면 웹 보기를 사용하지 마십시오.
>




For developer guidance, see [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview).

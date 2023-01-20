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





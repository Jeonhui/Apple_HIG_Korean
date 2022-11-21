# **[components-presentation] action-sheets**

## An action sheet is a modal view that presents choices related to an action people initiate.
> 작업 시트는 사용자가 시작하는 작업과 관련된 선택사항을 표시하는 모달 뷰입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/action-sheet-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/action-sheet-intro-dark_2x.png)

**DEVELOPER NOTE**When you use SwiftUI, you can enable action sheet functionality in all platforms by specifying a [presentation modifier](https://developer.apple.com/documentation/swiftui/view-presentation) for a confirmation dialog. If you use UIKit, you use the [actionSheet](https://developer.apple.com/documentation/uikit/uialertcontroller/style/actionsheet) style of [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) to display an action sheet in iOS, iPadOS, and tvOS.
> 개발자 참고 스위프트를 사용할 때UI, 확인 대화 상자에 대한 프레젠테이션 수정자를 지정하여 모든 플랫폼에서 작업 시트 기능을 활성화할 수 있습니다. UIKit을 사용하면 작업을 사용합니다.iOS, iPadOS 및 TVOS에서 작업 시트를 표시하는 UIAlertController의 시트 스타일입니다.
>




# **Best practices**

**Use an action sheet — not an alert — to offer choices related to an intentional action.** For example, when people cancel the Mail message they’re editing, an action sheet provides three choices: delete the edits (or the entire draft), save the draft, or return to editing. Although an alert can also help people confirm or cancel an action that has destructive consequences, it doesn’t provide additional choices related to the action. More importantly, an alert is usually unexpected, generally telling people about a problem or a change in the current situation that might require them to act. For guidance, see [Alerts](../components/presentation/alerts).
> 사용자가 편집 중인 메일 메시지를 취소할 때 작업 시트는 편집 내용 삭제(또는 전체 초안 저장) 또는 편집으로 돌아가기의 세 가지 선택사항을 제공합니다. 경고는 또한 사람들이 파괴적인 결과를 초래하는 작업을 확인하거나 취소하는 데 도움이 될 수 있지만, 해당 작업과 관련된 추가 선택을 제공하지는 않습니다. 더 중요한 것은 경보가 일반적으로 사용자에게 조치를 취해야 할 수 있는 문제나 현재 상황의 변화에 대해 알려주는 예기치 않은 경보라는 것입니다. 자세한 내용은 경고를 참조하십시오.
>




**Use action sheets sparingly.** Action sheets give people important information and choices, but they interrupt the current task to do so. To encourage people to pay attention to action sheets, avoid using them more than necessary.
> 작업 시트를 사용하지 마십시오. 작업 시트는 사람들에게 중요한 정보와 선택 사항을 제공하지만 이를 위해 현재 작업을 방해합니다. 사람들이 작업 시트에 주의를 기울이도록 하려면 필요 이상으로 작업 시트를 사용하지 마십시오.
>




**Aim to keep titles short enough to display on a single line.** A long title is difficult to read quickly and might get truncated or require people to scroll.
> 제목을 한 줄에 표시할 수 있을 정도로 짧게 유지합니다. 긴 제목은 빨리 읽기 어렵고 잘리거나 스크롤해야 할 수 있습니다.
>




**Provide a message only if necessary.** In general, the title — combined with the context of the current action — provides enough information to help people understand their choices.
> 필요한 경우에만 메시지를 제공합니다. 일반적으로 제목은 현재 작업의 컨텍스트와 결합되어 사용자가 선택한 내용을 이해하는 데 도움이 되는 충분한 정보를 제공합니다.
>




**If necessary, provide a Cancel button that lets people reject an action that might destroy data.** Place the Cancel button at the bottom of the action sheet (or in the upper-left corner of the sheet in watchOS). A SwiftUI confirmation dialog includes a Cancel button by default.
> 필요한 경우 사용자가 데이터를 파괴할 수 있는 작업을 거부할 수 있도록 취소 단추를 제공합니다. 작업 시트의 맨 아래(또는 watchOS에서 시트의 왼쪽 위)에 취소 단추를 놓습니다. 스위프트UI 확인 대화상자에는 기본적으로 취소 버튼이 포함되어 있습니다.
>




**Make destructive choices visually prominent.** Use the destructive style for buttons that perform destructive actions, and place these buttons at the top of the action sheet where they tend to be most noticeable. For developer guidance, see [destructive](https://developer.apple.com/documentation/swiftui/buttonrole/destructive) (SwiftUI) or [UIAlertAction.Style.destructive](https://developer.apple.com/documentation/uikit/uialertaction/style/destructive) (UIKit)
> 파괴적인 선택을 시각적으로 두드러지게 한다. 파괴적인 행동을 하는 버튼에 파괴적인 스타일을 사용하고, 이 버튼들을 가장 눈에 잘 띄는 곳에 행동 시트의 맨 위에 놓는다. 개발자 지침은 파괴적(Swift)을 참조하십시오.UI) 또는 UIAlertAction.Style.Destruction(UIKit)
>




# **Platform considerations**

*No additional considerations for macOS or tvOS.*
> macOS 또는 tvOS에 대한 추가 고려사항은 없습니다.
>




# **iOS, iPadOS**

**Use an action sheet — not a menu — to provide choices related to an action.** People are accustomed to having an action sheet appear when they perform an action that might require clarifying choices. In contrast, people expect a menu to appear when they choose to reveal it.
> 메뉴가 아닌 수행 시트를 사용하여 수행과 관련된 선택사항을 제공합니다. 사람들은 명확한 선택이 필요한 수행을 수행할 때 수행 시트를 표시하는 데 익숙합니다. 이와는 대조적으로, 사람들은 메뉴를 공개하기로 선택했을 때 메뉴가 나타날 것으로 기대한다.
>




**Avoid letting an action sheet scroll.** The more buttons an action sheet has, the more time and effort it takes for people to make a choice. Also, scrolling an action sheet can be hard to do without inadvertently tapping a button.
> 작업 시트가 스크롤되지 않도록 하십시오. 단추가 많을수록 사용자가 선택하는 데 더 많은 시간과 노력이 필요합니다. 또한 작업 시트를 스크롤하는 것은 실수로 버튼을 누르지 않고는 수행하기 어려울 수 있습니다.
>




# **watchOS**

The system-defined style for action sheets includes a title, an optional message, a Cancel button, and one or more additional buttons. The appearance of this interface is different depending on the device.
> 수행 시트에 대한 시스템 정의 스타일에는 제목, 선택적 메시지, 취소 단추 및 하나 이상의 추가 단추가 포함됩니다. 이 인터페이스의 모양은 장치에 따라 다릅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/action-sheets/images/action-sheet-series-4_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/action-sheets/images/action-sheet-series-4_2x.png)

Series 4 and later

![https://developer.apple.com/design/human-interface-guidelines/components/presentation/action-sheets/images/action-sheet-series-3_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/action-sheets/images/action-sheet-series-3_2x.png)

Series 3 and earlier

Each button has an associated style that conveys information about the button’s effect. There are three system-defined button styles:
> 각 단추에는 단추의 효과에 대한 정보를 전달하는 관련 스타일이 있습니다. 세 가지 시스템 정의 버튼 스타일이 있습니다.
>




| Style | Meaning |
| --- | --- |
| Default | The button has no special meaning. |
| Destructive | The button destroys user data or performs a destructive action in the app. |
| Cancel | The button dismisses the view without taking any action. |

**Avoid displaying more than four buttons in an action sheet, including the Cancel button.** When there are fewer buttons onscreen, it’s easier for people to view all their options at once. Because the Cancel button is required, aim to provide no more than three additional choices.
> 작업 시트에 취소 단추를 포함하여 단추가 네 개 이상 표시되지 않도록 합니다. 화면에 단추 수가 적을 때 사용자는 모든 옵션을 한 번에 쉽게 볼 수 있습니다. Cancel(취소) 버튼이 필요하므로 세 가지 이상의 추가 옵션을 제공하는 것을 목표로 합니다.
>




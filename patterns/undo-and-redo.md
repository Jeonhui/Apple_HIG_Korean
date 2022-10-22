# **[patterns] undo-and-redo**

# Undo and redo gives people easy ways to reverse many types of actions, which can also help people explore and experiment safely as they learn a new interface or task.
> 실행 취소 및 다시 실행은 사람들이 새로운 인터페이스나 작업을 배울 때 안전하게 탐색하고 실험할 수 있도록 많은 유형의 작업을 되돌릴 수 있는 쉬운 방법을 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-undo-redo-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-undo-redo-intro-dark_2x.png)

People expect undo and redo to let them reverse their recent actions, so they’re likely to try undoing — often multiple times — until something changes. In a situation like this, people might not remember which of their previous actions an undo is targeting, which can lead to unintended changes and frustration. To help people remain in control, it’s essential to help people predict the outcome of undoing and redoing and to highlight the results.
> 사람들은 실행 취소와 재실행을 기대하기 때문에 무언가가 바뀔 때까지 실행 취소(종종 여러 번)를 시도할 가능성이 높습니다. 이런 상황에서, 사람들은 그들의 이전의 행동들 중 어떤 것이 실행 취소가 목표인지 기억하지 못할 수 있고, 이것은 의도하지 않은 변화와 좌절로 이어질 수 있다. 사람들이 통제력을 유지할 수 있도록 돕기 위해서는 사람들이 실행 취소와 실행의 결과를 예측하고 결과를 강조하도록 돕는 것이 필수적이다.
>




# **Best practices**

**Help people predict the results of undo and redo as much as possible.** On iPhone, for example, you can describe the result in the alert that displays when people shake the device, giving them the option of performing the undo or canceling it. If you provide undo and redo menu items, you can modify the menu item labels to identify the result. For example, a document-based app might use menu item labels like Undo Typing or Redo Bold.
> 사람들이 실행 취소와 재실행의 결과를 가능한 많이 예측할 수 있도록 도와줍니다. 예를 들어 iPhone에서는 사용자가 장치를 흔들 때 표시되는 경고에 결과를 설명하여 실행 취소 또는 취소 옵션을 제공할 수 있습니다. 실행 취소 및 다시 실행 메뉴 항목을 제공하는 경우 메뉴 항목 레이블을 수정하여 결과를 식별할 수 있습니다. 예를 들어 문서 기반 앱은 입력 취소 또는 굵게 다시 실행과 같은 메뉴 항목 레이블을 사용할 수 있습니다.
>




**Show the results of an undo or redo.** Sometimes, the most recent action that people want to undo affects content or an area that’s no longer visible. In cases like this, it’s crucial to highlight the result of each undo and redo to keep people from thinking that the action had no effect, which can lead them to perform it repeatedly. For example, if people undo after deleting a paragraph in a document area that’s no longer onscreen, you might scroll the document to show the restored paragraph.
> 실행 취소 또는 다시 실행 결과를 표시합니다. 사용자가 실행 취소하려는 가장 최근의 작업은 콘텐츠나 더 이상 볼 수 없는 영역에 영향을 미치는 경우가 있습니다. 이와 같은 경우, 각각의 실행 취소와 재실행의 결과를 강조하여 사람들이 그 조치가 효과가 없다고 생각하지 않도록 하는 것이 중요하며, 이것은 그들이 그것을 반복적으로 수행하게 할 수 있다. 예를 들어 더 이상 화면에 표시되지 않는 문서 영역의 문단을 삭제한 후 실행 취소할 경우 문서를 스크롤하여 복원된 문단을 표시할 수 있습니다.
>




**Let people undo multiple times.** Avoid placing unnecessary limits on the number of times people can undo or redo. People generally expect to undo every action they’ve performed since taking a logical step like opening a document or saving their work.
> 사람들이 여러 번 실행 취소하도록 놔두세요. 사용자가 실행 취소하거나 다시 실행할 수 있는 횟수에 불필요한 제한을 두지 마십시오. 사람들은 일반적으로 문서를 열거나 작업을 저장하는 것과 같은 논리적 단계를 수행한 후 수행한 모든 작업을 실행 취소하기를 기대합니다.
>




**Consider giving people the option to revert multiple changes at once.** In some scenarios, people might appreciate the ability to undo a batch of discrete but related actions — like incremental adjustments to a single property or attribute — so they don’t have to undo each individual adjustment. In other cases, it can make sense to give people a convenient way to undo all the changes they made since opening a document or saving their work.
> 여러 변경 사항을 한 번에 되돌릴 수 있는 옵션을 사용자에게 제공하는 것을 고려해 보십시오. 일부 시나리오에서는 단일 속성 또는 속성에 대한 증분 조정과 같이 개별적이지만 관련된 작업을 실행 취소할 수 있으므로 각 개별 조정을 실행 취소할 필요가 없습니다. 다른 경우에는 문서를 열거나 작업을 저장한 후 변경한 내용을 모두 취소할 수 있는 편리한 방법을 제공하는 것이 이치에 맞을 수 있습니다.
>




**Provide undo and redo buttons only when necessary.** People generally expect to initiate undo and redo in system-supported ways, such as choosing the items in a macOS app’s Edit menu, using keyboard shortcuts on a Mac or iPad, or shaking their iPhone. If it’s important to provide dedicated undo and redo buttons in your app, use the standard system-provided symbols and put the buttons in a familiar location, like a navigation bar or toolbar.
> 필요한 경우에만 실행 취소 및 다시 실행 버튼을 제공합니다. 사람들은 일반적으로 맥 OS 앱의 편집 메뉴에서 항목을 선택하거나 맥이나 아이패드의 키보드 단축키를 사용하거나 아이폰을 흔드는 등 시스템에서 지원하는 방식으로 실행 취소와 재실행을 시작할 것으로 예상한다. 앱에서 전용 실행 취소 및 다시 실행 버튼을 제공하는 것이 중요한 경우, 시스템에서 제공하는 표준 기호를 사용하여 탐색 모음이나 도구 모음과 같은 익숙한 위치에 버튼을 놓으십시오.
>




# **Platform considerations**

*Not supported in tvOS or watchOS.*
> tvOS 또는 시계에서 지원되지 않음OS.
>




# **iOS, iPadOS**

**Avoid redefining standard gestures for undo and redo.** For example, people can use a three-finger swipe to initiate an undo or redo, or shake their iPhone. As with all standard gestures, redefining them in your interface runs the risk of confusing people and making your experience unpredictable.
> 실행 취소 및 재실행의 표준 제스처를 재정의하지 않도록 합니다. 예를 들어, 사람들은 실행 취소나 재실행을 시작하거나 아이폰을 흔들기 위해 세 손가락으로 스와이프를 사용할 수 있다. 모든 표준 제스처와 마찬가지로 인터페이스에서 제스처를 재정의하면 사람들을 혼란스럽게 하고 사용자의 경험을 예측할 수 없게 만들 위험이 있습니다.
>




**Briefly and precisely describe the operation to be undone or redone.** The undo and redo alert title automatically includes a prefix of “Undo ” or “Redo ” (including the trailing space). You need to provide an additional word or two that describes what’s being undone or redone, to appear after this prefix. For example, you might create alert titles such as “Undo Name” or “Redo Address Change.”
> 실행 취소 또는 다시 실행할 작업에 대해 간략하고 정확하게 설명합니다. 실행 취소 및 다시 실행 경고 제목에는 자동으로 "실행 취소" 또는 "다시 실행" 접두사(후행 공간 포함)가 포함됩니다. 이 접두사 뒤에 나타나려면 실행 취소 또는 재실행하는 내용을 설명하는 단어를 추가로 한두 개 제공해야 합니다. 예를 들어, "이름 실행 취소" 또는 "주소 변경 다시 실행"과 같은 경고 제목을 만들 수 있습니다.
>




# **macOS**

**Place undo and redo commands in the Edit menu and support the standard keyboard shortcuts.** Mac users expect to find undo and redo at the top of the Edit menu; they also expect to use Command–Z and Shift–Command–Z to perform undo and redo, respectively.
> 편집 메뉴에 실행 취소 및 다시 실행 명령을 배치하고 표준 키보드 단축키를 지원합니다. Mac 사용자는 편집 메뉴의 맨 위에 실행 취소와 다시 실행이 있고, 또한 Command-Z와 Shift-Command-Z를 사용하여 실행 취소와 다시 실행이 가능합니다.
>




# **[components-menus-and-actions] menus**

## A menu reveals its options when people interact with it, making it a space-efficient way to present commands in your app or game.
> 메뉴는 사람들이 그것과 상호 작용할 때 그것의 옵션을 보여주므로 당신의 앱이나 게임에서 명령을 보여주는 공간 효율적인 방법이 됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/menus-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/menus-intro-dark_2x.png)

Menus are ubiquitous throughout the interface, so most people already know how to use them. When you use menus consistently in your app or game, it can help make your experience feel familiar and easy to learn.
> 메뉴는 인터페이스 전반에 걸쳐 어디에나 있으므로 대부분의 사람들은 이미 메뉴를 사용하는 방법을 알고 있다. 앱이나 게임에서 메뉴를 일관되게 사용하면 경험을 친숙하고 쉽게 배울 수 있습니다.
>




The system provides several types of menus that support different use cases, such as:
> 시스템은 다음과 같은 다양한 사용 사례를 지원하는 여러 가지 유형의 메뉴를 제공합니다.
>




- A button — like a [pop-up button](../components/menus-and-actions/pop-up-buttons) or [pull-down button](../components/menus-and-actions/pull-down-buttons) — that reveals a menu of options directly relating to its action
- >  팝업 버튼 또는 풀다운 버튼과 같이 동작과 직접 관련된 옵션 메뉴를 표시하는 버튼

- A hidden [context menu](../components/menus-and-actions/context-menus) that people can reveal to access to a small number of frequently used actions relevant to their current view or task
- >  현재 보기 또는 태스크와 관련하여 자주 사용되는 소수의 수행에 액세스하기 위해 사용자가 표시할 수 있는 숨겨진 컨텍스트 메뉴

- A macOS app’s [menu bar](../components/system-experiences/the-menu-bar) menus that contain all the commands people can perform in the app
- >  사용자가 앱에서 수행할 수 있는 모든 명령이 포함된 MacOS 앱의 메뉴 모음 메뉴


Regardless of type, all menus list one or more *menu items*, each of which represents a command, option, or state that affects the current selection or context. When people choose a menu item, the action occurs and the menu typically closes.
> 유형에 관계없이 모든 메뉴는 현재 선택 항목이나 컨텍스트에 영향을 미치는 명령, 옵션 또는 상태를 나타내는 하나 이상의 메뉴 항목을 나열합니다. 사용자가 메뉴 항목을 선택하면 작업이 수행되고 일반적으로 메뉴가 닫힙니다.
>




# **Labels**

Each menu item displays text to describe its action and may include a symbol or interface icon to clarify meaning. In addition to text and symbols, a menu item can also display the characters people type to perform the associated keyboard shortcut, if there is one. Unlike most other types of menus, a context menu doesn’t display keyboard shortcuts because it already provides a quick way to get task-specific actions.
> 각 메뉴 항목은 동작을 설명하는 텍스트를 표시하고 의미를 명확히 하기 위한 기호 또는 인터페이스 아이콘을 포함할 수 있습니다. 텍스트 및 기호 외에도 메뉴 항목에는 관련 키보드 단축키가 있는 경우 사용자가 입력하는 문자가 표시될 수 있습니다. 다른 대부분의 메뉴 유형과는 달리 상황에 맞는 메뉴는 이미 작업별 작업을 가져올 수 있는 빠른 방법을 제공하므로 키보드 단축키를 표시하지 않습니다.
>




**NOTE**Depending on menu layout, an iOS or iPadOS app can display a few unlabeled menu items that use only symbols or icons to identify them. For guidance, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus#ios-ipados).
> 참고 메뉴 레이아웃에 따라 iOS 또는 iPadOS 앱은 라벨이 지정되지 않은 몇 가지 메뉴 항목을 표시하여 기호나 아이콘만 사용하여 식별할 수 있습니다. 자세한 내용은 iOS, iPadOS를 참조하십시오.
>




**To help people understand what a menu item does, write a label that clearly and succinctly describes it.** Depending on the item you’re describing, consider the following guidance:
> 사람들이 메뉴 항목이 어떤 역할을 하는지 이해하도록 돕기 위해 해당 항목을 명확하고 간결하게 설명하는 레이블을 작성하십시오. 설명하는 항목에 따라 다음 지침을 고려하십시오.
>




- To label a menu item that initiates an action, use a verb or verb phrase that describes the action, such as *Copy*, *Share App*, or *Close*.
- >  작업을 시작하는 메뉴 항목에 레이블을 지정하려면 복사, 앱 공유 또는 닫기 등의 작업을 설명하는 동사 또는 동사 구문을 사용합니다.

- When describing the status of a menu item that toggles between attributes or states, indicate its current state. For example, you might use a pair of labels for a menu item that shows or hides something, like *Show Completed* and *Hide Completed*, or you might display a checkmark next to the label to show that the state or attribute is in effect, such as *Organize by Conversation*.
- >  속성 또는 상태 간에 전환되는 메뉴 항목의 상태를 설명할 때 현재 상태를 나타냅니다. 예를 들어 완료된 항목 표시 및 완료된 항목 숨김과 같이 메뉴 항목을 표시하거나 숨기는 데 레이블 쌍을 사용하거나 레이블 옆에 확인 표시를 표시하여 상태 또는 속성이 적용 중임을 표시할 수 있습니다(예: 대화별 구성).



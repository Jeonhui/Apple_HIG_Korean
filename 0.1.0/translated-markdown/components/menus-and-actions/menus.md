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


**For consistent labels, adopt a condensed style that doesn't include articles, and use title-style capitalization.** In English, the articles *a*, *an*, and *the* always lengthen labels, but rarely enhance understanding. For example, when people want to open a message in Mail, they understand that the *Open Message* menu item refers to the currently selected message, so adding an article to the label — such as *Open the Message* — doesn't help clarify the item's action.
> 일관된 레이블의 경우 기사를 포함하지 않는 축약된 스타일을 채택하고 제목 스타일 대문자화를 사용합니다. 영어에서는 기사 a, an 및 항상 길어지는 레이블이지만 이해도를 높이는 경우는 거의 없습니다. 예를 들어, 메일에서 메시지를 열려는 경우 메시지 열기 메뉴 항목이 현재 선택한 메시지를 참조하는 것으로 이해하므로 메시지 열기 같은 문서를 레이블에 추가하는 것은 항목의 작업을 명확히 하는 데 도움이 되지 않습니다.
>




**Append an ellipsis to a menu item’s label when people need to provide additional information before the action can complete.** The ellipsis character (…) signals that another view will open in which people can input information or make choices.
> 작업을 완료하기 전에 추가 정보를 제공해야 하는 경우 메뉴 항목의 레이블에 줄임표를 추가합니다. 줄임표 문자(…)는 사용자가 정보를 입력하거나 선택할 수 있는 다른 보기가 열린다는 것을 나타냅니다.
>




**Show people when a menu item is unavailable.** An unavailable menu item often appears dimmed and doesn’t respond to interactions. If all of a menu’s items are unavailable, ensure that the menu itself remains enabled so people can open it and learn about the commands it contains.
> 메뉴 항목을 사용할 수 없는 경우 사용자에게 표시합니다. 사용할 수 없는 메뉴 항목은 종종 흐리게 표시되고 상호 작용에 응답하지 않습니다. 모든 메뉴 항목을 사용할 수 없는 경우, 사용자가 메뉴를 열고 메뉴에 포함된 명령에 대해 배울 수 있도록 메뉴 자체를 사용 가능으로 유지합니다.
>




# **Toggled items**

When you need to help people switch an item or attribute between two states, you can support toggling in one of the following three ways:
> 사용자가 두 상태 간에 항목 또는 속성을 전환하는 데 도움이 필요한 경우 다음 세 가지 방법 중 하나를 사용하여 전환할 수 있습니다.
>




- A single menu item that displays a label that can change depending on the current state, such as *Show Ruler* and *Hide Ruler*. The parent menu never lists more than one label at a time.
- >  눈금자 표시 및 눈금자 숨기기 등 현재 상태에 따라 변경될 수 있는 레이블을 표시하는 단일 메뉴 항목입니다. 상위 메뉴는 한 번에 둘 이상의 레이블을 나열하지 않습니다.

- A single menu item that has a checkmark next to it when it’s turned on; for example, a text attribute like *Bold*. The parent menu always lists the item, displaying or removing the checkmark according to the current state.
- >  설정 시 옆에 확인 표시가 있는 단일 메뉴 항목(예: 굵은 글씨 같은 텍스트 속성) 상위 메뉴는 항상 항목을 나열하여 현재 상태에 따라 확인 표시를 표시하거나 제거합니다.

- A pair of menu items, each of which has a label that describes one of two opposing actions or states; for example, *Grid On* and *Grid Off*. The parent menu always lists both menu items, but only the menu item that’s currently in effect displays a checkmark or appears selected (usually dimmed).
- >  두 개의 서로 반대되는 작업 또는 상태(예: 그리드 켜기 및 그리드 끄기) 중 하나를 설명하는 레이블이 있는 한 쌍의 메뉴 항목입니다. 상위 메뉴에는 항상 두 메뉴 항목이 모두 나열되지만 현재 적용 중인 메뉴 항목만 확인 표시가 표시되거나 선택된 상태로 표시됩니다(일반적으로 흐리게 표시됨).


**Consider using changeable titles to shorten a long list of items that show and hide features.** For example, the View menu in Mail uses changeable titles to Show or Hide the Tab Bar, Mailbox List, Toolbar, or Favorites Bar.
> 예를 들어, 메일의 보기 메뉴는 변경 가능한 제목을 사용하여 탭 모음, 사서함 목록, 도구 모음 또는 즐겨찾기 모음 표시 또는 숨기기에 사용합니다.
>




**Use a changeable label when there isn't enough room to list a pair of menu items.** When necessary to make sure both titles are unambiguous, consider using two verbs that clearly express opposite actions, like *Turn Grid On* and *Turn Grid Off*.
> 한 쌍의 메뉴 항목을 나열할 공간이 충분하지 않을 때는 변경 가능한 레이블을 사용하십시오. 두 제목이 모두 모호하지 않도록 하려면 그리드 켜기 및 그리드 끄기 등 반대 동작을 명확하게 나타내는 두 개의 동사를 사용하는 것을 고려해 보십시오.
>




**Consider using a checkmark when a toggled item represents an attribute that’s currently in effect.** It’s easy for people to scan for checkmarks in a list of attributes to find the ones that are in effect. For example, in the standard Format > Font menu, checkmarks can make it easy for people notice the styles that apply to selected text.
> 전환된 항목이 현재 적용 중인 속성을 나타내는 경우 체크 표시를 사용하는 것이 좋습니다. 사용자가 속성 목록에서 체크 표시를 검색하여 적용 중인 항목을 쉽게 찾을 수 있습니다. 예를 들어 표준 형식 > 글꼴 메뉴에서 체크 표시를 사용하면 선택한 텍스트에 적용되는 스타일을 쉽게 알 수 있습니다.
>




**Consider offering a menu item that makes it easy to remove multiple toggled attributes.** For example, if you let people apply several styles to selected text, it can work well to provide a menu item — such as *Plain* — that removes all applied formatting attributes at one time.
> 여러 개의 토글 속성을 쉽게 제거할 수 있는 메뉴 항목을 제공하는 것이 좋습니다. 예를 들어, 사용자가 선택한 텍스트에 여러 가지 스타일을 적용하도록 하는 경우 적용된 모든 형식 속성을 한 번에 제거하는 메뉴 항목(예: 일반)을 제공하는 것이 좋습니다.
>




**Consider displaying a pair of menu items instead of one toggled menu item if it adds clarity.** Sometimes, it helps people to view both actions or states at the same time. The Mailbox menu in Mail, for example, includes both the *Take All Accounts Online* and *Take All Accounts Offline* items, so when someone's accounts are online, only the *Take All Accounts Offline* menu item appears enabled.
> 명확성을 더하는 경우 전환된 메뉴 항목 대신 한 쌍의 메뉴 항목을 표시하는 것을 고려하십시오. 때로는 작업이나 상태를 동시에 볼 수 있도록 도와줍니다. 예를 들어, 메일의 사서함 메뉴에는 모든 계정 온라인 사용 및 모든 계정 오프라인 사용 항목이 모두 포함되므로, 다른 사용자의 계정이 온라인일 때 모든 계정 오프라인 사용 메뉴 항목만 사용 가능으로 표시됩니다.
>




# **Organization**

To help people find the item they’re looking for, you can organize menu items according to frequency of use, object importance, functional categories, or another prioritization scheme that fits the way people use your app.
> 사용자가 원하는 항목을 찾을 수 있도록 사용 빈도, 개체 중요도, 기능 범주 또는 앱 사용 방식에 맞는 다른 우선 순위 체계에 따라 메뉴 항목을 구성할 수 있습니다.
>




Sometimes, it makes sense to group logically related items within a menu, such as the editing commands *Copy*, *Cut*, and *Paste*. To help people visually distinguish groups, you use a separator. Depending on the platform and type of menu, a *separator* appears between groups as a horizontal line or a short gap in the menu’s background appearance.
> 편집 명령 Copy, Cut, Paste와 같이 메뉴 내에서 논리적으로 관련된 항목을 그룹화하는 것이 적절한 경우도 있습니다. 사용자가 그룹을 시각적으로 구별하도록 하려면 구분 기호를 사용합니다. 플랫폼과 메뉴 유형에 따라 그룹 간 구분자가 가로줄로 나타나거나 메뉴의 배경 모양에 짧은 공백으로 나타납니다.
>




**List menu items according to your prioritization scheme.** People tend to start scanning a menu from the top, so listing high-priority items and groups first often means that people can find what they want without scanning the entire menu.
> 우선 순위 지정 체계에 따라 메뉴 항목을 나열하십시오. 사람들은 맨 위에서부터 메뉴를 검색하기 시작하는 경향이 있습니다. 따라서 우선 순위가 높은 항목과 그룹을 먼저 나열하면 전체 메뉴를 검색하지 않고도 원하는 항목을 찾을 수 있는 경우가 많습니다.
>




**Avoid letting your prioritization scheme separate a group of commands that are logically related, even if the commands don’t all have the same priority.** For example, people generally use Paste and Match Style much less often than they use Paste, but they expect to find both commands in the same group that contains other related editing actions like Copy and Cut.
> 예를 들어, 사람들은 일반적으로 붙여넣기보다 붙여넣기 및 일치 스타일을 훨씬 적게 사용하지만, 동일한 그룹에서 다음과 같은 다른 관련 편집 작업이 포함된 두 명령을 모두 찾을 것으로 예상합니다. 복사 및 잘라내기.
>




**Be mindful of menu length.** People need more time and attention to read a long menu, which means they may miss the command they want. If a menu is long, you might need to break it into separate menus. In some cases, you can use a submenu to shorten the list. The exception is a menu that contains user-defined or dynamically generated content, such as the History and Bookmarks menus in Safari. In this situation, people expect the menu to accommodate the items they add to it, so a long menu is fine, and scrolling is acceptable.
> 메뉴 길이에 주의하세요. 사람들은 긴 메뉴를 읽기 위해 더 많은 시간과 주의를 필요로 합니다. 이것은 그들이 원하는 명령을 놓칠 수 있다는 것을 의미합니다. 메뉴가 길면 별도의 메뉴로 분할해야 할 수 있습니다. 경우에 따라 하위 메뉴를 사용하여 목록을 단축할 수 있습니다. Safari의 기록 및 책갈피 메뉴와 같이 사용자 정의 또는 동적으로 생성된 내용을 포함하는 메뉴는 예외입니다. 이런 상황에서 사람들은 메뉴가 자신이 추가한 항목을 수용할 것으로 기대하기 때문에 긴 메뉴도 괜찮고 스크롤도 허용된다.
>




# **Submenus**

Sometimes, a menu item can reveal a set of closely related items in a subordinate list called a *submenu*. In this case, a menu item indicates the presence of a submenu by displaying a symbol — like a chevron — after its label.
> 때로는 메뉴 항목이 하위 메뉴라고 하는 하위 목록에서 밀접하게 관련된 항목 집합을 표시할 수 있습니다. 이 경우 메뉴 항목은 레이블 뒤에 쉐브론과 같은 기호를 표시하여 하위 메뉴의 존재를 나타냅니다.
>




**Use submenus sparingly.** Each submenu adds complexity to the interface and hides the items it contains. You might consider creating a submenu when a term appears in more than two menu items in the same group. For example, instead of offering separate menu items for *Sort by Date*, *Sort by Subject*, and *Sort by Unread*, the View menu in Mail includes a Sort By submenu that contains items like *Date*, *Subject*, and *Unread*. In a case like this, it generally works well to use the repeated term in the submenu label to help people predict what it contains.
> 하위 메뉴를 적게 사용합니다. 각 하위 메뉴는 인터페이스에 복잡성을 더하고 포함된 항목을 숨깁니다. 같은 그룹의 세 개 이상의 메뉴 항목에 용어가 나타나는 경우 하위 메뉴를 만드는 것을 고려할 수 있습니다. 예를 들어, 메일의 보기 메뉴에는 날짜별 정렬, 제목별 정렬 및 읽지 않은 문서별 정렬에 대해 별도의 메뉴 항목을 제공하는 대신 날짜, 제목 및 읽지 않은 문서별 정렬 하위 메뉴가 있습니다. 이와 같은 경우, 하위 메뉴 레이블에서 반복되는 용어를 사용하여 사람들이 무엇이 포함되어 있는지 예측할 수 있도록 하는 것이 일반적으로 효과적이다.
>




**Limit the depth and length of submenus.** It can be difficult for people to reveal multiple levels of hierarchical submenus, so it’s generally best to restrict them to a single level. Also, if a submenu contains more than about five items, consider creating a new menu.
> 하위 메뉴의 깊이와 길이를 제한합니다. 계층 하위 메뉴의 여러 단계를 표시하기 어려울 수 있으므로 일반적으로 단일 수준으로 제한하는 것이 가장 좋습니다. 또한 하위 메뉴에 약 5개 이상의 항목이 포함된 경우 새 메뉴를 만드는 것을 고려해 보십시오.
>




**Keep a submenu enabled even when its nested menu items are unavailable.** A submenu item — like all menu items — needs to let people open it and learn about the commands it contains.
> 중첩된 메뉴 항목을 사용할 수 없는 경우에도 하위 메뉴를 사용 가능으로 유지합니다. 하위 메뉴 항목은 모든 메뉴 항목과 마찬가지로 사용자가 하위 메뉴를 열고 하위 메뉴에 포함된 명령에 대해 배울 수 있어야 합니다.
>




**Prefer using a submenu to indenting menu items.** Using indentation is inconsistent with the system and doesn’t clearly express the relationships between the menu items.
> 메뉴 항목을 들여쓰기보다 하위 메뉴를 사용하는 것을 선호합니다. 들여쓰기를 사용하는 것은 시스템과 일치하지 않으며 메뉴 항목 간의 관계를 명확하게 표현하지 못합니다.
>




# **Platform considerations**

*No additional considerations for macOS, tvOS, or watchOS.*
> macOS, tvOS 또는 워치에 대한 추가 고려 사항 없음OS.
>




# **iOS, iPadOS**

Beginning in iOS 16 and iPadOS 16, a menu can display items in one of the following three layouts.
> iOS 16과 iPad OS 16부터는 메뉴를 통해 다음 세 가지 레이아웃 중 하나로 항목을 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus/images/small-medium-large-menu-layouts-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus/images/small-medium-large-menu-layouts-dark_2x.png)

- **Small.** A row of four items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon, but no label.
- >  작음. 메뉴 맨 위의 나머지 항목이 포함된 목록 위에 네 개의 항목 행이 나타납니다. 맨 위 행의 각 항목에 대해 메뉴에는 기호 또는 아이콘이 표시되지만 레이블은 표시되지 않습니다.

- **Medium.** A row of three items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon above a short label.
- >  중간. 메뉴 맨 위의 나머지 항목이 포함된 목록 위에 세 개의 항목 행이 나타납니다. 맨 위 행의 각 항목에 대해 메뉴는 짧은 레이블 위에 기호 또는 아이콘을 표시합니다.

- **Large (the default).** The menu displays all items in a list.
- >  큼(기본값). 메뉴는 목록의 모든 항목을 표시합니다.


For developer guidance, see [preferredElementSize](https://developer.apple.com/documentation/uikit/uimenu/4013313-preferredelementsize?language=objc).

**Choose a small or medium menu layout when it can help streamline people’s choices.** Consider using the medium layout if your app has three important actions that people often want to perform. For example, Notes uses the medium layout to give people a quick way to perform the Scan, Lock, and Pin actions. Use the small layout only for closely related actions that typically appear as a group, such as Bold, Italic, Underline, and Strikethrough. For each action, use a recognizable symbol that helps people identify the action without a label.
> 사용자의 선택을 간소화하는 데 도움이 될 수 있을 때 소형 또는 중형 메뉴 레이아웃을 선택하십시오. 앱에 사람들이 자주 수행하기를 원하는 세 가지 중요한 작업이 있다면 중형 레이아웃을 사용하는 것을 고려해 보십시오. 예를 들어, Notes는 매체 레이아웃을 사용하여 검색, 잠금 및 고정 작업을 빠르게 수행할 수 있도록 합니다. 굵은체, 기울임체, 밑줄 및 가로줄과 같이 일반적으로 그룹으로 나타나는 밀접하게 관련된 수행에만 작은 레이아웃을 사용하십시오. 각 수행에 대해 사용자가 레이블 없이 수행을 식별하는 데 도움이 되는 인식 가능한 기호를 사용하십시오.
>




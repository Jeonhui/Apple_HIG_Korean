# **[components-menus-and-actions] context-menus**

## A context menu provides access to functionality that’s directly related to an onscreen item, without cluttering the interface.
> 상황에 맞는 메뉴를 사용하면 인터페이스를 방해하지 않고 화면 항목과 직접 관련된 기능에 액세스할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/context-menu-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/context-menu-intro-dark_2x.png)

Although a context menu provides convenient access to frequently used items, it’s hidden by default, so people might not know it’s there. To reveal a context menu, people generally choose a view or select some content and then perform an action, using the input modes their current configuration supports. For example:
> 상황에 맞는 메뉴를 통해 자주 사용하는 항목에 편리하게 액세스할 수 있지만 기본적으로 숨겨져 있으므로 사용자가 해당 항목이 있는지 모를 수 있습니다. 상황에 맞는 메뉴를 표시하기 위해, 사람들은 일반적으로 보기를 선택하거나 일부 내용을 선택한 다음 현재 구성이 지원하는 입력 모드를 사용하여 작업을 수행합니다. 예:
>




- The system-defined long press gesture in iOS and iPadOS
- >  iOS 및 iPad의 시스템 정의 길게 누르는 제스처OS

- Pressing the Control key while clicking a pointing device in macOS and iPadOS
- >  MacOS 및 iPad에서 포인팅 장치를 클릭하면서 Control 키 누르기OS

- Using a secondary click on a Magic Trackpad in macOS or iPadOS
- >  MacOS 또는 iPad에서 Magic Trackpad를 두 번째로 클릭하기OS


# **Best practices**

**Prioritize relevancy when choosing items to include in a context menu.**A context menu isn’t for providing advanced or rarely used items; instead, it helps people quickly access the commands they’re most likely to need in their current context. For example, the context menu for a Mail message in the inbox includes commands for replying and moving the message, but not commands for editing message content, managing mailboxes, or filtering messages.
> 상황에 맞는 메뉴에 포함할 항목을 선택할 때 관련성의 우선 순위를 지정합니다.상황에 맞는 메뉴는 고급 또는 거의 사용되지 않는 항목을 제공하기 위한 것이 아니라 사람들이 현재 상황에 가장 필요할 수 있는 명령에 빠르게 액세스할 수 있도록 도와줍니다. 예를 들어, 받은 편지함에 있는 메일 메시지의 상황에 맞는 메뉴에는 메시지를 회신하고 이동하기 위한 명령이 포함되지만 메시지 내용 편집, 사서함 관리 또는 메시지 필터링을 위한 명령은 포함되지 않습니다.
>




**Aim for a small number of menu items.** A context menu that’s too long can be difficult to scan and scroll.
> 적은 수의 메뉴 항목을 목표로 합니다. 너무 긴 상황에 맞는 메뉴는 스캔하고 스크롤하기 어려울 수 있습니다.
>




**Enable context menus consistently throughout your app.** If you provide context menus for items in some places but not in others, people won’t know where they can use the feature and may think there’s a problem.
> 앱 전체에서 상황에 맞는 메뉴를 일관되게 사용하도록 설정합니다. 일부 장소에서는 항목에 대한 상황에 맞는 메뉴를 제공하지만 다른 장소에서는 제공하지 않는 경우, 사람들은 이 기능을 사용할 수 있는 위치를 알지 못하고 문제가 있다고 생각할 수 있습니다.
>




**Always make context menu items available in the main interface, too.**For example, in Mail in iOS and iPadOS, the context menu items that are available for a message in the inbox are also available in the toolbar of the message view. In macOS, an app’s menu bar menus list all the app’s commands, including those in various context menus.
> 기본 인터페이스에서도 상황에 맞는 메뉴 항목을 항상 사용할 수 있도록 합니다.예를 들어 iOS 및 iPadOS의 메일에서 받은 편지함의 메시지에 사용할 수 있는 상황에 맞는 메뉴 항목은 메시지 보기의 도구 모음에서도 사용할 수 있습니다. macOS에서 앱의 메뉴 모음 메뉴는 다양한 컨텍스트 메뉴에 있는 명령을 포함하여 앱의 모든 명령을 나열합니다.
>




**If you need to use submenus to manage a menu’s complexity, keep them to one level.** A submenu is a menu item that reveals a secondary menu of logically related commands. Although submenus can shorten a context menu and clarify its commands, more than one level of submenu complicates the experience and can be difficult for people to navigate. If you need to include a submenu, give it an intuitive title that helps people predict its contents without opening it.
> 메뉴의 복잡성을 관리하기 위해 하위 메뉴를 사용해야 하는 경우 하위 메뉴를 한 수준으로 유지하십시오. 하위 메뉴는 논리적으로 관련된 명령의 보조 메뉴를 표시하는 메뉴 항목입니다. 하위 메뉴가 상황별 메뉴를 단축하고 명령을 명확히 할 수 있지만, 하위 메뉴가 하나 이상이면 경험이 복잡해지고 사람들이 탐색하기 어려울 수 있다. 하위 메뉴를 포함해야 하는 경우, 하위 메뉴를 열지 않고도 내용을 예측할 수 있는 직관적인 제목을 지정하십시오.
>




**Aim to place the most frequently used menu items where people are likely to focus first.** When a context menu opens, people often read it starting from the part that’s closest to where their finger or pointer revealed it. Depending on the onscreen location of the selected content, a context menu might open above or below that area of the screen, so you might also need to reverse the order of items to match the position of the menu.
> 사람들이 가장 자주 사용하는 메뉴 항목을 가장 먼저 집중하기 쉬운 곳에 배치하는 것을 목표로 하고, 상황에 맞는 메뉴가 열리면 사람들은 종종 손가락이나 포인터가 드러낸 부분에 가장 가까운 부분부터 읽는다. 선택한 콘텐츠의 화면 위치에 따라 상황에 맞는 메뉴가 화면의 해당 영역 위나 아래에 열릴 수 있으므로 메뉴 위치와 일치하도록 항목의 순서를 반대로 해야 할 수도 있습니다.
>




**Show keyboard shortcuts in you app’s main menus, not in context menus.** Context menus already provide a shortcut to task-specific commands, so it's redundant to display keyboard shortcuts too.
> 상황에 맞는 메뉴가 아닌 앱의 기본 메뉴에 바로 가기 키를 표시합니다. 상황에 맞는 메뉴는 이미 작업별 명령에 대한 바로 가기를 제공하므로 키보드 바로 가기를 표시하는 것도 중복됩니다.
>




**Follow best practices for using separators.** As with other types of menus, you can use separators to group items in a context menu and help people scan the menu more quickly. In general, you don’t want more than about three groups in a context menu. For guidance, see [Menus](../components/menus-and-actions/menus).
> 다른 유형의 메뉴와 마찬가지로 구분 기호를 사용하여 상황에 맞는 메뉴의 항목을 그룹화하고 사용자가 메뉴를 더 빨리 검색할 수 있도록 지원할 수 있습니다. 일반적으로 상황에 맞는 메뉴에서 세 개 이상의 그룹을 사용하지 않습니다. 자세한 내용은 메뉴를 참조하십시오.
>




# **Content**

In most cases, a context menu doesn’t display a title, but as with all other menus, each item in a context menu displays a short label that describes what it does. For guidance, see [Menus > Labels](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus/#labels).
> 대부분의 경우 상황에 맞는 메뉴는 제목을 표시하지 않지만 다른 모든 메뉴와 마찬가지로 상황에 맞는 메뉴의 각 항목은 해당 작업을 설명하는 짧은 레이블을 표시합니다. 자세한 내용은 메뉴 > 레이블을 참조하십시오.
>




# **Platform considerations**

*Not supported in tvOS or watchOS.*
> tvOS 또는 시계에서 지원되지 않음OS.
>




# **iOS, iPadOS**

**In general, avoid adding a title to a context menu.** The exception is if a context menu targets content that might not be clear. For example, when people select multiple Mail messages and tap the Mark toolbar button, the resulting context menu displays a title that states the number of selected messages, reminding people that the command they choose affects all the messages they selected.
> 일반적으로 컨텍스트 메뉴에 제목을 추가하지 마십시오. 컨텍스트 메뉴가 명확하지 않을 수 있는 내용을 대상으로 하는 경우는 예외입니다. 예를 들어, 사용자가 여러 메일 메시지를 선택하고 표시 도구 모음 단추를 누르면, 결과 컨텍스트 메뉴는 선택한 메시지 수를 나타내는 제목을 표시하여, 선택한 명령이 선택한 모든 메시지에 영향을 미친다는 것을 알려줍니다.
>




**Include a symbol or interface icon with each command in a context menu.** A symbol or icon reinforces the meaning of a command, helping people instantly understand its function. In cases where there are multiple commands that need to use the same symbol, consider omitting all symbols to avoid repeating them.
> 상황에 맞는 메뉴에 각 명령어와 함께 기호나 인터페이스 아이콘을 포함합니다. 기호나 아이콘은 명령어의 의미를 강화하여 사람들이 명령어의 기능을 즉시 이해할 수 있도록 도와줍니다. 동일한 기호를 사용해야 하는 명령이 여러 개 있는 경우 반복되지 않도록 모든 기호를 생략하는 것이 좋습니다.
>




**Provide either a context menu or an edit menu for an item, but not both.** If you enable both features for the same item, it can be confusing to people — and difficult for the system to detect their intent. See [Edit menus](../components/menus-and-actions/edit-menus).
> 항목에 대한 상황에 맞는 메뉴 또는 편집 메뉴를 제공하되 둘 다 제공해서는 안 됩니다. 동일한 항목에 대해 두 기능을 모두 사용 가능으로 설정하면 사용자에게 혼란을 줄 수 있으며, 시스템에서 의도를 탐지하기 어려울 수 있습니다. 메뉴 편집을 참조하십시오.
>




**Warn people about context menu items that can destroy data.** If you need to include potentially destructive items in your context menu — such as Delete or Remove — list them at the end of the menu and identify them as destructive (for developer guidance, see [destructive](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/3335200-destructive)). The system can display a destructive menu item using a red text color.
> 사용자에게 데이터를 파괴할 수 있는 상황별 메뉴 항목에 대해 경고합니다. 삭제 또는 제거와 같은 상황별 메뉴에 잠재적으로 파괴적인 항목을 포함해야 하는 경우 메뉴 끝에 해당 항목을 나열하고 파괴적인 항목으로 식별합니다(개발자 지침은 파괴 항목 참조). 시스템은 빨간색 텍스트 색상을 사용하여 파괴적인 메뉴 항목을 표시할 수 있습니다.
>




**In iPadOS, consider using a context menu to let people create a new object in your app.** iPadOS lets you reveal a context menu when people perform a long press on the touchscreen or use a secondary click with an attached trackpad or keyboard. For example, Files lets people create a new folder by revealing a context menu in an area between existing files and folders.
> iPadOS에서 사용자가 앱에서 새 개체를 만들 수 있도록 상황에 맞는 메뉴를 사용하는 것을 고려해 보십시오. iPadOS를 사용하면 터치스크린을 길게 누르거나 연결된 트랙패드 또는 키보드로 보조 클릭을 사용할 때 상황에 맞는 메뉴를 표시할 수 있습니다. 예를 들어, 파일을 사용하면 기존 파일과 폴더 사이의 영역에 상황에 맞는 메뉴를 표시하여 새 폴더를 만들 수 있습니다.
>




In iOS and iPadOS, a context menu can display a preview of the current content near the list of commands. People can choose a command in the menu or — in some cases — they can tap the preview to open it or drag it to another area.
> iOS 및 iPadOS에서 컨텍스트 메뉴는 명령 목록 근처에 현재 콘텐츠의 미리 보기를 표시할 수 있습니다. 사용자는 메뉴에서 명령을 선택하거나(경우에 따라) 미리 보기를 눌러 열거나 다른 영역으로 끌 수 있습니다.
>




**Prefer a graphical preview that clarifies the target of a context menu’s commands.** For example, when people reveal a context menu on a list item in Notes or Mail, the preview shows a condensed version of the actual content to help people confirm that they're working with the item they intend.
> 상황에 맞는 메뉴 명령의 대상을 명확히 하는 그래픽 미리보기를 선호합니다. 예를 들어, Notes 또는 메일의 목록 항목에 상황에 맞는 메뉴를 표시할 때 미리보기는 실제 내용의 축약된 버전을 보여줌으로써 사용자가 원하는 항목으로 작업하고 있는지 확인할 수 있습니다.
>




**Ensure that your preview looks good as it animates.** As people reveal a context menu on an onscreen object, the system animates the preview image as it emerges from the content, dimming the screen behind the preview and the menu. It’s important to adjust the preview’s clipping path to match the shape of the preview image so that its contours, such as the rounded corners, don’t appear to change during animation. For developer guidance, see [UIContextMenuInteractionDelegate](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate).
> 미리보기가 애니메이션처럼 보이는지 확인하십시오. 사용자가 화면 개체에 상황에 맞는 메뉴를 표시하면 시스템이 미리보기 이미지를 미리보기 및 메뉴 뒤에 있는 화면을 어둡게 하여 내용에서 나오는 대로 미리보기 이미지를 애니메이션화합니다. 애니메이션 작업 중에 둥근 모서리와 같은 윤곽선이 변경되지 않도록 미리 보기 이미지의 모양에 맞게 미리 보기 클리핑 경로를 조정하는 것이 중요합니다. 개발자 지침은 UIC 컨텍스트 메뉴 상호 작용 위임을 참조하십시오.
>




# **macOS**

On a Mac, a context menu is sometimes called a *contextual* menu.
> Mac에서는 상황에 맞는 메뉴를 상황에 맞는 메뉴라고 부르기도 합니다.
>




# **watchOS**

In versions of watchOS before watchOS 7, people could press firmly on the display to open a hidden menu of actions relevant to the current screen. In watchOS 7 and later, watchOS apps elevate important items out of such menus and into the relevant screen or a settings screen.
> 시계 버전에서는감시 전 OSOS 7, 사람들은 디스플레이를 단단히 눌러 현재 화면과 관련된 숨겨진 동작 메뉴를 열 수 있다. 당직OS 7 이상, 보기OS 앱은 이러한 메뉴에서 관련 화면 또는 설정 화면으로 중요한 항목을 상승시킵니다.
>




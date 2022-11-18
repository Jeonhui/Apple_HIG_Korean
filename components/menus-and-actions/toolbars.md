# **[components-menus-and-actions] toolbars**

## A toolbar provides convenient access to frequently used commands and controls that perform actions relevant to the current view.
> 도구 모음을 사용하면 자주 사용하는 명령과 현재 보기와 관련된 작업을 수행하는 컨트롤에 편리하게 액세스할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toolbar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toolbar-intro-dark_2x.png)

Depending on the platform, a toolbar can look and behave differently.
> 플랫폼에 따라 도구 모음의 모양과 동작이 다를 수 있습니다.
>




- In iOS, a toolbar appears at the bottom of a screen. iOS toolbars aren’t customizable, and they don’t support grouping.
- >  iOS에서 도구 모음은 화면 아래에 나타납니다. iOS 도구 모음은 사용자 지정할 수 없으며 그룹화를 지원하지 않습니다.

- In iPadOS and macOS, a toolbar appears at the top of a screen or window. Both platforms support customizable toolbars and grouped toolbar items. In macOS, people can hide an app’s toolbar.
- >  iPadOS 및 macOS에서 도구 모음은 화면이나 창 위쪽에 나타납니다. 두 플랫폼 모두 사용자 정의 가능한 도구 모음 및 그룹화된 도구 모음 항목을 지원합니다. macOS에서 사람들은 앱의 도구 모음을 숨길 수 있다.

- In watchOS, the toolbar itself isn’t visible, but a toolbar button can appear at the top of a scrolling view. Typically, a toolbar button remains hidden behind a navigation bar until people reveal it by scrolling up.
- >  watchOS에서는 툴바 자체는 보이지 않지만 스크롤 뷰의 맨 위에 툴바 버튼이 나타날 수 있습니다. 일반적으로 도구 모음 단추는 사용자가 위로 스크롤하여 표시할 때까지 탐색 모음 뒤에 숨겨져 있습니다.


# **Best practices**

**Provide toolbar items that support the main tasks people perform.** In general, prioritize the commands that people are mostly likely to want. These commands are often the ones people use most frequently, but in some apps it might make sense to prioritize commands that map to the highest level or most important objects people work with. In a macOS app, consider ordering the items in the toolbar according to your prioritization scheme.
> 사용자가 수행하는 주요 작업을 지원하는 도구 모음 항목을 제공합니다. 일반적으로 사용자가 가장 원할 가능성이 높은 명령의 우선 순위를 지정합니다. 이러한 명령은 종종 사용자가 가장 자주 사용하는 명령이지만 일부 앱에서는 사용자가 작업하는 가장 높은 수준 또는 가장 중요한 개체에 매핑되는 명령의 우선 순위를 지정하는 것이 합리적일 수 있습니다. MacOS 앱에서 우선 순위 체계에 따라 도구 모음의 항목 순서를 지정하는 것을 고려해 보십시오.
>




**Avoid displaying too many toolbar items.** People need to be able to distinguish and activate each item, so you don’t want to overcrowd the toolbar.
> 도구 모음 항목이 너무 많이 표시되지 않도록 합니다. 사용자는 각 항목을 구분하고 활성화할 수 있어야 도구 모음이 과밀해지지 않습니다.
>




**Consider grouping toolbar items where supported.** In iPadOS and macOS, you can define logical groups of items to help people find commands that are related to certain subtasks or functional areas in your app. For example, Keynote includes several groups that are based on functionality, including one for presentation-level commands, one for playback commands, and one for object insertion. In iPadOS, you can also use grouping to keep items together in the Overflow menu (to learn more, see [iPadOS](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars#ipados)).
> 지원되는 경우 도구 모음 항목을 그룹화하는 것을 고려하십시오. iPadOS 및 macOS에서는 항목의 논리적 그룹을 정의하여 앱에서 특정 하위 작업 또는 기능 영역과 관련된 명령을 찾는 데 도움이 될 수 있습니다. 예를 들어, 키노트에는 프레젠테이션 수준 명령, 재생 명령, 개체 삽입 명령 등 기능을 기반으로 하는 여러 그룹이 포함됩니다. iPadOS에서 그룹화를 사용하여 오버플로 메뉴의 항목을 함께 보관할 수도 있습니다(자세한 내용은 iPadOS 참조).
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/layout_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/layout_2x.png)

**Make sure the meaning of each toolbar item is clear.** People shouldn’t need to guess or experiment to figure out what an item does. For each item, provide a simple, recognizable symbol or interface icon, or a short, descriptive label. In a macOS app, provide both so that people can view the symbol and the label in the toolbar if they choose. If you provide labels, prefer verbs and verb phrases like *View*, *Insert*, and *Share*. Use title-style capitalization and no ending punctuation.
> 각 도구 모음 항목의 의미가 명확한지 확인하십시오. 사람들은 항목이 무엇을 하는지 알아내기 위해 추측하거나 실험할 필요가 없습니다. 각 항목에 대해 단순하고 인식 가능한 기호 또는 인터페이스 아이콘 또는 짧고 설명적인 레이블을 제공합니다. MacOS 앱에서 사용자가 원하는 경우 도구 모음의 기호와 레이블을 볼 수 있도록 둘 다 제공합니다. 레이블을 제공하는 경우 동사와 보기, 삽입 및 공유와 같은 동사 구를 선호합니다. 제목 스타일의 대소문자를 사용하고 끝맺음 구두점을 사용하지 마십시오.
>




**Prefer system-provided symbols or interface icons.** System-provided symbols are familiar, automatically receive appropriate coloring, and respond consistently to user interactions and vibrancy.
> 시스템에서 제공하는 기호 또는 인터페이스 아이콘을 선호합니다. 시스템에서 제공하는 기호는 친숙하고 적절한 색상을 자동으로 수신하며 사용자 상호 작용 및 진동에 일관적으로 반응합니다.
>




**Prefer a consistent appearance for all toolbar items.** Toolbars look best and are easiest to understand when all items use a similar visual style.
> 모든 도구 모음 항목에 대해 일관된 모양을 선호합니다. 도구 모음은 모든 항목이 유사한 시각적 스타일을 사용할 때 가장 잘 보이고 이해하기 쉽습니다.
>




**If a toolbar item toggles between two states, make sure the item clearly communicates the current state.** You might consider changing the item’s color and label to clarify its current state. In the macOS Mail toolbar, for example, the online-offline toggle button displays a blue icon and a *Go Offline*label when accounts are online; when accounts are offline, the item displays a gray icon and a *Go Online* label.
> 도구 모음 항목이 두 상태 사이를 전환하는 경우 항목이 현재 상태를 명확하게 전달하는지 확인하십시오. 항목의 색상과 레이블을 변경하여 현재 상태를 명확히 할 수 있습니다. 예를 들어, macOS 메일 도구 모음에서 온라인으로 전환 단추를 누르면 계정이 온라인일 때 파란색 아이콘과 오프라인으로 전환 레이블이 표시되고, 계정이 오프라인일 때 항목에는 회색 아이콘과 온라인으로 전환 레이블이 표시됩니다.
>




**In iPadOS and macOS apps, consider letting people customize the toolbar.** Toolbar customization is especially useful in apps that provide a lot of items — or that include advanced functionality that not everyone needs — and in apps that people tend to use for long periods of time. For example, it often works well to make a range of editing actions available for toolbar customization, because people often use different types of editing commands based on their work style and their current project.
> iPadOS 및 macOS 앱에서는 사용자가 도구 모음을 사용자 지정할 수 있도록 허용하는 것을 고려하십시오. 도구 모음 사용자 지정은 특히 많은 항목을 제공하거나 모든 사용자가 필요로 하지 않는 고급 기능을 포함하는 앱 및 사용자가 장시간 사용하는 경향이 있는 앱에서 유용합니다. 예를 들어, 사람들은 종종 작업 스타일과 현재 프로젝트에 따라 다른 유형의 편집 명령을 사용하기 때문에 도구 모음 사용자 지정에 사용할 수 있는 편집 작업을 만드는 것이 좋습니다.
>




**Be prepared for translucency in the toolbar when content flows beneath it.** A toolbar automatically adopts translucency when placed above a scroll view or when the window is configured as a full-size content view. In iOS, for example, a toolbar is translucent by default, using a background material only when content appears behind it and removing the material when the view scrolls to the bottom. For guidance, see [Materials](../foundations/materials).
> 콘텐츠가 아래로 흐를 때 툴바의 투명성에 대비하십시오. 스크롤 뷰 위에 배치되거나 창이 전체 크기의 콘텐츠 뷰로 구성될 때 툴바는 자동으로 투명성을 적용합니다. 예를 들어 iOS에서 도구 모음은 기본적으로 반투명하며, 내용이 뒤에 나타날 때만 배경 자료를 사용하고 보기가 아래로 스크롤될 때 해당 자료를 제거합니다. 자세한 내용은 자료를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-background_2x.png)

The Mail toolbar uses a background material to distinguish itself from the mailboxes behind it.
> 메일 도구 모음은 배경 자료를 사용하여 배경에 있는 우편함과 구분합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-no-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-no-background_2x.png)

When no mailboxes appear behind the toolbar, the background material doesn’t appear.
> 도구 모음 뒤에 사서함이 나타나지 않으면 배경 자료가 나타나지 않습니다.
>




# **Platform considerations**

*No additional considerations for tvOS.*

# **iOS**

Although toolbars and tab bars both appear at the bottom of a screen, each has a different purpose.
> 도구 모음과 탭 표시줄이 모두 화면 아래에 나타나지만 각각의 용도는 다릅니다.
>




- A toolbar contains buttons for performing actions related to the screen, such as creating an item, filtering items, or marking up content.
- >  도구 모음에는 항목 만들기, 항목 필터링 또는 내용 표시와 같은 화면 관련 작업을 수행하기 위한 단추가 있습니다.

- A tab bar lets people navigate among different areas of an app, such as the Alarm, Stopwatch, and Timer tabs in the Clock app.
- >  탭 모음을 사용하면 시계 앱의 경보, 중지워치 및 타이머 탭과 같은 앱의 여러 영역을 탐색할 수 있습니다.


Toolbars and tab bars don’t appear together in the same view.
> 도구 모음과 탭 표시줄이 동일한 보기에 함께 나타나지 않습니다.
>




**Avoid using a segmented control in a toolbar.** Segmented controls let people switch contexts, whereas a toolbar’s actions are specific to the current screen.
> 도구 모음에서 세그먼트화된 컨트롤을 사용하지 마십시오. 세그먼트화된 컨트롤을 사용하면 사용자가 컨텍스트를 전환할 수 있지만 도구 모음의 동작은 현재 화면에 따라 다릅니다.
>




**In a toolbar that contains three or fewer buttons, consider using concise text labels instead of symbols to add clarity.** For example, Calendar uses the labels Today, Calendars, and Inbox. To ensure that the labels don’t run together, you can insert fixed spaces between the buttons. For developer guidance, see [UIBarButtonSystemItemFixedSpace](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace).
> 세 개 이하의 단추를 포함하는 도구 모음에서 명확성을 추가하기 위해 기호 대신 간결한 텍스트 레이블을 사용하는 것을 고려하십시오. 예를 들어, 일정관리는 오늘, 일정관리 및 받은 문서 레이블을 사용합니다. 레이블이 함께 실행되지 않도록 단추 사이에 고정된 공백을 삽입할 수 있습니다. 개발자 지침은 UIBarButtonSystemItemFixedSpace를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-spacing_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-spacing_2x.png)

**In a toolbar that has more than three buttons, consider using symbols to conserve space.** [SF Symbols](../foundations/sf-symbols) provides a wide range of customizable symbols you can use to represent actions in your app. If you need to create a custom interface icon for a toolbar button, use the following sizes, adjusting as needed for balance. For guidance, see [Icons](../foundations/icons).
> 세 개 이상의 단추가 있는 도구 모음에서 공간을 절약하기 위해 기호를 사용하는 것을 고려하십시오. SF 기호는 앱에서 작업을 나타내는 데 사용할 수 있는 사용자 지정 가능한 광범위한 기호를 제공합니다. 도구 모음 단추에 대한 사용자 정의 인터페이스 아이콘을 만들어야 하는 경우, 균형을 맞추기 위해 필요에 따라 조정하면서 다음 크기를 사용하십시오. 자세한 내용은 아이콘을 참조하십시오.
>




| Target size | Maximum size |
| --- | --- |
| 24x24 px @1x (48x48 px @2x, 72x72 px @3x) | 28x28 px @1x (56x56 px @2x, 84x84 px @3x) |

# **iPadOS**

In iPadOS, a toolbar offers commonly used actions that affect the current task, along with document-specific functionality, a Back button, and important actions that people might want to take at any time. In contrast, a [navigation bar](../components/navigation-and-search/navigation-bars) doesn’t typically include document-specific functionality; instead, it enables navigation through an app, offers actions that help people manage their content, and can include a search field.
> iPadOS에서 도구 모음은 현재 작업에 영향을 미치는 일반적으로 사용되는 작업과 문서별 기능, 뒤로 단추 및 사용자가 언제든지 수행하려는 중요한 작업을 제공합니다. 이와는 대조적으로, 탐색 모음은 일반적으로 문서별 기능을 포함하지 않으며, 대신 앱을 통해 탐색을 가능하게 하고, 사람들이 콘텐츠를 관리하는 데 도움이 되는 작업을 제공하며, 검색 필드를 포함할 수 있습니다.
>




**DEVELOPER NOTE**In iPadOS, you use [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar) to create a toolbar.
> 개발자 참고 iPadOS에서는 UI 탐색 모음을 사용하여 도구 모음을 만듭니다.
>




In iPadOS 16 and later, different areas of the toolbar can display different types of items.
> iPadOS 16 이상에서는 도구 모음의 다른 영역에서 다른 유형의 항목을 표시할 수 있습니다.
>




- **Leading end.** Elements that let people return to the previous document and show or hide a sidebar appear at the far leading end, followed by the document title. Next to the title the toolbar can include a document menu that contains standard and app-specific commands that affect the document as a whole, such as Duplicate, Rename, Move, and Export. To ensure that these items are always available regardless of window size, items in the toolbar’s leading end aren't customizable.
- >  선행 끝. 사용자가 이전 문서로 돌아가 사이드바를 표시하거나 숨길 수 있는 요소가 맨 끝에 나타나고 이어서 문서 제목이 나타납니다. 제목 옆에 도구 모음에는 문서 전체에 영향을 미치는 표준 및 앱별 명령(예: 복제, 이름 바꾸기, 이동 및 내보내기)이 포함된 문서 메뉴가 포함될 수 있습니다. 창 크기에 상관없이 이러한 항목을 항상 사용할 수 있도록 하려면 도구 모음의 맨 앞에 있는 항목은 사용자 지정할 수 없습니다.

- **Center area.** Frequently used items appear in the center area, where people can add, remove, and rearrange them. Items in the center section automatically collapse into the system-managed Overflow menu when the window shrinks enough in size.
- >  가운데 영역. 자주 사용하는 항목이 가운데 영역에 나타나며, 여기서 사용자는 항목을 추가, 제거 및 재정렬할 수 있습니다. 창 크기가 충분히 줄어들면 중앙 섹션의 항목이 자동으로 시스템에서 관리하는 오버플로 메뉴로 축소됩니다.

- **Trailing end.** The trailing end of a toolbar contains important items that need to remain available, buttons that open nearby inspectors, an optional search field, and the Overflow menu that reveals hidden items and enables toolbar customization. Items in the trailing end remain visible at all window sizes.
- >  후행 끝. 도구 모음의 후행 끝에는 사용 가능한 상태를 유지해야 하는 중요한 항목, 근처 검사기를 여는 단추, 선택적 검색 필드 및 숨겨진 항목을 표시하고 도구 모음 사용자 지정을 활성화하는 오버플로 메뉴가 포함되어 있습니다. 후행 끝에 있는 항목은 모든 창 크기에서 볼 수 있습니다.


**Place a toolbar at the top edge of the screen.** iPad has a large display that provides enough room for the functionality people appreciate, while preserving access to the most important commands even at small window sizes. If you’re transitioning an iPhone app to run on iPad, be sure to move toolbar buttons at the bottom of your iOS screen to the top of your iPadOS screen.
> 화면 상단 가장자리에 도구 모음을 배치합니다. iPad는 큰 디스플레이를 갖추고 있어 사람들이 감상할 수 있는 기능을 충분히 제공하는 동시에 작은 창 크기에서도 가장 중요한 명령에 대한 액세스를 유지합니다. iPhone 앱을 iPad에서 실행하도록 전환하는 경우 iOS 화면 하단의 도구 모음 버튼을 iPad 상단으로 이동하십시오.OS 화면.
>




**Use the Document menu to offer commands that affect a document as a whole.** For example, you might include commands like Duplicate, Rename, Move, and Print. Avoid listing editing commands in the Document menu — instead, consider elevating these actions to the center area of the toolbar. Also avoid offering commands that open the document in other apps, because the Share menu already lets people perform actions like using Messages to send the document to someone else, opening it in another app, or adding it to a reading list.
> 문서 메뉴를 사용하여 문서 전체에 영향을 미치는 명령을 제공할 수 있습니다. 예를 들어, 복제, 이름 바꾸기, 이동 및 인쇄와 같은 명령을 포함할 수 있습니다. 문서 메뉴에서 편집 명령을 나열하지 않도록 합니다. 대신 이러한 작업을 도구 모음의 가운데 영역으로 올리는 것이 좋습니다. 또한 공유 메뉴에서는 이미 메시지를 사용하여 다른 사람에게 문서를 보내거나 다른 앱에서 문서를 열거나 읽기 목록에 추가하는 등의 작업을 수행할 수 있으므로 다른 앱에서 문서를 여는 명령을 제공하지 마십시오.
>




**Prefer the center area for task-specific commands that people are most likely to use while they’re actively engaged with the content.** The center area is always available when the window is at full size, making it a convenient location for editing commands and other actions that affect the window’s content. Also, you can let people customize the items in the center area to support their personal work style. When people make your window smaller, items in the center section of the toolbar automatically transition into the toolbar-managed Overflow menu when there’s no longer enough room to display them.
> 사용자가 콘텐츠에 적극적으로 참여하는 동안 사용할 가능성이 가장 높은 작업별 명령어는 가운데 영역을 선호합니다. 창 크기가 완전할 때는 중앙 영역을 항상 사용할 수 있기 때문에 창 내용에 영향을 미치는 명령 및 기타 작업을 편집하기에 편리합니다. 또한 사용자가 중앙 영역의 항목을 사용자 정의하여 개인 작업 스타일을 지원할 수 있습니다. 사용자가 창을 작게 만들면 도구 모음의 중앙 섹션에 있는 항목을 표시할 공간이 더 이상 충분하지 않으면 자동으로 도구 모음 관리 오버플로 메뉴로 전환됩니다.
>




**Prefer the trailing end of the toolbar for important items that need to be visible at all window sizes.** For example, Pages offers the Share menu in this area because people often want to perform an action on the document as a whole without expanding it. The trailing end of the toolbar is also an intuitive place to put inspector buttons that reveal panels located on the trailing side of the window.
> 모든 창 크기에서 볼 수 있어야 하는 중요한 항목의 경우 도구 모음 끝을 사용하십시오. 예를 들어, 문서를 확장하지 않고 전체적으로 수행하려는 경우가 많기 때문에 페이지는 이 영역에서 공유 메뉴를 제공합니다. 도구 모음의 후미 끝은 창의 후미에 있는 패널을 표시하는 검사기 버튼을 직관적으로 배치할 수 있는 위치이기도 합니다.
>




# **macOS**

In a macOS app, the toolbar resides in the frame at the top of a window, either below or integrated with the title bar. Starting in macOS 11, window titles can display inline with controls, and toolbar items don’t include a bezel.
> MacOS 앱에서 도구 모음은 창 상단의 프레임 아래에 있거나 제목 표시줄과 통합되어 있습니다. MacOS 11부터는 창 제목이 컨트롤에 맞춰 표시될 수 있으며 도구 모음 항목에는 베젤이 포함되어 있지 않습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-macos_2x.png)

When horizontal space is limited, the toolbar can display the Search button in place of the search bar. When people click the Search button, the bar expands; when they click elsewhere in the window, the search bar collapses and the toolbar displays the button again.
> 수평 공간이 제한된 경우 도구 모음은 검색 표시줄 대신 검색 단추를 표시할 수 있습니다. 검색 단추를 누르면 막대가 확장되고, 창에서 다른 곳을 누르면 검색 표시줄이 축소되고 도구 모음에 단추가 다시 표시됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-collapsed-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-collapsed-macos_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-expanded-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-expanded-macos_2x.png)

In a settings window, the toolbar can use [SF Symbols](../foundations/sf-symbols) to harmonize with the appearance of the main window, but the title position remains above the toolbar buttons. When needed for clarity, individual toolbar buttons can include color. To indicate the active pane, the window applies a system-provided selection appearance to the selected toolbar button.
> 설정 창에서 도구 모음은 SF 기호를 사용하여 기본 창 모양과 조화를 이룰 수 있지만 제목 위치는 도구 모음 단추 위에 남아 있습니다. 명확성을 위해 필요한 경우 개별 도구 모음 단추에 색상이 포함될 수 있습니다. 활성 창을 표시하기 위해 창에서 선택한 도구 모음 단추에 시스템에서 제공한 선택 모양을 적용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-settings-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-settings-macos_2x.png)

**Make every toolbar item available as a command in the menu bar.**Because people can customize the toolbar or hide it, it can’t be the only place that presents a command. In contrast, it doesn’t make sense to provide a toolbar item for every menu item because not all menu commands are important enough or used often enough to warrant space in the toolbar.
> 메뉴 모음에서 모든 도구 모음 항목을 명령으로 사용할 수 있도록 합니다.사용자가 도구 모음을 사용자 지정하거나 숨길 수 있기 때문에 명령을 표시하는 유일한 장소일 수 없습니다. 반대로 모든 메뉴 명령이 도구 모음의 공간을 보장할 만큼 충분히 중요하거나 자주 사용되는 것은 아니기 때문에 모든 메뉴 항목에 도구 모음 항목을 제공하는 것은 의미가 없습니다.
>




**DEVELOPER NOTE**Toolbar items automatically use the large control size. The exception is an integrated toolbar-title bar area — such as the one in a Safari window — which continues to use the regular control size. You can use constraints if you need to specify minimum or maximum sizes for a toolbar control.
> 개발자 참고 도구 모음 항목은 자동으로 큰 컨트롤 크기를 사용합니다. 예외는 일반 제어 크기를 계속 사용하는 통합 도구 모음 제목 표시줄 영역(예: Safari 창의 영역)입니다. 도구 모음 컨트롤의 최소 또는 최대 크기를 지정해야 하는 경우 제약 조건을 사용할 수 있습니다.
>




**Use recommended sizes if you need to create a custom image for a toolbar item.** To create a custom interface icon, use a maximum size of 19x19 px (38x38 px @2x). To create a full-color freestanding toolbar icon, use the PNG format and provide @1x version that measures 32x32 px and a @2x version that measures 64x64 px. If you use a recognizable full-color icon from elsewhere, don’t change its appearance or perspective.
> 도구 모음 항목에 대한 사용자 지정 이미지를 생성해야 하는 경우 권장 크기를 사용하십시오. 사용자 지정 인터페이스 아이콘을 생성하려면 19x19px(38x38px@2x)의 최대 크기를 사용하십시오. 전체 색상의 독립형 도구 모음 아이콘을 생성하려면 PNG 형식을 사용하여 32x32px를 측정하는 @1x 버전과 64x64px를 측정하는 @2x 버전을 제공합니다. 다른 곳에서 인식 가능한 전체 색상 아이콘을 사용하는 경우 모양이나 관점을 변경하지 마십시오.
>




**In general, avoid giving a toolbar item a persistent selected appearance.** The system adds a rounded-rectangle background to an item only when people move the pointer over it or choose it, removing the appearance when the item performs its action or the pointer moves away. There are two exceptions to this behavior. One is a segmented control that shows a persistent selected appearance within the context of the control — such as the view controls in a Finder window toolbar — and the second is in a settings window that uses toolbar items as pane switchers.
> 일반적으로 도구 모음 항목에 지속적으로 선택된 모양을 지정하지 마십시오. 시스템은 사용자가 포인터를 항목 위로 이동하거나 선택할 때만 항목에 둥근 직사각형 배경을 추가하여 해당 작업을 수행하거나 포인터가 이동할 때 모양을 제거합니다. 이 동작에는 두 가지 예외가 있습니다. 하나는 Finder 창 도구 모음의 보기 컨트롤과 같이 컨트롤의 컨텍스트 내에서 지속적으로 선택된 모양을 보여주는 세그먼트화된 컨트롤이고, 두 번째 컨트롤은 도구 모음 항목을 창 전환기로 사용하는 설정 창에 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/sidebar-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/sidebar-macos_2x.png)

**Consider letting people hide the toolbar, in addition to automatically hiding it in full-screen mode.** Sometimes people appreciate being able to hide the toolbar to minimize distractions or reveal more content. If you support this action, provide commands for hiding and revealing the toolbar in the [View menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/#view-menu). In full-screen mode, it can work well to hide the toolbar if people don’t need it to accomplish the focused task. For example, Preview hides the toolbar in a full-screen window because people are more likely to view content than to annotate it. If you hide the toolbar in a full-screen window, reveal it (along with the menu bar) when the pointer moves to the top of the screen.
> 사용자가 도구 모음을 전체 화면 모드에서 자동으로 숨길 수 있을 뿐만 아니라 숨길 수 있도록 허용하는 것을 고려해 보십시오. 때때로 사용자는 도구 모음을 숨겨 산만함을 최소화하거나 더 많은 내용을 표시할 수 있습니다. 이 작업을 지원하는 경우 보기 메뉴에서 도구 모음을 숨기거나 표시하기 위한 명령을 제공합니다. 전체 화면 모드에서는 사람들이 집중적인 작업을 수행하는 데 도구 모음이 필요하지 않은 경우 도구 모음을 숨기는 것이 잘 작동할 수 있습니다. 예를 들어, 미리 보기는 사용자가 주석을 달기보다는 내용을 볼 가능성이 높기 때문에 도구 모음을 전체 화면 창에서 숨깁니다. 도구 모음을 전체 화면 창에서 숨기는 경우 포인터가 화면 상단으로 이동하면 메뉴 모음과 함께 표시합니다.
>




**Consider letting people click nondestructive toolbar items when a window is inactive.** Usually, clicking the toolbar of an inactive window brings the window to the front. In some cases, it may be useful to let people invoke a toolbar item without bringing the window to the front so they can stay focused on a task in a different window. The toolbar of the standard Fonts panel behaves this way.
> 창이 비활성 상태일 때 사용자가 비파괴 도구 모음 항목을 클릭하도록 허용하는 것이 좋습니다. 일반적으로 비활성 창의 도구 모음을 클릭하면 창이 맨 앞으로 이동합니다. 경우에 따라 사용자가 창을 앞으로 가져오지 않고 도구 모음 항목을 호출하여 다른 창에서 작업에 집중할 수 있도록 하는 것이 유용할 수 있습니다. 표준 글꼴 패널의 도구 모음은 이러한 방식으로 작동합니다.
>




**Consider adding spring-loading support to toolbar items.** On pressure-sensitive systems, such as systems with the Magic Trackpad, spring loading lets people activate a button or segmented control segment by dragging items over it and force clicking — that is, pressing harder — without dropping the items. People can then continue dragging the items, possibly to perform additional actions. In Calendar, for example, people can drag an event over the day, week, month, or year segments in the toolbar. Force clicking a segment switches the calendar view without releasing the event, so people can drop the event at the desired location in the new calendar view.
> 스프링 로드 지원을 도구 모음 항목에 추가하는 것이 좋습니다. Magic Trackpad가 있는 시스템과 같이 압력에 민감한 시스템에서는 스프링 로드를 사용하여 사용자가 단추 또는 세그먼트 컨트롤 세그먼트를 활성화하고 항목을 떨어뜨리지 않고 항목을 끌어다 클릭(더 세게 누름)할 수 있습니다. 그런 다음 사용자는 항목을 계속 끌어서 추가 작업을 수행할 수 있습니다. 예를 들어, 일정관리에서 사용자는 도구 모음의 일, 주, 월 또는 연도 세그먼트에 이벤트를 끌 수 있습니다. 세그먼트를 강제로 클릭하면 이벤트를 해제하지 않고 일정관리 보기가 전환되므로 사용자는 새 일정관리 보기에서 원하는 위치에 이벤트를 놓을 수 있습니다.
>




# **watchOS**

A toolbar button lets you offer important app functionality in a view that displays related content. Located at the top of a scrolling view, a toolbar button can stay hidden behind the navigation bar until people reveal it by scrolling up.
> 도구 모음 단추를 사용하면 관련 콘텐츠를 표시하는 보기에서 중요한 앱 기능을 제공할 수 있습니다. 스크롤 보기의 맨 위에 위치한 도구 모음 단추는 사용자가 스크롤하여 표시할 때까지 탐색 모음 뒤에 숨겨져 있을 수 있습니다.
>




Toolbar buttons are available in watchOS 7 and later; for developer guidance, see [ToolbarItemPlacement.primaryAction.](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/primaryaction)
> 툴바 버튼은 시계에서 사용할 수 있습니다.OS 7 이상. 개발자 지침은 도구 모음을 참조하십시오.ItemPlacement.primaryAction.
>




**Place a toolbar button only in a scrolling view.** People frequently scroll to the top of a scrolling view, so discovering a toolbar button is almost automatic. Placing a toolbar button in a nonscrolling view makes it permanently visible, eliminating the advantage of hiding it when it’s not needed.
> 스크롤 보기에만 도구 모음 단추를 배치합니다. 사용자가 스크롤 보기의 맨 위로 스크롤하는 경우가 많기 때문에 도구 모음 단추를 검색하는 것은 거의 자동으로 수행됩니다. 스크롤하지 않는 보기에 도구줄 단추를 놓으면 도구줄 단추가 영구적으로 표시되므로 필요하지 않을 때 도구줄 단추를 숨길 수 있습니다.
>




**Use a toolbar button for an important action that isn’t a primary app function.** A toolbar button gives you the flexibility to offer important functionality in a view whose primary purpose is related to that functionality, but may not be the same. For example, Mail provides the essential New Message action in a toolbar button at the top of the Inbox view. The primary purpose of the Inbox is to display a scrollable list of email messages, so it makes sense to offer the closely related compose action in a toolbar button at the top of the view.
> 기본 앱 기능이 아닌 중요한 작업에는 도구 모음 단추를 사용합니다. 도구 모음 단추를 사용하면 해당 기능과 관련된 주요 목적을 가진 보기에서 중요한 기능을 제공할 수 있지만 동일하지 않을 수도 있습니다. 예를 들어, 메일은 받은 문서 보기의 맨 위에 있는 도구줄 단추에서 기본적인 새 메시지 수행을 제공합니다. 받은 편지함의 기본 목적은 스크롤 가능한 전자 메일 메시지 목록을 표시하는 것이므로 보기 맨 위의 도구 모음 단추에서 밀접하게 관련된 작성 작업을 제공하는 것이 좋습니다.
>




**Prefer a single, full-width toolbar button.** Displaying multiple toolbar buttons — whether stacked or side by side — can complicate the view and require people to make sure they’ve discovered the full set of actions before making a choice. If you’re considering more than one toolbar button, also consider whether your app needs a separate view to enable these essential actions.
> 여러 개의 도구 모음 단추를 겹치거나 나란히 표시하면 보기가 복잡해지고 사용자가 선택하기 전에 전체 작업 집합을 발견했는지 확인해야 합니다. 두 개 이상의 도구 모음 단추를 고려하는 경우 이러한 필수 작업을 활성화하기 위해 앱에 별도의 보기가 필요한지 여부도 고려하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-revealed_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-revealed_2x.png)

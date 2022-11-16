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


# **[components-navigation-and-search] tab-bars**

## Tab bars use bar items to navigate between mutually exclusive panes of content in the same view.
> 탭 표시줄은 막대 항목을 사용하여 동일한 보기에서 상호 배타적인 내용 영역 간을 이동합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-bar-intro-dark_2x.png)

Tab bars help people understand the different types of information or functionality that a view provides. They also let people quickly switch between sections of the view while preserving the current navigation state within each section.
> 탭 표시줄은 보기가 제공하는 다양한 유형의 정보 또는 기능을 이해하는 데 도움이 됩니다. 또한 각 섹션 내에서 현재 네비게이션 상태를 유지하면서 보기 섹션 간에 빠르게 전환할 수 있습니다.
>




See [Tab views](../components/layout-and-organization/tab-views) for the similar component in macOS.
> macOS의 유사한 구성 요소는 탭 보기를 참조하십시오.
>




# **Best practices**

**Use a tab bar only to enable navigation, not to help people perform actions.** A tab bar lets people navigate among different areas of an app, like the Alarm, Stopwatch, and Timer tabs in the Clock app. If you need to provide controls that act on elements in the current view, use a [toolbar](../components/menus-and-actions/toolbars) instead.
> 탭 모음은 사람들이 작업을 수행하는 데 도움이 되지 않고 탐색을 활성화하는 데만 사용합니다. 탭 모음을 사용하면 사람들이 시계 앱의 경보, 중지 및 타이머 탭과 같은 앱의 여러 영역을 탐색할 수 있습니다. 현재 뷰의 요소에 작용하는 컨트롤을 제공해야 하는 경우 대신 도구 모음을 사용하십시오.
>




**Make sure the tab bar is visible when people navigate to different areas in your app.** The exception is a tab bar within a modal view. Because a modal view gives people a separate experience that they dismiss when they’re finished, hiding the view’s tab bar doesn’t affect app navigation.
> 사용자가 앱의 다른 영역으로 이동할 때 탭 표시줄이 표시되는지 확인하십시오. 모달 보기 내의 탭 표시줄은 예외입니다. 모달 뷰는 사용자가 완료되면 무시할 수 있는 별도의 경험을 제공하기 때문에 뷰의 탭 표시줄을 숨기는 것은 앱 탐색에 영향을 미치지 않습니다.
>




**Use the minimum number of tabs required to help people navigate your app.** Each additional tab increases the complexity of your app, making it harder for people to locate information. Aim for a few tabs with short titles or icons to avoid crowding and causing tabs to truncate. In general, use three to five tabs in iOS; use a few more in iPadOS and tvOS if necessary.
> 사용자가 앱을 탐색하는 데 필요한 최소 탭 수를 사용하십시오. 탭이 추가될 때마다 앱의 복잡성이 증가하여 사용자가 정보를 찾기가 더 어려워집니다. 짧은 제목이나 아이콘이 있는 몇 개의 탭을 목표로 하여 탭이 잘리지 않도록 합니다. 일반적으로 iOS에서는 3~5개의 탭을 사용하고, 필요한 경우 iPadOS와 tvOS에서는 몇 개의 탭을 더 사용합니다.
>




**Keep tabs visible even when their content is unavailable.** If tabs are enabled in some cases but not in others, your app’s interface might appear unstable and unpredictable. When necessary, explain why a tab’s content is unavailable. For example, even when there is no music on an iOS device, the Listen Now tab in the Music app remains available and offers suggestions for downloading music.
> 콘텐츠를 사용할 수 없는 경우에도 탭을 계속 볼 수 있습니다. 탭이 활성화되어 있지만 다른 경우에는 활성화되어 있지 않으면 앱의 인터페이스가 불안정하고 예측할 수 없는 것처럼 보일 수 있습니다. 필요한 경우 탭의 내용을 사용할 수 없는 이유를 설명합니다. 예를 들어 iOS 장치에 음악이 없는 경우에도 음악 앱의 지금 듣기 탭을 사용할 수 있으며 음악 다운로드에 대한 제안을 제공합니다.
>




**Use concrete nouns or verbs as tab titles.** A good tab title helps people navigate by clearly describing the type of content people find when they select the tab. Consider nouns for category titles like Music, Movies, TV Shows, and Sports, and verbs or short verb phrases for things related to time or peoples’ perspectives on the content (like Watch Now or For You).
> 탭 제목으로 구체적인 명사나 동사를 사용하라. 좋은 탭 제목은 사람들이 탭을 선택할 때 찾을 수 있는 내용의 유형을 명확하게 설명함으로써 사람들이 탐색하는 것을 돕는다. 음악, 영화, TV 쇼, 스포츠와 같은 범주 제목에는 명사를, 콘텐츠에 대한 시간 또는 사람들의 관점과 관련된 것에는 동사 또는 짧은 동사 구문을 고려하십시오(예: 지금 시청 또는 당신을 위해).
>




**Be cautious of overcrowding tabs with functionality.** Tabs represent an app’s menu of options. Tabs titled “Home” tend to be too large in scope for an app. Aim to create focus by representing specific and descriptive categories of content or functionality on each tab.
> 탭은 앱의 옵션 메뉴를 나타냅니다. "홈"이라는 제목의 탭은 앱에 비해 범위가 너무 큰 경향이 있습니다. 각 탭에서 내용 또는 기능의 구체적이고 설명적인 범주를 표현하여 포커스를 만드는 것을 목표로 합니다.
>




# **Platform considerations**

*Not supported in macOS or watchOS.*
> macOS 또는 watch에서 지원되지 않음운영 체제
>




# **iOS, iPadOS**

By default, a tab bar is translucent: It uses a background material only when content appears behind it, removing the material when the view scrolls to the bottom. A tab bar hides when a keyboard is onscreen.
> 기본적으로 탭 표시줄은 반투명합니다. 내용이 뒤에 나타날 때만 배경 재료를 사용하고, 보기가 아래로 스크롤될 때 재료를 제거합니다. 키보드가 화면에 나타나면 탭 표시줄이 숨겨집니다.
>




**Avoid overflow tabs whenever possible.** Depending on device size and orientation, the number of visible tabs can be smaller than the total number of tabs. If horizontal space limits the number of visible tabs, the trailing tab becomes a More tab, revealing the remaining items in a list on a separate screen. The More tab makes it harder for people to reach and notice content on tabs that are hidden, so try to limit scenarios in your app where this can happen.
> 장치 크기 및 방향에 따라 표시되는 탭의 수가 총 탭 수보다 적을 수 있습니다. 수평 공간으로 표시되는 탭의 수가 제한되면 후행 탭이 추가 탭이 되어 별도의 화면에 목록의 나머지 항목이 표시됩니다. 추가 탭을 사용하면 숨겨진 탭의 콘텐츠에 사람들이 접근하고 알아차리기가 더 어려워지므로, 앱에서 이러한 상황이 발생할 수 있는 시나리오를 제한하도록 하십시오.
>




**In an iPadOS app, consider using a sidebar instead of a tab bar.**Because a sidebar can display a large number of items, it can make navigating an iPad app more efficient. You can also let people customize a sidebar’s items and let them hide it to make more room for content. For guidance, see [Sidebars](../components/navigation-and-search/sidebars).
> iPadOS 앱에서 탭 표시줄 대신 사이드바를 사용하는 것을 고려해 보십시오.사이드바는 많은 항목을 표시할 수 있기 때문에 iPad 앱을 더 효율적으로 탐색할 수 있습니다. 또한 사용자가 사이드바의 항목을 사용자 정의하고 숨길 수 있도록 하여 내용을 저장할 수 있습니다. 자세한 내용은 사이드바를 참조하십시오.
>




**Ensure that tabs affect the view that’s attached to the tab bar, not views elsewhere onscreen.** For example, make sure selecting a tab on the left side of a split view doesn’t cause the right side of the split view to change.
> 탭이 화면의 다른 보기가 아니라 탭 표시줄에 연결된 보기에 영향을 주는지 확인하십시오. 예를 들어 분할 보기의 왼쪽에서 탭을 선택해도 분할 보기의 오른쪽이 변경되지 않는지 확인하십시오.
>




**Use a badge to communicate unobtrusively.** You can display a badge — a red oval containing white text and either a number or an exclamation point — on a tab to indicate that new information associated with that view or mode is available. For guidance, see [Notifications](../components/system-experiences/notifications).
> 배지를 사용하여 눈에 띄지 않게 통신합니다. 배지(흰색 텍스트와 숫자 또는 느낌표가 포함된 빨간색 타원형)를 탭에 표시하여 해당 보기 또는 모드와 관련된 새 정보를 사용할 수 있음을 나타낼 수 있습니다. 자세한 내용은 통지를 참조하십시오.
>




**Consider using SF Symbols to provide scalable, visually consistent tab bar items.** When you use [SF Symbols](../foundations/sf-symbols), tab bar items automatically adapt to different contexts. For example, the tab bar can be regular or compact, depending on the current device and orientation. Also, tab bar icons can appear above tab titles in portrait orientation, whereas in landscape, the icons and titles can appear side by side. Prefer filled symbols or icons for consistency with the platform. If your app uses a sidebar instead of a tab bar when it runs on iPad, switch the filled symbols or icons to the outlined variant in the sidebar.
> 확장 가능하고 시각적으로 일관된 탭 모음 항목을 제공하기 위해 SF 기호를 사용하는 것을 고려하십시오. SF 기호를 사용할 때 탭 모음 항목은 자동으로 다른 컨텍스트에 적용됩니다. 예를 들어 현재 장치 및 방향에 따라 탭 표시줄은 일반 또는 소형일 수 있습니다. 또한 탭 표시줄 아이콘은 세로 방향으로 탭 제목 위에 표시될 수 있지만 가로 방향에서는 아이콘과 제목이 나란히 표시될 수 있습니다. 플랫폼과의 일관성을 위해 채워진 기호 또는 아이콘을 선호합니다. 앱이 iPad에서 실행될 때 탭 표시줄 대신 사이드바를 사용하는 경우, 채워진 기호나 아이콘을 사이드바의 윤곽이 잡힌 변형으로 전환합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/tab-bar-landscape_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/tab-bar-landscape_2x.png)

If you need to create custom tab bar icons using bitmaps, create each icon in two sizes so that the tab bar looks good in both regular and compact environments. Use the following metrics when creating tab bar icons in different shapes. For guidance, see [Icons](../foundations/icons).
> 비트맵을 사용하여 사용자 지정 탭 모음 아이콘을 만들어야 하는 경우 일반 환경과 소형 환경 모두에서 탭 모음이 잘 보이도록 각 아이콘을 두 가지 크기로 만듭니다. 탭 표시줄 아이콘을 다른 모양으로 만들 때 다음 메트릭을 사용합니다. 자세한 내용은 아이콘을 참조하십시오.
>




**Target width and height (circular icons)**
> 대상 너비 및 높이(원형 아이콘)
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/max-width-height-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/max-width-height-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 25x25 pt (75x75 px @3x) | 18x18 pt (54x54 px @3x) |
| 25x25 pt (50x50px @2x) | 18x18 pt (36x36 px @2x) |

**Target width and height (square icons)**
> 대상 너비 및 높이(사각 아이콘)
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 23x23 pt (69x69 px @3x) | 17x17 pt (51x51 px @3x) |
| 23x23 pt (46x46 px @2x) | 17x17 pt (34x34 px @2x) |

**Target width (wide icons)**

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-height-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-height-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 31pt (93px @3x) | 23pt (69px @3x) |
| 31pt (62px @2x) | 23pt (46px @2x) |

**Target height (tall icons)**

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-height-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-height-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 28pt (84px @3x) | 20pt (60px @3x) |
| 28pt (56px @2x) | 20pt (40px @2x) |

# **macOS**

Tab bars aren’t available in macOS. Instead, [tab views](../components/layout-and-organization/tab-views) perform a similar function.
> MacOS에서는 탭 바를 사용할 수 없습니다. 대신 탭 보기도 유사한 기능을 수행합니다.
>




# **tvOS**

A tab bar is highly customizable. For example, you can:
> 탭 표시줄은 사용자 정의가 용이합니다. 예를 들어, 다음을 수행할 수 있습니다.
>




- Specify a tint, color, or image for the tab bar background
- >  탭 표시줄 배경에 대한 색조, 색상 또는 이미지 지정

- Choose a font for tab items, including a different font for the selected item
- >  선택한 항목에 대한 다른 글꼴을 포함하여 탭 항목에 대한 글꼴

- Specify tints for selected and unselected items
- >  선택한 항목과 선택하지 않은 항목에 대한 색조 지정

- Add button icons, like settings and search
- >  설정 및 검색과 같은 단추 아이콘 추가


By default, a tab bar is translucent, and only the selected tab is opaque. When people use the remote to focus on the tab bar, the selected tab includes a drop shadow that emphasizes its selected state. The height of a tab bar is 68 points, and its top edge is 46 points from the top of the screen; you can’t change either of these values.
> 기본적으로 탭 표시줄은 반투명하며 선택한 탭만 불투명합니다. 사용자가 리모컨을 사용하여 탭 표시줄에 초점을 맞출 때 선택한 탭에는 선택한 상태를 강조하는 드롭 섀도가 포함됩니다. 탭 모음의 높이는 68점이고 상단 가장자리는 화면 상단에서 46점이므로 이러한 값을 변경할 수 없습니다.
>




If there are more items than can fit in the tab bar, the system truncates the rightmost item by applying a fade effect that begins at the right side of the tab bar. If there are enough items to cause scrolling, the system also applies a truncating fade effect that starts from the left side.
> 탭 표시줄에 들어갈 수 있는 것보다 많은 항목이 있는 경우 시스템은 탭 표시줄의 오른쪽에서 시작되는 페이드 효과를 적용하여 맨 오른쪽 항목을 잘라냅니다. 스크롤을 유발할 만큼 충분한 항목이 있는 경우 시스템은 왼쪽에서 시작하는 잘라내기 페이드 효과도 적용합니다.
>




**If you use an icon for a tab title, make sure it’s familiar.** You can use icons as tab titles to help save space, but only for universally recognized symbols like search or settings. Using an unfamiliar symbol without a descriptive title can confuse people. For guidance, see [SF Symbols](../foundations/sf-symbols).
> 아이콘을 탭 제목으로 사용할 경우 아이콘을 탭 제목으로 사용하여 공간을 절약할 수 있지만 검색 또는 설정과 같이 일반적으로 인식되는 기호에 대해서만 사용할 수 있습니다. 설명적인 제목 없이 낯선 기호를 사용하는 것은 사람들을 혼란스럽게 할 수 있다. 자세한 내용은 SF 기호를 참조하십시오.
>




**Be aware of tab bar scrolling behaviors.** By default, people can scroll the tab bar offscreen when the current tab contains a single main view. You can see examples of this behavior in the Watch Now, Movies, TV Show, Sports, and Kids tabs in the TV app. The exception is when a screen contains a split view, such as the TV app's Library tab or an app's Settings screen. In this case, the tab bar remains pinned at the top of the view while people scroll the content within the primary and secondary panes of the split view. Regardless of a tab's contents, focus always returns to the tab bar at the top of the page when people press Menu on the remote.
> 탭 모음 스크롤 동작에 주의하십시오. 기본적으로 현재 탭에 기본 보기가 하나만 있으면 사용자가 탭 모음을 화면 밖으로 스크롤할 수 있습니다. TV 앱의 지금 시청, 영화, TV 쇼, 스포츠 및 어린이 탭에서 이러한 동작의 예를 볼 수 있습니다. 예외는 화면에 TV 앱의 라이브러리 탭이나 앱의 설정 화면과 같은 분할 보기가 포함되어 있는 경우입니다. 이 경우 탭 표시줄은 분할 보기의 기본 및 보조 창에서 내용을 스크롤하는 동안 보기 맨 위에 고정되어 있습니다. 탭의 내용에 상관없이 리모컨에서 메뉴를 누르면 항상 페이지 상단의 탭 표시줄로 포커스가 돌아갑니다.
>




**In a live-viewing app, organize tabs in a consistent way.** For the best experience, organize content in live-streaming apps with tabs in the following order:
> 라이브 뷰잉 앱에서는 탭을 일관된 방식으로 구성합니다. 최상의 경험을 위해 다음 순서로 탭을 사용하여 라이브 스트리밍 앱의 콘텐츠를 구성합니다.
>




- Live content
- Cloud DVR or other recorded content
- >  클라우드 DVR 또는 기타 녹화된 콘텐츠

- Other content

For additional guidance, see [Live-viewing apps](../patterns/live-viewing-apps).

**Create a branded logo image to display next to the leading or trailing end of the tab bar, if it makes sense in your app.** To ensure enough room between the branded logo image and the edge of the tab bar, place the image within the safe margin. Use the following image size values for guidance:
> 앱에서 적합한 경우 탭 모음의 선행 또는 후행 끝 옆에 표시할 브랜드 로고 이미지를 만듭니다. 브랜드 로고 이미지와 탭 모음의 가장자리 사이에 충분한 공간을 확보하려면 이미지를 안전한 여백 안에 놓으십시오. 지침으로 다음 영상 크기 값을 사용합니다.
>




| Maximum width | Maximum height |
| --- | --- |
| 200 pt | 68 pt |

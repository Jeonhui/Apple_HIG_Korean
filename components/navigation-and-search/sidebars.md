# **[components-navigation-and-search] sidebars**

## A sidebar enables app navigation and provides quick access to top-level collections of content in your app or game.
> 사이드바를 사용하면 앱 탐색이 가능하고 앱 또는 게임의 최상위 콘텐츠 모음에 빠르게 액세스할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/sidebar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/sidebar-intro-dark_2x.png)

The term *sidebar* refers to a list of top-level app areas and collections, almost always displayed in the primary pane of a [split view](../components/layout-and-organization/split-views). When people choose an item in a sidebar, the split view displays the item’s details in a secondary pane or — if the item contains a list — the secondary pane presents the list and a tertiary pane presents the details. For example, Mail in iOS, iPadOS, and macOS uses sidebar styling and behavior to display the list of accounts and mailboxes, typically displaying the message list in a secondary pane and a message’s content in a tertiary pane.
> 사이드바라는 용어는 거의 항상 분할 보기의 기본 창에 표시되는 최상위 앱 영역 및 컬렉션 목록을 나타냅니다. 사용자가 사이드바에서 항목을 선택하면 분할 보기는 항목의 세부사항을 보조 영역에 표시하거나(항목에 목록이 포함된 경우) 보조 영역은 목록을 표시하고 세 번째 영역은 세부사항을 표시합니다. 예를 들어 iOS, iPadOS 및 macOS의 메일은 사이드바 스타일 및 동작을 사용하여 계정 및 사서함 목록을 표시합니다. 일반적으로 메시지 목록은 보조 창에 표시되고 메시지 내용은 보조 창에 표시됩니다.
>




A sidebar layout can take a lot of horizontal space, especially if you want the sidebar and its accompanying panes to be visible onscreen at the same time. In a compact environment, you might want to consider an alternative component, like a [tab bar](../components/navigation-and-search/tab-bars).
> 사이드바 레이아웃은 특히 사이드바와 함께 제공되는 창을 동시에 화면에 표시하려는 경우 많은 수평 공간을 차지할 수 있습니다. 소형 환경에서는 탭 표시줄과 같은 대체 구성 요소를 고려할 수 있습니다.
>




**DEVELOPER NOTE**When you use SwiftUI to construct a sidebar interface, you automatically get platform-appropriate appearance and behavior. For developer guidance, see [ColumnNavigationViewStyle](https://developer.apple.com/documentation/swiftui/columnnavigationviewstyle). If you don’t use SwiftUI, you can instead use [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/) or [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/).
> 개발자 참고 스위프트를 사용할 때사이드바 인터페이스를 구성하는 UI는 플랫폼에 적합한 모양과 동작을 자동으로 가져옵니다. 개발자 지침은 열 탐색 뷰 스타일을 참조하십시오. Swift를 사용하지 않는 경우UI에서 대신 UISplitViewController 또는 NSSplitViewController를 사용할 수 있습니다.
>




# **Best practices**

**Use a sidebar to enable quick navigation to key areas of your app or top-level collections of content, like folders and playlists.** A sidebar can help you flatten your information hierarchy, giving people access to several peer information categories or modes at the same time.
> 사이드바를 사용하여 앱의 주요 영역이나 폴더 및 재생 목록과 같은 최상위 콘텐츠 모음으로 빠르게 이동할 수 있습니다. 사이드바는 정보 계층을 평평하게 만드는 데 도움이 되어 사람들이 여러 피어 정보 범주 또는 모드에 동시에 액세스할 수 있도록 합니다.
>




**When possible, let people customize the contents of a sidebar.** A sidebar lets people navigate to important areas in your app, so it works well when people can decide which areas are most important and in what order they should appear.
> 사이드바를 사용하면 사용자가 앱의 중요한 영역으로 이동할 수 있으므로 사용자가 가장 중요한 영역과 표시할 순서를 결정할 수 있습니다.
>




**Consider letting people hide the sidebar.** People sometimes want to hide the sidebar to create more room for content details. When possible, let people hide and show the sidebar using the platform-specific interactions they already know. For example, in iPadOS, people expect to use the built-in edge swipe gesture; in macOS, you can include a show/hide button or add Show Sidebar and Hide Sidebar commands to your app’s View menu. Avoid hiding the sidebar by default to ensure that it remains discoverable.
> 사람들이 사이드바를 숨기도록 허용하는 것을 고려해 보십시오. 사람들은 때때로 내용 세부사항을 위한 공간을 더 많이 만들기 위해 사이드바를 숨기려고 합니다. 가능한 경우 사용자가 이미 알고 있는 플랫폼별 상호 작용을 사용하여 사이드바를 숨기고 표시하도록 합니다. 예를 들어, iPadOS에서는 기본 제공 에지 스와이프 제스처를 사용할 것으로 예상합니다. macOS에서는 표시/숨기기 단추를 포함하거나 사이드바 표시 및 사이드바 숨기기 명령을 앱의 보기 메뉴에 추가할 수 있습니다. 검색 가능한 상태를 유지하려면 사이드바를 기본적으로 숨기지 마십시오.
>




**In general, show no more than two levels of hierarchy in a sidebar.**When a data hierarchy is deeper than two levels, consider using a split view interface that includes a content list between the sidebar items and detail view.
> 일반적으로 사이드바에 세 단계 이하의 계층을 표시합니다.데이터 계층이 두 수준보다 깊은 경우 사이드바 항목과 상세 보기 사이에 내용 목록이 포함된 분할 보기 인터페이스를 사용하는 것이 좋습니다.
>




**If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group.** To help keep labels short, omit unnecessary words. For example, Mail omits the word *Messages* from the title of each mailbox, using more concise terms like *Flagged* and *Drafts*.
> 사이드바에 두 단계의 계층을 포함해야 할 경우, 간결하고 설명적인 레이블을 사용하여 각 그룹의 제목을 지정하십시오. 레이블을 짧게 유지하려면 불필요한 단어를 생략하십시오. 예를 들어, 메일은 플래그 지정 및 초안과 같은 더 간결한 용어를 사용하여 각 사서함 제목에서 메시지라는 단어를 생략합니다.
>




# **Platform considerations**

*No additional considerations for tvOS. Not supported in watchOS.*
> TVOS에 대한 추가 고려 사항은 없습니다. 워치에서 지원되지 않음운영 체제
>




# **iOS, iPadOS**

**In an iOS app, consider using a tab bar instead of a sidebar.** A sidebar interface can require a lot of horizontal space, which might make it too crowded on iPhone, especially in portrait orientation. In contrast, a tab bar works well to let people quickly switch between top-level sections in your app while preserving the current navigation state within each section.
> iOS 앱에서 사이드바 대신 탭 바를 사용하는 것을 고려해 보십시오. 사이드바 인터페이스는 많은 수평 공간을 필요로 할 수 있으므로 아이폰에서 특히 세로 방향으로 너무 붐빌 수 있습니다. 이와는 대조적으로 탭 바는 각 섹션 내에서 현재 탐색 상태를 유지하면서 앱의 최상위 섹션 사이를 빠르게 전환할 수 있게 해줍니다.
>




**In an iPadOS app, consider using a sidebar instead of a tab bar.**Because a sidebar can display a large number of items, it can make navigating an iPad app more efficient. You can also let people customize a sidebar’s items and let them hide it to make more room for content.
> iPadOS 앱에서 탭 표시줄 대신 사이드바를 사용하는 것을 고려해 보십시오.사이드바는 많은 항목을 표시할 수 있기 때문에 iPad 앱을 더 효율적으로 탐색할 수 있습니다. 또한 사용자가 사이드바의 항목을 사용자 정의하고 숨길 수 있도록 하여 내용을 저장할 수 있습니다.
>




**If necessary, apply the correct appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar, you can use the sidebar appearance of a collection view list layout. For developer guidance, see [UICollectionLayoutListConfiguration.Appearance](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration/appearance).
> 필요한 경우 사이드바에 올바른 모양을 적용합니다. Swift를 사용하지 않는 경우UI를 사용하여 사이드바를 만들 수 있으며, 컬렉션 뷰 목록 레이아웃의 사이드바 모양을 사용할 수 있습니다. 개발자 지침은 UICollection 레이아웃 목록 구성을 참조하십시오.외모.
>




# **macOS**

In macOS, a sidebar — also known as a *source list* — extends to the full height of the window, and uses a rounded-corner appearance for the selected-item highlight.
> macOS에서 사이드바(소스 목록이라고도 함)는 창 전체 높이까지 확장되며 선택한 항목 강조 표시에 둥근 모서리 모양을 사용합니다.
>




A sidebar’s row height, text, and glyph size depend on its overall size, which can be small, medium, or large. You can set the size programmatically, but people can also change it by selecting a different sidebar icon size in General settings. The table below shows the default metrics for a sidebar in macOS.
> 사이드바의 행 높이, 텍스트 및 문자 크기는 전체 크기에 따라 달라지며, 크기는 작거나 중간이거나 클 수 있습니다. 크기는 프로그래밍 방식으로 설정할 수 있지만 일반 설정에서 다른 사이드바 아이콘 크기를 선택하여 변경할 수도 있습니다. 아래 표는 macOS의 사이드바에 대한 기본 메트릭을 보여줍니다.
>




| Sidebar size | Sidebar component | Default metrics |
| --- | --- | --- |
| Small | Row height | 24 pt |
| SF Symbol scale | Medium * |  |
| Icon size | 16x16 px @1x |  |
| Text size (style) | 11 pt (Subhead) |  |
| Medium | Row height | 28 pt |
| SF symbol scale | Medium |  |
| Icon size | 20x20 px @1x |  |
| Text size (style) | 13 pt (Body) |  |
| Large | Row height | 32 pt |
| SF Symbol scale | Medium |  |
| Icon size | 24x24 px @1x |  |
| Text size (style) | 15 pt (Title 3) |  |
| All | Horizontal spacing between cells | 17 pt |
| Vertical spacing between cells | 0 pt |  |
- In some cases, a small sidebar uses small-scale SF Symbols by default.
- >  작은 사이드바가 기본적으로 작은 크기의 SF 기호를 사용하는 경우도 있습니다.


**Consider using familiar symbols to represent items in the sidebar.** [SF Symbols](../sf-symbols/overview/) provides a wide range of customizable symbols you can use to represent items in your app. If you need to use a bitmap image to create a custom interface icon for the sidebar, create the image in both @1x and @2x resolutions and in the small, medium, and large sizes shown in the table above.
> 친숙한 기호를 사용하여 사이드바의 항목을 표시하는 것을 고려해 보십시오. SF 기호는 앱에서 항목을 표시하는 데 사용할 수 있는 사용자 지정 가능한 광범위한 기호를 제공합니다. 사이드바에 대한 사용자 지정 인터페이스 아이콘을 만들기 위해 비트맵 이미지를 사용해야 하는 경우 @1x 및 @2x 해상도와 위 표에 표시된 소형, 중형 및 대형 크기로 이미지를 만듭니다.
>





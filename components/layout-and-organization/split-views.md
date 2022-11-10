# **[components-layout-and-organization] split-views**

## A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.
> 분할 보기는 테이블, 컬렉션, 이미지 및 사용자 정의 보기를 포함한 다양한 구성 요소를 포함할 수 있는 여러 인접 콘텐츠 창의 표시를 관리합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/split-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/split-view-intro-dark_2x.png)

Typically, you use a split view to support navigation through a hierarchy of information. In this scenario, selecting an item in the view’s primary pane displays the item’s contents in the secondary pane. Similarly, a split view can display a tertiary pane if items in the secondary pane contain additional content.
> 일반적으로 분할 보기를 사용하여 정보 계층을 통한 탐색을 지원합니다. 이 시나리오에서 보기의 기본 영역에서 항목을 선택하면 보조 영역에 항목의 내용이 표시됩니다. 마찬가지로, 보조 창의 항목이 추가 내용을 포함하는 경우 분할 보기는 3차 창을 표시할 수 있습니다.
>




It’s common to use a split view to create a [sidebar](../components/navigation-and-search/sidebars) interface, where the leading pane lists the top-level items or collections in an app, and the secondary and optional tertiary panes can present child collections and item details. For example, Mail in iPadOS lists accounts and mailboxes in the primary pane, a selected mailbox’s messages in the secondary pane, and a selected email in the tertiary pane. Rarely, you might also use a split view to provide groups of functionality that supplement the primary view — for example, Keynote in macOS uses split view panes to present the slide navigator, the presenter notes, and the inspector pane in areas that surround the main slide canvas.
> 분할 보기를 사용하여 사이드바 인터페이스를 만드는 것이 일반적입니다. 여기서 선두 창에는 앱의 최상위 항목 또는 컬렉션이 나열되고 보조 창과 선택적인 3차 창에는 하위 컬렉션 및 항목 세부 정보가 표시될 수 있습니다. 예를 들어 iPad의 메일OS에는 주 창에 계정 및 편지함, 보조 창에 선택한 편지함의 메시지, 세 번째 창에 선택한 이메일이 나열됩니다. macOS의 Keynote에서는 기본 보기를 보완하는 기능 그룹을 제공하기 위해 분할 보기를 사용할 수도 있습니다. 예를 들어, macOS의 Keynote에서는 분할 보기 창을 사용하여 기본 슬라이드 캔버스 주변 영역에 슬라이드 탐색기, 발표자 노트 및 검사자 창을 표시합니다.
>




# **Best practices**

**Prefer using a split view in a regular — not a compact — environment.**A split view needs horizontal space in which to display multiple panes. In a compact environment, such as iPhone in portrait orientation, it’s difficult to display multiple panes without wrapping or truncating the content, making it less legible and harder to interact with.
> 콤팩트한 환경이 아닌 일반 환경에서 분할 보기를 사용하는 것을 선호합니다.분할 보기에는 여러 창을 표시할 수 있는 수평 공간이 필요합니다. 세로 방향의 iPhone과 같은 컴팩트한 환경에서는 콘텐츠를 감싸거나 자르지 않고 여러 창을 표시하기가 어려워 읽기 어렵고 상호 작용이 어렵습니다.
>




**To enable navigation, persistently highlight the current selection in each pane that leads to the detail view.** The selected appearance clarifies the relationship between the content in various panes and helps people stay oriented.
> 탐색을 활성화하려면 상세 보기로 연결되는 각 창에서 현재 선택 항목을 지속적으로 강조 표시합니다. 선택한 모양은 다양한 창에서 내용 간의 관계를 명확하게 하고 사용자가 방향을 유지하도록 도와줍니다.
>




**Consider letting people drag and drop content between panes.** Because a split view provides access to multiple levels of hierarchy, people can conveniently move content from one part of your app to another by dragging items to different panes.
> 분할 보기를 통해 여러 계층 구조에 액세스할 수 있으므로, 다른 창으로 항목을 끌어다 놓으면 앱의 한 부분에서 다른 부분으로 편리하게 콘텐츠를 이동할 수 있습니다.
>




# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in watchOS.*
> iOS 또는 iPad OS에 대한 추가 고려 사항 없음. 시계에서 지원되지 않음OS.
>




# **macOS**

In macOS, you can arrange the panes of a split view horizontally, vertically, or both. A split view includes dividers between panes that can support dragging to resize them. For developer guidance, see [HSplitView](https://developer.apple.com/documentation/swiftui/hsplitview) and [VSplitView](https://developer.apple.com/documentation/swiftui/vsplitview).
> macOS에서는 분할된 뷰의 창을 수평, 수직 또는 둘 다 정렬할 수 있습니다. 분할 보기에는 크기를 조정하기 위해 끌기를 지원할 수 있는 창 사이의 구분선이 포함됩니다. 개발자 지침은 HSplitView 및 VSplitView를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/vertical-split-view_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/vertical-split-view_2x.png)

Vertical split view

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/horizontal-split-view_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/horizontal-split-view_2x.png)

Horizontal split view

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/multiple-split-view_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/multiple-split-view_2x.png)

Multiple split views

**Set reasonable defaults for minimum and maximum pane sizes.** If people can resize the panes in your app’s split view, make sure to use sizes that keep the divider visible. If a pane gets too small, the divider can seem to disappear, becoming difficult to use.
> 최소 및 최대 창 크기에 대해 적절한 기본값을 설정하십시오. 앱의 분할 보기에서 창 크기를 조정할 수 있는 경우 구분자를 계속 표시할 수 있는 크기를 사용하십시오. 창이 너무 작아지면 칸막이가 없어져 사용이 어려워질 수 있습니다.
>




**Consider letting people hide a pane when it makes sense.** If your app includes an editing area, for example, consider letting people hide other panes to reduce distractions or allow more room for editing — in Keynote, people can hide the navigator and presenter notes panes when they want to focus on editing slide content.
> 예를 들어 앱에 편집 영역이 포함되어 있는 경우 다른 창을 숨겨 주의를 분산시키거나 더 많은 편집 공간을 허용하도록 하는 키노트에서는 슬라이드 콘텐츠 편집에 집중할 때 네비게이터 및 발표자 노트 창을 숨길 수 있습니다.
>




**Provide multiple ways to reveal hidden panes.** For example, you might provide a toolbar button or a menu command — including a keyboard shortcut — that people can use to restore a hidden pane.
> 숨김 창을 표시하는 여러 가지 방법을 제공합니다. 예를 들어, 사용자가 숨김 창을 복원하는 데 사용할 수 있는 도구 모음 단추 또는 바로 가기 키를 포함한 메뉴 명령을 제공할 수 있습니다.
>




**Prefer the thin divider style.** The thin divider measures one point in width, giving you maximum space for content while remaining easy for people to use. Avoid using thicker divider styles unless you have a specific need. For example, if both sides of a divider present table rows that use strong linear elements that might make a thin divider hard to distinguish, it might work to use a thicker divider. For developer guidance, see [NSSplitView.DividerStyle](https://developer.apple.com/documentation/appkit/nssplitview/dividerstyle).
> 얇은 칸막이 스타일을 선호합니다. 얇은 칸막이는 너비가 1포인트이므로 사용자가 쉽게 사용할 수 있는 콘텐츠 공간을 최대한 확보할 수 있습니다. 특별한 필요가 없는 한 더 두꺼운 구분자 스타일을 사용하지 마십시오. 예를 들어, 칸막이의 양쪽이 강력한 선형 요소를 사용하는 테이블 행을 표시하여 얇은 칸막이를 구별하기 어렵게 만드는 경우 더 두꺼운 칸막이를 사용할 수 있습니다. 개발자 지침은 NSSplitView를 참조하십시오.구분자 스타일.
>




# **tvOS**

In tvOS, a split view can work well to enable content filtering. When people choose a filter category in the primary pane, your app can display the results in the secondary pane.
> tvOS에서 분할 보기는 콘텐츠 필터링을 활성화하는 데 효과적일 수 있다. 사람들이 기본 창에서 필터 범주를 선택하면 앱이 보조 창에 결과를 표시할 수 있습니다.
>




**Choose a split view layout that keeps the panes looking balanced.** By default, a split view devotes a third of the screen width to the primary pane and two-thirds to the secondary pane, but you can also specify a half-and-half layout.
> 창의 균형을 유지하는 분할 보기 레이아웃을 선택합니다. 기본적으로 분할 보기는 화면 너비의 3분의 1을 기본 창으로, 2/3을 보조 창으로 사용하지만 반반 레이아웃을 지정할 수도 있습니다.
>




**Display a single title above a split view, helping people understand the content as a whole.** People already know how to use a split view to navigate and filter content; they don’t need titles that describe what each pane contains.
> 단일 제목을 분할 보기 위에 표시하여 사용자가 내용을 전체적으로 이해하는 데 도움이 됩니다. 사용자는 분할 보기를 사용하여 내용을 탐색하고 필터링하는 방법을 이미 알고 있습니다. 각 창에 포함된 내용을 설명하는 제목은 필요하지 않습니다.
>





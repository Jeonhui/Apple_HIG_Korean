# **[technologies-mac-catalyst] app-structure**

iOS and macOS apps often organize data in similar ways, but they use different controls and visual indicators to help people understand and navigate through the data. When you bring your iOS app to the Mac with Mac Catalyst, plan to spend time making changes to your app’s structure and navigation so that it follows Mac conventions.
> iOS와 macOS 앱은 종종 비슷한 방식으로 데이터를 구성하지만, 사람들이 데이터를 이해하고 탐색하는 것을 돕기 위해 서로 다른 컨트롤과 시각적 표시기를 사용한다. iOS 앱을 Mac Catalyst가 설치된 Mac에 가져올 때 Mac 관례를 따르도록 앱의 구조와 탐색을 변경하는 데 시간을 할애할 계획입니다.
>




Typically, iPad apps use the following UIKit controls to organize their content and features:
> 일반적으로 아이패드 앱은 다음과 같은 UIKit 컨트롤을 사용하여 콘텐츠와 기능을 구성합니다:
>




- [Split views](../components/layout-and-organization/split-views). A split view enables hierarchical navigation which consists of a two- or three-column interface that shows a primary column, an optional supplementary column, and a secondary pane of content. Frequently, apps use the primary column to create a sidebar-based interface where changes in the sidebar drive changes in the optional supplementary column, which then affect the content in the content pane.
- >  뷰를 분할합니다. 분할 보기를 사용하면 기본 열, 선택적 보조 열 및 보조 내용 영역을 표시하는 두 열 또는 세 열 인터페이스로 구성된 계층 탐색이 가능합니다. 종종 앱은 기본 열을 사용하여 사이드바 기반 인터페이스를 만들고, 사이드바 드라이브의 변경 사항은 선택적인 보조 열에서 변경되며, 이는 콘텐츠 창의 콘텐츠에 영향을 미칩니다.

- [Tab bars](../components/navigation-and-search/tab-bars). A tab bar supports flat navigation by displaying top-level categories in a persistent bar at the bottom of the screen.
- >  탭 바. 탭 표시줄은 화면 하단의 영구 표시줄에 최상위 범주를 표시하여 평면 탐색을 지원합니다.

- [Page controls](../components/presentation/page-controls). A page control displays dots at the bottom of the screen that indicate the position of the current page in a flat list of pages.
- >  페이지 컨트롤. 페이지 컨트롤은 현재 페이지의 위치를 나타내는 점을 화면 하단에 표시합니다.


**If you use a tab bar in your iPad app, consider using a split view with a sidebar, or a segmented control.** Both items are similar to macOS navigation conventions. To choose between a split view or a segmented control, consider the following:
> iPad 앱에서 탭 모음을 사용하는 경우 사이드바가 있는 분할 보기 또는 세그먼트 컨트롤을 사용하는 것이 좋습니다. 두 항목 모두 MacOS 탐색 규칙과 비슷합니다. 분할 보기 또는 세그먼트 컨트롤 중에서 선택하려면 다음을 고려하십시오:
>




- A split view with a sidebar displays a list of top-level items, each of which can disclose a list of child items. Using a sidebar streamlines navigation, because users can view each tab’s contents within the sidebar. By using a sidebar on both iPad and Mac, you create a coherent layout that makes it easy for iPad users to start using the Mac app. To help users organize content, a sidebar can offer features such as labels, sorting, and filtering. Additionally, a sidebar can make use of glyphs to differentiate top-level items.
- >  사이드바가 있는 분할 보기에는 각 항목이 하위 항목 목록을 표시할 수 있는 최상위 항목 목록이 표시됩니다. 사이드바를 사용하면 사용자가 사이드바 내에서 각 탭의 내용을 볼 수 있으므로 탐색이 간소화됩니다. iPad와 Mac 모두에서 사이드바를 사용하면 iPad 사용자가 Mac 앱을 쉽게 사용할 수 있는 일관된 레이아웃을 만들 수 있습니다. 사용자가 내용을 구성할 수 있도록 사이드바는 레이블, 정렬 및 필터링과 같은 기능을 제공할 수 있습니다. 또한 사이드바는 글리프를 사용하여 최상위 항목을 구별할 수 있다.

- A segmented control and a tab bar both accommodate similar interactions — such as mutually exclusive selection. In general, using a split view instead of a tab bar works better than a segmented control. However, a segmented control can work well on the Mac if your app uses a flat navigation hierarchy.
- >  세그먼트화된 컨트롤과 탭 바는 모두 상호 배타적 선택과 같은 유사한 상호 작용을 수용합니다. 일반적으로 탭 표시줄 대신 분할 보기를 사용하면 분할된 컨트롤보다 더 잘 작동합니다. 그러나 앱이 평평한 탐색 계층을 사용하는 경우 분할된 컨트롤이 Mac에서 잘 작동할 수 있습니다.


Regardless of how you adapt the tab bar, be sure to give people quick access to top-level items — such as an item in the sidebar — through the macOS View menu. For guidance, see [App menus](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/user-interaction#app-menus).
> 탭 표시줄을 조정하는 방법에 관계없이 사용자가 macOS 보기 메뉴를 통해 사이드바의 항목과 같은 최상위 항목에 빠르게 액세스할 수 있도록 해야 합니다. 자세한 내용은 앱 메뉴를 참조하십시오.
>





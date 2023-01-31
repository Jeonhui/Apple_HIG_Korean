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




**If your app uses a nested top-level navigation structure, think about ways to create a flatter navigation hierarchy.** Many iPad apps that originated on iPhone use deeply nested navigation controllers, making it difficult for people to navigate within the app. When possible, avoid a nested top-level navigation hierarchy. Instead, adopt a split view with a sidebar and create a flatter hierarchy by making use of the additional screen space on iPad and Mac.
> 앱이 중첩된 최상위 탐색 구조를 사용하는 경우 더 평평한 탐색 계층을 만드는 방법을 생각해 보십시오. iPhone에서 시작된 많은 iPad 앱은 깊게 중첩된 탐색 컨트롤러를 사용하므로 앱 내에서 사람들이 탐색하기 어렵습니다. 가능한 경우 중첩된 최상위 탐색 계층을 피하십시오. 대신 사이드바가 있는 분할 보기를 채택하고 iPad와 Mac의 추가 화면 공간을 활용하여 더 평평한 계층 구조를 만듭니다.
>




**If you use a split view in your Mac app and can’t avoid a deep content hierarchy, include a back button.** If your content hierarchy is deeper than the number of columns supported by the split view, the middle levels between the primary view and the current content pane may not be visible. On iPad, people can use gestures to navigate to a hidden middle level in the content hierarchy. To ensure that people can retrace their steps on the Mac, include a back button in the toolbar and a corresponding navigation item in the View menu.
> Mac 앱에서 분할 보기를 사용하고 깊은 콘텐츠 계층을 피할 수 없는 경우 뒤로 단추를 포함하십시오. 분할 보기에서 지원하는 열 수보다 콘텐츠 계층이 더 깊으면 기본 보기와 현재 콘텐츠 창 사이의 중간 수준이 표시되지 않을 수 있습니다. iPad에서는 제스처를 사용하여 콘텐츠 계층의 숨겨진 중간 수준으로 이동할 수 있습니다. Mac에서 사용자가 자신의 단계를 다시 추적할 수 있도록 도구 모음에 뒤로 버튼을 포함하고 보기 메뉴에 해당하는 탐색 항목을 포함합니다.
>




**If you use a segmented control in your Mac app, place it at the top of the Mac app’s layout.**Mac users are accustomed to a top-down user flow and the bottom of a Mac app’s window isn’t always visible.
> Mac 앱에서 세그먼트화된 컨트롤을 사용하는 경우 Mac 앱 레이아웃의 맨 위에 배치합니다.Mac 사용자는 하향식 사용자 흐름에 익숙하며 Mac 앱의 창 하단이 항상 보이지는 않습니다.
>




**If you use horizontal paging for navigation, offer Mac users specific controls to navigate between pages.** While flicking or dragging laterally with a finger to navigate is easy, holding down a mouse button and dragging laterally is cumbersome. This is especially the case for people who use a mouse without a horizontal scroll wheel. If you support this type of lateral navigation, help people navigate through pages in your Mac app by putting navigation commands into a menu. In addition, display buttons in the toolbar that allow people to navigate to the next or previous page. For example, Stocks in macOS displays both a Back button in the toolbar and Next Story and Previous Story commands in the View menu.
> 탐색을 위해 수평 페이징을 사용하는 경우 Mac 사용자에게 페이지 사이를 탐색할 수 있는 특정 컨트롤을 제공합니다. 탐색을 위해 손가락으로 가로로 긋거나 끄는 것은 쉽지만 마우스 버튼을 누르고 가로로 끄는 것은 번거롭습니다. 특히 가로 스크롤 휠이 없는 마우스를 사용하는 사람의 경우에 해당한다. 이러한 가로 방향 탐색을 지원하는 경우 메뉴에 탐색 명령을 입력하여 Mac 앱의 페이지를 탐색할 수 있도록 도와줍니다. 또한 사용자가 다음 페이지 또는 이전 페이지로 이동할 수 있는 단추를 도구 모음에 표시합니다. 예를 들어, MacOS의 재고는 도구 모음에 뒤로 버튼을 표시하고 보기 메뉴에 다음 스토리 및 이전 스토리 명령을 표시합니다.
>




**Add support for tabs.** Users expect macOS apps to let them open documents or other content in a new tab instead of in a new window. In addition, they can use System Settings to prefer tabs over windows. In this case, the system dynamically adds the relevant menu items to an app’s menus, such as View > Show Tab Bar and Window > Show Next Tab.
> 탭에 대한 지원을 추가합니다. 사용자들은 MacOS 앱이 문서나 다른 콘텐츠를 새 창이 아닌 새 탭에서 열 수 있기를 기대합니다. 또한 시스템 설정을 사용하여 창보다 탭을 선호할 수 있습니다. 이 경우 시스템은 View > Show Tab Bar 및 Window > Show Next Tab과 같은 앱의 메뉴에 관련 메뉴 항목을 동적으로 추가합니다.
>




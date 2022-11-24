# **[components-presentation] scroll-views**

## A scroll view lets people view content that’s larger than the view’s boundaries by moving the content horizontally or vertically.
> 스크롤 보기를 사용하면 내용을 수평 또는 수직으로 이동하여 보기의 경계보다 큰 내용을 볼 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/scroll-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/scroll-view-intro-dark_2x.png)

The scroll view itself has no appearance, but it can display a translucent scroll *bar* or *indicator* that provides additional information about the action. For example, the position of an indicator shows whether the visible portion of the content is near the beginning, middle, or end. Its height hints at the total quantity of scrollable content in the view; the shorter the indicator, the more content there is to scroll.
> 스크롤 보기 자체에는 모양이 없지만 작업에 대한 추가 정보를 제공하는 반투명 스크롤 막대 또는 표시기를 표시할 수 있습니다. 예를 들어, 표시기의 위치는 내용의 가시적인 부분이 시작, 중간 또는 끝에 있는지 여부를 보여줍니다. 높이는 보기에서 스크롤 가능한 콘텐츠의 총 양을 나타냅니다. 표시기가 짧을수록 스크롤할 콘텐츠가 더 많습니다.
>




# **Best practices**

**Support default scrolling gestures and keyboard shortcuts.** People are accustomed to the systemwide scrolling behavior and expect it to work everywhere. If you build custom scrolling for a view, make sure your scroll bars use the elastic behavior that people expect.
> 기본 스크롤 제스처와 바로 가기 키를 지원합니다. 사람들은 시스템 전체의 스크롤 동작에 익숙하며 어디에서나 작동할 것으로 기대합니다. 보기에 대한 사용자 정의 스크롤을 작성하는 경우 스크롤 막대가 사용자가 예상하는 탄력적인 동작을 사용하는지 확인하십시오.
>




**Make it apparent when content is scrollable.** Because scroll bars aren’t always visible, it can be helpful to make it obvious when content extends beyond the view. For example, displaying partial content at the edge of a view indicates that there’s more content in that direction. Although most people immediately try scrolling a view to discover if additional content is available, it’s considerate to draw their attention to it.
> 스크롤 막대가 항상 표시되는 것은 아니므로 내용이 보기 밖으로 확장될 때 표시하는 것이 유용합니다. 예를 들어, 보기 가장자리에 부분 내용을 표시하면 해당 방향에 더 많은 내용이 있음을 나타냅니다. 대부분의 사용자는 즉시 보기를 스크롤하여 추가 콘텐츠를 사용할 수 있는지 확인하려고 하지만, 보기에 주의를 끄는 것이 좋습니다.
>




**Avoid putting a scroll view inside another scroll view with the same orientation.** Doing so creates an unpredictable interface that’s difficult to control. It’s alright to place a horizontal scroll view inside a vertical scroll view (or vice versa), however.
> 스크롤 뷰를 같은 방향의 다른 스크롤 뷰 안에 넣지 마십시오. 이렇게 하면 제어하기 어려운 예측 불가능한 인터페이스가 생성됩니다. 그러나 수평 스크롤 뷰를 수직 스크롤 뷰 안에 배치하는 것은 괜찮습니다.
>




**Consider enabling page-by-page scrolling if it makes sense for your content.** In some situations, people appreciate scrolling by a fixed amount of content per interaction instead of scrolling continuously. On most platforms, you can define the size of such a *page* — typically the current height or width of the view — and enable an interaction that scrolls one page at a time. To help maintain context during page-by-page scrolling, you can define a unit of overlap, such as a line of text, a row of glyphs, or part of a picture, and subtract the unit from the page size.
> 사용자의 콘텐츠에 적합한 경우 페이지별 스크롤을 사용하는 것을 고려해 보십시오. 어떤 상황에서는 사용자가 계속 스크롤하는 대신 상호 작용당 일정량의 콘텐츠를 스크롤하는 것을 선호합니다. 대부분의 플랫폼에서 이러한 페이지 크기(일반적으로 현재 보기 높이 또는 너비)를 정의하고 한 번에 한 페이지씩 스크롤하는 상호 작용을 사용할 수 있습니다. 페이지별로 스크롤하는 동안 컨텍스트를 유지하기 위해 텍스트 줄, 글리프 행 또는 사진의 일부와 같은 중첩 단위를 정의하고 페이지 크기에서 단위를 뺄 수 있습니다.
>




For developer guidance, see [isPagingEnabled](https://developer.apple.com/documentation/uikit/uiscrollview/1619432-ispagingenabled).

**In some cases, scroll automatically to help people find their place.**Although people initiate almost all scrolling, automatic scrolling can be helpful when relevant content is no longer in view, such as when:
> 경우에 따라 자동으로 스크롤하여 사용자가 원하는 위치를 찾을 수 있습니다.사람들이 거의 모든 스크롤을 시작하지만 자동 스크롤은 다음과 같은 경우와 같은 관련 콘텐츠를 더 이상 볼 수 없을 때 유용할 수 있습니다.
>




- Your app performs an operation that selects content or places the insertion point in an area that’s currently hidden. For example, when your app locates text that people are searching for, scroll the content to bring the new selection into view.
- >  앱은 콘텐츠를 선택하거나 삽입 지점을 현재 숨겨져 있는 영역에 배치하는 작업을 수행합니다. 예를 들어, 앱에서 사람들이 검색하는 텍스트를 찾으면 내용을 스크롤하여 새 선택 항목을 표시합니다.

- People start entering information in a location that’s not currently visible. For example, if the insertion point is on one page and people navigate to another page, scroll back to the insertion point as soon as they begin to enter data.
- >  사람들은 현재 보이지 않는 위치에 정보를 입력하기 시작합니다. 예를 들어, 삽입 지점이 한 페이지에 있고 사용자가 다른 페이지로 이동하는 경우 데이터 입력을 시작하는 즉시 삽입 지점으로 다시 스크롤합니다.

- The pointer moves past the edge of the view while people are making a selection. In this case, follow the pointer by scrolling in the direction it moves.
- >  사용자가 선택하는 동안 포인터가 보기 가장자리를 지나 이동합니다. 이 경우 포인터가 이동하는 방향으로 스크롤하여 포인터를 따릅니다.

- People select something and scroll to a new location before acting on the selection. In this case, scroll until the selection is in view before performing the operation.
- >  사용자는 선택 항목을 선택하고 새 위치로 스크롤한 후 선택 항목을 수행합니다. 이 경우 작업을 수행하기 전에 선택 영역이 표시될 때까지 스크롤합니다.


In all cases, automatically scroll the content only as much as necessary to help people retain context. For example, if part of a selection is visible, you don’t need to scroll the entire selection into view.
> 모든 경우 사용자가 컨텍스트를 유지할 수 있도록 필요한 만큼만 내용을 자동으로 스크롤합니다. 예를 들어 선택 영역의 일부가 표시되는 경우 전체 선택 영역을 보기로 스크롤할 필요가 없습니다.
>




**If you enable zoom, set appropriate maximum and minimum scale values.** For example, zooming in on text until a single character fills the screen doesn’t make sense in most situations.
> 예를 들어 화면에 문자 하나가 채워질 때까지 텍스트를 확대하는 것은 대부분의 경우 의미가 없습니다.
>




# **Platform considerations**

# **iOS, iPadOS**

**In general, display one scroll view per screen.** People often make large swipe gestures when scrolling, and it can be hard to avoid interacting with a neighboring scroll view on the same screen. If you need to put two scroll views on one screen, consider allowing them to scroll in different directions so one gesture is less likely to affect both views. For example, when iPhone is in portrait orientation, the Stocks app shows stock quotes that scroll vertically above company-specific information that scrolls horizontally.
> 일반적으로 화면당 하나의 스크롤 뷰를 표시하며, 사람들은 스크롤할 때 큰 스와이프 동작을 하는 경우가 많으며, 같은 화면에서 인접한 스크롤 뷰와 상호 작용하는 것을 피하기 어려울 수 있다. 한 화면에 두 개의 스크롤 보기를 배치해야 하는 경우 한 가지 제스처가 두 보기 모두에 영향을 미치지 않도록 다른 방향으로 스크롤할 수 있도록 허용하는 것이 좋습니다. 예를 들어 iPhone이 세로 방향일 때 Stocks 앱은 가로로 스크롤하는 회사별 정보 위에 수직으로 스크롤하는 주가를 표시합니다.
>




**Consider showing a page control when a scroll view is in page-by-page mode.** [Page controls](../components/presentation/page-controls) show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. For example, Weather uses a page control to indicate movement between people’s saved locations. If you show a page control with a scroll view, disable the scrolling indicator on the same axis to avoid confusing people with redundant controls.
> 스크롤 보기가 페이지별 모드일 때 페이지 컨트롤을 표시하는 것이 좋습니다. 페이지 컨트롤은 사용 가능한 페이지, 화면 또는 기타 콘텐츠 청크 수를 표시하고 현재 볼 수 있는 콘텐츠 청크를 표시합니다. 예를 들어, 날씨는 페이지 컨트롤을 사용하여 사용자의 저장된 위치 간 이동을 나타냅니다. 스크롤 뷰가 있는 페이지 컨트롤을 표시하는 경우, 중복 컨트롤이 있는 사용자를 혼동하지 않도록 동일한 축에서 스크롤 표시기를 사용 불가능으로 설정하십시오.
>




# **macOS**

**Account for scroll bars in your layout.** By default, scroll bars appear only when people interact with views that contain them, but people can use a setting in General settings to make them to appear all the time. Some input devices also cause scroll bars to display all the time. If necessary, adjust the layout of your window so important interface elements don't appear beneath scroll bars. The scroll bar track has a thickness of 15 points (regular size) or 11 points (small or mini size).
> 레이아웃에서 스크롤 막대를 설명합니다. 기본적으로 스크롤 막대는 사용자가 이 막대를 포함하는 보기와 상호 작용할 때만 나타나지만 일반 설정의 설정을 사용하여 항상 나타나도록 만들 수 있습니다. 일부 입력 장치는 스크롤 막대가 항상 표시되도록 합니다. 필요한 경우 중요한 인터페이스 요소가 스크롤 막대 아래에 나타나지 않도록 창 레이아웃을 조정합니다. 스크롤 막대 트랙의 두께는 15포인트(정규 크기) 또는 11포인트(소형 또는 미니 크기)입니다.
>




**Avoid moving window content when transient scroll bars appear.**Constantly shifting content every time scroll bars appear can be disorienting.
> 일시적인 스크롤 막대가 나타날 때 창 내용을 이동하지 않도록 합니다.스크롤 막대가 나타날 때마다 콘텐츠를 계속 이동하는 것은 방향을 잃을 수 있습니다.
>




**Avoid placing controls inline with a scroll bar.** Doing this can cause the bar to appear even when people set it to be transient.
> 스크롤 막대에 컨트롤을 정렬하지 마십시오. 이렇게 하면 사용자가 일시적으로 설정한 경우에도 막대가 나타날 수 있습니다.
>




**If necessary, use small or mini scroll bars in a panel.** When space is tight, you can use smaller scroll bars in panels that need to coexist with other windows. Be sure to use the same size for all controls in such a panel.
> 필요한 경우 패널에서 작은 스크롤 막대 또는 미니 스크롤 막대를 사용하고, 공간이 부족할 때 다른 창과 공존해야 하는 패널에서 더 작은 스크롤 막대를 사용할 수 있습니다. 이러한 패널의 모든 컨트롤에 동일한 크기를 사용해야 합니다.
>




# **tvOS**

Views in tvOS can scroll, but they aren’t treated as distinct objects with scroll bars. Instead, when content exceeds the size of the screen, the system automatically scrolls the interface to keep focused items visible.
> vOS의 보기는 스크롤할 수 있지만 스크롤 막대가 있는 별개의 개체로 취급되지는 않습니다. 대신 콘텐츠가 화면 크기를 초과할 경우 시스템은 자동으로 인터페이스를 스크롤하여 초점이 맞는 항목을 계속 볼 수 있도록 합니다.
>




# **watchOS**

The transient scroll bar and knob appear during active scrolling, and people can use the Digital Crown to scroll. If your interface includes multiple pages, you can set whether they scroll horizontally or vertically with [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation).
> 일시적 스크롤 막대와 노브는 활성 스크롤 중에 나타나며, 사람들은 디지털 크라운을 사용하여 스크롤할 수 있습니다. 인터페이스에 여러 페이지가 포함된 경우 WKPageOrientation을 사용하여 페이지를 가로로 스크롤할지 세로로 스크롤할지 설정할 수 있습니다.
>




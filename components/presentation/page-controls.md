# **[components-presentation] page-controls**

## A page control displays a row of indicator images, each of which represents a page in a flat list.
> 페이지 컨트롤은 표시기 이미지의 행을 표시하며, 각 행은 플랫 목록의 페이지를 나타냅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/page-dots-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/page-dots-intro-dark_2x.png)

The scrolling row of indicators helps people navigate the list to find the page they want. Page controls can handle an arbitrary number of pages, making them particularly useful in situations where people can create custom lists.
> 표시기의 스크롤 행은 사용자가 원하는 페이지를 찾기 위해 목록을 탐색하는 데 도움이 됩니다. 페이지 컨트롤은 임의의 수의 페이지를 처리할 수 있으므로 사용자가 사용자 정의 목록을 작성할 수 있는 상황에서 특히 유용합니다.
>




Page controls appear as a series of small indicator dots by default, representing the available pages. A solid dot denotes the current page. Visually, these dots are always equidistant, and are clipped if too many appear onscreen.
> 페이지 컨트롤은 기본적으로 사용 가능한 페이지를 나타내는 일련의 작은 표시기 점으로 나타납니다. 실점은 현재 페이지를 나타냅니다. 시각적으로 이 점들은 항상 동일한 거리에 있으며 화면에 너무 많이 표시되면 잘립니다.
>




# **Best practices**

**Use page controls to represent movement between an ordered list of pages.** Page controls don’t represent hierarchical or nonsequential page relationships. For more complex navigation, consider using a sidebar or split view instead.
> 페이지 컨트롤을 사용하여 정렬된 페이지 목록 간의 이동을 나타냅니다. 페이지 컨트롤은 계층적 또는 비순차적 페이지 관계를 나타내지 않습니다. 더 복잡한 탐색의 경우 사이드바 또는 분할 보기를 대신 사용하는 것이 좋습니다.
>




**Center a page control at the bottom of the screen.** To ensure people always know where to find a page control, center it horizontally and position it near the bottom of the screen.
> 페이지 컨트롤을 화면 하단에 중앙에 배치합니다. 페이지 컨트롤을 찾을 위치를 항상 사용자가 알 수 있도록 페이지 컨트롤을 수평으로 중앙에 배치하고 화면 하단 근처에 배치합니다.
>




**Although page controls can handle any number of pages, don’t display too many**. More than about 10 dots are hard to count at a glance. If your app needs to display more than 10 pages as peers, consider using a different arrangement‚ such as a grid, that enables nonsequential navigation.
> 페이지 컨트롤이 원하는 수의 페이지를 처리할 수 있지만 너무 많은 페이지를 표시하지 마십시오. 10개가 넘는 점들은 한 눈에 세기 어렵다. 앱이 피어로 10페이지 이상을 표시해야 하는 경우, 순차적이지 않은 탐색을 가능하게 하는 그리드와 같은 다른 배열을 사용하는 것이 좋습니다.
>




# **Customizing indicators**

By default, a page control uses the system-provided dot image for all indicators, but it can also display a unique image to help people identify a specific page. For example, Weather uses the `location.fill` symbol to distinguish the current location's page.
> 기본적으로 페이지 컨트롤은 모든 표시기에 대해 시스템에서 제공한 점 이미지를 사용하지만 사용자가 특정 페이지를 식별하는 데 도움이 되는 고유한 이미지를 표시할 수도 있습니다. 예를 들어, Weather는 '위치'를 사용합니다.현재 위치의 페이지를 구분하는 기호를 채웁니다.
>




If it enhances your app or game, you can provide a custom image to use as the default image for all indicators and you can also supply a different image for a specific page. For developer guidance, see [preferredIndicatorImage](https://developer.apple.com/documentation/uikit/uipagecontrol/3577679-preferredindicatorimage) and [setIndicatorImage(_:forPage:)](https://developer.apple.com/documentation/uikit/uipagecontrol/3577680-setindicatorimage).
> 앱이나 게임이 향상된 경우 모든 표시기의 기본 이미지로 사용할 사용자 지정 이미지를 제공할 수 있으며 특정 페이지에 대해 다른 이미지를 제공할 수도 있습니다. 개발자 지침은 기본 설정을 참조하십시오.표시기 이미지 및 설정표시기 이미지(_: 페이지:의 경우).
>




**Make sure custom indicator images are simple and clear.** Avoid complex shapes, and don't include negative space, text, or inner lines, because these details can make an icon muddy and indecipherable at very small sizes. Consider using simple [SF Symbols](../foundations/sf-symbols) as indicators or design your own icons. For guidance, see [Icons](../foundations/icons).
> 사용자 지정 표시기 이미지가 단순하고 명확한지 확인하십시오. 복잡한 모양을 피하고 음의 공백, 텍스트 또는 내선을 포함하지 마십시오. 이러한 세부 정보는 아이콘을 매우 작은 크기에서 흐리게 하고 해독할 수 없게 만들 수 있습니다. 간단한 SF 기호를 표시기로 사용하거나 자신만의 아이콘을 디자인하는 것을 고려해 보십시오. 자세한 내용은 아이콘을 참조하십시오.
>




**Customize the default indicator image only when it enhances the page control's overall meaning.** For example, if every page you list contains bookmarks, you might use the `bookmark.fill` symbol as the default indicator image.
> 페이지 컨트롤의 전체적인 의미를 향상시키는 경우에만 기본 표시기 이미지를 사용자 정의합니다. 예를 들어, 나열하는 모든 페이지에 책갈피가 포함되어 있으면 'bookmark.fill' 기호를 기본 표시기 이미지로 사용할 수 있습니다.
>




**Avoid using more than two different indicator images in a page control.**If your list contains one page with special meaning — like the current-location page in Weather — you can make the page easy to find by giving it a unique indicator image. In contrast, a page control that uses several unique images to mark several important pages is hard to use because people must memorize the meaning of each image. A page control that displays more than two types of indicator images tends to look messy and haphazard, even when each image is clear.
> 한 페이지 컨트롤에서 세 개 이상의 다른 표시기 이미지를 사용하지 않도록 합니다.목록에 날씨의 현재 위치 페이지와 같이 특별한 의미가 있는 페이지가 하나 있으면 고유한 표시기 이미지를 제공하여 페이지를 쉽게 찾을 수 있습니다. 대조적으로, 여러 개의 고유한 이미지를 사용하여 몇 개의 중요한 페이지를 표시하는 페이지 컨트롤은 사람들이 각 이미지의 의미를 기억해야 하기 때문에 사용하기 어렵다. 두 가지 이상의 표시기 이미지를 표시하는 페이지 컨트롤은 각 이미지가 선명한 경우에도 지저분하고 임의적으로 보이는 경향이 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/customizing-indicator-right_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/customizing-indicator-right_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

Using only two different indicators looks well-organized and provides a consistent experience.
> 두 가지 지표만 사용하는 것은 잘 조직된 것처럼 보이며 일관된 경험을 제공한다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/customizing-indicator-wrong_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/customizing-indicator-wrong_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

Using several different indicators can make a page control look busy and difficult to use.
> 여러 가지 표시기를 사용하면 페이지 컨트롤이 사용 중이거나 사용하기 어려워 보일 수 있습니다.
>




**Avoid coloring indicator images.** Custom colors can reduce the contrast that differentiates the current-page indicator and makes the page control visible on the screen. To ensure that your page control is easy to use and looks good in different contexts, let the system automatically color the indicators.
> 표시기 이미지를 색칠하지 않도록 합니다. 사용자 지정 색은 현재 페이지 표시기를 구별하고 화면에 페이지 컨트롤을 표시하는 대비를 줄일 수 있습니다. 페이지 컨트롤을 사용하기 쉽고 다양한 컨텍스트에서 보기 좋게 표시하려면 시스템에서 자동으로 표시기에 색을 지정합니다.
>




# **Platform considerations**

*No additional considerations for watchOS. Not supported in macOS.*
> 워치OS에 대한 추가 고려사항은 없습니다. macOS에서는 지원되지 않습니다.
>




# **iOS, iPadOS**

A page control can adjust the appearance of indicators to provide more information about the list. For example, the control highlights the indicator of the current page so people can estimate the page's relative position in the list. When there are more indicators than fit in the space, the control can shrink indicators at both sides to suggest that more pages are available.
> 페이지 컨트롤은 표시기의 모양을 조정하여 목록에 대한 자세한 정보를 제공할 수 있습니다. 예를 들어, 컨트롤은 사용자가 목록에서 페이지의 상대적 위치를 추정할 수 있도록 현재 페이지의 표시기를 강조 표시합니다. 공간에 적합한 것보다 많은 지시자가 있는 경우 컨트롤은 양쪽의 지시자를 축소하여 더 많은 페이지를 사용할 수 있음을 나타낼 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/page-controls-many_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/page-controls-many_2x.png)

People interact with page controls by tapping or scrubbing (to *scrub*, people touch the control and drag left or right). Tapping on the leading or trailing side of the current-page indicator reveals the next or previous page; in iPadOS, people can also use the pointer to target a specific indicator. Scrubbing opens pages in sequence, and scrubbing past the leading or trailing edge of the control helps people quickly reach the first or last page.
> 사용자는 탭을 누르거나 문지르며 페이지 컨트롤과 상호 작용합니다(스크럽하려면 컨트롤을 누르고 왼쪽 또는 오른쪽으로 끕니다). 현재 페이지 표시기의 앞이나 뒤의 면을 탭하면 다음 페이지 또는 이전 페이지가 나타납니다. 스크러빙은 페이지를 순차적으로 열고, 컨트롤의 맨 앞 또는 맨 뒤의 가장자리를 스크러빙하면 사용자가 첫 번째 또는 마지막 페이지에 빠르게 도달할 수 있습니다.
>




**DEVELOPER NOTE**In the API, *tapping* is a *discrete interaction*, whereas *scrubbing* is a *continuous interaction*; for developer guidance, see [UIPageControl.InteractionState](https://developer.apple.com/documentation/uikit/uipagecontrol/interactionstate).
> 개발자 참고 API에서 탭핑은 별개의 상호 작용인 반면 스크러빙은 지속적인 상호 작용입니다. 개발자 지침은 UIPageControl을 참조하십시오.상호 작용 상태.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/page-controls-scrub_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls/images/page-controls-scrub_2x.png)

Play

**Avoid animating page transitions during scrubbing.** People can scrub very quickly, and using the scrolling animation for every transition can make your app lag and cause distracting visual flashes. Use the animated scrolling transition only for tapping.
> 스크러빙하는 동안 페이지 전환을 애니메이션화하지 마십시오. 사용자는 매우 빠르게 스크러빙할 수 있으며, 모든 전환에 스크롤 애니메이션을 사용하면 애플리케이션이 지연되고 주의를 산만하게 하는 시각적 섬광이 발생할 수 있습니다. 애니메이션 스크롤 전환은 탭핑에만 사용하십시오.
>




A page control can include a translucent, rounded-rectangle background appearance that provides visual contrast for the indicators. You can choose one of the following background styles:
> 페이지 컨트롤은 지시자에 대한 시각적 대비를 제공하는 반투명하고 둥근 직사각형 배경 모양을 포함할 수 있습니다. 다음 배경 스타일 중 하나를 선택할 수 있습니다.
>




- Automatic — Displays the background only when people interact with the control. Use this style when the page control isn't the primary navigational element in the UI.
- >  자동 - 사용자가 컨트롤과 상호 작용할 때만 배경을 표시합니다. 페이지 컨트롤이 UI의 기본 탐색 요소가 아닌 경우 이 유형을 사용합니다.

- Prominent — Always displays the background. Use this style only when the control is the primary navigational control in the screen.
- >  두드러짐 - 항상 배경을 표시합니다. 컨트롤이 화면에서 기본 탐색 컨트롤인 경우에만 이 스타일을 사용하십시오.

- Minimal — Never displays the background. Use this style when you just want to show the position of the current page in the list and you don't need to provide visual feedback during scrubbing.
- >  최소 - 배경을 표시하지 않습니다. 목록에서 현재 페이지의 위치를 표시하고 스크러빙 중 시각적 피드백을 제공할 필요가 없는 경우 이 유형을 사용하십시오.


For developer guidance, see [backgroundStyle](https://developer.apple.com/documentation/uikit/uipagecontrol/3577676-backgroundstyle).

**Avoid supporting the scrubber when you use the minimal background style.** The minimal style doesn't provide visual feedback during scrubbing. If you want to let people scrub a list of pages in your app, use the automatic or prominent background styles.
> 최소 배경 스타일을 사용할 때는 스크러버를 지원하지 않도록 합니다. 최소 스타일은 스크러버 작업 중 시각적 피드백을 제공하지 않습니다. 사용자가 앱에서 페이지 목록을 스크럽하도록 하려면 자동 또는 눈에 띄는 배경 스타일을 사용하십시오.
>




# **tvOS**

**Use page controls on collections of full-screen pages.** A page control is designed to operate in a full-screen environment where multiple content-rich pages are peers in the page hierarchy. Inclusion of additional controls makes it difficult to maintain focus while moving between pages.
> 전체 화면 페이지 모음에서 페이지 컨트롤을 사용합니다. 페이지 컨트롤은 내용이 많은 여러 페이지가 페이지 계층의 피어인 전체 화면 환경에서 작동하도록 설계되었습니다. 추가 컨트롤을 포함하면 페이지 간을 이동하는 동안 포커스를 유지하기가 어렵습니다.
>




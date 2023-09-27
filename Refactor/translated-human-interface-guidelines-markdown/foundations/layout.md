### [[Foundations](./translated-human-interface-guidelines-markdown/foundations.md)]  
  
# **Layout**  



#### [Rating template](/design/human-interface-guidelines/layout#Rating-template)



The rating template lets people adjust the rating of a particular item, such as a movie or a song.

> 등급 템플릿을 사용하면 영화나 노래와 같은 특정 항목의 등급을 조정할 수 있습니다.
>



![An illustration of Apple TV, displaying the search template.](https://docs-assets.developer.apple.com/published/b600976ca0eec92f1c7666f92b54847d/template-search@2x.png)



#### [Search template](/design/human-interface-guidelines/layout#Search-template)



The search template lets people search your content and view results. It includes a search field, a keyboard, and a list of results.

> 검색 템플릿을 사용하여 사용자가 내용을 검색하고 결과를 볼 수 있습니다. 여기에는 검색 필드, 키보드 및 결과 목록이 포함됩니다.
>



![An illustration of Apple TV, displaying the stack template.](https://docs-assets.developer.apple.com/published/ed260fb6063fb3845960bc4bec42bddb/template-stack@2x.png)



#### [Stack template](/design/human-interface-guidelines/layout#Stack-template)



The stack template displays groups of products — such as different genres of movies — in rows. Each group of products displays directly beneath the previous group.

> 스택 템플릿은 여러 장르의 동영상과 같은 제품 그룹을 행으로 표시합니다. 각 제품 그룹은 이전 그룹 바로 아래에 표시됩니다.
>



**Customize templates tastefully.** Layout templates are highly customizable; you have control over the background, tinting, size, layout, and more. As you design your app, defer to content whenever possible, avoiding customizations that appear distracting, jarring, or obtrusive.

> **템플릿을 사용자 정의합니다.** 레이아웃 템플릿은 사용자 정의가 매우 용이합니다. 배경, 선팅, 크기, 레이아웃 등을 제어할 수 있습니다. 앱을 설계할 때, 방해가 되거나 방해가 되거나 방해가 되는 사용자 지정을 피하면서 가능한 한 콘텐츠에 의존하십시오.
>



**Understand a template’s purpose before using it.** If your customizations make the underlying template unrecognizable, consider using a different template or building a custom interface.

> **템플릿을 사용하기 전에 템플릿의 용도를 이해하십시오.** 사용자 지정으로 인해 기본 템플릿을 인식할 수 없는 경우 다른 템플릿을 사용하거나 사용자 지정 인터페이스를 구축하는 것을 고려하십시오.
>



For detailed information about integrating templates into your app, see [TVML](https://developer.apple.com/design/human-interface-guidelines/documentation/TVML)

> 템플릿을 앱에 통합하는 방법에 대한 자세한 내용은 [TVML](https://developer.apple.com/design/human-interface-guidelines/documentation/TVML) 을 참조하십시오
>

.



#### [Grids](/design/human-interface-guidelines/layout#Grids)



The following grid layouts provide an optimal viewing experience. Be sure to use appropriate spacing between unfocused rows and columns to prevent overlap when an item is brought into focus.

> 다음 그리드 레이아웃은 최적의 보기 환경을 제공합니다. 항목이 포커스를 맞출 때 겹치지 않도록 하려면 포커스가 없는 행과 열 사이에 적절한 간격을 사용해야 합니다.
>



If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content. For developer guidance, see [`UICollectionViewFlowLayout`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uicollectionviewflowlayout)

> UIKit 집합 보기 흐름 요소를 사용하는 경우 그리드의 열 수는 내용의 너비와 간격에 따라 자동으로 결정됩니다. 개발자 지침은 ['UICollectionViewFlowLayout'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uicollectionviewflowlayout) 을 참조하십시오
>

.



* [Two-column](#)

* [Three-column](#)

* [Four-column](#)

* [Five-column](#)

* [Six-column](#)

* [Seven-column](#)

* [Eight-column](#)

* [Nine-column](#)

![An illustration of Apple TV, displaying a two-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/d577c3ac4e484d949c170cfa505073c4/visual-design-grid-2-column@2x.png)



#### [Two-column grid](/design/human-interface-guidelines/layout#Two-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 860 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



![An illustration of Apple TV, displaying a three-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/d6d33c16e558689e5df794a40240030e/visual-design-grid-3-column@2x.png)



#### [Three-column grid](/design/human-interface-guidelines/layout#Three-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 560 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



![An illustration of Apple TV, displaying a four-column grid of media items. Additional media items are partially visible on the right side of the screen.](https://docs-assets.developer.apple.com/published/53465d4cbf4d54bf7f54a1fe0aad69c2/visual-design-grid-4-column@2x.png)



#### [Four-column grid](/design/human-interface-guidelines/layout#Four-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 410 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



![An illustration of Apple TV, displaying a five-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/7729a9baf067e70d987871466c875829/visual-design-grid-5-column@2x.png)



#### [Five-column grid](/design/human-interface-guidelines/layout#Five-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 320 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



![An illustration of Apple TV, displaying a six-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/363166bc22bb12746940ac6a0ee47d9f/visual-design-grid-6-column@2x.png)



#### [Six-column grid](/design/human-interface-guidelines/layout#Six-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 260 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



![An illustration of Apple TV, displaying a seven-column grid of media items. Additional media items are partially visible on the right side of the screen.](https://docs-assets.developer.apple.com/published/d2129f4b27dc80a9d7528f9cb382a477/visual-design-grid-7-column@2x.png)



#### [Seven-column grid](/design/human-interface-guidelines/layout#Seven-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 217 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



![An illustration of Apple TV, displaying an eight-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/ba74e699570d39b4c7d4142f9abfb8b2/visual-design-grid-8-column@2x.png)



#### [Eight-column grid](/design/human-interface-guidelines/layout#Eight-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 184 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



![An illustration of Apple TV, displaying a nine-column grid of media items.](https://docs-assets.developer.apple.com/published/32367e6123252d802948995cccab7fb0/visual-design-grid-9-column@2x.png)



#### [Nine-column grid](/design/human-interface-guidelines/layout#Nine-column-grid)







| Attribute | Value |

| --- | --- |

| Unfocused content width | 160 pt |

| Horizontal spacing | 40 pt |

| Minimum vertical spacing | 100 pt |



**Include additional vertical spacing for titled rows.** If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.

> **제목이 지정된 행에는 추가 수직 간격을 포함합니다.** 행에 제목이 있는 경우, 이전에 포커스가 없는 행의 맨 아래와 제목의 중심 사이에 충분한 간격을 제공하여 혼잡을 방지하십시오. 또한 제목 하단과 행의 초점이 맞지 않는 항목 상단 사이에 간격을 지정합니다.
>



**Use consistent spacing.** When content isn’t consistently spaced, it no longer looks like a grid and it’s harder for people to scan.

> **일정한 간격을 사용합니다.** 콘텐츠가 지속적으로 간격을 유지하지 않으면 더 이상 그리드처럼 보이지 않고 사람들이 스캔하기가 더 어렵습니다.
>



**Make partially hidden content look symmetrical.** To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.

> **부분적으로 숨겨진 내용을 대칭으로 보이게 합니다.** 완전히 보이는 콘텐츠에 주의를 기울이려면 부분적으로 숨긴 오프스크린 콘텐츠를 화면 양쪽에서 동일한 너비로 유지하십시오.
>



### [visionOS](/design/human-interface-guidelines/layout#visionOS)



The guidance below can help you lay out content within the windows of your visionOS app or game, making it feel familiar and easy to use. For guidance on displaying windows in space and best practices for using depth, scale, and field of view in your visionOS app, see [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/spatial-layout)

> 아래 지침은 비전의 창 안에 콘텐츠를 배치하는 데 도움이 될 수 있습니다친숙하고 사용하기 쉬운 느낌을 주는 OS 앱 또는 게임. 창을 공간에 표시하는 방법과 비전에서 깊이, 척도 및 시야를 사용하는 모범 사례에 대한 지침OS 앱, [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/spatial-layout) 참조)
>

. To learn more about visionOS window components, see [Windows > visionOS](/design/human-interface-guidelines/windows#visionOS)

> . 비전에 대해 자세히 알아보기OS 창 구성 요소, [Windows > vision OS](/design/human-interface-guideline/windows#vision 참조)OS)
>

.



Note



When you add depth to content in a standard window, the content extends beyond the window’s bounds along the z-axis. If content extends too far along the z-axis, the system clips it.

> 표준 창의 내용에 깊이를 추가하면 내용이 z 축을 따라 창의 경계를 넘어 확장됩니다. 컨텐츠가 z 축을 따라 너무 많이 확장되면 시스템이 해당 컨텐츠를 클리핑합니다.
>



**Keep a window’s content within its bounds.** In visionOS, the system displays window controls just outside a window’s bounds in the XY plane. For example, the Share menu appears above the window and the controls for resizing, moving, and closing the window appear below it. Letting 2D or 3D content encroach on these areas can make the system-provided controls, especially those below the window, difficult for people to use.

> **창의 내용을 제한 범위 내에 유지합니다.** 시야에OS, 시스템은 윈도우 컨트롤을 XY 평면의 윈도우 경계 바로 밖에 표시한다. 예를 들어 공유 메뉴가 창 위에 나타나고 창 크기 조정, 이동 및 닫기에 대한 컨트롤이 창 아래에 나타납니다. 2D 또는 3D 콘텐츠가 이러한 영역을 잠식하게 하면 시스템이 제공하는 제어장치, 특히 창 아래의 제어장치가 사람들이 사용하기 어렵게 만들 수 있다.
>



**In general, avoid placing important content and controls in a window’s corners.** The farther content is from the center of a window, the more difficult it can be for people to see and interact with it, especially when the window is large.

> **일반적으로 창의 모서리에 중요한 내용과 컨트롤을 배치하지 마십시오.** 창 중앙에서 멀리 떨어져 있는 콘텐츠일수록 특히 창이 클 때 사람들이 창을 보고 상호작용하는 것이 더 어려워질 수 있다.
>



**Make a window’s interactive components easy for people to focus.** You need to include enough space around an interactive component so that focusing it is easy and comfortable, and to prevent the system-provided hover effect from obscuring other content. For example, place buttons so their centers are at least 60 points apart. For guidance, see [Eyes](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/eyes)

> **창의 대화형 구성요소를 사람들이 쉽게 집중할 수 있도록 합니다.** 대화형 구성요소 주위에 충분한 공간을 포함해야 초점을 쉽게 맞출 수 있고, 시스템에서 제공하는 호버 효과가 다른 내용을 가리는 것을 방지할 수 있습니다. 예를 들어, 단추의 중심이 60점 이상 떨어져 있도록 단추를 놓습니다. 자세한 내용은 [Eyes](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/eyes) 를 참조하십시오
>

, [Spatial layout](/design/human-interface-guidelines/spatial-layout)

, and [Buttons > visionOS](/design/human-interface-guidelines/buttons#visionOS)

> , 그리고 [버튼 > vision OS](/design/human-interface-가이드라인/버튼#비전OS)
>

.



**If you need to display additional controls that don’t belong within a window, use an ornament.** An ornament lets you offer app controls that remain visually associated with a window without interfering with the system-provided controls. For example, a window’s toolbar and tab bar appear as ornaments. For guidance, see [Ornaments](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/ornaments)

> **창에 속하지 않는 추가 컨트롤을 표시해야 할 경우 장식을 사용하십시오.** 장식을 사용하면 시스템에서 제공하는 컨트롤을 방해하지 않고 창과 시각적으로 연결된 상태로 있는 앱 컨트롤을 제공할 수 있습니다. 예를 들어, 창의 도구 모음 및 탭 표시줄은 장식으로 나타납니다. 자세한 내용은 [장식](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/ornaments) 을 참조하십시오
>

.



### [watchOS](/design/human-interface-guidelines/layout#watchOS)



**Design your content to extend from one edge of the screen to the other.** The Apple Watch bezel provides a natural visual padding around your content. To avoid wasting valuable space, consider minimizing the padding between elements.

> **화면의 한쪽 끝에서 다른 쪽 끝까지 콘텐츠가 확장되도록 설계합니다.** Apple Watch 베젤은 콘텐츠 주변에 자연스러운 시각적 패딩을 제공합니다. 귀중한 공간을 낭비하지 않으려면 요소 간 패딩을 최소화하는 것을 고려하십시오.
>



![An illustration of the Workout app’s main list of workouts on Apple Watch. A callout indicates that the currently focused workout item spans the full width of the available screen area.](https://docs-assets.developer.apple.com/published/180d82ec20b9f85908474cc931d4707e/layout-full-width@2x.png)



**Avoid placing more than two or three controls side by side in your interface.** As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it’s usually better to let text buttons span the full width of the screen, two side-by-side buttons with short text labels can also work well, as long as the screen doesn’t scroll.

> **인터페이스에 두 개 또는 세 개 이상의 컨트롤을 나란히 배치하지 마십시오.** 일반적으로 글리프가 포함된 단추 세 개 또는 텍스트가 포함된 단추 두 개를 한 행에 표시할 수 없습니다. 일반적으로 텍스트 단추가 화면의 전체 너비에 걸쳐 있도록 하는 것이 더 좋지만, 화면이 스크롤되지 않는 한 짧은 텍스트 레이블이 있는 두 개의 나란히 있는 단추도 잘 작동할 수 있습니다.
>



![A diagram of an Apple Watch screen showing two side-by-side buttons beneath three lines of text.](https://docs-assets.developer.apple.com/published/aa5904c73a0b5295604bb551c164325c/layout-controls@2x.png)



**Support autorotation in views people might want to show others.** When people flip their wrist away, apps typically respond to the motion by sleeping the display, but in some cases it makes sense to autorotate the content. For example, a wearer might want to show an image to a friend or display a QR code to a reader. For developer guidance, see [`isAutorotating`](https://developer.apple.com/design/human-interface-guidelines/documentation/watchkit/wkextension/2868464-isautorotating)

> **사람들이 다른 사람들에게 보여주고 싶어할 수 있는 보기에서 자동 회전을 지원합니다.** 사람들이 손목을 뒤집을 때, 앱들은 일반적으로 디스플레이를 잠재우는 것으로 동작에 반응하지만, 일부 경우에는 콘텐츠를 자동으로 회전시키는 것이 합리적이다. 예를 들어, 착용자는 친구에게 이미지를 보여주거나 리더에게 QR 코드를 표시하기를 원할 수 있다. 개발자 지침은 ['isAutorating'](https://developer.apple.com/design/human-interface-guidelines/documentation/watchkit/wkextension/2868464-isautorotating) 을 참조하십시오
>

.



[Specifications](/design/human-interface-guidelines/layout#Specifications)

--------------------------------------------------------------------------



### [iOS, iPadOS](/design/human-interface-guidelines/layout#iOS-iPadOS)



#### [Device screen sizes and orientations](/design/human-interface-guidelines/layout#Device-screen-sizes-and-orientations)

> #### [기기 화면 크기 및 방향] (/디자인/인간-인터페이스-가이드라인/레이아웃#기기 화면 크기 및 방향)
>







| Device | Dimensions (portrait) |

| --- | --- |

| 12.9” iPad Pro | 1024x1366 pt (2048x2732 px @2x) |

| 11” iPad Pro | 834x1194 pt (1668x2388 px @2x) |

| 10.5” iPad Pro | 834x1194 pt (1668x2388 px @2x) |

| 9.7” iPad Pro | 768x1024 pt (1536x2048 px @2x) |

| 7.9” iPad mini | 768x1024 pt (1536x2048 px @2x) |

| 10.5” iPad Air | 834x1112 pt (1668x2224 px @2x) |

| 9.7” iPad Air | 768x1024 pt (1536x2048 px @2x) |

| 10.2” iPad | 810x1080 pt (1620x2160 px @2x) |

| 9.7” iPad | 768x1024 pt (1536x2048 px @2x) |

| iPhone 14 Pro Max | 430x932 pt (1290x2796 px @3x) |

| iPhone 14 Pro | 393x852 pt (1179x2556 px @3x) |

| iPhone 14 Plus | 428x926 pt (1284x2778 px @3x) |

| iPhone 14 | 390x844 pt (1170x2532 px @3x) |

| iPhone 13 Pro Max | 428x926 pt (1284x2778 px @3x) |

| iPhone 13 Pro | 390x844 pt (1170x2532 px @3x) |

| iPhone 13 | 390x844 pt (1170x2532 px @3x) |

| iPhone 13 mini | 375x812 pt (1125x2436 px @3x) |

| iPhone 12 Pro Max | 428x926 pt (1284x2778 px @3x) |

| iPhone 12 Pro | 390x844 pt (1170x2532 px @3x) |

| iPhone 12 | 390x844 pt (1170x2532 px @3x) |

| iPhone 12 mini | 375x812 pt (1125x2436 px @3x) |

| iPhone 11 Pro Max | 414x896 pt (1242x2688 px @3x) |

| iPhone 11 Pro | 375x812 pt (1125x2436 px @3x) |

| iPhone 11 | 414x896 pt (828x1792 px @2x) |

| iPhone XS Max | 414x896 pt (1242x2688 px @3x) |

| iPhone XS | 375x812 pt (1125x2436 px @3x) |

| iPhone XR | 414x896 pt (828x1792 px @2x) |

| iPhone X | 375x812 pt (1125x2436 px @3x) |

| iPhone 8 Plus | 414x736 pt (1080x1920 px @3x) |

| iPhone 8 | 375x667 pt (750x1334 px @2x) |

| iPhone 7 Plus | 414x736 pt (1080x1920 px @3x) |

| iPhone 7 | 375x667 pt (750x1334 px @2x) |

| iPhone 6s Plus | 414x736 pt (1080x1920 px @3x) |

| iPhone 6s | 375x667 pt (750x1334 px @2x) |

| iPhone 6 Plus | 414x736 pt (1080x1920 px @3x) |

| iPhone 6 | 375x667 pt (750x1334 px @2x) |

| 4.7” iPhone SE | 375x667 pt (750x1334 px @2x) |

| 4” iPhone SE | 320x568 pt (640x1136 px @2x) |

| iPod touch 5th generation and later | 320x568 pt (640x1136 px @2x) |



Note



All scale factors in the table above are UIKit scale factors, which may differ from native scale factors. For developer guidance, see [`scale`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiscreen/1617836-scale)

> 위 표의 모든 척도 인자는 고유 척도 인자와 다를 수 있는 UIKit 척도 인자입니다. 개발자 안내는 ['scale'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiscreen/1617836-scale) 을 참조하십시오
>

 and [`nativeScale`](/documentation/uikit/uiscreen/1617825-nativescale)

.



#### [Device size classes](/design/human-interface-guidelines/layout#Device-size-classes)



Different size class combinations apply to the full-screen experience on different devices, based on screen size.

> 화면 크기에 따라 다른 장치의 전체 화면 경험에 다른 크기 클래스 조합이 적용됩니다.
>



![An illustration of an iPad and an iPhone in both portrait and landscape orientations. Each device in each orientation includes a red screen and arrowed lines that indicate the full height and width of the screen.](https://docs-assets.developer.apple.com/published/ea27d20bc28241ad815bbca4b92b9b71/layout-size-classes@2x.png)







| Device | Portrait orientation | Landscape orientation |

| --- | --- | --- |

| 12.9” iPad Pro | Regular width, regular height | Regular width, regular height |

| 11” iPad Pro | Regular width, regular height | Regular width, regular height |

| 10.5” iPad Pro | Regular width, regular height | Regular width, regular height |

| 9.7” iPad | Regular width, regular height | Regular width, regular height |

| 7.9” iPad mini | Regular width, regular height | Regular width, regular height |

| iPhone 14 Pro Max | Compact width, regular height | Regular width, compact height |

| iPhone 14 Pro | Compact width, regular height | Compact width, compact height |

| iPhone 14 Plus | Compact width, regular height | Regular width, compact height |

| iPhone 14 | Compact width, regular height | Compact width, compact height |

| iPhone 13 Pro Max | Compact width, regular height | Regular width, compact height |

| iPhone 13 Pro | Compact width, regular height | Compact width, compact height |

| iPhone 13 | Compact width, regular height | Compact width, compact height |

| iPhone 13 mini | Compact width, regular height | Compact width, compact height |

| iPhone 12 Pro Max | Compact width, regular height | Regular width, compact height |

| iPhone 12 Pro | Compact width, regular height | Compact width, compact height |

| iPhone 12 | Compact width, regular height | Compact width, compact height |

| iPhone 12 mini | Compact width, regular height | Compact width, compact height |

| iPhone 11 Pro Max | Compact width, regular height | Regular width, compact height |

| iPhone 11 Pro | Compact width, regular height | Compact width, compact height |

| iPhone 11 | Compact width, regular height | Regular width, compact height |

| iPhone XS Max | Compact width, regular height | Regular width, compact height |

| iPhone XS | Compact width, regular height | Compact width, compact height |

| iPhone XR | Compact width, regular height | Regular width, compact height |

| iPhone X | Compact width, regular height | Compact width, compact height |

| iPhone 8 Plus | Compact width, regular height | Regular width, compact height |

| iPhone 8 | Compact width, regular height | Compact width, compact height |

| iPhone 7 Plus | Compact width, regular height | Regular width, compact height |

| iPhone 7 | Compact width, regular height | Compact width, compact height |

| iPhone 6s Plus | Compact width, regular height | Regular width, compact height |

| iPhone 6s | Compact width, regular height | Compact width, compact height |

| iPhone SE | Compact width, regular height | Compact width, compact height |

| iPod touch 5th generation and later | Compact width, regular height | Compact width, compact height |



On iPad, size classes also apply when your app or game runs in a [multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)

> iPad에서 크기 클래스는 앱 또는 게임이 [스크래킹](https://developer.apple.com/design/human-interface-guidelines/multitasking) 에서 실행될 때도 적용됩니다
>

 configuration.



![An illustration of iPad in landscape orientation with the left two-thirds of its screen shaded.](https://docs-assets.developer.apple.com/published/e2c436a11b4dd3636828c6c3844465b2/layout-two-thirds@2x.png)2/3 split view![An illustration of iPad in landscape orientation with the left half of its screen shaded.](https://docs-assets.developer.apple.com/published/976669fb0a060433ac179c23d4728186/layout-half@2x.png)1/2 split view![An illustration of iPad in landscape orientation with the left one-third of its screen shaded.](https://docs-assets.developer.apple.com/published/f25f319072f994822c92d9ffa63bf9c8/layout-thirds@2x.png)1/3 split view



| Device | Mode | Portrait orientation | Landscape orientation |

| --- | --- | --- | --- |

| 12.9” iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |

|  | 1/2 split view | N/A | Regular width, regular height |

|  | 1/3 split view | Compact width, regular height | Compact width, regular height |

| 11” iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |

|  | 1/2 split view | N/A | Compact width, regular height |

|  | 1/3 split view | Compact width, regular height | Compact width, regular height |

| 10.5” iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |

|  | 1/2 split view | N/A | Compact width, regular height |

|  | 1/3 split view | Compact width, regular height | Compact width, regular height |

| 9.7” iPad | 2/3 split view | Compact width, regular height | Regular width, regular height |

|  | 1/2 split view | N/A | Compact width, regular height |

|  | 1/3 split view | Compact width, regular height | Compact width, regular height |

| 7.9” iPad mini 4 | 2/3 split view | Compact width, regular height | Regular width, regular height |

|  | 1/2 split view | N/A | Compact width, regular height |

|  | 1/3 split view | Compact width, regular height | Compact width, regular height |



### [watchOS](/design/human-interface-guidelines/layout#watchOS)







| Series | Screen size | Width (pixels) | Height (pixels) |

| --- | --- | --- | --- |

| Apple Watch Ultra | 49mm | 410 | 502 |

| 7 and later | 41mm | 352 | 430 |

| 7 and later | 45mm | 396 | 484 |

| 4, 5, and 6 | 40mm | 324 | 394 |

| 4, 5, and 6 | 44mm | 368 | 448 |

| 1, 2, and 3 | 38mm | 272 | 340 |

| 1, 2, and 3 | 42mm | 312 | 390 |



[Resources](/design/human-interface-guidelines/layout#Resources)

----------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/layout#Related)



[Right to left](/design/human-interface-guidelines/right-to-left)





#### [Developer documentation](/design/human-interface-guidelines/layout#Developer-documentation)



[`UITraitCollection`](/documentation/uikit/uitraitcollection)





[`UITraitEnvironment`](/documentation/uikit/uitraitenvironment)





[Responding to changing display modes on Apple TV](/documentation/uikit/app_and_environment/responding_to_changing_display_modes_on_apple_tv)





#### [Videos](/design/human-interface-guidelines/layout#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/48/0F960683-D91F-4CA9-9658-6FBB11F0683D/3272_wide_250x141_1x.jpg) What's New in iOS Design](https://developer.apple.com/videos/play/wwdc2019/808) 

[![](https://devimages-cdn.apple.com/wwdc-services/images/7/2546ECBD-6443-41EC-921D-6429026F8B67/1700_wide_250x141_1x.jpg) Essential Design Principles](https://developer.apple.com/videos/play/wwdc2017/802) 

[Change log](/design/human-interface-guidelines/layout#Change-log)

------------------------------------------------------------------







| Date | Changes |

| --- | --- |

| June 21, 2023 | Updated to include guidance for visionOS. |

| September 14, 2022 | Added specifications for iPhone 14 Pro Max, iPhone 14 Pro, iPhone 14 Plus, iPhone 14, and Apple Watch Ultra. |




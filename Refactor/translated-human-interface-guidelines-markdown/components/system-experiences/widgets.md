### [[Components - System experiences](./translated-human-interface-guidelines-markdown/components/system-experiences.md)]  
  
# **Widgets**  



![An image of the small Notes widget. Below the yellow bar that contains the app icon and name, the widget displays a single note in black text on a white background.](https://docs-assets.developer.apple.com/published/0fb7093d499f2152926c4f6143786f53/notes-small-light@2x.png)



![An image of the small Notes widget. Below the yellow bar that contains the app icon and name, the widget a single note in white text on a black background.](https://docs-assets.developer.apple.com/published/d6644cc54f9ab3bfcd3f689f3170fc76/notes-small-dark@2x.png)



**Support StandBy and Night Mode.** In StandBy, the system displays two small system family widgets side-by-side, scaled up so they fill the Lock Screen. Widgets that appear in StandBy typically don’t use rich images or color to convey meaning but instead make use of the additional space by scaling up and rearranging text so people can glance at the widget content from a greater distance. To seamlessly blend with the black background, don’t use background colors for your widget when it appears in StandBy.

> **스탠바이 및 야간 모드를 지원합니다.** 대기 모드에서 시스템은 두 개의 작은 시스템 제품군 위젯을 나란히 표시하고 잠금 화면을 채우도록 확대합니다. 스탠바이에 나타나는 위젯은 일반적으로 의미를 전달하기 위해 풍부한 이미지나 색상을 사용하지 않고 텍스트를 확대하고 재배치하여 사용자가 더 멀리서 위젯 내용을 볼 수 있도록 추가 공간을 활용합니다. 검은색 배경과 완벽하게 혼합하려면 위젯이 대기에 나타날 때 배경색을 사용하지 마십시오.
>



* [Correct usage](#)

* [Incorrect usage](#)

![An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.](https://docs-assets.developer.apple.com/published/b45b626f06315aa7ecee84d57851b3b8/removed-background@2x.png)![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)



![An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right. The Watch widget appears with the background removed and the Weather widget isn't optimized for StandBy.](https://docs-assets.developer.apple.com/published/a3770022b9c5348dca2ab246e1809da6/with-background@2x.png)![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)



In Night Mode, the system applies a red tint to widgets.

> 야간 모드에서 시스템은 위젯에 빨간색 선트를 적용합니다.
>



![An image of iPhone in Night Mode. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.](https://docs-assets.developer.apple.com/published/5742993fb79cf715b9b0dbe799de708a/widgets-night-mode@2x.png)Night Mode**Adjust colors and images for the vibrant rendering mode.** The system renders widgets on the Lock Screen and on the Mac desktop using a vibrant, blurred appearance. The opacity of pixels within your image determines the strength of the blurred material effect. Fully transparent pixels let the background wallpaper pass through as–is. When creating assets for the vibrant rendering mode, render content like images, numbers, or text at full opacity. The brightness of pixels determines how vibrant they appear on the Lock Screen: Brighter gray values provide more contrast, and darker values provide less contrast. To establish hierarchy, use white or light gray for the most prominent content and darker grayscale values for secondary elements.



To make sure images look great in the vibrant rendering mode:

> 선명한 렌더링 모드에서 이미지가 잘 보이도록 하려면:
>



* Confirm that image content has sufficient contrast in grayscale.

> * 영상 콘텐츠의 그레이스케일 대비가 충분한지 확인합니다.
>

* Use opaque grayscale values, rather than opacities of white, to achieve the best vibrant material effect.

> * 흰색의 불투명도가 아닌 불투명 계조 값을 사용하여 최상의 선명한 재료 효과를 얻을 수 있습니다.
>



**Support full color and vibrant appearances for widgets on the Mac desktop.** Widgets that people place on the Mac desktop take on rich, full color appearances and a vibrant, monochromatic appearance to recede when people use apps so they can focus on their app usage. Be sure to prepare your widgets to offer enough contrast to be glanceable and show their information while they take on the vibrant appearance. Note that, starting with macOS 14, people can place iPhone widgets on the Mac. Be sure to modify your iPhone widgets to support the vibrant appearance in macOS.

> **Mac 데스크톱의 위젯에 대해 전체 색상과 선명한 외관을 지원합니다.** 사람들이 Mac 바탕화면에 배치하는 위젯은 풍부하고 풀 컬러의 외관과 앱 사용에 집중할 수 있도록 앱을 사용할 때 선명하고 단색의 외관을 갖추고 있습니다. 선명한 모습을 보여주는 동안 위젯을 충분히 대비할 수 있도록 준비하고 정보를 표시해야 합니다. 맥OS 14부터는 아이폰 위젯을 맥에 배치할 수 있다. macOS에서 선명한 모습을 지원하도록 아이폰 위젯을 수정해야 합니다.
>



[Previews and placeholders](/design/human-interface-guidelines/widgets#Previews-and-placeholders)

-------------------------------------------------------------------------------------------------



**Design a realistic preview to display in the widget gallery.** Highlighting your widget’s capabilities — and clearly representing the experiences each widget type or size can provide — helps people make an informed decision. You can display real data in your widget preview, but if the data takes too long to generate or load, display realistic simulated data instead.

> **위젯 갤러리에 표시할 사실적인 미리보기를 설계합니다.** 위젯의 기능을 강조하고 각 위젯 유형 또는 크기가 제공할 수 있는 경험을 명확하게 나타내는 것은 사람들이 정보에 입각한 결정을 내리는 데 도움이 됩니다. 위젯 미리 보기에 실제 데이터를 표시할 수 있지만, 데이터를 생성하거나 로드하는 데 시간이 너무 오래 걸리는 경우에는 실제 시뮬레이션된 데이터를 대신 표시하십시오.
>



**Design placeholder content that helps people recognize your widget.** An installed widget displays placeholder content while its data loads. You can create an effective placeholder appearance by combining static interface components with semi-opaque shapes that stand in for dynamic content. For example, you can use rectangles of different widths to suggest lines of text, and circles or squares in place of glyphs and images.

> **위젯을 사람들이 인식할 수 있도록 도와주는 자리 표시자 콘텐츠를 디자인합니다.** 설치된 위젯은 데이터가 로드되는 동안 자리 표시자 컨텐츠를 표시합니다. 정적 인터페이스 구성요소와 동적 내용을 나타내는 반투명 모양을 결합하여 효과적인 자리 표시자 모양을 만들 수 있습니다. 예를 들어, 다른 너비의 직사각형을 사용하여 텍스트 선을 제안하고 글리프 및 이미지 대신 원 또는 사각형을 사용할 수 있습니다.
>



![An image of a small Tips widget that displays placeholder content on top of a yellow background. In the bottom half of the widget, three horizontal bars in different shades of yellow represent lines of text.](https://docs-assets.developer.apple.com/published/58159b6d0c63c30d5a93fe9842fbe93d/tips-placeholder@2x.png)



![An image of a small Tips widget that displays actual data on top of a yellow background. The horizontal bars in the placeholder widget are replaced by three short lines of text in different shades of yellow.](https://docs-assets.developer.apple.com/published/c346b25f7fc0ec1d084d3b9db6dce4ce/tips@2x.png)



**Write a succinct description of your widget.** The widget gallery displays descriptions that help people understand what each widget does. It generally works well to begin a description with an action verb — for example, “See the current weather conditions and forecast for a location” or “Keep track of your upcoming events and meetings.” Avoid including unnecessary phrases that reference the widget itself, like “This widget shows…,” “Use this widget to…,” or “Add this widget.” Use approachable language and [sentence-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)

> **위젯에 대한 간단한 설명을 작성합니다.** 위젯 갤러리에는 각 위젯이 수행하는 작업을 이해하는 데 도움이 되는 설명이 표시됩니다. 일반적으로 "현재 날씨 상태 및 장소 예측 보기" 또는 "앞으로 있을 이벤트 및 회의를 계속 추적"과 같은 동작 동사로 설명을 시작하는 것이 좋습니다 위젯 자체를 참조하는 불필요한 문구(예: "이 위젯을 사용하여..." 또는 "이 위젯 추가")는 포함하지 마십시오 접근 가능한 언어와 [어댑티브 스타일 대문자화](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64) 를 사용하십시오
>

.



**Group your widget’s sizes together, and provide a single description.** If your widget is available in multiple sizes, group the sizes together so people don’t think each size is a different widget. Provide a single description of your widget — regardless of how many sizes you offer — to avoid repetition and to help people understand how each size provides a slightly different perspective on the same content and functionality.

> **위젯의 크기를 함께 그룹화하고 하나의 설명을 제공합니다.** 여러 크기의 위젯을 사용할 수 있는 경우 크기를 그룹화하여 사용자가 각 크기가 서로 다른 위젯이라고 생각하지 않도록 하십시오. 제공하는 크기에 상관없이 위젯에 대한 단일 설명을 제공하여 반복을 방지하고 각 크기가 동일한 콘텐츠와 기능에 대해 어떻게 다른 관점을 제공하는지 이해하도록 지원합니다.
>



**Consider coloring the Add button.** After people choose your app in the widget gallery, an Add button appears below the group of widgets you offer. You can specify a color for this button to help remind people of your brand.

> **Add 버튼을 색칠하는 것을 고려해 보십시오.** 위젯 갤러리에서 사용자의 앱을 선택하면 제공하는 위젯 그룹 아래에 추가 단추가 나타납니다. 이 단추의 색상을 지정하여 사용자의 브랜드를 상기시킬 수 있습니다.
>



![An illustration that represents the widget gallery open to the small widget for the Notes app. Below the widget is a page control showing that this is the first page of three; below the page control is a button that uses the Notes app’s yellow accent color.](https://docs-assets.developer.apple.com/published/0676d2342d1dfc1b2e7101a6ba621063/add-button-custom-color-1@2x.png)



![An illustration that represents the widget gallery open to the small widget for the Weather app. Below the widget is a page control showing that this is the first page of three; below the page control is a button that uses the Weather app’s blue accent color.](https://docs-assets.developer.apple.com/published/7f90fe184f20b46fd1afab61bd736592/add-button-custom-color-2@2x.png)



[Platform considerations](/design/human-interface-guidelines/widgets#Platform-considerations)

---------------------------------------------------------------------------------------------



*No additional considerations for macOS. Not supported in tvOS or visionOS.*

*No additional considerations for macOS. Not supported in tvOS or visionOS.*

> *macOS에 대한 추가 고려 사항 없음. TVOS 또는 비전에서 지원되지 않음OS.*
>



### [iOS and iPadOS](/design/human-interface-guidelines/widgets#iOS-and-iPadOS)



Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for [Complications](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/complications)

> 잠금 화면의 위젯은 기능적으로 [Complexions](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/complications) 의 설계 원리를 따르고 복잡한 문제를 관찰하는 것과 유사합니다
>

 in addition to design principles for widgets. Both support Always-On displays and emphasize glanceable content within their limited space. Provide useful information in your Lock Screen widget, and don’t treat it only as an additional way for people to launch into your app. Additionally, the vibrant rendering mode that widgets on the Lock Screen use is similar to the accented rendering mode for watch complications because they both communicate information without relying on color only. In many cases, a design for complications also works well for widgets on the Lock Screen (and vice versa), so consider creating them in tandem.

> 또한 위젯에 대한 설계 원칙도 포함됩니다. 두 제품 모두 상시 디스플레이를 지원하며 제한된 공간 내에서 눈에 띄는 콘텐츠를 강조합니다. 잠금 화면 위젯에서 유용한 정보를 제공하고, 사용자가 앱을 실행하기 위한 추가 방법으로만 취급하지 마십시오. 또한, 잠금 화면에서 위젯을 사용하는 선명한 렌더링 모드는 색상에만 의존하지 않고 정보를 전달하기 때문에 시계 문제에 대한 악센트 렌더링 모드와 유사하다. 대부분의 경우 복잡한 설계는 잠금 화면의 위젯에도 잘 작동하므로 함께 만드는 것을 고려해 보십시오.
>



Your app can offer widgets on the Lock Screen in three different shapes: as inline text that appears above the clock, and as circular and rectangular shapes that appear below the clock.

> 잠금 화면의 위젯은 시계 위에 나타나는 인라인 텍스트와 시계 아래에 나타나는 원형 및 직사각형 모양의 세 가지 모양으로 제공할 수 있습니다.
>



![A partial screenshot of the Lock Screen on iPhone that shows three Weather widgets below the time. From the left, the widgets are an inline text widget and two circular widgets.](https://docs-assets.developer.apple.com/published/a823acc4c31f5a7483d116321d45755b/weather-widget-lock-screen@2x.png)### [iOS](/design/human-interface-guidelines/widgets#iOS)



**Support Always-On display.** Devices with Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in Always-On display, and make sure your content is legible.

> **상시 지원 디스플레이.** Always-On 디스플레이가 있는 장치는 잠금 화면의 위젯을 감소된 휘도로 렌더링합니다. 상시 디스플레이에서 충분한 대비를 제공하는 회색 수준을 사용하고 콘텐츠를 읽을 수 있는지 확인합니다.
>



For developer guidance, see [Creating accessory widgets and watch complications](https://developer.apple.com/design/human-interface-guidelines/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications)

> 개발자 지침은 [액세서리 위젯 작성 및 복잡도 감시](https://developer.apple.com/design/human-interface-guidelines/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications) 를 참조하십시오
>

, [WidgetRenderingMode](https://developer.apple.com/documentation/widgetkit/WidgetRenderingMode)

, and [vibrant](https://developer.apple.com/documentation/widgetkit/WidgetRenderingMode/vibrant)

.



### [watchOS](/design/human-interface-guidelines/widgets#watchOS)



**Provide a colorful background that conveys meaning.** By default, widgets in the Smart Stack use a black background. Consider using a custom color that provides additional meaning. For example, the Stocks app uses a red background for falling stock values and a green background if a stock’s value rises.

> **의미를 전달하는 다채로운 배경을 제공합니다.** 기본적으로 스마트 스택의 위젯은 검은색 배경을 사용합니다. 추가적인 의미를 제공하는 사용자 정의 색상을 사용하는 것을 고려해 보십시오. 예를 들어, 주식 앱은 주식 가치 하락에 빨간색 배경을 사용하고 주식 가치가 상승할 경우 녹색 배경을 사용한다.
>



[Specifications](/design/human-interface-guidelines/widgets#Specifications)

---------------------------------------------------------------------------



As you design your widgets, use the following values for guidance.

> 위젯을 설계할 때 다음 값을 사용하여 지침을 제공합니다.
>



### [iOS widget dimensions](/design/human-interface-guidelines/widgets#iOS-widget-dimensions)







| Screen size (portrait, pt) | Small (pt) | Medium (pt) | Large (pt) | Circular (pt) | Rectangular (pt) | Inline (pt) |

| --- | --- | --- | --- | --- | --- | --- |

| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |

| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |

| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |

| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |

| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |

| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |

| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |

| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |

| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |

| 320x568 | 141x141 | 292x141 | 292x311 | N/A | N/A | N/A |



### [iPadOS widget dimensions](/design/human-interface-guidelines/widgets#iPadOS-widget-dimensions)







| Screen size (portrait, pt) | Target | Small (pt) | Medium (pt) | Large (pt) | Extra large (pt) |

| --- | --- | --- | --- | --- | --- |

| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |

| Device | 120x120 | 260x120 | 260x260 | 540x260 |

| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |

| Device | 120x120 | 260x120 | 260x260 | 540x260 |

| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |

| Device | 124x124 | 272x124 | 272x272 | 568x272 |

| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |

| Device | 136x136 | 300x136 | 300x300 | 628x300 |

| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |

| Device | 132x132 | 288x132 | 288x288 | 600x288 |

| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |

| Device | 136x136 | 300x136 | 300x300 | 628x300 |

| 954x1373 \* | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |

| Device | 162x162 | 350x162 | 350x350 | 726x350 |

| 970x1389 \* | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |

| Device | 162x162 | 350x162 | 350x350 | 726x350 |

| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |

| Device | 160x160 | 356x160 | 356x356 | 748x356 |

| 1192x1590 \* | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |

| Device | 188x188 | 412x188 | 412x412 | 860x412 |



\* When Display Zoom is set to More Space.

> \* Display Zoom(디스플레이 줌)이 More Space(추가 공간)로 설정된 경우.
>



### [watchOS widget dimensions](/design/human-interface-guidelines/widgets#watchOS-widget-dimensions)







| Apple Watch size | Size of a widget in the Smart Stack (pts) |

| --- | --- |

| 40mm | 304x139 |

| 41mm | 330x145 |

| 44mm | 346x153 |

| 45mm | 368x161 |

| 49mm | 382x163 |



[Resources](/design/human-interface-guidelines/widgets#Resources)

-----------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/widgets#Related)



[Layout](/design/human-interface-guidelines/layout)





#### [Developer documentation](/design/human-interface-guidelines/widgets#Developer-documentation)



[WidgetKit](/documentation/WidgetKit)





[Developing a WidgetKit strategy](/documentation/WidgetKit/Developing-a-WidgetKit-strategy)





#### [Videos](/design/human-interface-guidelines/widgets#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/5631C647-3158-42F6-A1D3-50566815A1BB/8056_wide_250x141_1x.jpg) Bring widgets to life](https://developer.apple.com/videos/play/wwdc2023/10028) 

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/D21F46FB-1BFA-479D-B9DD-71C620C5E482/8055_wide_250x141_1x.jpg) Bring widgets to new places](https://developer.apple.com/videos/play/wwdc2023/10027) 

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/079B9406-40CE-48BA-88DC-21BCA7841674/4938_wide_250x141_1x.jpg) Principles of great widgets](https://developer.apple.com/videos/play/wwdc2021/10048) 

[Change log](/design/human-interface-guidelines/widgets#Change-log)

-------------------------------------------------------------------







| Date | Changes |

| --- | --- |

| June 5, 2023 | Updated guidance to include widgets in watchOS, widgets on the iPad Lock Screen, and updates for iOS 17, iPadOS 17, and macOS 14. |

| November 3, 2022 | Added guidance for widgets on the iPhone Lock Screen and updated design comprehensives for iPhone 14, iPhone 14 Pro, and iPhone 14 Pro Max. |




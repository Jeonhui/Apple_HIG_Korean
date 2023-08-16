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


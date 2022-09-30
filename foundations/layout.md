# **[foundations] layout**

### Using a consistent layout that adapts to various contexts makes your experience more approachable and helps people enjoy their favorite apps and games on all their devices.
> 다양한 상황에 적응하는 일관된 레이아웃을 사용하면 사용자의 환경에 더 쉽게 접근할 수 있고 사람들이 좋아하는 앱과 게임을 모든 장치에서 즐길 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-layout-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-layout-intro-dark_2x.png)

# **Guides and safe areas**

A *layout guide* defines a rectangular region that helps you position, align, and space your content on the screen. The system includes predefined layout guides that make it easy to apply standard margins around content and restrict the width of text for optimal readability. You can also define custom layout guides.
> 레이아웃 안내서는 화면에서 콘텐츠를 배치, 정렬 및 띄어쓰기에 도움이 되는 직사각형 영역을 정의합니다. 이 시스템에는 콘텐츠 주변에 표준 여백을 쉽게 적용하고 최적의 가독성을 위해 텍스트 폭을 제한할 수 있는 사전 정의된 레이아웃 가이드가 포함되어 있습니다. 사용자 정의 레이아웃 가이드를 정의할 수도 있습니다.
>




A *safe area* defines the area within a view that isn’t covered by a navigation bar, tab bar, toolbar, or other views a window or scene might provide. Safe areas are essential for avoiding a device’s interactive and display features, like the Dynamic Island on iPhone or the camera housing on some Mac models.
> 안전 영역은 탐색 모음, 탭 모음, 도구 모음 또는 창이나 장면이 제공할 수 있는 다른 보기로 포함되지 않는 보기 내의 영역을 정의합니다. iPhone의 Dynamic Island 또는 일부 Mac 모델의 카메라 하우징과 같은 장치의 대화식 및 디스플레이 기능을 피하려면 안전한 영역이 필수적입니다.
>




In iOS, iPadOS, and tvOS, the system defines a collection of *traits* that characterize variations in the device environment that can affect the way your app displays on the screen. Using SwiftUI or Auto Layout, you can ensure that your interface adapts dynamically to a wide range of traits and contexts, including:
> iOS, iPadOS 및 tvOS에서 시스템은 화면에 앱이 표시되는 방식에 영향을 줄 수 있는 장치 환경의 변화를 특징짓는 특성 모음을 정의합니다. 스위프트 사용UI 또는 자동 레이아웃에서는 인터페이스가 다음과 같은 다양한 특성과 상황에 동적으로 적응하도록 할 수 있습니다.
>




- Different device screen sizes, resolutions, and color spaces
- >  다양한 장치 화면 크기, 해상도 및 색 공간

- Different device orientations (portrait/landscape)
- Split view
- External display support, Display Zoom, and multitasking modes on iPad
- >  iPad의 외부 디스플레이 지원, 디스플레이 줌 및 멀티태스킹 모드

- Dynamic Type text-size changes
- Internationalization features the system can enable based on locale (left-to-right/right-to-left layout direction, date/time/number formatting, font variation, text length)
- >  시스템이 로케일(왼쪽에서 오른쪽으로/오른쪽에서 왼쪽으로 레이아웃 방향, 날짜/시간/숫자 형식, 글꼴 변형, 텍스트 길이)을 기준으로 활성화할 수 있는 국제화 기능

- System feature availability

# **Best practices**

**Design a consistent layout that adapts gracefully to context changes, while displaying the same content as much as possible.** People expect your experience to work well and remain familiar when they rotate their device, resize a window, add another display, or switch to a different device. Ensure an adaptable interface by respecting system-defined safe areas, margins, and guides and specifying layout modifiers to fine-tune the placement of views in your hierarchy.
> 가능한 한 동일한 콘텐츠를 표시하면서 상황 변화에 적절하게 적응하는 일관된 레이아웃을 설계하십시오. 사람들은 장치를 회전하거나, 창의 크기를 조정하거나, 다른 디스플레이를 추가하거나, 다른 장치로 전환할 때 사용자 환경이 잘 작동하고 친숙해지기를 기대합니다. 시스템 정의 안전 영역, 여백 및 가이드를 존중하고 계층에서 뷰 배치를 미세 조정하기 위한 레이아웃 수정자를 지정하여 적응 가능한 인터페이스를 보장합니다.
>




**Respect key display and system features in each platform.** Safe areas help you accommodate features like the corner radius and sensor housings on various devices, and avoid interfering with interactive system elements like Dynamic Island on iPhone and the Home indicator and app switcher on iPhone and iPad. Safe areas also help you account for interactive components like bars, dynamically repositioning content if sizes change.
> 각 플랫폼의 주요 디스플레이 및 시스템 기능을 존중합니다. 안전한 영역은 다양한 장치의 코너 반경 및 센서 하우징과 같은 기능을 수용하도록 도와줍니다. iPhone의 Dynamic Island와 iPhone 및 iPad의 Home 표시기와 앱 전환기와 같은 대화형 시스템 요소에 간섭하지 않도록 합니다. 또한 안전 영역은 막대와 같은 대화형 구성 요소를 설명하는 데 도움이 되며 크기가 변경되면 동적으로 컨텐츠의 위치를 변경할 수 있습니다.
>




**Use placement to convey relative importance.** In general, place principal items in the upper half of the screen or window, near the leading side. People typically start in this area, whether they’re looking at the screen or using a screen reader like VoiceOver.
> 상대적인 중요성을 전달하기 위해 배치를 사용합니다. 일반적으로 주요 항목은 화면 또는 창의 위쪽, 앞쪽 근처에 배치합니다. 사람들은 일반적으로 화면을 보든 VoiceOver와 같은 화면 판독기를 사용하든 이 영역에서 시작합니다.
>




**Elevate essential information by giving it sufficient space.** People want to view the most important information instantly, so you don’t want to clutter the screen or window with nonessential details. People can easily access secondary information by scrolling.
> 중요한 정보에 충분한 공간을 제공하여 정보를 높이십시오. 사람들은 가장 중요한 정보를 즉시 보고 싶어하므로 필수적이지 않은 세부 정보로 화면이나 창을 어지럽히지 않을 것입니다. 사람들은 스크롤을 통해 2차 정보에 쉽게 접근할 수 있다.
>




**Create visual groupings to help people find the information they want.** For example, you might use negative space, background shapes, colors, and materials, or separator lines to display related elements and information in distinct areas.
> 예를 들어 부정적인 공간, 배경 모양, 색상 및 재료 또는 구분선을 사용하여 관련 요소 및 정보를 서로 다른 영역에 표시할 수 있습니다.
>




**Use alignment to ease visual scanning and to communicate organization and hierarchy.** Alignment makes an app look neat and organized, helps people focus while scrolling, and makes it easier to find information. Indentation and alignment can also help people visualize an information hierarchy.
> 정렬을 사용하면 시각적 스캔을 쉽게 하고 조직과 계층을 전달할 수 있습니다. 정렬은 앱을 깔끔하고 조직적으로 보이게 하고 스크롤하는 동안 집중할 수 있도록 하며 정보를 쉽게 찾을 수 있습니다. 들여쓰기 및 정렬은 또한 사람들이 정보 계층을 시각화하는 데 도움이 될 수 있습니다.
>




**Be mindful of aspect ratio.** Different screen sizes may have different aspect ratios, causing artwork to appear cropped, letterboxed, or pillarboxed. When this is the case, don’t change the aspect ratio of the artwork; instead, scale it to fill the screen so that important visual content remains in view on all display sizes.
> 가로 세로 비율에 유의하십시오. 화면 크기에 따라 가로 세로 비율이 다를 수 있으며, 이로 인해 아트워크가 잘리거나 편지함 또는 필러박스로 표시될 수 있습니다. 이 경우 아트워크의 가로 세로 비율을 변경하지 말고 모든 디스플레이 크기에 중요한 시각적 콘텐츠가 계속 표시되도록 화면을 채우도록 크기를 조정합니다.
>




**Be prepared for text-size changes.** People expect most apps to respond when they choose a different text size. To accommodate text-size changes, you might need to adjust the layout. For guidance on displaying text in your app, see [Typography](../foundations/typography).
> 텍스트 크기 변경에 대비하십시오. 사람들은 대부분의 앱이 다른 텍스트 크기를 선택할 때 응답할 것으로 기대합니다. 텍스트 크기 변경 사항을 수용하려면 레이아웃을 조정해야 할 수 있습니다. 앱에 텍스트를 표시하는 방법에 대한 지침은 타이포그래피를 참조하십시오.
>




**When possible, consider alluding to hidden content by partially displaying offscreen elements.** In large collections where content doesn’t fit on a single screen, you might be able to hint at the additional content by showing portions of the offscreen items.
> 가능하면 오프스크린 요소를 부분적으로 표시하여 숨겨진 콘텐츠를 암시하는 것을 고려하십시오. 콘텐츠가 단일 화면에 맞지 않는 대규모 컬렉션에서는 오프스크린 항목의 일부를 표시하여 추가 콘텐츠를 암시할 수 있습니다.
>




**On touch screens, provide ample touch targets for interactive components.** Maintain a minimum tappable area of 44x44 points for all controls.
> 터치 스크린에서 대화형 구성 요소를 위한 충분한 터치 표적을 제공한다. 모든 조정기에 대해 최소 44x44 포인트의 탭 영역을 유지한다.
>




**Preview your app on multiple devices, using different orientations, localizations, and text sizes.** Although it’s generally best to preview features like wide color on actual devices, you can use Xcode Simulator to check for clipping and other layout issues. For example, if your iOS app supports landscape mode, you can use Simulator to make sure your layouts look great regardless of whether the device rotates left or right.
> 여러 장치에서 다른 방향, 지역화 및 텍스트 크기를 사용하여 앱을 미리 봅니다. 일반적으로 실제 장치에서 넓은 색상과 같은 기능을 미리 보는 것이 가장 좋지만 Xcode Simulator를 사용하여 클리핑 및 기타 레이아웃 문제를 확인할 수 있습니다. 예를 들어, iOS 앱이 가로 모드를 지원하는 경우 시뮬레이터를 사용하여 장치가 왼쪽 또는 오른쪽으로 회전하는지 여부에 관계없이 레이아웃이 멋지게 보이도록 할 수 있습니다.
>




# **Platform considerations**

# **iOS, iPadOS**

**Aim to support both portrait and landscape orientations.** People choose different orientations for a variety of reasons, and they generally expect apps to work well in every context. If it’s essential that your app run in a single orientation, don’t tell people to rotate their device to match; if your app doesn’t rotate automatically when someone holds the device in an unsupported orientation, they’ll know instinctively to rotate it. If your app is landscape-only, make sure it runs equally well whether people rotate their device to the left or the right.
> 세로 방향과 가로 방향 모두를 지원하는 것을 목표로 한다. 사람들은 다양한 이유로 다른 방향을 선택하고, 일반적으로 모든 상황에서 앱이 잘 작동하기를 기대한다. 앱을 단일 방향으로 실행하는 것이 필수인 경우, 다른 사람이 장치를 지원하지 않는 방향으로 잡을 때 앱이 자동으로 회전하지 않으면 본능적으로 장치를 회전시킬 수 있습니다. 앱이 가로 전용인 경우, 사람들이 장치를 왼쪽으로 회전하든 오른쪽으로 회전하든 똑같이 잘 실행되도록 하십시오.
>




**If your app runs on a specific device, make sure it runs on every screen size for that device.** In other words, an iPhone-only app must run on every iPhone screen size and an iPad-only app must run on every iPad screen size. For guidance, see [Device screen sizes and orientations](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#device-screen-sizes-and-orientations).
> 즉, iPhone 전용 앱은 iPhone 화면 크기마다 실행되어야 하며 iPad 전용 앱은 iPad 화면 크기마다 실행되어야 합니다. 자세한 내용은 장치 화면 크기 및 방향을 참조하십시오.
>




**Inset full-width buttons.** Respect the standard system-defined margins on the sides of full-width buttons. A full-width button at the bottom of the screen generally looks best when it has rounded corners and it aligns with the bottom of the safe area — which also ensures that it doesn’t conflict with the Home indicator.
> 전체 너비 단추를 삽입합니다. 전체 너비 단추의 측면에 있는 표준 시스템 정의 여백을 준수하십시오. 일반적으로 화면 아래쪽의 전체 너비 단추는 모서리가 둥글고 안전 영역의 맨 아래에 정렬되어 홈 표시기와 충돌하지 않을 때 가장 잘 보입니다.
>




**Extend visual content to fill the screen.** Make sure backgrounds extend to the edges of the display, and that vertically scrollable layouts, like tables and collections, continue all the way to the bottom.
> 화면을 채우도록 시각적 콘텐츠를 확장합니다. 배경은 디스플레이 가장자리까지 확장되고 테이블 및 모음과 같이 수직으로 스크롤할 수 있는 레이아웃이 아래까지 계속되는지 확인합니다.
>




**On iPad, consider placing controls on the sides of the screen in landscape orientation.** When controls are on the left and right sides of the screen, people can reach them easily with both hands while they’re holding the device.
> iPad에서는 가로 방향으로 화면 측면에 컨트롤을 배치하는 것을 고려하십시오. 컨트롤이 화면의 왼쪽과 오른쪽에 있으면 사용자가 장치를 잡고 있는 동안 두 손으로 쉽게 컨트롤에 접근할 수 있습니다.
>




**Avoid placing interactive controls at the bottom edge of the screen when possible.** Regardless of orientation, people use system gestures at the bottom edge of the display to access features like the Home screen and app switcher, and these gestures may cancel custom gestures you implement in this area. Also avoid placing controls in the far corners of the screen because these areas can be difficult for people to reach comfortably. If your game needs to place controls in the lower portion of the screen — below the safe area — use matching insets when placing them at the top and bottom of the screen, and leave ample space around the Home indicator so people don’t accidentally target it when trying to interact with a control.
> 대화식 컨트롤은 가능한 화면 아래쪽 가장자리에 배치하지 마십시오. 방향과 관계없이 디스플레이 아래쪽 가장자리에 있는 시스템 제스처를 사용하여 홈 스크린 및 앱 전환기와 같은 기능에 액세스하며 이러한 제스처는 이 영역에서 구현하는 사용자 지정 제스처를 취소할 수 있습니다. 또한 조정기를 화면의 먼 모서리에 배치하지 마십시오. 이러한 영역은 사람들이 편안하게 접근하기 어려울 수 있습니다. 게임이 화면 아래쪽(안전 영역 아래)에 컨트롤을 배치해야 하는 경우 화면의 상단과 하단에 배치할 때 일치하는 삽입을 사용하고 홈 표시기 주변에 충분한 공간을 두어 사용자가 컨트롤과 상호 작용하려고 할 때 실수로 컨트롤을 겨냥하지 않도록 합니다.
>




**Be prepared for different status bar heights.** If you display content below the status bar, you can use the safe area to help dynamically reposition the content as needed.
> 다양한 상태 표시줄 높이에 대비하십시오. 상태 표시줄 아래에 콘텐츠를 표시할 경우 안전 영역을 사용하여 필요에 따라 콘텐츠를 동적으로 재배치할 수 있습니다.
>




**Hide the status bar only when it adds value or enhances your experience.** The status bar displays information people find useful and it occupies an area of the screen most apps don’t fully use, so it’s generally a good idea to keep it visible.
> 상태 표시줄은 사용자가 유용하다고 생각하는 정보를 표시하며 대부분의 앱이 완전히 사용하지 않는 화면 영역을 차지하므로 일반적으로 표시되도록 하는 것이 좋습니다.
>




### **iOS, iPadOS safe areas**

The safe area defines the area within a view that isn’t covered by a navigation bar, tab bar, toolbar, or other views a view controller might provide.
> 안전 영역은 탐색 모음, 탭 모음, 도구 모음 또는 뷰 컨트롤러가 제공할 수 있는 다른 뷰로 가려지지 않는 뷰 내의 영역을 정의합니다.
>




• [iPhone](../foundations/layout#)
• [iPad](../foundations/layout#)

-

![../foundations/layout/images/layout-guides-portrait-dark_2x.png](../foundations/layout/images/layout-guides-portrait-dark_2x.png)

![../foundations/layout/images/layout-guides-landscape-dark_2x.png](../foundations/layout/images/layout-guides-landscape-dark_2x.png)


### **iOS keyboard layout guide**

iOS 15 and later provides a keyboard layout guide that represents the space the keyboard currently occupies and accounts for safe area insets. Using this guide can help you make the keyboard feel like an integral part of your app, regardless of the type of keyboard people use or where they position it. For developer guidance, see [UIKeyboardLayoutGuide](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/).
> iOS 15 이상은 키보드가 현재 점유하고 있는 공간을 나타내고 안전 영역을 설명하는 키보드 레이아웃 가이드를 제공한다. 이 가이드를 사용하면 사용자가 사용하는 키보드 유형이나 위치에 관계없이 키보드가 앱의 필수 구성 요소처럼 느껴질 수 있습니다. 개발자 지침은 UIKeyboard Layout Guide를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-visible-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-visible-dark_2x.png)

When the keyboard is visible, the layout guide represents its area and position.
> 키보드가 보이면 레이아웃 가이드가 해당 영역과 위치를 나타냅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-dismissed-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-dismissed-dark_2x.png)

When the keyboard dismisses, the top of the layout guide matches the bottom of the safe area layout guide.
> 키보드가 해제되면 레이아웃 가이드의 상단이 안전 영역 레이아웃 가이드의 하단과 일치합니다.
>




# **macOS**

**Avoid placing controls or critical information at the bottom of a window.** People often move windows so that the bottom edge is below the bottom of the screen.
> 컨트롤이나 중요한 정보를 창 하단에 배치하지 마십시오. 사람들은 종종 창을 움직여 하단 가장자리가 화면 하단 아래에 오도록 합니다.
>




# **tvOS**

TVs vary widely in size. On Apple TV, app layouts don’t automatically adapt to the size of the screen like they do on iPhone or iPad. Instead, apps show the same interface on every display. Take extra care in designing your layout so that it looks great in a variety of screen sizes.
> 텔레비전은 크기가 매우 다양하다. Apple TV에서 앱 레이아웃은 iPhone이나 iPad에서처럼 화면 크기에 자동으로 적응하지 않습니다. 대신, 앱은 모든 디스플레이에 동일한 인터페이스를 보여준다. 다양한 화면 크기에 적합하도록 레이아웃을 설계할 때 각별히 주의하십시오.
>




**Adhere to the screen’s safe zone.** Inset primary content 60 pixels from the top and bottom of the screen, and 80 pixels from the sides. It can be difficult for people to see content that close to the edges, and unintended cropping can occur due to overscanning on older TVs. Allow only partially displayed offscreen content and elements that deliberately flow offscreen to appear outside this zone.
> 화면의 안전 영역을 고수합니다. 화면 상단과 하단에서는 60픽셀, 측면에서는 80픽셀을 기본 콘텐츠를 삽입합니다. 사람들이 가장자리에 가까이 있는 콘텐츠를 보기 어려울 수 있으며, 구형 TV의 오버스캔으로 인해 의도하지 않은 크롭이 발생할 수 있습니다. 의도적으로 화면 밖으로 흐르는 일부 화면 외 콘텐츠 및 요소만 이 영역 밖에 나타나도록 허용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-safe-zone_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-safe-zone_2x.png)

**Include appropriate padding between focusable elements.** When you use UIKit and the focus APIs, an element gets bigger when it comes into focus. Consider how elements look when they’re focused, and make sure they don’t unintentionally overlap important information.
> 포커스 가능한 요소 사이에 적절한 패딩을 포함합니다. UIKit과 포커스 API를 사용하면 포커스가 되면 요소가 커집니다. 초점이 맞춰져 있을 때 요소가 어떻게 보이는지 고려하고, 중요한 정보와 의도치 않게 겹치지 않도록 해야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-padding_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-padding_2x.png)

**Use layout templates to build media-centered apps and use grids to provide collections of content.** If the layout of your media app simply needs to present content beautifully with minimal layout customization, use a predesigned layout template. If your app needs to showcase a collection of content, use a grid to make the content easy to browse at a distance and quick to navigate with the remote.
> 레이아웃 템플릿을 사용하여 미디어 중심 앱을 구축하고 그리드를 사용하여 콘텐츠 모음을 제공합니다. 미디어 앱의 레이아웃이 최소한의 레이아웃 사용자 정의로 콘텐츠를 아름답게 표시하기만 하면 되는 경우에는 미리 설계된 레이아웃 템플릿을 사용하십시오. 앱에서 콘텐츠 모음을 보여줘야 하는 경우 그리드를 사용하여 먼 곳에서 콘텐츠를 쉽게 탐색하고 원격에서 빠르게 탐색할 수 있습니다.
>




### **Layout templates**

Apple TV templates deliver clean, consistent layouts that make content the center of attention. These templates — based on JavaScript and the Apple TV markup language (TVML) — dynamically load and populate with content when people open your app. Templates give you flexibility to create content-rich apps with predefined layouts that look good on the TV screen and are ideal for streaming media.
> Apple TV 템플릿은 콘텐츠를 관심의 중심으로 만드는 깨끗하고 일관된 레이아웃을 제공합니다. 이러한 템플릿은 JavaScript 및 Apple TV Markup Language(TVML)에 기반하여 사람들이 앱을 열 때 동적으로 콘텐츠를 로드하고 채웁니다. 템플릿을 사용하면 TV 화면에서 보기 좋고 스트리밍 미디어에 이상적인 미리 정의된 레이아웃으로 컨텐츠가 풍부한 앱을 유연하게 만들 수 있습니다.
>




**Choose a template based on its purpose.** You can customize a template’s background, color, size, layout, and more, but if your customizations make the template jarring or unrecognizable, consider using a different one or designing a custom interface.
> 용도에 따라 템플릿을 선택하십시오. 템플릿의 배경, 색상, 크기, 레이아웃 등을 사용자 지정할 수 있지만 사용자 지정으로 인해 템플릿이 지저분하거나 인식할 수 없는 경우 다른 템플릿을 사용하거나 사용자 지정 인터페이스를 설계하는 것을 고려해 보십시오.
>




-

![../foundations/layout/images/visual-design-templates-alert_2x.png](../foundations/layout/images/visual-design-templates-alert_2x.png)

### **Alert Template**

The alert template displays a message that asks for permission to perform an action, such as confirming a purchase or a destructive action like a deletion.See also [Alerts](../tvos/interface-elements/alerts/).
> 알림 템플릿에는 구매 확인 또는 삭제와 같은 파괴적인 작업 수행과 같은 작업을 수행할 수 있는 권한을 요청하는 메시지가 표시됩니다.경고를 참조하십시오.
>




- [Alert template](../foundations/layout#)
- [Catalog template](../foundations/layout#)
- [Compilation template](../foundations/layout#)
- [Descriptive alert template](../foundations/layout#)
- [Form template](../foundations/layout#)
- [List template](../foundations/layout#)
- [Loading template](../foundations/layout#)
- [Menu bar template](../foundations/layout#)
- [Parade template](../foundations/layout#)
- [Product template](../foundations/layout#)
- [Product bundle template](../foundations/layout#)
- [Rating template](../foundations/layout#)
- [Search template](../foundations/layout#)
- [Stack template](../foundations/layout#)

**Customize templates tastefully.** Layout templates are highly customizable; you have control over the background, tinting, size, layout, and more. As you design your app, defer to content whenever possible, avoiding customizations that appear distracting, jarring, or obtrusive.
> 템플리트를 세련되게 사용자 정의합니다. 레이아웃 템플리트는 매우 사용자 정의 가능하며, 배경, 색조, 크기, 레이아웃 등을 제어할 수 있습니다. 앱을 디자인할 때, 가능한 한 콘텐츠를 준수하고, 산만하거나 방해하거나 눈에 거슬리는 사용자 지정을 피하십시오.
>




**Understand a template’s purpose before using it.** If your customizations make the underlying template unrecognizable, consider using a different template or building a custom interface.
> 템플릿을 사용하기 전에 템플릿의 용도를 파악하십시오. 사용자 지정으로 인해 기본 템플릿을 인식할 수 없는 경우 다른 템플릿을 사용하거나 사용자 지정 인터페이스를 구축하는 것을 고려해 보십시오.
>




For detailed information about integrating templates into your app, see [TVML](https://developer.apple.com/documentation/tvml).
> 앱에 템플릿을 통합하는 방법에 대한 자세한 내용은 TVML을 참조하십시오.
>




### **Grids**

The following grid layouts provide an optimal viewing experience. Be sure to use appropriate spacing between unfocused rows and columns to prevent overlap when an item is brought into focus.
> 다음 그리드 레이아웃은 최적의 보기 환경을 제공합니다. 초점이 맞지 않는 행과 열 사이에 적절한 간격을 사용하여 항목이 포커스를 맞출 때 겹치지 않도록 해야 합니다.
>




If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content. For developer guidance, see [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout).
> UIKit 컬렉션 보기 흐름 요소를 사용하는 경우, 그리드의 열 수는 내용의 너비 및 간격에 따라 자동으로 결정됩니다. 개발자 지침은 UI CollectionViewFlowLayout을 참조하십시오.
>




• [Two-column](../foundations/layout#)
• [Three-column](../foundations/layout#)
• [Four-column](../foundations/layout#)
• [Five-column](../foundations/layout#)
• [Six-column](../foundations/layout#)
• [Seven-column](../foundations/layout#)
• [Eight-column](../foundations/layout#)
• [Nine-column](../foundations/layout#)

-

![../foundations/layout/images/visual-design-grid-2-column_2x.png](../foundations/layout/images/visual-design-grid-2-column_2x.png)

### **Two-Column Grid**


**Include additional vertical spacing for titled rows.** If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.
> 제목 있는 행에 대한 추가 세로 간격을 포함합니다. 행에 제목이 있는 경우, 포커스가 없는 이전 행의 아래쪽과 제목 중앙 사이에 충분한 간격을 제공하여 붐비지 않도록 하십시오. 또한 제목의 아래쪽과 행의 포커스가 없는 항목의 위쪽 사이에 간격을 지정합니다.
>




**Use consistent spacing.** When content isn’t consistently spaced, it no longer looks like a grid and it’s harder for people to scan.
> 일정한 간격을 사용합니다. 콘텐츠가 일정한 간격을 유지하지 않으면 더 이상 그리드처럼 보이지 않고 사람들이 검색하기가 더 어렵습니다.
>




**Make partially hidden content look symmetrical.** To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.
> 부분적으로 숨겨진 콘텐츠를 대칭적으로 보이게 합니다. 완전히 보이는 콘텐츠에 주의를 기울이도록 하려면 부분적으로 숨겨진 오프스크린 콘텐츠를 화면의 각 측면에서 동일한 폭으로 유지하십시오.
>




# **watchOS**

**Design your content to extend from one edge of the screen to the other.** The Apple Watch bezel provides a natural visual padding around your content. To avoid wasting valuable space, consider minimizing the padding between elements.
> 화면의 한 가장자리에서 다른 가장자리로 확장되도록 콘텐츠를 디자인하십시오. Apple Watch 베젤은 콘텐츠 주위에 자연스러운 시각적 패딩을 제공합니다. 귀중한 공간을 낭비하지 않으려면 요소 사이의 패딩을 최소화하는 것을 고려하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-full-width-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-full-width-dark_2x.png)

**Avoid placing more than two or three controls side by side in your interface.** As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it’s usually better to let text buttons span the full width of the screen, two side-by-side buttons with short text labels can also work well, as long as the screen doesn’t scroll.
> 인터페이스에 두 개 또는 세 개 이상의 컨트롤을 나란히 배치하지 마십시오. 일반적으로 글리프가 포함된 단추가 세 개 또는 텍스트가 포함된 단추가 두 개 이상 연속으로 표시되지 않도록 합니다. 일반적으로 텍스트 단추가 화면 전체 너비에 걸쳐지도록 하는 것이 더 낫지만 화면이 스크롤되지 않는 한 짧은 텍스트 레이블이 있는 두 개의 나란히 있는 단추도 잘 작동할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-controls-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-controls-dark_2x.png)


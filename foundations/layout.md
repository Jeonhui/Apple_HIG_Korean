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





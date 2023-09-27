# **[foundations] materials**

### On Apple platforms, a material imparts translucency and blurring to a background, creating a sense of visual separation between foreground and background layers.
> 애플 플랫폼에서는 소재가 배경에 투명성과 흐림을 부여해 전경과 배경 레이어 사이에 시각적 분리감을 조성한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-materials-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-materials-intro-dark_2x.png)

Materials can combine with vibrancy to add visual interest to the interface. *Vibrancy* applies to foreground content that displays on top of a material — such as text, symbols, and fills — and works by pulling color forward from behind the material to enhance the sense of depth.
> 재료는 진동과 결합하여 인터페이스에 시각적 관심을 더할 수 있습니다. 진동은 텍스트, 기호 및 채우기 등 재료 위에 표시되는 전경 콘텐츠에 적용되며 재료 뒤에서 색상을 앞으로 당겨서 깊이감을 향상시킵니다.
>




**NOTE**Vibrancy can affect all apps and games — even ones that don’t display any vibrant views — because some components are vibrant by default, such as menus in macOS and labels in iOS.
> 참고 MacOS의 메뉴 및 iOS의 레이블과 같은 일부 구성 요소는 기본적으로 활기가 있기 때문에 Vibrance는 모든 앱과 게임(활기찬 보기를 표시하지 않는 앱도 포함)에 영향을 미칠 수 있습니다.
>




# **Best practices**

The system defines several materials — each intended for a specific usage — that automatically adapt to both light and dark modes. In addition, the system provides several blur and vibrancy effects you can apply to UI components to help them integrate well with materials and achieve the prominence you want. Using system-defined materials and effects can give your app or game a native feel, and create smooth transitions when people switch between apps.
> 이 시스템은 명암 모드에 자동으로 적응하는 여러 가지 재료(각각 특정 용도용)를 정의합니다. 또한 이 시스템은 UI 구성 요소에 적용할 수 있는 여러 가지 흐림 및 진동 효과를 제공하여 재료와 잘 통합되고 원하는 명성을 얻을 수 있도록 도와줍니다. 시스템 정의 재료와 효과를 사용하면 앱이나 게임에 네이티브한 느낌을 줄 수 있으며, 사람들이 앱 사이를 전환할 때 원활한 전환을 할 수 있습니다.
>




**Choose system materials and effects based on semantic meaning and recommended usage.** Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or style to your specific use case. For example, use the [menu](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material/menu) material for a menu in your macOS app, use the [label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) vibrancy style for primary labels in your iOS app, and use the [prominent](https://developer.apple.com/documentation/uikit/uiblureffect/style/prominent) material for adaptable, full-screen backgrounds in your tvOS app.
> 의미론적 의미와 권장 용도에 따라 시스템 재료와 효과를 선택하십시오. 시스템 설정이 인터페이스 모양과 동작을 변경할 수 있으므로 인터페이스에 부여하는 명백한 색상에 따라 재료나 효과를 선택하지 마십시오. 대신 소재나 스타일을 특정 사용 사례에 연결하십시오. 예를 들어, macOS 앱의 메뉴에 대한 메뉴 자료를 사용하고, iOS 앱의 기본 레이블에 대한 레이블 바이브런시 스타일을 사용하며, tvOS 앱에서 적응 가능한 전체 화면 배경에 대한 눈에 띄는 자료를 사용합니다.
>




**Help ensure legibility by using only vibrant colors on top of materials.** When you use system-defined vibrant colors, you don’t need to worry about colors seeming too dark, bright, saturated, or low contrast in different contexts. For example, iOS defines Dynamic System Colors for text, fills, glyphs, and separators, making these items look great on translucent backgrounds. In macOS, all standard system colors have vibrant versions. For guidance, see [Color](../foundations/color).
> 재료 위에 선명한 색상만 사용하여 읽기 쉽게 할 수 있습니다. 시스템 정의 선명한 색상을 사용할 경우 다른 컨텍스트에서 색상이 너무 어둡거나 밝거나 포화 상태이거나 대비가 낮다고 걱정할 필요가 없습니다. 예를 들어, iOS는 텍스트, 채우기, 글리프 및 구분 기호에 대해 동적 시스템 색상을 정의하여 이러한 항목이 반투명한 배경에서 멋지게 보이도록 합니다. macOS에서 모든 표준 시스템 색상은 선명한 버전을 가지고 있다. 자세한 내용은 색상을 참조하십시오.
>




**Consider using SF Symbols instead of full-color icons.** Full-color images may not have sufficient contrast with a view’s background, making them seem out of place when the background is translucent, whereas symbols and interface icons work with dynamic system colors and vibrancy effects to look good in any context. For guidance, see [SF Symbols](../foundations/sf-symbols).
> 풀컬러 아이콘 대신 SF 심볼을 사용하는 것을 고려해 보십시오. 풀컬러 이미지는 뷰의 배경과 충분한 대비를 이루지 못해 배경이 반투명할 때 위치가 맞지 않는 것처럼 보일 수 있습니다. 반면 심볼과 인터페이스 아이콘은 동적 시스템 색상과 활력 효과로 작동하여 모든 상황에서 잘 보입니다. 자세한 내용은 SF 기호를 참조하십시오.
>




**Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.** For example, consider that:
> 블러 및 진동 효과와 결합할 재료를 선택할 때 대비 및 시각적 분리를 고려하십시오. 예를 들어, 다음을 고려하십시오.
>




- Thicker materials can provide better contrast for text and other elements with fine features
- >  소재가 두꺼울수록 텍스트 및 기타 요소의 대비가 더 우수하고 기능이 정교합니다.

- Translucency can help people retain their context by providing a visible reminder of the content that’s in the background
- >  투명성은 배경에 있는 콘텐츠를 시각적으로 상기시켜 사람들이 자신의 컨텍스트를 유지하는 데 도움을 줄 수 있습니다.


The system supplies several materials you can use to convey a sense of depth and hierarchical structure without distracting from content. Ranging from ultra thin to ultra thick, some of the materials adapt to appearance modes and some are always light or always dark. Regardless of the material you choose, you want to avoid using non-vibrant colors on top of it.
> 이 시스템은 콘텐츠에 집중하지 않고 깊이감과 계층 구조를 전달하기 위해 사용할 수 있는 여러 가지 자료를 제공합니다. 초박형에서 초박형까지 다양한 소재 중 일부는 외관 모드에 적응하고 일부는 항상 밝거나 항상 어둡다. 재료에 상관없이 재료 위에 생동감이 없는 색상을 사용하는 것을 피하려고 합니다.
>




For developer guidance, see [UIBlurEffect.Style](https://developer.apple.com/documentation/uikit/uiblureffect/style).

# **Platform considerations**

*Not supported in watchOS.*

# **iOS, iPadOS**

iOS and iPadOS define vibrancy values for labels, fills, and separators that are specifically designed to work with each material; standard system colors aren’t available in vibrant versions.
> iOS와 iPadOS는 각 재료와 함께 작동하도록 특별히 설계된 레이블, 채우기 및 분리기에 대해 진동 값을 정의합니다. 표준 시스템 색상은 활기찬 버전에서는 사용할 수 없습니다.
>




Labels and fills each provide several levels of vibrancy; separators have one level. The names of the levels indicate the relative amount of contrast between an element and the background: the default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.
> 레이블과 채우기는 각각 몇 가지 수준의 활성을 제공하며 구분자는 한 가지 수준을 가집니다. 레벨 이름은 요소와 배경 사이의 상대적인 대비량을 나타냅니다. 기본 레벨은 가장 높은 대비도를 갖는 반면, 4차 레벨(존재하는 경우)은 가장 낮은 대비도를 가집니다.
>




Except for quaternary, you can use the following vibrancy values for labels on any material. It's not recommended to use quaternary on thin and ultra thin materials, because the contrast is too low.
> 4분의 1을 제외하고 모든 재료의 레이블에 다음 진동 값을 사용할 수 있습니다. 얇은 재료와 초박형 재료에는 4차 재료를 사용하지 않는 것이 좋습니다. 대비가 너무 낮기 때문입니다.
>




- [label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) (default)
- [secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
- [tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
- [quaternaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/quaternarylabel)

You can use the following vibrancy values for fills on all materials.
> 모든 재료의 충진에는 다음과 같은 진동 값을 사용할 수 있습니다.
>




- [fill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/fill) (default)
- [secondaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondaryfill)
- [tertiaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiaryfill)

The system provides a single, default vibrancy value for a [separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator), which works well on all materials.
> 이 시스템은 분리기에 대해 단일 기본 진동 값을 제공하므로 모든 재료에서 잘 작동합니다.
>




# **macOS**

macOS provides vibrant versions of all standard colors, and provides materials that define the amounts of translucency, blurring, and vibrancy applied to your interface. The system provides several standard materials, each with a designated purpose. For example, you can choose a material to match the default look of a window, menu, popover, sidebar, title bar, and more. For developer guidance, see [NSVisualEffectView.Material](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material).
> macOS는 모든 표준 색상의 생생한 버전을 제공하며, 인터페이스에 적용되는 투명도, 흐림 및 생동감의 양을 정의하는 자료를 제공합니다. 이 시스템은 각각 지정된 목적을 가진 몇 가지 표준 재료를 제공합니다. 예를 들어 창, 메뉴, 팝업, 사이드바, 제목 표시줄 등의 기본 모양과 일치하는 재료를 선택할 수 있습니다. 개발자 지침은 NSVisualEffectView를 참조하십시오.재료.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-light-appearance_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-light-appearance_2x.png)

Light appearance

![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-dark-appearance_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-dark-appearance_2x.png)

Dark appearance

**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.
> 사용자 지정 보기 및 컨트롤에서 진동 허용 시기를 선택합니다. 구성 및 시스템 설정에 따라 시스템 보기 및 컨트롤은 진동 기능을 사용하여 어떤 배경에서도 전경 콘텐츠를 돋보이게 합니다. 다양한 컨텍스트에서 인터페이스를 테스트하여 활력이 언제 외관을 개선하고 커뮤니케이션을 향상시키는지 확인합니다.
>




**Choose a background blending mode that complements your interface design.** macOS defines two modes that blend background content: behind window and within window. For developer guidance, see [NSVisualEffectBlendingMode](https://developer.apple.com/documentation/appkit/nsvisualeffectblendingmode).
> 당신의 인터페이스 디자인을 보완하는 배경 혼합 모드를 선택하세요. macOS는 배경 콘텐츠를 혼합하는 두 가지 모드를 정의합니다: 창 뒤와 창 안. 개발자 지침은 NSVisualEffectBlending 모드를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-behind-window-blending_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-behind-window-blending_2x.png)

**Behind-window blending.** In this mode, the content behind a window shows through, helping people retain some of the context that surrounds your app or game. Components such as menus, sheets, and sidebars automatically use this mode.
> 백그라운드 윈도우 블렌딩. 이 모드에서는 창 뒤의 콘텐츠가 보여서 사람들이 앱이나 게임을 둘러싼 일부 컨텍스트를 유지할 수 있도록 도와줍니다. 메뉴, 시트 및 사이드바와 같은 구성요소는 자동으로 이 모드를 사용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-in-window-blending_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-in-window-blending_2x.png)

**In-window blending.** This mode lets window content show through other window components. For example, a toolbar can use this mode to give people a sense of continuity as window content scrolls under it.
> 창 내 혼합. 이 모드에서는 창 내용이 다른 창 구성 요소를 통해 표시됩니다. 예를 들어, 도구 모음은 이 모드를 사용하여 창 내용이 그 아래로 스크롤될 때 사람들에게 연속성을 느낄 수 있습니다.
>




# **tvOS**

**Use lighter, translucent materials to elevate content and make it feel fresh.** Darker materials tend to hide shadows, reducing depth and making it harder to distinguish content clearly. You might consider using darker materials if you want to evoke a heavier feeling or suggest that the content is older.
> 더 가볍고 반투명 소재를 사용하여 콘텐츠를 높이고 신선하게 느껴집니다. 소재가 어두우면 그림자가 가려져 깊이가 줄어들고 콘텐츠를 명확하게 구분하기가 어렵습니다. 더 무거운 느낌을 주거나 내용이 더 오래된 것을 제안하려면 어두운 소재를 사용하는 것을 고려할 수 있습니다.
>




For example, consider using system materials in the following ways:
> 예를 들어 다음과 같은 방법으로 시스템 재료를 사용하는 것을 고려해 보십시오.
>




| Material | Recommended for | Adaptive behavior |
| --- | --- | --- |
| Prominent | Full-screen backgrounds | Displays the extra light material in the light appearance and the extra dark material in the dark appearance |
| Regular | Overlay views that partially obscure onscreen content | Displays the light material in the light appearance and the dark material in the dark appearance |
| Extra light | Full-screen views that require a light color scheme | – |
| Light | Overlay views that partially obscure onscreen content and require a light color scheme | – |
| Extra dark | Full-screen views that require a dark color scheme | – |
| Dark | Overlay views that partially obscure onscreen content and require a dark color scheme | – |

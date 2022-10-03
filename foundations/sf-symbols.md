# **[foundations] sf-symbols**

### SF Symbols provides thousands of consistent, highly configurable symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes.
> SF 심볼은 샌프란시스코 시스템 글꼴과 완벽하게 통합되어 모든 무게와 크기의 텍스트와 자동으로 정렬되는 수천 개의 일관되고 구성 가능한 기호를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-sf-symbols-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-sf-symbols-intro-dark_2x.png)

You can use a symbol to convey an object or concept wherever interface icons can appear, such as in navigation bars, toolbars, tab bars, context menus, and within text.
> 기호를 사용하여 탐색 모음, 도구 모음, 탭 모음, 상황에 맞는 메뉴 및 텍스트 내에서 인터페이스 아이콘이 나타날 수 있는 모든 곳에 개체 또는 개념을 전달할 수 있습니다.
>




Availability of individual symbols and features varies based on the version of the system you’re targeting. For example, if you add to your app bundle a symbol introduced in SF Symbols 3, you can use the symbol when your app runs in earlier platforms — such as iOS 13, Mac Catalyst 13, tvOS 13, or watchOS 6 — but without the benefit of SF Symbols 3 features like Hierarchical or Palette color rendering.
> 개별 기호 및 기능의 가용성은 대상 시스템의 버전에 따라 다릅니다. 예를 들어, SF 기호 3에 도입된 기호를 앱 번들에 추가하면 iOS 13, Mac Catalyst 13, tvOS 13 또는 watch와 같은 이전 플랫폼에서 앱이 실행될 때 기호를 사용할 수 있습니다.OS 6 — 그러나 계층적 또는 팔레트 색상 렌더링과 같은 SF 기호 3의 이점은 없습니다.
>




Visit [SF Symbols](https://developer.apple.com/sf-symbols/) to download the app and browse the full set of symbols. Be sure to understand the terms and conditions for using SF Symbols, including the prohibition against using symbols — or images that are confusingly similar — in app icons, logos, or any other trademarked use. For developer guidance, see [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/uiimage/configuring_and_displaying_symbol_images_in_your_ui/).
> 앱을 다운로드하고 전체 기호 집합을 탐색하려면 SF 심볼을 방문하십시오. 앱 아이콘, 로고 또는 기타 상표 사용 시 기호(또는 혼동하기 쉬운 이미지)를 사용하는 것을 금지하는 내용을 포함하여 SF 기호를 사용하는 약관을 이해해야 합니다. 개발자 지침은 UI에서 기호 이미지 구성 및 표시를 참조하십시오.
>




# **Rendering modes**

SF Symbols 3 and later provide four rendering modes — monochrome, hierarchical, palette, and multicolor — that enable multiple options when applying color to symbols. For example, you might want to use multiple opacities of your app’s accent color to give symbols depth and emphasis, or specify a palette of contrasting colors to display symbols that coordinate with various color schemes.
> SF 심볼 3 이상은 심볼에 색상을 적용할 때 여러 옵션을 사용할 수 있는 4가지 렌더링 모드(단색, 계층형, 팔레트 및 멀티컬러)를 제공합니다. 예를 들어 앱의 악센트 색상의 여러 불투명도를 사용하여 심볼의 깊이와 강조를 제공하거나 대비되는 색 팔레트를 지정하여 다양한 색 구성표와 조화를 이루는 기호를 표시할 수 있습니다.
>




To support the rendering modes, SF Symbols organizes a symbol’s paths into distinct layers. For example, the `cloud.sun.rain.fill` symbol consists of three layers: the primary layer contains the cloud paths, the secondary layer contains the paths that define the sun and its rays, and the tertiary layer contains the raindrop paths.
> 렌더링 모드를 지원하기 위해 SF 심볼은 심볼의 경로를 별도의 레이어로 구성합니다. 예를 들어, 'cloud.sun.rain.fill' 기호는 3개의 레이어로 구성됩니다. 1차 레이어는 구름 경로를 포함하고, 2차 레이어는 태양과 그 광선을 정의하는 경로를 포함하고, 3차 레이어는 빗방울 경로를 포함합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-primary-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-primary-dark_2x.png)

Primary

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-secondary-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-secondary-dark_2x.png)

Secondary

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-tertiary-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-tertiary-dark_2x.png)

Tertiary

Depending on the rendering mode you choose, a symbol can produce various appearances. For example, Hierarchical rendering mode assigns a different opacity of a single color to each layer, creating a visual hierarchy that gives depth to the symbol.
> 선택한 렌더링 모드에 따라 기호가 다양한 모양을 만들 수 있습니다. 예를 들어 계층적 렌더링 모드는 각 레이어에 단일 색상의 다른 불투명도를 할당하여 심볼에 깊이를 부여하는 시각적 계층을 만듭니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-color-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-color-dark_2x.png)

To learn more about supporting rendering modes in custom symbols, see [Custom symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols#custom-symbols).
> 사용자 지정 기호에서 렌더링 모드를 지원하는 방법에 대한 자세한 내용은 사용자 지정 기호를 참조하십시오.
>




SF Symbols supports the following rendering modes.
> SF 심볼은 다음과 같은 렌더링 모드를 지원합니다.
>




**Monochrome** — Applies one color to all layers in a symbol. Within a symbol, paths render in the color you specify or as a transparent shape within a color-filled path.
> 단색 - 기호의 모든 레이어에 한 가지 색을 적용합니다. 기호 내에서 경로는 지정한 색으로 렌더링되거나 색상이 채워진 경로 내에서 투명 모양으로 렌더링됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/monochrome-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/monochrome-dark_2x.png)

**Hierarchical** — Applies one color to all layers in a symbol, varying the color’s opacity according to each layer’s hierarchical level.
> 계층적 - 기호의 모든 계층에 한 가지 색을 적용하여 각 계층의 계층적 수준에 따라 색상의 불투명도를 변경합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/hierarchical-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/hierarchical-dark_2x.png)

**Palette** — Applies two or more colors to a symbol, using one color per layer. Specifying only two colors for a symbol that defines three levels of hierarchy means the secondary and tertiary layers use the same color.
> 팔레트 — 레이어당 하나의 색상을 사용하여 둘 이상의 색상을 심볼에 적용합니다. 계층 구조의 세 단계를 정의하는 기호에 대해 두 가지 색상만 지정하면 2차 및 3차 계층이 동일한 색상을 사용함을 의미합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/palette-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/palette-dark_2x.png)

**Multicolor** — Applies intrinsic colors to some symbols to enhance meaning. For example, the `leaf` symbol uses green to reflect the appearance of leaves in the physical world, whereas the `trash.slash` symbol uses red to signal data loss. Some multicolor symbols include layers that can receive other colors.
> 다중 색상 — 의미를 강화하기 위해 일부 기호에 고유 색상을 적용합니다. 예를 들어, 'leaf' 기호는 물리적 세계에서 나뭇잎의 모양을 나타내기 위해 녹색을 사용하는 반면, 'trash.slash' 기호는 데이터 손실을 나타내기 위해 빨간색을 사용한다. 일부 다중 색상 기호는 다른 색상을 수신할 수 있는 레이어를 포함한다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/multicolor-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/multicolor-dark_2x.png)

Regardless of rendering mode, using system-provided colors ensures that symbols automatically adapt to accessibility accommodations and appearance modes like vibrancy and Dark Mode. For developer guidance, see [renderingMode(_:)](https://developer.apple.com/documentation/swiftui/image/renderingmode(_:)).
> 렌더링 모드에 관계없이 시스템에서 제공한 색상을 사용하면 기호가 자동으로 접근성 조절 및 진동 및 다크 모드와 같은 모양 모드에 적응할 수 있습니다. 개발자 지침은 렌더링 모드(_:)를 참조하십시오.
>




**Confirm that a symbol’s rendering mode works well in every context.** Depending on factors like the size of a symbol and its contrast with the current background color, different rendering modes can affect how well people can discern the symbol’s details. In SF Symbols 4 and later, you can use the automatic setting to get a symbol’s preferred rendering mode, but it’s still a good idea to check the results for places where a different rendering mode might improve a symbol’s legibility.
> 심볼의 렌더링 모드가 모든 컨텍스트에서 잘 작동하는지 확인합니다. 심볼의 크기 및 현재 배경색과의 대비와 같은 요인에 따라 다양한 렌더링 모드는 사람들이 심볼의 세부 정보를 얼마나 잘 식별할 수 있는지에 영향을 줄 수 있습니다. SF 심볼 4 이상에서는 자동 설정을 사용하여 심볼의 기본 렌더링 모드를 가져올 수 있지만 다른 렌더링 모드를 사용하면 심볼의 가독성이 향상될 수 있는 위치에 대한 결과를 확인하는 것이 좋습니다.
>




# **Variable color**

With variable color, SF Symbols 4 introduces a way to represent a characteristic that can change over time — like capacity or strength — regardless of rendering mode. To visually communicate such a change, variable color applies color to different layers of a symbol as a value reaches different thresholds between zero and 100 percent.
> 가변 색상으로 SF 심볼 4는 렌더링 모드에 관계없이 용량이나 강도 등 시간이 지남에 따라 변화할 수 있는 특성을 나타낼 수 있는 방법을 도입합니다. 이러한 변화를 시각적으로 전달하기 위해, 값이 0%와 100% 사이의 다른 임계값에 도달하기 때문에 가변 색상은 기호의 다른 레이어에 색상을 적용합니다.
>




For example, you could use variable color with the `speaker.wave.3` symbol to communicate three different ranges of sound — plus the state where there’s no sound — by mapping the layers that represent the curved wave paths to different ranges of decibel values. In the case of no sound, no wave layers get color. In all other cases, a wave layer receives color when the sound reaches a threshold the system defines based on the number of nonzero states you want to represent.
> 예를 들어, 'speaker.wave'에 가변 색상을 사용할 수 있습니다.3' 기호는 곡면파 경로를 나타내는 레이어를 데시벨 값의 다른 범위에 매핑하여 3가지 음역(게다가 소리가 없는 상태)을 전달한다. 소리가 나지 않는 경우, 어떤 파동층도 색을 띠지 않습니다. 다른 모든 경우, 음향이 0이 아닌 상태의 수를 기준으로 시스템이 정의하는 임계값에 도달하면 파동 레이어는 색상을 수신합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/variable-color_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/variable-color_2x.png)

Sometimes, it can make sense for some of a symbol’s layers to opt out of variable color. For example, in the `speaker.wave.3` symbol shown above, the layer that contains the speaker path doesn’t receive variable color because a speaker doesn’t change as the sound level changes. A symbol can support variable color in any number of layers.
> 때때로 기호의 일부 레이어가 가변적인 색상에서 제외되는 것이 타당할 수 있습니다. 예를 들어 'speaker.wave'를 사용합니다.위에 나온 3' 기호는 스피커의 음량이 바뀌어도 스피커가 변하지 않기 때문에 스피커 경로가 포함된 레이어는 가변적인 색상을 받지 못한다. 기호는 임의의 수의 레이어에서 다양한 색상을 지원할 수 있습니다.
>




**Use variable color to communicate change — don’t use it to communicate depth.** To convey depth and visual hierarchy, use Hierarchical rendering mode to elevate certain layers and distinguish foreground and background elements in a symbol.
> 가변 색상을 사용하여 변경 내용을 전달합니다. 깊이 및 시각적 계층 구조를 전달하려면 계층 렌더링 모드를 사용하여 특정 레이어를 올리고 기호에서 전경 및 배경 요소를 구분하십시오.
>




# **Weights and scales**

SF Symbols provides symbols in a wide range of weights and scales to help you create adaptable designs.
> SF 기호는 적응 가능한 설계를 만드는 데 도움이 되는 광범위한 가중치와 척도로 기호를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/scales-weights-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/scales-weights-dark_2x.png)

Each of the nine symbol weights — from ultralight to black — corresponds to a weight of the San Francisco system font, helping you achieve precise weight matching between symbols and adjacent text, while supporting flexibility for different sizes and contexts.
> 초경량에서 검정색에 이르는 9가지 기호 가중치는 각각 샌프란시스코 시스템 글꼴의 가중치에 해당하므로 다양한 크기와 컨텍스트에 대한 유연성을 지원하는 동시에 기호와 인접 텍스트 간에 정확한 가중치를 일치시킬 수 있습니다.
>




Each symbol is also available in three scales: small, medium (the default), and large. The scales are defined relative to the cap height of the San Francisco system font.
> 각 기호는 소형, 중형(기본값) 및 대형의 세 가지 척도로도 사용할 수 있습니다. 축척은 샌프란시스코 시스템 글꼴의 캡 높이에 대해 정의됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/small-medium-large-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/small-medium-large-dark_2x.png)

Specifying a scale lets you adjust a symbol’s emphasis compared to adjacent text, without disrupting the weight matching with text that uses the same point size. For developer guidance, see [imageScale](https://developer.apple.com/documentation/swiftui/view/3280160-imagescale) (SwiftUI), [SymbolScale](https://developer.apple.com/documentation/uikit/uiimage/symbolscale) (UIKit), and [SymbolConfiguration](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration) (AppKit).
> 축척을 지정하면 동일한 점 크기를 사용하는 텍스트와의 가중치 일치를 중단하지 않고 인접 텍스트와 비교하여 기호의 강조를 조정할 수 있습니다. 개발자 지침은 imageScale(Swift)을 참조하십시오.UI, 기호 척도(UIKit) 및 기호 구성(AppKit)입니다.
>




# **Design variants**


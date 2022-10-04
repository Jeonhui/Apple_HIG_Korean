# **[foundations] Typography**

### In addition to ensuring legible text, your typographic choices can help you clarify an information hierarchy, communicate important content, and express your brand.
> 읽기 쉬운 텍스트를 보장하는 것 외에도, 타이포그래피 선택은 정보 계층을 명확히 하고, 중요한 내용을 전달하며, 브랜드를 표현하는 데 도움이 될 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-typography-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-typography-intro-dark_2x.png)

# **Best practices**

**Strive to maintain a minimum font size that most people can read easily.** Differences in device displays, including pixel density and brightness, can influence the appropriate minimum font size. Other factors — such as the reader’s proximity to the display, their eyesight and whether they’re in motion, and environmental lighting conditions — all impact legibility. When you support Dynamic Type — a feature that lets people choose the size of onscreen text in iOS, iPadOS, tvOS, and watchOS — your app or game can respond appropriately when people adjust text to a size that works for them. For developer guidance, see [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output); for available sizes, see [Specifications](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#specifications).
> 대부분의 사람들이 쉽게 읽을 수 있는 최소 글꼴 크기를 유지하도록 노력한다. 픽셀 밀도와 밝기를 포함한 기기 디스플레이의 차이는 적절한 최소 글꼴 크기에 영향을 미칠 수 있다. 독자가 디스플레이에 근접한 위치, 시력, 동작 여부, 환경 조명 조건과 같은 다른 요소들은 모두 가독성에 영향을 미칩니다. 동적 유형을 지원하는 경우 - iOS, iPadOS, tvOS 및 시청에서 화면 텍스트 크기를 선택할 수 있는 기능OS — 사용자가 자신에게 맞는 크기로 텍스트를 조정할 때 앱이나 게임이 적절하게 응답할 수 있습니다. 개발자 지침은 텍스트 입력 및 출력을 참조하고, 사용 가능한 크기는 사양을 참조하십시오.
>




**Adjust font weight, size, and color as needed to emphasize important information and help people visualize hierarchy.** Be sure to maintain the relative hierarchy and visual distinction of text elements when people adjust text sizes.
> 중요한 정보를 강조하고 계층 구조를 시각화하는 데 도움이 되도록 필요에 따라 글꼴 무게, 크기 및 색상을 조정합니다. 사용자가 텍스트 크기를 조정할 때 텍스트 요소의 상대적 계층 및 시각적 구별을 유지해야 합니다.
>




**Minimize the number of typefaces you use in your interface.** Mixing too many different typefaces can obscure your information hierarchy and hinder readability.
> 인터페이스에서 사용하는 서체의 수를 최소화하십시오. 너무 많은 서체를 혼합하면 정보 계층이 흐려지고 가독성이 저하될 수 있습니다.
>




**Test legibility in different contexts.** For example, in addition to adjusting text size, people may view your content outside in bright sunlight, glance at it while they’re in motion, or view it from a distance. If testing shows that some of your text is difficult to read, consider modifying the text or background colors to increase contrast, using a larger type size, or using typefaces designed for optimized legibility, like the system fonts.
> 예를 들어, 텍스트 크기를 조정하는 것 외에도, 사람들은 밝은 햇빛 아래 밖에서 콘텐츠를 보거나, 이동 중에 콘텐츠를 힐끗 보거나, 멀리서 콘텐츠를 볼 수 있습니다. 테스트 결과 일부 텍스트를 읽기 어려운 경우 대비를 증가시키기 위해 텍스트 또는 배경색을 수정하거나, 더 큰 활자 크기를 사용하거나, 시스템 글꼴과 같이 최적화된 가독성을 위해 설계된 서체를 사용하는 것이 좋습니다.
>




**In general, avoid light font weights to help maintain readability.** For example, if you’re using system-provided fonts, use Regular, Medium, Semibold, or Bold font weights, and avoid Ultralight, Thin, and Light font weights, which can be difficult to see, especially when text is small.
> 일반적으로 시스템에서 제공하는 글꼴을 사용하는 경우 일반, 중간, 세미볼드 또는 볼드 글꼴을 사용하고 특히 텍스트가 작을 경우 보기 어려운 초경량, 얇은 두께 및 가벼운 글꼴을 사용하지 않도록 합니다.
>




**Prioritize important content when responding to text-size changes.** Not all content is equally important. When someone chooses a larger text size, they typically want to make the content they care about easier to read; they don’t always want to increase the size of every word on the screen. For example, when people choose a large accessibility text size, Mail displays the subject and body of the message in the large size, but leaves less important text — such as the date and the sender — in a smaller size.
> 텍스트 크기 변경에 응답할 때 중요한 내용의 우선순위를 지정합니다. 모든 내용이 동일하게 중요한 것은 아닙니다. 더 큰 텍스트 크기를 선택할 경우 일반적으로 관심 있는 내용을 읽기 쉽게 만들고자 하지만 화면에 표시되는 모든 단어의 크기를 늘리기 원하는 것은 아닙니다. 예를 들어, 접근성 텍스트 크기를 크게 선택할 때, 메일은 메시지의 제목과 본문을 큰 크기로 표시하지만 날짜 및 발신인과 같은 중요도가 낮은 텍스트는 작은 크기로 남겨둡니다.
>




# **Using system fonts**

Apple provides two typeface families that support an extensive range of weights, sizes, styles, and languages.
> Apple은 광범위한 가중치, 크기, 스타일 및 언어를 지원하는 두 개의 글꼴 패밀리를 제공합니다.
>




**San Francisco (SF)** is a sans serif typeface family that includes the SF Pro, SF Compact, SF Arabic, and SF Mono variants.
> 샌프란시스코(San Francisco)는 SF Pro, SF Compact, SF 아랍어 및 SF Mono 변형을 포함하는 산세리프 서체 계열이다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/sf-pro-text-regular_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/sf-pro-text-regular_2x.png)

The system also offers the SF Pro Rounded, SF Arabic Rounded, and SF Compact Rounded variants you can use to coordinate text with the appearance of soft or rounded UI elements, or to provide an alternative typographic voice.
> 또한 이 시스템은 소프트 또는 둥근 UI 요소의 모양과 텍스트를 조정하거나 대체 타이포그래피 음성을 제공하는 데 사용할 수 있는 SF Pro Rounded, SF Arabic Rounded 및 SF Compact Rounded 변형을 제공합니다.
>




**New York (NY)** is a serif typeface family designed to work well by itself and alongside the SF fonts.
> 뉴욕(NY)은 SF 글꼴과 함께 스스로 잘 작동하도록 설계된 세리프 글꼴 계열이다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/new-york_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/new-york_2x.png)

You can download the San Francisco and New York fonts [here](https://developer.apple.com/fonts/).
> 여기서 샌프란시스코와 뉴욕 글꼴을 다운로드할 수 있습니다.
>




The system provides the SF and NY fonts in the *variable* font format, which combines different font styles together in one file, and supports interpolation between styles to create intermediate ones.
> 이 시스템은 SF와 NY 글꼴을 가변 글꼴 형식으로 제공하여 서로 다른 글꼴 스타일을 하나의 파일로 결합하고 스타일 간 보간을 지원하여 중간 글꼴을 만듭니다.
>




**NOTE**Variable fonts enable *optical sizing*, which refers to the adjustment of different typographic designs to fit different sizes. On all platforms, the system fonts support *dynamic optical sizes*, which merge discrete optical sizes (like Text and Display) and weights into a single, continuous design, letting the system interpolate each glyph or letterform to produce a structure that’s precisely adapted to the point size. With dynamic optical sizes, you don’t need to use discrete optical sizes unless you’re working with a design tool that doesn’t support all the features of the variable font format.
> 참고 Variable 글꼴을 사용하면 광학 크기를 조정할 수 있습니다. 즉, 다양한 타이포그래피 디자인을 다양한 크기에 맞게 조정할 수 있습니다. 모든 플랫폼에서 시스템 글꼴은 동적 광학 크기를 지원하며, 텍스트 및 디스플레이와 같은 개별 광학 크기와 가중치를 단일 연속 설계로 병합하여 시스템이 각 글리프 또는 문자 형식을 보간하여 점 크기에 정확히 맞는 구조를 생성할 수 있도록 합니다. 동적 광학 크기를 사용하는 경우 가변 글꼴 형식의 모든 기능을 지원하지 않는 설계 도구를 사용하는 경우가 아니라면 별도의 광학 크기를 사용할 필요가 없습니다.
>




To help you define visual hierarchies and create clear and legible designs in many different sizes and contexts, the system fonts are available in a variety of weights, ranging from Ultralight to Black, and — in the case of SF — several widths, including Condensed and Expanded. Because SF Symbols use equivalent weights, you can achieve precise weight matching between symbols and adjacent text, regardless of the size or style you choose.
> 시각적인 계층을 정의하고 다양한 크기와 컨텍스트에서 선명하고 읽기 쉬운 디자인을 만드는 데 도움이 되도록 시스템 글꼴은 Ultralight에서 Black에 이르는 다양한 가중치와 SF의 경우 Congred 및 Expanded를 포함한 여러 너비로 사용할 수 있습니다. SF 기호는 동일한 가중치를 사용하기 때문에 선택한 크기나 스타일에 관계없이 기호와 인접 텍스트 간에 정확한 가중치를 일치시킬 수 있습니다.
>




**NOTE**[SF Symbols](../foundations/sf-symbols) provides a comprehensive library of symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes. Consider using symbols when you need to convey a concept or depict an object, especially within text.
> NOTESF 심볼은 샌프란시스코 시스템 글꼴과 완벽하게 통합되어 모든 무게와 크기의 텍스트와 자동으로 정렬되는 포괄적인 기호 라이브러리를 제공합니다. 특히 텍스트 내에서 개념을 전달하거나 개체를 묘사해야 할 때 기호를 사용하는 것을 고려하십시오.
>





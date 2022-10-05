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




The system defines a set of typographic attributes — called text styles — that work with both typeface families. A *text style* specifies a combination of font weight, point size, and leading values for each text size. For example, the *body* text style uses values that support a comfortable reading experience over multiple lines of text, while the *headline* style assigns a font size and weight that help distinguish a heading from surrounding content. Taken together, the text styles form a typographic hierarchy you can use to express the different levels of importance in your content. Text styles also allow text to scale proportionately when people change the system’s text size or make accessibility adjustments, like turning on Larger Text in Accessibility settings.
> 시스템은 두 서체 패밀리와 함께 작동하는 일련의 타이포그래피 속성(텍스트 스타일)을 정의합니다. 텍스트 스타일은 각 텍스트 크기에 대한 글꼴 무게, 점 크기 및 선행 값의 조합을 지정합니다. 예를 들어 본문 텍스트 스타일은 여러 줄의 텍스트에 걸쳐 편안한 읽기 경험을 지원하는 값을 사용하는 반면, 헤드라인 스타일은 제목과 주변 내용을 구별하는 데 도움이 되는 글꼴 크기와 무게를 할당합니다. 텍스트 스타일은 내용에서 서로 다른 수준의 중요도를 표현하는 데 사용할 수 있는 타이포그래피 계층을 형성합니다. 또한 텍스트 스타일을 사용하면 사용자가 시스템 텍스트 크기를 변경하거나 내게 필요한 옵션 설정에서 큰 텍스트 설정처럼 내게 필요한 옵션을 조정할 때 텍스트 크기를 비례적으로 조정할 수 있습니다.
>




**Consider using the built-in text styles.** The system-defined text styles give you a convenient and consistent way to convey your information hierarchy through font size and weight. Using text styles with the system fonts also supports Dynamic Type and the larger accessibility type sizes (where available), which let people choose the text size that works for them.
> 기본 제공 텍스트 스타일을 사용해 보십시오. 시스템 정의 텍스트 스타일을 사용하면 글꼴 크기와 무게를 통해 정보 계층을 쉽고 일관성 있게 전달할 수 있습니다. 또한 시스템 글꼴에 텍스트 스타일을 사용하면 동적 유형과 더 큰 내게 필요한 유형 크기(사용 가능한 경우)를 지원하므로 사용자가 자신에게 맞는 텍스트 크기를 선택할 수 있습니다.
>




**Modify the built-in text styles if necessary.** System APIs define font adjustments — called *symbolic traits* — that let you modify some aspects of a text style. For example, the bold trait adds weight to text, letting you create another level of hierarchy. You can also use symbolic traits to adjust leading if you need to improve readability or conserve space. For example, when you display text in wide columns or long passages, more space between lines (*loose leading*) can make it easier for people to keep their place while moving from one line to the next. Conversely, if you need to display multiple lines of text in an area where height is constrained — for example, in a list row — decreasing the space between lines (*tight leading*) can help the text fit well. If you need to display three or more lines of text, avoid tight leading even in areas where height is limited. For developer guidance, see [leading(_:)](https://developer.apple.com/documentation/swiftui/font/leading(_:)).
> 필요한 경우 기본 제공 텍스트 스타일을 수정합니다. 시스템 API는 텍스트 스타일의 일부 측면을 수정할 수 있는 기호 특성이라고 하는 글꼴 조정을 정의합니다. 예를 들어, 굵은 글씨 특성은 텍스트에 가중치를 부여하여 다른 수준의 계층을 작성할 수 있습니다. 또한 가독성을 개선하거나 공간을 절약해야 하는 경우 기호 특성을 사용하여 선행 기능을 조정할 수 있습니다. 예를 들어, 텍스트를 넓은 열이나 긴 구절로 표시할 때, 줄 사이의 공백이 많을수록(느슨하게 선행됨) 한 줄에서 다음 줄로 이동하는 동안 사용자가 자신의 위치를 더 쉽게 유지할 수 있습니다. 반대로 높이가 제한된 영역(예: 목록 행)에서 여러 줄의 텍스트를 표시해야 하는 경우 줄 사이의 공간을 줄이면 텍스트가 잘 맞을 수 있습니다. 세 줄 이상의 텍스트를 표시해야 하는 경우 높이가 제한된 영역에서도 선두를 좁히지 않도록 하십시오. 개발자 지침은 선행(_:)을 참조하십시오.
>




**Adjust tracking as needed in interface mockups.** In a running app, the system font dynamically adjusts tracking at every point size. To produce an accurate interface mockup of an interface that uses the variable system fonts, you don’t have to choose a discrete optical size at certain point sizes, but you might need to adjust the tracking. For guidance, see [Specifications](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#specifications).
> 인터페이스 목업의 필요에 따라 추적을 조정합니다. 실행 중인 앱에서 시스템 글꼴은 모든 포인트 크기의 추적을 동적으로 조정합니다. 가변 시스템 글꼴을 사용하는 인터페이스의 정확한 인터페이스 목업을 생성하기 위해 특정 지점 크기로 개별 광학 크기를 선택할 필요는 없지만 추적을 조정해야 할 수도 있습니다. 자세한 내용은 사양을 참조하십시오.
>




**DEVELOPER NOTE**You can use the constants defined in [Font.Design](https://developer.apple.com/documentation/swiftui/font/design) to access all system fonts — don’t embed system fonts in your app or game. For example, use [default](https://developer.apple.com/documentation/swiftui/font/design/default) to get the system font on all platforms; use [serif](https://developer.apple.com/documentation/swiftui/font/design/serif) to get the New York font.
> 개발자 참고 글꼴에 정의된 상수를 사용할 수 있습니다.모든 시스템 글꼴에 액세스하도록 설계 - 앱이나 게임에 시스템 글꼴을 내장하지 마십시오. 예를 들어 모든 플랫폼에서 시스템 글꼴을 가져오려면 default를 사용하고 뉴욕 글꼴을 가져오려면 serif를 사용합니다.
>




# **Using custom fonts**

**Make sure custom fonts are legible.** Unless your app has a compelling need for a custom font — such as for branding purposes or to create an immersive gaming experience — prefer the system fonts. If you do use a custom font, make sure people can read it easily at various viewing distances and under a variety of conditions.
> 사용자 정의 글꼴이 읽기 쉽도록 하십시오. 브랜딩 목적이나 몰입형 게임 환경을 만드는 것과 같은 사용자 정의 글꼴에 대한 강력한 요구가 앱에 없는 한 시스템 글꼴을 선호합니다. 사용자 지정 글꼴을 사용하는 경우 다양한 보기 거리에서 다양한 조건에서 쉽게 읽을 수 있는지 확인합니다.
>




**Implement accessibility features for custom fonts.** System fonts automatically support Dynamic Type (where available) and respond when people turn on accessibility features, such as Bold Text. If you use a custom font, make sure it implements the same behaviors. For developer guidance, see [Applying custom fonts to text](https://developer.apple.com/documentation/swiftui/applying-custom-fonts-to-text).
> 사용자 지정 글꼴에 대한 내게 필요한 옵션 기능을 구현합니다. 시스템 글꼴은 동적 유형(사용 가능한 경우)을 자동으로 지원하며 굵은 텍스트와 같은 내게 필요한 옵션 기능을 설정하면 응답합니다. 사용자 정의 글꼴을 사용하는 경우 동일한 동작을 구현해야 합니다. 개발자 지침은 텍스트에 사용자 지정 글꼴 적용을 참조하십시오.
>




# **Platform considerations**

# **iOS, iPadOS**

SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.
> SF Pro는 iOS와 iPadOS의 시스템 글꼴이며 iOS와 iPadOS 앱도 NY를 사용할 수 있습니다.
>




# **macOS**

SF Pro is the system font in macOS. NY is available for Mac apps built with Mac Catalyst. macOS doesn’t support Dynamic Type.
> SF Pro는 macOS의 시스템 글꼴이다. NY는 Mac Catalyst로 구축된 Mac 앱에서 사용할 수 있습니다. macOS는 Dynamic Type을 지원하지 않습니다.
>




**When necessary, use dynamic system font variants to match the text in standard controls.** Dynamic system font variants give your text the same look and feel of the text that appears in system-provided controls. Use the variants listed below to achieve a look that’s consistent with other apps on the platform.
> 필요한 경우 동적 시스템 글꼴 변형을 사용하여 표준 컨트롤의 텍스트를 일치시킵니다. 동적 시스템 글꼴 변형을 사용하면 시스템에서 제공하는 컨트롤에 나타나는 텍스트와 동일한 모양과 느낌을 텍스트에 제공합니다. 아래 나열된 변형을 사용하여 플랫폼의 다른 앱과 일치하는 외관을 만드십시오.
>




# **tvOS**

SF Pro is the system font in tvOS, and apps can also use NY.
> SF Pro는 tvOS의 시스템 글꼴이며, 앱도 NY를 사용할 수 있다.
>




# **watchOS**

SF Compact is the system font in watchOS, and apps can also use NY. In complications, watchOS uses SF Compact Rounded.
> SF Compact는 워치OS의 시스템 글꼴이며, 앱도 NY를 사용할 수 있다. 복잡할 때, 보세요.OS는 SF Compact Rounded를 사용합니다.
>




# **Specifications**

# **iOS, iPadOS**

### **Dynamic Type sizes (iOS)**

• [xSmall](../foundations/typography#)
• [Small](../foundations/typography#)
• [Medium](../foundations/typography#)
• [Large (Default)](../foundations/typography#)
• [xLarge](../foundations/typography#)
• [xxLarge](../foundations/typography#)
• [xxxLarge](../foundations/typography#)

- **Large (Default)**

Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
> @2x의 경우 144ppi, @3x 디자인의 경우 216ppi의 이미지 해상도를 기반으로 한 포인트 크기입니다.
>





### **Larger accessibility type sizes (iOS)**
> 더 큰 접근성 유형 크기(iOS)
>




• [AX1](../foundations/typography#)
• [AX2](../foundations/typography#)
• [AX3](../foundations/typography#)
• [AX4](../foundations/typography#)
• [AX5](../foundations/typography#)

- **AX1**

Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
> @2x의 경우 144ppi, @3x 디자인의 경우 216ppi의 이미지 해상도를 기반으로 한 포인트 크기입니다.
>





### **Tracking values (iOS)**

• [SF Pro](../foundations/typography#)
• [SF Pro Rounded](../foundations/typography#)
• [New York](../foundations/typography#)

- **SF Pro**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
> 일부 앱은 추적 값을 1/1000em으로 표현하지 않습니다. @2x의 경우 144ppi, @3x 디자인의 경우 216ppi의 이미지 해상도를 기반으로 한 포인트 크기입니다.
>





# **macOS**

### **Built-in text styles**

Point size based on image resolution of 144ppi for @2x designs.
> @2x 설계의 경우 이미지 해상도 144ppi를 기반으로 한 포인트 크기입니다.
>




### **Tracking values (macOS)**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
> 일부 앱은 추적 값을 1/1000em으로 표현하지 않습니다. @2x의 경우 144ppi, @3x 디자인의 경우 216ppi의 이미지 해상도를 기반으로 한 포인트 크기입니다.
>




# **tvOS**

### **Dynamic Type sizes (tvOS)**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 72ppi for @1x and 144ppi for @2x designs.
> 일부 앱은 추적 값을 1/1000em으로 표현하지 않습니다. @1x 설계의 경우 72ppi, @2x 설계의 경우 144ppi의 이미지 해상도를 기반으로 한 포인트 크기입니다.
>




### **Tracking values (tvOS)**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
> 일부 앱은 추적 값을 1/1000em으로 표현하지 않습니다. @2x의 경우 144ppi, @3x 디자인의 경우 216ppi의 이미지 해상도를 기반으로 한 포인트 크기입니다.
>




# **watchOS**

### **Dynamic Type sizes (watchOS)**

• [xSmall](../foundations/typography#)
• [Small](../foundations/typography#)
• [Large](../foundations/typography#)
• [xLarge](../foundations/typography#)
• [xxLarge](../foundations/typography#)
• [xxxLarge](../foundations/typography#)

- **Large (default 40mm/41mm/42mm)**

### **Larger accessibility type sizes (watchOS)**
> 접근성 유형 크기 확대(시계)OS)
>




• [AX1](../foundations/typography#)
• [AX2](../foundations/typography#)
• [AX3](../foundations/typography#)

- **AX1**

### **Tracking values (watchOS)**

• [SF Compact](../foundations/typography#)
• [SF Compact Rounded](../foundations/typography#)

- **SF Compact**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x designs.
> 일부 앱은 추적 값을 1/1000em으로 표현하지 않습니다. @2x 설계의 경우 이미지 해상도 144ppi를 기반으로 한 포인트 크기입니다.
>





| Dynamic font variant | API |
| --- | --- |
| Control content | controlContentFontOfSize |
| Label | labelFontOfSize |
| Menu | menuFontOfSize |
| Menu bar | menuBarFontOfSize |
| Message | messageFontOfSize |
| Palette | paletteFontOfSize |
| Title | titleBarFontOfSize |
| Tool tips | toolTipsFontOfSize |
| Document text (user) | userFontOfSize |
| Monospaced document text (user fixed pitch) | userFixedPitchFontOfSize |
| Bold system font | boldSystemFontOfSize |
| System font | systemFontOfSize |

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Subheadline | Regular | 11 | 14 | Semibold |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

| Size (points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

| Style (standard) | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Title 1 | Medium | 76 | 96 |
| Title 2 | Medium | 57 | 66 |
| Title 3 | Medium | 48 | 56 |
| Headline | Medium | 38 | 46 |
| Subtitle 1 | Regular | 38 | 46 |
| Callout | Medium | 31 | 38 |
| Body | Medium | 29 | 36 |
| Caption 1 | Regular | 25 | 32 |
| Caption 2 | Medium | 23 | 30 |

| Style (emphasized) | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Title 1 | Bold | 76 | 96 | +11 |
| Title 2 | Bold | 57 | 66 | +13 |
| Title 3 | Bold | 48 | 56 | +15 |
| Headline | Bold | 38 | 46 | -26 |
| Subtitle 1 | Medium | 38 | 46 | -26 |
| Callout | Bold | 31 | 38 | -16 |
| Body | Bold | 29 | 36 | -13 |
| Caption 1 | Medium | 25 | 32 | -3 |
| Caption 2 | Bold | 23 | 30 | +3 |

| Size (points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

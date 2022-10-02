# **[foundations] right-to-left**

### Support right-to-left languages like Arabic and Hebrew by reversing your interface as needed to match the reading direction of the related scripts.
> 관련 스크립트의 읽기 방향에 맞게 필요에 따라 인터페이스를 반대로 하여 아랍어 및 히브리어와 같은 오른쪽에서 왼쪽 언어를 지원합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-rtl-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-rtl-intro-dark_2x.png)

When people choose a language for their device — or just your app or game — they expect the interface to adapt in various ways (to learn more, see [Localization](https://developer.apple.com/localization/)).
> 사용자가 자신의 장치 또는 앱이나 게임에 사용할 언어를 선택할 때, 사용자는 인터페이스가 다양한 방식으로 적응할 것으로 기대합니다(자세한 내용은 현지화 참조).
>




System-provided UI frameworks support right-to-left (RTL) by default, enabling system-provided UI components to flip automatically in the RTL context. If you use system-provided elements and standard layouts, you might not need to make any changes to your app’s automatically reversed interface.
> 시스템에서 제공하는 UI 프레임워크는 기본적으로 오른쪽에서 왼쪽으로(RTL)를 지원하므로 시스템에서 제공하는 UI 구성 요소가 RTL 컨텍스트에서 자동으로 플립할 수 있습니다. 시스템 제공 요소 및 표준 레이아웃을 사용하는 경우 앱의 자동 역방향 인터페이스를 변경할 필요가 없을 수 있습니다.
>




If you want to fine-tune your layout or enhance specific localizations to adapt to different currencies, numerals, or mathematical symbols that can occur in various locales in countries that use RTL languages, follow these guidelines.
> 레이아웃을 미세 조정하거나 특정 지역화를 강화하여 RTL 언어를 사용하는 국가의 다양한 지역에서 발생할 수 있는 다양한 통화, 숫자 또는 수학적 기호에 적응하려면 다음 지침을 따르십시오.
>




# **Text alignment**

**Adjust text alignment to match the interface direction, if the system doesn’t do so automatically.** For example, if you left-align text with content in the left-to-right (LTR) context, right-align the text to match the content’s mirrored position in the RTL context.
> 텍스트 정렬은 시스템이 자동으로 조정하지 않는 경우 인터페이스 방향과 일치하도록 조정합니다. 예를 들어, 텍스트를 왼쪽에서 오른쪽으로(LTR) 컨텍스트의 콘텐츠와 왼쪽에서 오른쪽으로 정렬하는 경우 RTL 컨텍스트에서 콘텐츠의 미러링된 위치와 일치하도록 텍스트를 오른쪽 정렬합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-ltr-screen-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-ltr-screen-dark_2x.png)

Left-aligned text in the LTR context
> LTR 컨텍스트의 왼쪽 정렬 텍스트
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-rtl-screen-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-rtl-screen-dark_2x.png)

Right-aligned content in the RTL context
> RTL 컨텍스트에서 올바르게 정렬된 콘텐츠
>




**Align a paragraph based on its language, not on the current context.** When the alignment of a paragraph — defined as three or more lines of text — doesn’t match its language, it can be difficult to read. For example, right-aligning a paragraph that consists of LTR text can make the beginning of each line difficult to see. To improve readability, continue aligning one- and two-line text blocks to match the reading direction of the current context, but align a paragraph to match its language.
> 현재 컨텍스트가 아닌 언어에 따라 문단을 정렬합니다. 세 줄 이상의 텍스트로 정의된 문단의 정렬이 언어와 일치하지 않으면 읽기 어려울 수 있습니다. 예를 들어, LTR 텍스트로 구성된 단락을 오른쪽 정렬하면 각 줄의 시작 부분을 보기가 어려울 수 있습니다. 가독성을 향상시키려면 한 줄 및 두 줄 텍스트 블록을 현재 컨텍스트의 읽기 방향과 일치하도록 계속 정렬하되 문단을 해당 언어와 일치시키십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-correct-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-correct-dark_2x.png)

A left-aligned paragraph in the RTL context
> RTL 문맥의 왼쪽 정렬 단락
>




![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-wrong-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-wrong-dark_2x.png)

A right-aligned paragraph in the RTL context
> RTL 맥락에서 오른쪽 정렬된 단락
>




![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Use a consistent alignment for all text items in a list.** To ensure a comfortable reading and scanning experience, reverse the alignment of all items in a list, including items that are displayed in a different script.
> 목록의 모든 텍스트 항목에 대해 일관된 정렬을 사용합니다. 편안한 읽기 및 스캔 환경을 보장하려면 다른 스크립트에 표시되는 항목을 포함하여 목록의 모든 항목의 정렬을 반대로 수행하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-correct_2x.png)

Right-aligned content in the RTL context
> RTL 컨텍스트에서 올바르게 정렬된 콘텐츠
>




![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-wrong_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-wrong_2x.png)

Mixed alignment in the RTL content
> RTL 컨텐츠의 혼합 정렬
>




![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

# **Numbers and characters**

Different RTL languages can use different number systems. For example, Hebrew text uses Western Arabic numerals, whereas Arabic text might use either Western or Eastern Arabic numerals. The use of Western and Eastern Arabic numerals varies among countries and regions and even among areas within the same country or region.
> RTL 언어마다 다른 숫자 체계를 사용할 수 있다. 예를 들어, 히브리어 텍스트는 서아라비아 숫자를 사용하는 반면, 아랍어 텍스트는 서아라비아 숫자 또는 동아라비아 숫자를 사용할 수 있다. 서아라비아 숫자와 동아라비아 숫자의 사용은 국가와 지역에 따라, 심지어 같은 나라나 지역에 있는 지역들 사이에서도 다르다.
>




If your app focuses on mathematical concepts or other number-centric topics, it’s a good idea to identify the appropriate way to display such information in each locale you support. In contrast, apps that don’t focus on number-related topics can generally rely on system-provided number representations.
> 앱이 수학적 개념이나 다른 숫자 중심 주제에 초점을 맞춘다면 지원하는 각 로케일에서 이러한 정보를 표시하는 적절한 방법을 식별하는 것이 좋습니다. 대조적으로, 숫자 관련 주제에 초점을 맞추지 않는 앱은 일반적으로 시스템이 제공하는 숫자 표현에 의존할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123_2x.png)

Western Arabic numerals

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123-ar_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123-ar_2x.png)

Eastern Arabic numerals

**Don’t reverse the order of numerals in a specific number.** Regardless of the current language or the surrounding content, the digits in a specific number — such as “541,” a phone number, or a credit card number — always appear in the same order.
> 특정 번호의 숫자 순서를 거꾸로 하지 마십시오. 현재 언어 또는 주변 내용에 관계없이 특정 번호의 숫자(예: "541", 전화 번호 또는 신용카드 번호)는 항상 같은 순서로 표시됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/latin-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/latin-numerals-dark_2x.png)

Latin

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/hebrew-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/hebrew-numerals-dark_2x.png)

Hebrew

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/western-arabic-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/western-arabic-numerals-dark_2x.png)

Arabic (Western Arabic numerals)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/eastern-arabic-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/eastern-arabic-numerals-dark_2x.png)

Arabic (Eastern Arabic numerals)

**Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves.** Controls like progress bars, sliders, and rating controls often include numerals to clarify their meaning. If you use numerals in this way, be sure to reverse the order of the numerals to match the direction of the flipped control. Also reverse a sequence of numerals if you use the sequence to communicate a specific order.
> 진행률 또는 계수 방향을 나타내는 숫자의 순서를 뒤집습니다. 숫자 자체를 뒤집지 마십시오. 진행률 표시줄, 슬라이더 및 등급 제어와 같은 컨트롤에는 의미를 명확히 하기 위해 숫자가 포함되는 경우가 많습니다. 이러한 방식으로 숫자를 사용할 경우 뒤집힌 컨트롤의 방향과 일치하도록 숫자 순서를 거꾸로 해야 합니다. 또한 순서를 사용하여 특정 순서를 전달할 경우 숫자 순서를 반대로 사용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-latin-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-latin-dark_2x.png)

Latin

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-eastern-arabic-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-eastern-arabic-dark_2x.png)

Arabic (Eastern Arabic numerals)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-hebrew-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-hebrew-dark_2x.png)

Hebrew

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-western-arabic-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-western-arabic-dark_2x.png)

Arabic (Western Arabic numerals)

# **Controls**

**Flip controls that show progress from one value to another.** Because people tend to view forward progress as moving in the same direction as the language they read, it makes sense to flip controls like sliders and progress indicators in the RTL context. When you do this, also be sure to reverse the positions of the accompanying glyphs or images that depict the beginning and ending values of the control.
> 한 값에서 다른 값으로 진행 상황을 보여주는 플립 컨트롤. 사람들은 앞으로 진행 상황을 읽은 언어와 같은 방향으로 이동하는 것으로 보는 경향이 있기 때문에 슬라이더 및 RTL 컨텍스트에서 진행률 표시기와 같은 컨트롤을 플립하는 것이 이치에 맞습니다. 이 작업을 수행할 때는 컨트롤의 시작 및 끝 값을 나타내는 함께 제공된 글리프 또는 이미지의 위치를 반대로 표시해야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-ltr_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-ltr_2x.png)

Directional controls in the LTR context
> LTR 컨텍스트에서 방향 컨트롤
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-rtl_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-rtl_2x.png)

Directional controls in the RTL context
> RTL 상황에서의 방향 제어
>




**Flip controls that help people navigate or access items in a fixed order.** For example, in the RTL context, a back button must point to the right so the flow of screens matches the reading order of the RTL language. Similarly, next or previous buttons that let people access items in an ordered list need to flip in the RTL context to match the reading order.
> 고정된 순서로 항목을 탐색하거나 액세스하는 데 도움이 되는 플립 컨트롤. 예를 들어, RTL 컨텍스트에서는 화면 흐름이 RTL 언어의 읽기 순서와 일치하도록 뒤로 단추가 오른쪽을 가리켜야 합니다. 마찬가지로, 순서 목록의 항목에 액세스할 수 있는 다음 또는 이전 버튼은 읽기 순서와 일치하도록 RTL 컨텍스트를 플립해야 합니다.
>




**Preserve the direction of a control that refers to an actual direction or points to an onscreen area.** For example, if you provide a control that means “to the right,” it must always point right, regardless of the current context.
> 실제 방향을 참조하거나 화면 영역을 가리키는 컨트롤의 방향을 유지합니다. 예를 들어 "오른쪽"을 의미하는 컨트롤을 제공하는 경우 현재 컨텍스트에 관계없이 항상 오른쪽을 가리켜야 합니다.
>




**Visually balance adjacent Latin and RTL scripts when necessary.** In buttons, labels, and titles, Arabic or Hebrew text can appear too small when next to uppercased Latin text, because Arabic and Hebrew don’t include uppercase letters. To visually balance Arabic or Hebrew text with Latin text that uses all capitals, it often works well to increase the RTL font size by about 2 points.
> 필요에 따라 인접한 라틴어와 RTL 스크립트의 균형을 시각적으로 조정합니다. 단추, 레이블 및 제목에서 아랍어와 히브리어에는 대문자가 포함되지 않기 때문에 대소문자 옆에 아랍어 또는 히브리어 텍스트가 너무 작게 나타날 수 있습니다. 아랍어 또는 히브리어 텍스트와 모든 대소문자를 사용하는 라틴어 텍스트의 시각적 균형을 맞추기 위해 RTL 글꼴 크기를 약 2포인트 정도 늘리는 것이 잘 작동하는 경우가 많습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-uneven-vertical-height_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-uneven-vertical-height_2x.png)

Arabic and Hebrew text can look too small next to uppercased Latin text of the same font size.
> 같은 글꼴 크기의 대문자로 된 라틴어 텍스트 옆에 아랍어와 히브리어 텍스트가 너무 작게 보일 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-even-vertical-height_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-even-vertical-height_2x.png)

You can slightly increase the font size of Arabic and Hebrew text to visually balance uppercased Latin text.
> 아랍어 및 히브리어 텍스트의 글꼴 크기를 약간 늘려 대문자로 표시된 라틴 텍스트의 균형을 시각적으로 조정할 수 있습니다.
>




# **Images**

**Avoid flipping images like photographs, illustrations, and general artwork.** Flipping an image often changes the image’s meaning; flipping a copyrighted image could be a violation. If an image’s content is strongly connected to reading direction, consider creating a new version of the image instead of flipping the original.
> 사진, 그림 및 일반 예술작품과 같은 이미지를 뒤집지 마십시오. 이미지를 뒤집으면 이미지의 의미가 자주 변경됩니다. 저작권이 있는 이미지를 뒤집으면 위반이 될 수 있습니다. 이미지 내용이 읽기 방향에 강하게 연결된 경우 원본을 뒤집는 대신 이미지의 새 버전을 만드는 것을 고려해 보십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-right_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-right_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-wrong_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-wrong_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Reverse the positions of images when their order is meaningful.** For example, if you display multiple images in a specific order like chronological, alphabetical, or favorite, reverse their positions to preserve the order’s meaning in the RTL context.
> 예를 들어 시간순, 알파벳순 또는 즐겨찾기와 같은 특정 순서로 여러 이미지를 표시할 경우 RTL 컨텍스트에서 해당 위치를 반대로 표시하여 순서의 의미를 보존합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-ltr_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-ltr_2x.png)

Items with meaningful positions in the LTR context
> LTR 컨텍스트에서 의미 있는 위치가 있는 항목
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-rtl_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-rtl_2x.png)

Items with meaningful positions in the RTL context
> RTL 컨텍스트에서 의미 있는 위치를 가진 항목
>




# **Interface icons**

When you use [SF Symbols](../foundations/sf-symbols) to supply interface icons for your app, you get variants for the RTL context and localized symbols for Arabic and Hebrew, among other languages. If you create custom symbols, you can specify their directionality. For developer guidance, see [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/uiimage/creating_custom_symbol_images_for_your_app).
> SF 기호를 사용하여 앱의 인터페이스 아이콘을 제공하면 다른 언어 중에서도 RTL 컨텍스트에 대한 변형과 아랍어와 히브리어의 지역화된 기호를 얻을 수 있습니다. 사용자 정의 기호를 만드는 경우 방향을 지정할 수 있습니다. 개발자 지침은 앱에 대한 사용자 지정 기호 이미지 만들기를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-dark.svg)

LTR variants of directional symbols

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-rtl-dark.svg)

RTL variants of directional symbols

**Flip interface icons that represent text or reading direction.** For example, if an interface icon uses left-aligned bars to represent text in the LTR context, right-align the bars in the RTL context.
> 텍스트 또는 읽기 방향을 나타내는 인터페이스 아이콘을 뒤집습니다. 예를 들어 인터페이스 아이콘이 왼쪽 정렬 막대를 사용하여 LTR 컨텍스트에서 텍스트를 나타내는 경우 RTL 컨텍스트에서 막대를 오른쪽 정렬합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-dark.svg)

LTR variant of a symbol that represents text
> 텍스트를 나타내는 기호의 LTR 변형
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-rtl-dark.svg)

RTL variant of a symbol that represents text
> 텍스트를 나타내는 기호의 RTL 변형
>




**Consider creating a localized version of an interface icon that displays text.** Some interface icons include letters or words to help communicate a script-related concept, like font-size choice or a signature. If you have a custom interface icon that needs to display actual text, consider creating a localized version. For example, SF Symbols offers different versions of the signature, rich-text, and I-beam pointer symbols for use with Latin, Hebrew, and Arabic text, among others.
> 텍스트를 표시하는 인터페이스 아이콘의 지역화된 버전을 만드는 것이 좋습니다. 일부 인터페이스 아이콘에는 글꼴 크기 선택이나 서명과 같은 스크립트 관련 개념을 전달하는 데 도움이 되는 문자나 단어가 포함되어 있습니다. 실제 텍스트를 표시해야 하는 사용자 지정 인터페이스 아이콘이 있는 경우 지역화된 버전을 만드는 것을 고려해 보십시오. 예를 들어 SF 심볼은 라틴어, 히브리어 및 아랍어 텍스트와 함께 사용할 수 있는 다양한 버전의 시그니처, 리치 텍스트 및 I-빔 포인터 기호를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-dark.svg)

Latin

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-he-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-he-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-he-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-he-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-he-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-he-dark.svg)

Hebrew

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-ar-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-ar-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-ar-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-ar-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-ar-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-ar-dark.svg)

Arabic

If you have a custom interface icon that uses letters or words to communicate a concept unrelated to reading or writing, consider designing an alternative image that doesn’t use text.
> 문자나 단어를 사용하여 읽기 또는 쓰기와 무관한 개념을 전달하는 사용자 지정 인터페이스 아이콘이 있는 경우 텍스트를 사용하지 않는 대체 이미지를 설계하는 것을 고려해 보십시오.
>





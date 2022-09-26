# **[foundations] icons**

### An effective icon is a graphic asset that expresses a single concept in ways people instantly understand.
> 효과적인 아이콘은 사람들이 즉시 이해하는 방식으로 하나의 개념을 표현하는 그래픽 자산이다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-icons-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-icons-intro-dark_2x.png)

Apps and games use a variety of simple icons to help people understand the items, actions, and modes they can choose. Unlike [app icons](../foundations/app-icons), which can use rich visual details like shading, texturing, and highlighting to evoke the app’s personality, an *interface icon* typically uses streamlined shapes and touches of color to communicate a straightforward idea.
> 앱과 게임은 다양한 간단한 아이콘을 사용하여 사람들이 선택할 수 있는 항목, 동작 및 모드를 이해할 수 있도록 도와줍니다. 음영, 텍스처링, 하이라이팅과 같은 풍부한 시각적 디테일을 사용하여 앱의 개성을 불러일으킬 수 있는 앱 아이콘과는 달리, 인터페이스 아이콘은 일반적으로 유선형의 모양과 색의 터치를 사용하여 간단한 아이디어를 전달한다.
>




You can design interface icons — also called *glyphs* or *template images* — or you can choose symbols from the SF Symbols app, using them as-is or customizing them to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image. For guidance, see [SF Symbols](../foundations/sf-symbols).
> 인터페이스 아이콘(글리프 또는 템플릿 이미지라고도 함)을 디자인하거나 SF 기호 앱에서 기호를 선택하여 그대로 사용하거나 필요에 맞게 사용자 지정할 수 있습니다. 인터페이스 아이콘과 기호는 모두 검은색과 선명한 색상을 사용하여 모양을 정의합니다. 시스템은 각 이미지의 검은색 영역에 다른 색상을 적용할 수 있습니다. 자세한 내용은 SF 기호를 참조하십시오.
>




# **Best practices**

**Create a recognizable, highly simplified design.** Too many details can make an interface icon confusing or unreadable. Strive for a simple, universal design that most people will recognize quickly. In general, icons work best when they use familiar visual metaphors that are directly related to the actions they initiate or content they represent.
> 인식 가능하고 매우 단순화된 설계를 만듭니다. 세부 정보가 너무 많으면 인터페이스 아이콘을 혼동하거나 읽을 수 없게 됩니다. 대부분의 사람들이 빠르게 인식할 수 있는 단순하고 보편적인 디자인을 위해 노력하십시오. 일반적으로 아이콘은 시작하는 동작이나 그들이 나타내는 내용과 직접 관련된 익숙한 시각적 은유를 사용할 때 가장 잘 작동한다.
>




**Maintain visual consistency across all interface icons in your app.** Whether you use only custom icons or mix custom and system-provided ones, all interface icons in your app should use a consistent size, level of detail, stroke thickness (or weight), and perspective. Depending on the visual weight of an icon, you may need to adjust its dimensions to ensure that it appears visually consistent with other icons.
> 앱의 모든 인터페이스 아이콘에 대해 시각적 일관성을 유지합니다. 사용자 지정 아이콘만 사용하거나 사용자 지정 아이콘과 시스템이 제공하는 아이콘을 혼합하든 앱의 모든 인터페이스 아이콘은 일관된 크기, 세부 수준, 스트로크 두께(또는 무게) 및 관점을 사용해야 합니다. 아이콘의 시각적 무게에 따라 다른 아이콘과 시각적으로 일치하도록 크기를 조정해야 할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/custom-icon-sizes_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/custom-icon-sizes_2x.png)

To help achieve visual consistency, adjust individual icon sizes as necessary...
> 시각적 일관성을 유지하기 위해 필요에 따라 개별 아이콘 크기를 조정합니다...
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/custom-icon-line-weights_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/custom-icon-line-weights_2x.png)

...and use the same stroke weight in every icon.
> 모든 아이콘에서 동일한 스트로크 무게를 사용합니다.
>




**In general, match the weights of interface icons and adjacent text.** Unless you want to emphasize either the icons or the text, using the same weight for both gives your content a consistent appearance and level of emphasis.
> 일반적으로 인터페이스 아이콘과 인접 텍스트의 가중치를 일치시킵니다. 아이콘 또는 텍스트를 강조하지 않으려면 두 아이콘에 동일한 가중치를 사용하면 콘텐츠에 일관된 모양과 강조 수준을 제공할 수 있습니다.
>




**If necessary, add padding to a custom interface icon to achieve optical alignment.** Some icons — especially asymmetric ones — can look unbalanced when you center them geometrically instead of optically. For example, the download icon shown below has more visual weight on the bottom than on the top, which can make it look too low if it’s geometrically centered.
> 필요한 경우 사용자 지정 인터페이스 아이콘에 패딩을 추가하여 광학 정렬을 수행하십시오. 일부 아이콘(특히 비대칭 아이콘)은 광학 대신 기하학적으로 중심을 맞출 때 불균형적으로 보일 수 있습니다. 예를 들어, 아래 표시된 다운로드 아이콘은 위쪽보다 아래쪽의 시각적 무게가 더 크기 때문에 기하학적 중심에 있는 경우 너무 낮게 보일 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/asymmetric-glyph.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/asymmetric-glyph.svg)

An asymmetric icon can look off center even though it’s not.
> 비대칭 아이콘은 중심에서 벗어난 것처럼 보일 수 있습니다.
>




In such cases, you can slightly adjust the position of the icon until it’s optically centered. When you create an asset that includes your adjustments as padding around an interface icon (as shown below on the right), you can optically center the icon by geometrically centering the asset.
> 이러한 경우 아이콘이 광학적으로 중앙에 위치할 때까지 아이콘의 위치를 약간 조정할 수 있습니다. 조정을 패딩으로 포함하는 자산을 인터페이스 아이콘(오른쪽 아래 표시) 주위에 생성할 때 자산을 기하학적으로 중앙에 배치하여 아이콘의 중심을 광학적으로 지정할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/asymmetric-glyph-optically-centered.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/asymmetric-glyph-optically-centered.svg)

Moving the icon a few pixels higher optically centers it; including the pixels in padding simplifies centering.
> 아이콘을 몇 픽셀 더 높게 이동하면 광학적으로 중심이 조정됩니다. 패딩에 픽셀을 포함하면 중심이 단순해집니다.
>




Adjustments for optical centering are typically very small, but they can have a big impact on your app’s appearance.
> 광학 중심 조정은 일반적으로 매우 작지만 앱 모양에 큰 영향을 미칠 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/asymmetric-glyph-before-and-after.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/asymmetric-glyph-before-and-after.svg)

Before optical centering (left) and after optical centering (right).
> 광학 센터링 전(왼쪽)과 광학 센터링 후(오른쪽)입니다.
>




**Provide a selected-state version of an interface icon only if necessary.** You don’t need to provide selected and unselected appearances for an icon that’s used in controls and areas that automatically indicate selection. For example, sidebars, iOS tab bars, and macOS toolbars can convey selection state by applying your app’s accent color or adding a background appearance.
> 필요한 경우에만 인터페이스 아이콘의 선택된 상태 버전을 제공하십시오. 자동으로 선택을 나타내는 컨트롤 및 영역에 사용되는 아이콘에 대해 선택 및 선택되지 않은 모양을 제공할 필요는 없습니다. 예를 들어 사이드바, iOS 탭바, macOS 툴바는 앱의 악센트 색상을 적용하거나 배경 모양을 추가하여 선택 상태를 전달할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/selected-deselected-right-2.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/selected-deselected-right-2.svg)

In iOS, a selected tab bar icon receives the app’s accent color.
> iOS에서 선택한 탭 바 아이콘은 앱의 악센트 색상을 받는다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/selected-deselected-right-1.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/selected-deselected-right-1.svg)

In macOS, a selected toolbar icon receives a darker stroke and a background appearance.
> macOS에서 선택한 도구 모음 아이콘은 더 어두운 스트로크와 배경 모양을 받습니다.
>




In contrast, iOS toolbars and navigation bars don’t provide a selection appearance, so you need to create both filled and unfilled versions of each interface icon you supply for these areas.
> 반대로 iOS 도구 모음과 탐색 모음은 선택 모양을 제공하지 않으므로 이러한 영역에 대해 제공하는 각 인터페이스 아이콘의 채워진 버전과 채워지지 않은 버전을 모두 만들어야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/selected-deselected-wrong.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/selected-deselected-wrong.svg)

**Create inclusive designs.** Prefer depicting human figures without unnecessary references to specific genders, and be sure that your icons are welcoming and understandable to everyone. For guidance, see [Inclusion](../foundations/inclusion).
> 포괄적인 디자인을 만드십시오. 특정 성별에 대한 불필요한 언급 없이 인간의 모습을 묘사하는 것을 선호하고, 여러분의 아이콘이 모든 사람들에게 환영받고 이해되도록 해야 합니다. 자세한 내용은 포함을 참조하십시오.
>




**Include text in your design only when it’s essential for conveying meaning.** For example, using a character in an interface icon that represents text formatting can be the most direct way to communicate the concept. If you need to display individual characters in your icon, be sure to localize them. If you need to suggest a passage of text, design an abstract representation of it, and include a flipped version of the icon to use when the context is right-to-left. For guidance, see [Right to left](../foundations/right-to-left).
> 예를 들어, 텍스트 형식을 나타내는 인터페이스 아이콘의 문자를 사용하는 것이 개념을 전달하는 가장 직접적인 방법이 될 수 있습니다. 아이콘에 개별 문자를 표시해야 하는 경우 해당 문자를 현지화해야 합니다. 텍스트 구절을 제안해야 하는 경우, 텍스트의 추상적 표현을 설계하고 컨텍스트가 오른쪽에서 왼쪽으로 이동할 때 사용할 반전된 버전의 아이콘을 포함합니다. 자세한 내용은 오른쪽에서 왼쪽으로를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/character-in-glyph_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/character-in-glyph_2x.png)

Create localized versions of an icon that displays individual characters.
> 개별 문자를 표시하는 아이콘의 지역화된 버전을 만듭니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/abstract-text-in-glyph_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/images/abstract-text-in-glyph_2x.png)

Create a flipped version of an icon that suggests reading direction.
> 읽기 방향을 제안하는 반전된 버전의 아이콘을 만듭니다.
>




**If you create a custom interface icon, use a vector format like PDF or SVG.** The system automatically scales a vector-based interface icon for high-resolution displays, so you don’t need to provide high-resolution versions of it. In contrast, PNG — used for app icons and other images that include effects like shading, textures, and highlighting — doesn’t support scaling, so you have to supply multiple versions for each PNG-based interface icon. Alternatively, you can create a custom SF Symbol and specify a scale that ensures the symbol’s emphasis matches adjacent text. For guidance, see [SF Symbols](../foundations/sf-symbols).
> 사용자 지정 인터페이스 아이콘을 만드는 경우 PDF 또는 SVG와 같은 벡터 형식을 사용합니다. 시스템은 고해상도 디스플레이를 위해 벡터 기반 인터페이스 아이콘의 크기를 자동으로 조정하므로 고해상도 버전을 제공할 필요가 없습니다. 이와는 대조적으로 음영, 텍스처 및 강조 표시와 같은 효과를 포함하는 앱 아이콘 및 기타 이미지에 사용되는 PNG는 배율을 지원하지 않으므로 각 PNG 기반 인터페이스 아이콘에 대해 여러 버전을 제공해야 합니다. 또는 사용자 정의 SF 기호를 작성하고 기호의 강조가 인접한 텍스트와 일치하도록 축척을 지정할 수 있습니다. 자세한 내용은 SF 기호를 참조하십시오.
>




**Provide alternative text labels for custom interface icons.** Alternative text labels — or accessibility descriptions — aren’t visible, but they let VoiceOver audibly describe what’s onscreen, simplifying navigation for people with visual disabilities. For guidance, see [Content descriptions](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/#content-descriptions).
> 사용자 지정 인터페이스 아이콘에 대한 대체 텍스트 레이블을 제공합니다. 대체 텍스트 레이블 또는 내게 필요한 옵션 설명은 볼 수 없지만 VoiceOver에서 화면에 표시되는 내용을 청각적으로 설명할 수 있으므로 시각 장애가 있는 사용자의 탐색을 간소화할 수 있습니다. 자세한 내용은 내용 설명을 참조하십시오.
>




**Avoid using replicas of Apple hardware products.** Hardware designs tend to change frequently and can make your interface icons and other content appear dated. If you must display Apple hardware, use only the images available in [Apple Design Resources](https://developer.apple.com/design/resources/) or the SF Symbols that represent various Apple products.
> Apple 하드웨어 제품의 복제본을 사용하지 마십시오. 하드웨어 설계는 자주 변경되며 인터페이스 아이콘 및 기타 컨텐츠가 오래된 것으로 나타날 수 있습니다. Apple 하드웨어를 표시해야 하는 경우 Apple Design Resources 또는 다양한 Apple 제품을 나타내는 SF 기호에서 사용할 수 있는 이미지만 사용하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, tvOS, or watchOS.*
> No additional considerations for iOS, iPadOS, tvOS, or watchOS.
>




# **macOS**

### **Document icons**

If your macOS app can use a custom document type, you can create a document icon to represent it. Traditionally, a document icon looks like a piece of paper with its top-right corner folded down. This distinctive appearance helps people distinguish documents from apps and other content, even when icon sizes are small.
> macOS 앱에서 사용자 정의 문서 유형을 사용할 수 있는 경우 이를 나타내는 문서 아이콘을 만들 수 있습니다. 일반적으로 문서 아이콘은 오른쪽 상단 모서리가 아래로 접힌 종이처럼 보입니다. 이러한 독특한 모양은 아이콘 크기가 작더라도 사람들이 문서와 앱 및 기타 콘텐츠를 구별하는 데 도움이 된다.
>




If you don’t supply a document icon for a file type you support, macOS creates one for you by compositing your app icon and the file’s extension onto the canvas. For example, Preview uses a system-generated document icon to represent JPG files.
> 지원하는 파일 형식에 대한 문서 아이콘을 제공하지 않으면 macOS에서 앱 아이콘과 파일 확장자를 캔버스에 합성하여 만듭니다. 예를 들어, 미리보기는 시스템에서 생성된 문서 아이콘을 사용하여 JPG 파일을 나타냅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-generated_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-generated_2x.png)

In some cases, it can make sense to create a set of document icons to represent a range of file types your app handles. For example, Xcode uses custom document icons to help people distinguish projects, AR objects, and Swift code files.
> 경우에 따라 응용프로그램이 처리하는 파일 유형의 범위를 나타내는 문서 아이콘 집합을 만드는 것이 합리적일 수 있습니다. 예를 들어 Xcode는 사용자 정의 문서 아이콘을 사용하여 프로젝트, AR 개체 및 Swift 코드 파일을 구분합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-custom-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-custom-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-custom-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-custom-2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-custom-3_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-custom-3_2x.png)

To create a custom document icon, you can supply any combination of background fill, center image, and text. Beginning in macOS 11, the system layers, positions, and masks these elements as needed and composites them onto the familiar folded-corner icon shape.
> 사용자 정의 문서 아이콘을 작성하려면 배경 채우기, 중앙 이미지 및 텍스트의 모든 조합을 제공할 수 있습니다. macOS 11부터, 시스템은 필요에 따라 이러한 요소를 레이어, 위치 및 마스크하고 익숙한 접힌 모서리 아이콘 모양에 합성한다.
>




![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts-background-fill_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts-background-fill_2x.png)

Background fill

![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts-center-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts-center-image_2x.png)

Center image

![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts-text_2x.png)

Text

![https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts_2x.png](https://developer.apple.com/design/human-interface-guidelines/macos/images/doc-icon-parts_2x.png)

macOS 11 composites the elements you supply to produce your custom document icon.
> macOS 11은 사용자 정의 문서 아이콘을 생성하기 위해 사용자가 제공하는 요소를 합성합니다.
>




[Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps) provides a template you can use to create a custom background fill and center image for a document icon. As you use this template, follow the guidelines below.
> Apple Design Resources는 문서 아이콘의 사용자 정의 배경 채우기 및 중앙 이미지를 작성하는 데 사용할 수 있는 템플리트를 제공합니다. 이 템플릿을 사용할 때 아래 지침을 따르십시오.
>





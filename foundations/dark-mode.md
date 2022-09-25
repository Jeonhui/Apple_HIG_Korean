# **[foundations] dark-mode**

### Dark Mode is a systemwide appearance setting that uses a dark color palette to provide a comfortable viewing experience tailored for low-light environments.
> 다크 모드는 어두운 색 팔레트를 사용하여 저조도 환경에 맞춘 편안한 시청 환경을 제공하는 시스템 전체의 외관 설정입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-dark-mode-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-dark-mode-intro-dark_2x.png)

In iOS, iPadOS, macOS, and tvOS, people often choose Dark Mode as their default interface style, and they generally expect all apps and games to respect their preference. In Dark Mode, the system uses a dark color palette for all screens, views, menus, and controls, and may also use greater perceptual contrast to make foreground content stand out against the darker backgrounds.
> iOS, iPadOS, macOS 및 tvOS에서 사람들은 종종 다크 모드를 기본 인터페이스 스타일로 선택하며, 일반적으로 모든 앱과 게임이 자신의 선호도를 존중하기를 기대합니다. 다크 모드에서 시스템은 모든 화면, 보기, 메뉴 및 컨트롤에 어두운 색 팔레트를 사용하며, 또한 더 높은 지각 대비를 사용하여 어두운 배경에 대해 전경 내용을 두드러지게 할 수 있습니다.
>




# **Best practices**

**Avoid offering an app-specific appearance setting.** An app-specific appearance mode option creates more work for people because they have to adjust more than one setting to get the appearance they want. Worse, they may think your app is broken because it doesn't respond to their systemwide appearance choice.
> 앱별 모양 설정을 제공하지 마십시오. 앱별 모양 모드 옵션은 원하는 모양을 얻기 위해 둘 이상의 설정을 조정해야 하기 때문에 사용자에게 더 많은 작업을 만듭니다. 더 나쁜 것은, 그들은 당신의 앱이 그들의 시스템 전체의 외관 선택에 반응하지 않기 때문에 당신의 앱이 고장났다고 생각할 수 있다.
>




**Ensure that your app looks good in both appearance modes.** In addition to using one mode or the other, people can choose the Auto appearance setting, which switches between light and dark appearances as conditions change throughout the day, potentially while your app is running.
> 두 가지 모양 모드 모두에서 앱이 잘 보이는지 확인하십시오. 한 가지 모드 또는 다른 모드를 사용하는 것 외에도, 사람들은 앱이 실행되는 동안 하루 종일 상태가 변경됨에 따라 밝은 모양과 어두운 모양을 전환하는 자동 모양 설정을 선택할 수 있습니다.
>




**Test your content to make sure that it remains comfortably legible in both appearance modes.** For example, in Dark Mode with Increase Contrast and Reduce Transparency turned on (both separately and together), you may find places where dark text is less legible when it’s on a dark background. You might also find that turning on Increase Contrast in Dark Mode can result in reduced visual contrast between dark text and a dark background. Although people with strong vision might still be able to read lower contrast text, such text could be illegible for many. For guidance, see [Color and effects](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/#color-and-effects).
> 내용을 테스트하여 두 모양 모드 모두에서 읽기 쉬운 상태로 유지되도록 하십시오. 예를 들어 대비 증가 및 투명도 감소 기능이 설정된 다크 모드에서(별도 함께 사용 가능) 어두운 배경에 어두운 텍스트가 잘 보이지 않는 곳을 찾을 수 있습니다. 어두운 모드에서 대비 증가를 설정하면 어두운 텍스트와 어두운 배경 사이의 시각적 대비가 감소할 수도 있습니다. 비록 강한 시각을 가진 사람들이 여전히 낮은 대조 텍스트를 읽을 수 있을지 모르지만, 그러한 텍스트는 많은 사람들에게 읽기 어려울 수 있다. 자세한 내용은 색상 및 효과를 참조하십시오.
>




**In rare cases, consider using only a dark appearance in the interface.** For example, it can make sense for an app that enables immersive media viewing to use a permanently dark appearance that lets the UI recede and helps people focus on the media.
> 예를 들어 몰입형 미디어 보기를 가능하게 하는 앱에서 UI가 멀어지고 미디어에 집중할 수 있도록 도와주는 영구적으로 어두운 외관을 사용하는 것이 이치에 맞는 경우도 있습니다.
>




# **Dark Mode colors**

The color palette in Dark Mode includes dimmer background colors and brighter foreground colors. It’s important to realize that these colors aren’t necessarily inversions of their light counterparts: while many colors are inverted, some are not. For more information, see [Color > Specifications](https://developer.apple.com/design/human-interface-guidelines/foundations/color/#specifications).
> 다크 모드의 색상 팔레트에는 더 어두운 배경색과 더 밝은 전경색이 포함됩니다. 이러한 색상이 반드시 밝은 색상의 반전일 필요는 없다는 것을 깨닫는 것이 중요합니다. 많은 색상이 반전되어 있지만, 일부는 반전되어 있지 않습니다. 자세한 내용은 색상 > 사양을 참조하십시오.
>




**Embrace colors that adapt to the current appearance.** Semantic colors (like [labelColor](https://developer.apple.com/documentation/appkit/nscolor/1534657-labelcolor) and [controlColor](https://developer.apple.com/documentation/appkit/nscolor/1524856-controlcolor) in macOS or [separator](https://developer.apple.com/documentation/uikit/uicolor/3173139-separator) in iOS and iPadOS) automatically adapt to the current appearance. When you need a custom color, add a Color Set asset to your app’s asset catalog in Xcode, and specify the bright and dim variants of the color. Avoid using hard-coded color values or colors that don’t adapt.
> 현재 외관에 맞는 색상을 수용합니다. 의미 색상(macOS의 labelColor 및 controlColor, iOS 및 iPad의 구분자 등)OS)가 현재 모양에 자동으로 적응합니다. 사용자 지정 색상이 필요한 경우 Xcode의 앱 자산 카탈로그에 색상 세트 자산을 추가하고 색상의 밝은 색과 어두운 색을 지정합니다. 하드 코딩된 색상 값이나 맞지 않는 색상을 사용하지 않도록 합니다.
>




**Aim for sufficient color contrast in all appearances.** Using system-defined colors can help you achieve a good contrast ratio between your foreground and background content. At a minimum, make sure the contrast ratio between colors is no lower than 4.5:1. For custom foreground and background colors, strive for a contrast ratio of 7:1, especially in small text. This ratio ensures that your foreground content stands out from the background, and helps your content meet recommended accessibility guidelines.
> 모든 모양에서 충분한 색 대비가 되도록 합니다. 시스템 정의 색상을 사용하면 전경과 배경 내용 간에 양호한 대비 비율을 얻을 수 있습니다. 최소한 색상 간 대비 비율이 4.5:1 이상이어야 합니다. 사용자 정의 전경색과 배경색을 사용하려면 특히 작은 텍스트에서 7:1의 대비 비율을 확보하십시오. 이 비율은 전경 콘텐츠가 백그라운드에서 두드러지도록 하며 권장 접근성 지침을 충족하도록 도와줍니다.
>




**Soften the color of white backgrounds.** If you display a content image that includes a white background, consider slightly darkening the image to prevent the background from glowing in the surrounding Dark Mode context.
> 흰색 배경의 색을 부드럽게 합니다. 흰색 배경이 포함된 내용 이미지를 표시할 경우 주변 다크 모드 컨텍스트에서 배경이 빛나지 않도록 이미지를 약간 어둡게 하는 것이 좋습니다.
>




# **Icons and images**

The system uses [SF Symbols](../foundations/sf-symbols) (which automatically adapt to Dark Mode) and full-color images that are optimized for both light and dark appearances.
> 이 시스템은 SF 기호(Dark Mode에 자동으로 적응)와 밝은 색과 어두운 색상에 모두 최적화된 풀 컬러 이미지를 사용합니다.
>




**Use SF Symbols wherever possible.** Symbols work well in both appearance modes when you use dynamic colors to tint them or when you add vibrancy. For guidance, see [Color](../foundations/color).
> 가능한 경우 SF 기호를 사용하십시오. 기호는 동적 색상을 사용하여 색을 입히거나 활성을 추가할 때 두 모양 모드에서 모두 잘 작동합니다. 자세한 내용은 색상을 참조하십시오.
>




**Design separate interface icons for light and dark appearances if necessary.** For example, an icon that depicts a full moon might need a subtle dark outline to contrast well with a light background, but need no outline when it displays on a dark background. Similarly, an icon that represents a drop of oil might need a slight border to make the edge visible against a dark background.
> 예를 들어, 보름달을 묘사하는 아이콘은 밝은 배경과 잘 대비하기 위해 은은한 어두운 윤곽선이 필요하지만 어두운 배경에 표시될 때는 윤곽선이 필요 없습니다. 마찬가지로, 기름 한 방울을 나타내는 아이콘은 어두운 배경에 가장자리가 보이도록 약간의 테두리가 필요할 수 있습니다.
>




**Make sure full-color images and icons look good in both appearances.** Use the same asset if it looks good in both light and dark appearances. If an asset looks good in only one mode, modify the asset or create separate light and dark assets. Use asset catalogs to combine your assets into a single named image.
> 전체 색상의 이미지와 아이콘이 모두 잘 보이는지 확인하십시오. 밝은 색과 어두운 색 모두에서 잘 보이는 경우 동일한 자산을 사용하십시오. 한 가지 모드에서만 자산이 잘 보이는 경우 자산을 수정하거나 밝은 자산과 어두운 자산을 별도로 생성합니다. 자산 카탈로그를 사용하여 자산을 하나의 명명된 이미지로 결합합니다.
>




# **Text**

The system uses vibrancy and increased contrast to maintain the legibility of text on darker backgrounds.
> 이 시스템은 어두운 배경에서 텍스트의 가독성을 유지하기 위해 진동과 향상된 대비를 사용합니다.
>




**Use the system-provided label colors for labels.** The primary, secondary, tertiary, and quaternary label colors adapt automatically to light and dark appearances.
> 시스템에서 제공한 레이블 색상을 레이블에 사용합니다. 기본, 보조, 3차 및 4차 레이블 색상은 밝은 색과 어두운 색상에 자동으로 적응합니다.
>




**Use system views to draw text fields and text views.** System views and controls make your app’s text look good on all backgrounds, adjusting automatically for the presence or absence of vibrancy. When possible, use a system-provided view to display text instead of drawing the text yourself.
> 시스템 보기를 사용하여 텍스트 필드 및 텍스트 보기를 그릴 수 있습니다. 시스템 보기 및 컨트롤은 앱의 텍스트를 모든 배경에서 보기 좋게 만들어 활력 유무에 따라 자동으로 조정합니다. 가능한 경우 직접 텍스트를 그리는 대신 시스템에서 제공한 보기를 사용하여 텍스트를 표시합니다.
>




# **Platform considerations**

*No additional considerations for tvOS. Dark Mode isn't supported in watchOS.*
> tvOS에 대한 추가 고려 사항 없음. 시계에서 다크 모드가 지원되지 않습니다.OS.
>




# **iOS, iPadOS**


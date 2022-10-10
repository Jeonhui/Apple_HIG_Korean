# **[foundations] color**

### Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.
> 색상을 현명하게 사용하면 커뮤니케이션을 강화하고, 브랜드를 환기하며, 시각적 연속성을 제공하고, 상태와 피드백을 전달하며, 사람들이 정보를 이해하도록 도울 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-color-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-color-intro-dark_2x.png)

The system defines colors that look good on various backgrounds and appearance modes, and can automatically adapt to
> 이 시스템은 다양한 배경 및 외관 모드에서 잘 어울리는 색상을 정의하고 자동으로 적응할 수 있습니다.
>



vibrancy and accessibility settings. People are familiar with the system colors, and using them is a convenient way to
> 활력 및 접근성 설정. 사람들은 시스템 색상에 익숙하고, 그것들을 사용하는 것은 편리한 방법이다.
>



make your experience feel at home on the device.
> 기기에서 편안한 경험을 할 수 있습니다.
>




You may also want to use custom colors to enhance the visual experience of your app or game and express its unique
> 여러분은 또한 독특한를 표명하세요 앱이나 게임의 시각적 경험을 향상시키기 위해 사용자 지정 색을 사용하기를 원할 겁니다.
>



personality. The following guidelines can help you use color in ways that people appreciate, regardless of whether you
> 성격. 다음 가이드라인은 당신이 당신이 당신이 당신이 좋아하는 방법으로 색을 사용하는 것을 도울 수 있다.
>



use system-defined or custom colors.

# **Best practices**

**Use color sparingly in nongame apps.** In a nongame app, overuse of color can make communication less clear and can be
> 게임 이외의 앱에서는 색상을 적게 사용합니다. 게임 이외의 앱에서, 색상의 남용은 의사소통을 덜 명확하게 만들 수 있고 더 명확해질 수 있다.
>



distracting. Prefer using touches of color to call attention to important information or show the relationship between
> 산만한 중요한 정보에 주의를 환기시키거나 그 사이의 관계를 보여주기 위해 색의 터치를 사용하는 것을 선호합니다.
>



parts of the interface.

**Avoid using the same color to mean different things.** Use color consistently throughout your interface, especially
> 다른 것을 의미하기 위해 같은 색을 사용하는 것을 피하세요. 특히 인터페이스 전반에 걸쳐 일관된 색상 사용
>



when you use it to help communicate information like status or interactivity. For example, an app might use blue to
> 상태 또는 상호 작용과 같은 정보를 전달하기 위해 사용할 때. 예를 들어, 앱이 파란색을 사용하여
>



indicate that people can tap text to view more. Even when the app communicates interactivity using a visual indicator
> 사용자가 텍스트를 눌러 더 많이 볼 수 있음을 나타냅니다. 앱이 시각적 표시기를 사용하여 상호 작용을 전달하는 경우에도
>



that doesn't rely on color — such as a chevron or arrow icon — using a color other than blue for the interactive text is
> 색상(예: 쉐브론 또는 화살표 아이콘)에 의존하지 않는 대화형 텍스트에 파란색이 아닌 다른 색상을 사용하는 것은
>



confusing.

**Make sure your app’s colors work well in both light and dark appearance modes.** With the exception of watchOS, which
> 앱의 색상이 밝은 모양과 어두운 모양 모드 모두에서 잘 작동하는지 확인합니다. watchOS를 제외하고,
>



always uses a pure black background, the platforms offer a dark alternative to the default light appearance. Dark Mode
> 항상 순수한 검은색 배경을 사용하며, 플랫폼은 기본 조명 모양에 대한 어두운 대안을 제공합니다. 다크 모드
>



uses a darker color palette for all screens, views, menus, and controls, and can increase *vibrancy* — a subtle effect
> 모든 화면, 보기, 메뉴 및 컨트롤에 어두운 색 팔레트를 사용하며, 생동감을 높일 수 있습니다. 미묘한 효과입니다.
>



that dynamically blends foreground and background colors — to make foreground content stand out against darker
> 전경색과 배경색을 역동적으로 혼합함으로써 전경 콘텐츠를 어두운 색보다 돋보이게 합니다.
>



backgrounds. System colors automatically support both appearances; if you use a custom color, you need to supply both
> 배경 시스템 색상은 자동으로 두 모양을 지원합니다. 사용자 지정 색상을 사용하는 경우 두 가지 색상을 모두 제공해야 합니다.
>



light and dark variants. For guidance,
> 명암 변종 안내를 위해,
>



see [Dark Mode](../foundations/dark-mode).

**Test your app’s color scheme under a variety of lighting conditions.** Colors can look different when you run your app
> 다양한 조명 조건에서 앱의 색 구성표를 테스트합니다. 앱을 실행할 때 색상이 다르게 보일 수 있습니다.
>



outside on a sunny day or in dim light. Adjust colors to provide an optimal viewing experience in the majority of use
> 햇빛이 내리쬐는 날이나 어두운 불빛 아래서 대부분의 사용에서 최적의 보기 환경을 제공하도록 색상 조정
>



cases.

**Test your app on devices with different displays.** For example, the True Tone display — available on certain iPhone,
> 디스플레이가 다른 장치에서 앱을 테스트합니다. 예를 들어, True Tone 디스플레이 - 특정 iPhone에서 사용할 수 있습니다.
>



iPad, and Mac models — uses ambient light sensors to automatically adjust the white point of the display to adapt to the
> iPad 및 Mac 모델— 주변 광센서를 사용하여 디스플레이의 흰색 점을 자동으로 조정하여 적응시킵니다.
>



lighting conditions of the current environment. Apps that focus primarily on reading, photos, video, and gaming can
> 현재 환경의 조명 조건 읽기, 사진, 비디오 및 게임에 주로 초점을 맞춘 앱은 다음과 같습니다.
>



strengthen or weaken this effect by specifying a white point adaptivity style (for developer guidance,
> 화이트 포인트 적응 스타일을 지정함으로써 이 효과를 강화하거나 약화시킨다(개발자 지침의 경우,
>



see [UIWhitePointAdaptivityStyle](https://developer.apple.com/documentation/bundleresources/information_property_list/uiwhitepointadaptivitystyle))
. Test tvOS apps on multiple brands of HD and 4K TVs, and with different display settings. You can also test the
> . 여러 브랜드의 HD 및 4K TV에서 서로 다른 디스플레이 설정을 사용하여 tvOS 앱을 테스트합니다. 또한 테스트 할 수 있습니다.
>



appearance of your app using different color profiles on a Mac — such as P3 and Standard RGB (sRGB) — by choosing a
> P3 및 표준 RGB(sRGB)와 같은 Mac에서 다른 색 프로필을 사용하는 앱의 외관:
>



profile in System Settings > Displays. For guidance,
> [시스템 설정] > [디스플레이]에서 프로파일을 선택합니다. 안내를 위해,
>



see [Color management](https://developer.apple.com/design/human-interface-guidelines/foundations/color#color-management)
.

**Consider how artwork and translucency affect nearby colors.** Variations in artwork sometimes warrant changes to
> 예술작품과 반투명함이 주변 색상에 어떤 영향을 미치는지 생각해 보세요. 예술작품의 변형은 때때로 다음의 변경을 보증한다.
>



nearby colors to maintain visual continuity and prevent interface elements from becoming overpowering or underwhelming.
> 시각적 연속성을 유지하고 인터페이스 요소가 지나치게 강력해지거나 압도되지 않도록 하기 위한 주변 색상.
>



Maps, for example, displays a light color scheme when in map mode but switches to a dark color scheme when in satellite
> 예를 들어 지도 모드에서는 밝은 색 구성표를 표시하지만 위성 모드에서는 어두운 색 구성표로 전환합니다.
>



mode. Colors can also appear different when placed behind or applied to a translucent element like a toolbar.
> 색상은 도구 모음과 같은 반투명 요소에 배치되거나 적용될 때 다르게 나타날 수 있습니다.
>




**If your app lets people choose colors, prefer system-provided color controls where available.** Using built-in color
> 앱에서 색상을 선택할 수 있는 경우 시스템에서 제공하는 색상 컨트롤을 선택합니다. 기본 제공 색상 사용
>



pickers provides a consistent user experience, in addition to letting people save a set of colors they can access from
> 피커는 사람들이 접근할 수 있는 색상 세트를 저장할 수 있게 하는 것 외에도 일관된 사용자 경험을 제공한다.
>



any app. For developer guidance, see [NSColorPanel](https://developer.apple.com/documentation/appkit/nscolorpanel) (
> 어떤 앱이든 개발자 지침은 NSColorPanel(색상 패널)을 참조하십시오.
>



macOS), and [UIColorWell](https://developer.apple.com/documentation/uikit/uicolorwell)
and [UIColorPickerViewController](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller) (iOS,
iPadOS, and Mac Catalyst).

# **Inclusive color**

**Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential
> 개체를 구별하고, 상호 작용을 나타내거나, 필수적인 정보를 전달하기 위해 색상에만 의존하지 마십시오.
>



information.** When you use color to convey information, be sure to provide the same information in alternative ways so
> 정보. 당신이 정보를 전달하기 위해 색을 사용할 때, 반드시 다른 방법으로 같은 정보를 제공해야 한다.
>



people with color blindness or other visual disabilities can understand it. For example, you can use labels or glyph
> 색맹이나 다른 시각 장애가 있는 사람들은 그것을 이해할 수 있다. 예를 들어 레이블 또는 글리프를 사용할 수 있습니다.
>



shapes to identify objects or states.
> 개체 또는 상태를 식별하는 도형입니다.
>




**Avoid using colors that make it hard to perceive content in your app.** For example, insufficient contrast can cause
> 앱에서 콘텐츠를 인식하기 어렵게 만드는 색상을 사용하지 마십시오. 예를 들어, 불충분한 대비는 다음을 일으킬 수 있다.
>



icons and text to blend with the background and make content hard to read, and people who are color blind might not be
> 배경과 섞여서 내용을 읽기 어렵게 만드는 아이콘과 텍스트, 그리고 색맹인 사람들은 그렇지 않을 수 있다.
>



able to distinguish some color combinations. For guidance,
> 일부 색상 조합을 구별할 수 있습니다. 안내를 위해,
>



see [Color and effects](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/#color-and-effects)
.

**Consider how the colors you use might be perceived in other countries and cultures.** For example, red communicates
> 여러분이 사용하는 색이 다른 나라와 문화에서 어떻게 인식될 수 있는지 생각해 보세요. 예를 들어, 빨간색은 통신합니다.
>



danger in some cultures, but has positive connotations in other cultures. Make sure the colors in your app send the
> 어떤 문화권에서는 위험하지만, 다른 문화권에서는 긍정적인 의미를 가지고 있다. 앱의 색상이 다음을 전송하는지 확인하십시오.
>



message you intend.

# **System colors**

**Avoid hard-coding system color values in your app.** Documented color values are for your reference during the app
> 앱에서 시스템 색상 값을 하드 코딩하지 않도록 합니다. 문서화된 색상 값은 앱에서 참조할 수 있습니다.
>



design process. The actual color values may fluctuate from release to release, based on a variety of environmental
> 설계 과정 실제 색상 값은 다양한 환경에 따라 릴리스마다 변동할 수 있습니다.
>



variables. Use APIs like [Color](https://developer.apple.com/documentation/swiftui/color) to apply system colors.
> 변수 시스템 색상을 적용하려면 Color와 같은 API를 사용하십시오.
>




iOS and macOS also define sets of *dynamic system colors* that match the color schemes of standard UI components and
> iOS와 macOS는 또한 표준 UI 구성 요소의 색상 체계와 일치하는 동적 시스템 색상 집합을 정의합니다.
>



automatically adapt to both light and dark appearances. Each dynamic color is semantically defined by its purpose,
> 자동으로 밝은 외관과 어두운 외관에 적응합니다. 각각의 동적 색상은 그 목적에 의해 의미적으로 정의된다.
>



rather than its appearance or color values. For example, some colors represent view backgrounds at different levels of
> 외관이나 색상 값보다는. 예를 들어, 일부 색상은 다른 수준의 뷰 배경을 나타냅니다.
>



hierarchy and other colors represent foreground content, such as labels, links, and separators.
> 계층 및 기타 색상은 레이블, 링크 및 구분 기호와 같은 전경 내용을 나타냅니다.
>




**Avoid replicating dynamic system colors.** Dynamic system colors — some of which can be patterns — may fluctuate from
> 동적 시스템 색상을 복제하지 않도록 합니다. 동적 시스템 색상(일부는 패턴일 수 있음)은 다음과 같이 변동할 수 있습니다.
>



release to release, based on a variety of environmental variables.
> 다양한 환경 변수를 기반으로 출시됩니다.
>




**Avoid redefining the semantic meanings of dynamic system colors.** To ensure a consistent experience and ensure your
> 동적 시스템 색상의 의미적 의미를 재정의하지 않도록 합니다. 일관된 경험을 보장하고 다음을 보장하기 위해
>



interface looks great when the appearance of macOS changes in the future, use dynamic system colors as intended.
> 향후 macOS의 외관이 바뀔 때 인터페이스가 훌륭해 보입니다, 의도한 대로 동적 시스템 색상을 사용하십시오.
>




# **Color management**

A *color space* represents the colors in a *color model* like RGB or CMYK. Common color spaces — sometimes called *
> 색 공간은 RGB 또는 CMYK와 같은 색상 모델에서 색상을 나타냅니다.
>



gamuts* — are sRGB and Display P3.
> Gamuts — sRGB 및 Display P3입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/color-graphic-wide-color-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/color-graphic-wide-color-dark_2x.png)

A *color profile* describes the colors in a color space using, for example, mathematical formulas or tables of data that
> 색상 프로파일은 예를 들어 다음과 같은 수학 공식 또는 데이터 테이블을 사용하여 색상 공간의 색상을 설명합니다.
>



map colors to numerical representations. An image embeds its color profile so that a device can interpret the image’s
> 색을 숫자로 나타내다 이미지가 색 프로필을 내장하여 장치가 이미지를 해석할 수 있도록 합니다.
>



colors correctly and reproduce them on a display.
> 올바른 색상과 디스플레이에서 재현합니다.
>




**Apply color profiles to your images.** Color profiles help ensure that your app’s colors appear as intended on
> 이미지에 색상 프로파일을 적용합니다. 색 프로필은 앱의 색상이 의도한 대로 나타나도록 합니다.
>



different displays. The sRGB color space produces accurate colors on most displays.
> 여러 가지 디스플레이 sRGB 색 공간은 대부분의 디스플레이에서 정확한 색상을 생성합니다.
>




**Use wide color to enhance the visual experience on compatible displays.** Wide color displays support a P3 color
> 호환되는 디스플레이의 시각적 경험을 향상시키려면 넓은 색상을 사용하십시오. 와이드 컬러 디스플레이는 P3 컬러를 지원합니다.
>



space, which can produce richer, more saturated colors than sRGB. As a result, photos and videos that use wide color are
> sRGB보다 더 풍부하고 포화된 색을 만들 수 있는 공간. 결과적으로, 넓은 색상을 사용하는 사진과 비디오는
>



more lifelike, and visual data and status indicators that use wide color can be more meaningful. When appropriate, use
> 보다 실제적인 색상과 넓은 색상을 사용하는 시각적 데이터 및 상태 표시기가 보다 의미 있을 수 있습니다. 적절한 경우,
>



the Display P3 color profile at 16 bits per pixel (per channel) and export images in PNG format. Note that you need to
> P3 컬러 프로파일을 픽셀당 16비트(채널당)로 표시하고 이미지를 PNG 형식으로 내보냅니다. 다음 작업을 수행해야 합니다.
>



use a wide color display to design wide color images and select P3 colors.
> 와이드 컬러 디스플레이를 사용하여 와이드 컬러 이미지를 디자인하고 P3 색상을 선택합니다.
>




**Provide color space–specific image and color variations if necessary.** In general, P3 colors and images appear fine
> 필요한 경우 색 공간별 이미지 및 색 변형을 제공합니다. 일반적으로 P3 색상과 이미지는 정상으로 보입니다.
>



on sRGB displays. Occasionally, it may be hard to distinguish two very similar P3 colors when viewing them on an sRGB
> sRGB 디스플레이에. 때때로 sRGB에서 매우 유사한 두 가지 P3 색상을 구별하기 어려울 수 있습니다.
>



display. Gradients that use P3 colors can also sometimes appear clipped on sRGB displays. To avoid these issues and to
> 진열하다 P3 색상을 사용하는 그라데이션은 sRGB 디스플레이에 잘린 것처럼 보일 수도 있다. 이러한 문제를 방지하고 다음을 수행합니다.
>



ensure visual fidelity on both wide color and sRGB displays, you can use the asset catalog of your Xcode project to
> 넓은 색상과 sRGB 디스플레이 모두에서 시각적 충실도를 보장합니다. Xcode 프로젝트의 자산 카탈로그를 사용하여
>



provide different versions of images and colors for each color space.
> 각 색 공간에 대해 서로 다른 버전의 이미지와 색상을 제공합니다.
>




To learn more, see [How to start designing assets in Display P3](https://developer.apple.com/news/?id=5cda5ipr).
> 자세한 내용은 디스플레이 P3에서 자산 설계를 시작하는 방법을 참조하십시오.
>




# **Platform considerations**

# **iOS, iPadOS**

iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary,
> iOS는 두 세트의 동적 배경색을 정의한다 - 시스템과 그룹 - 각각 기본, 보조,
>



and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background
> 그리고 정보의 계층 구조를 전달하는 데 도움이 되는 3차 변종. 일반적으로 그룹화된 배경을 사용합니다.
>



colors ([systemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/3173145-systemgroupedbackground)
, [secondarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/3173138-secondarysystemgroupedbackground)
,
and [tertiarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/3173155-tertiarysystemgroupedbackground))
when you have a grouped table view; otherwise, use the system set of background
> 그룹화된 테이블 보기가 있는 경우; 그렇지 않으면 배경의 시스템 세트를 사용합니다.
>



colors ([systemBackground](https://developer.apple.com/documentation/uikit/uicolor/3173140-systembackground)
, [secondarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/3173137-secondarysystembackground)
,
and [tertiarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/3173154-tertiarysystembackground))
.

With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:
> 두 배경색 집합 모두 일반적으로 변형을 사용하여 다음과 같은 방식으로 계층을 나타냅니다.
>




- Primary for the overall view
- >  전체 보기에 대한 기본 설정

- Secondary for grouping content or elements within the overall view
- >  전체 보기 내에서 내용 또는 요소를 그룹화하기 위한 보조

- Tertiary for grouping content or elements within secondary elements
- >  2차 요소 내에서 내용 또는 요소를 그룹화하기 위한 3차


For foreground content, iOS defines the following dynamic colors:
> 포그라운드 콘텐츠의 경우 iOS는 다음과 같은 동적 색상을 정의한다.
>




# **macOS**

macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color
> macOS는 다음과 같은 동적 시스템 색상을 정의합니다(표준 색상의 개발자 팔레트에서도 볼 수 있습니다).
>



panel):

### **App accent colors**

Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection
> macOS 11부터 액센트 색상을 지정하여 앱의 단추 모양과 선택 항목을 사용자 지정할 수 있습니다.
>



highlighting, and sidebar icons. The system applies your accent color when the current value in General > Accent color
> 강조 표시 및 사이드바 아이콘. 현재 값이 General(일반) > Accent(액센트) 색상일 때 시스템이 액센트 색상을 적용합니다.
>



settings is *multicolor*.

![https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/app-accent-colors-podcasts_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/app-accent-colors-podcasts_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/app-accent-colors-podcasts-preferences_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/app-accent-colors-podcasts-preferences_2x.png)

If people set their accent color setting to a value other than multicolor, the system applies their chosen color to the
> 만약 사람들이 그들의 악센트 색상 설정을 멀티컬러 이외의 값으로 설정한다면, 시스템은 그들이 선택한 색상을
>



relevant items throughout your app, replacing your accent color. The exception is a sidebar icon that uses a fixed color
> 앱 전체에서 관련 항목을 선택하여 액센트 색상을 대체합니다. 고정된 색상을 사용하는 사이드바 아이콘은 예외입니다.
>



you specify. Because a fixed-color sidebar icon uses a specific color to provide meaning, the system doesn’t override
> 당신이 지정하세요. 고정 색상 사이드바 아이콘은 의미를 제공하기 위해 특정 색상을 사용하기 때문에 시스템이 재정의되지 않습니다.
>



its color when people change the value of accent color settings. For guidance,
> 사람들이 액센트 색상 설정의 값을 변경할 때 그것의 색상. 안내를 위해,
>



see [Sidebars](../components/navigation-and-search/sidebars).

![https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/fixed-color-orange_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/fixed-color-orange_2x.png)

The iCloud glyph remains teal, even when the other glyphs use orange.
> 아이클라우드 글리프는 다른 글리프가 오렌지를 사용하더라도 스틸로 남아 있다.
>




# **tvOS**

**Consider choosing a limited color palette that coordinates with your app logo.** Subtle use of color can help you
> 당신의 앱 로고와 어울리는 제한된 색상 팔레트를 선택하는 것을 고려해보세요. 미묘한 색의 사용은 당신을 도울 수 있다.
>



communicate your brand while deferring to the content.
> 내용을 고려하면서 브랜드를 전달합니다.
>




**Avoid using only color to indicate focus.** Subtle scaling and responsive animation are the primary ways to denote
> 초점을 나타내기 위해 색상만 사용하지 마십시오. 미묘한 스케일링과 반응성 애니메이션은 다음과 같은 주요 방법입니다.
>



interactivity when an element is in focus.
> 요소가 포커스에 있을 때 상호 작용.
>




# **watchOS**

**Use pure black for your app’s background color.** Pure black — that is, #000000 hex — blends seamlessly with the Apple
> 앱의 배경색에 순검색을 사용합니다. 순수 블랙(즉, 00000000 헥스)은 Apple과 완벽하게 혼합됩니다.
>



Watch bezel and creates the illusion of an edgeless screen.
> 베젤을 보고 가장자리가 없는 화면의 착각을 일으킨다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/color-black-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/color/images/color-black-background_2x.png)

**Recognize that people might prefer graphic complications to use tinted mode instead of full color.** The system can
> 사람들은 전체 색상 대신 색조 모드를 사용하기 위해 그래픽 합병증을 선호할 수 있다는 것을 인식한다. 시스템은 할 수 있다.
>



use a single color that’s based on the wearer’s selected color in a graphic complication’s images, gauges, and text. For
> 그래픽 합병증의 이미지, 게이지 및 텍스트에서 착용자가 선택한 색상을 기반으로 하는 단일 색상을 사용합니다. 위해서
>



guidance,
see [Complications](../components/system-experiences/complications)
.

# **Specifications**

# **iOS, iPadOS**

### **System colors (iOS)**

• [Default](../foundations/color#)
• [Accessible](../foundations/color#)


| Light            | Dark              | Name   | SwiftUI API                                                                          |
|------------------|-------------------|--------|--------------------------------------------------------------------------------------|
| R 255 G 59 B 48  | R 255 G 69 B 58   | Red    | [systemRed](https://developer.apple.com/documentation/swiftui/color/red-r0xf)        |
| R 255 G 149 B 0  | R 255 G 159 B 10  | Orange | [systemOrange](https://developer.apple.com/documentation/swiftui/color/orange-82f82) |
| R 255 G 204 B 0  | R 255 G 214 B 10  | Yellow | [systemYellow](https://developer.apple.com/documentation/swiftui/color/yellow-7dwbr) |
| R 52 G 199 B 89  | R 48 G 209 B 88   | Green  | [systemGreen](https://developer.apple.com/documentation/swiftui/color/green-w7ed)    |
| R 0 G 199 B 190  | R 102 G 212 B 207 | Mint   | [systemMint](https://developer.apple.com/documentation/swiftui/color/mint-35bmu)     |
| R 48 G 176 B 199 | R 64 G 200 B 224  | Teal   | [systemTeal](https://developer.apple.com/documentation/swiftui/color/teal-7u2cz)     |
| R 50 G 173 B 230 | R 100 G 210 B 255 | Cyan   | [systemCyan](https://developer.apple.com/documentation/swiftui/color/cyan-7osri)     |
| R 0 G 122 B 255  | R 10 G 132 B 255  | Blue   | [systemBlue](https://developer.apple.com/documentation/swiftui/color/blue-8buzr)     |
| R 88 G 86 B 214  | R 94 G 92 B 230   | Indigo | [systemIndigo](https://developer.apple.com/documentation/swiftui/color/indigo-7talx) |
| R 175 G 82 B 222 | R 191 G 90 B 242  | Purple | [systemPurple](https://developer.apple.com/documentation/swiftui/color/purple-8yxzw) |
| R 255 G 45 B 85  | R 255 G 55 B 95   | Pink   | [systemPink](https://developer.apple.com/documentation/swiftui/color/pink-49kdx)     |
| R 162 G 132 B 94 | R 172 G 142 B 104 | Brown  | [systemBrown](https://developer.apple.com/documentation/swiftui/color/brown-59e5a)   |

### **System gray colors (iOS)**

• [Default](../foundations/color#)
• [Accessible](../foundations/color#)

| Light             | Dark              | Name     | UIKit API                                                                                  |
|-------------------|-------------------|----------|--------------------------------------------------------------------------------------------|
| R 142 G 142 B 147 | R 142 G 142 B 147 | Gray     | [systemGray](https://developer.apple.com/documentation/swiftui/color/gray-7dqon)           |
| R 174 G 174 B 178 | R 99 G 99 B102    | Gray (2) | [systemGray2](https://developer.apple.com/documentation/uikit/uicolor/3255071-systemgray2) |
| R 199 G 199 B 204 | R 72 G 72 B 74    | Gray (3) | [systemGray3](https://developer.apple.com/documentation/uikit/uicolor/3255072-systemgray3) |
| R 209G 209B 214   | R 58 G 58 B 60    | Gray (4) | [systemGray4](https://developer.apple.com/documentation/uikit/uicolor/3255073-systemgray4) |
| R 229 G 229 B 234 | R 44 G 44 B 46    | Gray (5) | [systemGray5](https://developer.apple.com/documentation/uikit/uicolor/3255074-systemgray5) |
| R 242 G 242 B 247 | R 28 G 28 B 30    | Gray (6) | [systemGray6](https://developer.apple.com/documentation/uikit/uicolor/3255075-systemgray6) |

# **macOS**

### **System colors (macOS)**

• [Default](../foundations/color#)
• [Vibrant](../foundations/color#)
• [Accessible](../foundations/color#)
• [Accessible + Vibrant](../foundations/color#)

| Aqua              | Dark              | Name   | SwiftUI API                                                                               |
|-------------------|-------------------|--------|-------------------------------------------------------------------------------------------|
| R 255 G 59 B 48   | R 255 G 69 B 58   | Red    | [systemRedColor](https://developer.apple.com/documentation/swiftui/color/red-r0xf)        |
| R 255 G 149 B 0   | R 255 G 159 B 10  | Orange | [systemOrangeColor](https://developer.apple.com/documentation/swiftui/color/orange-82f82) |
| R 255 G 204 B 0   | R 255 G 214 B 10  | Yellow | [systemYellowColor](https://developer.apple.com/documentation/swiftui/color/yellow-7dwbr) |
| R 40 G 205 B 65   | R 50 G 215 B 75   | Green  | [systemGreenColor](https://developer.apple.com/documentation/swiftui/color/green-w7ed)    |
| R 0 G 199 B 190   | R 102 G 212 B 207 | Mint   | [systemMintColor](https://developer.apple.com/documentation/swiftui/color/mint-35bmu)     |
| R 89 G 173 B 196  | R 106 G 196 B 220 | Teal   | [systemTealColor](https://developer.apple.com/documentation/swiftui/color/teal-7u2cz)     |
| R 85 G 190 B 240  | R 90 G 200 B 245  | Cyan   | [systemCyanColor](https://developer.apple.com/documentation/swiftui/color/cyan-7osri)     |
| R 0 G 122 B 255   | R 10 G 132 B 255  | Blue   | [systemBlueColor](https://developer.apple.com/documentation/swiftui/color/blue-8buzr)     |
| R 88 G 86 B 214   | R 94 G 92 B 230   | Indigo | [systemIndigoColor](https://developer.apple.com/documentation/swiftui/color/indigo-7talx) |
| R 175G 82 B 222   | R 191 G 90 B 242  | Purple | [systemPurpleColor](https://developer.apple.com/documentation/swiftui/color/purple-8yxzw) |
| R 255 G 45 B 85   | R 255 G 55 B 95   | Pink   | [systemPinkColor](https://developer.apple.com/documentation/swiftui/color/pink-49kdx)     |
| R 162 G 132 B 94  | R 172 G 142 B 104 | Brown  | [systemBrownColor](https://developer.apple.com/documentation/swiftui/color/brown-59e5a)   |
| R 142 G 142 B 147 | R 152 G 152 B 157 | Gray   | [systemGrayColor](https://developer.apple.com/documentation/swiftui/color/gray-7dqon)     |

# **watchOS**

### **System colors (watchOS)**

| Color | Use for... | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | label |
| Secondary label | A text label that contains secondary content. | secondaryLabel |
| Tertiary label | A text label that contains tertiary content. | tertiaryLabel |
| Quaternary label | A text label that contains quaternary content. | quaternaryLabel |
| Placeholder text | Placeholder text in controls or text views. | placeholderText |
| Separator | A separator that allows some underlying content to be visible. | separator |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | opaqueSeparator |
| Link | Text that functions as a link. | link |

| Color | Use for... | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | alternateSelectedControlTextColor |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | alternatingContentBackgroundColors |
| Control accent | The accent color selected by the user in System Settings. | controlAccent |
| Control background color | The background of a large interface element, such as a browser or table. | controlBackgroundColor |
| Control color | The surface of a control. | controlColor |
| Control text color | The text of a control that is enabled. | controlTextColor |
| Current control tint | The system-defined control tint. | currentControlTint |
| Disabled control text color | The text of a control that’s disabled. | disabledControlTextColor |
| Find highlight color | The color of a find indicator. | findHighlightColor |
| Grid color | The gridlines of an interface element, such as a table. | gridColor |
| Header text color | The text of a header cell in a table. | headerTextColor |
| Highlight color | The virtual light source onscreen. | highlightColor |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | keyboardFocusIndicatorColor |
| Label color | The text of a label containing primary content. | labelColor |
| Link color | A link to other content. | linkColor |
| Placeholder text color | A placeholder string in a control or text view. | placeholderTextColor |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | quaternaryLabelColor |
| Scrubber textured background color | The background of a scrubber in the Touch Bar. For guidance, see Touch Bar > Visual Design > Color. | scrubberTexturedBackgroundColor |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | secondaryLabelColor |
| Selected content background color | The background for selected content in a key window or view. | selectedContentBackgroundColor |
| Selected control color | The surface of a selected control. | selectedControlColor |
| Selected control text color | The text of a selected control. | selectedControlTextColor |
| Selected menu item text color | The text of a selected menu. | selectedMenuItemTextColor |
| Selected text background color | The background of selected text. | selectedTextBackgroundColor |
| Selected text color | The color for selected text. | selectedTextColor |
| Separator color | A separator between different sections of content. | separatorColor |
| Shadow color | The virtual shadow cast by a raised object onscreen. | shadowColor |
| Tertiary label color | The text of a label of lesser importance than a secondary label, such as a label used to represent disabled text. | tertiaryLabelColor |
| Text background color | The background color behind text. | textBackgroundColor |
| Text color | The text in a document. | textColor |
| Under page background color | The background behind a document’s content. | underPageBackgroundColor |
| Unemphasized selected content background color | The selected content in a non-key window or view. | unemphasizedSelectedContentBackgroundColor |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | unemphasizedSelectedTextBackgroundColor |
| Unemphasized selected text color | Selected text in a non-key window or view. | unemphasizedSelectedTextColor |
| Window background color | The background of a window. | windowBackgroundColor |
| Window frame text color | The text in the window’s title bar area. | windowFrameTextColor |

| Values | Name | SwiftUI API |
| --- | --- | --- |
| R 255G 59B 48 | Red | systemRed |
| R 255G 149B 0 | Orange | systemOrange |
| R 255G 230B 32 | Yellow | systemYellow |
| R 4G 222B 113 | Green | systemGreen |
| R 102G 212B 207 | Mint | systemMint |
| R 106G 196B 220 | Teal | systemTeal |
| R 90G 200B 250 | Cyan | systemCyan |
| R 32G 148B 250 | Blue | systemBlue |
| R 120G 122B 255 | Indigo | systemIndigo |
| R 191G 90B 242 | Purple | systemPurple |
| R 250G 17B 79 | Pink | systemPink |
| R 172G 142B 104 | Brown | systemBrown |
| R 155G 160B 170 | Gray | systemGray |

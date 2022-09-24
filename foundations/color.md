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




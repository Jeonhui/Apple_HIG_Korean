# **[components-presentation] panels**

## In a macOS app, a panel typically floats above other open windows providing supplementary controls, options, or information related to the active window or current selection.
> macOS 앱에서 패널은 일반적으로 열려 있는 다른 창 위에 떠서 활성 창 또는 현재 선택과 관련된 추가 제어, 옵션 또는 정보를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/panel-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/panel-intro-dark_2x.png)

In general, a panel has a less prominent appearance than an app’s [main window](../components/presentation/windows). When the situation calls for it, a panel can also use a dark, translucent style to enable a heads-up display (or *HUD*) experience.
> 일반적으로 패널은 앱의 메인 창보다 덜 두드러지게 나타난다. 상황이 필요할 때 패널은 어둡고 반투명한 스타일을 사용하여 헤드업 디스플레이(HUD) 경험을 가능하게 할 수도 있습니다.
>




When your app runs in other platforms, consider using a modal view to present supplementary content that’s relevant to the current task or selection. For guidance, see [Modality](../patterns/modality).
> 앱이 다른 플랫폼에서 실행되는 경우 모달 뷰를 사용하여 현재 작업 또는 선택과 관련된 보충 콘텐츠를 표시하는 것을 고려해 보십시오. 자세한 내용은 촬영장비를 참조하십시오.
>




# **Best practices**

**Use a panel to give people quick access to important controls or information related to the content they’re working with.** For example, you might use a panel to provide controls or settings that affect the selected item in the active document or window.
> 패널을 사용하여 작업 중인 콘텐츠와 관련된 중요한 컨트롤 또는 정보에 빠르게 액세스할 수 있습니다. 예를 들어 패널을 사용하여 활성 문서 또는 창에서 선택한 항목에 영향을 주는 컨트롤 또는 설정을 제공할 수 있습니다.
>




**Consider using a panel to present inspector functionality.** An *inspector*displays the details of the currently selected item, automatically updating its contents when the item changes or when people select a new item. In contrast, if you need to present an *Info* window — which always maintains the same contents, even when the selected item changes — use a regular window, not a panel. Depending on the layout of your app, you might also consider using a [split view](../components/layout-and-organization/split-views) pane to present an inspector.
> 패널을 사용하여 검사기 기능을 표시하는 것을 고려해 보십시오. 검사기는 현재 선택된 항목의 세부 정보를 표시하여 항목이 변경되거나 사용자가 새 항목을 선택할 때 내용을 자동으로 업데이트합니다. 반면, 선택한 항목이 변경되더라도 항상 동일한 내용을 유지하는 정보 창을 표시해야 하는 경우 패널이 아닌 일반 창을 사용합니다. 앱의 레이아웃에 따라 분할 보기 창을 사용하여 검사기를 표시하는 것도 고려할 수 있습니다.
>




**Prefer simple adjustment controls in a panel.** As much as possible, avoid including controls that require typing text or selecting items to act upon because these actions can require multiple steps. Instead, consider using controls like sliders and steppers because these components can give people more direct control.
> 패널의 간단한 조정 컨트롤을 선호합니다. 텍스트를 입력하거나 작업할 항목을 선택해야 하는 컨트롤은 여러 단계가 필요할 수 있으므로 가능한 한 포함하지 마십시오. 대신, 슬라이더와 스테퍼와 같은 조정기를 사용하는 것을 고려하십시오. 왜냐하면 이러한 구성 요소는 사람들에게 더 직접적인 조정기를 제공할 수 있기 때문입니다.
>




**Write a brief title that describes the panel’s purpose.** Because a panel often floats above other open windows in your app, it needs a title bar so people can position it where they want. Create a short title using a noun — or a noun phrase with [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) — that can help people recognize the panel onscreen. For example, macOS provides familiar panels titled “Fonts” and “Colors,” and many apps use the title “Inspector.”
> 패널의 목적을 설명하는 간단한 제목을 작성합니다. 패널이 종종 앱의 다른 열린 창 위에 뜨기 때문에 사람들이 원하는 곳에 패널을 배치할 수 있도록 제목 표시줄이 필요합니다. 사용자가 화면의 패널을 인식하는 데 도움이 되는 명사 또는 제목 스타일 대문자가 있는 명사구를 사용하여 짧은 제목을 만듭니다. 예를 들어, macOS는 "Fonts"와 "Colors"라는 친숙한 패널을 제공하며, 많은 앱들은 "Inspector"라는 제목을 사용한다.
>




**Show and hide panels appropriately.** When your app becomes active, bring all of its open panels to the front, regardless of which window was active when the panel opened. When your app is inactive, hide all of its panels.
> 패널을 적절하게 표시하고 숨깁니다. 앱이 활성화되면 패널을 열 때 활성화된 창에 관계없이 열려 있는 모든 패널을 앞으로 가져옵니다. 앱이 비활성화되면 해당 패널을 모두 숨깁니다.
>




**Avoid including panels in the Window menu’s documents list.** It’s fine to include commands for showing or hiding panels in the [Window menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/#window-menu), but panels aren’t documents or standard app windows, and they don’t belong in the Window menu’s list.
> 창 메뉴의 문서 목록에 패널을 포함하지 않도록 합니다. 창 메뉴에 패널을 표시하거나 숨기기 위한 명령을 포함하는 것은 좋지만 패널은 문서나 표준 앱 창이 아니며 창 메뉴의 목록에 속하지 않습니다.
>




**In general, disable the minimize button in a panel.** People don’t usually need to minimize a panel, because it displays only when needed and disappears when the app is inactive.
> 패널에서 최소화 단추를 사용하지 않도록 설정하십시오. 패널은 필요할 때만 표시되고 앱이 비활성 상태일 때 사라지므로 일반적으로 사용자가 패널을 최소화할 필요가 필요하지 않습니다.
>




**Refer to panels by title in your interface and in help documentation.** In menus, use the panel’s title without including the term *panel*: for example, “Show Fonts,” “Show Colors,” and “Show Inspector.” In help documentation, it can be confusing to introduce “panel” as a different type of window, so it’s generally best to refer to a panel by its title or — when it adds clarity — by appending *window* to the title. For example, the title “Inspector” often supplies enough context to stand on its own, whereas it can be clearer to use “Fonts window” and “Colors window” instead of just “Fonts” and “Colors.”
> 인터페이스 및 도움말 설명서에서 제목별 패널을 참조하십시오. 메뉴에서 패널의 제목을 포함하지 않고 "글꼴 표시", "색상 표시" 및 "검사기 표시"와 같이 사용하십시오. 도움말 설명서에서 "패널"을 다른 유형의 창으로 소개하는 것은 혼동될 수 있으므로 일반적으로 제목으로 패널을 참조하거나 제목에 창을 추가하여 명확성을 추가하는 것이 가장 좋습니다. 예를 들어, "인스펙터"라는 제목은 자주 스스로 설 수 있는 충분한 컨텍스트를 제공하지만, "글꼴"과 "색상" 대신 "글꼴 창"과 "색상 창"을 사용하는 것이 더 명확할 수 있다.
>




# **HUD-style panels**

A HUD-style panel serves the same function as a standard panel, but its appearance is darker and translucent. HUDs work well in apps that focus on highly visual content or that provide an immersive experience, such as media editing or a full-screen slide show. For example, QuickTime Player uses a HUD to display inspector information without obstructing too much content.
> HUD 스타일의 패널은 표준 패널과 동일한 기능을 수행하지만 외관은 더 어둡고 반투명합니다. HUD는 고도로 시각적인 콘텐츠에 초점을 맞추거나 미디어 편집 또는 전체 화면 슬라이드 쇼와 같이 몰입감 있는 경험을 제공하는 앱에서 잘 작동합니다. 예를 들어 QuickTime Player는 HUD를 사용하여 너무 많은 콘텐츠를 방해하지 않고 검사기 정보를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/panels/images/hud-style-panel_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/panels/images/hud-style-panel_2x.png)

**Prefer standard panels.** People can be distracted or confused by a HUD when there’s no logical reason for its presence. Also, a HUD might not match the current appearance setting. In general, use a HUD only:
> 표준 패널을 선호합니다. 사람들은 HUD의 존재에 대한 논리적인 이유가 없을 때 HUD에 의해 주의가 산만해지거나 혼란스러울 수 있습니다. 또한 HUD가 현재 모양 설정과 일치하지 않을 수 있습니다. 일반적으로 HUD만 사용합니다.
>




- In a media-oriented app that focuses on movies, photos, or slides
- >  동영상, 사진 또는 슬라이드에 초점을 맞춘 미디어 지향 앱에서

- When a standard panel would obscure essential content
- >  표준 패널이 필수 내용을 모호하게 만드는 경우

- When you don’t need to include controls — with the exception of the disclosure triangle, most system-provided controls don’t match a HUD’s appearance.
- >  공개 삼각형을 제외하고 대부분의 시스템 제공 컨트롤은 HUD의 모양과 일치하지 않습니다.


**Maintain one panel style when your app switches modes.** For example, if you use a HUD when your app is in full-screen mode, prefer maintaining the HUD style when people take your app out of full-screen mode.
> 앱이 모드를 전환할 때 하나의 패널 스타일을 유지합니다. 예를 들어, 앱이 전체 화면 모드에 있을 때 HUD를 사용하는 경우, 사람들이 전체 화면 모드를 종료할 때 HUD 스타일을 유지하는 것을 선호합니다.
>




**Use color sparingly in HUDs.** Too much color in the dark appearance of a HUD can be distracting. Often, you need only small amounts of high-contrast color to highlight important information in a HUD.
> HUD에서는 색을 적게 사용하십시오. HUD의 어두운 모양에서 너무 많은 색을 사용하면 주의가 산만해질 수 있습니다. 종종 HUD에서 중요한 정보를 강조하기 위해 적은 양의 고대비 색상만 필요합니다.
>




**Keep HUDs small.** HUDs are designed to be unobtrusively useful, so letting them grow too large defeats their primary purpose. Don’t let a HUD obscure the content it adjusts, and make sure it doesn’t compete with the content for people’s attention.
> HUD를 작게 유지하십시오. HUD는 눈에 띄지 않게 유용하도록 설계되었으므로 너무 크게 성장하도록 하는 것이 주된 목적을 방해합니다. HUD가 조정하는 콘텐츠를 흐리게 하지 말고 사람들의 관심을 끌기 위해 콘텐츠와 경쟁하지 않도록 하십시오.
>




For developer guidance, see [NSWindowStyleMaskHUDWindow](https://developer.apple.com/documentation/appkit/nswindowstylemask/nswindowstylemaskhudwindow).

# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*
> iOS, iPadOS, tvOS 또는 watch에서 지원되지 않음운영 체제
>




# **[inputs] touch-bar**

## The Touch Bar is a Retina display and input device located above the keyboard on supported MacBook Pro models.
> 터치 바는 지원되는 맥북 프로 모델의 키보드 위에 위치한 레티나 디스플레이 및 입력 장치입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-bar-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-bar-intro_2x.png)

Dynamic controls in the Touch Bar let people interact with content on the main screen and offer quick access to system-level and app-specific functionality based on the current context. For example, when people type text in a document, the Touch Bar could include controls for adjusting the font style and size. Or when viewing a location on a map, the Touch Bar could offer quick, one-tap access to nearby points of interest.
> 터치 바의 동적 컨트롤을 사용하면 메인 화면의 콘텐츠와 상호 작용할 수 있으며 현재 컨텍스트를 기반으로 시스템 수준 및 앱별 기능에 빠르게 액세스할 수 있습니다. 예를 들어, 사람들이 문서에 텍스트를 입력할 때 터치 바에는 글꼴 스타일과 크기를 조정하기 위한 컨트롤이 포함될 수 있습니다. 또는 지도에서 위치를 볼 때 터치 바를 사용하면 근처의 관심 지점에 한 번만 빠르게 액세스할 수 있습니다.
>




The following guidelines can help you provide a Touch Bar experience that people appreciate. For developer guidance, see [NSTouchBar](https://developer.apple.com/documentation/appkit/nstouchbar) and [Xcode Help](https://help.apple.com/xcode).
> 다음 지침은 사람들이 높이 평가하는 터치 바 경험을 제공하는 데 도움이 될 수 있습니다. 개발자 지침은 NSTouchBar 및 Xcode 도움말을 참조하십시오.
>




A Touch ID sensor to the right of the Touch Bar supports fingerprint authentication for logging into the computer and approving App Store and Apple Pay purchases. On devices that include the Touch Bar (2nd generation), a physical Esc (Escape) key appears to the left of the Touch Bar.
> 터치 바 오른쪽에 있는 터치 ID 센서는 컴퓨터에 로그인하고 App Store 및 Apple Pay 구매를 승인하기 위한 지문 인증을 지원합니다. 터치 바(2세대)가 포함된 장치에서는 터치 바 왼쪽에 물리적 Esc(탈출) 키가 나타납니다.
>




By default, the right side of the Touch Bar displays an expandable region called the *Control Strip* that includes controls for performing system-level tasks such as invoking Siri, adjusting the brightness of the main display, and changing the volume. You can place app-specific controls in the *app region*to the left of the Control Strip. In Touch Bar (1st generation), an Esc button or other system-provided button may appear to the left of the app region, depending on the context.
> 기본적으로 터치 바의 오른쪽에는 Siri 호출, 메인 디스플레이 밝기 조정 및 볼륨 변경과 같은 시스템 수준 작업을 수행하기 위한 컨트롤이 포함된 Control Strip(제어 스트립)이라는 확장 가능 영역이 표시됩니다. 제어 스트립의 왼쪽에 있는 앱 영역에 앱별 컨트롤을 배치할 수 있습니다. 터치 바(1세대)에서는 상황에 따라 앱 영역 왼쪽에 Esc 버튼 또는 기타 시스템 제공 버튼이 나타날 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-overview_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-overview_2x.png)

Touch Bar (2nd generation)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-overview_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-overview_2x.png)

Touch Bar (1st generation)

People can configure the Touch Bar to suit their needs. For example, people can remove items from, or hide the Control Strip completely, in which case only the controls in the app region and the system button remain. Alternatively, people can hide the app region to view an expanded Control Strip.
> 사용자는 필요에 따라 터치 바를 구성할 수 있습니다. 예를 들어, 사람들은 컨트롤 스트립에서 항목을 제거하거나 완전히 숨길 수 있으며, 이 경우 앱 영역과 시스템 버튼의 컨트롤만 남아 있습니다. 또는 앱 영역을 숨겨 확장된 제어 스트립을 볼 수 있습니다.
>




You can support additional customization within the app region by letting people add and remove items.
> 사용자가 항목을 추가 및 제거할 수 있도록 하여 앱 영역 내에서 추가 사용자 지정을 지원할 수 있습니다.
>




**In general, let people customize your app’s Touch Bar experience.**Provide reasonable defaults for important and commonly used functions, but let people make adjustments to support their individual working styles.
> 일반적으로, 사람들이 당신의 앱의 터치바 경험을 사용자 정의하도록 한다.중요하고 일반적으로 사용되는 기능에 대해 합리적인 기본값을 제공하되, 사람들이 각자의 작업 스타일을 지원하도록 조정할 수 있도록 한다.
>




**Provide alternative text labels for your Touch Bar controls.** By providing alternative text for your controls in the Touch Bar, VoiceOver can audibly describe the controls, making navigation easier for people with visual disabilities (for guidance, see [Accessibility](../foundations/accessibility)). Also create labels for any customizable Touch Bar controls that you provide so VoiceOver can describe these controls on the customization screen.
> 터치 바 컨트롤에 대체 텍스트 레이블을 제공합니다. 터치 바에서 컨트롤에 대한 대체 텍스트를 제공함으로써 VoiceOver는 컨트롤을 청각적으로 설명하여 시각 장애가 있는 사람들이 쉽게 탐색할 수 있도록 합니다(참고 사항은 접근성 참조). 또한 VoiceOver가 사용자 지정 화면에서 이러한 컨트롤을 설명할 수 있도록 제공하는 사용자 지정 가능한 터치 바 컨트롤에 대한 레이블을 만듭니다.
>




# **Gestures**

People use a subset of the standard gestures to interact with the Touch Bar.
> 사람들은 터치 바와 상호 작용하기 위해 표준 제스처의 일부를 사용한다.
>




# **Tap**

People tap to activate a control, like a button, or select an item, such as an emoji, a color, or a segment in a segmented control.
> 사람들은 버튼과 같은 컨트롤을 활성화하거나 세그먼트화된 컨트롤의 이모지, 색상 또는 세그먼트와 같은 항목을 선택합니다.
>




# **Touch and hold**

A touch and hold gesture initiates a control’s secondary action. In Mail, for example, tapping the Flag button adds a flag to a message, but touching and holding the button reveals a modal view that lets people change the flag’s color.
> 터치 및 홀드 제스처는 컨트롤의 보조 동작을 시작합니다. 예를 들어 메일에서 플래그 단추를 누르면 메시지에 플래그가 추가되지만 단추를 길게 누르면 플래그의 색상을 변경할 수 있는 모달 보기가 표시됩니다.
>




# **Horizontal swipe or pan**

People use a horizontal swipe or pan to drag an element, like a slider thumb, or navigate through content, such as a list of dates or a group of photos in a scrubber.
> 슬라이더 엄지와 같은 요소를 끌거나 스크러버에 있는 날짜 목록 또는 사진 그룹과 같은 내용을 탐색하기 위해 수평 스와이프 또는 팬을 사용합니다.
>




# **Multi-Touch**

Although the Touch Bar supports Multi-Touch gestures — like a pinch — such gestures can be cumbersome for people to perform. In general, it’s best to use Multi-Touch gestures sparingly.
> 터치 바는 핀치와 같은 멀티 터치 제스처를 지원하지만 이러한 제스처는 사용자가 수행하는 데 번거로울 수 있습니다. 일반적으로 멀티터치 제스처는 적게 사용하는 것이 가장 좋습니다.
>




# **Best practices**

Keep the following guidance in mind as you design your app’s Touch Bar interfaces.
> 앱의 터치 바 인터페이스를 설계할 때 다음 지침을 기억하십시오.
>




**Make the Touch Bar relevant to the current context on the main screen.**Identify the different contexts within your app. Then, consider how you can expose varying levels of functionality based on how your app is used.
> 터치 바를 메인 화면의 현재 컨텍스트와 관련되게 합니다.앱 내의 다양한 컨텍스트를 식별합니다. 그런 다음 앱 사용 방법에 따라 다양한 수준의 기능을 노출할 수 있는 방법을 고려해 보십시오.
>




**Use the Touch Bar as an extension of the keyboard and trackpad, not as a display.** Although the Touch Bar is a screen, its primary function is to serve as an input device — not a secondary display. People may glance at the Touch Bar to locate or use a control, but their primary focus is the main screen. The Touch Bar shouldn’t display alerts, messages, scrolling content, static content, or anything else that distracts people from the main screen.
> 터치 바는 디스플레이가 아니라 키보드 및 트랙패드의 확장으로 사용합니다. 터치 바는 화면이지만 기본 기능은 보조 디스플레이가 아닌 입력 장치 역할을 하는 것입니다. 사람들은 컨트롤을 찾거나 사용하기 위해 터치 바를 힐끗 볼 수 있지만, 그들의 주된 초점은 메인 화면이다. 터치 바에는 알림, 메시지, 스크롤 콘텐츠, 정적 콘텐츠 또는 기본 화면에서 다른 사용자의 주의를 분산시키는 다른 내용이 표시되지 않아야 합니다.
>




**Strive to match the look of the physical keyboard.** When possible, aim to design Touch Bar controls that resemble the size and color of keys in the physical keyboard.
> 실제 키보드의 모양과 일치하도록 노력하십시오. 가능하면 실제 키보드의 키 크기와 색상과 유사한 터치 바 컨트롤을 설계하는 것을 목표로 합니다.
>




**Avoid making functionality available only in the Touch Bar.** Not all devices have a Touch Bar, and people can disable app controls in the Touch Bar if they choose. Always give people ways to perform tasks using the keyboard or trackpad.
> 모든 장치에 터치 바가 있는 것은 아니며, 원하는 경우 터치 바에서 앱 컨트롤을 사용하지 않도록 설정할 수 있습니다. 항상 키보드 또는 트랙패드를 사용하여 작업을 수행할 수 있는 방법을 제공합니다.
>




**In a full-screen context, consider displaying relevant controls in the Touch Bar.** In full-screen mode, apps often hide onscreen controls and reveal them only when people call for them by, for example, moving the pointer to the top of the screen. If you support full screen, you can use the Touch Bar to give people persistent access to important controls without distracting them from the full-screen experience.
> 전체 화면 컨텍스트에서는 터치 바에 관련 컨트롤을 표시하는 것을 고려해 보십시오. 전체 화면 모드에서 앱은 종종 화면 컨트롤을 숨기고 포인터를 화면 맨 위로 이동하여 사람들이 요청할 때만 표시합니다. 전체 화면을 지원하는 경우 터치 막대를 사용하여 사람들이 전체 화면 환경에서 중요한 컨트롤에 집중하지 않고 지속적으로 액세스할 수 있도록 할 수 있습니다.
>




**Prefer controls that produce immediate results.** Ideally, Touch Bar controls give people quick ways to perform actions that would otherwise require extra time spent clicking controls or choosing from menus. Minimize Touch Bar controls that present additional choices, such as popovers. For guidance, see [Controls and views](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#controls-and-views).
> 터치 바 컨트롤을 사용하면 컨트롤을 클릭하거나 메뉴에서 선택하는 데 시간이 더 걸리는 작업을 신속하게 수행할 수 있습니다. 팝업과 같은 추가 선택사항을 제공하는 터치 바 컨트롤을 최소화합니다. 자세한 내용은 컨트롤 및 보기를 참조하십시오.
>




**Be responsive to Touch Bar interactions.** Even when your app is busy doing work or updating the main screen, respond instantly when people use a Touch Bar control.
> 터치 바 상호 작용에 반응합니다. 앱이 작업을 하거나 기본 화면을 업데이트하는 중인 경우에도 터치 바 컨트롤을 사용할 때 즉시 반응합니다.
>




**When possible, people should be able to start and finish a task in the Touch Bar.** Avoid making people switch to the keyboard or trackpad to complete a task unless the task requires more complex interface controls than the Touch Bar provides.
> 가능하면 터치 바에서 작업을 시작하고 끝낼 수 있어야 합니다. 터치 바에서 제공하는 것보다 더 복잡한 인터페이스 컨트롤이 필요한 경우가 아니면 키보드나 트랙패드로 전환하여 작업을 완료하지 마십시오.
>




**Avoid using the Touch Bar for tasks associated with well-known keyboard shortcuts.** The Touch Bar shouldn’t include controls for tasks such as find, select all, deselect, copy, cut, paste, undo, redo, new, save, close, print, and quit. It also shouldn’t include controls that replicate key-based navigation, such as page up and page down.
> 잘 알려진 바로 가기 키와 관련된 작업에는 터치 막대를 사용하지 마십시오. 터치 막대에는 찾기, 모두 선택, 선택 취소, 복사, 붙여넣기, 실행 취소, 다시 실행, 새로 만들기, 저장, 닫기, 인쇄 및 종료와 같은 작업에 대한 컨트롤이 포함되어 있지 않아야 합니다. 또한 페이지 업 및 페이지 다운과 같은 키 기반 탐색을 복제하는 컨트롤을 포함하지 않아야 합니다.
>




**Accurately reflect the state of a control that appears in both the Touch Bar and on the main screen.** For example, if a button is unavailable on the main screen, it shouldn't be available in the Touch Bar.
> 예를 들어, 기본 화면에서 단추를 사용할 수 없는 경우 터치 표시줄에서 단추를 사용할 수 없는 경우 터치 표시줄과 기본 화면에 모두 표시되는 컨트롤의 상태를 정확하게 반영합니다.
>




**When responding to user interactions, avoid showing the same UI in both the Touch Bar and the main screen.** For example, when people click the onscreen Emoji & Symbols button in a new message window in Mail, they expect the Character Viewer to open on the main screen, not in the Touch Bar. Unless people interact with the same control in both places, avoid distracting people by displaying redundant UI.
> 예를 들어, 사람들이 메일의 새 메시지 창에서 화면의 이모지 및 기호 단추를 클릭하면 문자 뷰어가 터치 모음이 아닌 기본 화면에서 열릴 것으로 예상됩니다. 사람들이 두 장소에서 동일한 컨트롤로 상호 작용하지 않는 한 중복 UI를 표시하여 사람들의 주의를 산만하게 하지 않도록 한다.
>




# **Animation**

**Avoid animation.** The Touch Bar is an extension of the keyboard, and people don’t expect animation in their keyboard. In addition, excessive or gratuitous animation can distract people from their work.
> 터치 바는 키보드의 확장이므로 키보드에서 애니메이션을 기대하지 않습니다. 게다가, 과도하거나 불필요한 애니메이션은 사람들이 그들의 일에서 주의를 산만하게 할 수 있다.
>




# **Color**

**Prefer standard controls and system icons.** The standard controls and system icons already use colors that work well in the Touch Bar. For a list of available system icons, see [Interface icons](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#interface-icons).
> 표준 컨트롤과 시스템 아이콘을 선호합니다. 표준 컨트롤과 시스템 아이콘은 이미 터치 바에서 잘 작동하는 색을 사용합니다. 사용 가능한 시스템 아이콘 목록은 인터페이스 아이콘을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorOne_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorOne_2x.png)

**Use color tastefully and minimally.** In general, make the Touch Bar similar in appearance to the physical keyboard. Monochromatic colors work best. If you must use colors in your controls, do so tastefully and primarily in temporary states. Colors shouldn’t appear overwhelming or out of place.
> 일반적으로 터치 바는 실제 키보드와 모양이 비슷하도록 합니다. 단색 컬러가 가장 잘 어울린다. 컨트롤에서 색상을 사용해야 하는 경우에는 주로 임시 상태에서 맛깔스럽게 사용하십시오. 색상이 압도적으로 보이거나 어울리지 않아야 합니다.
>




**Use color to denote prominence.** Color can draw the eye to important controls. Reserve blue for default controls and red for destructive controls.
> 색상을 사용하여 눈에 띄는 부분을 표시합니다. 색상은 중요한 컨트롤로 눈을 끌 수 있습니다. 기본 컨트롤의 경우 파란색으로, 파괴 컨트롤의 경우 빨간색으로 예약합니다.
>




**If you use color, choose a limited palette that coordinates with your app.** Subtle use of color is one way to communicate your brand.
> 색상을 사용하는 경우 앱과 조화를 이루는 한정된 팔레트를 선택하십시오. 색상의 미묘한 사용은 브랜드를 전달하는 한 가지 방법입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorTwo_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorTwo_2x.png)

**Provide wide color artwork.** The Touch Bar supports a P3 color space that can produce richer, more saturated colors than sRGB. Use the Display P3 color profile at 16 bits per pixel (per channel) and export your artwork in the PNG format. For guidance, see [Color management](https://developer.apple.com/design/human-interface-guidelines/foundations/color#color-management).
> 넓은 컬러 아트워크를 제공합니다. 터치바는 SRGB보다 더 풍부하고 더 포화된 컬러를 생성할 수 있는 P3 컬러 공간을 지원합니다. 디스플레이 P3 색상 프로파일을 픽셀당 16비트(채널당)로 사용하고 아트워크를 PNG 형식으로 내보냅니다. 자세한 내용은 색 관리를 참조하십시오.
>




**TIP**On a Mac that features a wide color display, you can use the system color picker to select and preview P3 colors, and to compare them with sRGB colors.
> 팁넓은 색 디스플레이를 갖춘 Mac에서는 시스템 색 선택기를 사용하여 P3 색을 선택하고 미리 보고 sRGB 색과 비교할 수 있습니다.
>




### **System colors**

macOS offers a range of standard system colors that respond automatically to system white-point changes based on factors such as ambient light and keyboard backlight level.
> macOS는 주변 조도와 키보드 백라이트 레벨과 같은 요소를 기반으로 시스템 화이트포인트 변화에 자동으로 반응하는 다양한 표준 시스템 색상을 제공한다.
>




| Color | API |
| --- | --- |
| Blue | systemBlueColor |
| Brown | systemBrownColor |
| Gray | systemGrayColor |
| Green | systemGreenColor |
| Orange | systemOrangeColor |
| Pink | systemPinkColor |
| Purple | systemPurpleColor |
| Red | systemRedColor |
| Yellow | systemYellowColor |

**Don't replicate system colors.** System color values may fluctuate from release to release and based on various environmental variables. Instead of trying to create custom colors that match the system colors, just use the system colors.
> 시스템 색상을 복제하지 마십시오. 시스템 색상 값은 다양한 환경 변수에 따라 릴리즈마다 변동될 수 있습니다. 시스템 색상과 일치하는 사용자 지정 색상을 만드는 대신 시스템 색상을 사용하십시오.
>




For developer guidance, see [NSColor](https://developer.apple.com/documentation/appkit/nscolor).

### **Dynamic system colors**

macOS defines a range of system colors that dynamically match the color scheme of standard interface controls such as buttons and labels. The following system colors are ideal for use in the Touch Bar.
> macOS는 버튼과 레이블과 같은 표준 인터페이스 컨트롤의 색상 체계와 동적으로 일치하는 시스템 색상 범위를 정의합니다. 다음 시스템 색상은 터치 바에 사용하기에 적합합니다.
>




| Color | Description | API |
| --- | --- | --- |
| Control Color | The system color for the surface of a control. | controlColor |
| Label Color | The system color for the text of a label. | labelColor |
| Secondary Label Color | The system color for label text of lesser importance than labelColor text, for example, a subheading or additional information. | secondaryLabelColor |
| Tertiary Label Color | The system color for label text of lesser importance than secondaryLabelColor, for example, disabled text. | tertiaryLabelColor |
| Quaternary Label Color | The system color for label text of lesser importance than tertiaryLabelColor, for example, disabled text. | quaternaryLabelColor |

# **Layout**

The width of the Touch Bar display differs depending on the device.
> 터치 바 디스플레이의 폭은 장치에 따라 다릅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-total_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-total_2x.png)

Touch Bar (2nd generation)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-total_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-total_2x.png)

Touch Bar (1st generation)

### **Touch Bar areas**

In its standard configuration, the Touch Bar display consists of either two or three areas, depending on the device. The system enforces a 16pt separation between areas.
> 표준 구성에서 터치 바 디스플레이는 장치에 따라 두 개 또는 세 개의 영역으로 구성됩니다. 이 시스템은 영역 간에 16pt의 분리를 시행합니다.
>




The Touch Bar (2nd generation) display contains two areas: the app region and the Control Strip. Although the second generation Touch Bar doesn’t include a system button area, you can display a system button within your app region.
> 터치 바(2세대) 디스플레이에는 앱 영역과 컨트롤 스트립이라는 두 가지 영역이 있습니다. 2세대 터치 바에는 시스템 버튼 영역이 없지만 앱 영역 내에 시스템 버튼을 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-regions_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-regions_2x.png)

The Touch Bar (1st generation) display includes three areas: the system button area, the app region, and the Control Strip.
> 터치 바(1세대) 디스플레이에는 시스템 버튼 영역, 앱 영역 및 제어 스트립의 세 가지 영역이 포함됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-regions_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-regions_2x.png)

| Area | Contains | User configurable? |
| --- | --- | --- |
| Control Strip | System-level controls for performing actions, like initiating Siri or adjusting the volume level. | Yes. People can extend the Control Strip to the full width of the Touch Bar, collapse it to the right side of the Touch Bar, reduce it in size, or hide it entirely. By default, the Control Strip appears in its collapsed state and contains four controls. |
| App region | Your app’s controls. | Yes. People can hide this area entirely. When the Control Strip is visible, the app region has a minimum width of 685pt. |
| System button (available on some models) | A contextually relevant button, like Esc, Cancel, or Done. | No. When present, this area's width is 64pt. In Touch Bar (2nd generation), you can use 8pt spacing to display the relevant button in the app region, where it's disabled by default. |

**Assume that the default Control Strip is visible.** Although people can reconfigure the Control Strip, reduce its size, or hide it completely, don’t rely on the availability of this space for your design.
> 기본 컨트롤 스트립이 표시된다고 가정합니다. 컨트롤 스트립을 재구성하거나, 크기를 줄이거나, 완전히 숨길 수 있지만, 이 공간을 설계에 사용할 수 있는지 여부에 의존하지 마십시오.
>




### **Positioning app controls**

You have several options for adding visual separation between app controls in the Touch Bar.
> 터치 바에서 앱 컨트롤 간에 시각적 분리를 추가할 수 있는 몇 가지 옵션이 있습니다.
>




| Spacing type | Width between controls |
| --- | --- |
| Default | 8pt |
| Small fixed space | 16pt |
| Large fixed space | 32pt |
| Flexible space | Varies to match the available space. |

**Position controls logically and intuitively.** If your app offers a control that persists across different modalities, it can work well to put the control in the left side of the app region. For example, the Compose button in Notes always appears in the far left of the Touch Bar, regardless of whether people are navigating notes, editing a note, or browsing attachments.
> 컨트롤을 논리적이고 직관적으로 배치합니다. 앱이 여러 양식에 걸쳐 지속되는 컨트롤을 제공하는 경우 해당 컨트롤을 앱 영역의 왼쪽에 배치하는 것이 좋습니다. 예를 들어, Notes의 작성 단추는 사용자가 노트를 탐색하는지, 노트를 편집하는지 또는 첨부 파일을 검색하는지 여부에 관계없이 항상 터치 막대의 맨 왼쪽에 나타납니다.
>




On the other hand, primary controls that command people’s attention — such as an alert or the suggested items in the QuickType bar — work best centered in the app region, with secondary options on the left. Consider using the order of controls in your app’s toolbar to inform the order of Touch Bar controls in the app region. When you use consistent control positions in both areas, people can rely on their familiarity with your onscreen controls to help them use your Touch Bar controls.
> 반면에 경고나 QuickType 표시줄의 제안된 항목과 같이 사람들의 주의를 명령하는 기본 컨트롤은 왼쪽에 보조 옵션이 있는 앱 영역을 중심으로 가장 잘 작동합니다. 앱의 도구 모음에서 컨트롤 순서를 사용하여 앱 영역의 터치 바 컨트롤 순서를 알려 보십시오. 두 영역 모두에서 일관된 제어 위치를 사용하면 화면에 표시되는 컨트롤에 익숙해져 있어 터치 바 컨트롤을 사용하는 데 도움이 됩니다.
>




**IMPORTANT**If the order of your Touch Bar controls mirrors the order of controls in your app’s window, make sure to adjust the control order in the app region when your app uses a right-to-left layout.
> 중요 터치 바 컨트롤의 순서가 앱 창의 컨트롤 순서와 일치하는 경우 앱이 오른쪽에서 왼쪽 레이아웃을 사용할 때 앱 영역에서 컨트롤 순서를 조정해야 합니다.
>




**Construct a flexible layout.** The app region varies in width depending on the configuration of the Control Strip and the device, so consider allowing certain controls — such as sliders and scrubbers — to stretch when additional space becomes available.
> 유연한 레이아웃을 구성합니다. 앱 영역은 제어 스트립과 장치의 구성에 따라 너비가 다르므로, 추가 공간을 사용할 수 있을 때 슬라이더 및 스크러버와 같은 특정 컨트롤을 확장할 수 있도록 허용하는 것을 고려해 보십시오.
>




**Strive for consistent spacing.** As much as possible, make controls in the Touch Bar equidistant, except when spacing variations are necessary for clarity or to cluster related controls.
> 일정한 간격을 유지하도록 노력하십시오. 가능한 한 간격 변경이 명확하거나 관련 컨트롤을 클러스터링하기 위해 필요한 경우를 제외하고 터치 바에서 컨트롤을 동일한 거리로 만듭니다.
>




**Use flexible spaces and grouping to aid alignment.** Flexible space between items pushes the items on the left toward the left side of the Touch Bar and the items on the right toward the right side of the Touch Bar. Grouping lets you position multiple controls at once. For example, you can center a control or group by marking it as the principal item in the Touch Bar.
> 정렬에 도움이 되도록 유연한 공간과 그룹화를 사용합니다. 항목 사이의 유연한 공간은 왼쪽의 항목을 터치 바의 왼쪽으로, 오른쪽의 항목을 터치 바의 오른쪽으로 밀어줍니다. 그룹화를 통해 여러 컨트롤을 한 번에 배치할 수 있습니다. 예를 들어 컨트롤 또는 그룹을 터치 막대에서 주 항목으로 표시하여 가운데에 배치할 수 있습니다.
>




**Avoid repositioning controls automatically.** People can become frustrated and confused if a control changes position by itself. If it makes sense in your app, consider letting people customize control positioning.
> 컨트롤의 위치가 자동으로 변경되지 않도록 합니다. 컨트롤이 자동으로 위치를 변경하면 사람들이 좌절하고 혼란스러워할 수 있습니다. 만약 당신의 앱에서 그것이 타당하다면, 사람들이 컨트롤 위치를 사용자 지정하도록 하는 것을 고려해보세요.
>




**Avoid manually reversing controls in right-to-left locales.** The system already reverses certain controls, such as segmented controls and sliders. Manually reversing controls can cause problems with Touch Bar customization features.
> 오른쪽에서 왼쪽 로케일의 컨트롤을 수동으로 반전시키지 마십시오. 시스템은 세그먼트화된 컨트롤 및 슬라이더와 같은 특정 컨트롤을 이미 반전시킵니다. 수동으로 컨트롤을 뒤집으면 터치 바 사용자 지정 기능에 문제가 발생할 수 있습니다.
>




For developer guidance, see [NSTouchBarItem](https://developer.apple.com/documentation/appkit/nstouchbaritem).

### **Common layout styles**

Touch Bar layouts can vary significantly from app to app because of factors like configuration options, various control sizes, and the device your app is running on. When possible, use one of the following common layout styles for your controls.
> 터치 바 레이아웃은 구성 옵션, 다양한 제어 크기 및 앱이 실행 중인 장치와 같은 요소 때문에 앱마다 크게 다를 수 있습니다. 가능한 경우 컨트롤에 다음과 같은 공통 레이아웃 스타일 중 하나를 사용하십시오.
>




**Layout with one principal item.** The center of the Touch Bar contains a single large control, such as a [candidate list](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#candidate-lists). Additional controls, such as buttons and segmented controls, are on the left. In Touch Bar (2nd generation), layouts with one principal item can look like this:
> 하나의 주요 항목이 있는 레이아웃. 터치 바의 중앙에는 후보 목록과 같은 하나의 대형 컨트롤이 포함되어 있습니다. 버튼 및 세그먼트 컨트롤과 같은 추가 컨트롤은 왼쪽에 있습니다. 터치 바(2세대)에서 주 항목이 하나인 레이아웃은 다음과 같을 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal1_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal2_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal3_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal3_2x.png)

**NOTE**In Touch Bar (2nd generation), a principal candidate list control typically remains centered with respect to the device, whereas other types of principal controls may appear off-center in some circumstances. For example, an item might be too large to center in the current configuration, but may become centered when people customize the Control Strip.
> 참고 터치 바(2세대)에서 주요 후보 목록 제어는 일반적으로 기기에 대해 중심이 유지되는 반면, 일부 상황에서는 다른 유형의 주요 제어가 중심에서 벗어난 것으로 나타날 수 있다. 예를 들어, 항목이 너무 커서 현재 구성에서 중심을 맞출 수 없지만 사용자가 제어 스트립을 사용자 정의할 때 중심이 될 수 있습니다.
>




In Touch Bar (1st generation), layouts with one principal item can look like this:
> 터치 바(1세대)에서 주 항목이 하나인 레이아웃은 다음과 같을 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal1_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal2_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal3_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal3_2x.png)

**Layout with two principal items.** The center of the Touch Bar contains two consistently sized controls. Additional controls are on the left.
> 두 개의 주요 항목이 있는 레이아웃. 터치 바의 중앙에는 두 개의 일관된 크기의 컨트롤이 있습니다. 추가 컨트롤은 왼쪽에 있습니다.
>




In Touch Bar (2nd generation), a layout with two principal items can look like this:
> 터치 바(2세대)에서는 두 가지 주요 항목이 있는 레이아웃이 다음과 같이 표시될 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-2principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-2principal_2x.png)

In Touch Bar (1st generation), a layout with two principal items can look like this:
> 터치 바(1세대)에서 두 개의 주요 항목이 있는 레이아웃은 다음과 같을 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-2principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-2principal_2x.png)

**Layout with three principal items.** The center of the Touch Bar contains three consistently sized controls. Additional controls are on the left.
> 세 가지 주요 항목으로 구성된 레이아웃. 터치 바의 중앙에는 세 가지 크기의 컨트롤이 일관되게 포함되어 있습니다. 추가 컨트롤은 왼쪽에 있습니다.
>




In Touch Bar (2nd generation), a layout with three principal items can look like this:
> 터치 바(2세대)에서 세 가지 주요 항목이 있는 레이아웃은 다음과 같을 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-3principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-3principal_2x.png)

In Touch Bar (1st generation), a layout with three principal items can look like this:
> 터치 바(1세대)에서 세 가지 주요 항목이 있는 레이아웃은 다음과 같을 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-3principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-3principal_2x.png)

**Fluid layout.** This layout includes consistently-sized controls, such as buttons.
> 유체 레이아웃. 이 레이아웃에는 버튼과 같은 일정한 크기의 컨트롤이 포함됩니다.
>




In Touch Bar (2nd generation), a fluid layout can look like this:
> 터치 바(2세대)에서 유체 레이아웃은 다음과 같습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-fluid_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-fluid_2x.png)

In Touch Bar (1st generation), a fluid layout can look like this:
> 터치 바(1세대)에서 유체 레이아웃은 다음과 같습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-fluid_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-fluid_2x.png)

# **Typography**

The Touch Bar uses a variant of San Francisco, the system font in macOS. Standard Touch Bar controls, such as buttons and segmented controls, automatically use this variant. For guidance, see [Typography](../foundations/typography); for developer guidance, see [NSFont](https://developer.apple.com/documentation/appkit/nsfont).
> 터치 바는 맥 OS의 시스템 글꼴인 샌프란시스코의 변형을 사용한다. 버튼 및 세그먼트 컨트롤과 같은 표준 터치 바 컨트롤은 자동으로 이 변형을 사용합니다. 자세한 내용은 타이포그래피를 참조하고, 개발자 지침은 NSFont를 참조하십시오.
>




# **Interface icons**

macOS provides many interface icons you can use to represent common tasks and types of content in your app’s Touch Bar controls.
> macOS는 앱의 터치 바 컨트롤에서 일반적인 작업과 콘텐츠 유형을 나타내는 데 사용할 수 있는 많은 인터페이스 아이콘을 제공합니다.
>




When you use AppKit API to display a system-provided glyph, you automatically get an image in the format that’s appropriate for the version of macOS in which your app is running. For example, if your app runs in macOS 11 and later, you get an [SF Symbol](../foundations/sf-symbols/); if your app runs in Catalina or earlier, AppKit continues to provide the existing template image. For developer guidance, see [NSTouchBarItem](https://developer.apple.com/documentation/appkit/nstouchbaritem).
> AppKit API를 사용하여 시스템에서 제공하는 글리프를 표시하면 앱이 실행 중인 macOS 버전에 적합한 형식의 이미지가 자동으로 표시됩니다. 예를 들어, 앱이 macOS 11 이상에서 실행되면 SF 기호가 표시되고, 앱이 카탈리나 이하에서 실행되면 AppKit는 기존 템플릿 이미지를 계속 제공합니다. 개발자 지침은 NSTouchBarItem을 참조하십시오.
>




**IMPORTANT**By default, the system APIs return SF symbols configured as 13 pt, large scale, and medium weight.In some cases, a symbol might not have the same size or alignment as the image it replaces, so it’s important to check your layout.
> 중요 기본적으로 시스템 API는 13pt, 대규모 및 중간 무게로 구성된 SF 기호를 반환합니다.경우에 따라 기호의 크기나 정렬이 바꿀 이미지와 다를 수 있으므로 레이아웃을 확인하는 것이 중요합니다.
>




**Prefer system images because people are familiar with them.** Also, system-provided glyphs automatically receive appropriate coloring, respond to system white-point changes based on factors such as ambient light and keyboard backlight level, and respond to user interactions.
> 시스템 이미지에 익숙하기 때문에 시스템 이미지를 선호하며, 시스템이 제공하는 글리프는 자동으로 적절한 컬러링을 받고, 주변 조도 및 키보드 백라이트 레벨 등의 요소를 기반으로 시스템 화이트 포인트 변화에 대응하며, 사용자 상호작용에 대응한다.
>




**Use each system-defined glyph according to its meaning — not its appearance.** When you choose an image for its meaning, your app can remain visually consistent with the system even if the appearance of the image changes.
> 각 시스템 정의 글리프는 모양이 아니라 의미에 따라 사용합니다. 의미에 맞게 이미지를 선택하면 이미지 모양이 변경되더라도 앱이 시스템과 시각적으로 일관되게 유지될 수 있습니다.
>




**Use only system images that are designed for the Touch Bar.** Don’t use other types of images in the Touch Bar, such as toolbar glyphs.
> 터치 막대에 맞게 설계된 시스템 이미지만 사용하십시오. 도구 모음 글리프와 같은 다른 유형의 이미지는 사용하지 마십시오.
>




**Design a custom symbol or image if you can’t find a system-defined one that meets your needs.** Designing a custom symbol or image lets you communicate unique details that help people use your app; repurposing a system-defined image can cause confusion. For guidance, see [Custom Touch Bar icons](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#custom-touch-bar-icons); for general design guidance, see [Icons](../foundations/icons/).
> 사용자의 요구에 맞는 시스템 정의 기호나 이미지를 찾을 수 없으면 사용자 지정 기호나 이미지를 디자인하십시오. 사용자 지정 기호나 이미지를 디자인하면 사용자가 앱을 사용하는 데 도움이 되는 고유한 세부 정보를 전달할 수 있습니다. 시스템 정의 이미지의 용도를 변경하면 혼란이 발생할 수 있습니다. 자세한 내용은 사용자 지정 터치 막대 아이콘을 참조하고, 일반적인 설계 지침은 아이콘을 참조하십시오.
>




**NOTE**Some system icons, like Go Back and Go Forward, automatically reverse direction in right-to-left locales.
> 참고뒤로 이동 및 앞으로 이동과 같은 일부 시스템 아이콘은 오른쪽에서 왼쪽 로케일의 방향을 자동으로 반대로 바꿉니다.
>




[제목 없음](https://www.notion.so/e1afda82c9da492c8a5bf4520deb1955)

# **Custom Touch Bar icons**


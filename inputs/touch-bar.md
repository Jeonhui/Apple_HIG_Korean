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


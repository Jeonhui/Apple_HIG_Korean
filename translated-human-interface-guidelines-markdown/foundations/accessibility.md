### [[Foundations](./translated-human-interface-guidelines-markdown/foundations.md)]  
  
# **Accessibility**  



 Updated to include guidance for visionOS. Accessibility

> 비전에 대한 지침을 포함하도록 업데이트됨OS. 접근성
>

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 Apple의 내게 필요한 옵션 기능을 사용하여 장치와 상호 작용하는 방식을 개인화합니다.![내게 필요한 옵션 아이콘 스케치]. 이미지는 직사각형과 원형 격자선으로 겹쳐져 있으며 원래의 6색 애플 로고에서 노란색을 미묘하게 반영하기 위해 노란색으로 착색되어 있다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계별로 액세스 가능한 개인 설정을 지원하고 모든 사람이 자신의 기능이나 기기 사용 방법에 상관없이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 대략 7명 중 1명의 사람들이 세상과 그들의 기기와 상호작용하는 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이든, 어떤 기간이든, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 넘어져서 손목을 다치거나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 기기와 상호작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 고려한 설계.** 접근성은 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것뿐만 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성*과 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 기능을 가지고 있거나 서로 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **단순성** — 복잡한 작업을 쉽고 간편하게 수행할 수 있는 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성** — 사람들이 시각, 청각 또는 촉각을 사용하는지 여부에 관계없이 모든 콘텐츠를 인지할 수 있도록 합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인화를 지원합니다.** 사용자는 이미 환경 변화(예: 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기)에 적응할 수 있도록 사용자 환경을 설계했습니다. 사용자는 사용자가 모든 환경과 지원되는 모든 장치에서 사용하기를 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 내게 필요한 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성 요소를 사용하여 인터페이스를 구현하면 텍스트 및 컨트롤이 굵게 표시된 텍스트, 큰 텍스트, 색상 반전 및 대비 증가와 같은 여러 내게 필요한 옵션 설정에 자동으로 적용됩니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **앱 또는 게임을 감사하고 테스트하여 접근성을 확인하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 어떻게 상호 작용하는지에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 내게 필요한 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 환경을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있습니다 이 흐름을 구성하는 작업은 다음과 같습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱이나 게임에서 중요한 각 사용자 흐름에 대해 VoiceOver(음성 오버), Reduce Motion(동작 감소) 또는 Large Text Size(큰 텍스트 크기)와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있도록 하십시오. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 켜고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 관리자를 사용해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능의 제스처가 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순화된 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임이 필요한 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사용자의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **동작 기반 동작을 수행할 수 있는 다른 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 사람들이 제스처를 사용하여 표의 행을 삭제할 수 있는 경우, 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우 앱과 상호 작용할 수 있는 다른 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어 포인터 컨트롤을 사용하면 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 개체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control, Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIAccessibilityCustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술을 통해 사람들이 항목을 드래그 앤 드롭할 수 있습니다. 개발자 지침은 ['accessibilityDragSourceDescriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤과 대화형 요소에 충분히 큰 적중 대상을 지정합니다.** 예를 들어 터치스크린 장치의 경우 적중한 대상은 시야에서 최소 44x44 pt를 측정해야 한다OS, 중앙이 최소 60pt 이상 떨어져 있도록 제어 장치를 배치합니다. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 대상이 필요합니다. 사람들이 포인터를 사용할 때도 플랫폼에서 너무 작은 컨트롤과 상호 작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 정의 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소가 어떻게 동작하는지 알려줄 수 있습니다. 예를 들어 ['button'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) )을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 보기를 단추로 특성화한다는 것은 VoiceOver가 보기 설명에 이어 *button*이라는 단어를 사용한다는 것을 의미하며, 이는 보기가 단추처럼 작동한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> **버튼의 상대적 중요성을 전달하기 위해 일관된 스타일의 계층 구조를 사용합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러진 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 수행하는 단추에는 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내는 ['UIButton]을 참조하십시오.).구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템에서 제공하는 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전에서OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 활성 버튼과 주변 콘텐츠를 더 쉽게 구별하기 위해 버튼 셰이프를 켤 수 있다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템에서 제공하는 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색으로 상태를 나타내는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 인식할 수 있다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOSOS 및 watchOS는 사람들이 라벨을 켜거나 끌 때 자동으로 그 안에 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타이핑이나 제스처 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **음성만으로 중요한 작업을 수행할 수 있도록 Sir 바로 가기 기능을 지원합니다.** 당신의 앱에서 사람들이 시리 상호작용을 사용하도록 돕는 것에 대한 자세한 내용은 [시리](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존한다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱 지원.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호 작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리는 햅틱을 재생합니다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의된 햅틱을 일관되게 사용해야 합니다. 자세한 내용은 [haptics 재생](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 을 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 지정 개체와 상호 작용할 때 피드백을 제공하는 다른 방법을 사용하십시오.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 가시적인 콘텐츠에 대한 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달합니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 그들의 손 입력을 해석하는 앱에 대해 걱정하지 않고 보이스오버 제스처를 수행하여 앱을 탐색할 수 있다. 보이스오버의 다이렉트 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 대신 앱이 직접 입력을 처리하도록 한다. 개발자 지침은 [비전에서 내게 필요한 내게 필요한 옵션 지원 향상]을 참조하십시오OS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 만들려면 먼저 이미지를 볼 수 있는 사용자에게 설명할 수 있는 내용을 보고합니다. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명의 초점을 맞춥니다.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 애플의 접근성 기능을 사용하여 자신에게 적합한 방식으로 기기와 상호 작용하는 방법을 개인화합니다.![접근성 아이콘의 스케치입니다. 이미지는 직사각형과 원형 격자선으로 겹쳐지고 원래의 6색 애플 로고에 노란색을 은은하게 반영하기 위해 노란색으로 색칠되었다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계에 따라 액세스 가능한 개인 설정을 지원하며 기능이나 장치 사용 방법에 관계없이 모든 사람이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 약 7명 중 1명은 장애를 가지고 있으며, 이는 그들이 세상과 그들의 장치와 상호작용하는 방식에 영향을 미친다. 사람들은 나이, 기간, 그리고 다양한 중증도에서 장애를 경험할 수 있다. 예를 들어, 낙상으로 인한 손목 부상이나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 자신의 기기와 상호 작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 염두에 두고 설계하십시오.** 접근성은 단지 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것이 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것이다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성* 및 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 능력을 가지고 있거나 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **Simplicity**—복잡한 작업을 간단하고 쉽게 수행할 수 있도록 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성**—사람들이 시각, 청각 또는 촉각을 사용하든 모든 콘텐츠를 인지할 수 있는지 확인합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인 설정을 지원합니다.** 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기와 같은 환경 변화에 적응할 수 있도록 이미 경험을 설계하고 있습니다. 이는 사람들이 어떤 맥락에서든 지원되는 모든 장치에서 경험을 즐기길 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 접근성 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성요소를 사용하여 인터페이스를 구현할 때 텍스트와 컨트롤은 굵은 텍스트, 큰 텍스트, 색 반전 및 대비 증가와 같은 여러 접근성 설정에 자동으로 적응합니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **사용자의 앱 또는 게임을 감사하고 접근성을 테스트하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 상호 작용하는 방식에 상관없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 접근성 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제에 대한 인식을 얻을 수 있습니다. 또한 앱이 훌륭한 사용자 경험을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있다 이 흐름을 구성하는 작업에는 다음이 포함될 수 있습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱 또는 게임의 중요한 각 사용자 흐름에 대해 VoiceOver, Reduce Motion 또는 Large Text Size와 같은 접근성 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있는지 확인합니다. 발견한 문제를 해결한 후 다른 접근성 기능을 설정하고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되려면 Xcode의 내게 필요한 옵션 관리자를 사용하는 것을 고려해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 그들의 장치와 상호작용할 수 있는 방법을 확장한다. 이러한 기술은 시스템 제공 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원해야 합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능이 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순한 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임을 필요로 하는 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사람의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **제스처 기반 작업을 수행하는 대체 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사람을 위한 옵션을 포함합니다. 예를 들어, 사용자가 제스처를 사용하여 테이블의 행을 삭제할 수 있는 경우 편집 모드를 통해 또는 항목 상세 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우, 사람들에게 앱과 상호 작용할 수 있는 대안적인 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어, 포인터 컨트롤을 사용하면 사람들은 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 객체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control 및 Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIA Accessibility CustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭을 사용할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스를 식별하고 대상을 드롭할 때 보조 기술을 사용하면 사람들이 항목을 드래그하고 드롭하는 데 도움이 될 수 있습니다. 개발자 지침은 ['접근성 DragSource Descriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤 및 대화형 요소에 충분히 큰 목표치를 부여하십시오.** 예를 들어, 터치스크린 장치에서 히트 대상은 최소 44x44 pt를 측정해야 합니다OS, 중심이 최소 60p 이상 떨어져 있도록 컨트롤을 배치하십시오. 이동성이 제한된 사람들은 당신의 앱과 상호작용하는 것을 돕기 위해 더 큰 목표물이 필요하다. 사람들이 포인터를 사용할 때조차도 어떤 플랫폼에서도 너무 작은 컨트롤과 상호작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 지정 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소의 동작 방식을 알려줄 수 있습니다. 예를 들어 ['버튼'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) 을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 뷰를 버튼으로 특성화한다는 것은 VoiceOver가 뷰의 설명과 *버튼*이라는 단어를 말하는 것을 의미하며, 이는 뷰가 버튼처럼 동작한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> ** 일관된 스타일 계층을 사용하여 단추의 상대적인 중요성을 전달합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서는 보기에서 가장 가능성이 높은 동작을 수행하는 버튼에 시각적으로 두드러지는 채우기 스타일을 사용할 수 있으며, 덜 중요한 동작을 수행하는 버튼에 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내에 대해서는 [`UIButton]을 참조하십시오.구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템 제공 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 버튼 모양을 사용하여 활성 버튼과 주변 콘텐츠를 더 쉽게 구분할 수 있습니다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템 제공 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색상으로 상태를 나타내는 스위치를 제공합니다. 그러나 어떤 사람들은 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 알 수 있습니다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOS, 비전OS, 그리고 시청OS는 사람들이 온/오프 라벨을 켜면 자동으로 그 안에 온/오프 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타자를 치거나 손짓을 하는 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 버튼을 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **중요한 작업을 음성으로만 수행할 수 있는 Siri 또는 바로 가기를 지원합니다.** 앱에서 사람들이 Siri 상호작용을 사용할 수 있도록 돕는 방법에 대한 자세한 내용은 [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존합니다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱을 지원합니다.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리기 위해 햅틱을 재생한다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의 햅틱을 일관되게 사용해야 한다. 자세한 내용은 [Haptics 플레이하기](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 를 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 정의 객체와 상호 작용할 때 다른 방법을 사용하여 피드백을 제공한다.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 표시된 콘텐츠에 대한 청각적 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달하는 데 도움이 됩니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 자신의 손 입력을 해석하는 앱에 대한 걱정 없이 앱을 탐색하기 위해 보이스 오버 제스처를 수행할 수 있다. 보이스오버의 직접 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 앱이 직접 손 입력을 처리하도록 합니다. 개발자 지침은 [비전 내 접근성 지원 향상]을 참조하십시오OS 앱](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠의 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하도록 합니다. 유용한 설명을 작성하려면 먼저 이미지를 볼 수 있는 사용자에게 설명이 필요한 내용을 보고하십시오. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명을 집중하십시오.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 애플의 접근성 기능을 사용하여 자신에게 적합한 방식으로 기기와 상호 작용하는 방법을 개인화합니다.![접근성 아이콘의 스케치입니다. 이미지는 직사각형과 원형 격자선으로 겹쳐지고 원래의 6색 애플 로고에 노란색을 은은하게 반영하기 위해 노란색으로 색칠되었다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계에 따라 액세스 가능한 개인 설정을 지원하며 기능이나 장치 사용 방법에 관계없이 모든 사람이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 약 7명 중 1명은 장애를 가지고 있으며, 이는 그들이 세상과 그들의 장치와 상호작용하는 방식에 영향을 미친다. 사람들은 나이, 기간, 그리고 다양한 중증도에서 장애를 경험할 수 있다. 예를 들어, 낙상으로 인한 손목 부상이나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 자신의 기기와 상호 작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 염두에 두고 설계하십시오.** 접근성은 단지 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것이 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것이다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성* 및 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 능력을 가지고 있거나 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **Simplicity**—복잡한 작업을 간단하고 쉽게 수행할 수 있도록 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성**—사람들이 시각, 청각 또는 촉각을 사용하든 모든 콘텐츠를 인지할 수 있는지 확인합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인 설정을 지원합니다.** 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기와 같은 환경 변화에 적응할 수 있도록 이미 경험을 설계하고 있습니다. 이는 사람들이 어떤 맥락에서든 지원되는 모든 장치에서 경험을 즐기길 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 접근성 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성요소를 사용하여 인터페이스를 구현할 때 텍스트와 컨트롤은 굵은 텍스트, 큰 텍스트, 색 반전 및 대비 증가와 같은 여러 접근성 설정에 자동으로 적응합니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **사용자의 앱 또는 게임을 감사하고 접근성을 테스트하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 상호 작용하는 방식에 상관없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 접근성 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제에 대한 인식을 얻을 수 있습니다. 또한 앱이 훌륭한 사용자 경험을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있다 이 흐름을 구성하는 작업에는 다음이 포함될 수 있습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱 또는 게임의 중요한 각 사용자 흐름에 대해 VoiceOver, Reduce Motion 또는 Large Text Size와 같은 접근성 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있는지 확인합니다. 발견한 문제를 해결한 후 다른 접근성 기능을 설정하고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되려면 Xcode의 내게 필요한 옵션 관리자를 사용하는 것을 고려해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 그들의 장치와 상호작용할 수 있는 방법을 확장한다. 이러한 기술은 시스템 제공 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원해야 합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능이 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순한 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임을 필요로 하는 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사람의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **제스처 기반 작업을 수행하는 대체 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사람을 위한 옵션을 포함합니다. 예를 들어, 사용자가 제스처를 사용하여 테이블의 행을 삭제할 수 있는 경우 편집 모드를 통해 또는 항목 상세 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우, 사람들에게 앱과 상호 작용할 수 있는 대안적인 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어, 포인터 컨트롤을 사용하면 사람들은 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 객체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control 및 Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIA Accessibility CustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭을 사용할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스를 식별하고 대상을 드롭할 때 보조 기술을 사용하면 사람들이 항목을 드래그하고 드롭하는 데 도움이 될 수 있습니다. 개발자 지침은 ['접근성 DragSource Descriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤 및 대화형 요소에 충분히 큰 목표치를 부여하십시오.** 예를 들어, 터치스크린 장치에서 히트 대상은 최소 44x44 pt를 측정해야 합니다OS, 중심이 최소 60p 이상 떨어져 있도록 컨트롤을 배치하십시오. 이동성이 제한된 사람들은 당신의 앱과 상호작용하는 것을 돕기 위해 더 큰 목표물이 필요하다. 사람들이 포인터를 사용할 때조차도 어떤 플랫폼에서도 너무 작은 컨트롤과 상호작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 지정 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소의 동작 방식을 알려줄 수 있습니다. 예를 들어 ['버튼'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) 을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 뷰를 버튼으로 특성화한다는 것은 VoiceOver가 뷰의 설명과 *버튼*이라는 단어를 말하는 것을 의미하며, 이는 뷰가 버튼처럼 동작한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> ** 일관된 스타일 계층을 사용하여 단추의 상대적인 중요성을 전달합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서는 보기에서 가장 가능성이 높은 동작을 수행하는 버튼에 시각적으로 두드러지는 채우기 스타일을 사용할 수 있으며, 덜 중요한 동작을 수행하는 버튼에 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내에 대해서는 [`UIButton]을 참조하십시오.구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템 제공 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 버튼 모양을 사용하여 활성 버튼과 주변 콘텐츠를 더 쉽게 구분할 수 있습니다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템 제공 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색상으로 상태를 나타내는 스위치를 제공합니다. 그러나 어떤 사람들은 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 알 수 있습니다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOS, 비전OS, 그리고 시청OS는 사람들이 온/오프 라벨을 켜면 자동으로 그 안에 온/오프 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타자를 치거나 손짓을 하는 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 버튼을 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **중요한 작업을 음성으로만 수행할 수 있는 Siri 또는 바로 가기를 지원합니다.** 앱에서 사람들이 Siri 상호작용을 사용할 수 있도록 돕는 방법에 대한 자세한 내용은 [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존합니다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱을 지원합니다.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리기 위해 햅틱을 재생한다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의 햅틱을 일관되게 사용해야 한다. 자세한 내용은 [Haptics 플레이하기](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 를 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 정의 객체와 상호 작용할 때 다른 방법을 사용하여 피드백을 제공한다.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 표시된 콘텐츠에 대한 청각적 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달하는 데 도움이 됩니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 자신의 손 입력을 해석하는 앱에 대한 걱정 없이 앱을 탐색하기 위해 보이스 오버 제스처를 수행할 수 있다. 보이스오버의 직접 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 앱이 직접 손 입력을 처리하도록 합니다. 개발자 지침은 [비전 내 접근성 지원 향상]을 참조하십시오OS 앱](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠의 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하도록 합니다. 유용한 설명을 작성하려면 먼저 이미지를 볼 수 있는 사용자에게 설명이 필요한 내용을 보고하십시오. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명을 집중하십시오.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 애플의 접근성 기능을 사용하여 자신에게 적합한 방식으로 기기와 상호 작용하는 방법을 개인화합니다.![접근성 아이콘의 스케치입니다. 이미지는 직사각형과 원형 격자선으로 겹쳐지고 원래의 6색 애플 로고에 노란색을 은은하게 반영하기 위해 노란색으로 색칠되었다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계에 따라 액세스 가능한 개인 설정을 지원하며 기능이나 장치 사용 방법에 관계없이 모든 사람이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 약 7명 중 1명은 장애를 가지고 있으며, 이는 그들이 세상과 그들의 장치와 상호작용하는 방식에 영향을 미친다. 사람들은 나이, 기간, 그리고 다양한 중증도에서 장애를 경험할 수 있다. 예를 들어, 낙상으로 인한 손목 부상이나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 자신의 기기와 상호 작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 염두에 두고 설계하십시오.** 접근성은 단지 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것이 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것이다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성* 및 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 능력을 가지고 있거나 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **Simplicity**—복잡한 작업을 간단하고 쉽게 수행할 수 있도록 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성**—사람들이 시각, 청각 또는 촉각을 사용하든 모든 콘텐츠를 인지할 수 있는지 확인합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인 설정을 지원합니다.** 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기와 같은 환경 변화에 적응할 수 있도록 이미 경험을 설계하고 있습니다. 이는 사람들이 어떤 맥락에서든 지원되는 모든 장치에서 경험을 즐기길 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 접근성 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성요소를 사용하여 인터페이스를 구현할 때 텍스트와 컨트롤은 굵은 텍스트, 큰 텍스트, 색 반전 및 대비 증가와 같은 여러 접근성 설정에 자동으로 적응합니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **사용자의 앱 또는 게임을 감사하고 접근성을 테스트하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 상호 작용하는 방식에 상관없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 접근성 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제에 대한 인식을 얻을 수 있습니다. 또한 앱이 훌륭한 사용자 경험을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있다 이 흐름을 구성하는 작업에는 다음이 포함될 수 있습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱 또는 게임의 중요한 각 사용자 흐름에 대해 VoiceOver, Reduce Motion 또는 Large Text Size와 같은 접근성 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있는지 확인합니다. 발견한 문제를 해결한 후 다른 접근성 기능을 설정하고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되려면 Xcode의 내게 필요한 옵션 관리자를 사용하는 것을 고려해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 그들의 장치와 상호작용할 수 있는 방법을 확장한다. 이러한 기술은 시스템 제공 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원해야 합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능이 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순한 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임을 필요로 하는 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사람의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **제스처 기반 작업을 수행하는 대체 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사람을 위한 옵션을 포함합니다. 예를 들어, 사용자가 제스처를 사용하여 테이블의 행을 삭제할 수 있는 경우 편집 모드를 통해 또는 항목 상세 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우, 사람들에게 앱과 상호 작용할 수 있는 대안적인 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어, 포인터 컨트롤을 사용하면 사람들은 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 객체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control 및 Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIA Accessibility CustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭을 사용할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스를 식별하고 대상을 드롭할 때 보조 기술을 사용하면 사람들이 항목을 드래그하고 드롭하는 데 도움이 될 수 있습니다. 개발자 지침은 ['접근성 DragSource Descriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤 및 대화형 요소에 충분히 큰 목표치를 부여하십시오.** 예를 들어, 터치스크린 장치에서 히트 대상은 최소 44x44 pt를 측정해야 합니다OS, 중심이 최소 60p 이상 떨어져 있도록 컨트롤을 배치하십시오. 이동성이 제한된 사람들은 당신의 앱과 상호작용하는 것을 돕기 위해 더 큰 목표물이 필요하다. 사람들이 포인터를 사용할 때조차도 어떤 플랫폼에서도 너무 작은 컨트롤과 상호작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 지정 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소의 동작 방식을 알려줄 수 있습니다. 예를 들어 ['버튼'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) 을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 뷰를 버튼으로 특성화한다는 것은 VoiceOver가 뷰의 설명과 *버튼*이라는 단어를 말하는 것을 의미하며, 이는 뷰가 버튼처럼 동작한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> ** 일관된 스타일 계층을 사용하여 단추의 상대적인 중요성을 전달합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서는 보기에서 가장 가능성이 높은 동작을 수행하는 버튼에 시각적으로 두드러지는 채우기 스타일을 사용할 수 있으며, 덜 중요한 동작을 수행하는 버튼에 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내에 대해서는 [`UIButton]을 참조하십시오.구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템 제공 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 버튼 모양을 사용하여 활성 버튼과 주변 콘텐츠를 더 쉽게 구분할 수 있습니다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템 제공 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색상으로 상태를 나타내는 스위치를 제공합니다. 그러나 어떤 사람들은 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 알 수 있습니다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOS, 비전OS, 그리고 시청OS는 사람들이 온/오프 라벨을 켜면 자동으로 그 안에 온/오프 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타자를 치거나 손짓을 하는 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 버튼을 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **중요한 작업을 음성으로만 수행할 수 있는 Siri 또는 바로 가기를 지원합니다.** 앱에서 사람들이 Siri 상호작용을 사용할 수 있도록 돕는 방법에 대한 자세한 내용은 [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존합니다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱을 지원합니다.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리기 위해 햅틱을 재생한다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의 햅틱을 일관되게 사용해야 한다. 자세한 내용은 [Haptics 플레이하기](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 를 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 정의 객체와 상호 작용할 때 다른 방법을 사용하여 피드백을 제공한다.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 표시된 콘텐츠에 대한 청각적 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달하는 데 도움이 됩니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 자신의 손 입력을 해석하는 앱에 대한 걱정 없이 앱을 탐색하기 위해 보이스 오버 제스처를 수행할 수 있다. 보이스오버의 직접 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 앱이 직접 손 입력을 처리하도록 합니다. 개발자 지침은 [비전 내 접근성 지원 향상]을 참조하십시오OS 앱](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠의 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하도록 합니다. 유용한 설명을 작성하려면 먼저 이미지를 볼 수 있는 사용자에게 설명이 필요한 내용을 보고하십시오. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명을 집중하십시오.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 애플의 접근성 기능을 사용하여 자신에게 적합한 방식으로 기기와 상호 작용하는 방법을 개인화합니다.![접근성 아이콘의 스케치입니다. 이미지는 직사각형과 원형 격자선으로 겹쳐지고 원래의 6색 애플 로고에 노란색을 은은하게 반영하기 위해 노란색으로 색칠되었다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계에 따라 액세스 가능한 개인 설정을 지원하며 기능이나 장치 사용 방법에 관계없이 모든 사람이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 약 7명 중 1명은 장애를 가지고 있으며, 이는 그들이 세상과 그들의 장치와 상호작용하는 방식에 영향을 미친다. 사람들은 나이, 기간, 그리고 다양한 중증도에서 장애를 경험할 수 있다. 예를 들어, 낙상으로 인한 손목 부상이나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 자신의 기기와 상호 작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 염두에 두고 설계하십시오.** 접근성은 단지 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것이 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것이다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성* 및 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 능력을 가지고 있거나 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **Simplicity**—복잡한 작업을 간단하고 쉽게 수행할 수 있도록 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성**—사람들이 시각, 청각 또는 촉각을 사용하든 모든 콘텐츠를 인지할 수 있는지 확인합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인 설정을 지원합니다.** 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기와 같은 환경 변화에 적응할 수 있도록 이미 경험을 설계하고 있습니다. 이는 사람들이 어떤 맥락에서든 지원되는 모든 장치에서 경험을 즐기길 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 접근성 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성요소를 사용하여 인터페이스를 구현할 때 텍스트와 컨트롤은 굵은 텍스트, 큰 텍스트, 색 반전 및 대비 증가와 같은 여러 접근성 설정에 자동으로 적응합니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **사용자의 앱 또는 게임을 감사하고 접근성을 테스트하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 상호 작용하는 방식에 상관없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 접근성 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제에 대한 인식을 얻을 수 있습니다. 또한 앱이 훌륭한 사용자 경험을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있다 이 흐름을 구성하는 작업에는 다음이 포함될 수 있습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱 또는 게임의 중요한 각 사용자 흐름에 대해 VoiceOver, Reduce Motion 또는 Large Text Size와 같은 접근성 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있는지 확인합니다. 발견한 문제를 해결한 후 다른 접근성 기능을 설정하고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되려면 Xcode의 내게 필요한 옵션 관리자를 사용하는 것을 고려해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 그들의 장치와 상호작용할 수 있는 방법을 확장한다. 이러한 기술은 시스템 제공 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원해야 합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능이 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순한 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임을 필요로 하는 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사람의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **제스처 기반 작업을 수행하는 대체 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사람을 위한 옵션을 포함합니다. 예를 들어, 사용자가 제스처를 사용하여 테이블의 행을 삭제할 수 있는 경우 편집 모드를 통해 또는 항목 상세 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우, 사람들에게 앱과 상호 작용할 수 있는 대안적인 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어, 포인터 컨트롤을 사용하면 사람들은 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 객체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control 및 Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIA Accessibility CustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭을 사용할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스를 식별하고 대상을 드롭할 때 보조 기술을 사용하면 사람들이 항목을 드래그하고 드롭하는 데 도움이 될 수 있습니다. 개발자 지침은 ['접근성 DragSource Descriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤 및 대화형 요소에 충분히 큰 목표치를 부여하십시오.** 예를 들어, 터치스크린 장치에서 히트 대상은 최소 44x44 pt를 측정해야 합니다OS, 중심이 최소 60p 이상 떨어져 있도록 컨트롤을 배치하십시오. 이동성이 제한된 사람들은 당신의 앱과 상호작용하는 것을 돕기 위해 더 큰 목표물이 필요하다. 사람들이 포인터를 사용할 때조차도 어떤 플랫폼에서도 너무 작은 컨트롤과 상호작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 지정 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소의 동작 방식을 알려줄 수 있습니다. 예를 들어 ['버튼'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) 을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 뷰를 버튼으로 특성화한다는 것은 VoiceOver가 뷰의 설명과 *버튼*이라는 단어를 말하는 것을 의미하며, 이는 뷰가 버튼처럼 동작한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> ** 일관된 스타일 계층을 사용하여 단추의 상대적인 중요성을 전달합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서는 보기에서 가장 가능성이 높은 동작을 수행하는 버튼에 시각적으로 두드러지는 채우기 스타일을 사용할 수 있으며, 덜 중요한 동작을 수행하는 버튼에 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내에 대해서는 [`UIButton]을 참조하십시오.구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템 제공 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 버튼 모양을 사용하여 활성 버튼과 주변 콘텐츠를 더 쉽게 구분할 수 있습니다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템 제공 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색상으로 상태를 나타내는 스위치를 제공합니다. 그러나 어떤 사람들은 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 알 수 있습니다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOS, 비전OS, 그리고 시청OS는 사람들이 온/오프 라벨을 켜면 자동으로 그 안에 온/오프 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타자를 치거나 손짓을 하는 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 버튼을 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **중요한 작업을 음성으로만 수행할 수 있는 Siri 또는 바로 가기를 지원합니다.** 앱에서 사람들이 Siri 상호작용을 사용할 수 있도록 돕는 방법에 대한 자세한 내용은 [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존합니다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱을 지원합니다.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리기 위해 햅틱을 재생한다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의 햅틱을 일관되게 사용해야 한다. 자세한 내용은 [Haptics 플레이하기](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 를 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 정의 객체와 상호 작용할 때 다른 방법을 사용하여 피드백을 제공한다.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 표시된 콘텐츠에 대한 청각적 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달하는 데 도움이 됩니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 자신의 손 입력을 해석하는 앱에 대한 걱정 없이 앱을 탐색하기 위해 보이스 오버 제스처를 수행할 수 있다. 보이스오버의 직접 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 앱이 직접 손 입력을 처리하도록 합니다. 개발자 지침은 [비전 내 접근성 지원 향상]을 참조하십시오OS 앱](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠의 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하도록 합니다. 유용한 설명을 작성하려면 먼저 이미지를 볼 수 있는 사용자에게 설명이 필요한 내용을 보고하십시오. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명을 집중하십시오.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

=============



People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.![A sketch of the Accessibility icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro@2x.png)

> 사람들은 애플의 접근성 기능을 사용하여 자신에게 적합한 방식으로 기기와 상호 작용하는 방법을 개인화합니다.![접근성 아이콘의 스케치입니다. 이미지는 직사각형과 원형 격자선으로 겹쳐지고 원래의 6색 애플 로고에 노란색을 은은하게 반영하기 위해 노란색으로 색칠되었다.](https://docs-assets.developer.apple.com/published/4a0cd0e3a75fcc9b409f6d1bffbcf031/foundations-accessibility-intro @2x.png)
>



An accessible app or game supports accessibility personalizations by design and helps everyone have a great experience, regardless of their capabilities or how they use their devices.

> 액세스 가능한 앱 또는 게임은 설계에 따라 액세스 가능한 개인 설정을 지원하며 기능이나 장치 사용 방법에 관계없이 모든 사람이 훌륭한 경험을 할 수 있도록 도와줍니다.
>



Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.

> 약 7명 중 1명은 장애를 가지고 있으며, 이는 그들이 세상과 그들의 장치와 상호작용하는 방식에 영향을 미친다. 사람들은 나이, 기간, 그리고 다양한 중증도에서 장애를 경험할 수 있다. 예를 들어, 낙상으로 인한 손목 부상이나 과도한 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 자신의 기기와 상호 작용하는 방식에 영향을 미칠 수 있다.
>



[Best practices](/design/human-interface-guidelines/accessibility#Best-practices)

---------------------------------------------------------------------------------



**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.

> **접근성을 염두에 두고 설계하십시오.** 접근성은 단지 장애가 있는 사람들이 정보를 이용할 수 있도록 하는 것이 아니라, 그들의 능력이나 상황에 관계없이 모든 사람들이 정보를 이용할 수 있도록 하는 것이다. 접근성을 염두에 두고 앱을 설계한다는 것은 *단순성* 및 *지각성*을 우선시하고 모든 설계 결정을 검토하여 서로 다른 능력을 가지고 있거나 다른 방식으로 기기와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>



**Simplicity** — Support familiar, consistent interactions that make complex tasks simple and straightforward to perform.

> **Simplicity**—복잡한 작업을 간단하고 쉽게 수행할 수 있도록 친숙하고 일관된 상호 작용을 지원합니다.
>



**Perceivability** — Make sure that all content can be perceived whether people are using sight, hearing, or touch.

> **지각성**—사람들이 시각, 청각 또는 촉각을 사용하든 모든 콘텐츠를 인지할 수 있는지 확인합니다.
>



**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, display size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.

> **개인 설정을 지원합니다.** 장치 방향, 디스플레이 크기, 해상도, 색역 및 분할 보기와 같은 환경 변화에 적응할 수 있도록 이미 경험을 설계하고 있습니다. 이는 사람들이 어떤 맥락에서든 지원되는 모든 장치에서 경험을 즐기길 원하기 때문입니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하기 위해 사용하는 접근성 기능을 지원하도록 앱을 설계할 수 있습니다.
>



When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.

> 표준 구성요소를 사용하여 인터페이스를 구현할 때 텍스트와 컨트롤은 굵은 텍스트, 큰 텍스트, 색 반전 및 대비 증가와 같은 여러 접근성 설정에 자동으로 적응합니다.
>



**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.

> **사용자의 앱 또는 게임을 감사하고 접근성을 테스트하십시오.** 감사는 사용자 경험의 모든 요소를 검사하고 해결해야 할 포괄적인 문제 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 상호 작용하는 방식에 상관없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>



When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.

> 접근성 기능이 설정된 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제에 대한 인식을 얻을 수 있습니다. 또한 앱이 훌륭한 사용자 경험을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>



For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:

> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있다 이 흐름을 구성하는 작업에는 다음이 포함될 수 있습니다:
>



* Read posted comments.

* Choose a comment for a response.

> * 응답에 대한 설명을 선택합니다.
>

* Open the response view.

> * 응답 보기를 엽니다.
>

* Edit the response.

* Post the response.



For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.

> 앱 또는 게임의 중요한 각 사용자 흐름에 대해 VoiceOver, Reduce Motion 또는 Large Text Size와 같은 접근성 기능을 설정하고 흐름의 모든 작업을 어렵지 않게 완료할 수 있는지 확인합니다. 발견한 문제를 해결한 후 다른 접근성 기능을 설정하고 사용자 흐름을 다시 실행합니다. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되려면 Xcode의 내게 필요한 옵션 관리자를 사용하는 것을 고려해 보십시오.
>



[Interactions](/design/human-interface-guidelines/accessibility#Interactions)

-----------------------------------------------------------------------------



Assistive technologies like VoiceOver, Assistive Touch, Pointer Control, and Switch Control expand the ways people can interact with their devices. Because these technologies integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.

> VoiceOver, Assistive Touch, Pointer Control 및 Switch Control과 같은 보조 기술은 사람들이 그들의 장치와 상호작용할 수 있는 방법을 확장한다. 이러한 기술은 시스템 제공 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원해야 합니다.
>



### [Gestures](/design/human-interface-guidelines/accessibility#Gestures)



**Don’t override the platform gestures.** People expect gestures that target system features — like swiping down to reveal Notification Center — to work regardless of the app they’re using.

> **플랫폼 제스처를 무시하지 마십시오.** 사람들은 Notification Center를 표시하기 위해 아래로 쓸어 내리는 것과 같은 대상 시스템 기능이 사용 중인 앱에 상관없이 작동하기를 기대합니다.
>



**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger or multihand gestures, long presses, or gestures that require repeated movements can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.

> **일반적인 상호작용을 위해 단순한 제스처를 선호합니다.** 멀티핑거나 멀티핸드 제스처, 길게 누르기 또는 반복적인 움직임을 필요로 하는 제스처와 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사람의 경험이 향상됩니다.
>



**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if people can use a gesture to delete a row in a table, you can also provide a way to delete items through an edit mode or by offering a Delete button in an item detail view.

> **제스처 기반 작업을 수행하는 대체 방법을 제공합니다.** 특정 제스처를 수행할 수 없는 사람을 위한 옵션을 포함합니다. 예를 들어, 사용자가 제스처를 사용하여 테이블의 행을 삭제할 수 있는 경우 편집 모드를 통해 또는 항목 상세 보기에서 삭제 단추를 제공하여 항목을 삭제하는 방법을 제공할 수도 있습니다.
>



![An illustration of a list-based app on iPhone. The list is in edit mode, and each list item displays a circular Delete button on the left.](https://docs-assets.developer.apple.com/published/0ef69eb127a1f8225ebbd5ba6786fb63/tap-to-delete@2x.png)Edit to delete.![An illustration of a list-based app on iPhone. The Delete button for the first item is revealed, as if someone swiped the item to the left.](https://docs-assets.developer.apple.com/published/7180d8c6c9a19832cebdfb515b0dbfea/swipe-to-delete@2x.png)Swipe to delete.**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device’s volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.



**If you define custom gestures, be sure to support assistive technologies that give people alternative ways to interact with your app.** For example, with Pointer Control, people can use a wrist, index finger, or head-based pointer; with Dwell Control, they can use only their eyes to select and activate objects. One way to support technologies like VoiceOver, Dwell Control, and Switch Control is to implement custom actions; for developer guidance, see [`UIAccessibilityCustomAction`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction)

> **사용자 지정 제스처를 정의하는 경우, 사람들에게 앱과 상호 작용할 수 있는 대안적인 방법을 제공하는 보조 기술을 지원해야 합니다.** 예를 들어, 포인터 컨트롤을 사용하면 사람들은 손목, 검지 또는 머리 기반 포인터를 사용할 수 있고, 드웰 컨트롤을 사용하면 눈만 사용하여 객체를 선택하고 활성화할 수 있습니다. VoiceOver, Dwell Control 및 Switch Control과 같은 기술을 지원하는 한 가지 방법은 사용자 지정 작업을 구현하는 것입니다. 개발자 지침은 ['UIA Accessibility CustomAction'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomaction) 을 참조하십시오
>

.



**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop items. For developer guidance, see [`accessibilityDragSourceDescriptors`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto)

> **iOS 또는 iPadOS 앱에서 드래그 앤 드롭을 사용할 수 있도록 합니다.** 접근성 API를 사용하여 앱에서 드래그 소스를 식별하고 대상을 드롭할 때 보조 기술을 사용하면 사람들이 항목을 드래그하고 드롭하는 데 도움이 될 수 있습니다. 개발자 지침은 ['접근성 DragSource Descriptors'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) 를 참조하십시오
>

 and [`accessibilityDropPointDescriptors`](/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)

.



### [Buttons and controls](/design/human-interface-guidelines/accessibility#Buttons-and-controls)



**Give all controls and interactive elements a hit target that’s large enough.** For example, on touchscreen devices, a hit target needs to measure at least 44x44 pt; in visionOS, place controls so that their centers are at least 60 pt apart. People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.

> **모든 컨트롤 및 대화형 요소에 충분히 큰 목표치를 부여하십시오.** 예를 들어, 터치스크린 장치에서 히트 대상은 최소 44x44 pt를 측정해야 합니다OS, 중심이 최소 60p 이상 떨어져 있도록 컨트롤을 배치하십시오. 이동성이 제한된 사람들은 당신의 앱과 상호작용하는 것을 돕기 위해 더 큰 목표물이 필요하다. 사람들이 포인터를 사용할 때조차도 어떤 플랫폼에서도 너무 작은 컨트롤과 상호작용하는 것은 좌절감을 줄 수 있다.
>



**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [`button`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button)

> **사용자 지정 요소의 접근성을 특성화합니다.** 시스템 API를 사용하여 보조 기술에 구성 요소의 동작 방식을 알려줄 수 있습니다. 예를 들어 ['버튼'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitytraits/1620194-button) 을 사용합니다
>

 or [`NSAccessibilityButton`](/documentation/appkit/nsaccessibilitybutton)

 to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.

> 뷰를 버튼으로 특성화한다는 것은 VoiceOver가 뷰의 설명과 *버튼*이라는 단어를 말하는 것을 의미하며, 이는 뷰가 버튼처럼 동작한다는 것을 사람들에게 알려줍니다.
>



**Use a consistent style hierarchy to communicate the relative importance of buttons.** In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that perform less important actions. (For developer guidance, see [`UIButton.Configuration`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)

> ** 일관된 스타일 계층을 사용하여 단추의 상대적인 중요성을 전달합니다.** 예를 들어 iOS, iPadOS 및 TVOS에서는 보기에서 가장 가능성이 높은 동작을 수행하는 버튼에 시각적으로 두드러지는 채우기 스타일을 사용할 수 있으며, 덜 중요한 동작을 수행하는 버튼에 회색 또는 일반과 같은 덜 두드러지는 스타일을 사용할 수 있습니다. (개발자 안내에 대해서는 [`UIButton]을 참조하십시오.구성'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uibutton/configuration)
>

.) In visionOS, system-provided buttons generally include a visible background by default. In iOS, iPadOS, visionOS, and for some buttons in macOS, people can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.

> .) 비전OS, 시스템 제공 버튼은 일반적으로 기본적으로 보이는 배경을 포함한다. iOS, iPadOS, 비전OS, 그리고 macOS의 일부 버튼의 경우, 사람들은 버튼 모양을 사용하여 활성 버튼과 주변 콘텐츠를 더 쉽게 구분할 수 있습니다.
>



**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, visionOS, and watchOS automatically display on/off glyphs within them when people turn on On/Off Labels.

> **시스템 제공 스위치 구성 요소를 선호합니다.** 스위프트UI는 노브의 위치와 채우기 색상으로 상태를 나타내는 스위치를 제공합니다. 그러나 어떤 사람들은 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지를 더 쉽게 알 수 있습니다. 시스템에서 제공하는 스위치를 사용하는 경우 iOS, iPadOS, tvOS, 비전OS, 그리고 시청OS는 사람들이 온/오프 라벨을 켜면 자동으로 그 안에 온/오프 글리프를 표시한다.
>



![An illustration of two switches. The on/off labels are turned off.](https://docs-assets.developer.apple.com/published/a8ffdabefeb92d1f9c364a973ff3a9dc/switches-without-labels@2x.png)Without on/off labels![An illustration of two switches. The on/off labels are turned on.](https://docs-assets.developer.apple.com/published/8020de55fd585edbf1d0733b518a7a7e/switches-with-labels@2x.png)With on/off labels**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.



### [User input](/design/human-interface-guidelines/accessibility#User-input)



**Let people input information by speaking instead of typing or gesturing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.

> **사람들이 타자를 치거나 손짓을 하는 대신 말을 통해 정보를 입력하도록 합니다.** 텍스트 입력 필드에 받아쓰기 버튼을 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기용 마이크 키를 포함해야 합니다.
>



**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about helping people use Siri interactions in your app, see [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri)

> **중요한 작업을 음성으로만 수행할 수 있는 Siri 또는 바로 가기를 지원합니다.** 앱에서 사람들이 Siri 상호작용을 사용할 수 있도록 돕는 방법에 대한 자세한 내용은 [Siri](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/siri) 를 참조하십시오
>

.



**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.

> **가능한 경우, 사람들이 일반 텍스트를 선택하는 것을 막지 마십시오.** 많은 사람들이 번역과 정의를 위한 입력으로 선택된 텍스트를 사용하는 것에 의존합니다.
>



### [Haptics](/design/human-interface-guidelines/accessibility#Haptics)



**Support the system-defined haptics where available.** Many people rely on haptics to help them interact with apps when they can’t see the display. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics)

> **사용 가능한 경우 시스템 정의 햅틱을 지원합니다.** 많은 사람들이 디스플레이를 볼 수 없을 때 앱과 상호작용하는 것을 돕기 위해 햅틱에 의존한다. 예를 들어, 시스템 앱은 작업이 성공 또는 실패했을 때 또는 이벤트가 발생하려고 할 때 사람들에게 알리기 위해 햅틱을 재생한다. 사람들을 혼란스럽게 하지 않도록 앱에서 시스템 정의 햅틱을 일관되게 사용해야 한다. 자세한 내용은 [Haptics 플레이하기](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/playing-haptics) 를 참조하십시오
>

.



Note



In platforms that don’t play haptics, use other ways to provide feedback when people interact with custom objects, such as sound.

> 햅틱을 재생하지 않는 플랫폼에서는 사람들이 소리와 같은 사용자 정의 객체와 상호 작용할 때 다른 방법을 사용하여 피드백을 제공한다.
>



[VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)

-----------------------------------------------------------------------



VoiceOver gives audible descriptions of visible content, helping people get information and navigate when they can’t see the display. In visionOS, VoiceOver uses Spatial Audio to help communicate the location of accessible objects.

> VoiceOver는 표시된 콘텐츠에 대한 청각적 설명을 제공하여 사람들이 디스플레이를 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다. 시야에OS, VoiceOver는 Spatial Audio를 사용하여 접근 가능한 객체의 위치를 전달하는 데 도움이 됩니다.
>



Important



When VoiceOver is on in visionOS, apps that define custom gestures don’t receive hand input by default. Instead, people can perform VoiceOver gestures to explore apps without worrying about an app interpreting their hand input. In VoiceOver’s Direct Gesture mode, VoiceOver doesn’t process its standard gestures, instead letting an app process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> 비전에서 VoiceOver가 켜져 있을 때사용자 지정 제스처를 정의하는 앱인 OS는 기본적으로 손 입력을 받지 않습니다. 대신, 사람들은 자신의 손 입력을 해석하는 앱에 대한 걱정 없이 앱을 탐색하기 위해 보이스 오버 제스처를 수행할 수 있다. 보이스오버의 직접 제스처 모드에서 보이스오버는 표준 제스처를 처리하지 않고 앱이 직접 손 입력을 처리하도록 합니다. 개발자 지침은 [비전 내 접근성 지원 향상]을 참조하십시오OS 앱](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



### [Content descriptions](/design/human-interface-guidelines/accessibility#Content-descriptions)



**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.

> **의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다.** 콘텐츠의 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하도록 합니다. 유용한 설명을 작성하려면 먼저 이미지를 볼 수 있는 사용자에게 설명이 필요한 내용을 보고하십시오. VoiceOver는 이미지와 캡션을 둘러싼 텍스트를 읽으므로 이미지 자체가 전달하는 정보에 설명을 집중하십시오.
>



![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.

![A partial screenshot of a summary screen in the Activity app on iPhone. The activity rings element has a frame around it, representing the active element in VoiceOver.](https://docs-assets.developer.apple.com/published/c6b54e401411a6488486e5b960f05ab5/image-with-alt-text@2x.png)The alternative description for this element is “Moving: 125 percent; Exercise: zero percent; Standing: 58 percent.”**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.



**When an image is purely decorative and isn’t intended to communicate anything important, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.


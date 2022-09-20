# **[Foundations] Accessibility**

### People use Apple’s accessibility features to personalize how they interact with their devices in ways that work for them.
> 사람들은 Apple의 접근성 기능을 사용하여 자신에게 맞는 방식으로 장치와 상호 작용하는 방식을 개인화합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-accessibility-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-accessibility-intro-dark_2x.png)

An accessible app or game supports accessibility personalizations by design and gives everyone a great user experience, regardless of their capabilities or how they use their devices.
> 접근 가능한 앱이나 게임은 설계에 의한 접근성 개인화를 지원하며, 기능이나 기기 사용 방법에 관계없이 모든 사람에게 훌륭한 사용자 경험을 제공한다.
>




Approximately one in seven people have a disability that affects the way they interact with the world and their devices. People can experience disabilities at any age, for any duration, and at varying levels of severity. For example, situational disabilities — such as a wrist injury from a fall or voice loss from overuse — can affect the way almost everyone interacts with their devices at various times.
> 대략 7명 중 1명은 세상과 그들의 기기와의 상호작용 방식에 영향을 미치는 장애를 가지고 있다. 사람들은 어떤 나이, 어떤 기간, 그리고 다양한 수준의 중증도에서 장애를 경험할 수 있다. 예를 들어 낙상으로 인한 손목 부상이나 과다 사용으로 인한 음성 손실과 같은 상황적 장애는 거의 모든 사람이 다양한 시간에 자신의 기기와 상호 작용하는 방식에 영향을 미칠 수 있다.
>




# **Best practices**

**Design with accessibility in mind.** Accessibility is not just about making information available to people with disabilities — it’s about making information available to everyone, regardless of their capabilities or situation. Designing your app with accessibility in mind means prioritizing *simplicity* and *perceivability* and examining every design decision to ensure that it doesn’t exclude people who have different abilities or interact with their devices in different ways.
> 접근성을 염두에 두고 설계합니다. 접근성은 단순히 장애인이 정보를 이용할 수 있도록 하는 것이 아닙니다. 능력이나 상황에 관계없이 모든 사람이 정보를 이용할 수 있도록 하는 것입니다. 접근성을 염두에 두고 앱을 설계한다는 것은 단순성과 인식 가능성을 우선시하고 모든 설계 결정을 검토하여 다른 능력을 갖거나 다른 방식으로 장치와 상호 작용하는 사람들을 배제하지 않도록 하는 것을 의미합니다.
>




**Simplicity** — Enabling familiar, consistent interactions that make complex tasks simple and straightforward to perform.
> 단순성 — 친숙하고 일관된 상호 작용을 통해 복잡한 작업을 단순하고 간편하게 수행할 수 있습니다.
>




**Perceivability** — Making sure that all content can be perceived whether people are using sight, hearing, or touch.
> 인식 가능성 — 사람들이 시각, 청각 또는 촉각을 사용하든 모든 콘텐츠를 인식할 수 있도록 보장합니다.
>




**Support personalization.** You already design your experience to adapt to environmental variations — such as device orientation, screen size, resolution, color gamut, and split view — because you want people to enjoy it in any context and on all supported devices. With minimal additional effort, you can design your app to support the accessibility features people use to personalize the ways they interact with their devices.
> 개인 설정을 지원합니다. 사용자가 모든 컨텍스트와 지원되는 모든 장치에서 사용자 환경을 즐기기를 원하기 때문에 장치 방향, 화면 크기, 해상도, 색역 및 분할 보기와 같은 환경 변화에 적응할 수 있도록 이미 사용자 환경을 설계했습니다. 최소한의 추가 노력으로 사람들이 장치와 상호 작용하는 방식을 개인화하는 데 사용하는 접근성 기능을 지원하도록 앱을 설계할 수 있습니다.
>




When you use standard components to implement your interface, text and controls automatically adapt to several accessibility settings, such as Bold Text, Larger Text, Invert Colors, and Increase Contrast.
> 표준 구성 요소를 사용하여 인터페이스를 구현할 때 텍스트와 컨트롤은 굵은 텍스트, 큰 텍스트, 색 반전, 대비 증가 등의 몇 가지 접근성 설정에 자동으로 적응합니다.
>




**Audit and test your app or game for accessibility.** An audit examines every element in your experience and gives you a comprehensive list of issues to fix. Testing helps you ensure that everyone can complete the most important tasks in your app, no matter how they interact with their devices.
> 앱이나 게임의 접근성을 감사하고 테스트합니다. 감사는 경험의 모든 요소를 검사하고 수정할 문제의 포괄적인 목록을 제공합니다. 테스트를 통해 모든 사용자가 장치와 상호 작용하는 방식에 관계없이 앱에서 가장 중요한 작업을 완료할 수 있습니다.
>




When you test important user flows with accessibility features turned on, you gain an appreciation for the challenges of interacting with a device in different ways. You also discover places where your app might fail to deliver a great user experience.
> 내게 필요한 옵션 기능을 설정한 상태에서 중요한 사용자 흐름을 테스트하면 다양한 방식으로 장치와 상호 작용하는 문제를 이해할 수 있습니다. 또한 앱이 훌륭한 사용자 경험을 제공하지 못할 수 있는 장소도 발견할 수 있습니다.
>




For example, a common user flow in a social media app might be “post a response to a comment.” The tasks that make up this flow could include:
> 예를 들어, 소셜 미디어 앱의 일반적인 사용자 흐름은 "댓글에 대한 응답 게시"일 수 있다. 이 흐름을 구성하는 작업에는 다음이 포함될 수 있습니다.
>




- Read posted comments
- Choose a comment for a response
- >  응답에 대한 주석 선택

- Open the response view
- Edit the response
- Post the response

For each critical user flow in your app or game, turn on an accessibility feature, such as VoiceOver, Reduce Motion, or Large Text Size, and make sure that you can complete every task in the flow without difficulty. After you fix the problems you uncover, turn on a different accessibility feature and run through the user flow again. To help you audit, test, and fix your app or game, consider using Xcode’s Accessibility Inspector.
> 앱이나 게임의 각 중요한 사용자 흐름에 대해 VoiceOver, Reduce Motion 또는 Large Text Size와 같은 내게 필요한 기능을 설정하고 흐름의 모든 작업을 어려움 없이 완료할 수 있는지 확인합니다. 발견한 문제를 해결한 후 다른 내게 필요한 옵션 기능을 설정하고 사용자 흐름을 다시 실행하십시오. 앱이나 게임을 감사, 테스트 및 수정하는 데 도움이 되도록 Xcode의 내게 필요한 옵션 검사기를 사용하는 것을 고려해 보십시오.
>




# **Interactions**

Assistive technologies like VoiceOver, and accessibility features like display accommodations, expand the ways people can interact with their devices. Because these technologies and features integrate with system-provided interactions, it’s essential that you support the system interactions correctly in your app.
> VoiceOver와 같은 보조 기술 및 디스플레이 시설과 같은 접근성 기능은 사람들이 장치와 상호 작용할 수 있는 방법을 확장합니다. 이러한 기술과 기능은 시스템에서 제공하는 상호 작용과 통합되므로 앱에서 시스템 상호 작용을 올바르게 지원하는 것이 중요합니다.
>




# **Gestures**

**Don’t override the platform gestures.** People expect system gestures — such as swiping down to reveal Notification Center or the macOS trackpad gestures available in System Settings — to work regardless of the app they’re using.
> 플랫폼 제스처를 재정의하지 마십시오. Notification Center를 표시하기 위해 아래로 스와이프하는 것과 같은 시스템 제스처나 시스템 설정에서 사용할 수 있는 macOS 트랙패드 제스처가 사용 중인 앱에 관계없이 작동하기를 기대합니다.
>




**Prefer simplified gestures for common interactions.** Complex gestures such as multifinger gestures, long presses, or repeated button presses can be challenging for many people. Using the simplest gestures possible improves the experience for everyone who interacts with your app.
> 일반적인 상호 작용을 위해 간단한 제스처를 선호합니다. 다중 손가락 제스처, 길게 누르기 또는 반복되는 버튼 누름과 같은 복잡한 제스처는 많은 사람들에게 어려울 수 있습니다. 가능한 가장 간단한 제스처를 사용하면 앱과 상호 작용하는 모든 사람의 경험이 향상됩니다.
>




**Provide alternative ways to perform gesture-based actions.** Include an option for people who may not be able to perform a specific gesture. For example, if swiping deletes a row in a table, you can also provide an alternative way to delete items through an edit mode or by offering a Delete button in an item detail view.
> 제스처 기반 작업을 수행할 수 있는 대체 방법을 제공합니다. 특정 제스처를 수행할 수 없는 사용자를 위한 옵션을 포함합니다. 예를 들어, 표에서 행을 삭제하는 경우 편집 모드를 통해 또는 항목 세부 정보 보기에서 삭제 단추를 제공하여 항목을 삭제하는 다른 방법을 제공할 수도 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/edit-button-to-delete_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/edit-button-to-delete_2x.png)

**When possible, make your app’s core functionality accessible through more than one type of physical interaction.** For example, Camera on iPhone and iPad lets people take a photo by tapping the onscreen button or by pressing the device's volume down button. In addition to making photo-capture more convenient for everyone, these alternative interactions provide options to people who might have limited grip strength or dexterity.
> 가능하면 둘 이상의 물리적 상호 작용을 통해 앱의 핵심 기능에 액세스할 수 있도록 하십시오. 예를 들어 iPhone 및 iPad의 Camera를 사용하면 화면 단추를 누르거나 장치의 볼륨 작게 단추를 눌러 사진을 찍을 수 있습니다. 사진 캡처를 모두에게 더 편리하게 하는 것 외에도, 이러한 대안적인 상호작용은 악력이나 손재주가 제한적일 수 있는 사람들에게 선택권을 제공한다.
>




**Make drag and drop accessible in your iOS or iPadOS app.** When you use the accessibility APIs to identify drag sources and drop targets in your app, assistive technologies can help people drag and drop onscreen items. For developer guidance, see [accessibilityDragSourceDescriptors](https://developer.apple.com/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) and [accessibilityDropPointDescriptors](https://developer.apple.com/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor).
> iOS 또는 iPadOS 앱에서 드래그 앤 드롭에 액세스할 수 있도록 합니다. 접근성 API를 사용하여 앱에서 드래그 소스와 드롭 대상을 식별할 때 보조 기술은 사람들이 화면 항목을 드래그 앤 드롭하는 데 도움이 될 수 있습니다. 개발자 지침은 내게 필요한 옵션DragSourceDescriptors 및 내게 필요한 옵션 DropPointDescriptors를 참조하십시오.
>




# **Buttons and controls**

**Give all touchscreen controls and interactive elements a hit target that measures at least 44x44 pt.** People with limited mobility need larger hit targets to help them interact with your app. It can be frustrating to interact with too-small controls in any platform, even when people use a pointer.
> 모든 터치스크린 컨트롤과 대화형 요소에 최소 44x44pt의 적중 목표를 지정하십시오. 이동성이 제한된 사용자는 앱과 상호 작용할 수 있도록 더 큰 적중 목표가 필요합니다. 어떤 플랫폼에서든 너무 작은 컨트롤과 상호작용하는 것은 사람들이 포인터를 사용할 때도 좌절감을 줄 수 있다.
>




**Characterize the accessibility of custom elements.** You can use system APIs to tell assistive technologies how a component behaves. For example, using [button](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620194-button) or [NSAccessibilityButton](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton) to characterize a view as a button means that VoiceOver speaks the view’s description followed by the word *button*, which tells people that the view behaves like a button.
> 사용자 지정 요소의 접근성을 특성화합니다. 시스템 API를 사용하여 구성 요소가 어떻게 동작하는지 보조 기술에 알려줄 수 있습니다. 예를 들어, 버튼 또는 NSA 접근성 버튼을 사용하여 보기를 단추로 특성화한다는 것은 VoiceOver가 보기에 대한 설명을 말하고 단어 버튼이 뒤따른다는 것을 의미하며, 이는 보기가 단추처럼 동작한다는 것을 알려줍니다.
>




**Use a consistent style hierarchy to communicate the relative importance of buttons.** When you use a consistent hierarchy of button styles, people can grasp the importance of buttons based on their appearance. In iOS, iPadOS, and tvOS, for example, you can use the visually prominent filled style for the button that performs the most likely action in a view, using less prominent styles — such as gray or plain — for buttons that enable less important actions. (For developer guidance, see [UIButton.Configuration](https://developer.apple.com/documentation/uikit/uibutton/configuration).) People can also turn on Button Shapes to make it easier to distinguish active buttons from surrounding content.
> 단추의 상대적 중요도를 전달하기 위해 일관된 스타일 계층을 사용합니다. 단추 스타일의 일관된 계층을 사용하면 사람들은 모양에 따라 단추의 중요도를 파악할 수 있습니다. 예를 들어 iOS, iPadOS 및 tvOS에서는 보기에서 가장 가능성이 높은 작업을 수행하는 단추에 시각적으로 두드러지게 채워진 스타일을 사용할 수 있으며, 덜 중요한 작업을 실행하는 단추에는 회색 또는 보통과 같은 덜 두드러지는 스타일을 사용할 수 있습니다.구성). 또한 단추 모양을 설정하여 활성 단추와 주변 내용을 쉽게 구분할 수 있습니다.
>





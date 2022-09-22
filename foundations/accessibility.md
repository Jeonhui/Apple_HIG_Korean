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
- > 게시된 댓글 읽기

- Choose a comment for a response
- >  응답에 대한 주석 선택

- Open the response view
- > 응답 보기 열기

- Edit the response
- > 응답 편집

- Post the response
- > 응답 전송

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




**Prefer the system-provided switch component.** SwiftUI provides a switch that indicates its state by the position of its knob and its fill color. For some people, however, the addition of labels makes it easier to perceive whether a switch is on or off. When you use system-provided switches, iOS, iPadOS, tvOS, and watchOS automatically displays on/off glyphs within them when people turn on On/Off Labels.
> 시스템에서 제공하는 스위치 구성 요소를 선호합니다. SwiftUI는 노브의 위치와 채우기 색상으로 상태를 표시하는 스위치를 제공합니다. 그러나 일부 사람들에게는 라벨을 추가하면 스위치가 켜져 있는지 또는 꺼져 있는지 더 쉽게 인식할 수 있다. 시스템 제공 스위치를 사용하는 경우 iOS, iPadOS, tvOS 및 watchOS는 사람들이 온/오프 라벨을 켜면 자동으로 그 안에 온/오프 글리프를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/switches-without-labels_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/switches-without-labels_2x.png)

Without on/off labels

![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/switches-with-labels_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/switches-with-labels_2x.png)

With on/off labels

**Consider giving links a visual indicator in addition to color, such as an underline.** It’s fine to use color to identify a link, but if you use it as the only indicator, people — such as those with color blindness or cognitive or situational attention impairments — may not be able to perceive the distinction.
> 링크에 밑줄과 같은 색 이외에 시각적 표시기를 제공하는 것을 고려하십시오. 링크를 식별하기 위해 색을 사용하는 것은 괜찮지만 색맹이나 인지적 또는 상황적 주의력 장애가 있는 사람과 같은 사람들은 구별을 인식하지 못할 수 있습니다.
>




# **User input**

**Let people input information by speaking instead of typing.** Adding a dictation button in a text entry field lets people choose speech as their preferred input method. If you create a custom keyboard, be sure to include a microphone key for dictation.
> 텍스트 입력 필드에 받아쓰기 단추를 추가하면 사용자가 선호하는 입력 방법으로 음성을 선택할 수 있습니다. 사용자 지정 키보드를 만드는 경우 받아쓰기를 위한 마이크 키를 포함해야 합니다.
>




**Support Siri or Shortcuts for performing important tasks by voice alone.** To learn more about enabling Siri interactions in your app, see [Siri](../technologies/siri/introduction).
> 음성만으로 중요한 작업을 수행하기 위한 Siri 또는 바로 가기 지원. 앱에서 Siri 상호 작용을 활성화하는 방법에 대한 자세한 내용은 Siri를 참조하십시오.
>




**When possible, don’t prevent people from selecting plain text.** Many people rely on using selected text as input for translations and definitions.
> 가능하면 일반 텍스트를 선택하지 마십시오. 많은 사람들이 선택한 텍스트를 번역 및 정의 입력으로 사용합니다.
>




# **Haptics**

**Support the system-defined haptics.** Many people rely on haptics to help them interact with apps when they can’t see the screen. For example, system apps play haptics to notify people when a task has succeeded or failed or when an event is about to happen. Be sure to use the system-defined haptics consistently in your app so that you don’t confuse people. For guidance, see [Playing haptics](../patterns/playing-haptics).
> 시스템 정의 햅틱을 지원합니다. 많은 사람들이 화면이 보이지 않을 때 앱과 상호 작용할 수 있도록 햅틱을 사용합니다. 예를 들어 시스템 앱은 작업이 성공하거나 실패하거나 이벤트가 발생하려고 할 때 사람들에게 알리기 위해 햅틱을 재생한다. 사람들에게 혼란을 주지 않도록 앱에서 시스템 정의 햅틱을 일관되게 사용해야 한다. 자세한 내용은 햅틱 재생을 참조하십시오.
>




# **VoiceOver**

VoiceOver gives audible descriptions of onscreen content, helping people get information and navigate when they can’t see the screen.
> VoiceOver는 화면 내용에 대한 청각적 설명을 제공하여 사람들이 화면을 볼 수 없을 때 정보를 얻고 탐색할 수 있도록 도와줍니다.
>




# **Content descriptions**

**Provide alternative descriptions for all images that convey meaning.** If you don’t describe the meaningful images in your content, you prevent VoiceOver users from fully experiencing your app. To create a useful description, start by reporting what would be self-explanatory to someone who is able to see the image. Because VoiceOver reads the text surrounding the image and any captions, focus your description on information that’s conveyed by the image itself.
> 의미를 전달하는 모든 이미지에 대한 대체 설명을 제공합니다. 콘텐츠에 의미 있는 이미지를 설명하지 않으면 VoiceOver 사용자가 앱을 완전히 경험하지 못하게 됩니다. 유용한 설명을 작성하려면 먼저 이미지를 볼 수 있는 사용자에게 직접 설명하는 내용을 보고하십시오. VoiceOver는 이미지 주변의 텍스트와 캡션을 읽으므로 이미지 자체에서 전달되는 정보에 설명을 집중합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/image-with-alt-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/image-with-alt-text_2x.png)

The alternative description for this image is “Man and woman signing on FaceTime.”
> 이 이미지에 대한 대체 설명은 "FaceTime에 서명하는 남자와 여자"입니다.
>




**Make infographics fully accessible.** Provide a concise description of the infographic that explains what it conveys. If people can interact with the infographic to get more or different information, you need to make these interactions available to VoiceOver users, too. The accessibility APIs provide ways to represent custom interactive elements so that assistive technologies can help people use them.
> 인포그래픽에 완전히 접근할 수 있도록 합니다. 인포그래픽이 전달하는 의미를 설명하는 인포그래픽에 대한 간결한 설명을 제공하십시오. 사람들이 더 많은 또는 다른 정보를 얻기 위해 인포그래픽과 상호 작용할 수 있다면 VoiceOver 사용자들도 이러한 상호 작용을 사용할 수 있도록 해야 합니다. 접근성 API는 보조 기술이 사람들이 사용하는 데 도움을 줄 수 있도록 사용자 지정 대화형 요소를 표현하는 방법을 제공합니다.
>




**When an image is purely decorative and isn't intended to communicate anything, hide it from assistive technologies.** Making VoiceOver describe a purely decorative image can waste people’s time and add to their cognitive load without providing any benefit.
> 이미지가 순수하게 장식되어 있고 어떤 것도 전달하기 위한 것이 아닐 때, 그것을 보조 기술로부터 숨기세요. 보이스오버가 순수하게 장식된 이미지를 묘사하도록 만드는 것은 사람들의 시간을 낭비하고 아무런 이점도 제공하지 않고 그들의 인지적 부담을 가중시킬 수 있습니다.
>




**Give each screen a unique title and provide headings that identify sections in your information hierarchy.** When people arrive on a screen, the title is the first piece of information they receive from an assistive technology. To help people understand the structure of your app, create a unique title for each screen that succinctly describes its contents or purpose. Similarly, people need accurate section headings to help them build a mental map of the information hierarchy of each screen.
> 각 화면에 고유한 제목을 지정하고 정보 계층에서 섹션을 식별하는 제목을 지정합니다. 사용자가 화면에 도착하면 해당 제목은 보조 기술로부터 받은 첫 번째 정보입니다. 사람들이 앱의 구조를 이해하도록 돕기 위해 각 화면에 대한 내용이나 목적을 간결하게 설명하는 고유한 제목을 만드십시오. 마찬가지로, 사람들은 각 화면의 정보 계층의 마인드 맵을 구축하는 데 도움이 되는 정확한 섹션 표제가 필요하다.
>




**Help everyone enjoy your video and audio content.** When you provide closed captions, audio descriptions, and transcripts, you can help people benefit from audio and video content in ways that work for them.
> 모든 사람이 비디오 및 오디오 콘텐츠를 즐길 수 있도록 지원합니다. 폐쇄 캡션, 오디오 설명 및 스크립트를 제공할 때 사용자에게 적합한 방식으로 오디오 및 비디오 콘텐츠의 혜택을 받을 수 있도록 지원할 수 있습니다.
>




*Closed captions* give people a textual equivalent for the audible information in a video. You can also use closed captions to provide multiple translations for the same content, letting the system choose the version that matches the device’s current settings. Because closed captions aren’t always available, it’s important to provide subtitles, too.
> 폐쇄 캡션은 사람들에게 비디오의 청각 정보에 대해 텍스트로 동등한 것을 제공한다. 또한 폐쇄 캡션을 사용하여 동일한 콘텐츠에 대해 여러 번 번역할 수 있으므로 시스템에서 장치의 현재 설정과 일치하는 버전을 선택할 수 있습니다. 자막을 항상 사용할 수 있는 것은 아니기 때문에 자막을 제공하는 것도 중요합니다.
>




*Audio descriptions* provide a spoken narration of important information that’s presented only visually.
> 오디오 설명은 시각적으로만 표시되는 중요한 정보에 대한 음성 내레이션을 제공합니다.
>




A *transcript* provides a complete textual description of a video, covering both audible and visual information, so that people can enjoy the video in different ways.
> 녹취록은 사람들이 다양한 방법으로 비디오를 즐길 수 있도록 청각과 시각 정보를 모두 포함하는 비디오에 대한 완전한 텍스트 설명을 제공한다.
>




For developer guidance, see [Selecting subtitles and alternative audio tracks](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/selecting_subtitles_and_alternative_audio_tracks).
> 개발자 지침은 자막 및 대체 오디오 트랙 선택을 참조하십시오.
>




# **Navigation**

**Make sure VoiceOver users can navigate to every element.** VoiceOver uses accessibility information from onscreen elements to help people understand the location of each element and what it can do. System-provided UI components include this accessibility information by default, but VoiceOver can’t help people discover and use custom elements unless you provide the information. For developer guidance, see [Accessibility modifiers](https://developer.apple.com/documentation/swiftui/view-accessibility).
> VoiceOver 사용자가 모든 요소를 탐색할 수 있는지 확인합니다. VoiceOver는 화면 요소의 내게 필요한 정보를 사용하여 사람들이 각 요소의 위치와 기능을 이해할 수 있도록 도와줍니다. 시스템에서 제공하는 UI 구성 요소에는 기본적으로 이 접근성 정보가 포함되지만 사용자가 정보를 제공하지 않는 한 VoiceOver는 사용자가 사용자 지정 요소를 검색하고 사용하는 데 도움이 될 수 없습니다. 개발자 지침은 내게 필요한 옵션 수정자를 참조하십시오.
>




**Improve the VoiceOver experience by specifying how elements should be grouped, ordered, or linked.** Proximity, alignment, and other contextual cues can help sighted people perceive the relationships among onscreen elements, but these cues don’t work well for VoiceOver users. Examine your app for places where relationships among elements are visual only, and describe these relationships to VoiceOver.
> 요소 그룹화, 순서 지정 또는 연결 방법을 지정하여 VoiceOver 환경을 개선합니다. 근접성, 정렬 및 기타 상황별 단서는 시각장애인이 화면 요소 간의 관계를 인식하는 데 도움이 될 수 있지만 이러한 단서는 VoiceOver 사용자에게 잘 작동하지 않습니다. 앱에서 요소 간의 관계가 시각적으로만 표시되는 장소를 검사하고 VoiceOver와의 관계를 설명합니다.
>




For example, the layout below relies on proximity and centering to imply that each phrase is a caption for the image above it. However, if you don’t tell VoiceOver that each image should be grouped with its phrase, VoiceOver reads, “A large container holding a variety of mangoes. A large container holding many green artichokes. Mangoes come from trees that belong to the genus Mangifera. Artichokes come from a variety of a species of thistle.” This happens because VoiceOver reads elements from top to bottom by default. For developer guidance, see [shouldGroupAccessibilityChildren](https://developer.apple.com/documentation/objectivec/nsobject/1615143-shouldgroupaccessibilitychildren) and [accessibilityTitleUIElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535155-accessibilitytitleuielement?language=occ).
> 예를 들어, 아래 레이아웃은 각 구문이 위 이미지에 대한 캡션임을 암시하기 위해 근접성과 중심에 의존합니다. 그러나, 만약 당신이 VoiceOver에게 각각의 이미지를 문구와 함께 그룹화해야 한다고 말하지 않는다면, VoiceOver는 "다양한 망고를 담은 큰 용기"라고 읽는다. 많은 녹색 아티초크를 담고 있는 큰 용기. 망고는 망기페라속에 속하는 나무에서 나온다. 아티초크는 엉겅퀴의 다양한 종에서 나옵니다." 이 문제는 VoiceOver가 기본적으로 위에서 아래로 요소를 읽기 때문에 발생합니다. 개발자 지침은 그룹 내게 필요한 옵션 하위 항목 및 내게 필요한 옵션을 참조하십시오.제목 UIElement.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/mangoes_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/mangoes_2x.png)

Mangoes come from trees that belong to the genus Mangifera.
> 망고는 망기페라속에 속하는 나무에서 나온다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/artichokes_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/artichokes_2x.png)

Artichokes come from a variety of a species of thistle.
> 아티초크는 엉겅퀴의 다양한 종에서 나온다.
>




**Tell VoiceOver when onscreen content or layout changes.** An unexpected change in content or layout can be very confusing to VoiceOver users, because it means that their mental map of the screen is no longer accurate. It’s crucial to report onscreen changes so that VoiceOver and other assistive technologies can help people update their understanding of the screen. For developer guidance, see [UIAccessibility.Notification](https://developer.apple.com/documentation/uikit/uiaccessibility/notification) (UIKit) or [NSAccessibility.Notification](https://developer.apple.com/documentation/appkit/nsaccessibility/notification) (AppKit).
> 화면 내용 또는 레이아웃이 변경될 때 VoiceOver에 알립니다. 예상치 못한 내용 또는 레이아웃 변경은 VoiceOver 사용자가 더 이상 화면의 마인드 맵이 정확하지 않다는 것을 의미하기 때문에 매우 혼란스러울 수 있습니다. VoiceOver 및 기타 보조 기술이 사람들이 화면에 대한 이해를 업데이트하는 데 도움이 될 수 있도록 화면 변경 사항을 보고하는 것이 중요합니다. 개발자 지침은 UIAaccessibility를 참조하십시오.알림(UIKit) 또는 NSA 액세스 가능성.알림(AppKit).
>




**Help people predict when a control opens a different webpage or app.** An unexpected change in context can cause confusion and require people to suddenly rebuild their mental model of the onscreen environment. One way to draw attention to a potential change in context is append an ellipsis to a button’s title. Throughout the system, an ellipsis trailing the title is the standard way for a button to communicate that it opens another window or view in which people can complete the action. For example, Mail in iOS and iPadOS appends an ellipsis to the Move Message button, signaling that a separate view opens, listing the destinations people can choose.
> 컨트롤이 다른 웹 페이지나 앱을 열 때 사람들이 예측할 수 있도록 도와줍니다. 예상치 못한 상황 변화는 혼란을 야기할 수 있고 사람들이 갑자기 화면 환경의 마인드 모델을 재구성해야 합니다. 문맥의 잠재적인 변화에 주의를 끄는 한 가지 방법은 단추의 제목에 줄임표를 추가하는 것이다. 시스템 전체에서 줄임표 후행은 사용자가 작업을 완료할 수 있는 다른 창이나 보기를 연다는 것을 알리는 버튼의 표준 방법입니다. 예를 들어 iOS 및 iPadOS의 메일은 메시지 이동 단추에 줄임표를 추가하여 별도의 보기가 열리며 사용자가 선택할 수 있는 수신처를 나열합니다.
>




**Provide alternative text labels for all important interface elements.** Alternative text labels aren’t visible onscreen, but they let VoiceOver audibly describe onscreen elements, making navigation easier for people with visual disabilities. System-provided controls have useful labels by default, but you need to create labels for custom elements. For example, if you create an accessibility element that represents a custom rating button, you might supply the label “Rate.”
> 모든 중요한 인터페이스 요소에 대해 대체 텍스트 레이블을 제공합니다. 대체 텍스트 레이블은 화면에는 표시되지 않지만 VoiceOver에서 화면 요소를 청각적으로 설명할 수 있으므로 시각 장애가 있는 사람들이 쉽게 탐색할 수 있습니다. 시스템에서 제공하는 컨트롤에는 기본적으로 유용한 레이블이 있지만 사용자 정의 요소에 대한 레이블을 만들어야 합니다. 예를 들어, 사용자 정의 등급 단추를 나타내는 접근성 요소를 작성하는 경우 "등급" 레이블을 제공할 수 있습니다.
>




**Support the VoiceOver rotor when necessary.** VoiceOver users can use an onscreen control called the *rotor* to navigate a document or webpage by headings, links, or other section types. The rotor can also bring up the braille keyboard. You can help VoiceOver users navigate among related items in your app by identifying these items to the rotor. For developer guidance, see [UIAccessibilityCustomRotor](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor) and [NSAccessibilityCustomRotor](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor).
> 필요한 경우 VoiceOver 로터를 지원합니다. VoiceOver 사용자는 로터라는 화면 컨트롤을 사용하여 제목, 링크 또는 기타 섹션 유형으로 문서 또는 웹 페이지를 탐색할 수 있습니다. 회전자는 또한 점자 키보드를 올릴 수 있다. VoiceOver 사용자가 로터에 연결된 항목을 식별하여 앱에서 관련 항목 사이를 탐색할 수 있도록 도울 수 있습니다. 개발자 지침은 UIAAccessibilityCustomRotor 및 NSAAccessibilityCustomRotor를 참조하십시오.
>




**In iPadOS and macOS, make sure people can use the keyboard to navigate and interact with all onscreen components in your app.** Ideally, people can turn on Full Keyboard Access and perform every task in your experience using only the keyboard. In addition to [accessibility keyboard shortcuts](https://support.apple.com/en-us/HT204434), the system defines a large number of other [keyboard shortcuts](https://support.apple.com/en-us/HT201236) that many people use all the time. To support all users, it’s important to avoid overriding any system-defined keyboard shortcuts in your app. For guidance, see [Keyboards](../inputs/keyboards).
> iPadOS 및 macOS에서 사용자가 키보드를 사용하여 앱의 모든 화면 구성 요소를 탐색하고 상호 작용할 수 있는지 확인하십시오. 이상적인 경우, 사용자는 전체 키보드 액세스를 설정하고 키보드만 사용하여 사용자 환경의 모든 작업을 수행할 수 있습니다. 접근성 바로 가기 키 외에도, 시스템은 많은 사람들이 항상 사용하는 많은 다른 바로 가기 키를 정의합니다. 모든 사용자를 지원하려면 앱에서 시스템 정의 키보드 단축키를 재정의하지 않는 것이 중요합니다. 자세한 내용은 키보드를 참조하십시오.
>




# **Text display**

**In iOS, iPadOS, tvOS, and watchOS, use Dynamic Type and test that your app’s layout adapts to all font sizes.** Dynamic Type lets people pick the font size that works for them. Verify that your design can scale and that both text and glyphs are legible at all font sizes. On iPhone or iPad, for example, turn on Larger Accessibility Text Sizes in Settings > Accessibility > Display & Text Size > Larger Text, and make sure your app remains comfortably readable. You can download the Dynamic Type size tables in the Sketch, Photoshop, and Adobe XD [Apple Design Resources](https://developer.apple.com/design/resources/) for each platform.
> iOS, iPadOS, tvOS 및 watchOS에서 동적 유형을 사용하여 앱의 레이아웃이 모든 글꼴 크기에 맞게 조정되는지 테스트합니다. 동적 유형을 사용하면 사용자에게 적합한 글꼴 크기를 선택할 수 있습니다. 설계가 축척할 수 있고 텍스트와 글리프가 모든 글꼴 크기에서 읽을 수 있는지 확인합니다. 예를 들어 iPhone 또는 iPad의 경우 설정 > 내게 필요한 옵션 > 디스플레이 및 텍스트 크기 > 큰 텍스트에서 큰 텍스트 크기를 설정하고 앱이 편안하게 읽을 수 있도록 합니다. 각 플랫폼의 스케치, 포토샵 및 Adobe XD Apple Design Resources에서 동적 유형 크기 표를 다운로드할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/small-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/small-text_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/large-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/large-text_2x.png)

**As font size increases, keep text truncation to a minimum.** In general, aim to display as much useful text in the largest accessibility font size as you do in the largest standard font size. Avoid truncating text in scrollable regions unless people can open a separate view to read the rest of the content. You can prevent text truncation in a label by configuring it to use as many lines as needed to display a useful amount of text; for developer guidance, see [numberOfLines](https://developer.apple.com/documentation/uikit/uilabel/1620539-numberoflines).
> 글꼴 크기가 커지면 텍스트 잘라내기를 최소화하십시오. 일반적으로 가장 큰 표준 글꼴 크기만큼 유용한 텍스트를 가장 큰 내게 필요한 글꼴 크기로 표시하도록 합니다. 다른 보기를 열어 나머지 내용을 읽을 수 없는 경우 스크롤 가능한 영역에서 텍스트를 잘라내지 마십시오. 유용한 양의 텍스트를 표시하는 데 필요한 만큼 많은 줄을 사용하도록 구성하여 레이블에서 텍스트 잘라내기를 방지할 수 있습니다. 개발자 지침은 numberOfLines를 참조하십시오.
>




**Consider adjusting layout at large font sizes.** When font size increases, inline items and container boundaries can crowd text, making it less readable. For example, if you display text inline with secondary items — such as glyphs or timestamps — the text has less horizontal space. At large font sizes, an inline layout might cause text to truncate or result in overlapping text and secondary items. In this case, consider using a stacked layout where the text appears above the secondary items. Similarly, multiple columns of text can become less readable at large font sizes because each column constrains horizontal space. In this case, consider reducing the number of columns when font size increases to avoid text truncation and improve overall readability. For developer guidance, see [isAccessibilityCategory](https://developer.apple.com/documentation/uikit/uicontentsizecategory/2897444-isaccessibilitycategory).
> 큰 글꼴 크기로 레이아웃을 조정하는 것을 고려하십시오. 글꼴 크기가 커지면 인라인 항목과 컨테이너 경계가 텍스트를 혼잡하게 하여 가독성이 떨어질 수 있습니다. 예를 들어, 텍스트를 보조 항목(예: 글리프 또는 타임스탬프)과 함께 인라인으로 표시할 경우 텍스트의 수평 공간이 줄어듭니다. 큰 글꼴 크기에서는 인라인 레이아웃으로 인해 텍스트가 잘리거나 텍스트와 보조 항목이 겹칠 수 있습니다. 이 경우 텍스트가 보조 항목 위에 나타나는 스택형 레이아웃을 사용하는 것이 좋습니다. 마찬가지로, 각 열은 수평 공간을 제한하기 때문에 큰 글꼴 크기에서는 텍스트의 여러 열이 읽기 어려워질 수 있습니다. 이 경우 글꼴 크기가 증가할 때 열 수를 줄여 텍스트 잘라내기를 방지하고 전체 가독성을 향상시키십시오. 개발자 지침은 내게 필요한 옵션 범주를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/inline-layout_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/inline-layout_2x.png)

At smaller text sizes, Mail displays the date inline with the sender’s name.
> 텍스트 크기가 작을수록 메일은 발신인 이름과 함께 날짜를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/stacked-layout_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/stacked-layout_2x.png)

At the largest accessibility text size, Mail displays the date below the recipient’s name.
> 접근성 텍스트 크기가 가장 큰 메일은 수신인 이름 아래에 날짜를 표시합니다.
>




**Increase the size of meaningful interface icons as font size increases.** If you use interface icons to communicate important information, make sure they are easy to view at larger font sizes, too. When you use [SF Symbols](../foundations/sf-symbols/), you get icons that scale automatically with Dynamic Type size changes.
> 글꼴 크기가 커질수록 의미 있는 인터페이스 아이콘의 크기를 늘립니다. 중요한 정보를 전달하기 위해 인터페이스 아이콘을 사용하는 경우 더 큰 글꼴 크기로도 쉽게 볼 수 있도록 하십시오. SF 기호를 사용하면 동적 유형 크기 변경에 따라 자동으로 크기가 조정되는 아이콘을 볼 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/icons-small_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/icons-small_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/icons-large_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/icons-large_2x.png)

**Maintain a consistent information hierarchy regardless of the current font size.** For example, keep primary elements toward the top of the screen even when the font size is very large, so that people don’t lose track of these elements.
> 예를 들어 글꼴 크기가 매우 큰 경우에도 기본 요소를 화면 맨 위로 유지하여 사용자가 이러한 요소를 놓치지 않도록 합니다.
>




**Prefer regular or heavy font weights in your app.** Consider using Regular, Medium, Semibold, or Bold font weights, because they are easier to see. Avoid Ultralight, Thin, and Light font weights, which can be more difficult to see.
> 앱에서 일반 글꼴이나 무거운 글꼴을 선호합니다. 일반 글꼴, 중간 글꼴, 세미볼드 글꼴 또는 굵은 글꼴을 사용하는 것을 고려하십시오. 보기 쉽기 때문입니다. 보기 어려울 수 있는 초경량, 얇은 글꼴 및 가벼운 글꼴 가중치는 피합니다.
>




**Ensure your app responds correctly and looks good when people enable bold text.** In iOS, iPadOS, tvOS, and watchOS, people turn on the bold text accessibility setting to make text and symbols easier to see. In response, your app should make all text bolder and give all glyphs an increased stroke weight. The system fonts and SF symbols automatically adjust to the bold text accessibility setting.
> iOS, iPadOS, tvOS 및 watchOS에서는 텍스트와 기호를 보다 쉽게 볼 수 있도록 굵은 텍스트 접근성 설정을 켭니다. 이에 대응하여, 당신의 앱은 모든 텍스트를 더 굵게 만들고 모든 글리프에 증가된 스트로크 가중치를 부여해야 한다. 시스템 글꼴 및 SF 기호는 굵은 텍스트 접근성 설정으로 자동으로 조정됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/bold-off_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/bold-off_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/bold-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/images/bold-text_2x.png)

**Make sure custom fonts are legible.** Custom typefaces can sometimes be difficult to read. Unless your app has a compelling need for a custom font, such as for branding purposes or to create an immersive gaming experience, it’s usually best to use the system fonts. If you do use a custom font, make sure it’s easy to read, even at small sizes.
> 사용자 정의 글꼴이 읽기 쉬운지 확인하십시오. 사용자 정의 글꼴은 때때로 읽기 어려울 수 있습니다. 브랜딩 목적이나 몰입형 게임 환경을 만드는 것과 같은 사용자 지정 글꼴에 대한 강력한 요구가 앱에 없는 한, 일반적으로 시스템 글꼴을 사용하는 것이 가장 좋습니다. 사용자 지정 글꼴을 사용하는 경우 작은 크기에서도 쉽게 읽을 수 있도록 합니다.
>




**Avoid full text justification.** The whitespace created by fully justified text can create patterns that make it difficult for many people to read and focus on the text. Left justification — or right justification in right-to-left languages — provides a framing reference for people with learning and literacy challenges, such as dyslexia.
> 전체 텍스트 정당성을 사용하지 마십시오. 완전히 정당화된 텍스트로 만들어진 공백은 많은 사람들이 텍스트를 읽고 집중하기 어렵게 만드는 패턴을 만들 수 있습니다. 왼쪽 정당성 또는 오른쪽에서 왼쪽 언어에서 오른쪽 정당성은 난독증과 같은 학습 및 문해력 문제를 가진 사람들에게 프레임 참조를 제공합니다.
>




**Avoid using italics or all caps for long passages of text.** Italics and all caps are great for occasional emphasis, but overuse of these styles makes text hard to read.
> 텍스트의 긴 구절에는 기울임꼴 또는 모든 캡을 사용하지 마십시오. 기울임꼴과 모든 캡은 가끔 강조할 때는 좋지만 이러한 스타일을 과도하게 사용하면 텍스트를 읽기 어렵습니다.
>




# **Color and effects**

**Don’t rely solely on color to differentiate between objects or communicate important information.** If you use color to convey information, be sure to provide text labels or glyph shapes to help everyone perceive it.
> 사물을 구별하거나 중요한 정보를 전달하기 위해 색상에만 의존하지 말고, 정보를 전달하기 위해 색상을 사용할 경우 모든 사람이 인식할 수 있도록 텍스트 레이블이나 글리프 모양을 제공해야 합니다.
>




**Prefer system colors for text.** When you use system colors in text, it responds correctly to accessibility settings such as Invert Colors and Increase Contrast.
> 텍스트에 시스템 색상을 선호합니다. 텍스트에서 시스템 색상을 사용하면 색 반전 및 대비 증가와 같은 내게 필요한 옵션 설정에 올바르게 응답합니다.
>




**Avoid using color combinations as the only way to distinguish between two states or values.** Many colorblind people find it difficult to distinguish blue from orange; other problematic combinations are red and green, red and black, and either red or green combined with gray. When it makes sense to use a combination of colors to communicate states or values, include additional visual indicators so everyone can perceive the information. For example, instead of using red and green circles to indicate offline and online, you could use a red square and a green circle. Some image-editing software includes tools that can help you proof for colorblindness.
> 두 상태 또는 값을 구별하는 유일한 방법으로 색상 조합을 사용하지 마십시오. 많은 색맹인들은 파란색과 주황색을 구별하는 것을 어려워합니다. 다른 문제가 있는 조합은 빨간색과 녹색, 빨간색과 검은색, 빨간색과 녹색이 회색과 결합됩니다. 상태나 값을 전달하기 위해 색상 조합을 사용하는 것이 타당할 경우, 모든 사람이 정보를 인식할 수 있도록 추가 시각적 표시기를 포함시킨다. 예를 들어, 빨간색과 녹색 원을 사용하여 오프라인과 온라인 상태를 나타내는 대신 빨간색 사각형과 녹색 원을 사용할 수 있습니다. 일부 이미지 편집 소프트웨어에는 색맹을 입증하는 데 도움이 되는 도구가 포함되어 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/ios/images/colorBlindness_fullColor_2x.png](https://developer.apple.com/design/human-interface-guidelines/ios/images/colorBlindness_fullColor_2x.png)

As seen without colorblindness.

![https://developer.apple.com/design/human-interface-guidelines/ios/images/colorBlindness_Protanopia_2x.png](https://developer.apple.com/design/human-interface-guidelines/ios/images/colorBlindness_Protanopia_2x.png)

As seen with red-green colorblindness.

**Ensure your views respond correctly to Invert Colors.** People can turn on Invert Colors when they prefer to view items on a dark background. In the Smart Invert mode of Invert Colors, images, video, and full-color icons (such as app icons and nontemplate images) don’t invert, and dark UI stays dark. Test your app or game to find places where you might need to prevent an image — like a photo in a custom view — from inverting.
> 보기가 색 반전(Invert Colors)에 올바르게 응답하는지 확인하십시오. 어두운 배경의 항목을 보고 싶을 때 색 반전(Invert Colors)을 설정할 수 있습니다. 색 반전(Invert Colors)의 스마트 반전(Smart Invert) 모드에서는 이미지, 비디오 및 전체 색상 아이콘(예: 앱 아이콘 및 템플릿이 아닌 이미지)이 반전되지 않고 어두운 UI가 어둡게 유지됩니다. 사용자 지정 보기에 있는 사진과 같이 이미지가 반전되지 않도록 해야 할 수 있는 장소를 찾기 위해 앱이나 게임을 테스트합니다.
>




**Use strongly contrasting colors to improve readability.** Many factors affect the perception of color, including font size and weight, color brightness, screen resolution, and lighting conditions. When you increase color contrast of visual elements like text, glyphs, and controls, you can help more people use your app in more situations. To find out if the contrast of adjacent colors in your UI meets minimum acceptable levels, you can use Xcode’s Accessibility Inspector or an online color calculator based on the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/) color contrast formula. In general, smaller or lighter-weight text needs to have greater contrast to be legible. Use the following values for guidance.
> 글꼴 크기 및 무게, 색 밝기, 화면 해상도, 조명 상태 등 다양한 요소가 색 인식에 영향을 미칩니다. 텍스트, 글리프 및 컨트롤과 같은 시각적 요소의 색상 대비를 높이면 더 많은 사람들이 더 많은 상황에서 앱을 사용할 수 있도록 도울 수 있습니다. UI에서 인접한 색 대비가 최소 허용 수준을 충족하는지 확인하려면 Xcode의 내게 필요한 옵션 검사기 또는 WCAG(Web Content 내게 필요한 옵션 지침) 색 대비 공식에 기반한 온라인 색 계산기를 사용할 수 있습니다. 일반적으로 더 작거나 가벼운 텍스트는 읽기 쉽도록 더 큰 대비를 가질 필요가 있다. 다음 값을 지침으로 사용합니다.
>




**Avoid requiring animations unless they’re essential for your experience.** In general, let people use your app without relying on any animations.
> 일반적으로 애니메이션에 의존하지 않고 앱을 사용할 수 있도록 합니다.
>




**Play tightened animations when Reduce Motion is on.** People can turn on Reduce Motion if they tend to get distracted or experience dizziness or nausea when viewing animations that include effects such as zooming, scaling, spinning, or peripheral motion. In response to this setting, you need to turn off or reduce animations that are known to cause problems (to learn more, see [Responsive design for motion](https://webkit.org/blog/7551/responsive-design-for-motion/)). If you use a problematic animation to communicate important information, consider designing a non animated alternative or tightening the physics of the animation to reduce its motion. For example:
> 줌, 스케일링, 회전 또는 주변 움직임과 같은 효과를 포함하는 애니메이션을 볼 때 주의가 산만해지거나 어지러움이나 메스꺼움을 느낄 경우 모션 감소 기능을 설정할 수 있습니다. 이 설정에 대응하려면 문제를 일으키는 것으로 알려진 애니메이션을 끄거나 줄여야 합니다(자세한 내용은 동작에 대한 반응 설계 참조). 문제가 있는 애니메이션을 사용하여 중요한 정보를 전달할 경우 애니메이션이 아닌 대체 애니메이션을 설계하거나 애니메이션의 물리학을 조여 움직임을 줄이는 것을 고려해 보십시오. 예:
>




- Tighten springs to reduce bounce effects or track 1:1 with the user’s finger
- >  스프링을 조여 바운스 효과를 줄이거나 사용자의 손가락으로 1:1 트랙을 합니다.

- Avoid animating depth changes in z-axis layers
- >  z축 도면층의 깊이 변경 애니메이션 방지

- Avoid animating into or out of blurs
- >  애니메이션이 흐려지거나 흐려지지 않도록 합니다.

- Replace a slide with a fade to avoid motion
- >  움직임을 방지하기 위해 슬라이드를 페이드로 바꿉니다.


**Let people control video and other motion effects.** Avoid autoplaying video or effects without also providing a button or other way to control them.
> 사람들이 비디오 및 기타 모션 효과를 제어할 수 있도록 합니다. 버튼이나 다른 제어 방법을 제공하지 않고 비디오 또는 효과를 자동 재생하는 것을 피하십시오.
>




**Be cautious when displaying moving or blinking elements.** Although subtle movement and blinking can draw people’s attention, these effects can also be distracting and they aren’t useful for people with visual disabilities. Worse, some blinking elements can cause epileptic episodes. In all cases, avoid using movement and blinking as the only way to convey information.
> 움직이는 요소나 깜빡이는 요소를 표시할 때 주의하세요. 비록 미묘한 움직임과 깜박임이 사람들의 주의를 끌 수 있지만, 이러한 효과들은 또한 산만할 수 있고 시각 장애가 있는 사람들에게 유용하지 않습니다. 더 나쁜 것은, 일부 깜박이는 요소들이 간질 증상을 일으킬 수 있다는 것이다. 모든 경우, 정보를 전달하는 유일한 방법으로 움직임과 깜박임을 사용하지 마십시오.
>




**Change blurring and transparency when people turn on Reduce Transparency.** For example, make areas of blurred content and translucency mostly opaque. For best results, use a color value in the opaque area that’s different from the original color value you used when the area was blurred or translucent.
> 예를 들어, 투명도 감소를 설정하면 흐릿한 내용과 투명도가 대부분 불투명하게 됩니다. 최상의 결과를 얻으려면 영역이 흐리거나 반투명할 때 사용한 원래 색상 값과 다른 불투명 영역의 색상 값을 사용하십시오.
>




| Text size | Text weight | Minimum contrast ratio |
| --- | --- | --- |
| Up to 17 points | All | 4.5:1 |
| 18점 이상 | 모두 | 3:1 |
| All | Bold | 3:1 |
| 모두 | 굵은 글씨 | 3:1 |




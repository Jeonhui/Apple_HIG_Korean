### [[Foundations](./translated-human-interface-guidelines-markdown/foundations.md)]  
  
# **Accessibility**  


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

> **이미지가 순수하게 장식적이고 중요한 정보를 전달하기 위한 것이 아닐 때는 보조 기술로부터 숨깁니다.** VoiceOver가 순수하게 장식적인 이미지를 묘사하도록 만드는 것은 사람들의 시간을 낭비하고 어떠한 이점도 제공하지 않으면서 그들의 인지 부하를 가중시킬 수 있다.
>



**Give each page a unique title and provide headings that identify sections in your information hierarchy.** When people arrive on a page, the title is the first piece of information they receive from an assistive technology. To help people understand the structure of your app, create a unique title for each page that succinctly describes its contents or purpose. Similarly, people need accurate section headings to help them build a mental map of the information hierarchy of each page.

> **각 페이지에 고유한 제목을 지정하고 정보 계층의 섹션을 식별하는 제목을 지정합니다.** 사람들이 페이지에 도착하면, 제목은 보조 기술로부터 받는 첫 번째 정보입니다. 앱의 구조를 사람들이 이해할 수 있도록 도와주려면, 앱의 내용이나 목적을 간결하게 설명하는 각 페이지에 대한 고유한 제목을 만드십시오. 마찬가지로, 사람들은 각 페이지의 정보 계층에 대한 마인드 맵을 구축하는 데 도움이 되는 정확한 섹션 제목이 필요하다.
>



**Help everyone enjoy your video and audio content.** When you provide closed captions, audio descriptions, and transcripts, you can help people benefit from audio and video content in ways that work for them.

> **모두가 비디오 및 오디오 컨텐츠를 즐길 수 있도록 도와주세요.** 폐쇄 캡션, 오디오 설명 및 스크립트를 제공하면 사용자에게 적합한 방식으로 오디오 및 비디오 컨텐츠의 이점을 제공할 수 있습니다.
>



*Closed captions* give people a textual equivalent for the audible information in a video. You can also use closed captions to provide multiple translations for the same content, letting the system choose the version that matches the device’s current settings. Because closed captions aren’t always available, it’s important to provide subtitles, too.

> *폐쇄 캡션*은 사람들에게 동영상의 청각적 정보에 해당하는 텍스트를 제공합니다. 또한 폐쇄 캡션을 사용하여 동일한 콘텐츠에 대해 여러 개의 번역을 제공하여 시스템이 장치의 현재 설정과 일치하는 버전을 선택할 수 있습니다. 닫힌 캡션을 항상 사용할 수 있는 것은 아니기 때문에 자막을 제공하는 것도 중요합니다.
>



*Audio descriptions* provide a spoken narration of important information that’s presented only visually.

> *오디오 설명*은 시각적으로만 제공되는 중요한 정보의 음성 내레이션을 제공합니다.
>



A *transcript* provides a complete textual description of a video, covering both audible and visual information, so that people can enjoy the video in different ways.

> *스크립트*는 청각적 정보와 시각적 정보를 모두 포함하는 동영상에 대한 완전한 텍스트 설명을 제공하여 사람들이 다양한 방식으로 동영상을 즐길 수 있도록 한다.
>



For developer guidance, see [Selecting Subtitles and Alternative Audio Tracks](https://developer.apple.com/design/human-interface-guidelines/documentation/avfoundation/media_playback/selecting_subtitles_and_alternative_audio_tracks)

> 개발자 안내는 [자막 및 대체 오디오 트랙 선택](https://developer.apple.com/design/human-interface-guidelines/documentation/avfoundation/media_playback/selecting_subtitles_and_alternative_audio_tracks) 을 참조하십시오
>

.



### [Navigation](/design/human-interface-guidelines/accessibility#Navigation)



**Make sure VoiceOver users can navigate to every element.** VoiceOver uses accessibility information from UI elements to help people understand the location of each element and what it can do. System-provided UI components include this accessibility information by default, but VoiceOver can’t help people discover and use custom elements unless you provide the information. For developer guidance, see [Accessibility modifiers](https://developer.apple.com/design/human-interface-guidelines/documentation/SwiftUI/View-Accessibility)

> **VoiceOver 사용자가 모든 요소를 탐색할 수 있는지 확인합니다.** VoiceOver는 UI 요소의 접근성 정보를 사용하여 사람들이 각 요소의 위치와 기능을 이해할 수 있도록 도와줍니다. 시스템 제공 UI 구성 요소에는 기본적으로 이 접근성 정보가 포함되어 있지만, 사용자가 정보를 제공하지 않는 한 VoiceOver는 사용자 지정 요소를 검색하고 사용하는 데 도움이 되지 않습니다. 개발자 지침은 [접근성 수식어](https://developer.apple.com/design/human-interface-guidelines/documentation/SwiftUI/View-Accessibility) 를 참조하십시오
>

.



**Improve the VoiceOver experience by specifying how elements are grouped, ordered, or linked.** Proximity, alignment, and other contextual cues can help sighted people perceive the relationships among visible elements, but these cues don’t work well for VoiceOver users. Examine your app for places where relationships among elements are visual only, and describe these relationships to VoiceOver.

**Improve the VoiceOver experience by specifying how elements are grouped, ordered, or linked.** Proximity, alignment, and other contextual cues can help sighted people perceive the relationships among visible elements, but these cues don’t work well for VoiceOver users. Examine your app for places where relationships among elements are visual only, and describe these relationships to VoiceOver.

> **요소를 그룹화, 순서화 또는 연결하는 방법을 지정하여 VoiceOver 환경을 개선합니다.** 근접성, 정렬 및 기타 맥락적 신호는 시력이 있는 사람들이 가시적 요소 간의 관계를 인식하는 데 도움이 될 수 있지만 이러한 신호는 VoiceOver 사용자에게는 잘 작동하지 않는다. 앱에서 요소 간의 관계가 시각적으로만 표시되는 장소를 검사하고 이러한 VoiceOver와의 관계를 설명합니다.
>



For example, the layout below relies on proximity and centering to imply that each phrase is a caption for the image above it. However, if you don’t tell VoiceOver that each image needs to be grouped with its phrase, VoiceOver reads, “A large container holding a variety of mangoes. A large container holding many green artichokes. Mangoes come from trees that belong to the genus Mangifera. Artichokes come from a variety of a species of thistle.” This happens because VoiceOver reads elements from top to bottom by default. For developer guidance, see [`shouldGroupAccessibilityChildren`](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/1615143-shouldgroupaccessibilitychildren)

> 예를 들어, 아래의 레이아웃은 근접성과 중심에 의존하여 각각의 구가 위의 이미지에 대한 캡션임을 암시합니다. 그러나 각 이미지가 해당 문구와 함께 그룹화되어야 한다는 것을 보이스오버에 말하지 않으면 보이스오버는 "다양한 망고를 담는 큰 컨테이너. 초록색 아티초크가 많이 들어있는 커다란 용기. 망고는 망기페라속에 속하는 나무에서 나온다. 아티초크는 엉겅퀴의 다양한 종이다." 이것은 VoiceOver가 기본적으로 요소를 위에서 아래로 읽기 때문에 발생합니다. 개발자 지침은 ['s should Group Accessibility Children'](https://developer.apple.com/design/human-interface-guidelines/documentation/objectivec/nsobject/1615143-shouldgroupaccessibilitychildren) 을 참조하십시오
>

 and [`accessibilityTitleUIElement`](/documentation/appkit/nsaccessibility/1535155-accessibilitytitleuielement)

.



![An image of a large container holding a variety of mangoes.](https://docs-assets.developer.apple.com/published/1658b1444c6743131c2cb5513a14eb08/mangoes@2x.png)Mangoes come from trees that belong to the genus Mangifera.![An image of a large container holding many green artichokes.](https://docs-assets.developer.apple.com/published/5750c7d12cf60f5054ec8c367ec98612/artichokes@2x.png)Artichokes come from a variety of a species of thistle.**Tell VoiceOver when visible content or layout changes.** An unexpected change in content or layout can be very confusing to VoiceOver users, because it means that their mental map of the content is no longer accurate. It’s crucial to report visible changes so that VoiceOver and other assistive technologies can help people update their understanding of the content. For developer guidance, see [`UIAccessibility.Notification`](/documentation/uikit/uiaccessibility/notification)

 (UIKit) or [`NSAccessibility.Notification`](/documentation/appkit/nsaccessibility/notification)

 (AppKit).



**Help people predict when a control opens a different webpage or app.** An unexpected change in context can cause confusion and require people to suddenly rebuild their mental model of the current experience. One way to draw attention to a potential change in context is append an ellipsis to a button’s title. Throughout the system, an ellipsis trailing the title is the standard way for a button to communicate that it opens another window or view in which people can complete the action. For example, Mail in iOS and iPadOS appends an ellipsis to the Move Message button, signaling that a separate view opens, listing the destinations people can choose.

> **컨트롤이 다른 웹 페이지나 앱을 열 때 사람들이 예측할 수 있도록 도와줍니다.** 예기치 않은 맥락의 변화는 혼란을 야기할 수 있고 사람들이 갑자기 현재 경험에 대한 정신 모델을 재구성해야 한다. 문맥의 잠재적인 변화에 주의를 끄는 한 가지 방법은 단추의 제목에 생략부호를 추가하는 것이다. 시스템 전체에서 제목 뒤에 오는 생략형은 버튼이 사람들이 동작을 완료할 수 있는 또 다른 창이나 보기를 연다는 것을 전달하는 표준 방법이다. 예를 들어, iOS 및 iPadOS의 메일은 메시지 이동 버튼에 타원을 추가하여 별도의 보기가 열리고 사용자가 선택할 수 있는 수신처가 표시됩니다.
>



**Provide alternative text labels for all important interface elements.** Alternative text labels aren’t visible, but they let VoiceOver audibly describe app elements, making navigation easier for people with visual disabilities. System-provided controls have useful labels by default, but you need to create labels for custom elements. For example, if you create an accessibility element that represents a custom rating button, you might supply the label “Rate.”

> **모든 중요한 인터페이스 요소에 대해 대체 텍스트 레이블을 제공합니다.** 대체 텍스트 레이블은 보이지 않지만 VoiceOver에서 앱 요소를 소리로 설명할 수 있으므로 시각 장애인이 쉽게 탐색할 수 있습니다. 시스템 제공 컨트롤에는 기본적으로 유용한 레이블이 있지만 사용자 지정 요소에 대한 레이블을 만들어야 합니다. 예를 들어 사용자 정의 등급 단추를 나타내는 내게 필요한 접근성 요소를 작성하는 경우 "레이트"라는 레이블을 제공할 수 있습니다
>



**Support the VoiceOver rotor when necessary.** VoiceOver users can use a control called the *rotor* to navigate a document or webpage by headings, links, or other section types. The rotor can also bring up the braille keyboard. You can help VoiceOver users navigate among related items in your app by identifying these items to the rotor. For developer guidance, see [`UIAccessibilityCustomRotor`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomrotor)

> **필요한 경우 VoiceOver 로터를 지원합니다.** VoiceOver 사용자는 *rotor*라는 컨트롤을 사용하여 제목, 링크 또는 기타 섹션 유형으로 문서 또는 웹 페이지를 탐색할 수 있습니다. 회전자는 점자 키보드를 올릴 수도 있다. VoiceOver 사용자가 회전자에 연결된 항목을 식별하여 앱의 관련 항목을 탐색하도록 도울 수 있습니다. 개발자 안내는 ['UIA Accessibility CustomRotor'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uiaccessibilitycustomrotor) 를 참조하십시오
>

 and [`NSAccessibilityCustomRotor`](/documentation/appkit/nsaccessibilitycustomrotor)

.



**In iPadOS, macOS, and visionOS, make sure people can use the keyboard to navigate and interact with all components in your app.** Ideally, people can turn on Full Keyboard Access and perform every task in your experience using only the keyboard. In addition to [accessibility keyboard shortcuts](https://support.apple.com/en-us/HT204434)

> **iPadOS, macOS 및 비전OS에서 사용자가 키보드를 사용하여 앱의 모든 구성 요소를 탐색하고 상호 작용할 수 있는지 확인하십시오.** 이상적으로, 사람들은 전체 키보드 액세스를 켜고 키보드만 사용하여 사용자 경험의 모든 작업을 수행할 수 있습니다. [접근성 키보드 바로가기] 외에도 (https://support.apple.com/en-us/HT204434)
>

, the system defines a large number of other [keyboard shortcuts](https://support.apple.com/en-us/HT201236)

> , 시스템은 많은 수의 다른 [바로가기](https://support.apple.com/en-us/HT201236) 를 정의합니다
>

 that many people use all the time. To support everyone, it’s important to avoid overriding any system-defined keyboard shortcuts in your app. For guidance, see [Keyboards](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/keyboards)

> 많은 사람들이 항상 사용하는 것. 모든 사람을 지원하려면 앱에서 시스템 정의 키보드 바로 가기를 재정의하지 않는 것이 중요합니다. 자세한 내용은 [키보드](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/keyboards) 를 참조하십시오
>

.



[Text display](/design/human-interface-guidelines/accessibility#Text-display)

-----------------------------------------------------------------------------



**In iOS, iPadOS, tvOS, visionOS, and watchOS, use Dynamic Type and test that your app’s layout adapts to all font sizes.** Dynamic Type lets people pick the font size that works for them. Verify that your design can scale and that both text and glyphs are legible at all font sizes. On iPhone or iPad, for example, turn on Larger Accessibility Text Sizes in Settings > Accessibility > Display & Text Size > Larger Text, and make sure your app remains comfortably readable. You can download the Dynamic Type size tables in [Apple Design Resources](https://developer.apple.com/design/resources/)

> **iOS, iPadOS, tvOS, 비전에서OS 및 watch OS는 동적 유형을 사용하여 앱의 레이아웃이 모든 글꼴 크기에 맞게 조정되는지 테스트합니다.** 동적 유형을 사용하면 사용자에게 적합한 글꼴 크기를 선택할 수 있습니다. 디자인이 확장 가능한지, 텍스트와 글리프 모두 모든 글꼴 크기에서 읽을 수 있는지 확인합니다. 예를 들어 아이폰이나 아이패드에서 설정 > 내게 필요한 접근성 > 디스플레이 & 텍스트 크기 > 큰 텍스트에서 큰 접근성 텍스트 크기를 설정하고 앱을 편하게 읽을 수 있도록 하십시오. [Apple Design Resources](https://developer.apple.com/design/resources/) 에서 동적 유형 크기 표를 다운로드할 수 있습니다
>

 for each platform.



![A screenshot of a Mail message without bold text.](https://docs-assets.developer.apple.com/published/f7d78e2c7726efc7845bc45e660e694e/regular-view@2x.png)![A screenshot of a Mail message on iPhone, using a large accessibility font size.](https://docs-assets.developer.apple.com/published/95a77147a6b6ed47726b28a22f20f446/large-text@2x.png)**As font size increases, keep text truncation to a minimum.** In general, aim to display as much useful text in the largest accessibility font size as you do in the largest standard font size. Avoid truncating text in scrollable regions unless people can open a separate view to read the rest of the content. You can prevent text truncation in a label by configuring it to use as many lines as needed to display a useful amount of text; for developer guidance, see [`numberOfLines`](/documentation/uikit/uilabel/1620539-numberoflines)

.



**Consider adjusting layout at large font sizes.** When font size increases in a horizontally constrained context, inline items and container boundaries can crowd text, making it less readable. For example, if you display text inline with secondary items — such as glyphs or timestamps — the text has less horizontal space. At large font sizes, an inline layout might cause text to truncate or result in overlapping text and secondary items. In this case, consider using a stacked layout where the text appears above the secondary items. Similarly, multiple columns of text can become less readable at large font sizes because each column constrains horizontal space. In this case, consider reducing the number of columns when font size increases to avoid text truncation and improve overall readability. For developer guidance, see [`isAccessibilityCategory`](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uicontentsizecategory/2897444-isaccessibilitycategory)

> **큰 글꼴 크기로 레이아웃을 조정하는 것을 고려하십시오.** 가로로 제한된 컨텍스트에서 글꼴 크기가 증가하면 인라인 항목과 컨테이너 경계가 텍스트를 크라우드할 수 있으므로 가독성이 떨어질 수 있습니다. 예를 들어 글리프 또는 타임스탬프와 같은 보조 항목과 함께 텍스트를 인라인으로 표시하는 경우 텍스트의 수평 공간이 줄어듭니다. 큰 글꼴 크기에서 인라인 레이아웃은 텍스트를 잘라내거나 텍스트와 보조 항목이 겹칠 수 있습니다. 이 경우 텍스트가 보조 항목 위에 나타나는 스택 레이아웃을 사용하는 것을 고려하십시오. 마찬가지로, 텍스트의 여러 열은 각각의 열이 수평 공간을 제약하기 때문에 큰 글꼴 크기에서 가독성이 떨어질 수 있다. 이 경우 텍스트 잘림을 방지하고 전반적인 가독성을 향상시키기 위해 글꼴 크기가 증가할 때 열 수를 줄이는 것을 고려하십시오. 개발자 지침은 ['is Accessibility Category'](https://developer.apple.com/design/human-interface-guidelines/documentation/uikit/uicontentsizecategory/2897444-isaccessibilitycategory) 를 참조하십시오
>

.



![A screenshot of a Mail message without bold text.](https://docs-assets.developer.apple.com/published/f7d78e2c7726efc7845bc45e660e694e/regular-view@2x.png)At smaller text sizes, Mail displays the date inline with the sender’s name.![A screenshot of a Mail message on iPhone, using the largest accessibility font size. From the top, the message header displays the sender name on one line, followed by the truncated recipient name on the next line, and the date and attachment glyph on the third line. Below the header, most of the three lines of message text are visible on the screen without scrolling.](https://docs-assets.developer.apple.com/published/a9250d8676c471a60e4d2fd4c2ab62a5/stacked-layout@2x.png)At the largest accessibility text size, Mail displays the date below the recipient’s name.**Increase the size of meaningful interface icons as font size increases.** If you use interface icons to communicate important information, make sure they are easy to view at larger font sizes, too. When you use [SF Symbols](/design/human-interface-guidelines/sf-symbols)

, you get icons that scale automatically with Dynamic Type size changes.

> , 동적 유형 크기 변경에 따라 자동으로 확장되는 아이콘을 얻을 수 있습니다.
>



![An illustration of a screen that contains a grouped list on iPhone. The first group in the list includes two rows, each of which contains a star-shaped glyph, a title, and a button to reveal more information. All text appears at a size consistent with the system's default font size.](https://docs-assets.developer.apple.com/published/0df94426f758ffa1837ed28494504f75/icons-small@2x.png)



![An illustration of a screen that contains a grouped list on iPhone. The first group in the list includes two rows, each of which contains a star-shaped glyph, a title, and a button to reveal more information. All text appears at a size consistent with a very large font size.](https://docs-assets.developer.apple.com/published/3d3f666342ca6995e62f9433102af96c/icons-large@2x.png)



**Maintain a consistent information hierarchy regardless of the current font size.** For example, keep primary elements toward the top of a view even when the font size is very large, so that people don’t lose track of these elements.

> **현재 글꼴 크기에 상관없이 일관된 정보 계층을 유지합니다.** 예를 들어, 글꼴 크기가 매우 큰 경우에도 기본 요소를 보기 맨 위에 유지하여 사용자가 이러한 요소를 추적하지 않도록 합니다.
>



**Prefer regular or heavy font weights in your app.** Consider using Regular, Medium, Semibold, or Bold font weights, because they are easier to see. Avoid Ultralight, Thin, and Light font weights, which can be more difficult to see.

> **앱에서 일반 글꼴 또는 무거운 글꼴 가중치를 선호합니다.** 일반, 중간, 세미볼드 또는 굵게 표시된 글꼴 가중치는 보기 쉽기 때문에 사용하는 것이 좋습니다. 보기가 더 어려울 수 있는 초경량, 얇은 글꼴 및 가벼운 글꼴 가중치를 사용하지 마십시오.
>



**Ensure your app responds correctly and looks good when people turn on bold text.** In iOS, iPadOS, tvOS, visionOS, and watchOS, people turn on the bold text accessibility setting to make text and symbols easier to see. In response, your app needs to make all text bolder and give all glyphs an increased stroke weight. The system fonts and SF symbols automatically adjust to the bold text accessibility setting.

> **사람들이 굵은 텍스트를 켤 때 당신의 앱이 정확하게 반응하고 잘 보이도록 하라.** iOS, iPadOS, tvOS, 비전OS, 그리고 OS를 보면서 사람들은 텍스트와 기호를 더 쉽게 볼 수 있도록 굵은 텍스트 접근성 설정을 켭니다. 이에 대응하여, 당신의 앱은 모든 텍스트를 더 대담하게 만들고 모든 글리프에 스트로크 가중치를 높여야 한다. 시스템 글꼴과 SF 기호는 굵은 텍스트 접근성 설정에 자동으로 조정됩니다.
>



![A screenshot of a Mail message without bold text.](https://docs-assets.developer.apple.com/published/f7d78e2c7726efc7845bc45e660e694e/regular-view@2x.png)![A screenshot of a Mail message with bold text.](https://docs-assets.developer.apple.com/published/615973545987af5adcbfa1b08c4113ca/bold-text@2x.png)**Make sure custom fonts are legible.** Custom typefaces can sometimes be difficult to read. Unless your app has a compelling need for a custom font, such as for branding purposes or to create an immersive gaming experience, it’s usually best to use the system fonts. If you do use a custom font, make sure it’s easy to read, even at small sizes.



**Avoid full text justification.** The whitespace created by fully justified text can create patterns that make it difficult for many people to read and focus on the text. Left justification — or right justification in right-to-left languages — provides a framing reference for people with learning and literacy challenges, such as dyslexia.

> **전체 텍스트 정당화를 피하십시오.** 완전히 정당화된 텍스트에 의해 만들어진 공백은 많은 사람들이 텍스트를 읽고 집중하기 어렵게 만드는 패턴을 만들 수 있다. 왼쪽 정당화(오른쪽에서 왼쪽으로) 또는 오른쪽 정당화는 난독증과 같은 학습 및 문해력 문제가 있는 사람들에게 프레임 참조를 제공합니다.
>



**Avoid using italics or all caps for long passages of text.** Italics and all caps are great for occasional emphasis, but overuse of these styles makes text hard to read.

> **긴 텍스트 행에 이탤릭체 또는 모든 대문자를 사용하지 마십시오.** 때때로 강조하기에는 이탤릭체와 모든 대문자가 좋지만, 이러한 스타일을 과도하게 사용하면 텍스트를 읽기가 어렵습니다.
>



[Color and effects](/design/human-interface-guidelines/accessibility#Color-and-effects)

---------------------------------------------------------------------------------------



**Don’t rely solely on color to differentiate between objects or communicate important information.** If you use color to convey information, be sure to provide text labels or glyph shapes to help everyone perceive it.

> **물건을 구별하거나 중요한 정보를 전달하기 위해 색상에만 의존하지 마십시오.** 색상을 사용하여 정보를 전달하는 경우 모든 사람이 인식할 수 있도록 텍스트 레이블이나 글리프 모양을 제공해야 합니다.
>



**Prefer system colors for text.** When you use system colors in text, it responds correctly to accessibility settings such as Invert Colors and Increase Contrast.

> **텍스트에 대한 시스템 색상을 선호합니다.** 텍스트에 시스템 색상을 사용하면 색상 반전 및 대비 증가와 같은 접근성 설정에 올바르게 응답합니다.
>



**Avoid using color combinations as the only way to distinguish between two states or values.** Many colorblind people find it difficult to distinguish blue from orange; other problematic combinations are red and green, red and black, and either red or green combined with gray. When it makes sense to use a combination of colors to communicate states or values, include additional visual indicators so everyone can perceive the information. For example, instead of using red and green circles to indicate offline and online, you could use a red square and a green circle. Some image-editing software includes tools that can help you proof for colorblindness.

> **두 가지 상태 또는 값을 구별하는 유일한 방법으로 색상 조합을 사용하지 마십시오.** 많은 색맹인 사람들은 파란색과 주황색을 구분하는 것을 어려워한다; 다른 문제가 되는 조합은 빨간색과 녹색, 빨간색과 검은색, 그리고 빨간색과 녹색이 회색과 결합된 것이다. 상태 또는 값을 전달하기 위해 색상 조합을 사용하는 것이 타당할 때는 모든 사람이 정보를 인식할 수 있도록 추가 시각적 표시를 포함한다. 예를 들어, 오프라인 및 온라인에서 빨간색 및 녹색 원을 사용하는 대신 빨간색 사각형 및 녹색 원을 사용할 수 있습니다. 일부 이미지 편집 소프트웨어에는 색맹을 증명하는 데 도움이 되는 도구가 포함되어 있습니다.
>



![A screenshot of the History view of the Activity app. The default colors of red, green, and blue are visible.](https://docs-assets.developer.apple.com/published/d543ffc547c6d078b7ff74958c641b88/color-blindness-full-color@2x.png)As seen without colorblindness.![A screenshot of the History view of the Activity app. The color red is replaced by dark gray, green is replaced by yellow, and blue is replaced by light gray.](https://docs-assets.developer.apple.com/published/9cca1cf0b16eaaae605b89d4c16c126c/color-blindness-protanopia@2x.png)As seen with red-green colorblindness.**Ensure your views respond correctly to Invert Colors.** People can turn on Invert Colors when they prefer to view items on a dark background. In the Smart Invert mode of Invert Colors, images, video, and full-color icons (such as app icons and nontemplate images) don’t invert, and dark UI stays dark. Test your app or game to find places where you might need to prevent an image — like a photo in a custom view — from inverting.



**Use strongly contrasting colors to improve readability.** Many factors affect the perception of color, including font size and weight, color brightness, screen resolution, and lighting conditions. When you increase color contrast of visual elements like text, glyphs, and controls, you can help more people use your app in more situations. To find out if the contrast of adjacent colors in your UI meets minimum acceptable levels, you can use Xcode’s Accessibility Inspector or an online color calculator based on the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/)

> **강력하게 대비되는 색상을 사용하여 가독성을 향상시킵니다.** 글자 크기와 무게, 색상 밝기, 화면 해상도 및 조명 조건을 포함하여 많은 요소가 색상 인식에 영향을 미친다. 텍스트, 글리프 및 컨트롤과 같은 시각적 요소의 색상 대비를 높이면 더 많은 사람들이 더 많은 상황에서 앱을 사용할 수 있도록 도울 수 있습니다. UI에서 인접한 색상의 대비가 허용 가능한 최소 수준을 충족하는지 확인하려면 Xcode의 내게 필요한 접근성 검사기 또는 [WCAG(Web Content Accessibility Guideline)](https://www.w3.org/TR/WCAG21/) 에 기반한 온라인 색상 계산기를 사용하면 됩니다
>

 color contrast formula. In general, smaller or lighter-weight text needs to have greater contrast to be legible. Use the following values for guidance.

> 색 대비 공식. 일반적으로 더 작거나 가벼운 텍스트는 읽기 쉽도록 더 큰 대비를 가져야 한다. 다음 값을 사용하여 지침을 제공합니다.
>







| Text size | Text weight | Minimum contrast ratio |

| --- | --- | --- |

| Up to 17 points | All | 4.5:1 |

| 18 points and larger | All | 3:1 |

| All | Bold | 3:1 |



**Change blurring and transparency when people turn on Reduce Transparency.** For example, make areas of blurred content and translucency mostly opaque. For best results, use a color value in the opaque area that’s different from the original color value you used when the area was blurred or translucent.

> **사람들이 투명도를 줄이면 흐려지고 투명도를 바꾼다.** 예를 들어, 흐린 내용과 반투명 영역을 대부분 불투명하게 만듭니다. 최상의 결과를 얻으려면 불투명 영역에서 해당 영역이 흐리거나 반투명할 때 사용한 원래 색상 값과 다른 색상 값을 사용하십시오.
>



[Motion](/design/human-interface-guidelines/accessibility#Motion)

-----------------------------------------------------------------



**Avoid requiring animations unless they’re essential for your experience.** In general, let people use your app without relying on any animations.

> **애니메이션이 당신의 경험에 필수적인 것이 아니라면 요구하지 마세요.** 일반적으로 사람들이 애니메이션에 의존하지 않고 당신의 앱을 사용하도록 하세요.
>



**Play tightened animations when Reduce Motion is on.** People can turn on Reduce Motion if they tend to get distracted or experience dizziness or nausea when viewing animations that include effects such as zooming, scaling, spinning, or peripheral motion. In response to this setting, you need to turn off or reduce animations that are known to cause problems (to learn more, see [Responsive design for motion](https://webkit.org/blog/7551/responsive-design-for-motion/)

> **동작 축소가 켜져 있을 때 강화된 애니메이션을 재생합니다.** 사람들은 줌, 스케일링, 회전 또는 주변 운동과 같은 효과를 포함하는 애니메이션을 볼 때 주의가 산만해지거나 어지러움 또는 메스꺼움을 경험하는 경향이 있는 경우 모션 감소를 켤 수 있습니다. 이 설정에 따라 문제가 발생하는 것으로 알려진 애니메이션을 끄거나 줄여야 합니다(자세한 내용은 [동작에 대한 반응 설계](https://webkit.org/blog/7551/responsive-design-for-motion/) 참조)
>

). If you use a problematic animation to communicate important information, consider designing a non animated alternative or tightening the physics of the animation to reduce its motion. For example:

> ). 중요한 정보를 전달하기 위해 문제가 있는 애니메이션을 사용한다면 애니메이션이 아닌 대안을 설계하거나 애니메이션의 물리학을 강화하여 움직임을 줄이는 것을 고려해 보자. 예:
>



* Tighten springs to reduce bounce effects or track 1:1 as a person gestures

> * 스프링을 조여서 바운스 효과를 줄이거나 사람이 제스처를 취하면서 1:1로 추적합니다
>

* Avoid animating depth changes in z-axis layers

> * z 축 도면층의 깊이 변화를 애니메이션화
>

* Avoid animating into or out of blurs

> * 블러로 또는 블러로 애니메이션화하는 것을 피합니다
>

* Replace a slide with a fade to avoid motion

> * 움직임을 피하기 위해 슬라이드를 페이드로 교체합니다
>



**Let people control video and other motion effects.** Avoid autoplaying video or effects without also providing a button or other way to control them.

> **사람들이 비디오 및 기타 모션 효과를 제어할 수 있도록 합니다.** 버튼이나 기타 제어 방법을 제공하지 않고 동영상이나 효과를 자동으로 재생하지 마십시오.
>



**Be cautious when displaying moving or blinking elements.** Although subtle movement and blinking can draw people’s attention, these effects can also be distracting and they aren’t useful for people with visual disabilities. Worse, some blinking elements can cause epileptic episodes. In all cases, avoid using movement and blinking as the only way to convey information.

> **움직이거나 깜박이는 요소를 표시할 때 주의하십시오.** 비록 미묘한 움직임과 깜박임이 사람들의 관심을 끌 수 있지만, 이러한 효과들은 또한 주의를 산만하게 할 수 있고 시각 장애가 있는 사람들에게 유용하지 않다. 더 나쁜 것은, 일부 깜박이는 요소들이 간질 증상을 일으킬 수 있다는 것이다. 모든 경우에 정보를 전달하는 유일한 방법으로 이동 및 깜박임을 사용하지 마십시오.
>



For additional guidance on helping people remain comfortable while they experience motion in your visionOS app, see [Motion > visionOS](/design/human-interface-guidelines/motion#visionOS)

For additional guidance on helping people remain comfortable while they experience motion in your visionOS app, see [Motion > visionOS](/design/human-interface-guidelines/motion#visionOS)

> 사용자가 시야에서 움직임을 경험하는 동안 사람들이 편안하게 지낼 수 있도록 지원하는 방법에 대한 추가 안내OS 앱, [모션] > vision OS](/design/human-interface-guideline/motion#vision 참조)OS)
>

. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)

> . 개발자 지침은 [비전 내 접근성 지원 향상]을 참조하십시오OS 앱](https://developer.apple.com/design/human-interface-guidelines/documentation/visionOS/improving-accessibility-support-in-your-app)
>

.



[Platform considerations](/design/human-interface-guidelines/accessibility#Platform-considerations)

---------------------------------------------------------------------------------------------------



*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*

> *iOS, iPadOS, macOS, tvOS 또는 시계에 대한 추가 고려 사항 없음OS.*
>



### [visionOS](/design/human-interface-guidelines/accessibility#visionOS)



**Avoid anchoring content to the wearer’s head.** In addition to making people feel stuck or confined, anchoring content to their can prevent someone from using Pointer Control to interact with that content. Head-anchored content can also prevent people with low vision from reading it because they can’t move closer to it or position the content inside the Zoom lens.

> ** 착용자의 머리에 내용물을 고정하지 마십시오.** 사람들이 막혔거나 갇힌 느낌을 갖게 할 뿐만 아니라 내용을 앵커링하면 포인터 컨트롤을 사용하여 해당 내용과 상호 작용하는 것을 방지할 수 있습니다. 머리 고정 콘텐츠는 더 가까이 이동하거나 줌 렌즈 안에 콘텐츠를 위치시킬 수 없기 때문에 시력이 낮은 사람이 읽지 못하도록 할 수도 있습니다.
>



* [Pointer control - hand](#)

> * [포인터 컨트롤 - 핸드](#)
>

* [Pointer control - head](#)

> * [포인터 컨트롤 - 헤드](#)
>

* [Zoom lens](#)

 [Play](#) 

 [Play](#) 

![A screenshot of an app's window in visionOS. A zoom lens is visible above a portion of the window, and displays a zoomed-in version of the content beneath the lens.](https://docs-assets.developer.apple.com/published/82d9878af5b6517724653da73d20b14b/visionos-accessibility-zoom-lens@2x.png)



[Resources](/design/human-interface-guidelines/accessibility#Resources)

-----------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/accessibility#Related)



[Inclusion](/design/human-interface-guidelines/inclusion)





#### [Developer documentation](/design/human-interface-guidelines/accessibility#Developer-documentation)



[Accessibility](/documentation/accessibility)





[Accessibility for developers](https://developer.apple.com/accessibility/)





[Accessibility modifiers](/documentation/SwiftUI/View-Accessibility)





[Accessibility for UIKit](/documentation/uikit/accessibility_for_uikit)





[Accessibility for AppKit](/documentation/appkit/accessibility_for_appkit)





#### [Videos](/design/human-interface-guidelines/accessibility#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/D1866B0D-617B-4A78-A645-915F82BC0B78/8062_wide_250x141_1x.jpg) Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034) 

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/2C47B638-090D-4CBB-9E9E-EBE8114536D9/8132_wide_250x141_1x.jpg) Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078) 

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/90B67086-3A99-49A5-965A-D35DB6552AE0/5206_wide_250x141_1x.jpg) The practice of inclusive design](https://developer.apple.com/videos/play/wwdc2021/10275) 

[Change log](/design/human-interface-guidelines/accessibility#Change-log)

-------------------------------------------------------------------------







| Date | Changes |

| --- | --- |

| June 21, 2023 | Updated to include guidance for visionOS. |




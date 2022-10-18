# **[patterns] playing-haptics**

# Playing haptics can engage people’s sense of touch and bring their familiarity with the physical world into your app or game.
> 햅틱 게임을 하는 것은 사람들의 촉각을 사로잡을 수 있고 실제 세계에 대한 친숙함을 당신의 앱이나 게임에 가져올 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-haptics-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-haptics-intro-dark_2x.png)

The system can play haptics in addition to visual and auditory feedback to communicate things like the confirmation of an Apple Pay transaction or the arrival of a notification in iOS and watchOS. On a Mac that’s equipped with a Force Touch trackpad, apps can play haptics while people are dragging content or respond to different strengths of a force click to enable different levels of change in an onscreen element. In a tvOS or iPadOS app, game controllers can provide haptic feedback.
> 이 시스템은 시각 및 청각 피드백 외에도 햅틱을 재생하여 애플 페이 거래 확인이나 iOS 및 워치 OS의 알림 도착과 같은 것들을 전달할 수 있다. Force Touch 트랙패드가 장착된 Mac에서는 앱을 사용하여 콘텐츠를 끌거나 다양한 강도의 힘 클릭에 반응하여 화면 요소에서 다양한 수준의 변경을 수행할 수 있습니다. tvOS 또는 iPadOS 앱에서 게임 컨트롤러는 촉각적인 피드백을 제공할 수 있습니다.
>




Depending on the platform, the system may provide haptic feedback for standard components by default. For example, components like switches, sliders, and pickers automatically play haptic feedback on supported iPhone models; on Apple Watch, the Taptic Engine generates haptics and watchOS combines an audible tone with some of them. In addition, the system may provide built-in haptic patterns you can use in your app or game or even let you design custom ones.
> 플랫폼에 따라 시스템은 기본적으로 표준 구성 요소에 대한 촉각 피드백을 제공할 수 있습니다. 예를 들어 스위치, 슬라이더 및 피커와 같은 구성 요소는 지원되는 iPhone 모델에서 자동으로 촉각 피드백을 재생합니다. Apple Watch에서 Taptic Engine은 촉각 및 시계를 생성합니다.OS는 오디오 톤을 그들 중 일부와 결합한다. 또한 이 시스템은 앱이나 게임에서 사용할 수 있는 내장 햅틱 패턴을 제공하거나 사용자 지정 패턴을 디자인할 수 있습니다.
>




# **Best practices**

**Use system-provided haptic patterns according to their documented meanings.** People recognize standard haptics because the system plays them consistently on interactions with standard controls. If the documented use case for a pattern doesn’t make sense in your app, use a generic pattern or create your own, where supported. For guidance, see [Custom haptics](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-haptics#custom-haptics).
> 시스템에서 제공한 촉각 패턴을 문서화된 의미에 따라 사용합니다. 표준 햅틱은 시스템이 표준 제어 장치와의 상호 작용에서 일관되게 재생하기 때문에 사람들은 표준 햅틱을 인식한다. 패턴에 대한 문서화된 사용 사례가 앱에서 이해되지 않는 경우 일반 패턴을 사용하거나 지원되는 경우 자신만의 패턴을 만드십시오. 자세한 내용은 사용자 지정 햅틱을 참조하십시오.
>




**Use haptics consistently.** It’s important to build a clear, causal relationship between each haptic and the action that causes it so people learn to associate certain haptic patterns with certain experiences. If a haptic doesn’t reinforce a cause-and-effect relationship, it can be confusing and seem gratuitous. For example, if your app plays a specific haptic pattern when a game character fails to finish a mission, people associate that pattern with a negative outcome. If you use the same haptic pattern for a positive outcome like a level completion, people will be confused.
> 햅틱을 꾸준히 사용하세요. 사람들이 특정한 햅틱 패턴을 특정한 경험과 연관시키는 것을 배울 수 있도록 각 햅틱과 그것을 일으키는 행동 사이에 명확하고 인과적인 관계를 구축하는 것이 중요하다. 햅틱이 인과관계를 강화하지 않는다면, 혼란스럽고 불필요해 보일 수 있다. 예를 들어, 게임 캐릭터가 미션을 완료하지 못했을 때 앱이 특정 햅틱 패턴을 재생하면, 사람들은 그 패턴을 부정적인 결과와 연관시킨다. 레벨 완성과 같은 긍정적인 결과를 위해 동일한 햅틱 패턴을 사용한다면, 사람들은 혼란스러울 것이다.
>




**Use haptics in ways that complement other feedback in your app.** When visual, auditory, and tactile feedback are in harmony — as they generally are in the physical world — the user experience is more coherent and can seem more natural. For example, match the intensity and sharpness of a haptic with the animation you use to accompany it. You can also synchronize sound with haptics; for developer guidance, see [Delivering rich app experiences with haptics](https://developer.apple.com/documentation/corehaptics/delivering_rich_app_experiences_with_haptics).
> 앱의 다른 피드백을 보완하는 방식으로 햅틱을 사용하십시오. 시각적, 청각적 및 촉각적 피드백이 일반적으로 물리적 세계에서와 같이 조화를 이룰 때 사용자 경험은 보다 일관성이 있고 보다 자연스럽게 보일 수 있다. 예를 들어, 햅틱의 강도와 선명도를 햅틱과 함께 사용하는 애니메이션과 일치시킵니다. 또한 소리를 햅틱과 동기화할 수도 있습니다. 개발자 지침은 햅틱으로 풍부한 앱 경험 제공을 참조하십시오.
>




**Avoid overusing haptics.** Sometimes a haptic can feel just right when it happens occasionally, but become tiresome when it plays frequently. It’s important to do user testing that can help you discover a balance that most people appreciate. Often, the best haptic experience is one that people may not be conscious of, but miss when it’s turned off.
> 햅틱을 과도하게 사용하지 마십시오. 때때로 햅틱은 가끔 일어날 때 딱 알맞게 느껴질 수 있지만, 자주 연주할 때는 지겨워진다. 대부분의 사람들이 인정하는 균형을 찾는 데 도움이 될 수 있는 사용자 테스트를 수행하는 것이 중요합니다. 종종, 최고의 촉각 경험은 사람들이 의식하지 못할 수도 있지만, 꺼졌을 때 놓치는 경험이다.
>




**Make haptics optional.** Let people turn off or mute haptics if they wish, and make sure people can still enjoy your app without them.
> 햅틱을 옵션으로 설정합니다. 사람들이 원한다면 햅틱을 끄거나 음소거하게 하고, 사람들이 그것 없이도 당신의 앱을 즐길 수 있도록 하세요.
>




**Be aware that playing haptics might impact other user experiences.** By design, haptics produce enough physical force for people to feel the vibration. Ensure that haptic vibrations don’t disrupt user experiences involving the camera, gyroscope, or microphone.
> 햅틱 플레이는 다른 사용자 경험에 영향을 미칠 수 있습니다. 설계상, 햅틱은 사람들이 진동을 느낄 수 있는 충분한 물리력을 생산한다. 촉각 진동이 카메라, 자이로스코프 또는 마이크를 포함한 사용자 경험을 방해하지 않도록 하십시오.
>




# **Custom haptics**

Games often use custom haptics to enhance gameplay. Although it’s less common, nongame apps might also use custom haptics to provide a richer, more delightful experience.
> 게임은 종종 게임플레이를 향상시키기 위해 사용자 지정 햅틱을 사용한다. 흔하지는 않지만 게임 이외의 앱은 사용자 지정 햅틱을 사용하여 더 풍부하고 즐거운 경험을 제공할 수도 있습니다.
>




You can design custom haptic patterns that vary dynamically, based on user input or context. For example, the impact players feel when a game character jumps from a tree can be stronger than when the character jumps in place, and substantial experiences — like a collision or a hit — can feel very different from subtle experiences like the approach of footsteps or a looming danger.
> 사용자 입력 또는 상황에 따라 동적으로 변화하는 사용자 지정 햅틱 패턴을 설계할 수 있습니다. 예를 들어, 게임 캐릭터가 나무에서 뛰어내릴 때 느끼는 충격은 캐릭터가 제자리에 뛰어내릴 때보다 더 강할 수 있으며, 충돌이나 적중과 같은 실질적인 경험은 발자국 접근이나 다가오는 위험과 같은 미묘한 경험과는 매우 다르게 느껴질 수 있다.
>




There are two basic building blocks you can use to generate custom haptic patterns.
> 사용자 정의 촉각 패턴을 생성하는 데 사용할 수 있는 두 가지 기본 구성 요소가 있습니다.
>




- *Transient* events are brief and compact, often feeling like taps or impulses. The experience of tapping the Flashlight button on the Home Screen is an example of a transient event.
- >  일시적인 사건은 짧고 간결하며, 종종 도청이나 충동처럼 느껴집니다. 홈 스크린에서 플래시라이트 버튼을 누르는 경험은 일시적인 이벤트의 한 예입니다.

- *Continuous* events feel like sustained vibrations, such as the experience of the lasers effect in a message.
- >  연속적인 사건들은 메시지에서 레이저 효과의 경험과 같은 지속적인 진동처럼 느껴진다.


Regardless of the type of haptic event you use to generate a custom haptic, you can also control its *sharpness* and *intensity*. You can think of sharpness as a way to abstract a haptic experience into the waveform that produces the corresponding physical sensations. Specifying sharpness lets you relay to the system your intent for the experience. For example, you might use sharpness values to convey an experience that’s soft, rounded, or organic, or one that’s crisp, precise, or mechanical. As the term implies, intensity means the strength of the haptic.
> 사용자 지정 햅틱을 생성하는 데 사용하는 햅틱 이벤트의 유형에 관계없이 선명도와 강도를 제어할 수도 있습니다. 선명도는 촉각 경험을 해당 물리적 감각을 생성하는 파형으로 추상화하는 방법이라고 생각할 수 있습니다. 선명도를 지정하면 경험에 대한 의도를 시스템에 전달할 수 있습니다. 예를 들어, 선명도 값을 사용하여 부드럽고 둥글거나 유기적인 경험 또는 선명하고 정밀하거나 기계적인 경험을 전달할 수 있습니다. 이 용어가 암시하듯이, 강도는 촉각의 강도를 의미한다.
>




By combining transient and continuous events, varying sharpness and intensity, and including optional audio content, you can create a wide range of different haptic experiences. For developer guidance, see [Core Haptics](https://developer.apple.com/documentation/corehaptics).
> 일시적 이벤트와 연속적 이벤트, 다양한 선명도 및 강도, 옵션 오디오 콘텐츠를 결합하면 다양한 햅틱 경험을 폭넓게 만들 수 있습니다. 개발자 지침은 핵심 햅틱스를 참조하십시오.
>




# **Platform considerations**

# **iOS, iPadOS**

Although iPad doesn’t play haptics, you can support game controller input in your iPadOS apps. For developer guidance, see [Playing haptics on game controllers](https://developer.apple.com/documentation/corehaptics/playing_haptics_on_game_controllers).
> iPad는 햅틱을 재생하지 않지만 iPadOS 앱에서 게임 컨트롤러 입력을 지원할 수 있습니다. 개발자 지침은 게임 컨트롤러에서 햅틱 재생을 참조하십시오.
>




On supported iPhone models, you can add haptics to your experience in the following ways:
> 지원되는 iPhone 모델에서는 다음과 같은 방법으로 사용자 환경에 햅틱을 추가할 수 있습니다.
>




- Use standard UI components — like [switches](../components/selection-and-input/toggles), [sliders](../components/selection-and-input/sliders), and [pickers](../components/selection-and-input/pickers) — that play Apple-designed system haptics by default.
- >  기본적으로 Apple에서 설계한 시스템 햅틱을 재생하는 스위치, 슬라이더 및 피커와 같은 표준 UI 구성 요소를 사용합니다.

- When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of [notification](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-haptics#notification), [impact](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-haptics#impact), and [selection](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-haptics#selection) (for developer guidance, see [UIFeedbackGenerator](https://developer.apple.com/documentation/uikit/uifeedbackgenerator)).
- >  이해가 되면 피드백 생성기를 사용하여 알림, 영향 및 선택 범주에서 미리 정의된 여러 햅틱 패턴 중 하나를 재생합니다(개발자 지침은 UI FeedbackGenerator 참조).


### **Notification**

Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.
> 알림 햅틱은 수표를 입금하거나 차량을 잠금 해제하는 것과 같은 작업 또는 조치의 결과에 대한 피드백을 제공합니다.
>




Play

**Success.** Indicates that a task or action has completed.
> 성공. 작업 또는 작업이 완료되었음을 나타냅니다.
>




Play

**Warning.** Indicates that a task or action has produced a warning of some kind.
> 경고. 작업 또는 작업이 어떤 종류의 경고를 생성했음을 나타냅니다.
>




Play

**Error.** Indicates that an error has occurred.
> 오류. 오류가 발생했음을 나타냅니다.
>




### **Impact**

Impact haptics provide a physical metaphor you can use to complement a visual experience. For example, people might feel a tap when a view snaps into place or a thud when two heavy objects collide.
> 충격 햅틱은 시각적 경험을 보완하는 데 사용할 수 있는 물리적 은유를 제공합니다. 예를 들어, 사람들은 시야가 제자리에 찰칵 소리를 내거나 두 개의 무거운 물체가 충돌할 때 쿵 소리를 느낄 수 있다.
>




Play

**Light.** Indicates a collision between small or lightweight UI objects.
> 가볍습니다. 소형 또는 경량 UI 개체 간의 충돌을 나타냅니다.
>




Play

**Medium.** Indicates a collision between medium-sized or medium-weight UI objects.
> 중간. 중간 크기 또는 중간 무게 UI 개체 간의 충돌을 나타냅니다.
>




Play

**Heavy.** Indicates a collision between large or heavyweight UI objects.
> 무겁습니다. 큰 UI 개체 또는 무거운 UI 개체 간의 충돌을 나타냅니다.
>




Play

**Rigid.** Indicates a collision between hard or inflexible UI objects.
> 경직. 하드 또는 유연하지 않은 UI 개체 간의 충돌을 나타냅니다.
>




Play

**Soft.** Indicates a collision between soft or flexible UI objects.
> 소프트. 소프트 또는 플렉시블 UI 개체 간의 충돌을 나타냅니다.
>




### **Selection**

Selection haptics provide feedback while the values of a UI element are changing.
> 선택 햅틱은 UI 요소의 값이 변경되는 동안 피드백을 제공합니다.
>




Play

**Selection.** Indicates that a UI element’s values are changing.
> 선택. UI 요소의 값이 변경되고 있음을 나타냅니다.
>




# **macOS**

When a Magic Trackpad is available, your app can provide one of the three following haptic patterns in response to a drag operation or force click.
> 매직 트랙패드를 사용할 수 있는 경우 끌기 작업이나 강제 클릭에 대한 응답으로 다음 세 가지 햅틱 패턴 중 하나를 앱에서 제공할 수 있습니다.
>




For developer guidance, see [NSHapticFeedbackPerformer](https://developer.apple.com/documentation/appkit/nshapticfeedbackperformer).

# **tvOS**

On Apple TV, game controllers can play haptics. For developer guidance, see [Playing haptics on game controllers](https://developer.apple.com/documentation/corehaptics/playing_haptics_on_game_controllers).
> 애플 TV에서는 게임 컨트롤러가 햅틱을 할 수 있다. 개발자 지침은 게임 컨트롤러에서 햅틱 재생을 참조하십시오.
>




# **watchOS**

Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content. By default, the system provides linear haptic detents that people can feel as they rotate the Digital Crown. Some system controls, like table views, provide detents as new items scroll onto the screen. For developer guidance, see [WKHapticType (WatchKit)](https://developer.apple.com/documentation/watchkit/wkhaptictype).
> 애플워치 시리즈 4 이상은 디지털 크라운에 대한 촉각 피드백을 제공하며, 콘텐츠를 스크롤할 때 더욱 촉각적인 경험을 제공한다. 기본적으로 이 시스템은 디지털 크라운을 회전할 때 느낄 수 있는 선형 촉각 멈춤쇠를 제공합니다. 테이블 보기와 같은 일부 시스템 컨트롤은 새 항목이 화면 위로 스크롤될 때 멈춤쇠를 제공합니다. 개발자 지침은 WKHapticType(WatchKit)을 참조하십시오.
>




watchOS defines the following set of haptics, each of which conveys a specific meaning to people.
> watchOS는 다음과 같은 햅틱을 정의하며, 각각의 햅틱은 사람들에게 특별한 의미를 전달한다.
>




- **[Notification](../patterns/playing-haptics)**
- [Up](../patterns/playing-haptics)
- [Down](../patterns/playing-haptics)
- [Success](../patterns/playing-haptics)
- [Failure](../patterns/playing-haptics)
- [Retry](../patterns/playing-haptics)
- [Start](../patterns/playing-haptics)
- [Stop](../patterns/playing-haptics)
- [Click](../patterns/playing-haptics)
-

**Notification.** Tells the user that something significant or out of the ordinary has happened and requires the user’s attention. The system plays this same haptic when a local or remote notification arrives.
> 알림. 사용자에게 중요한 일이 발생했거나 비정상적인 일이 발생했으며 사용자의 주의가 필요함을 알립니다. 로컬 또는 원격 알림이 도착할 때 시스템은 동일한 햅틱을 재생합니다.
>





# **Resources**

| Haptic feedback pattern | Description |
| --- | --- |
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don’t apply. |

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





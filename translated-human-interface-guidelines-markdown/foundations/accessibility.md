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


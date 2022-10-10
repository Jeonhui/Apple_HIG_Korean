# **[foundations] motion**

### On all platforms, beautiful, fluid motions bring the interface to life, conveying status, providing feedback and instruction, and enriching the visual experience.
> 모든 플랫폼에서 아름답고 유동적인 움직임은 인터페이스를 생동감 있게 하고, 상태를 전달하며, 피드백과 지시를 제공하며, 시각적 경험을 풍부하게 한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-motion-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-motion-intro-dark_2x.png)

System components automatically include motion, letting you offer of familiar and consistent experiences throughout your app or game. As you design custom motion, focus on intentional animations that keep people oriented, provide clear feedback in response to their actions, and help them learn your interface without getting overwhelmed.
> 시스템 구성요소는 자동으로 모션을 포함하므로 앱이나 게임 전체에서 친숙하고 일관된 경험을 제공할 수 있습니다. 사용자 지정 모션을 설계할 때, 사람들이 방향을 잡고, 그들의 행동에 대한 명확한 피드백을 제공하고, 그들이 압도당하지 않고 당신의 인터페이스를 배우도록 돕는 의도적인 애니메이션에 집중하세요.
>




# **Best practices**

**Use motion to communicate.** Motion can be a great way to enhance feedback and understanding by showing how things change, what will happen when people perform an action, and what they can do next. For example, when people minimize a window in macOS, it moves smoothly from the desktop to the Dock so they know exactly where it went; when people set up Face ID, the system briefly describes what they need to do and helps them during scanning by visually changing the tick marks encircling their face.
> 의사소통을 하기 위해 모션을 사용합니다. 모션은 사물이 어떻게 변하는지, 사람들이 행동을 할 때 어떤 일이 일어날지, 그리고 다음에 무엇을 할 수 있는지를 보여줌으로써 피드백과 이해를 증진시키는 좋은 방법이 될 수 있습니다. 예를 들어, macOS에서 창을 최소화하면 데스크톱에서 도크로 원활하게 이동하기 때문에 어디로 갔는지 정확히 알 수 있습니다. 페이스 ID를 설정할 때 시스템은 필요한 작업을 간략하게 설명하고 얼굴 주변의 눈금 표시를 시각적으로 변경하여 스캔하는 동안 도움을 줍니다.
>




**Add motion purposefully, supporting the experience without overshadowing it.** Don’t add motion for the sake of adding motion. Gratuitous or excessive animation can distract people or make them feel disconnected, especially in an app that doesn’t provide an immersive experience.
> 의도적으로 움직임을 추가해, 무색하게 하지 않고 경험을 지지하세요. 움직임을 추가하기 위해 움직임을 추가하지 마세요. 불필요하거나 과도한 애니메이션은 특히 몰입감 있는 경험을 제공하지 않는 앱에서 사람들의 주의를 산만하게 하거나 연결 끊김을 느끼게 할 수 있다.
>




**Make motion optional.** There are several reasons why people might not see onscreen animations, so it’s essential to avoid using it as the only way to communicate important information. For example, when the Reduce Motion accessibility setting is on, be sure to minimize or eliminate animations. For guidance, see [Color and effects](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/#color-and-effects).
> 모션을 선택 사항으로 만듭니다. 사람들이 화면에서 애니메이션을 볼 수 없는 몇 가지 이유가 있으므로 중요한 정보를 전달하는 유일한 방법으로 사용하지 않도록 하는 것이 중요합니다. 예를 들어, 모션 액세스 감소 설정이 켜져 있으면 애니메이션을 최소화하거나 제거해야 합니다. 자세한 내용은 색상 및 효과를 참조하십시오.
>




**Strive for realism and credibility.** Accurate, realistic motion can help people understand how something works, but motion that doesn’t make sense — or appears to defy physical laws — can make them feel disoriented. For example, if someone reveals a view by sliding it down from the top of the screen, they don’t expect to dismiss the view by sliding it to the side.
> 현실주의와 신뢰성을 추구하라. 정확하고 현실적인 움직임은 사람들이 어떤 것이 어떻게 작동하는지 이해하는 데 도움을 줄 수 있지만, 말이 되지 않거나 물리적 법칙을 거스르는 것처럼 보이는 움직임은 그들을 혼란스럽게 만들 수 있다. 예를 들어, 누군가가 화면 상단에서 보기를 아래로 미끄러뜨려 표시한다면, 그들은 보기를 옆으로 미끄러뜨려 무시하지 않을 것이다.
>




**Prefer quick, precise animations.** Animations that combine brevity and precision tend to feel more lightweight and less intrusive, and often convey information more effectively. For example, when people tap the list button in Weather on iPhone, the fullscreen view of the current city quickly transitions to the list view, pinpointing the city’s location in the list.
> 빠르고 정확한 애니메이션을 선호합니다. 간결함과 정밀함이 결합된 애니메이션은 더 가볍고 덜 거슬리는 경향이 있으며 정보를 더 효과적으로 전달하는 경우가 많습니다. 예를 들어 아이폰의 날씨에서 사람들이 목록 버튼을 누르면 현재 도시의 전체 화면 보기가 목록 보기로 빠르게 전환되어 목록에서 도시의 위치를 정확히 파악한다.
>




**In general, avoid adding motion to interactions that occur frequently.** The system already provides subtle animations for interactions with standard interface elements. Avoid making people spend extra time watching unnecessary motion every time they interact with something.
> 일반적으로 자주 발생하는 상호 작용에 모션을 추가하지 마십시오. 시스템은 이미 표준 인터페이스 요소와의 상호 작용을 위한 미묘한 애니메이션을 제공합니다. 사람들이 무언가와 상호작용할 때마다 불필요한 움직임을 보는 데 여분의 시간을 보내는 것을 피하세요.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항 없음.
>




# **watchOS**

SwiftUI provides a powerful and streamlined way to add motion to your app. If you need to use WatchKit to animate layout and appearance changes — or create animated image sequences — follow these guidelines.
> SwiftUI는 앱에 모션을 추가할 수 있는 강력하고 효율적인 방법을 제공합니다. WatchKit을 사용하여 레이아웃 및 모양을 변경하거나 애니메이션 이미지 시퀀스를 만들어야 하는 경우 다음 지침을 따르십시오.
>




**NOTE**All layout- and appearance-based animations automatically include built-in easing that plays at the start and end of the animation. You can’t turn off or customize easing.
> 참고 모든 레이아웃 및 모양 기반 애니메이션에는 애니메이션의 시작과 끝에 재생되는 기본 제공 이식이 자동으로 포함됩니다. 완화 기능을 해제하거나 사용자 지정할 수 없습니다.
>




Using WatchKit, you can animate changes to the following attributes of your app's UI elements:
> WatchKit을 사용하면 앱 UI 요소의 다음 특성에 대한 변경 내용을 애니메이션으로 만들 수 있습니다.
>




- Alignment
- Background color
- Group insets
- Height
- Opacity
- Accent color
- Width

WatchKit also lets you create an animated image sequence, which consists of two or more individual images displayed sequentially over time. Each image in the sequence constitutes a single frame of the animation, and the whole animation runs in a loop unless you modify the playback behavior at runtime. You install animated image sequences primarily in image, group, and button elements of your interface.
> 또한 WatchKit을 사용하면 시간이 지남에 따라 순차적으로 표시되는 두 개 이상의 개별 이미지로 구성된 애니메이션 이미지 시퀀스를 만들 수 있습니다. 시퀀스의 각 이미지는 애니메이션의 단일 프레임을 구성하며 런타임에 재생 동작을 수정하지 않는 한 전체 애니메이션이 루프에서 실행됩니다. 주로 인터페이스의 이미지, 그룹 및 버튼 요소에 애니메이션 이미지 시퀀스를 설치합니다.
>




You can programmatically control the playback speed, direction, and frame rate of animated sequences for image and group elements. Other interface elements display the full animation in an endless loop.
> 이미지 및 그룹 요소에 대한 애니메이션 시퀀스의 재생 속도, 방향 및 프레임률을 프로그래밍 방식으로 제어할 수 있습니다. 다른 인터페이스 요소는 전체 애니메이션을 무한 루프에 표시합니다.
>




**Store images in your watchOS app bundle when possible.** Storing images in your watchOS app bundle minimizes the delay in loading those images and showing the animation at runtime. Use this technique for animations that are part of your app’s design.
> 시계에 이미지 저장가능한 경우 OS 앱 번들. 시계에 이미지 저장OS 앱 번들은 런타임에 이러한 이미지를 로드하고 애니메이션을 보여주는 지연을 최소화한다. 앱 디자인의 일부인 애니메이션에 이 기술을 사용합니다.
>




**Optimize all images in your image sequences.** Optimized images take less space on disk and load more quickly in some situations.
> 이미지 시퀀스의 모든 이미지를 최적화합니다. 최적화된 이미지는 디스크에 더 적은 공간을 사용하고 일부 상황에서는 더 빨리 로드됩니다.
>




**Use the same image sequence for forward and reverse animations.** At runtime, you can animate image sequences in reverse, eliminating the need to provide a set of duplicate images in reverse order. Using this technique reduces the size of your app.
> 정방향 및 역방향 애니메이션에 동일한 이미지 시퀀스를 사용합니다. 런타임에 이미지 시퀀스를 역방향으로 애니메이션화할 수 있으므로 중복 이미지 세트를 역순으로 제공할 필요가 없습니다. 이 기술을 사용하면 앱의 크기가 줄어듭니다.
>




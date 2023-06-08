# **[patterns] loading**

# While content loads, avoid showing a blank or static screen that might make people think your app or game is sluggish or frozen.
> 콘텐츠가 로드되는 동안 앱이나 게임이 느려지거나 중지되었다고 생각할 수 있는 빈 화면이나 정적 화면을 표시하지 않도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-loading-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-loading-intro-dark_2x.png)

# **Best practices**

**Show content as soon as possible.** If you make people wait for loading to complete before displaying anything, they may interpret the lack of content as sluggishness. Instead, show placeholder text, graphics, or animations where content isn't available yet, and replace these elements as the content loads. When possible, preload upcoming content in the background, such as while an animation is playing or people are navigating a level or menu.
> 가능한 한 빨리 콘텐츠를 표시합니다. 사용자가 내용을 표시하기 전에 로딩이 완료될 때까지 기다리게 하는 경우, 내용이 부족한 것으로 해석할 수 있습니다. 대신 콘텐츠를 아직 사용할 수 없는 플레이스홀더 텍스트, 그래픽 또는 애니메이션을 표시하고 콘텐츠가 로드될 때 이러한 요소를 교체하십시오. 가능한 경우 애니메이션이 재생 중이거나 사용자가 수준 또는 메뉴를 탐색하는 경우와 같이 백그라운드에서 다가오는 콘텐츠를 미리 로드합니다.
>




**Clearly communicate that content is loading and how long it might take to complete.** Ideally, content displays instantly, but for situations where loading takes more than a moment or two, you can use system-provided components — called *progress indicators* — to show that content is loading. In general, you use a *determinate* progress indicator when you know how long loading will take, and you use an *indeterminate* progress indicator when you can’t quantify loading duration. In macOS, for example, the Finder combines a determinate progress bar with brief explanatory text to help people gauge how long a file copy will take to complete. For guidance, see [Progress indicators](../components/status/progress-indicators).
> 콘텐츠가 로드 중이고 완료되는 데 걸리는 시간을 명확히 전달합니다. 컨텐츠는 즉시 표시되지만 로드하는 데 1분 또는 2분 이상 걸리는 상황의 경우 시스템 제공 구성요소(진행 표시기)를 사용하여 컨텐츠가 로드 중임을 표시할 수 있습니다. 일반적으로 로딩에 걸리는 시간을 알 때는 확정 진행률 표시기를 사용하고, 로딩 기간을 정량화할 수 없을 때는 불확정 진행률 표시기를 사용합니다. 예를 들어 macOS에서 파인더는 파일 복사가 완료되는 데 걸리는 시간을 측정하기 위해 결정적 진행 표시줄과 간단한 설명 텍스트를 결합합니다. 자세한 내용은 진행률 표시를 참조하십시오.
>




**If loading takes an unavoidably long time, consider giving people something to view while they wait.** For example, you might provide hints about gameplay, show short video sequences, or display informative placeholder graphics. Gauge the remaining loading time as accurately as possible to help you avoid giving people too little time to enjoy interesting content or having so much time that you need to repeat content.
> 로딩이 불가피하게 오래 걸릴 경우 기다리는 동안 볼 수 있는 무언가를 제공하는 것을 고려해 보십시오. 예를 들어 게임 플레이에 대한 힌트를 제공하거나 짧은 비디오 시퀀스를 표시하거나 유용한 자리 표시자 그래픽을 표시할 수 있습니다. 남은 로딩 시간을 최대한 정확하게 측정하여 사람들에게 흥미로운 콘텐츠를 즐길 시간을 너무 적게 주거나 콘텐츠를 반복해야 할 시간이 너무 많아지지 않도록 합니다.
>




**Consider customizing loading screens.** Although standard progress indicators are usually OK, they can sometimes feel out of context. Consider designing a more immersive experience through custom animations and elements that match the style of your app or game.
> 로딩 화면을 사용자 정의하는 것을 고려해 보십시오. 표준 진행률 지표는 일반적으로 괜찮지만, 때때로 문맥을 벗어난다고 느낄 수 있다. 당신의 앱이나 게임의 스타일에 맞는 맞춤형 애니메이션과 요소를 통해 더 몰입감 있는 경험을 디자인하는 것을 고려해보세요.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항 없음.
>




# **watchOS**

**As much as possible, avoid showing a loading indicator in your watchOS experience.** People expect quick interactions with their Apple Watch, so aim to display content immediately. In situations where content needs a second or two to load, it’s better to display a loading indicator than a blank screen.
> 가능한 한 시계에 적재 표시기가 표시되지 않도록 하십시오.OS 경험. 사람들은 그들의 애플워치와의 빠른 상호작용을 기대하기 때문에, 즉시 콘텐츠를 표시하는 것을 목표로 한다. 콘텐츠를 로드하는 데 1~2초가 필요한 상황에서는 빈 화면보다 로드 표시기를 표시하는 것이 좋습니다.
>




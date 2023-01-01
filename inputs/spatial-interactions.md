# **[inputs] spatial-interactions**

## Spatial interactions enable on-device experiences that integrate the presence of people and objects in the nearby environment.
> 공간 상호 작용은 가까운 환경에서 사람과 물체의 존재를 통합하는 장치 내 경험을 가능하게 한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-spatial-interaction-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-spatial-interaction-intro_2x.png)

A great spatial interaction feels intuitive and natural to people, because it builds on their innate spatial awareness of the world around them. For example, a person playing music on their iPhone can continue listening on their HomePod mini when they bring the devices close together, simply by transferring the audio output from their iPhone to the HomePod mini.
> 위대한 공간적 상호작용은 사람들에게 직관적이고 자연스럽게 느껴지는데, 왜냐하면 그것은 그들 주변의 세계에 대한 그들의 타고난 공간적 인식을 기반으로 하기 때문이다. 예를 들어, 아이폰에서 음악을 재생하는 사람은 아이폰에서 홈팟 미니로 오디오 출력을 전송하는 것만으로 장치를 가까이 가져와도 홈팟 미니로 계속 들을 수 있습니다.
>




Spatial interactions are available on devices that support Ultra Wideband technology (to learn more, see [Ultra Wideband availability](https://support.apple.com/en-us/HT212274)), and rely on the [Nearby Interaction](https://developer.apple.com/documentation/nearbyinteraction) framework. Before participating in spatial interaction experiences, people grant permission for their device to interact while they’re using your app. The Nearby Interaction APIs help you preserve people’s privacy by relying on randomly generated device identifiers that last only as long as the interaction session your app initiates.
> 공간 상호 작용은 Ultra Wideband 기술을 지원하는 장치에서 사용할 수 있으며(자세한 내용은 Ultra Wideband 가용성 참조), 근거리 상호 작용 프레임워크에 의존합니다. 공간 상호 작용 경험에 참여하기 전에 사람들은 앱을 사용하는 동안 장치가 상호 작용할 수 있는 권한을 부여합니다. 주변 상호 작용 API는 앱이 시작하는 상호 작용 세션 동안만 지속되는 임의로 생성된 장치 식별자에 의존하여 사람들의 개인 정보를 보존하는 데 도움이 됩니다.
>




# **Best practices**

**Consider a task from the perspective of the physical world to find inspiration for a spatial interaction.** For example, although people can easily use your app’s UI to transfer a song from their iPhone to their HomePod mini, initiating the transfer by bringing the devices close together makes the task feel rooted in the physical world. Discovering the physical actions that inform the concept of a task can help you create an engaging experience that makes performing it feel easy and natural.
> 물리적 세계의 관점에서 공간적 상호 작용을 위한 영감을 찾기 위한 작업을 고려해 보십시오. 예를 들어, 사람들이 쉽게 당신의 앱 UI를 사용하여 아이폰에서 홈팟 미니로 노래를 전송할 수 있지만, 장치들을 서로 가깝게 함으로써 전송을 시작하면 작업이 물리적 세계에 뿌리를 두고 있는 것처럼 느껴집니다. 작업의 개념을 알려주는 물리적 동작을 발견하면 작업을 수행하는 것이 쉽고 자연스럽게 느낄 수 있는 매력적인 경험을 만들 수 있습니다.
>




**Use distance, direction, and context to inform an interaction.** Although your app may get information from a variety of sources, prioritizing nearby, contextually relevant information can help you deliver experiences that feel organic. For example, if people want to share content with a friend in a crowded room, the iOS share sheet can suggest a likely recipient by using on-device knowledge about the person’s most frequent and recent contacts. Combining this knowledge with information from nearby devices that include the U1 chip can let the share sheet improve the experience by suggesting the closest contact the person is facing.
> 거리, 방향 및 컨텍스트를 사용하여 상호 작용을 알립니다. 앱이 다양한 소스로부터 정보를 얻을 수 있지만, 근처에 있는 컨텍스트 관련 정보의 우선 순위를 지정하면 유기적인 느낌을 주는 경험을 제공하는 데 도움이 될 수 있습니다. 예를 들어, 사람들이 붐비는 방에서 친구와 콘텐츠를 공유하고 싶다면 iOS 공유 시트는 그 사람의 가장 빈번한 연락처와 최근 연락처에 대한 장치 내 지식을 사용하여 가능한 수신자를 제안할 수 있다. 이러한 지식을 U1 칩을 포함하는 주변 장치의 정보와 결합하면 당사자가 직면한 가장 가까운 접촉을 제안함으로써 Share Sheet가 경험을 개선할 수 있습니다.
>




**Consider how changes in physical distance can guide a spatial interaction.** In the physical world, people generally expect their perception of an object to sharpen as they get closer to it. A spatial interaction can mirror this experience by providing feedback that changes with the proximity of an object. For example, when people use iPhone to find an AirTag, the display transitions from a directional arrow to a pulsing circle as they get closer.
> 물리적 거리의 변화가 어떻게 공간적 상호작용을 이끌 수 있는지 생각해보라. 물리적 세계에서, 사람들은 일반적으로 물체에 대한 그들의 인식이 그것에 가까워질수록 날카로워지기를 기대한다. 공간적 상호작용은 물체의 근접성에 따라 변화하는 피드백을 제공함으로써 이러한 경험을 반영할 수 있다. 예를 들어, 사람들이 에어태그를 찾기 위해 아이폰을 사용할 때, 그들이 가까워질수록 디스플레이는 방향 화살표에서 펄스 원으로 전환된다.
>





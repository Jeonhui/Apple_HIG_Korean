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




**Provide continuous feedback.** Continuous feedback reflects the dynamism of the physical world and strengthens the connection between a spatial interaction and the task people are performing. For example, when looking for a lost item in Find My, people get continuous updates that communicate the item’s direction and proximity. Keep people engaged by providing uninterrupted feedback that responds to their movements.
> 지속적인 피드백을 제공합니다. 지속적인 피드백은 물리적 세계의 역동성을 반영하고 공간적 상호작용과 사람들이 수행하는 작업 사이의 연결을 강화합니다. 예를 들어, 내 찾기에서 분실물을 찾을 때 사람들은 그 물건의 방향과 근접성을 알려주는 지속적인 업데이트를 받는다. 사용자의 움직임에 반응하는 중단 없는 피드백을 제공하여 사용자를 참여시킵니다.
>




**Consider using multiple feedback types to create a holistic experience.**Fluidly transitioning among visual, audible, and haptic feedback can help a spatial interaction’s task feel more engaging and real. Using more than one type of feedback also lets you vary the experience to coordinate with both the task and the current context. For example, while people are interacting with the device screen, visual feedback makes sense; while people are interacting with their environment, audible and haptic feedback complement their shift in focus.
> 전체적인 경험을 만들기 위해 여러 피드백 유형을 사용하는 것을 고려해 보십시오.시각적, 청각적 및 촉각적 피드백 사이에서 유동적으로 전환하면 공간 상호 작용의 작업이 더 매력적이고 실제적으로 느낄 수 있다. 두 가지 이상의 피드백 유형을 사용하면 작업 및 현재 컨텍스트와 조정할 수 있는 환경을 변경할 수도 있습니다. 예를 들어, 사람들이 기기 화면과 상호작용하는 동안 시각적 피드백은 의미가 있다. 사람들이 환경과 상호작용하는 동안 청각적 및 촉각적 피드백은 초점의 변화를 보완한다.
>




**Avoid using a spatial interaction as the only way to perform a task.** You can’t assume that everyone can experience a spatial interaction, so it’s essential to provide alternative ways to get things done in your app.
> 작업을 수행하는 유일한 방법으로 공간 상호 작용을 사용하는 것을 피하십시오. 모든 사람이 공간 상호 작용을 경험할 수 있다고 가정할 수는 없으므로 앱에서 작업을 수행할 수 있는 다른 방법을 제공하는 것이 필수적입니다.
>




# **Device usage**

**Encourage people to hold the device in portrait orientation.** Holding a device in landscape can decrease the accuracy and availability of information about the distance and relative direction of other devices. If you support only portrait orientation while your spatial interaction feature runs, prefer giving people implicit, visual feedback on how to hold the device for an optimal experience; when possible, avoid explicitly telling people to hold the device in portrait.
> 사람들이 장치를 세로 방향으로 잡도록 권장합니다. 가로 방향으로 잡으면 다른 장치의 거리와 상대적 방향에 대한 정보의 정확성과 가용성이 저하될 수 있습니다. 공간 상호 작용 기능이 실행되는 동안 세로 방향만 지원하는 경우 최적의 경험을 위해 장치를 잡는 방법에 대해 암시적이고 시각적인 피드백을 사람들에게 제공하는 것이 좋습니다. 가능하면 사람들에게 장치를 세로 방향으로 고정하라고 명시적으로 말하지 마십시오.
>




**Design for the device’s directional field of view.** Nearby interaction relies on a hardware sensor with a specific field of view similar to that of the Ultra Wide camera in iPhone 11 and later. If a participating device is outside of this field of view, your app might receive information about its distance, but not its relative direction.
> 장치의 방향 시야를 위한 디자인. 근처 상호 작용은 아이폰 11 이상의 울트라 와이드 카메라와 유사한 특정 시야를 가진 하드웨어 센서에 의존한다. 참여 단말기가 이 시야 밖에 있는 경우 앱은 상대적인 방향이 아닌 거리에 대한 정보를 수신할 수 있습니다.
>




**Help people understand how intervening objects can affect the nearby interaction experience in your app.** When other people, animals, or sufficiently large objects come between two participating devices, the accuracy or availability of distance and direction information can decrease. Consider adding advice on avoiding this situation to onboarding or tutorial content you present.
> 다른 사람, 동물 또는 충분히 큰 개체가 두 개의 참여 장치 사이에 있으면 거리 및 방향 정보의 정확성이나 가용성이 저하될 수 있습니다. 이러한 상황을 피하는 방법에 대한 조언을 제공하는 온보딩 또는 튜토리얼 콘텐츠에 추가하는 것을 고려해 보십시오.
>




# **Platform considerations**

*No additional considerations for iPadOS. Not supported in macOS or tvOS.*
> iPadOS에 대한 추가 고려 사항은 없습니다. macOS 또는 tvOS에서는 지원되지 않습니다.
>




# **iOS**

On iPhone, Nearby Interaction APIs provide a peer device’s distance and direction.
> 아이폰에서 근거리 상호작용 API는 피어 장치의 거리와 방향을 제공한다.
>




# **watchOS**

On Apple Watch, Nearby Interaction APIs provide a peer device’s distance. Also, all watchOS apps participating in a nearby interaction experience must be in the foreground.
> Apple Watch에서 Neighbor Interaction API는 피어 장치의 거리를 제공합니다. 또한, 모든 시계가까운 상호 작용 경험에 참여하는 OS 앱이 전면에 있어야 합니다.
>




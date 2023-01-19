# **[technologies-carplay] interaction**

# **Audio**

Regardless of whether audio is a primary aspect of your app’s experience, you need to know how people expect audio to behave and meet those expectations.
> 오디오가 앱 경험의 주요 측면인지 여부에 관계없이, 사람들이 오디오가 어떻게 작동하고 그러한 기대를 충족시키길 기대하는지 알아야 한다.
>




**Transition to the Now Playing screen only when content is ready to play.** Due to buffering and network conditions, it may take several seconds for audio to begin playing after a user selects it. The user’s selection remains highlighted, and a spinning activity indicator is displayed until your app informs the system that the audio is ready to play.
> 콘텐츠를 재생할 준비가 되었을 때만 지금 재생 화면으로 전환합니다. 버퍼링 및 네트워크 상태로 인해 사용자가 오디오를 선택한 후 재생을 시작하는 데 몇 초가 걸릴 수 있습니다. 앱에서 오디오를 재생할 준비가 되었다고 시스템에 알릴 때까지 사용자의 선택이 강조 표시되고 회전 작업 표시기가 표시됩니다.
>




**Start playback as soon as audio has sufficiently loaded, even if descriptive information is still loading.** Continue loading descriptive information in the background, and show it once it's available.
> 설명 정보가 여전히 로드 중인 경우에도 오디오가 충분히 로드되면 바로 재생을 시작합니다. 배경에 설명 정보를 계속 로드하고 사용 가능한 경우 표시합니다.
>




**Avoid beginning playback automatically.** Unless your app’s purpose is to play a single source of audio, or your app is resuming previously interrupted audio, it shouldn’t begin playback until the user initiates it.
> 앱의 목적이 단일 오디오 소스를 재생하는 것이거나 이전에 중단된 오디오를 다시 시작하는 것이 아니라면 사용자가 재생을 시작할 때까지 재생을 시작하면 안 됩니다.
>




**Resume audio playback after an interruption only when it's appropriate.** Temporary interruptions such as incoming phone calls are resumable. Permanent interruptions, such as a music playlist initiated by Siri, are nonresumable. When a resumable interruption occurs, your app should resume playback when the interruption ends if audio was actively playing when the interruption started.
> 중단 후 오디오 재생을 다시 시작합니다. 걸려오는 전화와 같은 일시적인 중단은 다시 시작할 수 있습니다. 시리가 시작한 음악 재생 목록과 같은 영구적인 중단은 재개할 수 없습니다. 재개 가능한 중단이 발생하면 중단이 시작되었을 때 오디오가 재생 중이었다면 중단이 종료될 때 앱이 재생을 재개해야 합니다.
>




**Adjust levels automatically when necessary, but not the overall volume.** Your app can adjust relative, independent volume levels to achieve a great mix of audio. However, the final output volume should always be controlled by the user.
> 전체 볼륨은 아니지만 필요할 때 자동으로 레벨을 조정할 수 있습니다. 앱은 상대적이고 독립적인 볼륨 레벨을 조정하여 오디오를 훌륭하게 혼합할 수 있습니다. 그러나 최종 출력 볼륨은 항상 사용자가 제어해야 합니다.
>




**Use the system’s sound services for short sounds, such as a sound accompanying an alert.**For developer guidance, see [System Sound Services](https://developer.apple.com/documentation/audiotoolbox/system_sound_services).
> 경고에 수반되는 소리와 같은 짧은 소리에 대해서는 시스템의 사운드 서비스를 사용합니다.개발자 지침은 시스템 사운드 서비스를 참조하십시오.
>




If your app is an audio app, see [Audio apps](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/introduction#audio-apps) for related design guidance.
> 앱이 오디오 앱인 경우 오디오 앱에서 관련 설계 지침을 참조하십시오.
>




# **Car data**

Automaker apps that implement a custom data interface can integrate with a vehicle to retrieve and respond to data such as climate, radio information, speed, and GPS location. An app might offer a dashboard screen, for example, that presents climate and speed information in a highly visual manner.
> 맞춤형 데이터 인터페이스를 구현하는 자동차 회사 앱은 차량과 통합해 기후, 라디오 정보, 속도, GPS 위치 등의 데이터를 검색하고 대응할 수 있다. 예를 들어, 앱은 기후 및 속도 정보를 매우 시각적으로 표시하는 대시보드 화면을 제공할 수 있다.
>




**Respond gracefully when data is unavailable.** Data can become unavailable in the car for a variety of reasons, such as losing the GPS connection while driving through a tunnel. Make sure your app handles connection problems nonintrusively.
> 데이터를 사용할 수 없을 때 우아하게 응답하십시오. 터널을 통과하는 동안 GPS 연결이 끊어지는 등 다양한 이유로 차량에서 데이터를 사용할 수 없게 될 수 있습니다. 앱이 연결 문제를 비침입적으로 처리하는지 확인합니다.
>




For guidance regarding the development of a custom data interface, see [ExternalAccessory](https://developer.apple.com/documentation/externalaccessory).
> 사용자 지정 데이터 인터페이스 개발에 대한 지침은 외부 부속품을 참조하십시오.
>




# **iPhone**

CarPlay shows compatible apps from the user’s connected iPhone on the car’s built-in display, applying simplified interfaces that are optimized for use while driving.
> 카플레이는 사용자가 연결한 아이폰의 호환 앱을 자동차 내장 디스플레이에 보여주며, 운전 중 사용에 최적화된 단순화된 인터페이스를 적용한다.
>




**Eliminate app interactions on iPhone when CarPlay is active.** CarPlay is the best and safest way to interact with apps while driving, and interactions should occur using the car’s built-in controls and display. Any required setup on iPhone should occur before the vehicle is in motion.
> CarPlay가 활성화되면 iPhone에서 앱 상호작용을 제거합니다. CarPlay는 운전 중 앱과 상호작용하는 가장 안전한 방법이며, 자동차의 내장된 제어장치와 디스플레이를 사용하여 상호작용이 이루어져야 합니다. iPhone에 필요한 설정은 차량이 이동하기 전에 수행해야 합니다.
>




**Never lock the user out of CarPlay because the connected iPhone requires input.** Assume that the iPhone is inaccessible when CarPlay is active. If a problem must be resolved on the connected iPhone, let the user do so once the vehicle is stopped.
> 연결된 iPhone에 입력이 필요하므로 사용자를 CarPlay에서 잠그지 마십시오. CarPlay가 활성화되어 있을 때 iPhone에 액세스할 수 없다고 가정합니다. 연결된 iPhone에서 문제를 해결해야 하는 경우 차량이 정지된 후 사용자가 해결하도록 합니다.
>




**Make sure your app works when the iPhone is locked or in the trunk.** When CarPlay is active, the user’s phone may be locked or otherwise inaccessible. Your app should function regardless.
> iPhone이 잠겨 있거나 트렁크에 있을 때 앱이 작동하는지 확인하십시오. CarPlay가 활성화되면 사용자의 전화가 잠겨 있거나 액세스할 수 없습니다. 앱은 상관없이 작동해야 합니다.
>




# **Knobs and controls**

Vehicles that support CarPlay have physical controls (buttons, knobs, and touchpads, for example) that supplement the touchscreen and, in some cases, serve as the primary means of user input. At minimum, a Siri button, navigation controls, selection controls, and back controls are always present when physical controls provide the primary means of user input.
> CarPlay를 지원하는 차량에는 터치스크린을 보완하는 물리적 제어장치(예: 버튼, 노브 및 터치패드)가 있으며 경우에 따라 사용자 입력의 주요 수단으로 사용된다. 물리적 조정기가 사용자 입력의 주요 수단을 제공할 때는 최소한 시리 버튼, 항법 조정기, 선택 조정기 및 뒤로 조정기가 항상 존재한다.
>




**Respond to media controls as expected.** If your app offers audio playback features, it should respond when the user presses a physical play, pause, next track, previous track, fast forward, and rewind button in the car. For developer guidance, see [MPRemoteCommandCenter](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter).
> 예상대로 미디어 컨트롤에 응답합니다. 앱에서 오디오 재생 기능을 제공하는 경우 사용자가 차량에서 물리적 재생, 일시 중지, 다음 트랙, 이전 트랙, 빨리 감기 및 되감기 버튼을 누를 때 응답해야 합니다. 개발자 지침은 MPR 원격 명령 센터를 참조하십시오.
>




### **Focus-based navigation**

CarPlay has a focus model that helps people move through onscreen interface elements using a knob or touchpad when the built-in display doesn’t support touch interactions. By rotating a knob or swiping a touchpad, focus moves from element to element, stopping on a specific one. The user can then press the knob, tap the touchpad, or press a button to activate or interact with the element.
> CarPlay에는 내장 디스플레이가 터치 상호 작용을 지원하지 않을 때 노브 또는 터치 패드를 사용하여 화면 인터페이스 요소를 이동할 수 있도록 도와주는 포커스 모델이 있습니다. 노브를 돌리거나 터치 패드를 스와이프하면 포커스가 요소에서 요소로 이동하여 특정 요소에서 멈춥니다. 그런 다음 사용자는 노브를 누르거나 터치 패드를 가볍게 두드리거나 버튼을 눌러 요소를 활성화하거나 상호 작용할 수 있습니다.
>




Play

**Position onscreen elements so the user can navigate logically from item to item.** Changes in focus should be predictable.
> 사용자가 항목 간에 논리적으로 탐색할 수 있도록 화면 요소를 배치합니다. 초점의 변화는 예측 가능해야 합니다.
>




For developer guidance, see [UIFocusEnvironment](https://developer.apple.com/documentation/uikit/uifocusenvironment).

# **Touchscreen**

Users can interact with a CarPlay app by performing gestures on the car’s built-in touchscreen display. CarPlay supports both low-fidelity and high-fidelity touchscreen displays. High-fidelity screens have lower finger-tracking latency than low-fidelity screens, and therefore support more gestures. Depending on the display, CarPlay apps can respond single-finger gestures, as follows.
> 사용자는 자동차의 내장 터치스크린 디스플레이에서 제스처를 수행하여 카플레이 앱과 상호 작용할 수 있다. 카플레이는 저충실도와 고충실도 터치스크린 디스플레이를 모두 지원한다. 충실도가 높은 화면은 충실도가 낮은 화면보다 손가락 추적 지연 시간이 낮기 때문에 더 많은 제스처를 지원한다. 디스플레이에 따라 CarPlay 앱은 다음과 같이 한 손가락 제스처에 응답할 수 있습니다.
>




| Gesture | Usage | Low-fidelity screen | High-fidelity screen |
| --- | --- | --- | --- |
| Tap | Activates a control or selects an item. | ● | ● |
| Double-tap | Zooms in and centers content. | ● | ● |
| Touch and hold | Activates a control for a period of time. For example, touching and holding the Next Track button in the Music app fast-forwards the currently playing track. | ● | ● |
| Flick | Scrolls or pans quickly. |  | ● |
| Drag | Moves an element from side-to-side or drags an element across the screen. |  | ● |

**Minimize touchscreen interactions.** Don’t expect people to keep reaching out to touch the screen, especially while the car is in motion. Require as few manual interactions as possible to reach content and initiate functions.
> 터치 스크린 상호 작용을 최소화합니다. 특히 자동차가 움직이는 동안 사람들이 계속 손을 뻗어 스크린을 만지는 것을 기대하지 마십시오. 콘텐츠에 접근하고 기능을 시작하기 위해 가능한 한 적은 수의 수동 상호 작용이 필요합니다.
>




# **Siri**

Siri is an essential feature of CarPlay that facilitates distraction-free, voice-driven app interactions. Certain types of apps can integrate with Siri to perform tasks in response to spoken commands and questions from users.
> 시리는 카플레이의 필수 기능으로, 산만함이 없고 음성으로 구동되는 앱 상호작용을 촉진한다. 특정 유형의 앱은 Siri와 통합하여 음성 명령과 사용자의 질문에 응답하여 작업을 수행할 수 있습니다.
>




| Type of app | Supported Siri interactions |
| --- | --- |
| Automaker apps | Change the audio source.Change the climate.Change the defroster settings.Change seat settings.Change the radio station.Save and load driver profiles. |
| Messaging apps | Send messages.Read received messages. |
| Voice over Internet Protocol (VoIP) apps | Start audio calls. |

A voice command button on the steering wheel activates Siri, even when CarPlay isn’t visible on the car’s built-in display. Once activated, Siri handles the language processing and semantic analysis needed to turn spoken requests into actionable instructions your app can handle. You’re responsible for defining the tasks your app handles. Your app must validate the information it receives, provide information for Siri to present, and take action. While validating information, if something is missing or unclear, your app can instruct Siri to request confirmation or more information.
> 자동차의 내장 디스플레이에 CarPlay가 보이지 않을 때에도 스티어링 휠의 음성 명령 버튼이 Siri를 활성화합니다. 일단 활성화되면, Siri는 음성 요청을 당신의 앱이 처리할 수 있는 실행 가능한 명령으로 바꾸는 데 필요한 언어 처리와 의미 분석을 처리한다. 사용자는 앱에서 처리하는 작업을 정의할 책임이 있습니다. 당신의 앱은 그것이 받는 정보를 검증하고, Siri가 제시할 정보를 제공하고, 조치를 취해야 한다. 정보를 확인하는 동안, 무언가가 누락되거나 불분명한 경우, 당신의 앱은 시리에게 확인이나 더 많은 정보를 요청하도록 지시할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Siri_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Siri_2x.png)

**Respond quickly and minimize interaction.** People use Siri for convenience, so don't make them wait for a response. Your app should validate information and take action as quickly as possible after receiving a request. When clarification or additional information is needed, present efficient, focused choices that reduce the possibility of additional prompting.
> 신속하게 응답하고 상호작용을 최소화하십시오. 사람들은 편의상 시리를 사용하므로 응답을 기다리게 하지 마십시오. 당신의 앱은 정보를 확인하고 요청을 받은 후 가능한 한 빨리 조치를 취해야 한다. 명확한 설명이나 추가 정보가 필요한 경우, 추가적인 프롬프트의 가능성을 줄이는 효율적이고 집중적인 선택을 제시한다.
>




**Increase accuracy with custom vocabulary.** Help Siri learn more about the actions your app performs by defining specific terms people might use in requests. These terms should be nongeneric and unique to your app. Never include other app names, terms that are obviously connected with other apps, inappropriate language, or reserved phrases, such as “Hey Siri.” Note that any terms you define are used by Siri to help resolve requests, but aren’t guaranteed to be recognized.
> 사용자 지정 어휘를 사용하여 정확도를 높입니다. Siri가 사용자가 요청할 때 사용할 수 있는 특정 용어를 정의하여 앱이 수행하는 작업에 대해 자세히 알아볼 수 있도록 도와줍니다. 이러한 용어는 일반적이지 않고 앱에 고유해야 합니다. 다른 앱 이름, 다른 앱과 분명히 연결된 용어, 부적절한 언어 또는 예약된 문구(예: "안녕 시리")를 포함하지 마십시오 사용자가 정의한 용어는 Siri가 요청을 해결하는 데 도움을 주기 위해 사용되지만 인식된다는 보장은 없습니다.
>




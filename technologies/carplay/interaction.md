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


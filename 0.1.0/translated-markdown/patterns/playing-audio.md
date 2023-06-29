# **[patterns] playing-audio**

# People expect rich audio experiences that automatically adjust when the context changes on the device.
> 사람들은 장치의 콘텍스트가 바뀌면 자동으로 조정되는 풍부한 오디오 경험을 기대한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-audio-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-audio-intro-dark_2x.png)

Devices can play audio in a variety of ways, such as through internal or external speakers, headphones, and wirelessly through Bluetooth or AirPlay-enabled devices. To manipulate sound on their devices people use several types of controls, including volume buttons, the Ring/Silent switch on iPhone, headphone controls, the Control Center volume slider, and sound controls in third-party accessories. Whether sound is a primary part of your experience or an embellishment, you need to make sure it behaves as people expect as they make changes to volume and output.
> 장치는 내부 또는 외부 스피커, 헤드폰을 통해, 블루투스 또는 에어플레이 지원 장치를 통해 무선으로 오디오를 재생할 수 있습니다. 장치에서 소리를 조작하려면 볼륨 버튼, iPhone의 벨소리/사일런트 스위치, 헤드폰 컨트롤, Control Center 볼륨 슬라이더 및 타사 액세서리의 사운드 컨트롤을 비롯한 여러 가지 유형의 컨트롤을 사용합니다. 사운드가 경험의 주요 부분인지 또는 장식인지 여부에 관계없이, 음량과 출력을 변경할 때 사람들이 기대하는 대로 동작하는지 확인해야 합니다.
>




**Silence.** People switch their device to silent when they want to avoid being interrupted by unexpected sounds like ringtones and incoming message tones. In this scenario, they also want to silence nonessential sounds, such as keyboard clicks, sound effects, game soundtracks, and other audible feedback. When a device is in silent mode, it should play only the audio that people explicitly initiate, like media playback, alarms, and audio/video messaging.
> 침묵. 사람들은 벨소리나 들어오는 메시지 톤과 같은 예상치 못한 소리에 방해를 받지 않으려면 장치를 무음으로 전환한다. 이 시나리오에서는 키보드 클릭, 음향 효과, 게임 사운드 트랙 및 기타 청각 피드백과 같은 중요하지 않은 소리도 음소거하려고 합니다. 장치가 자동 모드일 때는 미디어 재생, 경보 및 오디오/비디오 메시징과 같이 사용자가 명시적으로 시작한 오디오만 재생해야 합니다.
>




**Volume.** People expect their volume settings to affect all sound in the system — including music and in-app sound effects — regardless of the method they use to adjust the volume. An exception is the ringer volume on iPhone, which people can adjust separately in Settings.
> 볼륨. 볼륨 설정은 볼륨을 조정하는 방법에 관계없이 음악 및 앱 내 사운드 효과를 포함하여 시스템의 모든 사운드에 영향을 미칠 것으로 예상됩니다. 예외적으로 아이폰의 호출음 볼륨은 설정에서 별도로 조정할 수 있다.
>




**Headphones.** People use headphones to keep their listening private and to free their hands. When plugging in headphones, users expect sound to reroute automatically without interruption; when unplugging headphones, they expect playback to pause immediately.
> 헤드폰. 사람들은 헤드폰을 사용하여 듣는 것을 비공개로 유지하고 손을 자유롭게 합니다. 헤드폰을 꽂을 때 사용자는 중단 없이 소리가 자동으로 재루팅되고 헤드폰을 뽑을 때 재생이 즉시 일시 중지됩니다.
>




# **Best practices**

**Adjust levels automatically when necessary — don’t adjust the overall volume.** Your app can adjust relative, independent volume levels to achieve a great mix of audio, but the system volume should always govern the final output.
> 필요한 경우 레벨을 자동으로 조정—전체 볼륨을 조정하지 마십시오. 당신의 앱은 오디오의 훌륭한 혼합을 달성하기 위해 상대적이고 독립적인 볼륨 레벨을 조정할 수 있지만, 시스템 볼륨은 항상 최종 출력을 통제해야 한다.
>




**Permit rerouting of audio when possible.** People often want to select a different audio output device. For example, they may want to listen to music through their living room stereo, car radio, or Apple TV. Support this capability unless there’s a compelling reason not to.
> 가능한 경우 오디오 재루팅을 허용합니다. 사람들은 종종 다른 오디오 출력 장치를 선택하기를 원한다. 예를 들어, 그들은 거실 스테레오, 자동차 라디오 또는 애플 TV를 통해 음악을 듣고 싶어할 수 있습니다. 특별한 이유가 없는 한 이 기능을 지원하십시오.
>




**Use the system-provided volume view to let people make audio adjustments.** The volume view includes a volume-level slider and a control for rerouting audio output. You can customize the appearance of the slider. For developer guidance, see [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview).
> 시스템에서 제공하는 볼륨 보기를 사용하여 사용자가 오디오를 조정할 수 있습니다. 볼륨 뷰에는 볼륨 레벨 슬라이더 및 오디오 출력 재루팅을 위한 컨트롤이 포함됩니다. 슬라이더의 모양을 사용자 정의할 수 있습니다. 개발자 지침은 MPVolumeView를 참조하십시오.
>




**Choose an audio category that fits the way your app or game uses sound.** Depending on the audio category you choose, your app’s sounds can mix with other audio, play while your app is in the background, or stop when people set the Ring/Silent switch to silent. As much as possible, pick a category that helps your app meet people’s expectations. For example, don’t make people stop listening to music from another app if you don’t need to. For developer guidance, see [AVAudioSession.Category](https://developer.apple.com/documentation/avfaudio/avaudiosession/category).
> 앱이나 게임이 소리를 사용하는 방식에 맞는 오디오 범주를 선택합니다. 선택한 오디오 범주에 따라 앱의 소리가 다른 오디오와 섞이거나, 앱이 백그라운드에 있는 동안 재생하거나, 벨소리/사일런트 스위치를 무음으로 설정하면 중지될 수 있습니다. 가능한 한, 당신의 앱이 사람들의 기대를 충족시키는 데 도움이 되는 카테고리를 선택하세요. 예를 들어, 다른 앱에서 음악을 들을 필요가 없다면 사람들이 듣는 것을 멈추게 하지 마세요. 개발자 지침은 AVAudioSession을 참조하십시오.카테고리.
>




**Respond to audio controls only when it makes sense.** People can control audio playback from outside your app’s interface — such as in Control Center or with controls on their headphones — regardless of whether your app is in the foreground or background. If your app is actively playing audio, in a clear audio-related context, or connected to a Bluetooth or AirPlay-enabled device, it’s fine to respond to audio controls. Otherwise, when people activate a control, avoid halting currently playing from another app.
> 오디오 컨트롤에 응답하는 것은 의미가 있을 때만 가능합니다. 사용자는 앱이 전경 또는 배경에 있는지 여부에 관계없이 제어 센터 또는 헤드폰의 컨트롤을 사용하여 앱 인터페이스 외부에서 오디오 재생을 제어할 수 있습니다. 앱이 오디오를 능동적으로 재생하고 있거나 오디오 관련 컨텍스트가 명확하거나 Bluetooth 또는 AirPlay 지원 장치에 연결되어 있는 경우 오디오 컨트롤에 응답해도 괜찮습니다. 그렇지 않으면, 사람들이 컨트롤을 활성화할 때 다른 앱에서 현재 재생하는 것을 중단하지 마십시오.
>




**Avoid repurposing audio controls.** People expect audio controls to behave consistently in all apps, so it’s essential to avoid redefining the meaning of an audio control in your app. If your app doesn’t support certain controls, don’t respond to them.
> 오디오 컨트롤의 용도를 변경하지 마십시오. 사람들은 오디오 컨트롤이 모든 앱에서 일관되게 작동하기를 기대하기 때문에 앱에서 오디오 컨트롤의 의미를 재정의하는 것을 피하는 것이 필수적이다. 앱이 특정 컨트롤을 지원하지 않는 경우 해당 컨트롤에 응답하지 마십시오.
>




**Consider creating custom audio player controls only if you need to offer commands that the system doesn’t support.** For example, you might want to define custom increments for skipping forward or backward, or present content that's related to the playing audio, such as a sports score.
> 시스템에서 지원하지 않는 명령을 제공해야 하는 경우에만 사용자 지정 오디오 플레이어 컨트롤을 만드는 것이 좋습니다. 예를 들어 앞으로 또는 뒤로 건너뛰기 위한 사용자 지정 증분을 정의하거나 스포츠 점수 등 재생 오디오와 관련된 콘텐츠를 표시할 수 있습니다.
>




**Let other apps know when your app finishes playing temporary audio.** If your app can temporarily interrupt the audio of other apps, be sure to flag your audio session in a way that lets other apps know when they can resume. For developer guidance, see [notifyOthersOnDeactivation](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactiveoptions/1616603-notifyothersondeactivation).
> 프로그램이 임시 오디오 재생을 마치면 다른 앱에 알립니다. 앱이 일시적으로 다른 앱의 오디오를 중단시킬 수 있는 경우, 다른 앱에서 언제 다시 시작할 수 있는지 알려주는 방식으로 오디오 세션에 플래그를 지정하십시오. 개발자 지침은 알림을 참조하십시오.기타 비활성화 시.
>




# **Handling interruptions**

Although most apps and games rely on the system’s default interruption behavior, you can customize this behavior to better accommodate your needs.
> 대부분의 앱과 게임은 시스템의 기본 중단 동작에 의존하지만, 이 동작을 사용자 지정하여 사용자의 요구를 더 잘 수용할 수 있습니다.
>




**Determine how to respond to audio-session interruptions.** For example, if your app enables recording or other audio-related tasks that people don’t want interrupted, you can tell the system to avoid interrupting the currently playing audio for an incoming call unless people choose to accept it. Another example is a VoIP app, which must end a call when people close the Smart Folio of their iPad while they’re using the built-in microphone. Closing the Smart Folio automatically mutes the iPad microphone and by default interrupts the audio session associated with it. If a VoIP app restarts the audio session when people reopen their Smart Folio, it risks invading people’s privacy by reenabling the microphone without their knowledge. You can inspect an audio-session interruption to help determine the right way to respond; for developer guidance, see [Responding to audio session interruptions](https://developer.apple.com/documentation/avfaudio/avaudiosession/responding_to_audio_session_interruptions).
> 오디오 세션 중단에 대응하는 방법을 결정합니다. 예를 들어, 앱에서 사용자가 중단하지 않으려는 녹음 또는 기타 오디오 관련 작업을 사용할 수 있는 경우, 사용자가 수신 전화를 수락하지 않는 한 현재 재생 중인 오디오를 중단하지 않도록 시스템에 지시할 수 있습니다. 또 다른 예는 VoIP 앱으로, 사람들이 내장 마이크를 사용하는 동안 아이패드의 스마트 폴리오를 닫으면 통화를 종료해야 합니다. 스마트 폴리오를 닫으면 iPad 마이크로폰이 자동으로 음소거되고 기본적으로 연결된 오디오 세션이 중단됩니다. 사람들이 스마트 폴리오를 다시 열었을 때 VoIP 앱이 오디오 세션을 다시 시작하면 자신도 모르게 마이크를 다시 활성화하여 사람들의 사생활을 침해할 위험이 있다. 오디오 세션 중단을 검사하여 올바른 응답 방법을 결정할 수 있습니다. 개발자 지침은 오디오 세션 중단에 응답을 참조하십시오.
>




**When an interruption ends, determine whether to resume audio playback automatically.** Sometimes, audio from a different app can interrupt the audio your app is playing. An interruption can be *resumable*, like an incoming phone call, or *nonresumable*, like when people start a new music playlist. Use the interruption type and your app’s type to decide whether to resume playback automatically. For example, a media playback app that’s actively playing audio when an interruption occurs can check to be sure the type is resumable before continuing playback when the interruption ends. On the other hand, a game doesn’t need to check the interruption type before automatically resuming playback, because a game plays audio without an explicit user choice. For developer guidance, see [shouldResume](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions/1616528-shouldresume).
> 중단이 끝나면 오디오 재생을 자동으로 재개할지 여부를 결정합니다. 때때로 다른 앱의 오디오가 재생 중인 오디오를 방해할 수 있습니다. 인터럽트는 수신 전화와 같이 다시 시작할 수 있거나 사람들이 새 음악 재생 목록을 시작할 때와 같이 다시 시작할 수 없습니다. 인터럽트 유형 및 앱 유형을 사용하여 자동으로 재생을 재개할지 여부를 결정합니다. 예를 들어 중단이 발생할 때 오디오를 적극적으로 재생하는 미디어 재생 앱은 중단이 종료될 때 재생을 계속하기 전에 유형이 재개되는지 확인할 수 있습니다. 반면에 게임은 자동으로 재생을 재개하기 전에 인터럽트 유형을 확인할 필요가 없다. 개발자 지침은 계속을 참조하십시오.
>




# **Platform considerations**

# **iOS, iPadOS**

**Use the system’s sound services to play short sounds and vibrations.** For developer guidance, see [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio_services).
> 시스템의 사운드 서비스를 사용하여 짧은 소리와 진동을 재생합니다. 개발자 지침은 오디오 서비스를 참조하십시오.
>




# **macOS**

In macOS, notification sounds mix with other audio by default.
> macOS에서 알림 소리는 기본적으로 다른 오디오와 혼합됩니다.
>




# **tvOS**

In tvOS, the system plays audio only when people initiate it, through interactions within apps and games or when performing device calibrations. For example, tvOS doesn’t play sounds to accompany components like alerts or notifications.
> tvOS에서, 이 시스템은 사람들이 그것을 시작할 때, 앱과 게임 내의 상호 작용을 통해 또는 장치 보정을 수행할 때만 오디오를 재생한다. 예를 들어, tvOS는 경고나 알림과 같은 구성 요소에 수반되는 소리를 재생하지 않습니다.
>




# **watchOS**

In watchOS, the system manages audio playback. An app can play short audio clips while it’s active and running in the foreground, or it can play longer audio that continues even when people lower their wrist or switch to another app. For developer guidance, see [Playing background audio](https://developer.apple.com/documentation/watchkit/storyboard_support/playing_background_audio).
> watch OS에서 시스템은 오디오 재생을 관리합니다. 앱은 활성 상태에서 포그라운드에서 실행되는 동안 짧은 오디오 클립을 재생할 수 있으며, 사람들이 손목을 내리거나 다른 앱으로 전환해도 계속 재생되는 긴 오디오를 재생할 수 있습니다. 개발자 지침은 배경 오디오 재생을 참조하십시오.
>




**Use the recommended encoding values for media assets.** Specifically, use the 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding) format to produce good-quality audio with lower data requirements.
> 미디어 자산에 권장되는 인코딩 값을 사용합니다. 특히 64kbps HE-AAC(고효율 고급 오디오 코딩) 형식을 사용하면 데이터 요구 사항이 낮은 고품질 오디오를 생성할 수 있습니다.
>




**Consider** **presenting a Now Playing view so people can control current or recently played audio without leaving your app.** The system-provided Now Playing view also displays information about the current audio source — which might be another app on a person's Apple Watch or iPhone — and automatically selects the current or most recently used source. For developer guidance, see [Adding a Now Playing view](https://developer.apple.com/documentation/watchkit/storyboard_elements/adding_a_now_playing_view).
> 앱을 종료하지 않고 사람들이 현재 또는 최근에 재생한 오디오를 제어할 수 있도록 지금 재생 보기를 제공하는 것을 고려해 보십시오. 또한 시스템에서 제공하는 지금 재생 보기는 사용자의 Apple Watch 또는 iPhone에 있는 다른 앱일 수 있는 현재 오디오 소스에 대한 정보를 표시하고 현재 또는 가장 최근에 사용된 소스를 자동으로 선택합니다. 개발자 지침은 지금 재생 보기 추가를 참조하십시오.
>




| Category | Meaning | Behavior |
| --- | --- | --- |
| Solo ambient | Sound isn’t essential, but it silences other audio. For example, a game with a soundtrack. | Responds to the silence switch.Doesn’t mix with other sounds.Doesn’t play in the background. |
| Ambient | Sound isn’t essential, and it doesn’t silence other audio. For example, a game that lets people play music from another app during gameplay in place of the game’s soundtrack. | Responds to the silence switch.Mixes with other sounds.Doesn’t play in the background. |
| Playback | Sound is essential and might mix with other audio. For example, an audiobook or educational app that teaches a foreign language, which people might want to listen to after leaving the app. | Doesn’t respond to the silence switch.May or may not mix with other sounds.Can play in the background. |
| Record | Sound is recorded. For example, a note-taking app that offers an audio recording mode. An app of this nature might switch its category to playback if it lets people play the recorded notes. | Doesn’t respond to the silence switch.Doesn’t mix with other sounds.Can record in the background. |
| Play and record | Sound is recorded and played, potentially simultaneously. For example, an audio messaging or video calling app. | Doesn’t respond to the silence switch.May or may not mix with other sounds.Can record and play in the background. |

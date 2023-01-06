# **[technologies-airplay] introduction**

## AirPlay lets people stream media content wirelessly from iOS, macOS, and tvOS devices to Apple TV, HomePod, and AirPlay-enabled TVs and speakers.
> 에어플레이는 사람들이 iOS, macOS, tvOS 기기에서 애플 TV, 홈팟, 에어플레이 지원 TV와 스피커로 미디어 콘텐츠를 무선으로 스트리밍할 수 있게 해준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-AirPlay-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-AirPlay-intro_2x.png)

If your app provides media playback, support AirPlay streaming — not just mirroring — for the best user experience.
> 앱에서 미디어 재생을 제공하는 경우 최상의 사용자 환경을 위해 미러링뿐만 아니라 AirPlay 스트리밍을 지원하십시오.
>




To support media playback and AirPlay, adopt the following frameworks:
> 미디어 재생 및 AirPlay를 지원하려면 다음 프레임워크를 사용합니다:
>




- [AVFoundation](https://developer.apple.com/documentation/avfoundation), for media playback
- [AVKit](https://developer.apple.com/documentation/avkit), for the built-in media player, which offers a standard set of user controls and supports features like chapter navigation, subtitles, closed captioning, and AirPlay streaming
- >  AVKit, 내장 미디어 플레이어용으로, 표준 사용자 제어 세트를 제공하고 챕터 탐색, 자막, 클로즈드 캡션 및 AirPlay 스트리밍과 같은 기능을 지원합니다


**Use the system-provided media player.** The built-in media player accommodates the needs of most media apps and provides a consistent playback experience across the system. It's familiar, easy to implement, and adopts new features and improvements automatically. Custom players with unfamiliar interfaces can be confusing and frustrating to people. Design a custom video player only if your app’s needs aren't met by the system-provided player. For developer guidance, see [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller).
> 시스템에서 제공하는 미디어 플레이어를 사용하십시오. 내장된 미디어 플레이어는 대부분의 미디어 앱의 요구를 수용하고 시스템 전체에서 일관된 재생 환경을 제공합니다. 친숙하고 구현하기 쉬우며 새로운 기능과 개선 사항을 자동으로 채택합니다. 익숙하지 않은 인터페이스를 가진 커스텀 플레이어는 사람들에게 혼란스럽고 좌절감을 줄 수 있다. 시스템에서 제공한 플레이어가 앱의 요구 사항을 충족하지 못하는 경우에만 사용자 지정 비디오 플레이어를 설계하십시오. 개발자 지침은 AVPlayerViewController를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_VideoScreen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_VideoScreen_2x.png)

**Provide content in the highest possible resolution.** Your [HLS](https://developer.apple.com/documentation/http_live_streaming) (HTTP Live Streaming) playlist should include the full range of available resolutions so that people can experience your content in the resolution that's appropriate for the device they're using (AVFoundation automatically selects the resolution based on the device). If you don't include a range of resolutions, your content will look low quality when people stream it to a device that can play at higher resolutions. For example, content that looks great on iPhone at 720p will look low quality when people use AirPlay to stream it to a 4K TV.
> 사용자가 사용 중인 장치에 적합한 해상도로 콘텐츠를 경험할 수 있도록 HLS(HTTP Live Streaming) 재생 목록에 사용 가능한 전체 해상도가 포함되어 있어야 합니다(AV Foundation은 장치에 따라 자동으로 해상도를 선택합니다). 해상도 범위를 포함하지 않으면 사람들이 콘텐츠를 더 높은 해상도로 재생할 수 있는 장치로 스트리밍할 때 콘텐츠 품질이 낮아 보입니다. 예를 들어, 720p의 아이폰에서 멋지게 보이는 콘텐츠는 사람들이 4K TV로 스트리밍하기 위해 에어플레이를 사용할 때 낮은 품질로 보일 것이다.
>




# **Entering AirPlay**

**Provide an intuitive way to enter AirPlay.** Clearly display the control for entering AirPlay within your custom player UI.
> 직관적으로 AirPlay에 들어갈 수 있는 방법을 제공합니다. 사용자 지정 플레이어 UI 내에서 AirPlay에 들어갈 수 있는 컨트롤을 명확하게 표시합니다.
>




**Use Apple-provided icons on controls that initiate AirPlay.** When you use the system-provided media player, the correct AirPlay icon displays automatically. If necessary, you can adjust the size and tint of the icon to match the appearance of your app. For developer guidance, see [AVRoutePickerView](https://developer.apple.com/documentation/avkit/avroutepickerview) and [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview).
> AirPlay를 시작하는 컨트롤에서 Apple 제공 아이콘을 사용합니다. 시스템 제공 미디어 플레이어를 사용하면 올바른 AirPlay 아이콘이 자동으로 표시됩니다. 필요한 경우 앱 모양에 맞게 아이콘의 크기와 색조를 조정할 수 있습니다. 개발자 지침은 AVRoutePickerView 및 MPVolumeView를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Video_Transparent.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Video_Transparent.svg)

AirPlay video

![https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Black_Transparent.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Black_Transparent.svg)

AirPlay audio

**Position the AirPlay icon correctly.** In a custom player, match the icon positions used in the system-provided media player. Specifically, display the AirPlay icon in the lower left corner when the device is in portrait orientation and in the lower right corner when the device is in landscape orientation.
> AirPlay 아이콘을 올바르게 배치합니다. 사용자 지정 플레이어에서 시스템 제공 미디어 플레이어에 사용된 아이콘 위치를 일치시킵니다. 특히 장치가 세로 방향일 때는 왼쪽 아래에, 가로 방향일 때는 오른쪽 아래에 AirPlay 아이콘을 표시합니다.
>




**Don't hide the AirPlay icon in a submenu or require people to use a control to see it.** If your app includes a control for initiating AirPlay, the system-provided icon should be visible on the control. Also, make sure the AirPlay icon is visible within the player UI.
> 하위 메뉴에서 AirPlay 아이콘을 숨기거나 사용자가 컨트롤을 사용하여 볼 수 있도록 하지 마십시오. 앱에 AirPlay를 시작하는 컨트롤이 포함되어 있으면 시스템에서 제공한 아이콘이 컨트롤에 표시되어야 합니다. 또한 플레이어 UI 내에 AirPlay 아이콘이 표시되는지 확인합니다.
>




**Ensure that custom controls for entering AirPlay are intuitive and behave as people expect.**Strive to match the appearance and behavior of the system-provided buttons, including distinct visual states that indicate when playback has been initiated, is occurring, or is unavailable.
> AirPlay에 들어가기 위한 사용자 지정 컨트롤이 직관적이고 사람들이 기대하는 대로 작동하는지 확인합니다.재생이 시작되었거나, 발생 중이거나, 사용할 수 없는 때를 나타내는 고유한 시각적 상태를 포함하여 시스템 제공 버튼의 모양과 동작을 일치시키도록 노력합니다.
>




# **During Playback**

**Support remote control events.** When you support remote control events, people can choose actions like play, pause, and fast forward on the lock screen, and through interaction with Siri or HomePod. For developer guidance, see [Remote Command Center Events](https://developer.apple.com/documentation/mediaplayer/remote_command_center_events).
> 원격 제어 이벤트를 지원합니다. 원격 제어 이벤트를 지원할 때 사용자는 잠금 화면에서 재생, 일시 중지 및 빠른 전달과 같은 작업을 선택할 수 있으며, 시리 또는 홈팟과 상호 작용할 수 있습니다. 개발자 지침은 원격 명령 센터 이벤트를 참조하십시오.
>




**Don't stop playback when your app enters the background or when the device locks.** For example, people expect the TV show they started streaming from your app to continue while they check their mail or put their device to sleep. In this type of scenario, it's also crucial to avoid mirroring, because people don't want to stream other types of content without explicitly choosing to do so.
> 예를 들어 앱에서 스트리밍하기 시작한 TV 프로그램이 메일을 확인하거나 단말기를 절전 모드로 전환하는 동안 계속될 것으로 예상합니다. 이러한 유형의 시나리오에서는 사람들이 명시적으로 선택하지 않고 다른 유형의 콘텐츠를 스트리밍하고 싶어하지 않기 때문에 미러링을 피하는 것도 중요합니다.
>




**Don't interrupt another app's playback unless your app is starting to play immersive media.**Although people can choose to play all new content, your app should not interrupt current playback by default. For example, if your app plays a video when it launches or auto-plays inline videos, you should play this content on only the local device, while allowing current playback to continue. For developer guidance, see [AVAudioSessionCategoryAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryambient?language=objc).
> 앱이 몰입형 미디어를 재생하기 시작하지 않는 한 다른 앱의 재생을 중단하지 마십시오.사용자가 모든 새 콘텐츠를 재생하도록 선택할 수 있지만 기본적으로 현재 재생을 중단하면 안 됩니다. 예를 들어 프로그램이 인라인 비디오를 시작하거나 자동으로 재생할 때 비디오를 재생하는 경우 로컬 장치에서만 이 콘텐츠를 재생하고 현재 재생은 계속할 수 있도록 해야 합니다. 개발자 지침은 AVAudio Session Category Ambient를 참조하십시오.
>




**Provide an interface for controlling media playback.** Your app should give people controls for performing common tasks during playback, like pause, play, skip, scrub, and exit. By default, the system-provided media player displays a screen that includes standard controls, and indicates playback is occurring on another device.
> 미디어 재생을 제어할 수 있는 인터페이스를 제공합니다. 사용자의 앱은 일시 중지, 재생, 건너뛰기, 스크럽 및 종료와 같은 재생 중에 일반적인 작업을 수행할 수 있는 컨트롤을 제공해야 합니다. 기본적으로 시스템에서 제공하는 미디어 플레이어는 표준 컨트롤이 포함된 화면을 표시하며 다른 장치에서 재생 중임을 나타냅니다.
>




**Let people use other parts of your app during playback.** When AirPlay is active, your app should still be functional. If the user navigates away from the playback screen, make sure other in-app videos don't begin playing and interrupt the streaming content.
> 재생 중에 다른 사용자가 앱의 다른 부분을 사용할 수 있도록 합니다. AirPlay가 활성화되어 있어도 앱은 계속 작동합니다. 사용자가 재생 화면에서 멀어지면 다른 앱 내 비디오가 재생을 시작하지 않고 스트리밍 콘텐츠를 중단하지 않도록 합니다.
>




**Stream only expected content.** Disable streaming of content like background loops and short video experiences that make sense only within the context of the app itself. For developer guidance, see [usesExternalPlaybackWhileExternalScreenIsActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624255-usesexternalplaybackwhileexterna).
> 예상 콘텐츠만 스트리밍합니다. 백그라운드 루프 및 짧은 비디오 경험과 같은 콘텐츠의 스트리밍을 앱 자체의 컨텍스트 내에서만 사용할 수 있습니다. 개발자 지침은 용도를 참조외부 재생외부 화면이 활성화되어 있는 동안.
>




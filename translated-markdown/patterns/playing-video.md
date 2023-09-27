# **[patterns] playing-video**

# People expect to enjoy rich video experiences on their devices, regardless of the app or game they're using.
> 사람들은 그들이 사용하는 앱이나 게임에 상관없이 그들의 기기에서 풍부한 비디오 경험을 즐기기를 기대한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-video-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-video-intro-dark_2x.png)

The system provides video players designed for you to use to embed playback experiences within your app or game in iOS, iPadOS, macOS, and tvOS. You can also offer your content through the TV app in these platforms, which gives people a convenient and consistent viewing experience.
> 이 시스템은 iOS, iPadOS, macOS 및 tvOS의 앱 또는 게임 내에 재생 경험을 내장하는 데 사용할 수 있도록 설계된 비디오 플레이어를 제공합니다. 또한 이러한 플랫폼에서 TV 앱을 통해 콘텐츠를 제공할 수 있어 사람들에게 편리하고 일관된 시청 경험을 제공한다.
>




The system-provided video players support different aspect-ratio playback modes and a picture-in-picture (PiP) viewing mode. Although people can switch modes during playback, by default, the system selects one of the following playback modes based on a video's aspect ratio:
> 시스템에서 제공하는 비디오 플레이어는 다양한 종횡비 재생 모드와 PiP(Picture-in-Picture) 보기 모드를 지원합니다. 재생 중에 모드를 전환할 수 있지만 기본적으로 시스템은 비디오의 가로 세로 비율을 기준으로 다음 재생 모드 중 하나를 선택합니다.
>




- In full-screen — or *aspect-fill* — mode, the video scales to fill the display, and some edge cropping may occur. This mode is the default for wide video (2:1 through 2.40:1). For developer guidance, see [resizeAspectFill](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/1385607-resizeaspectfill).
- >  전체 화면(또는 가로 세로 채우기) 모드에서는 비디오가 디스플레이를 채우도록 조정되고 일부 가장자리가 잘릴 수 있습니다. 이 모드는 와이드 비디오(2:1 ~ 2.40:1)의 기본값입니다. 개발자 지침은 AspectFill 크기 조정을 참조하십시오.

- In fit-to-screen — or *aspect* — mode, the entire video is visible onscreen, and letterboxing or pillarboxing occurs as needed. This mode is the default for standard video (4:3, 16:9, and anything up to 2:1) and ultrawide video (anything above 2.40:1). For developer guidance, see [resizeAspect](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/1387116-resizeaspect).
- >  화면에 맞춤(또는 가로 세로) 모드에서는 전체 비디오를 화면에 볼 수 있으며 필요에 따라 편지함 또는 필러박스가 발생합니다. 이 모드는 표준 비디오(4:3, 16:9, 최대 2:1) 및 울트라와이드 비디오(2.40:1 이상)의 기본 모드입니다. 개발자 지침은 측면 크기 조정을 참조하십시오.


In tvOS, the built-in video player also provides *transport bar controls,* which let people perform playback tasks, like turning on subtitles or changing the audio language, and actions, like adding a show to a library or favoriting a clip. Below the transport bar, the video player displays *content tabs*, like Info, Episodes, or Chapters, that can provide supporting information and help streamline navigation.
> tvOS에서 내장된 비디오 플레이어는 또한 전송 바 컨트롤을 제공하여 사람들이 자막을 켜거나 오디오 언어를 변경하는 것과 같은 재생 작업과 라이브러리에 프로그램을 추가하거나 클립을 즐겨찾는 것과 같은 작업을 수행할 수 있게 합니다. 비디오 플레이어는 전송 표시줄 아래에 정보, 에피소드 또는 장과 같은 내용 탭을 표시하여 지원 정보를 제공하고 탐색을 간소화할 수 있습니다.
>




# **Best practices**

**Use the system video player to give people a familiar and convenient experience.** The built-in video player provides an exceptional video playback experience that offers consistent interactions and behaviors that let people focus on enjoying immersive content. If your app truly requires a custom video player, reference the behavior and interface of the system video player to help you provide an experience that people can instantly understand. A custom experience that diverges slightly from the system-provided experience can cause frustration because people can rely on some of their habitual interactions, but not all of them.
> 시스템 비디오 플레이어를 사용하여 사람들에게 친숙하고 편리한 경험을 제공합니다. 내장된 비디오 플레이어는 사람들이 몰입형 콘텐츠를 즐기는 데 집중할 수 있도록 일관된 상호 작용과 동작을 제공하는 탁월한 비디오 재생 경험을 제공합니다. 앱에 사용자 지정 비디오 플레이어가 정말로 필요한 경우 시스템 비디오 플레이어의 동작과 인터페이스를 참조하여 사용자가 즉시 이해할 수 있는 환경을 제공하십시오. 시스템이 제공하는 경험과 약간 다른 맞춤형 경험은 사람들이 그들의 습관적인 상호작용 중 일부에 의존할 수 있지만, 그들 전부는 아니기 때문에 좌절감을 유발할 수 있다.
>




**Always display video content at its original aspect ratio.** When video content uses embedded letterbox or pillarbox padding to conform to a specific aspect ratio, the system may be unable to correctly scale the video based on the current playback mode. Padding embedded within the video frame can cause videos to appear smaller in both full-screen and fit-to-screen modes. It also prevents videos from displaying correctly in edge-to-edge, non-full-screen contexts, like [Picture in Picture](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/#multitasking-on-ipad) mode on iPad.
> 비디오 콘텐츠를 항상 원래 가로 세로 비율로 표시합니다. 비디오 콘텐츠가 특정 가로 세로 비율을 준수하기 위해 내장된 편지함 또는 기둥 상자 패딩을 사용하는 경우 시스템이 현재 재생 모드에 따라 비디오 크기를 올바르게 조정하지 못할 수 있습니다. 비디오 프레임에 내장된 패딩으로 인해 전체 화면 모드와 화면 크기에 맞게 모드에서 비디오가 더 작게 나타날 수 있습니다. 또한 iPad의 Picture in Picture 모드와 같이 전체 화면이 아닌 에지 투 에지 컨텍스트에서 비디오가 올바르게 표시되지 않도록 합니다.
>




Here are some examples that show how padding can affect video display on iPhone Xs.
> 패딩이 아이폰Xs의 비디오 디스플레이에 어떤 영향을 미칠 수 있는지를 보여주는 몇 가지 예가 있다.
>




• [Result of padding a 4:3 video](../patterns/playing-video#)
> • 4:3 동영상 패딩 결과
>



• [Result of padding a 21:9 video](../patterns/playing-video#)
> • 21:9 동영상 패딩 결과
>




-

![https://developer.apple.com/design/human-interface-guidelines/patterns/playing-video/images/video-fill-4-3-right.svg](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-video/images/video-fill-4-3-right.svg)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

4:3 video in full-screen viewing mode
> 전체 화면 보기 모드에서 4:3 비디오
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/playing-video/images/video-fill-4-3-wrong.svg](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-video/images/video-fill-4-3-wrong.svg)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

4:3 video with embedded padding, in full-screen viewing mode
> 전체 화면 보기 모드에서 내장 패딩 포함 4:3 비디오
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/playing-video/images/legend-letter-pillar.svg](https://developer.apple.com/design/human-interface-guidelines/patterns/playing-video/images/legend-letter-pillar.svg)


**Provide additional information when it adds value.** In iOS, iPadOS, and tvOS, you can customize a video’s additional information by providing an image, title, description, and other useful information. In general, restrict this content so that it doesn’t obscure media playback. For developer guidance, see [externalMetadata](https://developer.apple.com/documentation/avfoundation/avplayeritem/1627623-externalmetadata).
> 가치가 추가되면 추가 정보를 제공합니다. iOS, iPadOS 및 tvOS에서는 이미지, 제목, 설명 및 기타 유용한 정보를 제공하여 비디오의 추가 정보를 사용자 지정할 수 있습니다. 일반적으로 미디어 재생을 방해하지 않도록 이 콘텐츠를 제한합니다. 개발자 지침은 외부 메타데이터를 참조하십시오.
>




**Enable the interactions people expect, regardless of the device they’re using to control playback.** For example, people expect to press Space on a connected keyboard to play or pause media playback on Mac, iPhone, iPad, and Apple TV. Similarly, people expect to move through their media on Apple TV by making familiar, intuitive gestures with the Siri Remote. For guidance, see Keyboards and Remotes.
> 재생을 제어하는 데 사용하는 장치에 관계없이 사용자가 기대하는 상호 작용을 활성화합니다. 예를 들어, 사람들은 Mac, iPhone, iPad 및 Apple TV에서 미디어 재생을 재생하거나 일시 중지하기 위해 연결된 키보드의 Space를 누릅니다. 비슷하게, 사람들은 시리 리모컨으로 친숙하고 직관적인 제스처를 취함으로써 애플 TV에서 그들의 미디어를 통해 이동할 것으로 기대한다. 자세한 내용은 키보드 및 원격을 참조하십시오.
>




**If people need to access playback options or content-specific information in your tvOS app, consider adding a transport control or a custom content tab.** People typically open a transport control or content tab while they're watching a video, so it's essential to provide only the most useful actions and information. Help people return quickly to the viewing experience by making sure your actions don't take more than a step or two and your content is succinct. Use a transport control to enable a playback-related action like favoriting a video; use custom content tabs to display supplementary information or recommendations.
> 다른 사용자가 tvOS 앱에서 재생 옵션이나 콘텐츠 관련 정보에 액세스해야 하는 경우 전송 컨트롤 또는 사용자 지정 콘텐츠 탭을 추가하는 것을 고려해 보십시오. 일반적으로 동영상을 보는 동안 전송 컨트롤 또는 콘텐츠 탭을 열므로 가장 유용한 작업 및 정보만 제공해야 합니다. 작업이 한두 단계 이상 진행되지 않고 내용이 간결하게 표시되도록 하여 사람들이 빠르게 보기 환경으로 돌아갈 수 있도록 지원합니다. 전송 컨트롤을 사용하여 비디오 즐겨찾기와 같은 재생 관련 작업을 활성화하고 사용자 정의 컨텐츠 탭을 사용하여 보충 정보 또는 권장 사항을 표시합니다.
>




**Avoid allowing audio from different sources to mix as viewers switch between full-screen and PiP modes.** Mixed audio is an unpleasant and frustrating user experience. In general, audio mixes when at least one of the audio sources fails to handle secondary audio correctly. Here is a typical scenario: While watching a full-screen video, the viewer moves it into the PiP window, where the system automatically mutes the video. In the full-screen window, the viewer starts a game that plays background music, then switches to the PiP window and unmutes the video. If the game doesn't handle secondary audio appropriately, its audio mixes with the audio from the unmuted video. For developer guidance, see [silenceSecondaryAudioHintNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616622-silencesecondaryaudiohintnotific).
> 뷰어가 전체 화면 모드와 PiP 모드 사이를 전환할 때 서로 다른 소스의 오디오가 섞이지 않도록 합니다. 혼합 오디오는 불쾌하고 답답한 사용자 경험이다. 일반적으로 오디오 소스 중 적어도 하나가 보조 오디오를 올바르게 처리하지 못할 때 오디오가 혼합됩니다. 다음은 일반적인 시나리오입니다. 전체 화면 비디오를 보는 동안 뷰어는 비디오를 자동으로 음소거하는 PiP 창으로 이동합니다. 전체 화면 창에서 뷰어는 배경 음악을 재생하는 게임을 시작한 다음 PiP 창으로 전환하고 비디오 음소거를 해제합니다. 게임이 보조 오디오를 적절하게 처리하지 못하면 해당 오디오는 음소거되지 않은 비디오의 오디오와 혼합됩니다. 개발자 지침은 silenceSecondary를 참조하십시오.오디오 힌트 알림.
>




# **Integrating with the TV app**
> TV 앱과의 통합
>




The TV app provides global access to favorite, recently played, and recommended video content from across the system. When people initiate content playback within your app, the TV app automatically opens your app and transitions to it. Follow these guidelines to help the TV app experience feel like an integrated part of your app.
> TV 앱은 시스템 전체에서 즐겨찾기, 최근 재생 및 추천 비디오 콘텐츠에 대한 글로벌 액세스를 제공합니다. 다른 사람이 앱 내에서 콘텐츠 재생을 시작하면 TV 앱이 자동으로 앱을 열고 앱으로 전환합니다. TV 앱 경험이 앱의 통합된 부분처럼 느껴지도록 하려면 다음 지침을 따르십시오.
>




**Ensure a smooth transition to your app.** The TV app fades to black when transitioning to your app and doesn’t show your app’s launch screen. Maintain visual continuity with this transition by immediately presenting your own black screen before starting to play or resume content.
> 앱으로 원활하게 전환하십시오. TV 앱은 앱으로 전환하면 검은색으로 바래고 앱의 실행 화면이 표시되지 않습니다. 콘텐츠를 재생하거나 다시 시작하기 전에 즉시 검은색 화면을 표시하여 이 전환에서 시각적 연속성을 유지합니다.
>




**Show the expected content immediately.** People expect the content they choose to begin playing as soon as the transition to your app completes, especially when resuming playback. Jump right from your app’s black screen into content, and avoid displaying splash screens, detail screens, intro animations, or any other barriers that make it take longer to reach content. In rare situations where you must display an interstitial element before the selected media plays, people can choose Select to step through the element, or choose Play if they want to skip the interstitial content and start playback.
> 예상되는 내용을 즉시 표시합니다. 사람들은 특히 재생을 재개할 때 앱으로의 전환이 완료되는 즉시 선택한 콘텐츠가 재생을 시작하기를 기대합니다. 앱의 검은색 화면에서 콘텐츠로 바로 이동할 수 있으며, 콘텐츠에 도달하는 데 더 오래 걸리는 스플래시 화면, 세부 화면, 소개 애니메이션 또는 기타 장벽을 표시하지 않도록 합니다. 선택한 미디어를 재생하기 전에 중간 요소를 표시해야 하는 드문 경우지만, 사용자가 중간 내용을 건너뛰고 재생을 시작하려면 [선택]을 선택하거나 [재생]을 선택할 수 있습니다.
>




**Avoid asking people if they want to resume playback.** If playback can be resumed, do so automatically without prompting for confirmation.
> 재생을 다시 시작할지 묻는 메시지를 표시하지 않습니다. 재생을 재개할 수 있는 경우 확인 메시지를 표시하지 않고 자동으로 재생을 재개합니다.
>




**Play or pause playback when people press Space on a connected Bluetooth keyboard.** Pressing Space to control media playback is an interaction people expect, regardless of the keyboard they’re using.
> 연결된 Bluetooth 키보드에서 사용자가 Space를 누를 때 재생을 재생하거나 일시 중지합니다. 미디어 재생을 제어하기 위해 공간을 누르는 것은 사용 중인 키보드에 관계없이 사람들이 기대하는 상호 작용입니다.
>




**Make sure content plays for the correct viewer.** If your app supports multiple user profiles, the TV app can specify a profile when issuing a playback request. Make your app automatically switch to this profile before starting playback. If a playback request doesn’t specify a profile, ask the viewer to choose one before playback begins so this information can be provided in the future.
> 콘텐츠가 올바른 뷰어에 대해 재생되는지 확인합니다. 프로그램이 여러 사용자 프로필을 지원하는 경우 TV 앱은 재생 요청을 실행할 때 프로필을 지정할 수 있습니다. 재생을 시작하기 전에 앱이 자동으로 이 프로필로 전환되도록 하십시오. 재생 요청에 프로필이 지정되지 않은 경우 나중에 이 정보를 제공할 수 있도록 재생이 시작되기 전에 프로필을 선택하도록 뷰어에 요청하십시오.
>




**Use the previous end time when resuming playback of a long video clip.** Resuming playback at the previous stopping point lets people quickly continue where they left off.
> 긴 비디오 클립의 재생을 재개할 때 이전 종료 시간을 사용합니다. 이전 정지 지점에서 재생을 재개하면 사용자가 중단한 위치에서 빠르게 계속할 수 있습니다.
>




# **Loading content**

**Avoid displaying loading screens when possible.** A loading screen is unnecessary if your content loads quickly, but if loading takes more than 2 seconds, consider showing a black loading screen with a centered activity spinner and no surrounding content.
> 가능한 경우 로딩 화면을 표시하지 않도록 합니다. 콘텐츠가 빠르게 로드되는 경우에는 로드 화면이 필요하지 않지만 로드하는 데 2초 이상 걸리는 경우에는 검은색 로드 화면을 중앙에 두고 주변 콘텐츠가 없는 상태로 표시하는 것이 좋습니다.
>




**Start playback immediately.** If you must display a loading screen, display it only until enough content loads for playback to begin. Continue loading remaining content in the background.
> 재생을 즉시 시작합니다. 로드 화면을 표시해야 하는 경우 재생을 시작할 수 있을 만큼 콘텐츠가 로드될 때까지 표시하십시오. 백그라운드에서 나머지 콘텐츠를 계속 로드합니다.
>




**Minimize loading screen content.** If you include branding or images on your loading screen, do so minimally while maintaining the black background that enables a seamless transition to playback.
> 화면 내용 로드 최소화. 로드 화면에 브랜딩 또는 이미지를 포함할 경우 재생으로 원활하게 전환할 수 있도록 검은색 배경을 유지한 채 최소한의 작업을 수행하십시오.
>




# **Exiting playback**

After exiting playback, people remain in your app rather than returning to the TV app, so it’s a good idea to help people avoid becoming disoriented.
> 재생을 종료한 후에도 사람들은 TV 앱으로 돌아가지 않고 앱에 남아 있으므로 사람들이 혼란스러워하는 것을 방지하는 것이 좋습니다.
>




**Show a contextually relevant screen.** When exiting playback, display a detail screen for the content the viewer was just watching and include an option to resume playback. If a detail screen isn’t available, show either a menu that lists this content or your app’s main menu.
> 상황에 맞는 화면을 표시합니다. 재생을 종료할 때 뷰어가 방금 보고 있던 콘텐츠에 대한 세부 화면을 표시하고 재생을 재개하는 옵션을 포함합니다. 세부 정보 화면을 사용할 수 없는 경우 이 콘텐츠를 나열하는 메뉴 또는 앱의 기본 메뉴를 표시합니다.
>




**Be prepared for an immediate exit.** Prepare an exit screen as soon as possible after receiving a playback notification so you’re ready to display the screen if people exit immediately after playback begins.
> 즉시 출구에 대비하십시오. 재생 알림을 받은 후 가능한 한 빨리 종료 화면을 준비하여 재생이 시작된 후 즉시 종료할 수 있도록 합니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or macOS.*
> iOS, iPadOS 또는 macOS에 대한 추가 고려 사항은 없습니다.
>




# **tvOS**

**Defer to content when displaying logos or noninteractive overlays above video.** A small, unobtrusive logo or countdown timer may be appropriate for your video, but avoid large, distracting overlays that don’t enhance the viewing experience. Also, be aware that some devices are prone to image retention, so it’s generally better to keep overlays short and to prefer translucent graphics in Standard Dynamic Range (SDR) to bright, opaque content.
> 비디오 위에 로고 또는 비인터랙티브 오버레이를 표시할 때 내용에 따라 연기합니다. 눈에 띄지 않는 작은 로고 또는 카운트다운 타이머가 비디오에 적합할 수 있지만 보기 환경을 향상시키지 않는 큰 오버레이는 피합니다. 또한 일부 장치는 이미지 보존이 쉽기 때문에 일반적으로 오버레이를 짧게 유지하고 밝은 불투명 콘텐츠보다는 SDR(표준 동적 범위)의 반투명 그래픽을 선호하는 것이 좋습니다.
>




**Show interactive overlays gracefully.** Some videos display interactive overlays, such as quizzes, surveys, and progress check-ins. For the best user experience, implement a minimum delay of 0.5 seconds to pause playing media, and display an interactive overlay. Give people a clear way to dismiss the overlay and resume media playback after they finish interacting.
> 대화형 오버레이를 우아하게 표시합니다. 일부 비디오는 퀴즈, 설문조사 및 진행률 체크인과 같은 대화형 오버레이를 표시합니다. 최상의 사용자 환경을 위해 재생 중인 미디어를 일시 중지하고 대화형 오버레이를 표시하는 데 최소 0.5초의 지연을 구현합니다. 사용자가 상호 작용을 마친 후 오버레이를 해제하고 미디어 재생을 재개할 수 있는 명확한 방법을 제공합니다.
>




# **watchOS**

In watchOS, the system manages video playback. Apps can play short video clips while the app is active and running in the foreground. You can use a movie element to embed clips in your interface and play video inline, or you can play a clip in a separate interface. For developer guidance, see [VideoPlayer](https://developer.apple.com/documentation/avkit/videoplayer).
> watch OS에서 시스템은 비디오 재생을 관리합니다. 앱이 활성화되고 포그라운드에서 실행되는 동안 앱은 짧은 비디오 클립을 재생할 수 있습니다. 동영상 요소를 사용하여 인터페이스에 클립을 내장하고 비디오를 인라인으로 재생하거나 별도의 인터페이스에서 클립을 재생할 수 있습니다. 개발자 지침은 비디오 플레이어를 참조하십시오.
>




**Keep video clips short.** Prefer shorter clips of no longer than 30 seconds. Long clips consume more disk space and require people to keep their wrists raised for longer periods of time, which can cause fatigue.
> 비디오 클립을 짧게 유지합니다. 30초 이하의 짧은 클립을 선호합니다. 긴 클립은 더 많은 디스크 공간을 소비하고 사람들이 더 오랜 시간 동안 손목을 들어 올려야 하므로 피로를 유발할 수 있다.
>




**Use the recommended sizes and encoding values for media assets.** In particular, avoid scaling video clips, which affects performance and results in a suboptimal appearance. The following table lists the recommended encoding and resolution values for video assets. The audio encoding values apply to both movies and audio-only assets.
> 미디어 자산에 권장되는 크기 및 인코딩 값을 사용합니다. 특히 비디오 클립의 크기가 조정되지 않도록 하여 성능에 영향을 미치고 차선의 외관을 초래합니다. 다음 표에는 비디오 자산에 권장되는 인코딩 및 해상도 값이 나열되어 있습니다. 오디오 인코딩 값은 동영상과 오디오 전용 자산에 모두 적용됩니다.
>




**Avoid creating a poster image that looks like a system control.** You want people to understand that they can tap a movie element for playback; you don’t want to confuse people by making movie elements look like something else.
> 시스템 컨트롤처럼 보이는 포스터 이미지를 만들지 마십시오. 재생을 위해 동영상 요소를 누를 수 있다는 것을 사람들이 이해하기를 원하지만 동영상 요소를 다른 것처럼 만들어 사람들을 혼란스럽게 만들고 싶지 않습니다.
>




**Consider creating a poster image that represents a video clip’s contents.** When people tap a poster image, the system replaces the image with the video and begins inline playback. A relevant poster image can help people make an informed decision about whether to view the video. In general, avoid creating a poster image that has nothing to do with the content or that people might mistake for a control.
> 비디오 클립의 내용을 나타내는 포스터 이미지를 만드는 것을 고려해보세요. 사람들이 포스터 이미지를 누르면 시스템이 이미지를 비디오로 교체하고 인라인 재생을 시작합니다. 관련 포스터 이미지는 사람들이 비디오를 볼지 여부에 대해 정보에 입각한 결정을 내리는 데 도움이 될 수 있다. 일반적으로 내용과 관련이 없거나 사용자가 컨트롤로 착각할 수 있는 포스터 이미지를 만들지 마십시오.
>




| Attribute | Value |
| --- | --- |
| Video codec | H.264 High Profile |
| Video bit rate | 160 kbps at up to 30 fps |
| Resolution (full screen) | 208px × 260px (portrait orientation) |
| Resolution (16:9) | 320px × 180px (landscape orientation) |
| Audio | 64 kbps HE-AAC |

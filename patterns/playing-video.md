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





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



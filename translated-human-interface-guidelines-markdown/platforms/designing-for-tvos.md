### [[Platforms](./translated-human-interface-guidelines-markdown/platforms.md)]  
  
# **Designing for tvOS**  

=====================



People enjoy the vibrant content, immersive experiences, and streamlined interactions that tvOS delivers in media and games, as well as in fitness, education, and home utility apps.  

> 사람들은 피트니스, 교육 및 홈 유틸리티 앱뿐만 아니라 미디어 및 게임에서 TVOS가 제공하는 생생한 콘텐츠, 몰입형 경험 및 간소화된 상호 작용을 즐긴다.
>

![A stylized representation of a TV screen shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/cd98e6ef7baa3ddd91de67f43a979c8e/platforms-tvOS-intro@2x.png)



As you begin designing your app or game for tvOS, start by understanding the following fundamental device characteristics and patterns that distinguish the tvOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that tvOS users appreciate.  

> 당신이 당신의 앱이나 게임을 tvOS용으로 디자인하기 시작할 때, tvOS 경험을 구별하는 다음의 기본적인 장치 특성과 패턴을 이해하는 것으로 시작하세요. 이러한 특성과 패턴을 사용하여 디자인 결정을 알려주면 TVOS 사용자가 좋아하는 앱이나 게임을 제공하는 데 도움이 될 수 있습니다.
>





**Display.** A TV typically has a very large, high-resolution display.  

> **표시.** TV는 일반적으로 매우 큰 고해상도 디스플레이를 가지고 있다.
>





**Ergonomics.** Although people generally remain many feet away from their stationary TV — often 8 feet or more — they sometimes continue to interact with content as they move around the room.  

> **경제학.** 사람들은 일반적으로 고정된 TV로부터 수 피트(대개 8피트 이상) 떨어진 곳에 있지만, 때때로 방을 이동하면서 콘텐츠와 계속 상호 작용합니다.
>





**Inputs.** People can use a   

> **입력.** 사용자는 다음을 사용할 수 있습니다
>

[remote](https://developer.apple.com/design/human-interface-guidelines/remotes)

, a   

[game controller](https://developer.apple.com/design/human-interface-guidelines/game-controllers)

, their   

[voice](https://developer.apple.com/design/human-interface-guidelines/siri)

, and apps running on their other devices to interact with Apple TV.  

> , 그리고 애플 TV와 상호 작용하기 위해 다른 장치에서 실행되는 앱.
>





**App interactions.** People can get deeply immersed in a single experience — often lasting hours — but they also appreciate using a picture-in-picture view to simultaneously follow an alternative app or video.  

> **앱 상호 작용.** 사람들은 한 번의 경험(종종 몇 시간)에 깊이 빠져들 수 있지만, 사진 보기를 사용하여 다른 앱이나 비디오를 동시에 팔로우하는 것도 감사하게 생각합니다.
>





**System features.** Apple TV users expect their apps and games to integrate well with the following system experiences.  

> **시스템 기능.** 애플 TV 사용자들은 자신들의 앱과 게임이 다음과 같은 시스템 경험과 잘 통합되기를 기대한다.
>





* [Integrating with the TV app](/design/human-interface-guidelines/playing-video#Integrating-with-the-TV-app)

> * [TV앱과 연동] (/디자인/휴먼인터페이스-가이드라인/재생비디오#TV 앱과 통합)
>

* [SharePlay](/design/human-interface-guidelines/shareplay)

* [Top Shelf](/design/human-interface-guidelines/top-shelf)

* [TV provider accounts](/design/human-interface-guidelines/managing-accounts#TV-provider-accounts)



[Best practices](/design/human-interface-guidelines/designing-for-tvos#Best-practices)

--------------------------------------------------------------------------------------



Great tvOS experiences integrate the platform and device capabilities that people value most. To help your experience feel at home in tvOS, prioritize the following ways to incorporate these features and capabilities.  

> 훌륭한 TVOS 경험은 사람들이 가장 중요하게 여기는 플랫폼과 장치 기능을 통합한다. TV OS에서 편안한 경험을 할 수 있도록 다음과 같은 기능을 통합하는 방법에 우선 순위를 지정하십시오.
>





* Support powerful, delightful interactions through the fluid, familiar gestures people make with the Siri Remote.

> * 사람들이 Siri 리모컨으로 하는 유동적이고 친숙한 제스처를 통해 강력하고 즐거운 상호 작용을 지원합니다.
>

* Embrace the tvOS focus system, letting it gently highlight and expand onscreen items as people move among them, helping them know what to do and where they are at all times.

> * TVOS 포커스 시스템을 사용하여 사람들이 이동할 때 화면 항목을 부드럽게 강조 표시하고 확장할 수 있으므로 항상 무엇을 해야 하는지, 어디에 있는지 알 수 있습니다.
>

* Deliver beautiful, edge-to-edge artwork, subtle and fluid animations, and engaging audio, wrapping people in a rich, cinematic experience that’s clear, legible, and captivating from across the room.

> * 아름답고 완벽한 예술 작품, 섬세하고 유동적인 애니메이션, 매력적인 오디오를 제공하여 사람들을 깨끗하고 읽기 쉽고 매혹적인 풍부한 영화적 경험으로 감싸줍니다.
>

* Enhance multiuser support by making sign-in easy and infrequent, handling shared sign-in, and automatically switching profiles when people change the current viewer.

> * 로그인을 쉽고 자주 사용하지 않고, 공유 로그인을 처리하고, 사용자가 현재 뷰어를 변경할 때 프로필을 자동으로 전환하여 다중 사용자 지원을 향상시킵니다.
>



[Resources](/design/human-interface-guidelines/designing-for-tvos#Resources)

----------------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/designing-for-tvos#Related)



[Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps)





#### [Developer documentation](/design/human-interface-guidelines/designing-for-tvos#Developer-documentation)



[Planning your tvOS app](https://developer.apple.com/tvos/planning/)





#### [Videos](/design/human-interface-guidelines/designing-for-tvos#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/119/53F0161E-DB14-4A7D-8A94-B76244201AB8/5102_wide_250x141_1x.jpg) Deliver a great playback experience on tvOS](https://developer.apple.com/videos/play/wwdc2021/10191)

[Change log](/design/human-interface-guidelines/designing-for-tvos#Change-log)

------------------------------------------------------------------------------

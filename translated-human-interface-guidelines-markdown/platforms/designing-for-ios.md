### [[Platforms](./translated-human-interface-guidelines-markdown/platforms.md)]  
  
# **Designing for iOS**  

====================



People depend on their iPhone to help them stay connected, play games, view media, accomplish tasks, and track personal data in any location and while on the go.  

> 사람들은 어디에서나 이동 중에도 연결을 유지하고, 게임을 하고, 미디어를 보고, 작업을 수행하고, 개인 데이터를 추적할 수 있도록 아이폰에 의존한다.
>

![A stylized representation of an iPhone frame shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/fcb6f603e6672e3443637efe652e5bdb/platforms-iOS-intro@2x.png)



As you begin designing your app or game for iOS, start by understanding the following fundamental device characteristics and patterns that distinguish the iOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPhone users appreciate.  

> iOS용 앱이나 게임을 디자인하기 시작하면서 iOS 경험을 구분하는 다음과 같은 기본적인 장치 특성과 패턴을 이해하는 것부터 시작하십시오. 이러한 특성과 패턴을 사용하여 디자인 결정을 알려주면 아이폰 사용자가 좋아하는 앱이나 게임을 제공하는 데 도움이 될 수 있습니다.
>





**Display.** iPhone has a medium-size, high-resolution display.  

> **표시.** 아이폰은 중간 크기의 고해상도 디스플레이를 가지고 있다.
>





**Ergonomics.** People generally hold their iPhone in one or both hands as they interact with it, switching between landscape and portrait orientations as needed. While people are interacting with the device, their viewing distance tends to be no more than a foot or two.  

> **경제학.** 사람들은 일반적으로 아이폰과 상호 작용할 때 한 손 또는 두 손으로 아이폰을 들고 필요에 따라 가로 방향과 세로 방향을 바꾼다. 사람들이 기기와 상호 작용하는 동안, 그들의 시야 거리는 1~2피트에 지나지 않는 경향이 있다.
>





**Inputs.** Multi-Touch   

[gestures](https://developer.apple.com/design/human-interface-guidelines/touchscreen-gestures)

,   

[onscreen keyboards](https://developer.apple.com/design/human-interface-guidelines/onscreen-keyboards)

, and   

[voice](https://developer.apple.com/design/human-interface-guidelines/siri)

 control let people perform actions and accomplish meaningful tasks while they’re on the go. In addition, people often want apps to use their   

> 제어를 통해 사람들은 이동 중에 행동을 수행하고 의미 있는 작업을 수행할 수 있습니다. 게다가, 사람들은 종종 그들의 앱을 사용하기를 원한다
>

[personal data](https://developer.apple.com/design/human-interface-guidelines/accessing-private-data)

 and input from the device’s   

> 그리고 장치의 입력
>

[gyroscope and accelerometer](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer)

, and they may also want to participate in   

> , 그리고 그들은 또한 참여하기를 원할지도 모른다
>

[spatial interactions](https://developer.apple.com/design/human-interface-guidelines/spatial-interactions)

.  





**App interactions.** Sometimes, people spend just a minute or two checking on event or social media updates, tracking data, or sending messages. At other times, people can spend an hour or more browsing the web, playing games, or enjoying media. People typically have multiple apps open at the same time, and they appreciate switching frequently among them.  

> **앱 상호 작용.** 때때로, 사람들은 이벤트나 소셜 미디어 업데이트를 확인하고, 데이터를 추적하거나, 메시지를 보내는 데 1~2분을 소비한다. 다른 때에는, 사람들은 웹을 탐색하고, 게임을 하거나, 미디어를 즐기는 데 한 시간 이상을 보낼 수 있다. 사람들은 일반적으로 여러 개의 앱을 동시에 열고, 그들은 그들 사이에서 자주 전환하는 것에 감사한다.
>





**System features.** iOS provides several features that help people interact with the system and their apps in familiar, consistent ways.  

> **시스템 기능.** iOS는 사람들이 친숙하고 일관된 방식으로 시스템과 앱과 상호 작용할 수 있도록 도와주는 몇 가지 기능을 제공한다.
>





* [Widgets](/design/human-interface-guidelines/widgets)

* [Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/home-screen-quick-actions)

> * [홈 화면 빠른 동작](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/home-screen-quick-actions)
>

* [Spotlight](https://developer.apple.com/design/human-interface-guidelines/searching)

* [Shortcuts](https://developer.apple.com/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)

* [Activity views](/design/human-interface-guidelines/activity-views)



[Best practices](/design/human-interface-guidelines/designing-for-ios#Best-practices)

-------------------------------------------------------------------------------------



Great iPhone experiences integrate the platform and device capabilities that people value most. To help your design feel at home in iOS, prioritize the following ways to incorporate these features and capabilities.  

> 훌륭한 아이폰 경험은 사람들이 가장 중요하게 여기는 플랫폼과 기기 기능을 통합한다. 디자인이 iOS에서 편안함을 느낄 수 있도록 다음과 같은 기능을 통합하는 방법의 우선순위를 정하십시오.
>





* Help people focus on primary tasks and content by limiting the number of onscreen controls while making secondary details and actions discoverable with minimal interaction.

> * 최소한의 상호 작용으로 보조 세부 정보와 작업을 검색할 수 있도록 하면서 화면 컨트롤의 수를 제한하여 사용자가 기본 작업 및 내용에 집중할 수 있도록 지원합니다.
>

* Adapt seamlessly to appearance changes — like device orientation, Dark Mode, and Dynamic Type — letting people choose the configurations that work best for them.

> * 장치 방향, 다크 모드 및 동적 유형과 같은 모양 변경에 원활하게 적응하여 사용자에게 가장 적합한 구성을 선택할 수 있습니다.
>

* Support interactions that accommodate the way people usually hold their device. For example, it tends to be easier and more comfortable for people to reach a control when it’s located in the middle or bottom area of the display, so it’s especially important let people swipe to navigate back or initiate actions in a list row.

> * 사람들이 일반적으로 장치를 잡는 방식을 수용하는 상호 작용을 지원합니다. 예를 들어 컨트롤이 디스플레이의 중간 또는 하단 영역에 있을 때 컨트롤에 도달하는 것이 더 쉽고 편리한 경향이 있으므로 사람들이 뒤로 이동하거나 목록 행에서 작업을 시작할 수 있도록 하는 것이 특히 중요합니다.
>

* With people’s permission, integrate information available through platform capabilities in ways that enhance the experience without asking people to enter data. For example, you might accept payments, provide security through biometric authentication, or offer features that use the device’s location.

> * 사용자의 허가를 받아 플랫폼 기능을 통해 사용 가능한 정보를 사용자에게 데이터 입력을 요청하지 않고 경험을 향상시키는 방식으로 통합합니다. 예를 들어 결제를 수락하거나 생체 인증을 통해 보안을 제공하거나 장치의 위치를 사용하는 기능을 제공할 수 있습니다.
>



[Resources](/design/human-interface-guidelines/designing-for-ios#Resources)

---------------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/designing-for-ios#Related)



[Apple Design Resources](https://developer.apple.com/design/resources/#ios-apps)





#### [Developer documentation](/design/human-interface-guidelines/designing-for-ios#Developer-documentation)



[Planning your iOS app](https://developer.apple.com/ios/planning/)





#### [Videos](/design/human-interface-guidelines/designing-for-ios#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/119/9CCE8A5D-A751-441C-B88F-FB91E2D1958E/4949_wide_250x141_1x.jpg) What's new in UIKit](https://developer.apple.com/videos/play/wwdc2021/10059)

[![](https://devimages-cdn.apple.com/wwdc-services/images/48/0F960683-D91F-4CA9-9658-6FBB11F0683D/3272_wide_250x141_1x.jpg) What's New in iOS Design](https://developer.apple.com/videos/play/wwdc2019/808)

------------------------------------------------------------------------------

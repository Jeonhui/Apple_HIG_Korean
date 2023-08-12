### [[Platforms](./translated-human-interface-guidelines-markdown/platforms.md)]  
  
# **Designing for watchOS**  

========================
As you begin designing your app for Apple Watch, start by understanding the following fundamental device characteristics and patterns that distinguish the watchOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app that Apple Watch users appreciate.  

> Apple Watch용 앱을 설계하기 시작할 때, 다음과 같은 기본적인 장치 특성과 시계를 구별하는 패턴을 이해하는 것으로 시작하십시오OS 경험. 이러한 특성과 패턴을 사용하여 디자인 결정 사항을 알려주면 애플워치 사용자가 인식하는 앱을 제공하는 데 도움이 될 수 있습니다.
>





**Display.** The small Apple Watch display fits on the wrist while delivering an easy-to-read, high-resolution experience.  

> **표시.** 작은 Apple Watch 디스플레이는 읽기 쉽고 고해상도의 경험을 제공하는 동시에 손목에 딱 맞습니다.
>





**Ergonomics.** Because people wear Apple Watch, they’re usually no more than a foot away from the display as they raise their wrist to view it and use their opposite hand to interact with the device. In addition, the Always On display lets people view information on the watch face when they drop their wrist.  

> **공학.** 사람들이 애플워치를 착용하기 때문에, 그들은 손목을 들어 그것을 보고 기기와 상호작용하기 위해 반대쪽 손을 사용할 때 보통 디스플레이로부터 1피트에 지나지 않는다. 게다가 Always On 디스플레이는 사람들이 손목을 떨어뜨렸을 때 시계 얼굴의 정보를 볼 수 있게 해줍니다.
>





**Inputs.** People can navigate vertically or inspect data by turning the   

> **입력.** 사람들은 수직으로 탐색하거나 데이터를 검사할 수 있다
>

[Digital Crown](/design/human-interface-guidelines/digital-crown)

, which offers consistent control on the watch face, the Home Screen, and within apps. They can provide input even while they’re in motion with standard   

> , 이것은 시계 면, 홈 스크린 및 앱 내에서 일관성 있는 제어를 제공합니다. 표준에 따라 움직이는 동안에도 입력을 제공할 수 있습니다
>

[touchscreen gestures](/design/human-interface-guidelines/touchscreen-gestures)

 like tap, swipe, and drag. Pressing the   

> 탭, 스와이프, 드래그처럼. 을 누르다
>

[Action button](/design/human-interface-guidelines/action-button)

 initiates an essential action without looking at the screen, and using   

> 화면을 보지 않고 필수 작업을 시작합니다
>

[shortcuts](/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)

 helps people perform their routine tasks quickly and easily. People can also take advantage of data that device features provide, such as GPS, sensors for blood oxygen and heart function, and the altimeter, accelerometer, and gyroscope.  

> 사람들이 일상적인 작업을 빠르고 쉽게 수행할 수 있도록 도와줍니다. 사람들은 또한 GPS, 혈액 산소 및 심장 기능을 위한 센서, 고도계, 가속도계 및 자이로스코프와 같은 장치 기능이 제공하는 데이터를 활용할 수 있다.
>





**App interactions.** People glance at the Always On display many times throughout the day, performing concise app interactions that can last for less than a minute each. People frequently use a watchOS app’s related experiences — like complications, notifications, and Siri interactions — more than they use the app itself.  

> **앱 상호작용.** 사람들은 하루 동안 Always On 디스플레이를 여러 번 보면서 각각 1분 미만의 간결한 앱 상호작용을 수행합니다. 사람들은 시계를 자주 사용한다복잡한 문제, 알림, 시리 상호 작용과 같은 OS 앱의 관련 경험은 앱 자체를 사용하는 것보다 더 많다.
>





**System features.** watchOS provides several features that help people interact with the system and their apps in familiar, consistent ways.  

> **시스템 기능.** 망을 보다OS는 사람들이 친숙하고 일관된 방식으로 시스템 및 앱과 상호 작용할 수 있도록 도와주는 몇 가지 기능을 제공한다.
>





* [Complications](/design/human-interface-guidelines/complications)

* [Notifications](/design/human-interface-guidelines/notifications)

* [Always On](/design/human-interface-guidelines/always-on)

* [Watch faces](/design/human-interface-guidelines/watch-faces)



[Best practices](/design/human-interface-guidelines/designing-for-watchos#Best-practices)

-----------------------------------------------------------------------------------------



Great Apple Watch experiences are focused, specialized, and integrate the platform and device capabilities that people value most. To help your experience feel at home in watchOS, prioritize the following ways to incorporate these features and capabilities.  

> 위대한 애플워치 경험은 사람들이 가장 중시하는 플랫폼과 기기 기능에 집중하고 전문화되며 통합된다. 시계 OS에서 편안한 경험을 할 수 있도록 다음과 같은 기능을 통합하는 방법을 우선시하십시오.
>





* Support quick, glanceable, single-screen interactions that deliver critical information succinctly and help people perform targeted actions with a simple gesture or two.

> * 중요한 정보를 간결하게 전달하는 빠르고 눈에 띄는 단일 화면 상호 작용을 지원하고 간단한 제스처로 대상 작업을 수행할 수 있도록 지원합니다.
>

* Minimize the depth of hierarchy in your app’s navigation, and use the   

> * 앱의 탐색에서 계층의 깊이를 최소화하고
>

[Digital Crown](/design/human-interface-guidelines/digital-crown)

 to provide vertical navigation for scrolling or switching between screens.

> 화면을 스크롤하거나 전환할 수 있는 수직 탐색 기능을 제공합니다.
>

* Personalize the experience by proactively anticipating people’s needs and using on-device data to provide actionable content that’s relevant in the moment or very soon.

> * 사용자의 요구를 사전에 예측하고 기기 내 데이터를 사용하여 현재 또는 곧 관련성이 있는 실행 가능한 콘텐츠를 제공함으로써 경험을 개인화할 수 있습니다.
>

* Use   

[complications](/design/human-interface-guidelines/complications)

 to provide relevant, potentially dynamic data and graphics right on the watch face where people can view them on every wrist raise and tap them to dive straight into your app.

> 사람들이 모든 손목을 들어 볼 수 있는 관련 잠재적으로 동적인 데이터와 그래픽을 워치 페이스에 바로 제공하고 앱에 바로 뛰어들 수 있도록 탭할 수 있습니다.
>

* Use   

[notifications](/design/human-interface-guidelines/notifications)

 to deliver timely, high-value information and let people perform important actions without opening your app.

> 적시에 높은 가치의 정보를 제공하고 사용자가 앱을 열지 않고도 중요한 작업을 수행할 수 있도록 합니다.
>

* Use background content such as   

> * 다음과 같은 배경 콘텐츠 사용
>

[color](/design/human-interface-guidelines/color)

 to convey useful supporting information, and use   

> 유용한 지원 정보를 전달하고 사용하다
>

[materials](/design/human-interface-guidelines/materials)

 to illustrate hierarchy and a sense of place.

> 계층과 장소감을 설명하기 위해.
>

* Support Siri to help people access shortcuts on the Siri watch face.

> * 사람들이 시리 워치 페이스의 바로 가기에 액세스할 수 있도록 시리를 지원합니다.
>

* Design your app to function independently, complementing your notifications and complications by providing additional details and functionality.

> * 추가 세부 정보와 기능을 제공하여 알림과 복잡성을 보완하면서 앱이 독립적으로 작동하도록 설계하십시오.
>



[Resources](/design/human-interface-guidelines/designing-for-watchos#Resources)

-------------------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/designing-for-watchos#Related)



[Apple Design Resources](https://developer.apple.com/design/resources/#watchos-apps)





#### [Developer documentation](/design/human-interface-guidelines/designing-for-watchos#Developer-documentation)



[Planning your watchOS app](https://developer.apple.com/watchos/planning/)





#### [Videos](/design/human-interface-guidelines/designing-for-watchos#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/69EC76C8-B751-49E6-9B2D-ED5A7D633A9D/8195_wide_250x141_1x.jpg) Design and build apps for watchOS 10](https://developer.apple.com/videos/play/wwdc2023/10138)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/56D03FE8-0566-429A-81D2-2F6566031498/8390_wide_250x141_1x.jpg) Design widgets for the Smart Stack on Apple Watch](https://developer.apple.com/videos/play/wwdc2023/10309)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/0A411518-17FD-4D2E-8C52-E55D97FA61F9/8059_wide_250x141_1x.jpg) Update your app for watchOS 10](https://developer.apple.com/videos/play/wwdc2023/10031)

[Change log](/design/human-interface-guidelines/designing-for-watchos#Change-log)

---------------------------------------------------------------------------------

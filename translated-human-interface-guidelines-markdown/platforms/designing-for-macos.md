### [[Platforms](./translated-human-interface-guidelines-markdown/platforms.md)]  
  
# **Designing for macOS**  

======================



People rely on the power, spaciousness, and flexibility of a Mac as they perform in-depth productivity tasks, view media or content, and play games, often using several apps at once.  

> 사람들은 심층적인 생산성 작업을 수행하고, 미디어나 콘텐츠를 보고, 게임을 하면서 종종 한 번에 여러 개의 앱을 사용하기 때문에 Mac의 성능, 넓은 공간 및 유연성에 의존합니다.
>

![A stylized representation of a Mac shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/c553fef2b37b038dea23f7ef210433b9/platforms-macOS-intro@2x.png)



As you begin designing your app or game for macOS, start by understanding the fundamental device characteristics and patterns that distinguish the macOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that Mac users appreciate.  

> MacOS용 앱이나 게임을 디자인하기 시작할 때, MacOS 경험을 구별하는 기본적인 장치 특성과 패턴을 이해하는 것부터 시작하십시오. 이러한 특성과 패턴을 사용하여 디자인 결정을 알려주면 Mac 사용자가 좋아하는 앱이나 게임을 제공하는 데 도움이 될 수 있습니다.
>





**Display.** A Mac typically has a large, high-resolution display, and people can extend their workspace by connecting additional displays, including their iPad.  

> **표시.** Mac은 일반적으로 큰 고해상도 디스플레이를 가지고 있으며 사람들은 아이패드를 포함한 추가 디스플레이를 연결하여 작업 공간을 확장할 수 있습니다.
>





**Ergonomics.** People generally use a Mac while they’re stationary, often placing the device on a desk or table. In the typical use case, the viewing distance can range from about 1 to 3 feet.  

> **경제학.** 사람들은 일반적으로 맥을 책상이나 테이블 위에 놓고 정지해 있는 동안 사용한다. 일반적인 사용 사례에서, 시야 거리는 약 1피트에서 3피트 사이일 수 있다.
>





**Inputs.** People expect to enter data and control the interface using any combination of input modes, such as physical   

> **입력.** 사람들은 물리적 입력 모드와 같은 모든 입력 모드 조합을 사용하여 데이터를 입력하고 인터페이스를 제어하기를 기대합니다
>

[Keyboards](/design/human-interface-guidelines/keyboards)

,   

[Pointing devices](/design/human-interface-guidelines/pointing-devices)

,   

[Game controllers](/design/human-interface-guidelines/game-controllers)

, and   

[Siri](/design/human-interface-guidelines/siri)

.  





**App interactions.** Interactions can last anywhere from a few minutes of performing some quick tasks to several hours of deep concentration. People frequently have multiple apps open at the same time, and they expect smooth transitions between active and inactive states as they switch from one app to another.  

> **앱 상호 작용.** 상호 작용은 몇 분 동안의 빠른 작업부터 몇 시간 동안의 깊은 집중까지 어디서든 지속될 수 있다. 사람들은 여러 개의 앱을 동시에 여는 경우가 많으며, 한 앱에서 다른 앱으로 전환할 때 활성 상태와 비활성 상태 사이의 원활한 전환을 기대한다.
>





**System features.** macOS provides several features that help people interact with the system and their apps in familiar, consistent ways.  

> **시스템 기능.** macOS는 사람들이 친숙하고 일관된 방식으로 시스템과 앱과 상호 작용할 수 있도록 도와주는 몇 가지 기능을 제공한다.
>





* [The menu bar](/design/human-interface-guidelines/the-menu-bar)

* [File management](/design/human-interface-guidelines/file-management)

* [Going full screen](/design/human-interface-guidelines/going-full-screen)

* [Dock menus](/design/human-interface-guidelines/dock-menus)



[Best practices](/design/human-interface-guidelines/designing-for-macos#Best-practices)

---------------------------------------------------------------------------------------



Great Mac experiences integrate the platform and device capabilities that people value most. To help your design feel at home in macOS, prioritize the following ways to incorporate these features and capabilities.  

> 훌륭한 Mac 경험은 사람들이 가장 중요하게 여기는 플랫폼과 장치 기능을 통합합니다. 디자인이 macOS에서 편안함을 느낄 수 있도록 다음과 같은 기능을 통합하는 방법의 우선순위를 정하십시오.
>





* Leverage large displays to present more content in fewer nested levels and with less need for modality, while maintaining a comfortable information density that doesn’t make people strain to view the content they want.

> * 대형 디스플레이를 활용하여 더 적은 중첩 수준에서 더 많은 콘텐츠를 표시하고 촬영장비의 필요성을 줄이는 동시에 사용자가 원하는 콘텐츠를 보기 위해 무리하지 않는 편안한 정보 밀도를 유지할 수 있습니다.
>

* Let people resize, hide, show, and move your windows to fit their work style and device configuration, and support full-screen mode to help people focus in a distraction-free context.

> * 작업 스타일과 장치 구성에 맞게 창 크기를 조정, 숨기기, 표시 및 이동할 수 있으며 전체 화면 모드를 지원하여 사용자가 산만하지 않은 컨텍스트에서 집중할 수 있도록 지원할 수 있습니다.
>

* Use the menu bar to give people easy access to all the commands they need to do things in your app.

> * 메뉴 모음을 사용하여 사용자가 앱에서 작업하는 데 필요한 모든 명령에 쉽게 액세스할 수 있습니다.
>

* Help people take advantage of high-precision input modes to perform pixel-perfect selections and edits.

> * 사람들이 고정밀 입력 모드를 활용하여 픽셀 단위로 완벽한 선택과 편집을 수행할 수 있도록 지원합니다.
>

* Handle keyboard shortcuts to help people accelerate actions and use keyboard-only work styles.

> * 키보드 단축키를 사용하여 작업을 가속화하고 키보드 전용 작업 스타일을 사용할 수 있습니다.
>

* Support personalization, letting people customize toolbars, configure windows to display the views they use most, and choose the colors and fonts they want to see in the interface.

> * 개인 설정을 지원하고, 사용자가 도구 모음을 사용자 지정하고, 가장 많이 사용하는 보기를 표시하도록 창을 구성하고, 인터페이스에서 보려는 색과 글꼴을 선택할 수 있습니다.
>



[Resources](/design/human-interface-guidelines/designing-for-macos#Resources)

-----------------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/designing-for-macos#Related)



[Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps)





#### [Developer documentation](/design/human-interface-guidelines/designing-for-macos#Developer-documentation)



[Planning your macOS app](https://developer.apple.com/macos/planning/)





#### [Videos](/design/human-interface-guidelines/designing-for-macos#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/119/3C2CAD33-3DF6-4CF9-9EE5-2E17D21DFD11/4944_wide_250x141_1x.jpg) What's new in AppKit](https://developer.apple.com/videos/play/wwdc2021/10054)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/1C541F0B-9AEC-4636-A1D4-C051DEF8117E/3364_wide_250x141_1x.jpg) Adopt the new look of macOS](https://developer.apple.com/videos/play/wwdc2020/10104)

------------------------------------------------------------------------------

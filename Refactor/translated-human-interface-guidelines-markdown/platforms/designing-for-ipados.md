### [[Platforms](./translated-human-interface-guidelines-markdown/platforms.md)]  
  
# **Designing for iPadOS**  

==========================
==========================



People value the power, mobility, and flexibility of iPad as they enjoy media, play games, perform detailed productivity tasks, and bring their creations to life.  

> 사람들은 미디어를 즐기고, 게임을 하고, 세부적인 생산성 작업을 수행하고, 창작물에 생기를 불어넣기 때문에 아이패드의 힘, 이동성, 유연성을 중요하게 생각한다.
>

![A stylized representation of an iPad frame shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/9601c88115bc94c01906416dbb3b8be8/platforms-iPadOS-intro@2x.png)



As you begin designing your app or game for iPad, start by understanding the following fundamental device characteristics and patterns that distinguish the iPadOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPad users appreciate.  

> iPad용 앱이나 게임을 설계하기 시작할 때, 먼저 iPad를 구별하는 다음과 같은 기본적인 장치 특성과 패턴을 이해하는 것부터 시작하십시오OS 경험. 이러한 특성과 패턴을 사용하여 디자인 결정을 알리는 것은 아이패드 사용자들이 감상할 수 있는 앱이나 게임을 제공하는 데 도움이 될 수 있다.
>





**Display.** iPad has a large, high-resolution display.  

> **표시.** 아이패드는 대형 고해상도 디스플레이를 갖추고 있다.
>





**Ergonomics.** People often hold their iPad while using it, but they might also set it on a surface or place it on a stand. Positioning the device in different ways can change the viewing distance, although people are typically within about 3 feet of the device as they interact with it.  

> **공학.** 사람들은 아이패드를 사용하면서 아이패드를 들고 있는 경우가 많지만, 아이패드를 표면에 놓거나 거치대에 놓을 수도 있다. 사람들이 기기와 상호작용할 때 일반적으로 기기로부터 약 3피트 이내에 있지만 기기를 다른 방식으로 위치시키면 시청 거리를 변경할 수 있다.
>





**Inputs.** People can interact with iPad using Multi-Touch   

> **입력.** 사람들은 멀티 터치를 사용하여 iPad와 상호작용할 수 있습니다
>

[gestures](https://developer.apple.com/design/human-interface-guidelines/touchscreen-gestures)

 and   

[onscreen keyboards](https://developer.apple.com/design/human-interface-guidelines/onscreen-keyboards)

, an attached   

[keyboard](https://developer.apple.com/design/human-interface-guidelines/keyboards)

 or   

[pointing device](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)

,   

[Apple Pencil](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble)

, or   

[voice](https://developer.apple.com/design/human-interface-guidelines/siri)

, and they often combine multiple input modes.  

> , 그리고 그들은 종종 여러 입력 모드를 결합한다.
>





**App interactions.** Sometimes, people perform a few quick actions on their iPad. At other times, they spend hours immersed in games, media, content creation, or productivity tasks. People frequently have multiple apps open at the same time, and they appreciate viewing more than one app onscreen at once and taking advantage of inter-app capabilities like drag and drop.  

> **앱 상호작용.** 때때로, 사람들은 그들의 아이패드에서 몇 가지 빠른 행동을 합니다. 다른 때에는 게임, 미디어, 콘텐츠 제작 또는 생산성 작업에 몇 시간을 할애하기도 합니다. 사람들은 동시에 여러 개의 앱을 여는 경우가 많으며, 한 번에 여러 개의 앱을 화면에 보고 드래그 앤 드롭과 같은 앱 간 기능을 활용하는 것을 높이 평가한다.
>





**System features.** iPadOS provides several features that help people interact with the system and their apps in familiar, consistent ways.  

> **시스템 기능.** 아이패드OS는 사람들이 친숙하고 일관된 방식으로 시스템과 앱과 상호 작용할 수 있도록 도와주는 몇 가지 기능을 제공한다.
>





* [Multitasking](/design/human-interface-guidelines/multitasking)

* [Widgets](/design/human-interface-guidelines/widgets)

* [Drag and drop](/design/human-interface-guidelines/drag-and-drop)



[Best practices](/design/human-interface-guidelines/designing-for-ipados#Best-practices)

----------------------------------------------------------------------------------------



Great iPad experiences integrate the platform and device capabilities that people value most. To help your experience feel at home in iPadOS, prioritize the following ways to incorporate these features and capabilities.  

> 훌륭한 아이패드 경험은 사람들이 가장 중요하게 여기는 플랫폼과 기기 기능을 통합한다. iPad OS에서 편안한 경험을 얻으려면 다음과 같은 기능을 통합하는 방법을 우선시하십시오.
>





* Take advantage of the large display to elevate the content people care about, minimizing modal interfaces and full-screen transitions, and positioning onscreen controls where they’re easy to reach, but not in the way.

> * 대형 디스플레이를 활용하여 사람들이 신경 쓰는 콘텐츠를 업그레이드하고, 모달 인터페이스와 전체 화면 전환을 최소화하며, 화면 컨트롤에 접근하기 쉽지만 방해가 되지 않는 곳에 배치할 수 있습니다.
>

* Use viewing distance and input mode to help you determine the size and density of the onscreen content you display.

> * 표시하는 화면 콘텐츠의 크기와 밀도를 확인하려면 시청 거리 및 입력 모드를 사용하십시오.
>

* Let people use Multi-Touch gestures, a physical keyboard or trackpad, or Apple Pencil, and consider supporting unique interactions that combine multiple input modes.

> * 멀티 터치 제스처, 물리적 키보드 또는 트랙패드 또는 Apple Pencil을 사용하고 여러 입력 모드를 결합하는 고유한 상호 작용 지원을 고려해 보십시오.
>

* Adapt seamlessly to appearance changes — like device orientation, multitasking modes, Dark Mode, and Dynamic Type — and transition effortlessly to running in macOS, letting people choose the configurations that work best for them.

> * 장치 방향, 멀티태스킹 모드, 다크 모드 및 동적 유형과 같은 외관 변화에 완벽하게 적응하고 macOS에서 실행되도록 쉽게 전환하여 사용자가 가장 적합한 구성을 선택할 수 있습니다.
>



[Resources](/design/human-interface-guidelines/designing-for-ipados#Resources)

------------------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/designing-for-ipados#Related)



[Apple Design Resources](https://developer.apple.com/design/resources/#ios-apps)





#### [Developer documentation](/design/human-interface-guidelines/designing-for-ipados#Developer-documentation)



[Planning your iPadOS app](https://developer.apple.com/ipados/planning/)





#### [Videos](/design/human-interface-guidelines/designing-for-ipados#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/124/6E076CE0-7DDF-4471-B6F0-005ADF9C7960/6500_wide_250x141_1x.jpg) What’s new in iPad app design](https://developer.apple.com/videos/play/wwdc2022/10009)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/5C8F0205-3AE9-4647-870B-5C10FB7EA6FF/3520_wide_250x141_1x.jpg) Designed for iPad](https://developer.apple.com/videos/play/wwdc2020/10206)

------------------------------------------------------------------------------

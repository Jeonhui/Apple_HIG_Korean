# **[Platforms] Designing for iOS**

### **People depend on their iPhone to help them stay connected, play games, view media, accomplish tasks, and track personal data in any location and while on the go.**
> 사람들은 iPhone에 의존하여 어디서나 연결 상태를 유지하고, 게임을 하고, 미디어를 보고, 작업을 수행하고, 개인 데이터를 추적합니다.
>




As you begin designing your app or game for iOS, start by understanding the following fundamental device characteristics and patterns that distinguish the iOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPhone users appreciate.
> iOS용 앱이나 게임을 디자인하기 시작할 때, iOS 경험을 구별하는 다음과 같은 기본적인 장치 특성과 패턴을 이해하는 것부터 시작하세요. 이러한 특징과 패턴을 사용하여 디자인 결정을 알려주면 iPhone 사용자가 높이 평가하는 앱이나 게임을 제공하는 데 도움이 될 수 있습니다.
>




### **Display.**

iPhone has a medium-sized, high-resolution display.
> 아이폰은 중간 크기의 고해상도 디스플레이를 갖추고 있다.
>




### **Ergonomics.**

People generally hold their iPhone in one or both hands as they interact with it, switching between landscape and portrait orientations as needed. While people are interacting with the device, their viewing distance tends to be no more than a foot or two.
> 사람들은 일반적으로 아이폰과 상호작용할 때 한 손이나 양손으로 아이폰을 들고, 필요에 따라 가로 방향과 세로 방향을 바꾼다. 사람들이 기기와 상호작용하는 동안 시야 거리는 1피트 또는 2피트에 지나지 않는 경향이 있다.
>




### **Inputs.**

Multi-Touch [gestures](../inputs/touchscreen-gestures.md),[onscreen keyboards](../components/selection-and-input/onscreen-keyboards.md), and [voice](../technologies/siri/introduction.md) control let people perform actions and accomplish meaningful tasks while they’re on the go. In addition, people often want apps to use their [location](../patterns/accessing-private-data.md) and input from the device’s [accelerometer and gyroscope](../inputs/gyro-and-accelerometer.md), and they may also want to participate in [spatial interactions](../inputs/spatial-interactions.md).
> 멀티터치 제스처, 화면 키보드 및 음성 제어를 통해 이동 중에도 작업을 수행하고 의미 있는 작업을 수행할 수 있습니다. 또한, 사람들은 종종 앱이 장치의 가속도계와 자이로스코프의 위치와 입력을 사용하기를 원하며, 그들은 또한 공간 상호 작용에 참여하기를 원할 수 있다.
>




### **App interactions.**

Sometimes, people spend just a minute or two checking on event or social media updates, tracking data, or sending messages. At other times, people can spend an hour or more browsing the web, playing games, or enjoying media. People typically have multiple apps open at the same time, and they appreciate switching frequently among them.
> 때때로, 사람들은 이벤트나 소셜 미디어 업데이트를 확인하고, 데이터를 추적하거나, 메시지를 보내는 데 단지 1~2분을 소비한다. 다른 때에는, 사람들은 웹을 검색하거나, 게임을 하거나, 미디어를 즐기는데 한 시간 이상을 보낼 수 있다. 사람들은 일반적으로 동시에 여러 개의 앱을 열고 있으며, 그 사이에서 자주 전환하는 것을 높이 평가한다.
>




### **System features.**

iOS provides several features that help people interact with the system and their apps in familiar, consistent ways.
> iOS는 사람들이 친숙하고 일관된 방식으로 시스템 및 앱과 상호 작용할 수 있도록 도와주는 몇 가지 기능을 제공합니다.
>




- [Widgets](../components/system-experiences/widgets.md)
- [Home Screen quick actions](../components/system-experiences/home-screen-quick-actions.md)
- >  홈 스크린 빠른 동작

- [Spotlight](../patterns/searching.md)
- [Shortcuts](../technologies/siri/shortcuts-and-suggestions.md)
- [Activity views](../components/menus-and-actions/activity-views.md)


## **Best practices**

Great iPhone experiences integrate the platform and device capabilities that people value most. To help your design feel at home in iOS, prioritize the following ways to incorporate these features and capabilities.
> 훌륭한 아이폰 경험은 사람들이 가장 중요하게 생각하는 플랫폼과 기기 기능을 통합한다. iOS에서 디자인이 편안함을 느끼도록 하기 위해, 다음과 같은 특징과 기능을 통합하는 방법을 우선시하십시오.
>




- Help people focus on primary tasks and content by limiting the number of onscreen controls while making secondary details and actions discoverable with minimal interaction.
- >  최소한의 상호 작용으로 보조 세부 정보와 작업을 검색할 수 있도록 하는 동시에 화면 컨트롤의 수를 제한하여 사람들이 기본 작업과 내용에 집중할 수 있도록 지원합니다.

- Adapt seamlessly to appearance changes — like device orientation, Dark Mode, and Dynamic Type — letting people choose the configurations that work best for them.
- >  장치 방향, 다크 모드 및 동적 유형과 같은 외관 변화에 원활하게 적응하여 사용자가 자신에게 가장 적합한 구성을 선택할 수 있습니다.

- Enable interactions that support the way people usually hold their device. For example, it tends to be easier and more comfortable for people to reach a control when it’s located in the middle or bottom area of the display, so it’s especially important let people swipe to navigate back or initiate actions in a list row.
- >  사용자가 일반적으로 장치를 고정하는 방식을 지원하는 상호 작용을 활성화합니다. 예를 들어 컨트롤이 디스플레이의 중앙 또는 하단 영역에 위치하면 사용자가 컨트롤을 쉽게 찾을 수 있으므로 사용자가 뒤로 이동하거나 목록 행에서 작업을 시작할 수 있도록 하는 것이 특히 중요합니다.

- With people’s permission, integrate information available through platform capabilities in ways that enhance the experience without asking people to enter data. For example, you might accept payments, provide security through biometric authentication, or offer features that use the device’s location.
- >  사용자의 허가를 받아 플랫폼 기능을 통해 제공되는 정보를 사용자에게 데이터 입력을 요청하지 않고 경험을 향상시키는 방식으로 통합합니다. 예를 들어 결제를 수락하거나 생체 인증을 통해 보안을 제공하거나 장치의 위치를 사용하는 기능을 제공할 수 있습니다.


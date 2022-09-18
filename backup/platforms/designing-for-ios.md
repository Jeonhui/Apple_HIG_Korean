# **[Platforms] Designing for iOS**

### **People depend on their iPhone to help them stay connected, play games, view media, accomplish tasks, and track personal data in any location and while on the go.**

> 사용자들은 그들의 아이폰에 의존하여 언제, 어디에 있든 연결을 유지하고, 게임을 하며 미디어를 보고, 작업을 수행하고, 사용자들의 정보를 추적합니다.
>

<br/>

As you begin designing your app or game for iOS, start by understanding the following fundamental device characteristics and patterns that distinguish the iOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPhone users appreciate.

> 당신이 iOS 앱이나 게임 디자인을 하기 시작했을 때, iOS의 경험을 구분하는 것은 기초적인 장치의 특성과 패턴들을 이해하는 것부터 시작합니다. 이러한 특성과 패턴들을 사용하여 당신의 디자인을 전달하게 된다면, iPhone 사용자가 높이 평가하는 앱이나 게임을 제공하는 데 도움이 될 수 있습니다.
>

<br/>

### **Display.**

iPhone has a medium-sized, high-resolution display.

> 디스플레이. 아이폰은 중간 사이즈 고해상도 디스플레이를 가지고 있습니다.
>

### **Ergonomics.**

People generally hold their iPhone in one or both hands as they interact with it, switching between landscape and portrait orientations as needed. While people are interacting with the device, their viewing distance tends to be no more than a foot or two.

> 인체 공학. 사용자들은 일반적으로 iPhone을 사용할 한 손이나 양손으로 iPhone을 들고, 필요에 따라 가로와 세로로 화면을 전환합니다. 사용자들이 기기와 상호작용하는 동안, 그들의 시야 거리가 1피트나 2피트 보다 크지 않은 경향이 있습니다.
>

<br/>

### **Inputs.**

Multi-Touch [gestures](../inputs/touchscreen-gestures.md), [onscreen keyboards](../components/selection-and-input/onscreen-keyboards.md), and [voice](../technologies/siri/introduction.md) control let people perform actions and accomplish meaningful tasks while they’re on the go. In addition, people often want apps to use their [location](../patterns/accessing-private-data.md) and input from the device’s [accelerometer and gyroscope](../inputs/gyro-and-accelerometer.md), and they may also want to participate in [spatial interactions](../inputs/spatial-interactions.md).

> 입력, 멀티터치 제스쳐, 화상 키보드, 음성 제어를 통해 그들이 이동 중에도 행동을 하거나, 의미 있는 작업을 할 수 있습니다. 게다가, 사용자들은 자주 그들의 위치와 기기의 가속도계와 회전계로부터의 입력을 사용하는 앱을 원하고, 또한, 공간 상호 작용을 원할 수 있습니다.
>

<br/>

### **App interactions.**

Sometimes, people spend just a minute or two checking on event or social media updates, tracking data, or sending messages. At other times, people can spend an hour or more browsing the web, playing games, or enjoying media. People typically have multiple apps open at the same time, and they appreciate switching frequently among them.

> 앱 상호작용. 때때로, 사용자들은 이벤트 체크나 SNS 업데이트, 데이터 추적, 메세지를 보내는 데에 단지 1-2분 정도를 소비한다. 다른 때, 사용들은 웹페이지를 불러오는 것, 게임을 하거나 미디어를 즐기는 데에 1시간이나 더 많은 시간을 소비할 수 있습니다. 사용자들은 일반적으로 동시에 다양한 애플리케션을 열어 놓고 있고, 사용자들은 그것들 중에서 자주 바꿔주는 것을 높이 평가합니다.
>

<br/>

### **System features.**

iOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

> 시스템 특성. iOS는 사용자들이 친숙하고, 일관적인 방식으로 시스템과 앱에서 상호작용을 도와줄 수 있는 몇 개의 특성을 제공합니다.
>
- [Widgets](../components/system-experiences/widgets.md)
- [Home Screen quick actions](../components/system-experiences/home-screen-quick-actions.md)
- [Spotlight](../patterns/searching.md)
- [Shortcuts](../technologies/siri/shortcuts-and-suggestions.md)
- [Activity views](../components/menus-and-actions/activity-views.md)


## **Best practices**

Great iPhone experiences integrate the platform and device capabilities that people value most. To help your design feel at home in iOS, prioritize the following ways to incorporate these features and capabilities.

> 좋은 아이폰 경험 사용자들이 가장 중요시여기는 플랫폼과 기기 성능을 통합합니다. iOS에서 당신의 디자인이 편안함을 느낄 수 있도록 하기 위해, 다음과 같은 특징과 성능을 통합하는 방법의 우선 순위를 지정합니다.
>
- Help people focus on primary tasks and content by limiting the number of onscreen controls while making secondary details and actions discoverable with minimal interaction.
- <blockquote>최소한의 상호 작용으로 보조 세부 정보와 작업을 검색할 수 있도록 하는 동시에 화면 컨트롤의 수를 제한하여 사용자들이 기본 작업과 내용에 집중할 수 있도록 지원합니다.</blockquote>
- Adapt seamlessly to appearance changes — like device orientation, Dark Mode, and Dynamic Type — letting people choose the configurations that work best for them.
- <blockquote>외형 변화에 원활한 적응 - 기기 방향, 다크 모드, 동적 타입 - 사용자들이 자신에게 가장 적합한 구성을 선택하도록 허용</blockquote>
- Enable interactions that support the way people usually hold their device. For example, it tends to be easier and more comfortable for people to reach a control when it’s located in the middle or bottom area of the display, so it’s especially important let people swipe to navigate back or initiate actions in a list row.
- <blockquote>사용자들이 일반적으로 기기를 잡는 방식을 지지하는 상호작용들을 활성화합니다. 예를 들어, 컨트롤이 디스플레이의 중간이나 바닥 부분에 위치할 때, 컨트롤이 도달하는 것을 쉽고, 더 편안하게 하는 경향이 있으므로, 사용자가 뒤로 이동하거나 목록 행에서 작업을 시작할 수 있도록 하는 것이 특히 중요합니다.</blockquote>
- With people’s permission, integrate information available through platform capabilities in ways that enhance the experience without asking people to enter data. For example, you might accept payments, provide security through biometric authentication, or offer features that use the device’s location.
- <blockquote>사용자들의 권한을 가지고, 사용자에게 데이터 입력을 요청하지 않고 경험을 향상시키는 방식으로 플랫폼 기능을 통해 제공되는 정보를 통합합니다. 예를 들어, 당신은 결제 승인 및 생체인증을 통해 보안 제공하거나, 기기의 위치 정보를 사용하는 특성을 제공할 수 있습니다.</blockquote>
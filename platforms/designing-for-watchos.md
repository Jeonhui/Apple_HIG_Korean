# **[Platforms] Designing for watchOS**

### When people glance at their Apple Watch, they know they can access essential information and perform simple, timely tasks whether they’re stationary or in motion.
> 사람들이 Apple Watch를 보면, 그들이 중요한 정보에 접근할 수 있고, 그들이 정지해 있든 이동 중이든 간에 간단하고 시기 적절한 작업을 수행할 수 있다는 것을 알 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/platforms/platform-watchOS-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/platforms/platform-watchOS-intro-dark_2x.png)

As you begin designing your app for Apple Watch, start by understanding the following fundamental device characteristics and patterns that distinguish the watchOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app that Apple Watch users appreciate.
> Apple Watch용 앱을 디자인하기 시작할 때, 시계를 구별하는 다음과 같은 기본적인 장치 특성과 패턴을 이해하는 것부터 시작하십시오.OS 경험. 이러한 특징과 패턴을 사용하여 디자인 결정을 알려주면 Apple Watch 사용자가 높이 평가하는 앱을 제공하는 데 도움이 될 수 있습니다.
>




**Display.** The small Apple Watch display fits on the wrist while delivering an easy-to-read, high-resolution experience.
> 디스플레이. 작은 Apple Watch 디스플레이는 손목에 딱 맞으며 읽기 쉽고 고해상도 환경을 제공합니다.
>




**Ergonomics.** Because people wear Apple Watch, they’re usually no more than a foot away from the display as they raise their wrist to view it and use their opposite hand to interact with the device. In addition, the Always On display lets people view information on the watch face when they drop their wrist.
> 사람들은 애플워치를 착용하기 때문에 손목시계를 올려 보고 반대쪽 손으로 장치와 상호 작용할 때 보통 디스플레이에서 1피트 정도 떨어져 있지 않습니다. 게다가, 항상 켜져 있는 디스플레이는 사람들이 손목을 떨어뜨릴 때 시계 얼굴의 정보를 볼 수 있게 해준다.
>




**Inputs.** Using standard [Multi-Touch gestures](../inputs/touchscreen-gestures) like tap, swipe, and drag lets people control their experience even while they’re in motion. Turning the [Digital Crown](../inputs/digital-crown) imparts additional precision and feedback to scrolling interfaces, pressing the [Action button](../inputs/action-button) initiates an essential action without looking at the screen, and using [Siri Shortcuts](../technologies/siri/shortcuts-and-suggestions) can help people perform their routine tasks quickly and easily. People also appreciate taking advantage of data that device features — like GPS, sensors for blood oxygen and heart function, altimeter, accelerometer, and gyroscope — can provide.
> Inputs. 탭, 비난,과 항력과 같은 표준 Multi-Touch 몸짓을 이용하여 심지어 운동에 사람들 경험을 통제할 수 있다. 디지털 크라운을 돌리는 것, 화면을 보지 않고 필수적인 조치를 시작할 때, 시리 Shortcuts을 사용하여 사람들 빠르고 쉽게 그들의 통상적인 작업을 수행할 수 있는 액션 버튼을 누르고 추가 정밀도와 인터페이스 스크롤의 피드백을 전한다. 사람들은 또한 장치 — GPS처럼 특징의 데이터, 혈액 산소와 심장 기능용 센서, 고도계, 가속도계 이용하여, gyroscope —을 제공할 수 있어 주셔서 감사 드립니다.
>




**App interactions.** People often glance at the Always On display many times throughout the day, performing focused app interactions that can last for less than a minute each. People frequently use a watchOS app’s related experiences — like complications, notifications, and Siri interactions — more than they use the app itself.
> 앱 상호 작용. 사람들은 종종 하루 종일 상시(Always On) 디스플레이를 여러 번 쳐다보며 각각 1분도 채 지속되지 않는 집중적인 앱 상호 작용을 수행합니다. 사람들은 시계를 자주 사용한다.복잡한 문제, 알림 및 Siri 상호 작용과 같은 OS 앱의 관련 경험은 앱 자체를 사용하는 것보다 더 많습니다.
>




**System features.** watchOS provides several features that help people interact with the system and their apps in familiar, consistent ways.
> 시스템 기능. 시계OS는 사람들이 친숙하고 일관된 방식으로 시스템 및 앱과 상호 작용할 수 있도록 도와주는 몇 가지 기능을 제공합니다.
>




- [Complications](../components/system-experiences/complications)
- [Notifications](../components/system-experiences/notifications)
- [Always On](../technologies/always-on)
- [Faces](../components/system-experiences/watch-faces)

# **Best practices**

Great Apple Watch experiences integrate the platform and device capabilities that people value most. To help your experience feel at home in watchOS, prioritize the following ways to incorporate these features and capabilities.
> 훌륭한 Apple Watch 경험은 사람들이 가장 중요하게 생각하는 플랫폼과 장치 기능을 통합합니다. watch OS에서 편안함을 느끼도록 하기 위해, 다음과 같은 기능들을 통합하는 방법을 우선시하십시오.
>




- Enable quick, glanceable interactions that deliver critical information succinctly and help people perform targeted actions with a simple gesture or two.
- >  중요한 정보를 간결하게 전달하고 사람들이 간단한 제스처로 목표한 작업을 수행할 수 있도록 도와주는 빠르고 쉽게 상호 작용을 수행할 수 있습니다.

- Personalize the experience by proactively anticipating people’s needs and using on-device data to provide actionable content that’s relevant in the moment or very soon.
- >  사용자의 요구를 능동적으로 예측하고 장치 내 데이터를 사용하여 즉시 또는 즉시 관련성이 있는 실행 가능한 콘텐츠를 제공함으로써 경험을 개인화합니다.

- Use [complications](../components/system-experiences/complications) to provide relevant, potentially dynamic data and graphics right on the watch face where people can view them on every wrist raise and tap them to dive straight into your app.
- >  복잡한 작업을 통해 관련성이 있고 잠재적으로 역동적인 데이터 및 그래픽을 손목 위로 올릴 때마다 사람들이 볼 수 있고 앱으로 바로 뛰어들 수 있도록 탭할 수 있습니다.

- Use [notifications](../components/system-experiences/notifications) to deliver timely, high-value information and enable important actions people can take without opening your app.
- >  알림을 사용하여 시기적절하고 가치 있는 정보를 전달하고 앱을 열지 않고도 사용자가 수행할 수 있는 중요한 작업을 수행할 수 있습니다.

- Support Siri to help people access shortcuts on the Siri watch face.
- >  사람들이 시리 워치 페이스의 바로 가기에 접근할 수 있도록 시리를 지원하십시오.

- Design your app to function independently, complementing your notifications and complications by providing additional details and functionality.
- >  별도의 세부 정보와 기능을 제공하여 알림과 복잡성을 보완하여 독립적으로 작동하도록 앱을 설계하십시오.


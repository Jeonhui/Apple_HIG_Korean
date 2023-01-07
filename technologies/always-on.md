# **[technologies] always-on**

## On devices that include the Always On display, the system can continue to display an app’s interface when people suspend their interactions with the device.
> Always On 디스플레이가 포함된 장치에서는 사용자가 장치와의 상호 작용을 일시 중단할 때 시스템이 앱의 인터페이스를 계속 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-always-on-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-always-on-intro_2x.png)

In the Always On state, a device can continue to give people useful, glanceable information in a low-power, privacy-preserving way by dimming the display and minimizing onscreen motion. The system can display different items depending on the device.
> 항상 켜져 있는 상태에서 장치는 디스플레이를 어둡게 하고 화면 움직임을 최소화하여 개인 정보를 보존하는 저전력 방식으로 사람들에게 유용하고 눈에 띄는 정보를 계속 제공할 수 있다. 시스템은 장치에 따라 다른 항목을 표시할 수 있습니다.
>




- On iPhone 14 Pro and iPhone 14 Pro Max, the system displays Lock Screen items like [widgets](../components/system-experiences/widgets) and [Live Activities](../components/system-experiences/live-activities) when people set aside their device face up and stop interacting with it.
- >  아이폰 14 프로와 아이폰 14 프로 맥스에서, 이 시스템은 사람들이 그들의 기기를 얼굴을 위로 하고 그것과 상호 작용을 멈출 때 위젯과 라이브 액티비티와 같은 잠금 화면 항목을 표시한다.

- When people drop their wrist while wearing Apple Watch, the system dims the watch face, continuing to display the interface of the app as long as it’s either frontmost or running a background session.
- >  사람들이 애플 워치를 착용하고 있을 때 손목을 떨어뜨리면, 이 시스템은 시계의 얼굴을 어둡게 하며, 앱이 가장 앞쪽에 있거나 백그라운드 세션을 실행하는 한 계속해서 인터페이스를 표시한다.


On both devices, the system displays notifications while in Always On, and people can tap the display to exit Always On and resume interactions.
> 두 장치 모두에서 시스템은 항상 켜져 있는 동안 알림을 표시하며, 사용자는 디스플레이를 눌러 항상 켜져 있는 상태를 종료하고 상호 작용을 다시 시작할 수 있습니다.
>




# **Best practices**

**Hide sensitive information.** It’s crucial to redact personal information that people wouldn’t want casual observers to view, like bank balances or health data. You also need to hide personal information that might be visible in a notification; for guidance, see [Notifications](../components/system-experiences/notifications).
> 중요한 정보를 숨깁니다. 은행 잔고나 건강 데이터와 같이 사람들이 무심코 보는 것을 원하지 않는 개인 정보를 수정하는 것이 중요합니다. 또한 알림에 표시될 수 있는 개인 정보를 숨겨야 합니다. 자세한 내용은 알림을 참조하십시오.
>




**Keep other types of personal information glanceable when it makes sense.** On Apple Watch, for example, people typically appreciate getting pace and heart rate updates while they’re working out; on iPhone, people appreciate getting a glanceable update on a flight arrival or a notification when a ride-sharing service arrives. If people don’t want any information to be visible, they can turn off Always On.
> 예를 들어, Apple Watch에서는 일반적으로 운동하는 동안 속도 및 심박수 업데이트를 받는 것을 좋아하고, iPhone에서는 비행기 도착에 대한 업데이트나 승차 공유 서비스가 도착할 때 알림을 받는 것을 좋아합니다. 정보를 표시하지 않으려면 항상 설정을 해제할 수 있습니다.
>




**Keep important content legible and dim nonessential content.** You can increase dimming on secondary text, images, and color fills to give more prominence to the information that’s important to people. For example, a to-do list app might remove row backgrounds and dim each item’s additional details to highlight its title. Also, if you display rich images or large areas of color, consider removing the images and using dimmed colors.
> 중요한 내용을 읽기 쉽고 어둡게 유지합니다. 보조 텍스트, 이미지 및 색 채우기의 조광을 높여 사람에게 중요한 정보를 더 잘 나타낼 수 있습니다. 예를 들어, 할 일 목록 앱은 행 배경을 제거하고 각 항목의 추가 세부 정보를 흐리게 하여 제목을 강조 표시할 수 있습니다. 또한 풍부한 이미지를 표시하거나 색상이 큰 영역을 표시하는 경우 이미지를 제거하고 흐리게 표시되는 색상을 사용하는 것이 좋습니다.
>




**Maintain a consistent layout.** Avoid making distracting interface changes when Always On begins or ends and throughout the Always On experience. For example, when Always On begins, prefer transitioning an interactive component to an unavailable appearance — don’t just remove it. Within the Always On context, aim to make infrequent, subtle updates to the interface. For example, a sports app might pause granular play-by-play updates while in Always On, only updating the score when it changes. Note that unnecessary changes during Always On can be especially distracting on iPhone, because people often put their device face up on a surface, making motion on the screen visible even when they’re not looking directly at it.
> 일관된 레이아웃을 유지합니다. Always On이 시작되거나 끝날 때 그리고 Always On 환경 전체에서 주의를 산만하게 하는 인터페이스 변경을 피하십시오. 예를 들어 항상 설정이 시작되면 대화형 구성 요소를 사용할 수 없는 모양으로 전환하는 것을 선호합니다. 제거만 하지 마십시오. Always On 컨텍스트 내에서 인터페이스를 자주 업데이트하지 않고 미묘한 업데이트를 수행하는 것을 목표로 합니다. 예를 들어 스포츠 앱은 항상 켜져 있는 동안 세부적인 재생별 업데이트를 일시 중지하고 점수가 변경될 때만 업데이트할 수 있습니다. 사람들은 종종 장치를 표면 위에 올려놓고 직접 보지 않을 때에도 화면의 움직임을 볼 수 있도록 하기 때문에 항상 켜져 있는 동안의 불필요한 변경은 특히 iPhone에서 주의를 산만하게 할 수 있습니다.
>




**Gracefully transition motion to a resting state; don’t stop it instantly.** Smoothly finishing the current motion helps communicate the transition and avoids making people think that something went wrong.
> 동작을 정지 상태로 우아하게 전환합니다. 즉시 중지하지 마십시오. 현재 동작을 부드럽게 완료하면 전환을 전달하는 데 도움이 되고 사람들이 무언가 잘못되었다고 생각하지 않도록 합니다.
>




# **Platform considerations**

*No additional considerations for iOS or watchOS. Not supported in iPadOS, macOS, or tvOS.*
> iOS 또는 watch OS에 대한 추가 고려 사항은 없습니다. iPadOS, macOS 또는 tvOS에서는 지원되지 않습니다.
>




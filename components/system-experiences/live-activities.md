# **[components-status] live-activities**

## A Live Activity displays up-to-date information from your app, allowing people to view the progress of events or tasks at a glance.
> 실시간 활동은 앱의 최신 정보를 표시하여 사용자가 이벤트 또는 작업의 진행률을 한 눈에 볼 수 있도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/live-activities-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/live-activities-intro-dark_2x.png)

Live Activities help people keep track of tasks and events that they care about, offering persistent locations for displaying information that updates frequently. For example, a food delivery app could display the time remaining until a food order arrives, or a sports app can display the score for an ongoing game.
> 실시간 활동은 사용자가 관심 있는 작업 및 이벤트를 추적하는 데 도움이 되며, 자주 업데이트되는 정보를 표시할 수 있는 지속적인 위치를 제공합니다. 예를 들어, 음식 배달 앱은 음식 주문이 도착할 때까지 남은 시간을 표시하거나, 스포츠 앱은 진행 중인 게임의 점수를 표시할 수 있습니다.
>




In addition to displaying a Live Activity on the Lock Screen, devices that support Live Activities can display your app information in different ways, depending on whether the device also supports the Dynamic Island.
> 라이브 활동을 지원하는 장치는 잠금 화면에 라이브 활동을 표시할 뿐만 아니라 동적 섬도 지원하는지 여부에 따라 다양한 방법으로 앱 정보를 표시할 수 있습니다.
>




- On devices that support the Dynamic Island, the system displays Live Activities in a persistent location around the TrueDepth camera.
- >  Dynamic Island를 지원하는 장치에서는 TrueDepth 카메라 주변의 지속적인 위치에 Live Activities가 표시됩니다.

- On devices that don’t support the Dynamic Island, the system can display a Live Activity update in a banner that appears briefly on the top of the screen.
- >  Dynamic Island를 지원하지 않는 장치에서는 시스템이 실시간 활동 업데이트를 화면 상단에 잠깐 나타나는 배너에 표시할 수 있습니다.


To display a Live Activity, the system uses the following presentations:
> 실시간 활동을 표시하기 위해 시스템은 다음 프레젠테이션을 사용합니다.
>




- **Compact.** In the Dynamic Island, the system uses the compact presentation when there’s only one Live Activity that’s currently active. The compact presentation is composed of two separate presentations: one that displays on the leading side of the TrueDepth camera, and one that displays on the trailing side. Although the leading and trailing presentations are separate views, they form a cohesive view in the Dynamic Island, representing a single piece of information from your app. People can tap a compact Live Activity to open the app and get more details about the event or task.
- >  Dynamic Island에서는 현재 활성화된 라이브 활동이 하나만 있을 때 시스템이 컴팩트 프레젠테이션을 사용합니다. 컴팩트 프레젠테이션은 TrueDepth 카메라의 앞쪽에 표시되는 프레젠테이션과 뒤쪽에 표시되는 프레젠테이션의 두 가지로 구성됩니다. 선행 및 후행 프레젠테이션은 별도의 보기이지만 동적 섬에서 하나의 통합된 보기를 형성하여 앱의 단일 정보를 나타냅니다. 사람들은 앱을 열고 이벤트나 작업에 대한 자세한 정보를 얻기 위해 컴팩트한 라이브 활동을 탭 할 수 있다.


![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-compact-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-compact-dark_2x.png)

- **Minimal.** When multiple Live Activities are active, the system uses the minimal presentation to display two of them in the Dynamic Island. One Live Activity appears attached to the Dynamic Island while the other appears detached. Depending on its content size, the detached minimal Live Activity appears circular or oval. As with a compact Live Activity, people tap a minimal Live Activity to open the app and get more details about the event or task.
- >  최소. 여러 라이브 활동이 활성화된 경우 시스템은 최소 프레젠테이션을 사용하여 두 개의 활동을 동적 섬에 표시합니다. 하나의 라이브 활동은 Dynamic Island에 연결된 상태로 표시되고 다른 활동은 분리된 상태로 표시됩니다. 내용 크기에 따라 분리된 최소 실시간 활동은 원형 또는 타원형으로 나타납니다. 소형 라이브 활동과 마찬가지로, 사람들은 최소한의 라이브 활동을 눌러 앱을 열고 이벤트나 작업에 대한 자세한 정보를 얻습니다.


![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-minimal-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-minimal-dark_2x.png)

- **Expanded.** When people touch and hold a Live Activity in a compact or minimal presentation, the system displays the content in an expanded presentation.
- >  확장됨. 사용자가 실시간 활동을 소형 또는 최소 프리젠테이션으로 길게 누르면 시스템은 내용을 확장된 프리젠테이션으로 표시합니다.


![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-expanded-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-expanded-dark_2x.png)

- **Lock Screen.** On the Lock Screen and on devices that don't support the Dynamic Island, the system uses the Lock Screen presentation to display a banner on the top of the screen. It appears briefly while people view the Home Screen or use another app, but only if the app determines that the update is important enough to interrupt people.
- >  잠금 화면. 잠금 화면과 Dynamic Island를 지원하지 않는 장치에서 시스템은 잠금 화면 프레젠테이션을 사용하여 화면 상단에 배너를 표시합니다. 사용자가 홈 스크린을 보거나 다른 앱을 사용하는 동안 잠시 표시되지만, 앱이 업데이트가 사용자를 방해할 정도로 중요하다고 판단하는 경우에만 표시됩니다.


![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/live-activity-notch-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/live-activity-notch-dark_2x.png)

To ensure that your Live Activity works well on all devices that can support it — and in all system-determined presentations — you need to support all three presentation types for the Dynamic Island, in addition to the Lock Screen presentation.
> 라이브 활동을 지원할 수 있는 모든 장치와 시스템에서 결정된 모든 프레젠테이션에서 라이브 활동이 제대로 작동하려면 잠금 화면 프레젠테이션 외에 동적 아일랜드에 대한 세 가지 프레젠테이션 유형을 모두 지원해야 합니다.
>




For developer guidance, see [ActivityKit](https://developer.apple.com/documentation/activitykit).

# **Best practices**

**Offer a Live Activity for tasks and live events that have a defined beginning and end.** People use Live Activities to track events with frequently updating data or to monitor the status of ongoing tasks. Don’t offer a Live Activity for a task that exceeds eight hours, and always end a Live Activity immediately after the task completes or the event ends.
> 시작과 끝이 정의된 작업 및 라이브 이벤트에 대해 라이브 활동을 제공합니다. 사용자는 라이브 활동을 사용하여 자주 업데이트되는 데이터로 이벤트를 추적하거나 진행 중인 작업의 상태를 모니터링합니다. 8시간을 초과하는 작업에 대해 실시간 활동을 제공하지 말고 항상 작업이 완료되거나 이벤트가 종료된 직후에 실시간 활동을 종료하십시오.
>




**Present only the most essential content.** People appreciate getting a summary and key bits of information about an ongoing task or event; they don’t expect to receive a lot of details or to perform actions in a Live Activity. Let people tap your Live Activity to access additional details and functionality within your app.
> 가장 중요한 내용만 제시합니다. 사람들은 진행 중인 작업이나 이벤트에 대한 요약과 주요 정보를 얻는 것을 좋아합니다. 그들은 라이브 활동에서 많은 세부 정보를 받거나 행동을 수행할 것을 기대하지 않습니다. 사용자가 실시간 활동을 눌러 앱 내의 추가 세부 정보 및 기능에 액세스할 수 있습니다.
>





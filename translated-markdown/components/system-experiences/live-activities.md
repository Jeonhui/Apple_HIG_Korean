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




**Update a Live Activity only when new content is available, alerting people only if it’s essential to get their attention.** It can be disruptive to alert people to a Live Activity update, and alerting them too often — or alerting them to updates that aren’t crucial — can annoy people and encourage them to stop using your Live Activities. Note that the system alerts people to a Live Activity update in different ways, depending on the device and whether it supports the Dynamic Island.
> 새 콘텐츠가 있는 경우에만 실시간 활동을 업데이트하고, 관심을 끄는 것이 중요한 경우에만 사람들에게 경고합니다. 실시간 활동 업데이트에 대해 사람들에게 경고하는 것은 방해가 될 수 있으며, 너무 자주 경고하거나 중요하지 않은 업데이트에 대해 경고하는 것은 사람들을 짜증나게 하고 라이브 활동 사용을 중단하도록 권장할 수 있습니다. 시스템은 장치 및 동적 아일랜드 지원 여부에 따라 다른 방식으로 실시간 활동 업데이트를 사용자에게 알려줍니다.
>




**Avoid displaying sensitive information in a Live Activity.** A Live Activity is visually prominent and could be viewed by casual observers. If the information you need to provide refers to sensitive items, display an innocuous summary and let people tap the Live Activity to get more information in your app.
> 실시간 활동에는 중요한 정보가 표시되지 않도록 합니다. 실시간 활동은 시각적으로 두드러지며 일반 관찰자가 볼 수 있습니다. 제공해야 하는 정보가 중요한 항목을 참조하는 경우 악의 없는 요약을 표시하고 사람들이 실시간 활동을 눌러 앱에서 더 많은 정보를 얻을 수 있도록 합니다.
>




**Avoid using a Live Activity to display ads or promotions.** Live Activities help people stay informed about ongoing events and tasks, so it’s important to display only information that’s related to those events and tasks.
> 라이브 활동은 진행 중인 이벤트와 작업에 대한 정보를 제공하므로 이러한 이벤트와 작업과 관련된 정보만 표시하는 것이 중요합니다.
>




**Give people control over beginning and ending Live Activities.** For example, to help people end a Live Activity before the task or event ends, provide buttons to stop or cancel a Live Activity in the linked view in your app. Although it’s also a good idea to provide a button people can use to start a Live Activity from within your app, there are some situations in which people are likely to expect a Live Activity to start automatically. For example, if people use your app to start a task or event — such as ordering food for delivery or making a rideshare request — it makes sense to automatically initiate a Live Activity as soon as a person places an order or makes a request. In Settings, people can turn off Live Activities for your app, so it’s important to avoid surprising people by starting a Live Activity they don’t expect.
> 사용자에게 실시간 활동 시작 및 종료에 대한 제어 권한을 부여합니다. 예를 들어, 작업 또는 이벤트가 끝나기 전에 실시간 활동을 종료하려면 앱의 연결된 보기에서 실시간 활동을 중지하거나 취소할 수 있는 단추를 제공합니다. 앱 내에서 라이브 활동을 시작하는 데 사용할 수 있는 단추를 제공하는 것도 좋지만, 라이브 활동이 자동으로 시작될 것으로 예상되는 상황도 있습니다. 예를 들어, 사람들이 앱을 사용하여 배달 음식 주문 또는 승차 공유 요청과 같은 작업이나 이벤트를 시작하는 경우, 사용자가 주문을 하거나 요청을 하는 즉시 라이브 활동을 자동으로 시작하는 것이 좋습니다. 설정에서 사용자는 앱의 라이브 활동을 끌 수 있으므로 예상치 못한 라이브 활동을 시작하여 사람들을 놀라게 하지 않도록 하는 것이 중요합니다.
>




**Make sure tapping your Live Activity opens your app at the right location.** When people tap a Live Activity to open your app, take them directly to details and actions related to it — don’t require them to navigate to the relevant screen. For developer guidance on SwiftUI views that can deep link to specific screens in your app, see [Link](https://developer.apple.com/documentation/swiftui/link) and [widgetURL(`_:`)](https://developer.apple.com/documentation/WidgetKit/DynamicIsland/widgetURL(_:)).
> 실시간 활동을 누르면 올바른 위치에 앱이 열립니다. 사람들이 실시간 활동을 눌러 앱을 열 때 해당 앱과 관련된 세부 정보와 작업으로 직접 이동합니다. 해당 화면으로 이동할 필요는 없습니다. Swift에 대한 개발자 지침을 참조하십시오.앱의 특정 화면에 심층 링크할 수 있는 UI 보기, 링크 및 위젯 참조URL(`_:`).
>




**Consider removing your Live Activity from the Lock Screen after it ends.** In the Dynamic Island, the system immediately removes a Live Activity when it ends. By default, the system shows a Live Activity on the Lock Screen for up to four hours after it ends to give people time to view its final content update. If the outcome of your Live Activity is only relevant for a shorter time, tell the system to dismiss it at a specific time within the four-hour window or immediately after it ends. For example, a rideshare app might choose to display a summary of the ride in the Live Activity on the Lock Screen for 15 minutes after the ride ends so people can view the final fare.
> Dynamic Island에서는 라이브 활동이 종료되면 즉시 라이브 활동을 잠금 화면에서 제거합니다. 기본적으로 시스템은 종료 후 최대 4시간 동안 잠금 화면에 라이브 활동을 표시하여 사용자가 최종 콘텐츠 업데이트를 볼 수 있는 시간을 제공합니다. 라이브 활동의 결과가 더 짧은 시간 동안만 관련이 있는 경우, 시스템에 4시간 이내의 특정 시간에 또는 종료 직후에 종료하도록 지시합니다. 예를 들어, 승차 공유 앱은 승차 종료 후 15분 동안 잠금 화면에 승차 요약을 표시하여 사람들이 최종 요금을 볼 수 있도록 선택할 수 있습니다.
>




# **Designing useful Live Activities**

**Ensure unified information and design of the compact presentations in the Dynamic Island.** The TrueDepth camera separates the compact leading and compact trailing presentations of your Live Activity, but the contents of both should read as a single piece of information, and tapping either presentation should take people to the same screen in your app. Consider using color to help reinforce the relationship of content like text and icons in the two compact presentations.
> Dynamic Island에서 컴팩트한 프레젠테이션의 통일된 정보와 디자인을 보장합니다. TrueDepth 카메라는 라이브 활동의 컴팩트한 선행 프레젠테이션과 컴팩트한 후행 프레젠테이션을 구분하지만 둘 다의 내용은 단일 정보로 읽어야 하며, 두 프레젠테이션 중 하나를 탭하면 사람들이 앱의 동일한 화면으로 이동합니다.p. 두 개의 컴팩트한 프레젠테이션에서 텍스트와 아이콘과 같은 내용의 관계를 강화하기 위해 색상을 사용하는 것을 고려해 보십시오.
>




**Create consistent layouts between compact and expanded presentations.** The expanded presentation is an enlarged version of the compact presentation. Ensure that information and layouts expand predictably when the Live Activity transitions from compact to expanded presentation.
> 소형 및 확장된 프리젠테이션 사이에 일관된 레이아웃을 만듭니다. 확장된 프리젠테이션은 소형 프리젠테이션의 확대된 버전입니다. 실시간 활동이 소형에서 확장된 프리젠테이션으로 전환될 때 정보와 레이아웃이 예측 가능하게 확장되도록 합니다.
>




**Consider using a consistent design in both Lock Screen and expanded presentations.** When you use a consistent design approach in both presentations, you help people become familiar with your content and learn how to track an event’s or task’s progress in different locations.
> 잠금 화면과 확장된 프리젠테이션 모두에서 일관된 디자인을 사용하는 것을 고려해 보십시오. 두 프리젠테이션 모두에서 일관된 디자인 접근 방식을 사용하면 사람들이 사용자의 콘텐츠에 익숙해지도록 돕고 다른 위치에서 이벤트 또는 작업의 진행률을 추적하는 방법을 배울 수 있습니다.
>




**Adapt to different screen sizes and Live Activity presentations.** Live Activities scale to adapt to the screen sizes of different devices. Ensure your Live Activity looks great on every device by supplying content at appropriate sizes. As you create layouts and assets for various devices and scale factors, use the values listed in [Specifications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities#specifications) for guidance.
> 다양한 화면 크기와 실시간 활동 프레젠테이션에 적응합니다. 실시간 활동은 다양한 장치의 화면 크기에 맞게 확장됩니다. 적절한 크기의 콘텐츠를 제공하여 모든 장치에서 라이브 활동을 멋지게 보이도록 합니다. 다양한 장치 및 축척 계수에 대한 레이아웃 및 자산을 생성할 때는 사양에 나열된 값을 지침으로 사용하십시오.
>




**Consider carefully before using a custom background color and opacity on the Lock Screen.** If you set a background color or image for Live Activities that appear on the Lock Screen, test colors to be sure they offer enough contrast — especially tint colors on Always-On display with reduced luminance. Note that you can’t choose a custom background color for Live Activity presentations that appear in the Dynamic Island. However, you can apply a custom tint color for text, symbols, and a border that surrounds the Dynamic Island. For developer guidance, see [Displaying live data with Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities).
> 잠금 화면에서 사용자 지정 배경색과 불투명도를 사용하기 전에 신중하게 고려하십시오. 잠금 화면에 나타나는 실시간 활동의 배경색이나 이미지를 설정하는 경우 색상을 테스트하여 충분한 대비를 제공하는지 확인하십시오. 특히 밝기가 감소된 상시 작동 디스플레이의 틴트 색상을 테스트합니다. 동적 섬에 나타나는 실시간 활동 프레젠테이션의 사용자 정의 배경색은 선택할 수 없습니다. 그러나 동적 섬을 둘러싸는 텍스트, 기호 및 테두리에 사용자 정의 색조를 적용할 수 있습니다. 개발자 지침은 라이브 활동으로 라이브 데이터 표시를 참조하십시오.
>




**Coordinate the corner radius of your content with the corner radius of the Live Activity.** Margins between content items and the Live Activity edge need to be consistent. To ensure that your content looks good within a Live Activity’s rounded corners, use a SwiftUI container to apply the correct corner radius. For developer guidance, see [ContainerRelativeShape](https://developer.apple.com/documentation/swiftui/containerrelativeshape).
> 내용의 모서리 반지름을 실시간 활동의 모서리 반지름과 조정합니다. 내용 항목과 실시간 활동 가장자리 사이의 여백이 일정해야 합니다. 라이브 활동의 둥근 모서리 안에서 콘텐츠가 잘 보이도록 하려면 Swift를 사용합니다.올바른 모서리 반지름을 적용하기 위한 UI 컨테이너입니다. 개발자 지침은 컨테이너 상대 모양을 참조하십시오.
>




**In general, use standard margins to ensure your content is legible.** For the expanded and Lock Screen presentations, the standard margin width is 20 points. In some cases — such as for graphics and buttons — you might need to use tighter margins to avoid crowding edges or creating a cluttered appearance. For developer guidance, see [padding(`_:`_:)](https://developer.apple.com/documentation/swiftui/view/padding(_:_:)).
> 일반적으로 내용이 읽기 쉽도록 표준 여백을 사용하십시오. 확장 및 잠금 화면 프레젠테이션의 경우 표준 여백 폭은 20포인트입니다. 그래픽 및 단추와 같은 경우 가장자리가 혼잡하거나 모양이 흐트러지지 않도록 여백을 더 좁게 사용해야 할 수도 있습니다. 개발자 지침은 패딩(`_:`_:)을 참조하십시오.
>




**Choose colors that work well on a personalized Lock Screen.** People customize their Lock Screen with wallpaper, custom tint colors, and widgets. To make your Live Activity fit a custom Lock Screen aesthetic while remaining legible, apply custom tint colors and opacity sparingly.
> 사용자 지정된 잠금 화면에서 잘 작동하는 색을 선택하십시오. 사람들은 배경화면, 사용자 지정 색조 및 위젯을 사용하여 잠금 화면을 사용자 지정합니다. 실시간 활동을 사용자 지정 잠금 화면에 맞게 표시하면서도 읽기 쉽도록 하려면 사용자 지정 색조 색상과 불투명도를 사용하지 마십시오.
>




**Support Dark Mode and Always-On display.** A Live Activity adapts its colors to look great in both the light and dark appearances and on Always-On display with reduced luminance. For guidance, see [Dark Mode](../foundations/dark-mode) and [Always On](../technologies/always-on); for developer guidance, see [About asset catalogs](https://help.apple.com/xcode/mac/current/#/dev10510b1f7).
> Dark Mode(다크 모드) 및 Always-On 디스플레이를 지원합니다. Live Activity(실시간 활동)는 밝기와 어두운 모양 모두에서 보기 좋게 보이도록 색상을 조정하고 휘도를 낮춥니다. 자세한 내용은 다크 모드 및 항상 켜져 있음을 참조하고, 개발자 지침은 자산 카탈로그 정보를 참조하십시오.
>




**Use animations sparingly, and only to bring attention to content updates.** Live Activities use a subset of system animations, but the system doesn’t perform animations on Always-On display with reduced luminance. To learn which animations are available, see [Animate content updates](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Animate-content-updates).
> 실시간 활동에서는 시스템 애니메이션의 일부를 사용하지만 시스템에서 애니메이션을 수행하지 않고 밝기가 감소합니다. 사용 가능한 애니메이션에 대한 자세한 내용은 콘텐츠 업데이트 애니메이션을 참조하십시오.
>




# **Platform considerations**

*Not supported in iPadOS, macOS, tvOS, or watchOS.*
> iPadOS, macOS, tvOS 또는 watch에서 지원되지 않음운영 체제
>




# **Specifications**

# **The Dynamic Island**

The Dynamic Island uses a corner radius of 44 points, and its rounded corner shape matches the TrueDepth camera.
> Dynamic Island는 44개의 모서리 반지름을 사용하며, 둥근 모서리 모양이 TrueDepth 카메라와 일치합니다.
>




| Presentation type | Device | Dynamic Island width (points) |
| --- | --- | --- |
| Compact or minimal | iPhone 14 Pro Max | 250 |
|  | iPhone 14 Pro | 230 |
| Expanded | iPhone 14 Pro Max | 408 |
|  | iPhone 14 Pro | 371 |

# **Live Activity sizes**

All values listed in the table below are in points.
> 아래 표에 나열된 모든 값은 점 단위입니다.
>




| Screen dimensions (portrait) | Compact leading | Compact trailing | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen |
| --- | --- | --- | --- | --- | --- |
| 430x932 | 62.33x36.67 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 |
| 393x852 | 52.33x36.67 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 |

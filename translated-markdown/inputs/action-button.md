# **[inputs] action-button**

## The Action button can enable specific actions in workout apps running in watchOS 9 and later on Apple Watch Ultra.
> Action 버튼은 watch에서 실행되는 운동 앱에서 특정 작업을 활성화할 수 있습니다.Apple Watch Ultra의 OS 9 이상.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-action-button-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-action-button-intro_2x.png)

When wearing Apple Watch Ultra, people can use the Action button to easily start or progress through functions in apps that support Workout, Shortcuts, and Dive actions. The Action button can also give people quick access to system-provided functionality, like turning Flashlight on and off or marking a Compass Waypoint. People choose an initial function for the Action button when they set up their device; later, they can adjust this choice in Settings.
> 애플워치 울트라를 착용하면 액션 버튼을 이용해 워크아웃, 바로가기, 다이브 동작 등을 지원하는 앱의 기능을 통해 쉽게 시작하거나 진행할 수 있다. 작업 단추를 사용하면 사람들이 플래시 라이트를 켜고 끄거나 나침반 경유지를 표시하는 등 시스템에서 제공하는 기능에 빠르게 액세스할 수 있습니다. 사용자는 장치를 설정할 때 작업 단추의 초기 기능을 선택합니다. 나중에 설정에서 이 선택을 조정할 수 있습니다.
>




Depending on the actions you support, people can choose the function that occurs when they press the Action button for the first time and — in some cases — they can choose the actions that occur on subsequent presses. For example, when an app supports Shortcuts, people simply choose the Shortcut they want the Action button to initiate, making additional button presses unnecessary. In contrast, a Workout app might let people start a triathlon with the first button press and switch to another segment with a subsequent press.
> 사용자가 지원하는 작업에 따라 작업 단추를 처음 누를 때 발생하는 기능을 선택할 수 있으며, 경우에 따라 이후 누를 때 발생하는 작업을 선택할 수도 있습니다. 예를 들어, 앱이 바로 가기를 지원하는 경우 사용자는 수행 단추를 시작할 바로 가기를 선택하기만 하면 되므로 추가 단추를 누를 필요가 없습니다. 대조적으로, 워크아웃 앱은 사람들이 첫 번째 버튼을 누른 상태에서 트라이애슬론을 시작하고 그 다음 버튼을 누른 상태에서 다른 세그먼트로 전환하도록 할 수 있다.
>




**IMPORTANT**Apps don’t respond when people press and hold the Action button because watchOS reserves this interaction for the emergency SOS feature.
> 중요한 앱은 사람들이 작업 버튼을 길게 눌러도 응답하지 않습니다. 왜냐하면 보기 때문입니다.OS는 비상 SOS 기능을 위해 이 상호 작용을 예약합니다.
>




# **Best practices**

**Offer a set of essential actions from which people can choose the one they want to initiate with the first button press.** For example, if your app helps people track their progress during a triathlon, the “Start Race” action might be the one most people want to initiate when they first press the Action button. Avoid offering an Action button action that merely opens your app; your app icon and complications already give people quick ways to open your app.
> 예를 들어, 3종 경기 중에 사람들이 진행 상황을 추적하는 데 도움이 되는 앱을 사용하면 대부분의 사람들이 동작 버튼을 처음 누를 때 "시작 경주" 동작을 시작하고 싶을 수 있습니다. 단순히 앱을 여는 작업 단추 동작을 제공하지 마십시오. 앱 아이콘과 복잡성은 이미 사람들이 앱을 빠르게 열 수 있는 방법을 제공합니다.
>




**Consider offering a secondary function that supports or advances the primary action people choose.** People often use the Action button without looking at the screen, so a subsequent button press needs to flow logically from the first press, while also making sense in the current context. If your app supports Workout or Dive actions, consider designing a simple, intuitive secondary function that people can easily learn and remember. Consider carefully before you offer more than one secondary function, because doing so can increase people’s cognitive load and make your app seem harder to use.
> 사람들이 선택하는 주요 행동을 지원하거나 발전시키는 보조 기능을 제공하는 것을 고려해보라. 사람들은 종종 화면을 보지 않고 액션 버튼을 사용하기 때문에, 이후의 버튼 누르기는 첫 번째 누르는 것에서부터 논리적으로 흐를 필요가 있고, 동시에 현재 상황에서도 의미가 있다. 만약 당신의 앱이 운동이나 다이빙 동작을 지원한다면, 사람들이 쉽게 배우고 기억할 수 있는 간단하고 직관적인 보조 기능을 설계하는 것을 고려해보세요. 두 가지 이상의 보조 기능을 제공하기 전에 신중하게 고려하십시오. 그렇게 하면 사람들의 인지 부하가 증가하고 앱을 사용하기 어려워 보일 수 있기 때문입니다.
>




**For each action you support, write a short label that succinctly describes it.** People view your labels when they visit Settings to choose the action they want the Action button to initiate. Using [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64), create a label that begins with a verb, uses present tense, and avoids including articles and prepositions. For example, use “Start Race” instead of “Started Race” or “Start the Race.”
> 지원하는 각 작업에 대해 간략하게 설명하는 레이블을 작성하십시오. 사람들은 설정을 방문하여 [수행] 단추를 사용하여 시작할 작업을 선택할 때 레이블을 봅니다. 제목 스타일 대문자화를 사용하여 동사로 시작하고 현재 시제를 사용하며 기사와 전치사를 포함하지 않는 레이블을 만듭니다. 예를 들어, "시작 경주" 또는 "시작 경주" 대신 "시작 경주"를 사용합니다.
>




**Pause the current function when people press the Action and side buttons together.** The exception is in a diving app where pausing a dive could be dangerous to the diver, causing them to lose track of their depth or not understand how long they’ve been underwater. Unless pausing the current function would result in a negative experience, be sure to meet people’s expectations by letting them pause their current activity when they press both buttons at the same time.
> 사람들이 액션과 사이드 버튼을 함께 누를 때 현재 기능을 일시 중지합니다. 예외는 다이빙 앱에서 다이빙을 일시 중지하는 것은 잠수부에게 위험할 수 있으며, 그들의 깊이를 추적하지 못하거나 그들이 얼마나 오랫동안 물속에 있었는지 이해하지 못하게 할 수 있습니다. 현재 기능을 일시 중지하는 것이 부정적인 경험으로 이어지지 않는 한, 두 버튼을 동시에 누를 때 현재 활동을 일시 중지하도록 함으로써 사람들의 기대에 부응해야 합니다.
>




**Prefer using subsequent button presses to enable additional functionality; avoid offering a “stop” or “conclude” function.** If you need to let people stop their main task — as opposed to pausing the current function — offer this option within your interface instead.
> 추가 기능을 활성화하기 위해 후속 버튼 누르기를 사용하는 것을 선호합니다. "중지" 또는 "종료" 기능을 제공하지 마십시오. 현재 기능을 일시 중지하는 대신 사용자가 기본 작업을 중지하도록 하려면 인터페이스 내에서 이 옵션을 제공하십시오.
>




**Prefer letting the system show people how to use the Action button with your app.** When you support the Action button, the system automatically helps people configure it to initiate one of your app’s actions. If necessary, you can provide content that teaches people how to use the Action button with your app, but be sure to avoid creating content that repeats or conflicts with the system-provided flow.
> 사용자가 작업 단추를 앱과 함께 사용하는 방법을 시스템에서 사용자에게 보여주는 것을 선호합니다. 작업 단추를 지원하면 시스템은 자동으로 사용자가 앱의 작업 중 하나를 시작하도록 구성하도록 도와줍니다. 필요한 경우 앱에서 작업 단추를 사용하는 방법을 알려주는 콘텐츠를 제공할 수 있지만 시스템에서 제공하는 흐름과 반복되거나 충돌하는 콘텐츠는 만들지 않도록 해야 합니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에서는 지원되지 않습니다.
>




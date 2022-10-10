# **[patterns] feedback**

# Feedback helps people know what’s happening, discover what they can do next, understand the results of actions, and avoid mistakes.
> 피드백은 사람들이 무슨 일이 일어나고 있는지 알고, 다음에 무엇을 할 수 있는지 발견하고, 행동의 결과를 이해하고, 실수를 피하도록 도와줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-feedback-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-feedback-intro-dark_2x.png)

Providing clear, consistent feedback as people interact with your app or game can make it feel intuitive and encourage deeper exploration. Feedback can communicate several different things, such as:
> 사람들이 당신의 앱이나 게임과 상호작용할 때 명확하고 일관된 피드백을 제공하면 직관적으로 느낄 수 있고 더 깊은 탐색을 장려할 수 있다. 피드백은 다음과 같은 다양한 정보를 전달할 수 있습니다.
>




- The current status of something
- >  현재 상태

- The success or failure of an important task or action
- >  중요한 작업 또는 작업의 성공 또는 실패

- A warning about an action that can have negative consequences
- >  부정적인 결과를 초래할 수 있는 조치에 대한 경고

- An opportunity to correct a mistake or problematic situation
- >  실수나 문제가 있는 상황을 바로잡을 수 있는 기회


The most effective feedback tends to match the significance of the information to the way it’s delivered. For example, it often works well to display status information in a passive way so that people can view it when they need it. In contrast, a warning about possible data loss needs to interrupt people so they have a chance to avoid the problem.
> 가장 효과적인 피드백은 정보가 전달되는 방식과 정보의 중요성을 일치시키는 경향이 있습니다. 예를 들어, 사람들이 필요할 때 볼 수 있도록 상태 정보를 수동적으로 표시하는 것이 잘 작동하는 경우가 많습니다. 이와는 대조적으로, 데이터 손실 가능성에 대한 경고는 사람들이 문제를 피할 수 있도록 방해할 필요가 있다.
>




# **Best practices**

**Make sure all feedback is accessible.** When you use multiple ways to provide feedback, you reach more people and give them the opportunity to receive the feedback in ways that work for them. For example, when you provide feedback using color, text, sound, and haptics, people can receive it whether they silence their device, look away from the screen, or use VoiceOver. (For guidance on providing haptic feedback, see [Playing haptics](../patterns/playing-haptics).)
> 모든 피드백에 액세스할 수 있는지 확인합니다. 피드백을 제공하기 위해 여러 가지 방법을 사용하면 더 많은 사용자에게 연락하고 사용자에게 적합한 방식으로 피드백을 받을 수 있는 기회를 제공할 수 있습니다. 예를 들어 색상, 텍스트, 사운드 및 햅틱을 사용하여 피드백을 제공할 때 사용자가 단말기를 종료하거나 화면에서 눈을 돌리거나 VoiceOver를 사용하든 상관없이 피드백을 받을 수 있습니다(햅틱 피드백 제공에 대한 지침은 햅틱 재생을 참조하십시오.
>




**Consider integrating status feedback into your interface.** When status feedback is available near the items it describes, people get important information without having to take action or leave their current context. For example, Mail in iOS and iPadOS describes the most recent update and displays the number of unread messages in the toolbar of the mailbox screen, making the information unobtrusive but easy for people to check when they’re interested.
> 상태 피드백을 인터페이스에 통합하는 것을 고려해 보십시오. 상태 피드백이 설명된 항목 근처에서 사용 가능한 경우, 사람들은 조치를 취하거나 현재 상황을 벗어날 필요 없이 중요한 정보를 얻습니다. 예를 들어 iOS 및 iPadOS의 메일은 가장 최근의 업데이트를 설명하고 읽지 않은 메시지 수를 사서함 화면의 도구 모음에 표시하므로 눈에 띄지 않지만 관심 있을 때 쉽게 확인할 수 있습니다.
>




**Use alerts to deliver critical — and ideally actionable — information.** By design, alerts disrupt the current context, so you need to match the importance of the information to the level of interruption. Alerts can lose their impact if you use them too often or to deliver unimportant information. For guidance, see [Alerts](../components/presentation/alerts).
> 경고를 사용하여 중요하며 이상적으로 실행 가능한 정보를 제공합니다. 설계상 알림은 현재 컨텍스트를 중단시키므로 정보의 중요도를 중단 수준과 일치시켜야 합니다. 알림 기능을 너무 자주 사용하거나 중요하지 않은 정보를 전달하면 알림의 영향을 잃을 수 있습니다. 자세한 내용은 경고를 참조하십시오.
>




**Warn people when they initiate a task that can cause data loss that’s unexpected and irreversible.** In contrast, don’t warn people when data loss is the expected result of their action. For example, the Finder doesn’t warn people every time they throw away a file because deleting the file is the expected result.
> 예기치 않고 되돌릴 수 없는 데이터 손실을 초래할 수 있는 작업을 시작할 때 사용자에게 경고합니다. 이와는 대조적으로, 데이터 손실이 행동의 예상 결과일 때는 사람들에게 경고하지 마십시오. 예를 들어, 파일을 삭제하는 것이 예상된 결과이기 때문에 Finder는 파일을 버릴 때마다 사용자에게 경고하지 않습니다.
>




**When it makes sense, confirm that a significant action or task has completed.** For example, people appreciate getting feedback that confirms a successful Apple Pay transaction. It’s generally best to reserve this type of confirmation for activities that are sufficiently important — because people typically expect their action or task to succeed, they only need to know when it doesn’t.
> 타당하면 중요한 작업이나 작업이 완료되었는지 확인합니다. 예를 들어, 사람들은 성공적인 애플 페이 거래를 확인하는 피드백을 받는 것에 감사한다. 일반적으로 충분히 중요한 활동에 대해서는 이러한 확인 유형을 예약하는 것이 가장 좋습니다. 사람들은 일반적으로 자신의 행동이나 작업이 성공하기를 기대하지만 성공하지 못할 때만 알면 되기 때문입니다.
>




**Show people when a command can't be carried out and help them understand why.** For example, if people request directions without specifying a destination, Maps tells them that it can't provide directions to and from the same location.
> 명령이 수행되지 않을 때 사람들에게 보여주고 그 이유를 이해하도록 도와줍니다. 예를 들어, 사람들이 목적지를 지정하지 않고 길을 요청하면, 지도는 그들에게 같은 위치로 오고 가는 길을 제공할 수 없다고 알려준다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항 없음.
>




# **watchOS**

**Avoid displaying an indeterminate progress indicator — such as a loading indicator — in a watchOS app.** An animated indicator can make people think they need to continue paying attention to the display, which isn’t a good user experience. To provide a better experience, reassure people that they’ll receive a notification when the process completes.
> 시계에 로드 표시기와 같은 불확실한 진행 표시기를 표시하지 않도록 합니다.OS 앱. 애니메이션 표시기는 사람들이 디스플레이에 계속 주의를 기울여야 한다고 생각하게 만들 수 있는데, 이는 좋은 사용자 경험이 아닙니다. 더 나은 환경을 제공하기 위해 프로세스가 완료될 때 통지를 받을 것이라고 사람들에게 안심시킵니다.
>




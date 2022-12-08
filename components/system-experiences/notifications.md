# **[components-status] notifications**

## A notification gives people timely, high-value information they can understand at a glance.
> 알림은 사람들이 한 눈에 이해할 수 있는 시기적절하고 가치 있는 정보를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/notification-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/notification-intro-dark_2x.png)

Before you can send any notifications to people, you have to get their consent (for developer guidance, see [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications)). After agreeing, people generally use settings to specify the styles of notification they want to receive, and to specify delivery times for notifications that have different levels of urgency. To learn more about the ways people can customize the notification experience, see [Managing notifications](../patterns/managing-notifications).
> 사용자에게 알림을 보내기 전에 먼저 사용자의 동의를 얻어야 합니다(개발자 지침은 알림 사용 권한 요청 참조). 동의한 후 사용자는 일반적으로 설정을 사용하여 수신할 통지 유형을 지정하고 긴급도 수준이 다른 통지의 배달 시간을 지정합니다. 사용자가 통지 환경을 사용자 정의할 수 있는 방법에 대한 자세한 내용은 통지 관리를 참조하십시오.
>




# **Anatomy**

Depending on the platform, a notification can use various styles, such as:
> 플랫폼에 따라 알림은 다음과 같은 다양한 스타일을 사용할 수 있습니다.
>




- A banner on a Lock Screen, Home Screen, or desktop
- >  잠금 화면, 홈 화면 또는 바탕 화면의 배너

- A badge on an app icon
- >  앱 아이콘의 배지

- An item in Notification Center
- >  Notification Center의 항목


In addition, a notification related to direct communication — like a phone call or message — can provide an interface that’s distinct from noncommunication notifications, featuring prominent contact images (or *avatars*) and group names instead of the app icon.
> 또한 전화 또는 메시지와 같은 직접 통신과 관련된 알림은 앱 아이콘 대신 눈에 띄는 연락처 이미지(또는 아바타)와 그룹 이름을 특징으로 하는 비통신 알림과 구별되는 인터페이스를 제공할 수 있습니다.
>




# **Best practices**

**Provide concise, informative notifications.** People enable notifications to get quick updates, so focus on providing valuable information succinctly.
> 간결하고 유익한 알림을 제공합니다. 사람들은 알림을 사용하여 빠른 업데이트를 받을 수 있으므로 중요한 정보를 간결하게 제공하는 데 집중합니다.
>




**Avoid sending multiple notifications for the same thing, even if someone hasn’t responded.** People attend to notifications at their convenience. If you send multiple notifications for the same thing, you fill up Notification Center, and people may turn off all notifications from your app.
> 다른 사용자가 응답하지 않은 경우에도 동일한 항목에 대해 여러 개의 알림을 보내지 않도록 합니다. 동일한 항목에 대해 여러 개의 알림을 보내면 알림 센터가 가득 차게 되고, 사람들이 앱에서 모든 알림을 끌 수 있습니다.
>




**Avoid sending a notification that tells people to perform specific tasks within your app.** If it makes sense to enable simple tasks that people can perform without opening your app, you can provide [notification actions](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications#notification-actions). Otherwise, avoid telling people what to do because it’s hard for people to remember such instructions after they dismiss the notification.
> 앱 내에서 특정 작업을 수행하라는 알림을 보내지 마십시오. 앱을 열지 않고도 사용자가 수행할 수 있는 간단한 작업을 사용할 수 있는 경우 알림 작업을 제공할 수 있습니다. 그렇지 않으면 통지를 무시한 후에는 이러한 지시사항을 기억하기 어렵기 때문에 사용자에게 지시하지 마십시오.
>




**Use an alert — not a notification — to display an error message.** People are familiar with both alerts and notifications, so you don’t want to cause confusion by using the wrong component. For guidance, see [Alerts](../components/presentation/alerts).
> 오류 메시지를 표시하려면 알림이 아닌 알림을 사용하십시오. 알림과 알림 모두에 익숙하기 때문에 잘못된 구성 요소를 사용하여 혼란을 초래하지는 않습니다. 자세한 내용은 경고를 참조하십시오.
>




**Handle notifications gracefully when your app is in the foreground.**Your app’s notifications don’t appear onscreen when your app is in the front, but your app still receives the information. In this scenario, present the information in a way that’s discoverable but not distracting or invasive, such as incrementing a badge or subtly inserting new data into the current view. For example, when a new message arrives in a mailbox that people are currently viewing, Mail simply adds it to the list of unread messages because sending a notification about it would be unnecessary and distracting.
> 앱이 전면에 있을 때 알림을 우아하게 처리합니다.앱이 맨 앞에 있을 때 앱의 알림이 화면에 나타나지 않지만, 앱은 여전히 정보를 수신합니다. 이 시나리오에서는 배지를 늘리거나 현재 보기에 새 데이터를 미묘하게 삽입하는 등 검색 가능하지만 주의를 산만하게 하거나 침입하지 않는 방식으로 정보를 표시합니다. 예를 들어, 새 메시지가 사용자가 현재 보고 있는 사서함에 도착하면 메일은 메시지에 대한 통지를 발송할 필요가 없고 주의를 분산시킬 수 있으므로 읽지 않은 메시지 목록에 메시지를 추가합니다.
>




**Avoid including sensitive, personal, or confidential information in a notification.** You can’t predict what people will be doing when they receive a notification, so it’s essential to avoid including private information that could be visible to others on the device screen.
> 알림에 중요한 정보, 개인 정보 또는 기밀 정보를 포함하지 않도록 합니다. 알림을 받을 때 사용자가 어떤 작업을 수행할지 예측할 수 없으므로 장치 화면에서 다른 사람이 볼 수 있는 개인 정보를 포함하지 않도록 해야 합니다.
>




# **Content**

When a notification includes a title, the system displays it at the top where it’s most visible. In a notification related to direct communication, the system automatically displays the sender’s name in the title area; in a noncommunication notification, the system displays your app name if you don’t provide a title.
> 알림에 제목이 포함된 경우 시스템은 알림을 가장 잘 볼 수 있는 맨 위에 표시합니다. 직접 통신과 관련된 알림에서는 보낸 사람의 이름이 제목 영역에 자동으로 표시되고, 비통신 알림에서는 제목을 제공하지 않으면 앱 이름이 표시됩니다.
>




**Create a short title if it provides context for the notification content.**Prefer brief titles that people can read at a glance, especially on Apple Watch, where space is limited. When possible, take advantage of the prominent notification title area to provide useful information, like a headline, event name, or email subject. If you can only provide a generic title for a noncommunication notification — like New Document — it can be better to let the system display your app name instead. Use title-style capitalization and no ending punctuation.
> 통지 내용에 대한 컨텍스트를 제공하는 경우 짧은 제목을 작성합니다.특히 공간이 제한된 애플워치에서 사람들이 한눈에 읽을 수 있는 짧은 제목을 선호한다. 가능하면 제목, 이벤트 이름 또는 전자 메일 제목과 같은 유용한 정보를 제공하기 위해 눈에 띄는 통지 제목 영역을 활용하십시오. 새 문서와 같은 비통신 통지에 대한 일반 제목만 제공할 수 있는 경우 시스템에 앱 이름을 대신 표시하도록 하는 것이 좋습니다. 제목 스타일의 대소문자를 사용하고 끝맺음 구두점을 사용하지 마십시오.
>




**Write succinct, easy-to-read notification content.** Use complete sentences, sentence case, and proper punctuation, and don’t truncate your message — the system does this automatically when necessary.
> 간결하고 읽기 쉬운 알림 내용을 작성합니다. 완전한 문장, 문장 대소문자 및 적절한 구두점을 사용하고 메시지를 잘라내지 마십시오. 시스템은 필요할 때 자동으로 이 작업을 수행합니다.
>




**Provide generically descriptive text to display when notification previews aren’t available.** In Settings, people can choose to hide notification previews for all apps. In this situation, the system shows only your app icon and the default title *Notification*. To give people sufficient context to know whether they want to view the full notification, write body text that succinctly describes the notification content without revealing too many details, like “Friend request,” “New comment,” “Reminder,” or “Shipment” (for developer guidance, see [hiddenPreviewsBodyPlaceholder](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/2873736-hiddenpreviewsbodyplaceholder)). Use sentence-style capitalization for this text.
> 알림 미리 보기를 사용할 수 없는 경우 표시할 일반적인 설명 텍스트를 제공합니다. 설정에서 사용자는 모든 앱에 대한 알림 미리 보기를 숨기도록 선택할 수 있습니다. 이 경우 시스템에는 앱 아이콘과 기본 제목 알림만 표시됩니다. 전체 알림을 볼지 여부를 사람들이 알 수 있도록 충분한 컨텍스트를 제공하려면 "친구 요청", "새 의견", "주의사항" 또는 "발송"과 같이 너무 많은 세부 정보를 표시하지 않고 알림 내용을 간결하게 설명하는 본문 텍스트를 작성합니다(개발자 지침은 숨겨진 미리 보기 참조).본문 자리 표시자). 이 텍스트에는 문장 형식의 대소문자를 사용합니다.
>




**Avoid including your app name or icon.** The system automatically displays a large version of your app icon at the leading edge of each notification; in a communication notification, the system displays the sender’s contact image badged with a small version of your icon.
> 앱 이름이나 아이콘을 포함하지 마십시오. 시스템은 각 알림의 맨 앞 가장자리에 앱 아이콘의 큰 버전을 자동으로 표시합니다. 통신 알림에서 시스템은 아이콘의 작은 버전으로 표시된 보낸 사람의 연락처 이미지를 표시합니다.
>




**Consider providing a sound to supplement your notifications.** Sound can be a great way to distinguish your app’s notifications and get someone’s attention when they’re not looking at the screen. You can create a custom sound that coordinates with the style of your app or use a system-provided alert sound. If you use a custom sound, make sure it’s short, distinctive, and professionally produced. A notification sound can enhance the user experience, but don’t rely on it to communicate important information, because people may not hear it. Although people can also enable a vibration that accompanies alert sounds, you can’t enable such a vibration programmatically. For developer guidance, see [UNNotificationSound](https://developer.apple.com/documentation/usernotifications/unnotificationsound).
> 사운드는 앱의 알림을 구분하고 화면을 보지 않을 때 다른 사람의 주의를 끌 수 있는 좋은 방법은 사운드입니다. 앱 스타일에 맞춰 사용자 지정 사운드를 만들거나 시스템에서 제공하는 경고 사운드를 사용할 수 있습니다. 사용자 지정 사운드를 사용할 경우 짧고 독특하며 전문적으로 제작해야 합니다. 알림음은 사용자 경험을 향상시킬 수 있지만 사람들이 듣지 못할 수 있으므로 중요한 정보를 전달하기 위해 이 소리에 의존하지 마십시오. 사람들이 경보음을 동반하는 진동을 활성화할 수도 있지만, 프로그래밍 방식으로는 이러한 진동을 활성화할 수 없습니다. 개발자 지침은 UN 알림 사운드를 참조하십시오.
>




# **Notification actions**

A notification can present a customizable detail view that contains up to four buttons people use to perform actions without opening your app. For example, a Calendar event notification provides a Snooze button that postpones the event’s alarm for a few minutes. For developer guidance, see [Handling notifications and notification-related actions](https://developer.apple.com/documentation/usernotifications/handling_notifications_and_notification-related_actions).
> 알림은 사용자가 앱을 열지 않고 작업을 수행하는 데 사용하는 최대 4개의 단추를 포함하는 사용자 지정 가능한 세부 정보 보기를 제공할 수 있습니다. 예를 들어, 일정관리 이벤트 통지는 이벤트의 알람을 몇 분간 연기하는 중지 단추를 제공합니다. 개발자 지침은 알림 및 알림 관련 작업 처리를 참조하십시오.
>




**Provide beneficial actions that make sense in the context of your notification.** Prefer actions that let people perform common, time-saving tasks that eliminate the need to open your app. For each button, use a short, title-case term or phrase that clearly describes the result of the action. Don’t include your app name or any extraneous information in the button label, keep the text brief to avoid truncation, and take localization into account as you write it.
> 알림의 맥락에서 유용한 작업을 제공합니다. 앱을 열 필요가 없는 일반적인 시간 절약 작업을 수행할 수 있는 작업을 선호합니다. 각 단추에 대해 작업 결과를 명확하게 설명하는 짧은 제목 대소문자 용어 또는 구문을 사용합니다. 단추 레이블에 앱 이름이나 관련 없는 정보를 포함하지 말고, 잘리지 않도록 텍스트를 짧게 유지하고, 작성할 때 현지화를 고려하십시오.
>




**Avoid providing an action that merely opens your app.** When people tap a notification or its preview, they expect your app to open the relevant screen, so presenting an action button that does the same thing clutters the detail view and can be confusing.
> 사용자가 알림 또는 미리 보기를 누르면 해당 화면이 열리기 때문에 세부 정보 보기가 혼란스럽고 혼란스러울 수 있습니다.
>




**Prefer nondestructive actions.** If you must provide a destructive action, make sure people have enough context to avoid unintended consequences. The system gives a distinct appearance to the actions you identify as destructive.
> 파괴적이지 않은 행동을 선호한다. 파괴적인 행동을 제공해야 한다면, 사람들이 의도하지 않은 결과를 피할 수 있는 충분한 상황을 갖도록 해야 한다. 시스템은 사용자가 파괴적인 것으로 식별하는 작업을 뚜렷하게 보여줍니다.
>




**Provide a simple, recognizable interface icon for each notification action.** An interface icon reinforces an action’s meaning, helping people instantly understand what it does. The system displays your interface icon on the trailing side of the action title. When you use [SF Symbols](../foundations/sf-symbols), you can choose an existing symbol that represents your command or edit a related symbol to create a custom icon.
> 각 통지 작업에 대해 단순하고 인식 가능한 인터페이스 아이콘을 제공합니다. 인터페이스 아이콘은 작업의 의미를 강화하여 사용자가 작업을 즉시 이해할 수 있도록 도와줍니다. 시스템은 작업 제목의 뒷부분에 인터페이스 아이콘을 표시합니다. SF 기호를 사용할 때 명령을 나타내는 기존 기호를 선택하거나 관련 기호를 편집하여 사용자 지정 아이콘을 만들 수 있습니다.
>




# **Badging**

A badge is a small, filled oval containing a number that can appear on an app icon to indicate the number of unread notifications that are available. After people address unread notifications, the badge disappears from the app icon, reappearing when new notifications arrive. People can choose whether to allow an app to display badges in their notification settings.
> 배지는 앱 아이콘에 표시할 수 있는 번호가 포함된 채워진 작은 타원형으로, 사용 가능한 읽지 않은 알림 수를 나타냅니다. 사람들이 읽지 않은 알림을 수신인 지정하면 배지가 앱 아이콘에서 사라지고 새 알림이 도착하면 다시 나타납니다. 사용자는 앱이 알림 설정에 배지를 표시하도록 허용할지 여부를 선택할 수 있습니다.
>




**Use a badge only to show people how many unread notifications they have.** Don’t use a badge to convey numeric information that isn’t related to notifications, such as weather-related data, dates and times, stock prices, or game scores.
> 배지는 사람들에게 읽지 않은 알림의 수를 표시할 때만 사용합니다. 배지는 날씨 관련 데이터, 날짜 및 시간, 주가 또는 게임 점수와 같은 알림과 관련이 없는 숫자 정보를 전달할 때 사용하지 마십시오.
>




**Make sure badging isn’t the only method you use to communicate essential information.** People can turn off badging for your app, so if you rely on it to show people when there’s important information, people can miss the message. Always make sure that you make important information easy for people to find as soon as they open your app.
> 사람들은 앱에 대한 배깅을 해제할 수 있으므로 중요한 정보가 있을 때 사람들에게 보여주기 위해 사용하면 메시지를 놓칠 수 있습니다. 항상 중요한 정보를 사용자가 앱을 열자마자 쉽게 찾을 수 있도록 하십시오.
>




**Keep badges up to date.** Update your app’s badge as soon as people open the corresponding notifications. You don’t want people to think there are new notifications available, only to find that they’ve already viewed them all. Note that reducing a badge’s count to zero removes all related notifications from Notification Center.
> 배지를 최신 상태로 유지하고, 사람들이 해당 알림을 여는 즉시 앱의 배지를 업데이트하십시오. 사용자가 새 알림을 사용할 수 있다고 생각하지 않고 모든 알림을 이미 봤다는 사실만 알고 있으면 됩니다. 배지 수를 0으로 줄이면 Notification Center에서 모든 관련 통지가 제거됩니다.
>




**Avoid creating a custom image or component that mimics the appearance or behavior of a badge.** People can turn off notification badges if they choose, and will become frustrated if they have done so and then see what appears to be a badge.
> 배지의 모양이나 동작을 모방하는 사용자 지정 이미지 또는 구성 요소를 만들지 마십시오. 사용자가 원하는 경우 알림 배지를 끌 수 있으며, 사용자가 이를 해제한 다음 배지로 표시되는 것을 확인하면 사용자 지정이 취소됩니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항은 없습니다.
>




# **watchOS**

On Apple Watch, notifications occur in two stages: *short look* and *long look*. People can also view notifications in Notification Center.
> 애플 워치에서 알림은 쇼트 룩과 롱 룩의 두 단계로 발생한다. 또한 Notification Center에서 통지를 볼 수 있습니다.
>




You can help people have a great notification experience by designing app-specific assets and actions that are relevant on Apple Watch. If your watchOS app has an iPhone companion that supports notifications, watchOS can automatically provide default short-look and long-look interfaces if necessary.
> Apple Watch와 관련된 앱별 자산 및 작업을 설계하여 사용자가 우수한 알림 환경을 가질 수 있도록 지원할 수 있습니다. 네 시계라면OS 앱에는 알림, 워치를 지원하는 아이폰 동반자가 있습니다.OS는 필요한 경우 자동으로 기본 숏룩 및 롱룩 인터페이스를 제공할 수 있습니다.
>




### **Short looks**

A short look appears when the wearer’s wrist is raised and disappears when it’s lowered.
> 짧은 표정은 착용자의 손목이 위로 들어올릴 때 나타나고 아래로 내려갈 때 사라진다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications/images/notifications-short-looks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications/images/notifications-short-looks_2x.png)

**Avoid using a short look as the only way to communicate important information.** A short look appears only briefly, giving people just enough time to see what the notification is about and which app sent it. If your notification information is critical, make sure you deliver it in other ways, too.
> 짧은 모양을 중요한 정보를 전달하는 유일한 방법으로 사용하는 것을 피하십시오. 짧은 모양은 짧게만 표시되므로 알림의 내용과 보낸 앱을 확인할 수 있는 충분한 시간을 제공합니다. 알림 정보가 중요한 경우 다른 방법으로도 알림 정보를 전달해야 합니다.
>




**Keep privacy in mind.** Short looks are intended to be discreet, so it’s important to provide only basic information. Avoid including potentially sensitive information in the notification’s title.
> 짧은 외모는 신중하게 하기 위한 것이므로 기본적인 정보만 제공하는 것이 중요합니다. 통지 제목에 잠재적으로 중요한 정보가 포함되지 않도록 합니다.
>




### **Long looks**

Long looks provide more detail about a notification. If necessary, people can swipe vertically or use the Digital Crown to scroll a long look. After viewing a long look, people can dismiss it by tapping it or simply by lowering their wrist.
> 긴 모양은 알림에 대한 자세한 정보를 제공합니다. 필요한 경우, 사람들은 세로로 스와이프하거나 디지털 크라운을 사용하여 긴 모양을 스크롤할 수 있습니다. 길게 본 후에, 사람들은 그것을 두드리거나 단순히 손목을 내리는 것으로 그것을 없앨 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications/images/notifications-long-looks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications/images/notifications-long-looks_2x.png)

A custom long-look interface can be static or dynamic. The *static* interface lets you display a notification’s message along with additional static text and images. The *dynamic* interface gives you access to the notification’s full content and offers more options for configuring the appearance of the interface.
> 사용자 지정 롱 룩 인터페이스는 정적 또는 동적일 수 있습니다. 정적 인터페이스를 사용하여 추가 정적 텍스트 및 이미지와 함께 통지 메시지를 표시할 수 있습니다. 동적 인터페이스를 사용하면 알림의 전체 내용에 액세스할 수 있으며 인터페이스 모양을 구성하기 위한 추가 옵션을 제공합니다.
>




You can customize the content area for both static and dynamic long looks, but you can’t change the overall structure of the interface. The system-defined structure includes a *sash* at the top of the interface and a Dismiss button at the bottom, below all custom buttons.
> 정적 및 동적 긴 모양 모두에 대해 내용 영역을 사용자 정의할 수 있지만 인터페이스의 전체 구조를 변경할 수는 없습니다. 시스템 정의 구조에는 인터페이스 상단의 새시와 모든 사용자 정의 버튼 아래의 해제 버튼이 포함됩니다.
>




**Consider using a rich, custom long-look notification to let people get the information they need without launching your app.** You can use [SwiftUI](https://developer.apple.com/documentation/swiftui/animations) to create engaging, interruptible animations; alternatively, you can use [SpriteKit](https://developer.apple.com/documentation/spritekit) or [SceneKit](https://developer.apple.com/documentation/scenekit).
> 앱을 실행하지 않고도 사람들이 필요한 정보를 얻을 수 있도록 풍부한 사용자 지정 롱룩 알림을 사용하는 것을 고려해 보십시오. Swift를 사용할 수 있습니다.UI를 사용하여 매력적이고 중단 가능한 애니메이션을 만들 수 있습니다. 또는 SpriteKit 또는 SceneKit을 사용할 수도 있습니다.
>




**At the minimum, provide a static interface; prefer providing a dynamic interface too.** The system defaults to the static interface when the dynamic interface is unavailable, such as when there is no network or the iPhone companion app is unreachable. Be sure to create the resources for your static interface in advance and package them with your app.
> 최소한 정적 인터페이스를 제공합니다. 동적 인터페이스도 제공합니다. 네트워크가 없거나 iPhone 지원 앱에 연결할 수 없는 경우와 같이 동적 인터페이스를 사용할 수 없을 때 시스템은 기본적으로 정적 인터페이스를 사용합니다. 정적 인터페이스에 대한 리소스를 미리 생성하고 앱으로 패키지화하십시오.
>




**Choose a background appearance for the sash.** The system-provided sash, at the top of the long-look interface, displays your app icon and name. You can customize the sash’s color or give it a blurred appearance. If you display a photo at the top of the content area, you’ll probably want to use the blurred sash, which has a light, translucent appearance that gives the illusion of overlapping the image.
> 새시의 배경 모양을 선택하십시오. 시스템이 제공하는 새시는 롱 룩 인터페이스의 맨 위에 앱 아이콘과 이름을 표시합니다. 새시의 색상을 사용자 지정하거나 흐릿한 모양을 지정할 수 있습니다. 콘텐츠 영역 상단에 사진을 표시하면 이미지가 겹쳐지는 듯한 느낌을 주는 가볍고 반투명한 외관의 흐릿한 새시를 사용하고 싶을 것이다.
>




**Choose a background color for the content area.** By default, the long look’s background is transparent. If you want to match the background color of other system notifications, use white with 18% opacity; otherwise, you can use a custom color, such as a color within your brand’s palette.
> 내용 영역의 배경색을 선택합니다. 기본적으로 긴 모양의 배경은 투명합니다. 다른 시스템 알림의 배경색을 일치시키려면 불투명도가 18%인 흰색을 사용하십시오. 그렇지 않으면 브랜드 팔레트 내 색상과 같은 사용자 지정 색상을 사용할 수 있습니다.
>




**Provide up to four custom actions below the content area.** For each long look, the system uses the notification’s type to determine which of your custom actions to display as buttons in the notification UI. In addition, the system always displays a Dismiss button at the bottom of the long-look interface, below all custom buttons. If your watchOS app has an iPhone companion that supports notifications, the system shares the actionable notification types already registered by your iPhone app and uses them to configure your custom action buttons.
> 콘텐츠 영역 아래에 최대 4개의 사용자 지정 작업을 제공합니다. 시스템은 각 긴 모양에 대해 알림 유형을 사용하여 알림 UI에서 단추로 표시할 사용자 지정 작업을 결정합니다. 또한 시스템은 항상 모든 사용자 지정 버튼 아래에 롱 룩 인터페이스의 하단에 해제 버튼을 표시합니다. 네 시계라면OS 앱에는 알림을 지원하는 iPhone 지원 기능이 있으며, 시스템은 iPhone 앱에 이미 등록된 실행 가능한 알림 유형을 공유하고 이를 사용하여 사용자 지정 작업 버튼을 구성합니다.
>




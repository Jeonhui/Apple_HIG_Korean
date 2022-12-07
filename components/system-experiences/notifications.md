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





# **[patterns] managing-notifications**

# Notifications can give people timely and important information, whether the device is locked or in use.
> 통지는 기기가 잠겨 있든 사용 중이든 사람들에게 시기적절하고 중요한 정보를 줄 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-managing-notifications-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-managing-notifications-intro-dark_2x.png)

You need to get permission before sending any notification. The system lets people change this decision in settings, where they can also silence all notifications (except for government alerts in some locales).
> 알림을 보내기 전에 먼저 허가를 받아야 합니다. 이 시스템을 통해 사용자는 설정을 변경할 수 있으며, 여기서 모든 알림(일부 로케일의 정부 경고 제외)을 무음화할 수도 있습니다.
>




# **Integrating with Focus**

People appreciate receiving a notification for something they care about, but they don’t always appreciate being interrupted. To help people manage the experience, the system lets them specify delivery times and set up a Focus.
> 사람들은 자신이 아끼는 것에 대해 알림을 받는 것은 감사하지만, 항상 방해받는 것을 감사하게 여기지는 않는다. 사람들이 경험을 관리하는 것을 돕기 위해, 시스템은 배달 시간을 지정하고 포커스를 설정할 수 있게 한다.
>




- A Focus helps people filter notifications during a time period they reserve for an activity like sleeping, working, reading, or driving.
- >  포커스는 사람들이 수면, 작업, 독서 또는 운전과 같은 활동을 위해 예약한 시간 동안 알림을 필터링할 수 있도록 도와줍니다.

- Delivery scheduling lets people choose whether to receive notification alerts immediately or in a summary that’s delivered at times they choose.
- >  배달 예약을 통해 사용자는 통지 알림을 즉시 받을지 또는 선택한 시간에 배달되는 요약에서 받을지 선택할 수 있습니다.


People identify the contacts and apps that can break through a Focus to deliver notification alerts. In a Work Focus, for example, people might want to receive alerts from work colleagues, family members, and work-related apps as soon as notifications arrive. People might also want to receive all Time Sensitive notification alerts during a Focus. A *Time Sensitive* notification contains essential information people appreciate getting right away.
> 사람들은 포커스를 돌파하여 알림 경보를 전달할 수 있는 연락처와 앱을 식별합니다. 예를 들어 Work Focus에서 사람들은 알림이 도착하는 즉시 회사 동료, 가족 구성원 및 회사 관련 앱으로부터 알림을 받기를 원할 수 있습니다. 또한 포커스 중에 모든 Time Sensitive 알림 경보를 수신하고자 할 수도 있습니다. 시간 민감 알림에는 사람들이 즉시 얻을 수 있는 중요한 정보가 포함되어 있습니다.
>




**IMPORTANT**Even though a Focus might delay the delivery of a notification alert, the notification itself is available as soon as it arrives.
> 중요: 포커스로 인해 알림 알림 전송이 지연될 수 있지만 알림 자체는 알림이 도착하는 즉시 사용할 수 있습니다.
>




To support these behavior customizations, you first identify the types of notifications your app or game can send. If you support direct communications — like phone calls and messages — you use *communication* notifications; for all other types of tasks, you use *noncommunication* notifications. To support communication notifications, you adopt SiriKit intents, which means people can use Siri to customize notification behaviors; for developer guidance, see [INSendMessageIntent](https://developer.apple.com/documentation/sirikit/insendmessageintent) and [UNNotificationContentProviding](https://developer.apple.com/documentation/usernotifications/unnotificationcontentproviding).
> 이러한 동작 사용자 지정을 지원하려면 먼저 앱이나 게임이 보낼 수 있는 알림 유형을 식별합니다. 전화 및 메시지와 같은 직접 통신을 지원하는 경우 통신 통지를 사용하고 다른 모든 유형의 작업에는 비통신 통지를 사용합니다. 통신 알림을 지원하려면 SiriKit 의도를 사용합니다. 즉, 사용자가 Siri를 사용하여 알림 동작을 사용자 지정할 수 있습니다. 개발자 지침은 INSendMessage를 참조하십시오.의도 및 UNNotificationContentProviding.
>




You need to specify a system-defined interruption level for each noncommunication notification you send. The system uses the interruption level to help determine when to deliver the alert; when a communication notification arrives, the system uses the sender to determine when to deliver the alert.
> 보내는 각 비통신 통지에 대해 시스템 정의 중단 수준을 지정해야 합니다. 시스템은 중단 수준을 사용하여 알림을 전송할 시기를 결정합니다. 통신 알림이 도착하면 보낸 사람을 사용하여 알림을 전송할 시기를 결정합니다.
>




The system defines four interruption levels for noncommunication notifications:
> 시스템은 비통신 통지에 대한 네 가지 중단 수준을 정의합니다.
>




- *Passive*. Information people can view at their leisure, like a restaurant recommendation.
- >  수동적. 레스토랑 추천과 같이 사람들이 한가할 때 볼 수 있는 정보입니다.

- *Active* (the default). Information people might appreciate knowing about when it arrives, like a score update on their favorite sports team.
- >  활성(기본값). 사람들은 그들이 가장 좋아하는 스포츠 팀의 점수 업데이트와 같이 그것이 언제 도착하는지 아는 것에 대해 감사할 것이다.

- *Time Sensitive*. Information that directly impacts the user and requires their immediate attention, like an account security issue or a package delivery.
- >  시간 민감. 계정 보안 문제 또는 패키지 전송과 같이 사용자에게 직접적인 영향을 미치고 즉각적인 주의가 필요한 정보입니다.

- *Critical*. Urgent information about health and safety that directly impacts the user and demands their immediate attention. Critical notifications are extremely rare and typically come from governmental and public agencies or apps that help people manage their health or home.
- >  위급하다. 사용자에게 직접적인 영향을 미치며 즉각적인 주의가 필요한 건강 및 안전에 대한 긴급 정보입니다. 중요한 알림은 매우 드물며 일반적으로 건강 또는 가정을 관리하는 데 도움이 되는 정부 및 공공 기관 또는 앱에서 수신됩니다.


Notification alerts in each system-defined interruption level can behave in the following ways:
> 각 시스템 정의 중단 수준의 알림 알림은 다음과 같은 방식으로 작동할 수 있습니다.
>




**NOTE**Because a Critical notification can override the Ring/Silent switch and break through scheduled delivery and Focus, you must get an entitlement to send one.
> 참고 중요 통지는 벨소리/사일런트 스위치를 오버라이드하고 예약된 배달 및 포커스를 돌파할 수 있기 때문에 전송 권한을 얻어야 합니다.
>




# **Best practices**

**Build trust by accurately representing the urgency of each notification.** People have several ways to adjust how they receive your notifications — including turning off all notifications — so it’s essential to be as realistic as possible when assigning an interruption level. You don’t want people to feel that a notification uses a high level of urgency to interrupt them with low-priority information.
> 각 통지의 긴급성을 정확하게 표현하여 신뢰를 구축합니다. 사용자는 모든 알림을 끄는 등 여러 가지 방법으로 알림을 받는 방법을 조정할 수 있으므로 중단 수준을 할당할 때 가능한 한 현실적인 방법을 사용해야 합니다. 통지가 높은 수준의 긴급성을 사용하여 우선 순위가 낮은 정보로 사용자를 방해한다고 사람들이 느끼도록 하고 싶지 않을 것입니다.
>




**Use the Time Sensitive interruption level only for notifications that are relevant in the moment.** To help people understand the benefits of letting Time Sensitive notifications break through a Focus or scheduled delivery, make sure the notification is about an event that’s happening now or will happen within an hour. The first time a Time Sensitive notification arrives from your app, the system describes how such a notification works and gives people a way to turn it off if they don’t agree that the information requires their immediate attention. Going forward, the system periodically gives people additional opportunities to evaluate how your Time Sensitive notification is working for them. For developer guidance, see [UNNotificationInterruptionLevel](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel).
> 시간에 민감한 인터럽트 수준은 현재와 관련된 통지에 대해서만 사용하십시오. 포커스 또는 예약된 배달에 대한 시간 민감 알림의 이점을 이해하려면 알림이 현재 발생 중이거나 1시간 내에 발생할 수 있는 이벤트에 대한 것인지 확인하십시오. 시간 민감 알림이 앱에서 처음 도착하면 시스템은 이러한 알림의 작동 방식을 설명하고, 정보가 즉각적인 주의가 필요하다는 데 동의하지 않을 경우 알림을 해제할 수 있는 방법을 제공합니다. 앞으로 이 시스템은 정기적으로 사용자에게 시간 민감 알림이 어떻게 작동하는지 평가할 수 있는 추가 기회를 제공합니다. 개발자 지침은 UNNotification을 참조하십시오.중단레벨.
>




# **Sending marketing notifications**

Don’t use notifications to send marketing or promotional content unless people explicitly agree to receive such information. When people want to learn about new features, content, or events related to your app or game, they can grant their permission to receive marketing notifications. For example, people who use a subscription app might appreciate getting an offer to become a subscriber, and game players might want to receive a special offer related to a live game event.
> 사람들이 이러한 정보를 받는 것에 명시적으로 동의하지 않는 한, 마케팅 또는 홍보 콘텐츠를 보내기 위해 통지를 사용하지 마십시오. 사람들이 당신의 앱이나 게임과 관련된 새로운 기능, 콘텐츠 또는 이벤트에 대해 알고 싶을 때, 그들은 마케팅 알림을 받을 수 있는 그들의 허가를 부여할 수 있다. 예를 들어, 구독 앱을 사용하는 사람들은 구독자가 되기 위한 제안을 받는 것에 감사할 수 있고 게임 플레이어는 라이브 게임 이벤트와 관련된 특별 제안을 받기를 원할 수 있다.
>




**Never use the Time Sensitive interruption level to send a marketing notification.** People may have agreed to receive marketing notifications from your app, but such a notification should never break through a Focus or scheduled delivery setting.
> 마케팅 알림을 보낼 때 시간 민감 인터럽트 수준을 사용하지 마십시오. 사람들은 당신의 앱으로부터 마케팅 알림을 받는 것에 동의했을 수 있지만, 그러한 알림은 포커스 또는 예정된 배달 설정을 절대 위반해서는 안 된다.
>




**Get people’s permission if you want to send them promotional or marketing notifications.** Before you send these notifications to people, you must receive their explicit permission to do so. Create an alert, modal view, or other interface that describes the types of information you want to send and gives people a clear way to opt in or out.
> 홍보 또는 마케팅 알림을 보내려면 사용자의 허가를 받아야 합니다. 이러한 통지를 사용자에게 발송하기 전에 사용자의 명시적 권한을 받아야 합니다. 발송할 정보 유형을 설명하고 사용자에게 수신 또는 수신을 위한 명확한 방법을 제공하는 경고, 모달 보기 또는 기타 인터페이스를 만듭니다.
>




**Make sure people can manage their notification settings within your app.** In addition to requesting permission to send informational or marketing notifications, you must also provide an in-app settings screen that lets people change their choice. For guidance, see [Settings](../patterns/settings).
> 앱 내에서 다른 사용자가 알림 설정을 관리할 수 있는지 확인합니다. 정보 또는 마케팅 알림을 보낼 수 있는 권한을 요청하는 것 외에도, 사용자가 선택을 변경할 수 있는 앱 내 설정 화면도 제공해야 합니다. 자세한 내용은 설정을 참조하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항 없음.
>




# **watchOS**

By default, the notification settings people use for apps on their iPhone apply to the same apps on their Apple Watch. People can manage these settings in the Apple Watch app on iPhone, or they can access per-notification options — such as Mute 1 Hour or Turn off Time Sensitive — by swiping left when a notification arrives on their Apple Watch.
> 기본적으로 iPhone의 앱에 사용하는 알림 설정은 Apple Watch의 동일한 앱에 적용됩니다. iPhone의 Apple Watch 앱에서 이러한 설정을 관리하거나 Apple Watch에 알림이 도착할 때 왼쪽을 눌러 알림별 옵션(예: 음소거 1시간 또는 시간 민감 해제)에 액세스할 수 있습니다.
>




| Interruption level | Overrides scheduled delivery | Breaks through Focus | Overrides Ring/Silent switch on iPhone and iPad |
| --- | --- | --- | --- |
| Passive | No | No | No |
| Active | No | No | No |
| Time Sensitive | Yes | Yes | No |
| Critical | Yes | Yes | Yes |

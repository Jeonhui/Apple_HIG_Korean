# **[technologies] healthkit**

# HealthKit is the central repository for health and fitness data in iOS, iPadOS, and watchOS.
> HealthKit는 iOS, iPadOS 및 워치의 건강 및 피트니스 데이터를 위한 중앙 저장소입니다운영 체제.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-HealthKit-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-HealthKit-intro_2x.png)

When you enable HealthKit in your app, you can ask people for permission to access and update their health information.
> 앱에서 HealthKit을 활성화하면 사용자에게 건강 정보에 액세스하고 업데이트할 수 있는 권한을 요청할 수 있습니다.
>




**IMPORTANT**If your app doesn't provide health and fitness functionality, don't request access to people's private health data.
> 중요 앱이 건강 및 피트니스 기능을 제공하지 않는 경우, 사람들의 개인 건강 데이터에 대한 액세스를 요청하지 마십시오.
>




For example, a HealthKit-enabled nutrition app might ask for permission to retrieve people's weight and activity data, so it can define calorie consumption goals and make dietary recommendations. In this scenario, the nutrition app could also send data — such as the calories that people log — to HealthKit, which can include the data in its global progress metrics.
> 예를 들어, HealthKit 지원 영양 앱은 사람들의 체중과 활동 데이터를 검색할 수 있는 허가를 요청하여 칼로리 소비 목표를 정의하고 식이 요법을 권장할 수 있다. 이 시나리오에서 영양 앱은 사람들이 기록하는 칼로리와 같은 데이터를 HealthKit로 전송할 수 있으며, 이 데이터는 글로벌 진행률 메트릭에 포함될 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/health-summary-light_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/health-summary-light_2x.png)

For developer guidance, see [HealthKit](https://developer.apple.com/documentation/healthkit).

# **Privacy protection**

You must request permission to access people's data, and you must take all necessary steps to protect that data. After you receive permission, it's essential to maintain people's trust by clearly showing them how you use their data. For developer guidance, see [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting_user_privacy).
> 사용자의 데이터에 액세스할 수 있는 권한을 요청하고 해당 데이터를 보호하기 위해 필요한 모든 단계를 수행해야 합니다. 허가를 받은 후에는 데이터를 어떻게 사용하는지 명확히 보여줌으로써 사람들의 신뢰를 유지하는 것이 중요합니다. 개발자 지침은 사용자 개인 정보 보호를 참조하십시오.
>




**Provide a coherent privacy policy.** During the app submission process, you must provide a URL to a clearly stated privacy policy, so that people can view the policy when they click the link in the App Store page for your app. For developer guidance, see [App Information > App Store Connect Help](https://help.apple.com/app-store-connect/#/dev219b53a88).
> 일관된 개인 정보 보호 정책을 제공하십시오. 앱 제출 과정에서 개인 정보 보호 정책에 대한 URL을 제공하여 사용자가 앱의 앱 스토어 페이지에 있는 링크를 클릭할 때 정책을 볼 수 있도록 해야 합니다. 개발자 안내는 앱 정보 > 앱스토어 연결 도움말을 참고하세요.
>




**Request access to health data only when you need it.** It makes sense to request access to weight information when people log their weight, for example, but not immediately after your app launches. When your request is clearly related to the current context, you help people understand your app’s intentions. Also, people can change the permissions they grant, so your app should make a request every time it needs access. For developer guidance, see [requestAuthorization(toShare:read:completion:)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorization).
> 필요할 때만 건강 데이터에 대한 액세스를 요청하십시오. 예를 들어, 사람들이 체중을 기록할 때 체중 정보에 대한 액세스를 요청하는 것이 이치에 맞지만, 앱이 시작된 직후에는 요청하지 않습니다. 당신의 요청이 현재 상황과 명확하게 관련되어 있을 때, 당신은 사람들이 당신의 앱의 의도를 이해하도록 돕는다. 또한, 사람들은 자신이 부여한 권한을 변경할 수 있으므로, 앱은 액세스가 필요할 때마다 요청해야 합니다. 개발자 지침은 요청을 참조하십시오권한 부여(공유 대상: 읽기: 완료:).
>




**Clarify your app's intent by adding descriptive messages to the standard permission screen.**People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app. Avoid adding custom screens that replicate the standard permission screen’s behavior or content.
> 표준 권한 화면에 설명 메시지를 추가하여 앱의 의도를 명확히 합니다.사람들은 건강 데이터에 대한 액세스를 승인하라는 요청이 있을 때 시스템이 제공하는 권한 화면을 볼 것으로 예상한다. 당신이 왜 정보가 필요한지, 그리고 사람들이 당신의 앱과 정보를 공유함으로써 어떻게 이익을 얻을 수 있는지 설명하는 몇 가지 간결한 문장을 쓰세요. 표준 권한 화면의 동작이나 내용을 복제하는 사용자 정의 화면을 추가하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/health-access-requests_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/health-access-requests_2x.png)

**Manage health data sharing solely through the system’s privacy settings.** People expect to globally manage access to their health information in Settings > Privacy. Don’t confuse people by building additional screens in your app that affect the flow of health data.
> 시스템의 개인 정보 설정을 통해서만 건강 데이터 공유를 관리합니다. 사람들은 개인 정보 설정 > 개인 정보에서 자신의 건강 정보에 대한 접근을 전 세계적으로 관리하기를 기대합니다. 건강 데이터 흐름에 영향을 미치는 추가 화면을 앱에 구축하여 사람들을 혼란스럽게 하지 마십시오.
>




# **Activity Rings**

You can enhance your app's health and wellness offerings by displaying the Activity ring element to show people's progress toward their Move, Exercise, and Stand goals. The Activity app defines the position and color of each ring, so people are familiar with the element and understand what it means.
> 활동 링 요소를 표시하여 이동, 운동 및 스탠드 목표를 향한 사람들의 진행 상태를 보여줌으로써 앱의 건강 및 웰빙 서비스를 향상시킬 수 있습니다. 활동 앱은 각 링의 위치와 색상을 정의하므로 사람들은 그 요소에 익숙하고 그것이 무엇을 의미하는지 이해합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/activity-months_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/activity-months_2x.png)

**Use Activity rings for Move, Exercise, and Stand information only.** Activity rings consistently represent progress in these specific areas. Don’t attempt to replicate or modify Activity rings for other purposes or to display other types of data. Never show Move, Exercise, and Stand progress in another ring-like element.
> 이동, 연습 및 스탠드 정보에만 활동 링을 사용하십시오. 활동 링은 이러한 특정 영역의 진행 상태를 일관되게 나타냅니다. 다른 목적으로 활동 링을 복제하거나 수정하거나 다른 유형의 데이터를 표시하지 마십시오. 다른 링 모양 요소에서 이동, 연습 및 스탠드 진행 상태를 표시하지 마십시오.
>




**Use Activity rings to show progress for a single person.** Never use Activity rings to represent data for more than one person, and make sure it’s obvious whose progress is shown, such as by using a label, a photo, or an avatar.
> 활동 링을 사용하여 한 사람의 진행 상황을 표시하고, 활동 링을 사용하여 두 사람 이상의 데이터를 표시하지 마십시오. 레이블, 사진 또는 아바타를 사용하는 등 누구의 진행 상황이 표시되는지 확인하십시오.
>




**Don’t use Activity rings for ornamentation.** Activity rings provide information to people; they should not merely embellish your app’s design. Never display Activity rings in labels or background graphics.
> 액티비티 링을 장식용으로 사용하지 마십시오. 액티비티 링은 사람들에게 정보를 제공합니다. 앱의 디자인만 장식해서는 안 됩니다. 레이블이나 배경 그래픽에 활동 링을 표시하지 마십시오.
>




**Don’t use Activity rings for branding.** Use Activity rings strictly to display Activity progress in your app. Never use Activity rings in your app’s icon or marketing materials.
> 활동 링을 브랜딩에 사용하지 마십시오. 앱에 활동 진행률을 표시하려면 활동 링을 사용하십시오. 앱의 아이콘이나 마케팅 자료에 활동 링을 사용하지 마십시오.
>




**Maintain Activity ring and background colors.** For a consistent user experience, the visual appearance of Activity rings must always be the same, regardless of the context in which they appear. Never change the look of the rings or background by using filters, changing colors, or modifying opacity. Instead, design the surrounding interface to blend with the rings. For example, enclose the rings within a circle. Always scale the rings appropriately so they don’t seem disconnected or out of place.
> 활동 링과 배경색을 유지합니다. 일관된 사용자 환경을 위해 활동 링의 시각적 모양은 나타나는 컨텍스트에 관계없이 항상 동일해야 합니다. 필터를 사용하거나 색상을 변경하거나 불투명도를 수정하여 링이나 배경의 모양을 변경하지 마십시오. 대신 주변 인터페이스를 링과 혼합하도록 설계하십시오. 예를 들어 고리를 원 안에 넣습니다. 링이 분리되거나 제자리에 맞지 않는 것처럼 보이지 않도록 항상 적절히 크기를 조정하십시오.
>




**Maintain Activity ring margins.** An Activity ring element must include a minimum outer margin of no less than the distance between rings. Never allow other elements to crop, obstruct, or encroach upon this margin or the rings themselves. To display an Activity ring element within a circle, adjust the corner radius of the enclosing view rather than applying a circular mask.
> 활동 링 여백을 유지합니다. 활동 링 요소는 링 사이의 거리 이상의 최소 외부 여백을 포함해야 합니다. 다른 요소가 이 가장자리나 링 자체를 자르거나 방해하거나 침범하지 않도록 하십시오. 활동 고리 요소를 원 안에 표시하려면 원형 마스크를 적용하는 대신 둘러싸는 보기의 모서리 반지름을 조정합니다.
>




**Differentiate other ring-like elements from Activity rings.** Mixing different ring styles can lead to a visually confusing interface. If you must include other rings, use padding, lines, or labels to separate them from Activity rings. Color and scale can also help provide visual separation.
> 다른 링과 유사한 요소를 활동 링과 구별합니다. 서로 다른 링 스타일을 혼합하면 시각적으로 인터페이스를 혼동할 수 있습니다. 다른 링을 포함해야 하는 경우 패딩, 선 또는 레이블을 사용하여 활동 링과 구분하십시오. 색상과 스케일은 시각적인 분리를 제공하는 데도 도움이 될 수 있습니다.
>




**Provide app-specific information only in Activity notifications.** The system already delivers Move, Exercise, and Stand progress updates. Don’t repeat this same information, and never show an Activity ring element in your app’s notifications. It’s fine to reference Activity progress in a notification, but do so in a way that’s unique to your app and doesn’t replicate the same information provided by the system.
> 활동 알림에서만 앱별 정보를 제공합니다. 시스템이 이미 이동, 연습 및 스탠드 진행률 업데이트를 제공합니다. 동일한 정보를 반복하지 말고 앱의 알림에 활동 링 요소를 표시하지 마십시오. 알림에서 작업 진행률을 참조하는 것은 좋지만, 앱에 고유하고 시스템에서 제공하는 동일한 정보를 복제하지 않는 방식으로 작업 진행률을 참조하는 것이 좋습니다.
>




For developer guidance, see [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview).

# **Apple Health icon**

The Apple Health icon shows that an app works with HealthKit and the Health app. The following guidelines help you use the icon correctly. To learn how to refer to HealthKit and the Health app in copy and UI text, see [Editorial Guidelines](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit#editorial-guidelines); to learn about using the "Works with Apple Health" badge in your marketing communications, see [Works with Apple Health](https://developer.apple.com/health-fitness/works-with-apple-health/).
> Apple Health 아이콘은 앱이 HealthKit 및 Health 앱과 함께 작동함을 보여줍니다. 다음 지침은 아이콘을 올바르게 사용하는 데 도움이 됩니다. HealthKit 및 Health 앱을 복사 및 UI 텍스트로 참조하는 방법은 편집 지침을 참조하고, 마케팅 커뮤니케이션에서 "Works with Apple Health" 배지를 사용하는 방법은 Apple Health를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/health-icon-onboard-screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit/images/health-icon-onboard-screen_2x.png)

**Use only the Apple-provided icon.** Don't create your own Apple Health icon design or attempt to mimic any Apple-provided designs. Download the Apple Health app icon from [Apple Design Resources](https://developer.apple.com/design/resources/#technologies).
> Apple에서 제공한 아이콘만 사용하십시오. Apple Health 아이콘 디자인을 직접 만들거나 Apple에서 제공한 디자인을 모방하지 마십시오. Apple Design Resources에서 Apple Health 앱 아이콘을 다운로드합니다.
>




**Display the name *Apple Health* close to the Apple Health icon.** Displaying both elements near each other reminds people that the icon represents the Health app.
> Apple Health 아이콘 근처에 Apple Health라는 이름을 표시합니다. 두 요소를 서로 가까이에 표시하면 해당 아이콘이 Health 앱을 나타내는 것임을 알립니다.
>




**Display the Apple Health icon consistently with other health-related app icons.** In a view that contains other app icons, make the Apple Health icon no smaller than other icons.
> Apple Health 아이콘을 다른 상태 관련 앱 아이콘과 일관되게 표시합니다. 다른 앱 아이콘이 포함된 보기에서 Apple Health 아이콘을 다른 아이콘보다 작지 않게 설정합니다.
>




**Don't use the Apple Health icon as a button.** Use the icon only to indicate compatibility with the Health app.
> Apple Health 아이콘을 단추로 사용하지 마십시오. Health 앱과의 호환성을 나타내는 경우에만 아이콘을 사용하십시오.
>




**Don't alter the appearance of the Apple Health icon.** Don't mask the icon to change its corner radius or present it in a circular shape. Don't add embellishments like borders, color overlays, gradients, shadows, or other visual effects.
> Apple Health 아이콘의 모양을 변경하지 마십시오. 아이콘을 마스킹하여 모서리 반지름을 변경하거나 원형으로 표시하지 마십시오. 테두리, 색상 오버레이, 그라데이션, 그림자 또는 기타 시각적 효과와 같은 장식을 추가하지 마십시오.
>




**Maintain a minimum clear space around the Apple Health icon of 1/10 of its height.** Don't composite the icon onto another graphic element.
> Apple Health 아이콘의 높이의 10분의 1에 해당하는 최소 공백을 유지합니다. 아이콘을 다른 그래픽 요소에 합성하지 마십시오.
>




**Don't use the Apple Health icon within text or as a replacement for the terms *Health*, *Apple Health*, or *HealthKit*.** See [Editorial guidelines](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit#editorial-guidelines) to learn how to properly reference the Health app and HealthKit in text.
> Apple Health 아이콘을 텍스트 내에서 사용하거나 Health, Apple Health 또는 HealthKit 용어를 대체하는 데 사용하지 마십시오. Health 앱 및 HealthKit을 텍스트에서 올바르게 참조하는 방법은 편집 지침을 참조하십시오.
>




**Don't display Health app images or screenshots.** Like all Apple imagery, these designs are copyrighted and shouldn’t appear in your app or marketing materials. You can include an Activity ring element in your app to display Move, Exercise, and Stand progress; for guidance, see [Activity Rings](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit#activity-rings).
> 다른 모든 Apple 이미지와 마찬가지로 이러한 디자인도 저작권이 있으므로 앱이나 마케팅 자료에 표시해서는 안 됩니다. 앱에 활동 링 요소를 포함하여 이동, 연습 및 대기 진행률을 표시할 수 있습니다. 자세한 내용은 활동 링을 참조하십시오.
>




# **Editorial guidelines**

**Refer to the Health app as *Apple Health* or *the Apple Health app*.** In your app and marketing text, using *Apple Health* adds clarity.
> Health 앱을 Apple Health 또는 Apple Health 앱으로 참조하십시오. 앱 및 마케팅 텍스트에서 Apple Health를 사용하면 명확성이 추가됩니다.
>





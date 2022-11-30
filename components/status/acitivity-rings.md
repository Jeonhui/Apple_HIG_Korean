# **[components-status] acitivity-rings**

## Activity rings show an individual’s daily progress toward Move, Exercise, and Stand goals.
> 활동 링은 이동, 운동, 그리고 서서 하는 목표를 향한 개인의 일상적인 진전을 보여줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/activity-ring-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/activity-ring-intro-dark_2x.png)

In watchOS, the Activity ring element always contains three rings, whose colors and meanings match those the Activity app provides. In iOS, the Activity ring element contains either a single Move ring representing an approximation of activity, or all three rings if an Apple Watch is paired.
> watchOS에서 액티비티 링 요소는 항상 3개의 링을 포함하며, 이 링의 색상과 의미는 액티비티 앱이 제공하는 링과 일치합니다. iOS에서 Activity 링 요소는 활동의 근사치를 나타내는 단일 Move 링을 포함하거나 Apple Watch가 페어링된 경우 세 개의 링을 모두 포함합니다.
>




# **Best practices**

**Display Activity rings when they're relevant to the purpose of your app.**Activity rings are an important component of the Apple Watch experience. If your app is related to health or fitness, and especially if it contributes information to HealthKit, people generally expect to find Activity rings in your interface. For example, if you structure a workout or health session around the completion of Activity rings, consider displaying the element on a workout metrics screen so that people can track their progress during their session. Similarly, if you provide a summary screen that appears at the conclusion of a workout, you could display Activity rings to help people check on their progress toward their daily goals.
> 디스플레이 활동은 앱의 목적과 관련이 있을 때 울립니다.액티비티 링은 Apple Watch 경험의 중요한 구성 요소입니다. 만약 당신의 앱이 건강이나 피트니스와 관련이 있고, 특히 그것이 HealthKit에 정보를 제공한다면, 사람들은 일반적으로 당신의 인터페이스에서 활동 링을 찾기를 기대한다. 예를 들어, 활동 링의 완료를 중심으로 워크아웃 또는 건강 세션을 구성하는 경우, 사람들이 세션 중에 진행 상황을 추적할 수 있도록 워크아웃 메트릭 화면에 요소를 표시하는 것을 고려하십시오. 마찬가지로, 만약 당신이 운동이 끝날 때 나타나는 요약 화면을 제공한다면, 당신은 사람들이 그들의 일상적인 목표를 향한 그들의 진행을 확인하는 것을 돕기 위해 활동 링을 표시할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/status/activity-rings/images/activity-rings-summary_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/activity-rings/images/activity-rings-summary_2x.png)

**Use Activity rings only to show Move, Exercise, and Stand information.**Activity rings are designed to consistently represent progress in these specific areas. Don’t attempt to replicate or modify Activity rings for other purposes. Never use Activity rings to display other types of data. Never show Move, Exercise, and Stand progress in another ring-like element.
> 이동, 연습 및 스탠드 정보를 표시할 때만 활동 링을 사용하십시오.활동 링은 이러한 특정 영역의 진행 상황을 일관되게 나타내도록 설계되었습니다. 다른 목적으로 활동 링을 복제하거나 수정하지 마십시오. 활동 링을 사용하여 다른 유형의 데이터를 표시하지 마십시오. 다른 링 모양 요소에서 이동, 연습 및 스탠드 진행 상태를 표시하지 마십시오.
>




**Use Activity rings to show progress for a single person.** Never use Activity rings to represent data for more than one person, and make sure it’s obvious whose progress you're showing by using a label, a photo, or an avatar.
> 활동 링을 사용하여 한 사람의 진행 상황을 표시하고, 활동 링을 사용하여 두 사람 이상의 데이터를 표시하지 마십시오. 레이블, 사진 또는 아바타를 사용하여 누구의 진행 상황을 표시하는지 확인하십시오.
>




**Maintain Activity ring colors.** For a consistent experience, keep the visual appearance of Activity rings the same regardless of the context in which they appear. Never change the look of the rings by using filters, changing colors, or modifying opacity. Instead, design the surrounding interface to blend with the rings. For example, enclose the rings and background within a circle. Always scale the rings appropriately so they don’t seem disconnected or out of place.
> 활동 링 색상을 유지합니다. 일관된 환경을 위해 활동 링의 시각적 모양은 나타나는 컨텍스트에 관계없이 동일하게 유지하십시오. 필터를 사용하거나 색상을 변경하거나 불투명도를 수정하여 링 모양을 변경하지 마십시오. 대신 주변 인터페이스를 링과 혼합하도록 설계하십시오. 예를 들어 고리와 배경을 원 안에 넣습니다. 링이 분리되거나 제자리에 맞지 않는 것처럼 보이지 않도록 항상 적절히 크기를 조정하십시오.
>




**Always display Activity rings on a black background.** The background is a key component of Activity ring presentation. Don't display the rings on anything other than a black background.
> 항상 검은색 배경에 활동 링을 표시합니다. 배경은 활동 링 프레젠테이션의 주요 구성 요소입니다. 검은색 배경 이외의 다른 배경에는 반지를 표시하지 마십시오.
>




**Maintain Activity ring margins.** An Activity ring element must include a minimum outer margin of no less than the distance between rings. Never allow other elements to crop, obstruct, or encroach upon this margin or the rings themselves. To display an Activity ring element within a circle, adjust the corner radius of the enclosing view rather than applying a circular mask.
> 활동 링 여백을 유지합니다. 활동 링 요소는 링 사이의 거리 이상의 최소 외부 여백을 포함해야 합니다. 절대로 다른 요소들이 이 가장자리나 고리 자체를 자르거나 방해하거나 잠식하지 않도록 하십시오. 원 내에 활동 링 요소를 표시하려면 원형 마스크를 적용하는 대신 둘러보기의 모서리 반지름을 조정하십시오.
>




**Differentiate other ring-like elements from Activity rings.** Mixing different ring styles can lead to a visually confusing interface. If you must include other rings, use padding, lines, or labels to separate them from Activity rings. Color and scale can also help provide visual separation.
> 다른 링과 유사한 요소를 활동 링과 구별합니다. 서로 다른 링 스타일을 혼합하면 시각적으로 인터페이스를 혼동할 수 있습니다. 다른 링을 포함해야 하는 경우 패딩, 선 또는 레이블을 사용하여 활동 링과 구분하십시오. 색상과 스케일은 시각적인 분리를 제공하는 데도 도움이 될 수 있습니다.
>




**Don't send notifications that repeat the same information the Activity app sends.** The system already delivers Move, Exercise, and Stand progress updates, so it's confusing for people to receive redundant information from your app. Also, don't show an Activity ring element in your app’s notifications. It’s fine to reference Activity progress in a notification, but do so in a way that’s unique to your app and doesn’t replicate the same information the system provides.
> 시스템이 이미 이동, 연습 및 스탠드 진행률 업데이트를 제공하므로 사용자가 앱에서 중복 정보를 받는 것은 혼란스러운 일입니다. 또한 앱의 알림에 활동 링 요소를 표시하지 마십시오. 알림에서 활동 진행률을 참조하는 것은 좋지만, 앱에 고유하고 시스템이 제공하는 것과 동일한 정보를 복제하지 않는 방식으로 작업 진행률을 참조하는 것이 좋습니다.
>




**Don’t use Activity rings for ornamentation.** Activity rings provide information to people, not embellish your app’s design. Never display Activity rings in labels or background graphics.
> 활동 링을 장식용으로 사용하지 마십시오. 활동 링은 사람들에게 정보를 제공하는 것이지 앱의 디자인을 꾸미는 것이 아닙니다. 레이블이나 배경 그래픽에 활동 링을 표시하지 마십시오.
>




**Don’t use Activity rings for branding.** Use Activity rings strictly to display Activity progress in your app. Never use Activity rings in your app’s icon or marketing materials.
> 활동 링을 브랜딩에 사용하지 마십시오. 앱에 활동 진행률을 표시하려면 활동 링을 사용하십시오. 앱의 아이콘이나 마케팅 자료에 활동 링을 사용하지 마십시오.
>




# **Platform considerations**

*No additional considerations for iPadOS or watchOS. Not supported in macOS or tvOS.*
> iPad에 대한 추가 고려 사항 없음OS 또는 워치OS. macOS 또는 tvOS에서는 지원되지 않습니다.
>




# **iOS**

Activity rings are available in iOS with [HKActivityRingView](https://developer.apple.com/documentation/healthkit/hkactivityringview). The appearance of the Activity ring element changes automatically depending on whether an Apple Watch is paired:
> 활동 링은 HKActivityRingView가 있는 iOS에서 사용할 수 있습니다. Apple Watch가 페어링되어 있는지 여부에 따라 Activity 링 요소의 모양이 자동으로 변경됩니다.
>




- With an Apple Watch paired, iOS shows all three Activity rings.
- >  Apple Watch가 페어링된 경우 iOS는 세 가지 액티비티 링을 모두 표시합니다.

- Without an Apple Watch paired, iOS shows the Move ring only, which represents an approximation of a person’s activity based on their steps and workout information from other apps.
- >  애플 워치가 페어링되지 않은 상태에서 iOS는 무빙 링만 표시하며, 이 링은 다른 앱의 단계와 운동 정보를 기반으로 한 사람의 활동의 근사치를 나타냅니다.


Because iOS shows Activity rings whether or not an Apple Watch is paired, activity history can include a combination of both styles. For example, Activity rings in Fitness have three rings when a person exercises with their Apple Watch paired, and only the Move ring when they exercise without their Apple Watch.
> iOS는 Apple Watch가 페어링되었는지 여부에 관계없이 Activity 링을 표시하므로 활동 기록에는 두 가지 스타일의 조합이 포함될 수 있습니다. 예를 들어, 피트니스의 활동 링에는 애플 워치를 페어링하고 운동할 때 세 개의 링이 있고, 애플 워치 없이 운동할 때는 무빙 링만 있습니다.
>




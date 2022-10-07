# **[patterns] accessing-private-data**
# To help people trust your app or game, you must be transparent about the privacy-related data and resources you require and how you use them.
> 사람들이 당신의 앱이나 게임을 신뢰하도록 돕기 위해, 당신은 당신이 필요로 하는 개인 정보 관련 데이터와 자원 그리고 그것들을 사용하는 방법에 대해 투명해야 한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-accessing-private-data-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-accessing-private-data-intro-dark_2x.png)

People use their devices in very personal ways and they expect apps to help them preserve their privacy. In addition to requesting permission to track people or access their data and device resources (including the advertising identifier), it’s essential to protect the data you’re allowed to access.
> 사람들은 그들의 기기를 매우 개인적인 방식으로 사용하고 그들은 앱이 그들의 사생활을 보호하는데 도움을 줄 것으로 기대한다. 사용자를 추적하거나 사용자의 데이터 및 장치 리소스(광고 식별자 포함)에 액세스할 수 있는 권한을 요청하는 것 외에도 액세스할 수 있는 데이터를 보호하는 것이 중요합니다.
>




When you submit a new or updated app, you must provide details about your privacy practices and the privacy-relevant data you collect so the App Store can display the information on your product page. (You can manage this information at any time in [App Store Connect](https://help.apple.com/app-store-connect/#/dev1b4647c5b).) People use the privacy details on your product page to make an informed decision before they download your app. To learn more, see [App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/).
> 새 앱 또는 업데이트된 앱을 제출할 때 앱 스토어가 제품 페이지에 정보를 표시할 수 있도록 개인 정보 보호 관행 및 수집하는 개인 정보 관련 데이터에 대한 세부 정보를 제공해야 합니다. (이 정보는 앱 스토어 연결에서 언제든지 관리할 수 있습니다.) 사람들은 당신의 앱을 다운로드하기 전에 당신의 제품 페이지의 개인 정보 세부 정보를 사용하여 정보에 입각한 결정을 내린다. 자세한 내용은 앱 스토어에서 앱 개인 정보 정보를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/privacy-practices_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/privacy-practices_2x.png)

An app’s App Store product page helps people understand the app’s privacy practices before they download it.
> 앱의 앱 스토어 제품 페이지는 사람들이 앱을 다운로드하기 전에 앱의 개인 정보 보호 관행을 이해하는 데 도움이 됩니다.
>




# **Requesting permission**

Here are several examples of the things you must request permission to access:
> 다음은 액세스 권한을 요청해야 하는 몇 가지 예입니다.
>




- Personal data, including location, health, financial, contact, and other personally identifying information
- >  위치, 건강, 재무, 연락처 및 기타 개인 식별 정보를 포함한 개인 데이터

- User-generated content like emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, and audio, video, and photo content
- >  이메일, 메시지, 캘린더 데이터, 연락처, 게임 플레이 정보, Apple Music 활동, HomeKit 데이터, 오디오, 비디오 및 사진 콘텐츠와 같은 사용자 생성 콘텐츠

- Protected resources like Bluetooth peripherals, home automation features, Wi-Fi connections, and local networks
- >  Bluetooth 주변기기, 홈 자동화 기능, Wi-Fi 연결 및 로컬 네트워크와 같은 보호된 리소스

- Device capabilities like camera and microphone
- >  카메라 및 마이크와 같은 장치 기능

- The device’s advertising identifier, which enables app tracking
- >  앱 추적을 가능하게 하는 장치의 광고 식별자


The system provides a standard alert that lets people view each request you make. You supply copy that describes why your app needs access, and the system displays your description in the alert. People can also view the description — and update their choice — in Settings > Privacy.
> 시스템은 사용자가 요청한 각 요청을 볼 수 있는 표준 알림을 제공합니다. 앱에 액세스해야 하는 이유를 설명하는 복사본을 제공하고 시스템에서 사용자의 설명을 경고에 표시합니다. 또한 설정 > 개인 정보에서 설명을 보고 원하는 내용을 업데이트할 수 있습니다.
>




**Request permission only when your app clearly needs access to the data or resource.** It’s natural for people to be suspicious of a request for personal information or access to a device capability, especially if there’s no obvious need for it. Ideally, wait to request permission until people actually use an app feature that requires access. For example, you can use the [location button](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data#location-button) to give people a way to share their location after they indicate interest in a feature that needs that information.
> 앱에서 데이터나 리소스에 액세스할 필요가 있는 경우에만 권한을 요청합니다. 개인 정보에 대한 요청이나 장치 기능에 대한 액세스에 대해 사람들이 의심하는 것은 당연합니다. 특히, 개인 정보에 대한 명백한 필요성이 없는 경우에는 더욱 그렇습니다. 사람들이 실제로 액세스를 필요로 하는 앱 기능을 사용할 때까지 권한을 요청하는 것을 기다리는 것이 이상적입니다. 예를 들어 위치 단추를 사용하여 사용자가 해당 정보가 필요한 기능에 관심을 표시한 후 위치를 공유할 수 있습니다.
>




**Avoid requesting permission at launch unless the data or resource is required for your app to function.** People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it. For example, people understand that a navigation app needs access to their location before they can benefit from it.
> 앱이 작동하는 데 필요한 데이터나 리소스가 아닌 경우 시작할 때 사용 권한을 요청하지 마십시오. 사람들은 당신이 왜 그것을 만드는지 명백할 때 발사 시간 요청에 덜 신경 쓰입니다. 예를 들어, 사람들은 내비게이션 앱이 혜택을 받기 전에 자신의 위치에 액세스해야 한다는 것을 이해한다.
>




**Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting.** The standard alert displays your copy (called a *purpose string* or *usage description string*) after your app name and before the buttons people use to grant or deny their permission. Aim for a brief, complete sentence that’s straightforward, specific, and easy to understand. Use sentence case, avoid passive voice, and include a period at the end. For developer guidance, see [Requesting Access to Protected Resources](https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources) and [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency).
> 요청 중인 기능, 데이터 또는 리소스를 앱이 어떻게 사용하는지 명확하게 설명하는 복사본을 작성합니다. 표준 알림은 앱 이름 뒤에 복사(목적 문자열 또는 사용 설명 문자열이라고 함)를 표시하고 사용자가 권한을 부여하거나 거부하는 데 사용하는 단추 앞에 표시합니다. 간단하고, 구체적이고, 이해하기 쉬운 짧고, 완전한 문장을 목표로 하세요. 문장의 대소문자를 사용하고 수동적인 목소리를 피하고 끝에 마침표를 포함하세요. 개발자 지침은 보호된 리소스에 대한 액세스 요청 및 앱 추적 투명성을 참조하십시오.
>




[제목 없음](https://www.notion.so/aa78520928af4c49a871b6ef4f7d6568)

Here are several examples of the standard system alert:
> 다음은 표준 시스템 경고의 몇 가지 예입니다.
>




• [Example 1](../patterns/accessing-private-data#)
• [Example 2](../patterns/accessing-private-data#)
• [Example 3](../patterns/accessing-private-data#)

-

![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/permission-request-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/permission-request-1_2x.png)


# **Location button**

Beginning in iOS 15, iPadOS 15, and watchOS 8, Core Location provides a button so people can grant your app temporary authorization to access their location at the moment a task needs it. A location button’s appearance can vary to match your app’s UI and it always communicates the action of location sharing in a way that’s instantly recognizable.
> iOS 15, iPad OS 15, 그리고 watch.OS 8, Core Location은 작업이 필요한 순간에 앱에 액세스할 수 있는 임시 권한을 부여할 수 있는 버튼을 제공합니다. 위치 단추의 모양은 앱의 UI에 따라 달라질 수 있으며 항상 즉시 인식할 수 있는 방식으로 위치 공유 작업을 전달합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/location-button_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/location-button_2x.png)

The first time people open your app and tap a location button, the system displays a standard alert. The alert helps people understand how using the button limits your app’s access to their location, and reminds them of the location indicator that appears when sharing starts.
> 사람들이 당신의 앱을 처음 열고 위치 버튼을 누르면 시스템은 표준 경보를 표시합니다. 이 경고는 단추를 사용하여 앱의 위치에 대한 액세스를 제한하는 방법을 이해하고 공유를 시작할 때 나타나는 위치 표시기를 알려주는 데 도움이 됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/location-button-alert_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/location-button-alert_2x.png)

After people confirm their understanding of the button’s action, simply tapping the location button gives your app one-time permission to access their location. Although each one-time authorization expires when people stop using your app, they don’t need to reconfirm their understanding of the button’s behavior.
> 사람들이 버튼의 동작에 대한 이해를 확인한 후 위치 버튼을 누르기만 하면 앱에 한 번 자신의 위치에 액세스할 수 있는 권한을 부여합니다. 사람들이 당신의 앱 사용을 중단하면 각 일회성 인증이 만료되지만, 그들은 버튼의 동작에 대한 이해를 재확인할 필요가 없다.
>




**NOTE**If your app has no authorization status, tapping the location button has the same effect as when a person chooses *Allow Once* in the standard alert. If people previously chose *While Using the App*, tapping the location button doesn’t change your app’s status. For developer guidance, see [LocationButton](https://developer.apple.com/documentation/corelocationui/locationbutton) (SwiftUI) and [CLLocationButton](https://developer.apple.com/documentation/corelocationui/cllocationbutton) (Swift).
> 참고 앱에 권한 부여 상태가 없는 경우 위치 버튼을 누르면 표준 경고에서 한 번 허용을 선택한 경우와 동일한 효과가 있습니다. 이전에 앱 사용 중을 선택한 경우 위치 버튼을 눌러도 앱 상태가 변경되지 않습니다. 개발자 지침은 위치 단추(Swift)를 참조하십시오.UI) 및 CL 위치 버튼(Swift).
>




**Consider using the location button to give people a lightweight way to share their location for specific app features.** For example, your app might help people attach their location to a message or post, find a store, or identify a building, plant, or animal they’ve encountered in their location. If you know that people often grant your app *Allow Once *permission, consider using the location button to help them benefit from sharing their location without having to repeatedly interact with the alert.
> 위치 버튼을 사용하여 특정 앱 기능에 대한 위치를 공유할 수 있는 가벼운 방법을 고려해 보십시오. 예를 들어, 당신의 앱은 사람들이 그들의 위치를 메시지나 게시물에 첨부하거나, 상점을 찾거나, 그들이 그들의 위치에서 마주친 건물, 식물 또는 동물을 식별하는 데 도움을 줄 수 있다. 사용자가 앱에 한 번 허용 권한을 부여하는 경우가 많은 경우 위치 단추를 사용하여 경고와 반복적으로 상호 작용할 필요 없이 위치를 공유할 수 있습니다.
>




**Consider customizing the location button to harmonize with your UI.** Specifically, you can:
> 사용자 UI와 조화를 이루도록 위치 버튼을 사용자 지정하는 것을 고려해 보십시오. 특히 다음을 수행할 수 있습니다.
>




- Choose the system-provided title that works best with your feature, such as “Current Location” or “Share My Current Location”
- >  "현재 위치" 또는 "내 현재 위치 공유"와 같이 기능에 가장 적합한 시스템 제공 제목을 선택하십시오.

- Choose the filled or outlined location glyph
- >  채워지거나 윤곽이 잡힌 위치 글리프 선택

- Select a background color and a color for the title and glyph
- >  제목과 글리프의 배경색 및 색상을 선택합니다.

- Adjust the button’s corner radius
- >  단추의 모서리 반지름 조정


To help people recognize and trust location buttons, you can’t customize the button’s other visual attributes. The system also ensures a location button remains legible by warning you about problems like low-contrast color combinations or too much translucency. In addition to fixing such problems, you're responsible for making sure the text fits in the button — for example, button text needs to fit without truncation at all accessibility text sizes and when translated into other languages.
> 사용자가 위치 단추를 인식하고 신뢰할 수 있도록 단추의 다른 시각적 속성을 사용자 지정할 수 없습니다. 또한 이 시스템은 저대비 색상 조합 또는 너무 많은 투명도와 같은 문제에 대해 경고함으로써 위치 버튼을 읽기 쉽게 합니다. 이러한 문제를 해결할 뿐만 아니라 단추 텍스트가 단추에 맞는지 확인해야 합니다. 예를 들어 단추 텍스트는 모든 내게 필요한 텍스트 크기로 잘리지 않고 다른 언어로 번역될 때 잘려야 합니다.
>




**IMPORTANT**If the system identifies consistent problems with your customized location button, it won’t give your app access to the device location when people tap it. Although such a button can perform other app-specific actions, people may lose trust in your app if your location button doesn’t work as they expect.
> 중요 시스템이 사용자 지정 위치 단추의 일관된 문제를 식별하면 사용자가 장치 위치를 누를 때 앱에 액세스할 수 없습니다. 이러한 버튼은 다른 앱별 작업을 수행할 수 있지만 위치 버튼이 예상대로 작동하지 않으면 앱에 대한 신뢰를 잃을 수 있습니다.
>




# **Pre-alert screens**

Ideally, the current context helps people understand why you’re requesting their permission. If it’s essential to provide additional details, you can display a custom screen before the system alert appears. The following guidelines apply to custom screens that display before system alerts that request permission to access protected data and resources, including camera, microphone, location, contact, calendar, and tracking.
> 이상적인 경우, 현재 컨텍스트는 사용자가 자신의 권한을 요청하는 이유를 이해하는 데 도움이 됩니다. 추가 세부 정보를 제공해야 하는 경우 시스템 경고가 표시되기 전에 사용자 지정 화면을 표시할 수 있습니다. 다음 지침은 카메라, 마이크, 위치, 연락처, 일정관리 및 추적을 포함하여 보호된 데이터 및 리소스에 액세스할 수 있는 권한을 요청하는 시스템 경고 전에 표시되는 사용자 지정 화면에 적용됩니다.
>




**Include only one button and make it clear that it opens the system alert.** People can feel manipulated when a custom screen also includes a button that doesn’t open the alert because the experience diverts them from making their choice. Another type of manipulation is using a term like “Allow” to title the custom screen’s button. If the screen’s button seems similar in meaning and visual weight to the allow button in the alert, people can be more likely to choose the alert’s allow button without meaning to. Use a term like “Continue” or “Next” to title your custom screen’s single button, clarifying that its action is to open the system alert.
> 버튼 하나만 포함하고 시스템 경고가 열리는지 확인합니다. 사용자 지정 화면에 알림이 열리지 않는 버튼이 포함되어 있을 때 사람들은 조작되었다고 느낄 수 있다. 왜냐하면 경험으로 인해 선택을 할 수 없기 때문이다. 또 다른 유형의 조작은 사용자 정의 화면의 단추 제목을 "허용"과 같은 용어를 사용하는 것입니다. 화면의 버튼이 경고의 허용 버튼과 의미와 시각적 무게가 비슷해 보인다면, 사람들은 의도하지 않고 경고의 허용 버튼을 선택할 가능성이 높다. "계속" 또는 "다음"과 같은 용어를 사용하여 사용자 지정 화면의 단일 단추의 제목을 지정하여 시스템 경고를 여는 작업임을 명확히 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-correct-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-correct-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-correct-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-correct-2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

**Don’t include additional actions in your custom screen.** For example, don’t provide a way for people to leave the screen without viewing the system alert — like offering an option to close or cancel.
> 사용자 지정 화면에 추가 작업을 포함하지 마십시오. 예를 들어, 닫거나 취소할 수 있는 옵션 제공과 같이 사용자가 시스템 경고를 보지 않고 화면을 떠날 수 있는 방법을 제공하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-incorrect-5_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-incorrect-5_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-incorrect-6_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-incorrect-6_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

# **Tracking requests**

App tracking is a sensitive issue. In some cases, it might make sense to display a custom screen that describes the benefits of tracking. If you want to perform app tracking as soon as people launch your app, you must display the system-provided alert before you collect any tracking data.
> 앱 추적은 민감한 사안이다. 경우에 따라 추적의 이점을 설명하는 사용자 정의 화면을 표시하는 것이 합리적일 수 있습니다. 다른 사용자가 앱을 실행하는 즉시 앱 추적을 수행하려면 추적 데이터를 수집하기 전에 시스템에서 제공한 경고를 표시해야 합니다.
>




**Never precede the system-provided alert with a custom screen that could confuse or mislead people.** People sometimes tap quickly to dismiss alerts without reading them. A custom messaging screen that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.
> 시스템에 제공된 경고보다 먼저 사용자 지정 화면을 사용하면 사람을 혼란스럽게 하거나 오도할 수 있습니다. 사람들은 때때로 경고를 읽지 않고 빠르게 누르기 위해 경고를 무시한다. 이러한 행동을 이용하여 선택에 영향을 미치는 맞춤형 메시징 화면은 앱스토어 리뷰에 의해 거부될 것이다.
>




There are several prohibited custom-screen designs that will cause rejection. Some examples are offering incentives, displaying a screen that looks like a request, displaying an image of the alert, and annotating the screen behind the alert (as shown below). For guidance, see [App Store Review Guidelines: 5.1.1 (iv)](https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage).
> 거부 반응을 일으키는 몇 가지 금지된 사용자 지정 화면 설계가 있습니다. 인센티브 제공, 요청처럼 보이는 화면 표시, 경고 이미지 표시, 경고 뒤에 화면 주석 달기(아래 그림 참조) 등이 있습니다. 지침은 앱 스토어 검토 지침: 5.1.1(iv)을 참조하십시오.
>




• [Incentive](../patterns/accessing-private-data#)
• [Imitation request](../patterns/accessing-private-data#)
• [Alert image](../patterns/accessing-private-data#)
• [Alert annotation](../patterns/accessing-private-data#)

-

![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-incorrect-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/custom-messaging-incorrect-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

Don’t offer incentives for granting the request. You can’t offer people compensation for granting their permission, and you can’t withhold functionality or content or make your app unusable until people allow you to track them.
> 요청을 승인하는 데 대한 인센티브를 제공하지 마십시오. 당신은 사람들에게 그들의 허가를 내준 것에 대한 보상을 제공할 수 없으며, 사람들이 그들을 추적할 수 있도록 허락할 때까지 기능이나 콘텐츠를 보류하거나 당신의 앱을 사용할 수 없게 만들 수 없다.
>





# **Protecting data**

Protecting people’s information is paramount. Give people confidence in your app’s security and help preserve their privacy by taking advantage of system-provided security technologies when you need to store information locally, authorize people for specific operations, and transport information across a network.
> 사람들의 정보를 보호하는 것이 가장 중요하다. 로컬에 정보를 저장하고 특정 작업에 대한 권한을 부여하며 네트워크를 통해 정보를 전송해야 할 때 시스템에서 제공하는 보안 기술을 활용하여 앱 보안에 대한 신뢰를 제공하고 개인 정보를 보존할 수 있습니다.
>




Here are some high-level guidelines.

**Avoid relying solely on passwords for authentication.** Take advantage of other technologies like Touch ID, which lets people authenticate with a fingerprint. For developer guidance, see [Local Authentication](https://developer.apple.com/documentation/localauthentication).
> 인증확인을 위해 암호에만 의존하지 마십시오. 지문으로 인증할 수 있는 터치 ID와 같은 다른 기술을 활용하십시오. 개발자 지침은 로컬 인증을 참조하십시오.
>





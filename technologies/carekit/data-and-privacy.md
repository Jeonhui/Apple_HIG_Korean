# **[technologies-carekit] data-and-privacy**

Nothing is more important than protecting people’s privacy and safeguarding the extremely sensitive data your CareKit app collects and stores.
> 사람들의 사생활을 보호하고 CareKit 앱이 수집하고 저장하는 매우 민감한 데이터를 보호하는 것보다 더 중요한 것은 없다.
>




**Provide a coherent privacy policy.** During the app submission process, you must provide a URL to a clearly stated privacy policy, so that people can view the policy when they click the link in the App Store page for your app. For developer guidance, see [App information > App Store Connect help](https://help.apple.com/app-store-connect/#/dev219b53a88).
> 일관된 개인 정보 보호 정책을 제공하십시오. 앱 제출 과정에서 개인 정보 보호 정책에 대한 URL을 제공하여 사용자가 앱의 앱 스토어 페이지에 있는 링크를 클릭할 때 정책을 볼 수 있도록 해야 합니다. 개발자 안내는 앱 정보 > 앱스토어 커넥트 도움말을 참고하세요.
>




In addition to the data that people enter into your CareKit app, you may be able to access data through iOS features and capabilities. You must receive people's permission before accessing data through these features, and you must protect people's data whether people enter it into your app or you get it from the device or the system. For developer guidance, see [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting_user_privacy).
> 사용자가 CareKit 앱에 입력하는 데이터 외에도 iOS 기능을 통해 데이터에 액세스할 수 있습니다. 이러한 기능을 통해 데이터에 액세스하려면 먼저 사용자의 사용 권한을 받아야 하며, 사용자가 앱에 데이터를 입력하든 사용자가 장치 또는 시스템에서 데이터를 얻든 사용자의 데이터를 보호해야 합니다. 개발자 지침은 사용자 개인 정보 보호를 참조하십시오.
>




# **HealthKit integration**

HealthKit is the central repository for health and fitness data in iOS and watchOS. When you enable HealthKit in your CareKit app, you can ask people for permission to access and share their health and fitness data with designated caregivers.
> 헬스킷(HealthKit)은 iOS와 워치OS에서 건강 및 피트니스 데이터를 위한 중앙 저장소이다. CareKit 앱에서 HealthKit을 활성화하면 사람들에게 지정된 보호자와 자신의 건강 및 피트니스 데이터에 액세스하고 공유할 수 있는 권한을 요청할 수 있습니다.
>




**Request access to health data only when you need it.** It makes sense to request access to weight information when people log their weight, for example, but not immediately after your app launches. When your request is clearly related to the current context, you help people understand your app’s intentions. Also, people can change the permissions they grant, so your app should make a request every time it needs access. For developer guidance, see [requestAuthorization(toShare:read:completion:)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorization).
> 필요할 때만 건강 데이터에 대한 액세스를 요청하십시오. 예를 들어, 사람들이 체중을 기록할 때 체중 정보에 대한 액세스를 요청하는 것이 이치에 맞지만, 앱이 시작된 직후에는 요청하지 않습니다. 당신의 요청이 현재 상황과 명확하게 관련되어 있을 때, 당신은 사람들이 당신의 앱의 의도를 이해하도록 돕는다. 또한, 사람들은 자신이 부여한 권한을 변경할 수 있으므로, 앱은 액세스가 필요할 때마다 요청해야 합니다. 개발자 지침은 요청을 참조하십시오권한 부여(공유 대상: 읽기: 완료:).
>




**Clarify your app's intent by adding descriptive messages to the standard permission screen.**People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app. Avoid adding custom screens that replicate the standard permission screen’s behavior or content.
> 표준 권한 화면에 설명 메시지를 추가하여 앱의 의도를 명확히 합니다.사람들은 건강 데이터에 대한 액세스를 승인하라는 요청이 있을 때 시스템이 제공하는 권한 화면을 볼 것으로 예상한다. 당신이 왜 정보가 필요한지, 그리고 사람들이 당신의 앱과 정보를 공유함으로써 어떻게 이익을 얻을 수 있는지 설명하는 몇 가지 간결한 문장을 쓰세요. 표준 권한 화면의 동작이나 내용을 복제하는 사용자 정의 화면을 추가하지 마십시오.
>




**Manage health data sharing solely through the system’s privacy settings.** People expect to globally manage access to their health information in Settings > Privacy. Don’t confuse people by building additional screens in your app that affect the flow of health data.
> 시스템의 개인 정보 설정을 통해서만 건강 데이터 공유를 관리합니다. 사람들은 개인 정보 설정 > 개인 정보에서 자신의 건강 정보에 대한 접근을 전 세계적으로 관리하기를 기대합니다. 건강 데이터 흐름에 영향을 미치는 추가 화면을 앱에 구축하여 사람들을 혼란스럽게 하지 마십시오.
>




For related design guidance, see [HealthKit](../technologies/healthkit). For developer guidance, see [HealthKit](https://developer.apple.com/documentation/healthkit).
> 관련 설계 지침은 HealthKit를 참조하십시오. 개발자 지침은 HealthKit를 참조하십시오.
>




# **Motion data**

If it’s useful for treatment and if people give permission, your app can get motion information from the device to determine if people are standing still, walking, running, cycling, or driving. When people are walking or running, you can also determine the step count, pace, and number of flights of stairs ascended or descended.
> 치료에 유용하고 사람들이 허락하면 앱이 장치에서 모션 정보를 가져와 사람들이 가만히 서 있는지, 걷는지, 뛰는지, 자전거를 타는지, 운전하는지 확인할 수 있습니다. 사람들이 걷거나 달리고 있을 때 계단의 계단 수, 속도 및 상승 또는 하강 비행 횟수도 확인할 수 있습니다.
>




Motion information can also include custom data collected as part of physical therapy. For example, some ResearchKit tasks use device sensors to test flexibility, range of motion, and ambulatory capability.
> 동작 정보는 또한 물리 치료의 일부로 수집된 사용자 정의 데이터를 포함할 수 있다. 예를 들어, 일부 ResearchKit 작업은 장치 센서를 사용하여 유연성, 동작 범위 및 보행 능력을 테스트한다.
>




For developer guidance, see [Core Motion](https://developer.apple.com/documentation/coremotion).

# **Photos**

Pictures are a great way to communicate treatment progress. With people's permission, your app can access the device's camera and photos to share pictures with a care team. For example, a care plan might include a request for people to share periodic photos of an injury, so the physician can monitor the healing process.
> 사진은 치료 진행 상황을 전달하는 좋은 방법입니다. 사람들의 허가를 받으면, 당신의 앱은 장치의 카메라와 사진에 액세스하여 치료팀과 사진을 공유할 수 있다. 예를 들어, 치료 계획에는 의사가 치료 과정을 모니터링할 수 있도록 부상의 주기적인 사진을 공유하라는 요청이 포함될 수 있다.
>




For developer guidance, see [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller).

# **ResearchKit integration**

A ResearchKit app lets people participate in important medical research studies. Your CareKit app can incorporate ResearchKit features to display related surveys, tasks, and charts, if appropriate. ResearchKit also includes an informed consent module, which your CareKit app can use to request people's permission to collect and share data.
> ResearchKit 앱은 사람들이 중요한 의학 연구에 참여할 수 있게 해준다. CareKit 앱은 ResearchKit 기능을 통합하여 관련 설문조사, 작업 및 차트를 표시할 수 있습니다. 또한 ResearchKit에는 정보에 입각한 동의 모듈이 포함되어 있으며, 이 모듈을 사용하여 CareKit 앱을 사용하여 사람들에게 데이터 수집 및 공유 권한을 요청할 수 있습니다.
>




For related design guidance, see [ResearchKit](../technologies/researchkit). For developer guidance, see [Research & Care > Developers](https://www.researchandcare.org/developers/).
> 관련 설계 지침은 Research Kit를 참조하십시오. 개발자 안내는 리서치앤케어 > 개발자를 참고하세요.
>




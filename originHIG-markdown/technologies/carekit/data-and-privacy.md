# **[technologies-carekit] data-and-privacy**

Nothing is more important than protecting people’s privacy and safeguarding the extremely sensitive data your CareKit app collects and stores.

**Provide a coherent privacy policy.** During the app submission process, you must provide a URL to a clearly stated privacy policy, so that people can view the policy when they click the link in the App Store page for your app. For developer guidance, see [App information > App Store Connect help](https://help.apple.com/app-store-connect/#/dev219b53a88).

In addition to the data that people enter into your CareKit app, you may be able to access data through iOS features and capabilities. You must receive people's permission before accessing data through these features, and you must protect people's data whether people enter it into your app or you get it from the device or the system. For developer guidance, see [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting_user_privacy).

# **HealthKit integration**

HealthKit is the central repository for health and fitness data in iOS and watchOS. When you enable HealthKit in your CareKit app, you can ask people for permission to access and share their health and fitness data with designated caregivers.

**Request access to health data only when you need it.** It makes sense to request access to weight information when people log their weight, for example, but not immediately after your app launches. When your request is clearly related to the current context, you help people understand your app’s intentions. Also, people can change the permissions they grant, so your app should make a request every time it needs access. For developer guidance, see [requestAuthorization(toShare:read:completion:)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorization).

**Clarify your app's intent by adding descriptive messages to the standard permission screen.**People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app. Avoid adding custom screens that replicate the standard permission screen’s behavior or content.

**Manage health data sharing solely through the system’s privacy settings.** People expect to globally manage access to their health information in Settings > Privacy. Don’t confuse people by building additional screens in your app that affect the flow of health data.

For related design guidance, see [HealthKit](https://developer.apple.com/design/human-interface-guidelines/technologies/healthkit). For developer guidance, see [HealthKit](https://developer.apple.com/documentation/healthkit).

# **Motion data**

If it’s useful for treatment and if people give permission, your app can get motion information from the device to determine if people are standing still, walking, running, cycling, or driving. When people are walking or running, you can also determine the step count, pace, and number of flights of stairs ascended or descended.

Motion information can also include custom data collected as part of physical therapy. For example, some ResearchKit tasks use device sensors to test flexibility, range of motion, and ambulatory capability.

For developer guidance, see [Core Motion](https://developer.apple.com/documentation/coremotion).

# **Photos**

Pictures are a great way to communicate treatment progress. With people's permission, your app can access the device's camera and photos to share pictures with a care team. For example, a care plan might include a request for people to share periodic photos of an injury, so the physician can monitor the healing process.

For developer guidance, see [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller).

# **ResearchKit integration**

A ResearchKit app lets people participate in important medical research studies. Your CareKit app can incorporate ResearchKit features to display related surveys, tasks, and charts, if appropriate. ResearchKit also includes an informed consent module, which your CareKit app can use to request people's permission to collect and share data.

For related design guidance, see [ResearchKit](https://developer.apple.com/design/human-interface-guidelines/technologies/researchkit). For developer guidance, see [Research & Care > Developers](https://www.researchandcare.org/developers/).
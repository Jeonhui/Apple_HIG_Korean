CareKit
=======

People can use CareKit apps to manage care plans related to a chronic illness like diabetes, recover from an injury or surgery, or achieve health and wellness goals.![A sketch of the CareKit icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/ca3abb9c5686138572c9d3649257809f/technologies-CareKit-intro@2x.png)

To learn more about CareKit, see [Research & Care > CareKit](https://www.researchandcare.org/carekit/)
.

CareKit 2.0 contains two projects, CareKit UI and CareKit Store. CareKit UI provides a wide variety of prebuilt views you can use to create a custom CareKit app. CareKit Store defines a database scheme that incorporates CareKit entities — such as patients, care plans, tasks, and contacts — so you can store and manage data on the patient’s device. CareKit 2.0 provides seamless synchronization between your database and the UI, so you can always keep a care plan up to date. For developer guidance, see [CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit)
.

[Data and privacy](/design/human-interface-guidelines/carekit#Data-and-privacy)
-------------------------------------------------------------------------------

Nothing is more important than protecting people’s privacy and safeguarding the extremely sensitive data your CareKit app collects and stores.

**Provide a coherent privacy policy.** During the app submission process, you must provide a URL to a clearly stated privacy policy, so that people can view the policy when they click the link in the App Store page for your app. For developer guidance, see [App information > App Store Connect help](https://help.apple.com/app-store-connect/#/dev219b53a88)
.

In addition to the data that people enter into your CareKit app, you may be able to access data through iOS features and capabilities. You must receive people’s permission before accessing data through these features, and you must protect people’s data whether people enter it into your app or you get it from the device or the system. For developer guidance, see [Protecting user privacy](/documentation/healthkit/protecting_user_privacy)
.

### [HealthKit integration](/design/human-interface-guidelines/carekit#HealthKit-integration)

HealthKit is the central repository for health and fitness data in iOS and watchOS. When you support HealthKit in your CareKit app, you can ask people for permission to access and share their health and fitness data with designated caregivers.

**Request access to health data only when you need it.** It makes sense to request access to weight information when people log their weight, for example, but not immediately after your app launches. When your request is clearly related to the current context, you help people understand your app’s intentions. Also, people can change the permissions they grant, so it’s a good idea to make a request every time your app needs access. For developer guidance, see [`requestAuthorization(toShare:read:completion:)`](/documentation/healthkit/hkhealthstore/1614152-requestauthorization)
.

**Clarify your app’s intent by adding descriptive messages to the standard permission screen.** People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app. Avoid adding custom screens that replicate the standard permission screen’s behavior or content.

**Manage health data sharing solely through the system’s privacy settings.** People expect to globally manage access to their health information in Settings > Privacy. Don’t confuse people by building additional screens in your app that affect the flow of health data.

For related design guidance, see [HealthKit](/design/human-interface-guidelines/healthkit)
. For developer guidance, see [HealthKit](/documentation/healthkit)
.

### [Motion data](/design/human-interface-guidelines/carekit#Motion-data)

If it’s useful for treatment and if people give permission, your app can get motion information from the device to determine if people are standing still, walking, running, cycling, or driving. When people are walking or running, you can also determine the step count, pace, and number of flights of stairs ascended or descended.

Motion information can also include custom data collected as part of physical therapy. For example, some ResearchKit tasks use device sensors to test flexibility, range of motion, and ambulatory capability.

For developer guidance, see [Core Motion](/documentation/coremotion)
.

### [Photos](/design/human-interface-guidelines/carekit#Photos)

Pictures are a great way to communicate treatment progress. With people’s permission, your app can access the device’s camera and photos to share pictures with a care team. For example, a care plan might include a request for people to share periodic photos of an injury, so the physician can monitor the healing process.

For developer guidance, see [`UIImagePickerController`](/documentation/uikit/uiimagepickercontroller)
.

### [ResearchKit integration](/design/human-interface-guidelines/carekit#ResearchKit-integration)

A ResearchKit app lets people participate in important medical research studies. Your CareKit app can incorporate ResearchKit features to display related surveys, tasks, and charts, if appropriate. ResearchKit also includes an informed consent module, which your CareKit app can use to request people’s permission to collect and share data.

For related design guidance, see [ResearchKit](/design/human-interface-guidelines/researchkit)
. For developer guidance, see [Research & Care > Developers](https://www.researchandcare.org/developers/)
.

[CareKit views](/design/human-interface-guidelines/carekit#CareKit-views)
-------------------------------------------------------------------------

CareKit UI provides customizable views organized into three categories — tasks, charts, and contacts — and defines several default view styles in each. To design a CareKit app, you simply choose the view styles you need and supply CareKit Store data to display in them.

Each view category is designed to support specific types of content and interaction. To ensure a consistent experience, use each view type for its intended purpose.



| Category | Purpose |
| --- | --- |
| [Tasks](/design/human-interface-guidelines/carekit#Tasks)
 | Present tasks, like taking medication or doing physical therapy. Support logging of patient symptoms and other data. |
| [Charts](/design/human-interface-guidelines/carekit#Charts)
 | Display graphical data that can help people understand how their treatment is progressing. |
| [Contact views](/design/human-interface-guidelines/carekit#Contact-views)
 | Display contact information. Support communication through phone, message, and email, and link to a map of the contact’s location. |

![A screenshot of a CareKit app screen on iPhone that shows completed and uncompleted days, a medication task, a chart that compares the patient's nausea with their medication intake, and a logging task the patient can use to log each occurrence of nausea.](https://docs-assets.developer.apple.com/published/01c31ebd51f779053d69a726dfc7c719/carekit-tasks-and-charts@2x.png)Tasks and charts![A screenshot of a CareKit app screen on iPhone that shows contact information for two doctors, including buttons for phone, message, email, and map directions.](https://docs-assets.developer.apple.com/published/d092576dcf446a1bc1a66786674bf9ad/carekit-contacts@2x.png)ContactsA CareKit UI view consists of a header and may include a stack of content subviews. Located at the top of the view, the header can display text, a symbol, and a disclosure indicator, and can include a separator at its bottom edge. The content stack appears below the header and displays your content subviews in a vertical arrangement.

![An illustration of a CareKit task view. Callouts indicate the header area at the top of the view, which contains the title on the left and an optional disclosure indicator on the right. A subview area below the header includes circular checkmark buttons for marking off medication intake at different times of the day. Additional callouts point to the subview area and the horizontal separator between the header and the subview.](https://docs-assets.developer.apple.com/published/3d0bce479cd7fe334f28b0135309eee1/carekit-view-components@2x.png)

CareKit UI takes care of all the layout constraints within a view, so you don’t have to worry about breaking existing constraints when you add new subviews to the stack.

### [Tasks](/design/human-interface-guidelines/carekit#Tasks)

A care plan generally presents a set of prescribed actions for people to perform, such as taking medication, eating specific foods, exercising, or reporting symptoms. CareKit UI defines several styles of task views you can use to display prescribed actions. Typically, you customize a task view by providing the information to display, often by specifying data stored in an on-device CareKit Store database. In some cases, you might also supply custom UI elements.

A task can contain the following types of information.



| Information | Required | Description | Example value |
| --- | --- | --- | --- |
| Title | Yes | A word or short phrase that introduces the task. | *Ibuprofen* |
| Schedule | Yes | The schedule on which a task must be completed. | *Four times a day* |
| Instructions | No | Detailed instructions, recommendations, and warnings. | *Take 1 tablet every 4–6 hours (not to exceed 4 tablets daily).* |
| Group ID | No | An identifier you can use to group similar tasks in ways that make sense in your app. | A category identifier like *medication* or *exercise*. |

In CareKit 2.0, CareKit UI defines five styles of task views: simple, instructions, log, checklist, and grid. Each style is designed to support a particular use case.

**Use the simple style for a one-step task.** The default simple-style view consists of a header area that contains a title, subtitle, and button. You provide the title and subtitle, and you can provide a custom image to display in the button when the task is complete. If you don’t supply an image, CareKit shows that a task is complete by filling in the button and displaying a checkmark. Because the default simple-style view doesn’t include a content stack, consider using a different task style if you need to display additional content.

![An illustration of a task for taking a single dose of medicine at a specific time of day. The filled-in circle and checkmark indicate that the task is complete.](https://docs-assets.developer.apple.com/published/3dbf24cfe3257f20c8ff27069c826acc/carekit-simple-task@2x.png)

**Use the instructions style when you need to add informative text to a simple task.** For example, if a single-step medication task needs to include additional information — such as “Take on an empty stomach” or “Take at bedtime” — you can use an instructions-style task to display it.

![An illustration of a task for taking a single dose of medicine at a specific time of day. The task includes instructions for how to take the dose. Below the instructions, the task shows the word completed and a checkmark to indicate that the task is complete.](https://docs-assets.developer.apple.com/published/8fb94655f4b00d5c044aad450eac4d6e/carekit-instructions-task@2x.png)

**Use the log style to help people log events.** For example, you could use this task style to display a button people can tap whenever they feel nauseated. The log-style task can automatically display a timestamp every time the patient logs an event.

![An illustration of a task for logging incidents of nausea. The task's header area includes a title, a time range, and a disclosure button to display additional details. The subview area includes instructions, a Log button, and a time completed.](https://docs-assets.developer.apple.com/published/802fa318c201c93013e7fead995dedbc/carekit-log-task@2x.png)

**Use the checklist style to display a list of actions or steps in a multistep task.** For example, if people must take a medication three times per day, you could display the three scheduled times in a checklist. Each checklist item can include a text description and a button that people can tap to mark the item as done. By default, a checklist task can also display instructional text below the list.

![An illustration of a task that directs the patient to take a medicine at breakfast, lunch, and dinner. Filled-in circles containing checkmarks next to breakfast and lunch show that the patient has taken the first two doses.](https://docs-assets.developer.apple.com/published/c5cd3b6720e2907bbe5377a1fd8902a8/carekit-checklist-task@2x.png)

**Use the grid style to display a grid of buttons in a multistep task.** Like the checklist style, the grid style also supports a multistep task, but it displays the steps in a more compact arrangement. You can supply a succinct title for each button (if you need to provide additional description for each button, you might want to use the checklist style instead). By default, a grid-style task can also display instructional text below the grid of buttons. Unlike other task styles, the grid style gives you access to its underlying collection view, which means that you can display custom UI elements in the grid layout.

![An illustration of a task that consists of three circles that represent three doses of a medicine. The first two circles are filled in and contain checkmarks, indicating that the patient has already taken two doses.](https://docs-assets.developer.apple.com/published/80242c1b5b6d8d261e2e4261f00fce9b/carekit-grid-task@2x.png)

**Consider using color to reinforce the meaning of task items.** Color can be a good way to help people understand information at a glance. For example, you could use one color for medications and a different color for physical activities. Always avoid using color as the only way to convey information. For guidance, see [Color](/design/human-interface-guidelines/color)
.

**Combine accuracy with simplicity when describing a task and its steps.** For example, use a medication’s marketing name instead of its chemical description. Also, when the context of a task helps to clarify meaning, minimize the number of words you use. For example, a daily medication task generally tells people when to take specific medications, so it may be unnecessary to repeat words like *take*.

**Consider supplementing multistep or complex tasks with videos or images.** Visually demonstrating how to perform a task can help people avoid mistakes.

### [Charts](/design/human-interface-guidelines/carekit#Charts)

Chart views let you present data and trends in graphical ways that can help people visualize their progress in a care plan. CareKit chart views can display both current and historical data, and update automatically with new data.

In CareKit 2.0, CareKit UI provides three chart styles: bar, scatter, and line. For each style, you provide a descriptive title and subtitle, supply axis markers — like days of the week — and specify the data set.

![An illustration of a bar chart with days of the week on the x-axis and dosage numbers on the y-axis. The bar on Thursday reaches a value of two on the y-axis, indicating that the medicine was taken twice that day.](https://docs-assets.developer.apple.com/published/9309c7bf5a6b01637db66fee801b87a5/carekit-bar-chart@2x.png)Bar chart![An illustration of a scatter chart with days of the week on the x-axis and dosage numbers on the y-axis. A dot on Thursday reaches a value of two on the y-axis, indicating that the medicine was taken twice that day.](https://docs-assets.developer.apple.com/published/cb04ad1ad1a59a4de3ec48c880f8e161/carekit-scatter-chart@2x.png)Scatter chart![An illustration of a line chart with days of the week on the x-axis and dosage numbers on the y-axis. The line is at zero on the y-axis for all days but Thursday, where it reaches a value of two, indicating that the medicine was taken twice that day.](https://docs-assets.developer.apple.com/published/a4385195215d9349733467ab5132acf4/carekit-line-chart@2x.png)Line chart**Consider highlighting narratives and trends to illustrate progress.** For example, your app could display a bar chart that shows a correlation between the number of times people took medication and their level of pain. Displaying such data can encourage better adherence to a care plan.

**Label chart elements clearly and succinctly.** Long, detailed labels can make a chart difficult to read and understand. Keep labels short and avoid repeating the same information. For example, a heart rate chart might use the term *BPM* in an axis label instead of using it in the label of every data point.

**Use distinct colors.** In general, avoid using different shades of the same color to mean different things. Also ensure that you use colors with sufficient contrast. For related guidance, see [Color and effects](/design/human-interface-guidelines/accessibility#Color-and-effects)
.

**Consider providing a legend to add clarity.** If the colors you use to represent different types of data aren’t immediately clear, include a legend that clearly and succinctly describes them.

**Clearly denote units of time.** People need to know whether time-based data is represented in seconds, minutes, hours, days, weeks, months, or years. If you don’t want to include this information in individual data value labels, include it in an axis label or elsewhere on the chart.

**Consolidate large data sets for greater readability.** A large amount of data can make a chart unreadable by reducing the size of individual data points and presenting too much visible information. Look for ways to group and organize data for clarity and simplicity.

**If necessary, offset data to keep charts proportional.** It’s easy for very small data points to get lost or become unreadable in a chart that also contains very large data points. If the difference between data points is significant, find ways to offset or restructure the data so all data points are readable.

For developer guidance, see [CareKit > Chart Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/chart-interfaces)
. To learn about ResearchKit charts, see the [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit)
.

### [Contact views](/design/human-interface-guidelines/carekit#Contact-views)

A care plan typically includes a care team and other trusted individuals who can help patients follow the plan. CareKit UI defines a contact view you can use to help patients communicate with the people in their care plan.

In CareKit 2.0, CareKit UI provides two styles of the contact view: simple and detailed.

![An illustration of a simple contact view that displays a person glyph, followed by a doctor's name and practice type, and a disclosure button to display additional information.](https://docs-assets.developer.apple.com/published/91e7f82d3bd35b56a76ba229de9976f4/carekit-simple-contact@2x.png)Simple![An illustration of a detailed contact view that displays a person glyph, followed by a doctor's name and practice type in a header area. In a subview area, the view displays information about the doctor, and buttons for calling, messaging, emailing, and navigating to the doctor's physical address.](https://docs-assets.developer.apple.com/published/16cbd22d0341235eda0ab4e17b1a5a19/carekit-detailed-contact@2x.png)Detailed**Consider using color to categorize care team members.** Color can help people identify care team members at a glance.

[Notifications](/design/human-interface-guidelines/carekit#Notifications)
-------------------------------------------------------------------------

Notifications can tell people when it’s time to take medication or complete a task, and badging your app icon can show that there’s an unread message from a caregiver. Apple Watch can also display a notification from your app; for guidance, see [Notifications](/design/human-interface-guidelines/notifications)
.

**Minimize notifications.** Care plans vary from patient to patient. While one individual may have only a few daily tasks to complete, another may have a long list. Use notifications sparingly so people don’t feel overwhelmed. When possible, consider coalescing multiple items into a single notification.

**Consider providing a detail view.** In addition to providing more information, a notification detail view can help people take immediate action without leaving their current context to open your app. For example, you could use a notification detail view to display a list of pending tasks so that people can quickly mark them as complete.

[Symbols and branding](/design/human-interface-guidelines/carekit#Symbols-and-branding)
---------------------------------------------------------------------------------------

CareKit uses a variety of built-in symbols to help people understand what they can do in a care app. For example, CareKit can display the phone, messaging, and envelope symbols in a contact view and the clock symbol in a log-style task view.

Although you can customize the default symbols, most view styles work best with the CareKit-provided symbols. The exception is the highly customizable grid-style task view, which can display your custom UI in a grid layout.

In a grid view, you might want to display custom symbols that are relevant to the unique content and experience in your app. You could use symbols to indicate the grouping of tasks; for example, a pill to represent medication tasks, or a person walking to represent exercise tasks. In this scenario, consider using [SF Symbols](/design/human-interface-guidelines/sf-symbols)
 to illustrate custom items in your app.

Using SF Symbols in your app gives you:

* Designs that coordinate with CareKit’s visual design language
* Support for creating custom symbols to represent the unique content in your app

**Design a relevant care symbol.** If you need to customize a symbol, be sure the design is closely related to your app or the general concept of health and wellness. Avoid creating a purely decorative symbol or using a corporate logo as a custom symbol.

**Incorporate refined, unobtrusive branding.** People use CareKit apps to help them achieve their health and wellness goals; they don’t want to see advertising. To avoid distracting people from their care plan, subtly incorporate your brand through your app’s use of color and communication style.

[Platform considerations](/design/human-interface-guidelines/carekit#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/carekit#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/carekit#Related)

[Research & Care > CareKit](https://www.researchandcare.org/carekit/)


#### [Developer documentation](/design/human-interface-guidelines/carekit#Developer-documentation)

[CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit)


[Research & Care > Developers](https://www.researchandcare.org/developers/)


[Protecting user privacy](/documentation/healthkit/protecting_user_privacy)


[HealthKit](/documentation/healthkit)


[ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit)


#### [Videos](/design/human-interface-guidelines/carekit#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/196C46B0-DF68-4947-B211-4FEECE415A6E/3408_wide_250x141_1x.jpg) What's new in CareKit](https://developer.apple.com/videos/play/wwdc2020/10151) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/EAFF830B-8468-49BA-A5DC-D3A3E8B7F463/4960_wide_250x141_1x.jpg) Build a research and care app, part 1: Setup onboarding](https://developer.apple.com/videos/play/wwdc2021/10068) 
[Change log](/design/human-interface-guidelines/carekit#Change-log)
-------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| May 2, 2023 | Consolidated guidance into one page. |


June 21, 2023

 Updated to include guidance for visionOS. Modality
========

Modality is a design technique that presents content in a separate, focused mode that prevents interaction with the parent view and requires an explicit action to dismiss.![A sketch of an active window above an inactive window, suggesting focus on the frontmost window. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/9efb35fd7fafa01ce3447dc6f13ae2d8/patterns-modality-intro@2x.png)

Presenting content modally can:

* Ensure that people receive critical information and, if necessary, act on it
* Provide options that let people confirm or modify their most recent action
* Help people perform a distinct, narrowly scoped task without losing track of their previous context
* Give people an immersive experience or help them focus on a complex task

Depending on the platform, you might use different components to present these types of modal experiences. For example, all platforms can present an *alert*, which is modal view that delivers important information related to your app or game. In addition, each platform may define various types of modal views for presenting context-specific options, such as *activity views,* *sheets*, and *confirmation dialogs* or *action sheets*. To help people perform a distinct task, iOS, iPadOS, and macOS apps tend to use sheets or popovers, but iPadOS, macOS, and visionOS apps might also just use a separate window.

To provide a temporary experience, like viewing media, or to help people focus on a distinct, multistep task, like editing content, apps can offer a full-screen modal experience. In contrast, apps may also offer nonmodal types of full-screen experiences; for guidance, see [Going full screen](/design/human-interface-guidelines/going-full-screen)
. visionOS apps can offer a range of immersive experiences; for guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

[Best practices](/design/human-interface-guidelines/modality#Best-practices)
----------------------------------------------------------------------------

**Present content modally only when there’s a clear benefit.** A modal experience takes people out of their current context and requires an action to dismiss, so it’s important to use modality only when it helps people focus or make choices that affect their content or device.

**Aim to keep modal tasks simple, short, and narrowly focused.** If a modal task is too complicated, people can lose track of the task they suspended when they entered the modal view, especially if the modal view obscures their previous context.

**Take care to avoid creating a modal experience that feels like an app within your app.** In particular, presenting a hierarchy of views within a modal task can make people forget how to retrace their steps. If a modal task must contain subviews, provide a single path through the hierarchy and avoid including buttons that people might mistake for the button that dismisses the modal view.

**Consider using a full-screen modal style for in-depth content or a complex task.** A modal experience that fills the display or a window minimizes distractions, so it can work well for presenting videos, photos, or camera views, or to support a multistep task like marking up a document or editing a photo.

**Always give people an obvious way to dismiss a modal view.** In general, it works well to follow the platform conventions people already know. For example, in iOS, iPadOS, and watchOS apps, people typically expect to find a button in the navigation bar or swipe down; in macOS and tvOS apps, people expect to find a button in the main content view.

**When necessary, help people avoid data loss by getting confirmation before closing a modal view.** Regardless of whether people use a dismiss gesture or a button, if closing the view could result in the loss of user-generated content, be sure to explain the situation and give people ways to resolve it. For example, in iOS, you might present an action sheet that includes a save option.

**Make it easy to identify a modal view’s task.** When people enter a modal view, they switch away from their previous context and might not return to it right away. When you provide a title that names the modal view’s task — or additional text that describes the task or provides guidance — you can help people keep their place in your app.

**Avoid presenting a modal view on top of another modal view.** Multiple modal views onscreen at the same time can be confusing because people must remember more than one previous context. Although an alert can appear on top of all other content to deliver critical information, having more than one alert onscreen at the same time is very confusing.

[Platform considerations](/design/human-interface-guidelines/modality#Platform-considerations)
----------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/modality#Resources)
------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/modality#Related)

[Action sheets](/design/human-interface-guidelines/action-sheets)


[Activity views](/design/human-interface-guidelines/activity-views)


[Alerts](/design/human-interface-guidelines/alerts)


[Popovers](/design/human-interface-guidelines/popovers)


[Sheets](/design/human-interface-guidelines/sheets)


#### [Developer documentation](/design/human-interface-guidelines/modality#Developer-documentation)

[Presentation modifiers](/documentation/SwiftUI/View-Presentation)


[`UIModalPresentationStyle`](/documentation/uikit/uimodalpresentationstyle)


[Modal Windows and Panels](/documentation/appkit/nsapplication/modal_windows_and_panels)


#### [Videos](/design/human-interface-guidelines/modality#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/6E076CE0-7DDF-4471-B6F0-005ADF9C7960/6500_wide_250x141_1x.jpg) What’s new in iPad app design](https://developer.apple.com/videos/play/wwdc2022/10009) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/95386734-286A-4C41-8073-28AC9A155F44/6490_wide_250x141_1x.jpg) Explore navigation design for iOS](https://developer.apple.com/videos/play/wwdc2022/10001) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/48/0F960683-D91F-4CA9-9658-6FBB11F0683D/3272_wide_250x141_1x.jpg) What's New in iOS Design](https://developer.apple.com/videos/play/wwdc2019/808) 
[Change log](/design/human-interface-guidelines/modality#Change-log)
--------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |


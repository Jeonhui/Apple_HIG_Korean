June 21, 2023

 Consolidated guidance into new page and updated for visionOS. Privacy
=======

Privacy is paramount: it’s critical to be transparent about the privacy-related data and resources you require and essential to protect the data people allow you to access.![A sketch of an upright hand, suggesting protection. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/161fec1d77c705ccf076fb4c67d32f5c/foundations-privacy-intro@2x.png)

People use their devices in very personal ways and they expect apps to help them preserve their privacy.

When you submit a new or updated app, you must provide details about your privacy practices and the privacy-relevant data you collect so the App Store can display the information on your product page. (You can manage this information at any time in [App Store Connect](https://help.apple.com/app-store-connect/#/dev1b4647c5b)
.) People use the privacy details on your product page to make an informed decision before they download your app. To learn more, see [App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/)
.

![A screenshot of the App Privacy screen in an app’s App Store product page. The top card in the screen is titled Data Used to Track You and lists contact info, location, and identifiers. The bottom card is titled Data Linked to You and lists financial and contact info, location, purchases, identifiers, and browsing history.](https://docs-assets.developer.apple.com/published/6b45cc81a35043309fac0da19d280cd5/privacy-practices@2x.png)An app’s App Store product page helps people understand the app’s privacy practices before they download it.[Best practices](/design/human-interface-guidelines/privacy#Best-practices)
---------------------------------------------------------------------------

**Request access only to data that you actually need.** Asking for more data than a feature needs — or asking for data before a person shows interest in the feature — can make it hard for people to trust your app. Give people precise control over their data by making your permission requests as specific as possible.

**Be transparent about how your app collects and uses people’s data.** People are less likely to be comfortable sharing data with your app if they don’t understand exactly how you plan to use it. Always respect people’s choices to use system features like Hide My Email and Mail Privacy Protection, and be sure you understand your obligations with regard to app tracking. To learn more about Apple privacy features, see [Privacy](https://www.apple.com/privacy/)
; for developer guidance, see [User privacy and data use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
.

**Process data on the device where possible.** In iOS, for example, you can take advantage of the Apple Neural Engine and custom CreateML models to process the data right on the device, helping you avoid lengthy and potentially risky round trips to a remote server.

**Adopt system-defined privacy protections and follow security best practices.** For example, in iOS 15 and later, you can rely on CloudKit to provide encryption and key management for additional data types, like strings, numbers, and dates.

[Requesting permission](/design/human-interface-guidelines/privacy#Requesting-permission)
-----------------------------------------------------------------------------------------

Here are several examples of the things you must request permission to access:

* Personal data, including location, health, financial, contact, and other personally identifying information
* User-generated content like emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, and audio, video, and photo content
* Protected resources like Bluetooth peripherals, home automation features, Wi-Fi connections, and local networks
* Device capabilities like camera and microphone
* In a visionOS app running in a Full Space, ARKit data, such as hand tracking, plane estimation, image anchoring, and world tracking
* The device’s advertising identifier, which supports app tracking

The system provides a standard alert that lets people view each request you make. You supply copy that describes why your app needs access, and the system displays your description in the alert. People can also view the description — and update their choice — in Settings > Privacy.

**Request permission only when your app clearly needs access to the data or resource.** It’s natural for people to be suspicious of a request for personal information or access to a device capability, especially if there’s no obvious need for it. Ideally, wait to request permission until people actually use an app feature that requires access. For example, you can use the [location button](/design/human-interface-guidelines/privacy#Location-button)
 to give people a way to share their location after they indicate interest in a feature that needs that information.

**Avoid requesting permission at launch unless the data or resource is required for your app to function.** People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it. For example, people understand that a navigation app needs access to their location before they can benefit from it. Similarly, before people can play a visionOS game that lets them bounce virtual objects off walls in their surroundings, they need to permit the game to access information about their surroundings.

**Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting.** The standard alert displays your copy (called a *purpose string* or *usage description string*) after your app name and before the buttons people use to grant or deny their permission. Aim for a brief, complete sentence that’s straightforward, specific, and easy to understand. Use sentence case, avoid passive voice, and include a period at the end. For developer guidance, see [Requesting access to protected resources](/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources)
 and [App Tracking Transparency](/documentation/apptrackingtransparency)
.



|  | Example purpose string | Notes |
| --- | --- | --- |
| A checkmark in a circle to indicate a correct example. | The app records during the night to detect snoring sounds. | An active sentence that clearly describes how and why the app collects the data. |
| An X in a circle to indicate an incorrect example. | Microphone access is needed for a better experience. | A passive sentence that provides a vague, undefined justification. |
| An X in a circle to indicate an incorrect example. | Turn on microphone access. | An imperative sentence that doesn’t provide any justification. |

Here are several examples of the standard system alert:

* [Example 1](#)
* [Example 2](#)
* [Example 3](#)
![A screenshot of a permission alert for the Pal About app displaying a purpose string that reads Allow Pal About to access your location? Turning on location services allows us to show you when pals are nearby. Below the string is a small map image containing the Precise On notice and below the map are three buttons in a stack. From the top, the buttons are titled Allow Once, Allow While Using App, and Don’t Allow.](https://docs-assets.developer.apple.com/published/7606b1f491c09048bf8bd03b45ed36f8/permission-request-1@2x.png)![A screenshot of a permission alert for the Pal About app displaying a purpose string that reads Pal About would like to access your photos. Allow access to photos to upload photos from your library. The string is followed by three buttons in a stack. From the top, the buttons are titled Select Photos, Allow Access to All Photos, and Don’t Allow.](https://docs-assets.developer.apple.com/published/6c22cace0599c2630e86cebb50f28ba8/permission-request-2@2x.png)![A screenshot of a permission alert for the Pal About app displaying a purpose string that reads Allow Pal About to access your contacts? Find friends using Pal About and add them to your pal network. The string is followed by two side-by-side buttons: Don’t Allow and Allow.](https://docs-assets.developer.apple.com/published/7e87848e5908661a78eb73aee3976e73/permission-request-3@2x.png)### [Pre-alert screens, windows, or views](/design/human-interface-guidelines/privacy#Pre-alert-screens-windows-or-views)

Ideally, the current context helps people understand why you’re requesting their permission. If it’s essential to provide additional details, you can display a custom screen or window before the system alert appears. The following guidelines apply to custom views that display before system alerts that request permission to access protected data and resources, including camera, microphone, location, contact, calendar, and tracking.

**Include only one button and make it clear that it opens the system alert.** People can feel manipulated when a custom screen or window also includes a button that doesn’t open the alert because the experience diverts them from making their choice. Another type of manipulation is using a term like “Allow” to title the custom screen’s button. If the custom button seems similar in meaning and visual weight to the allow button in the alert, people can be more likely to choose the alert’s allow button without meaning to. Use a term like “Continue” or “Next” to title the single button in your custom screen or window, clarifying that its action is to open the system alert.

![A screenshot of an app’s pre-alert screen that reads Allow tracking on the next screen for special offers and promotions just for you, advertisements that match your interests, an improved personalized experience over time. You can change this option later in the Settings app. Below the text is a button titled Continue.](https://docs-assets.developer.apple.com/published/fc7f233de9ee89f9dbdb48c175225a59/custom-messaging-correct-1@2x.png)![A checkmark in a circle to indicate a correct example.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![A screenshot of the Pal About app’s pre-alert screen that reads Turning on location services allows us to provide features like: alerts when your pals are nearby, news of events happening near you, tagging and sharing your location. Below the text is a button titled Next and below the button is text that reads You can change this later in the Settings app.](https://docs-assets.developer.apple.com/published/237274110e00048cc265d0f0042dd0c8/custom-messaging-correct-2@2x.png)![A checkmark in a circle to indicate a correct example.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

**Don’t include additional actions in your custom screen or window.** For example, don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel.

![A screenshot of an app’s pre-alert screen highlighted to show a button titled Cancel that appears below the Continue button.](https://docs-assets.developer.apple.com/published/6ff09ed38ef7b3823347bc240c48b347/custom-messaging-incorrect-5@2x.png)![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

![A screenshot of an app’s pre-alert screen highlighted to show a Close button in the top-left corner and a More button in the top-right corner. The Continue button appears near the bottom of the screen.](https://docs-assets.developer.apple.com/published/6910c5e5f213833465fb3d06c6e9689a/custom-messaging-incorrect-6@2x.png)![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

### [Tracking requests](/design/human-interface-guidelines/privacy#Tracking-requests)

App tracking is a sensitive issue. In some cases, it might make sense to display a custom screen or window that describes the benefits of tracking. If you want to perform app tracking as soon as people launch your app, you must display the system-provided alert before you collect any tracking data.

**Never precede the system-provided alert with a custom screen or window that could confuse or mislead people.** People sometimes tap quickly to dismiss alerts without reading them. A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.

There are several prohibited custom-screen designs that will cause rejection. Some examples are offering incentives, displaying a screen or window that looks like a request, displaying an image of the alert, and annotating the screen behind the alert (as shown below). To learn more, see [App Store Review Guidelines: 5.1.1 (iv)](https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage)
.

* [Incentive](#)
* [Imitation request](#)
* [Alert image](#)
* [Alert annotation](#)
![A screenshot of an app’s pre-tracking message that reads Allow tracking and get a $100 credit toward your next purchase. Below the text is an image of a dollar sign inside a circle. Below the image is a button titled Get $100 credit.](https://docs-assets.developer.apple.com/published/cd97429e2555ad384979258c510fcf30/custom-messaging-incorrect-1@2x.png)![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)Don’t offer incentives for granting the request. You can’t offer people compensation for granting their permission, and you can’t withhold functionality or content or make your app unusable until people allow you to track them.![A screenshot of an app’s pre-tracking message that reads Allow tracking for a better experience. Below the text is a bar graph image that shows four bars increasing in height from left to right. Below the graph is a button titled Allow Tracking.](https://docs-assets.developer.apple.com/published/754adf94fd632793b649b54acaac0ecd/custom-messaging-incorrect-2@2x.png)![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)Don’t display a custom screen that mirrors the functionality of the system alert. In particular, don’t create a button title that uses “Allow” or similar terms, because people don’t allow anything in a pre-alert screen.![A screenshot of an app’s pre-tracking message that reads Choose Allow when prompted. Below the text is an image of the system-provided alert. Below the image is a button titled Continue. An Allow button in the system-provided alert image is circled.](https://docs-assets.developer.apple.com/published/7a5177d4bc1460b472577ea5e93ae61e/custom-messaging-incorrect-3@2x.png)![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)Don’t show an image of the standard alert and modify it in any way.![A screenshot of an app’s pre-tracking message that reads Allow tracking for a better experience. The app’s custom screen also includes an upward-pointing arrow and the words Choose Allow in the lower third of the screen. Because the system-provided alert displays on top of the custom screen, the arrow appears to be pointing to the alert’s Allow button.](https://docs-assets.developer.apple.com/published/e3f463b819afea891f0e7cab188e466b/custom-messaging-incorrect-4@2x.png)![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)Don’t draw a visual cue that draws people’s attention to the system alert’s Allow button.[Location button](/design/human-interface-guidelines/privacy#Location-button)
-----------------------------------------------------------------------------

In iOS, iPadOS, and watchOS, Core Location provides a button so people can grant your app temporary authorization to access their location at the moment a task needs it. A location button’s appearance can vary to match your app’s UI and it always communicates the action of location sharing in a way that’s instantly recognizable.

![An image of a lozenge-shaped blue button that displays a white location indicator — that is, a narrow arrow head shape that points to the top right — followed by the text Current Location.](https://docs-assets.developer.apple.com/published/2d4e44adec80170cec96d3446617e700/location-button@2x.png)

The first time people open your app and tap a location button, the system displays a standard alert. The alert helps people understand how using the button limits your app’s access to their location, and reminds them of the location indicator that appears when sharing starts.

![A screenshot of the alert displayed by the location button that appears on top of a background image showing a partial map of Northern California. The alert reads Park Finder can only access your location when you choose to share it. When you share your location with this app, a blue location indicator will appear in the status bar. Below this text the alert displays a small image of the map, zoomed in to show part of Cupertino. Below the map are two buttons; from the top the titles are OK and Not Now.](https://docs-assets.developer.apple.com/published/465bee128d71f71d03d20d6d9bb175db/location-button-alert@2x.png)After people confirm their understanding of the button’s action, simply tapping the location button gives your app one-time permission to access their location. Although each one-time authorization expires when people stop using your app, they don’t need to reconfirm their understanding of the button’s behavior.

Note

If your app has no authorization status, tapping the location button has the same effect as when a person chooses *Allow Once* in the standard alert. If people previously chose *While Using the App*, tapping the location button doesn’t change your app’s status. For developer guidance, see [`LocationButton`](/documentation/corelocationui/locationbutton)
 (SwiftUI) and [`CLLocationButton`](/documentation/corelocationui/cllocationbutton)
 (Swift).

**Consider using the location button to give people a lightweight way to share their location for specific app features.** For example, your app might help people attach their location to a message or post, find a store, or identify a building, plant, or animal they’ve encountered in their location. If you know that people often grant your app *Allow Once* permission, consider using the location button to help them benefit from sharing their location without having to repeatedly interact with the alert.

**Consider customizing the location button to harmonize with your UI.** Specifically, you can:

* Choose the system-provided title that works best with your feature, such as “Current Location” or “Share My Current Location.”
* Choose the filled or outlined location glyph.
* Select a background color and a color for the title and glyph.
* Adjust the button’s corner radius.

To help people recognize and trust location buttons, you can’t customize the button’s other visual attributes. The system also ensures a location button remains legible by warning you about problems like low-contrast color combinations or too much translucency. In addition to fixing such problems, you’re responsible for making sure the text fits in the button — for example, button text needs to fit without truncation at all accessibility text sizes and when translated into other languages.

Important

If the system identifies consistent problems with your customized location button, it won’t give your app access to the device location when people tap it. Although such a button can perform other app-specific actions, people may lose trust in your app if your location button doesn’t work as they expect.

[Protecting data](/design/human-interface-guidelines/privacy#Protecting-data)
-----------------------------------------------------------------------------

Protecting people’s information is paramount. Give people confidence in your app’s security and help preserve their privacy by taking advantage of system-provided security technologies when you need to store information locally, authorize people for specific operations, and transport information across a network.

Here are some high-level guidelines.

**Avoid relying solely on passwords for authentication.** Where possible, use [passkeys](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/)
 to replace passwords. If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see [Securing Logins with iCloud Keychain Verification Codes](/documentation/authenticationservices/securing_logins_with_icloud_keychain_verification_codes)
). To further protect access to apps that people keep logged in on their device, use biometric identification like Face ID, Optic ID, or Touch ID. For developer guidance, see [Local Authentication](/documentation/localauthentication)
.

**Store sensitive information in a keychain.** A keychain provides a secure, predictable user experience when handling someone’s private information. For developer guidance, see [Keychain Services](/documentation/security/keychain_services)
.

**Never store passwords or other secure content in plain-text files.** Even if you restrict access using file permissions, sensitive information is much safer in an encrypted keychain.

**Avoid inventing custom authentication schemes.** If your app requires authentication, prefer system-provided features like [passkeys](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/)
, [Sign in with Apple](/design/human-interface-guidelines/sign-in-with-apple)
 or [Password AutoFill](/documentation/security/password_autofill)
. For related guidance, see [Managing accounts](/design/human-interface-guidelines/managing-accounts)
.

[Platform considerations](/design/human-interface-guidelines/privacy#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, tvOS, or watchOS.*

### [macOS](/design/human-interface-guidelines/privacy#macOS)

**Sign your app with a valid Developer ID.** If you choose to distribute your app outside the store, signing your app with Developer ID identifies you as an Apple developer and confirms that your app is safe to use. For developer guidance, see [Xcode Help](https://developer.apple.com/go/?id=ios-app-distribution-guide)
.

**Protect people’s data with app sandboxing.** Sandboxing provides your app with access to system resources and user data while protecting it from malware. All apps submitted to the Mac App Store require sandboxing. For developer guidance, see [Configuring the macOS App Sandbox](/documentation/Xcode/configuring-the-macos-app-sandbox)
.

**Avoid making assumptions about who is signed in.** Because of fast user switching, multiple people may be active on the same system.

### [visionOS](/design/human-interface-guidelines/privacy#visionOS)

By default, visionOS uses ARKit algorithms to handle features like persistence, world mapping, segmentation, matting, and environment lighting. These algorithms are always running, allowing apps and games to automatically benefit from ARKit while in the Shared Space.

ARKit doesn’t send data to apps in the Shared Space; to access ARKit APIs, your app must open a Full Space. Additionally, features like Plane Estimation, Scene Reconstruction, Image Anchoring, and Hand Tracking require people’s permission to access any information. For developer guidance, see [Setting up access to ARKit data](/documentation/visionOS/setting-up-access-to-arkit-data)
.

In visionOS, user input is private by design. The system automatically displays hover effects when people bring focus to components that you create using SwiftUI or RealityKit, giving people the visual feedback they need without exposing the direction of their gaze before they tap. For guidance, see [Focus and selection](/design/human-interface-guidelines/focus-and-selection)
 and [Gestures > visionOS](/design/human-interface-guidelines/gestures#visionOS)
.

Developer access to device cameras works differently in visionOS than it does in other platforms. Specifically, the back camera provides blank input and is only available as a compatibility convenience; the front camera provides input for [Spatial Personas](/design/human-interface-guidelines/shareplay#visionOS)
, but only after people grant their permission. If the iOS or iPadOS app you’re bringing to visionOS includes a feature that needs camera access, remove it or replace it with an option for people to import content instead. For developer guidance, see [Checking whether your existing app is compatible with visionOS](/documentation/visionOS/checking-whether-your-app-is-compatible-with-visionos)
.

[Resources](/design/human-interface-guidelines/privacy#Resources)
-----------------------------------------------------------------

#### [Developer documentation](/design/human-interface-guidelines/privacy#Developer-documentation)

[Requesting access to protected resources](/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources)


[Security](/documentation/security)


#### [Videos](/design/human-interface-guidelines/privacy#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/B39F07BE-4E7A-4530-8BB9-B1C319F262EE/3354_wide_250x141_1x.jpg) Design for location privacy](https://developer.apple.com/videos/play/wwdc2020/10162) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/03EB5BF9-AF52-4140-BBCA-4B3D4DD99C96/4998_wide_250x141_1x.jpg) Meet the Location Button](https://developer.apple.com/videos/play/wwdc2021/10102) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/A6395752-EED6-4F4D-9910-6D7B5867BC28/4978_wide_250x141_1x.jpg) Apple’s privacy pillars in focus](https://developer.apple.com/videos/play/wwdc2021/10085) 
[Change log](/design/human-interface-guidelines/privacy#Change-log)
-------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Consolidated guidance into new page and updated for visionOS. |


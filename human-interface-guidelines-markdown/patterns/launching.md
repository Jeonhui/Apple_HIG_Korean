June 21, 2023

 Updated to include guidance for visionOS. Launching
=========

People appreciate a streamlined launch experience that helps them start using your app or game immediately.![A sketch of a square containing an arrow pointing to the upper-right corner, suggesting a transition to a new state. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/5ef419551a96fe1df7df2bd5d610b5dc/patterns-launching-intro@2x.png)

[Best practices](/design/human-interface-guidelines/launching#Best-practices)
-----------------------------------------------------------------------------

**If the platform requires it, provide a launch screen.** In iOS, iPadOS, and tvOS, the system displays a launch screen the moment your app or game starts and quickly replaces it with your first screen, giving people the impression that your experience is fast and responsive. The ideal launch screen is effectively invisible to people, because it simply provides a context for your initial content; for guidance, see [Launch screens](/design/human-interface-guidelines/launching#Launch-screens)
. macOS, visionOS, and watchOS apps don’t need launch screens.

**Ask for initial setup information only when necessary.** Help people accomplish something as soon as they start your app or game, letting them be successful before you request additional information. As much as possible, get setup information from existing device settings and defaults. If people need to sign in before doing anything useful, consider offering [Sign in with Apple](/design/human-interface-guidelines/sign-in-with-apple)
, or relying on a synchronization service, such as iCloud.

**Ask for permission to access private data at the right time.** When possible, avoid asking for permission to access private data when your app launches; instead, request permission after people indicate their interest in a feature that requires their private data. For example, a navigation app probably needs access to location information right away, but an app that includes a navigation-related feature doesn’t need location information until people want to use that feature. In visionOS, an app must be running in a [Full Space](/design/human-interface-guidelines/immersive-experiences)
 before it can request access to information such as hand position or details about a person’s surroundings. For guidance, see [Privacy](/design/human-interface-guidelines/privacy)
.

**Give people time to enjoy your app before showing supplementary information or asking for a review.** At first launch, people want to dive right in; they don’t want to be required to read a lot of content or provide a rating before they get a sense of the experience you offer. To help you streamline first launch, consider:

* Letting the App Store display agreements and disclaimers so people can read them before downloading your app
* Asking for ratings and reviews after people gain enough experience with your app to accurately rate it and provide a substantive review that potential customers might find helpful (for guidance, see [Ratings and reviews](/design/human-interface-guidelines/ratings-and-reviews)
)

**Restore the previous state when your app restarts so people can continue where they left off.** Avoid making people retrace steps to reach their previous location in your app or game. Restore granular details of the previous state as much as possible. For example, scroll the view to people’s most recent position, and display windows in the same state and location in which people left them.

[Launch screens](/design/human-interface-guidelines/launching#Launch-screens)
-----------------------------------------------------------------------------

Not every platform requires a launch screen.

* iOS, iPadOS, and tvOS apps must supply a launch screen.
* macOS, visionOS, and watchOS apps don’t need a launch screen.

A launch screen isn’t an onboarding experience or a splash screen, and it isn’t an opportunity for artistic expression. A launch screen’s sole function is to enhance the perception of your experience as quick to launch and immediately ready to use.

**Design a launch screen that’s nearly identical to the first screen of your app.** If you include elements that look different when the app finishes launching, people may experience an unpleasant flash between the launch screen and the first screen of the app. Also make sure that your launch screen matches the device’s current appearance, such as [Dark Mode](/design/human-interface-guidelines/dark-mode)
.

![An illustration that represents the Safari launch screen, which shows default status bar content, an empty rounded rectangle for the URL field, and a tab bar populated with standard Safari tab bar buttons.](https://docs-assets.developer.apple.com/published/cf915d3ef01f48e80d113be95f9fc36a/launch-screen@2x.png)Launch screen![An illustration that represents an apple.com webpage rendered in Safari.](https://docs-assets.developer.apple.com/published/9374c53c3471385f2681a71700186d12/first-screen@2x.png)First screen**Avoid including text on your launch screen.** Because the content in a launch screen doesn’t change, any text you display won’t be localized.

**Downplay the launch experience.** Design a launch screen that smooths the transition to the first screen of your app or game; avoid designing a launch screen that delays people from immediately getting into the experience.

**Don’t advertise.** The launch screen isn’t a branding opportunity. Avoid creating a screen that looks like a splash screen or an “About” window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen. If your game or other immersive app displays a solid color before transitioning to the first screen, create a launch screen that displays only that solid color.

[Platform considerations](/design/human-interface-guidelines/launching#Platform-considerations)
-----------------------------------------------------------------------------------------------

*No additional considerations for macOS or watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/launching#iOS-iPadOS)

**Launch in the appropriate orientation.** If your app supports both portrait and landscape modes, launch using the device’s current orientation. If your app only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only app responds correctly, regardless of whether people entered landscape orientation by rotating the device left or right. For guidance, see [Layout](/design/human-interface-guidelines/layout)
.

### [tvOS](/design/human-interface-guidelines/launching#tvOS)

Unlike the [layered images](/design/human-interface-guidelines/images#Layered-images)
 throughout much of a tvOS app, the launch screen is static.

**In a live-viewing app, consider automatically starting playback soon after people start the app.** People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see [Live-viewing apps](/design/human-interface-guidelines/live-viewing-apps)
.

### [visionOS](/design/human-interface-guidelines/launching#visionOS)

**Launch as quickly as possible.** If your app doesn’t load content quickly, the system displays a window that contains your app icon. This window uses the same background appearance and dimensions as the first window you open while running in the Shared Space; if your app is running in a Full Space, the window uses a system-defined size.

**Consider launching in the Shared Space even if your app is fully immersive.** Opening a window in the Shared Space lets you provide more context about your app while giving it time to load, and it also lets you present a control that people can use to open your fully immersive experience. In general, people appreciate being able to choose when to transition to a Full Space, especially if they’re currently running other apps in the Shared Space. For guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

[Resources](/design/human-interface-guidelines/launching#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/launching#Related)

[Onboarding](/design/human-interface-guidelines/onboarding)


[Loading](/design/human-interface-guidelines/loading)


#### [Developer documentation](/design/human-interface-guidelines/launching#Developer-documentation)

[Specifying your app’s launch screen](/documentation/Xcode/specifying-your-apps-launch-screen)


[Responding to the launch of your app](/documentation/uikit/app_and_environment/responding_to_the_launch_of_your_app)


#### [Videos](/design/human-interface-guidelines/launching#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/48/38776A03-1056-4A47-9AB0-E4A8652AD5C4/2662_wide_250x141_1x.jpg) Optimizing App Launch](https://developer.apple.com/videos/play/wwdc2019/423) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/7/2C48F507-180B-4858-BB26-488C234B067F/1920_wide_250x141_1x.jpg) Love at First Launch](https://developer.apple.com/videos/play/wwdc2017/816) 
[Change log](/design/human-interface-guidelines/launching#Change-log)
---------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |


# **[patterns] launching**

# People appreciate a streamlined launch experience so they can start using your app or game immediately.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-launching-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-launching-intro-dark_2x.png)

# **Best practices**

**Provide a launch screen if the platform requires it.** In iOS, iPadOS, and tvOS, the system displays a launch screen the moment your app or game starts and quickly replaces it with your first screen, giving people the impression that your experience is fast and responsive. The ideal launch screen is effectively invisible to people, because it simply provides a context for your initial content. watchOS and macOS apps don't need launch screens.

**Ask for initial setup information only when necessary.** Help people accomplish something as soon as they start your app or game, letting them be successful before you request additional information. As much as possible, get setup information from existing device settings and defaults. If people need to sign in before doing anything useful, consider offering [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/introduction), or relying on a synchronization service, such as iCloud.

**Give people time to start enjoying your app before showing supplementary information, asking for a review, or making permission requests.** At first launch, people want to dive right in; they don’t want to be required to read a lot of content, provide a rating, or grant access to their private data before they get a sense of the experience you offer. To help you streamline first launch, consider:

- Letting the App Store display agreements and disclaimers so people can read them before downloading your app
- Asking for ratings and reviews after people gain enough experience with your app to accurately rate it and provide a substantive review that potential customers might find helpful (for guidance, see [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/patterns/ratings-and-reviews))
- When possible, requesting permission after people indicate that they’re interested in sharing their private data (for guidance, see [Accessing private data](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data))

**Restore the previous state when your app restarts so people can continue where they left off.** Avoid making people retrace steps to reach their previous location in your app or game. Restore granular details of the previous state as much as possible. For example, scroll the view to people’s most recent position, and display windows in the same state and location in which people left them.

# **Launch screens**

A launch screen isn’t an onboarding experience or a splash screen, and it isn’t an opportunity for artistic expression. A launch screen’s sole function is to enhance the perception of your experience as quick to launch and immediately ready to use.

Not every platform requires a launch screen.

- iOS, iPadOS, and tvOS apps must supply a launch screen.
- watchOS and macOS apps don’t need a launch screen.

**Design a launch screen that’s nearly identical to the first screen of your app.** If you include elements that look different when the app finishes launching, people may experience an unpleasant flash between the launch screen and the first screen of the app. Also make sure that your launch screen matches the device's current appearance, such as [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/foundations/dark-mode).

![https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/launch-screen.png](https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/launch-screen.png)

Launch screen

![https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/first-screen.png](https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/first-screen.png)

First screen

**Avoid including text on your launch screen.** Because the content in a launch screen doesn't change, any text you display won’t be localized.

**Downplay the launch experience.** Design a launch screen that smooths the transition to the first screen of your app or game; avoid designing a launch screen that delays people from immediately getting into the experience.

**Don’t advertise.** The launch screen isn’t a branding opportunity. Avoid creating a screen that looks like a splash screen or an "About" window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen. If your game or other immersive app displays a solid color before transitioning to the first screen, create a launch screen that displays only that solid color.

# **Platform considerations**

*No additional considerations for macOS or watchOS.*

# **iOS, iPadOS**

**Launch in the appropriate orientation.** If your app supports both portrait and landscape modes, launch using the device’s current orientation. If your app only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only app responds correctly, regardless of whether people entered landscape orientation by rotating the device left or right. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/foundations/layout).

# **tvOS**

Unlike the [layered images](https://developer.apple.com/design/human-interface-guidelines/foundations/images/#layered-images) throughout much of a tvOS app, the launch screen is static.

**In a live-viewing app, consider automatically starting playback soon after people start the app.** People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/patterns/live-viewing-apps).
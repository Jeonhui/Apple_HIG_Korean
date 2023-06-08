# **[technologies-app-clips] user-experience**

# **Designing a great App Clip experience**

App Clips focus on offering the fastest solution possible to a task, and they remain on a device for a limited amount of time while preserving people’s privacy. As a result, it’s especially important to give careful consideration to your App Clip's features, user experience, and interface design.

**Focus on essential features.** Interactions with App Clips are quick and focused. Limit features to what’s necessary to accomplish the task at hand. Reserve advanced or complex features for the app.

**Don’t use App Clips solely for marketing purposes.** App Clips should provide real value and help people accomplish tasks. Don’t use them as a means to advertise services or products, and don’t display ads in your App Clip.

**Avoid using web views in your App Clip.** App Clips use native components and frameworks to offer an app-quality experience. If only web components are available to you, offer a quick link to your website instead of an App Clip.

**Design a linear, easy-to-use, and focused user interface.** App Clips shouldn’t have tab bars, complex navigation, or settings. Keep the number of screens and entry forms to a minimum. Remove extraneous information and reduce complexity in the user interface wherever possible.

**On launch, show the most relevant part of your App Clip.** Skip unnecessary steps and take people immediately to the part of the App Clip that best fits their context.

**Ensure people can use your App Clip immediately.** App Clips include all required assets, omit splash screens, and never make people wait on launch.

**Ensure your App Clip is small.** The smaller your App Clip, the faster it will launch on a person’s device. Keeping your App Clip small is especially important when bandwidth is limited. As much as possible, reduce unnecessary code and remove unused assets. Avoid downloading additional data, which can take away the feeling of immediacy.

**Make the App Clip shareable.** When a user shares a link to an App Clip in the Messages app, recipients can launch the App Clip from within the Messages app. Offer the ability to share links to specific points in your App Clip, and encourage people to share the App Clip with others.

**Make it easy to pay for a service or product.** Entering payment information can be a long and error-prone task. Consider supporting [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/introduction) to offer express checkout and enable people to enter shipping information with no typing.

![https://developer.apple.com/design/human-interface-guidelines/technologies/app-clips/images/app-clips-purchase-with-applepay_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/app-clips/images/app-clips-purchase-with-applepay_2x.png)

**Avoid requiring people to create an account before they can benefit from your App Clip.**Creating an account is a complex task that takes time and effort. Consider not requiring an account, or think about asking people to create an account after they finish a task. If your App Clip requires an account to provide value, limit the amount of information people need to provide — for example, by offering [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/introduction).

**Provide a familiar, focused experience in your app.** When people install the full app, it replaces the App Clip on their device. From this moment, invocations that would have launched the App Clip launch the full app instead. Ensure your app provides a focused, familiar experience to people who previously used the App Clip. Don’t require additional steps that slow people down; for example, don’t require people to log in again when they transition from the App Clip to the app.

# **Preserving privacy**

The system imposes limits on App Clips to ensure people’s privacy. For example, App Clips can’t perform background operations. For developer guidance, see [Choosing the right functionality for your App Clip](https://developer.apple.com/documentation/app_clips/choosing_the_right_functionality_for_your_app_clip).

**Limit the amount of data you store and handle yourself.** If you need to store people’s data — for example, login information — store it securely. In addition, don’t rely on the availability of data you previously stored on the device — the system may have removed the App Clip from the device between launches and deleted all of its data. If you store login information, securely store it off the device.

**Consider offering Sign in with Apple.** Sign in with Apple securely retains login information off people’s devices and preserves their privacy. For guidance, see [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/introduction).

**Offer a secure way to pay for services or goods that also respects people’s privacy.** For example, consider offering [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/introduction).

# **Showcasing your app**

People don’t manage App Clips themselves, and App Clips don’t appear on the Home screen. Instead, the system removes an App Clip after a period of inactivity.

Because apps remain the best way to keep people engaged over time, the system helps them discover and install the full app:

- On the App Clip card, people can either launch the App Clip or visit the full app’s page on the App Store.
- When people first launch the App Clip, the system displays an app banner at the top of the screen. Like the App Clip card, the banner allows people to visit the app’s page on the App Store.

In addition, you can display an overlay in your App Clip that allows people to download the full app from within the App Clip. However, be mindful of when you recommend your app to people.

![https://developer.apple.com/design/human-interface-guidelines/technologies/app-clips/images/app-clips-card-focus_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/app-clips/images/app-clips-card-focus_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/app-clips/images/app-clips-appstore-focus_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/app-clips/images/app-clips-appstore-focus_2x.png)

**Don’t compromise the user experience by asking people to install the full app.** Instead, consider whether the App Clip card and the system-provided app banner provide enough incentive for people to download the full app. App Clips don’t require people to install the full app to complete a task.

**Pick the right time to recommend your app.** Give people the opportunity to try out your App Clip and understand its value. Only recommend the full app to people who use your App Clip repeatedly, or after they complete a task.

**Recommend your app in a nonintrusive, polite way.** Don’t ask people to install the full app repeatedly or interrupt them during a task. Push notifications aren’t a good way to ask people to install the app either. Clearly communicate your app’s additional features.

For developer guidance, see [Recommending your app to App Clip users](https://developer.apple.com/documentation/app_clips/recommending_your_app_to_app_clip_users).

# **Limiting notifications**

App Clips provide the option to schedule and receive notifications for up to 8 hours after launch, enough time to follow up and complete most common tasks.

**Only ask for permission to use notifications for an extended period of time if it’s really needed.** If your App Clip’s functionality spans more than a day, explicitly request the user’s permission to schedule and receive notifications. For example, a car rental company’s App Clip can ask for permission to send a notification that reminds people that they need to return a rented car soon.

**Keep notifications focused.** App Clips don’t have an ongoing relationship with the user, making it especially important to only send relevant notifications. Don’t send purely promotional notifications, and only use notifications in response to an explicit user action. If a person completes their task without leaving the App Clip, notifications might not be needed at all.

**Use notifications to help people complete a task.** An App Clip’s notifications relate directly to the task the App Clip helps to accomplish. For example, an App Clip that allows people to order food could send notifications related to a scheduled delivery.

For developer guidance, see [Enabling notifications in App Clips](https://developer.apple.com/documentation/app_clips/enabling_notifications_in_app_clips).

# **Creating App Clips for businesses**

If you’re a platform provider who services businesses, you may create several App Clip experiences in [App Store Connect](https://appstoreconnect.apple.com/) and use a single App Clip to power them all. To people using the App Clip, it appears with the branding of an individual business or location instead of your own branding.

**Use consistent branding.** When people see the App Clip card for a business, the brand for that business is front and center. Tone down your own branding and make sure the branding for the business is clearly visible to avoid confusing people when they enter the App Clip experience.

**Consider multiple businesses.** An App Clip may power many different businesses or a business that has multiple locations. In both scenarios, people may end up using the App Clip for more than one business or location at a time. The App Clip must handle this use case and update its user interface accordingly. For example, consider a way to switch between recent businesses or locations within your App Clip, and verify the user’s location when they launch it.

For developer guidance, see [Configuring the launch experience of your App Clip](https://developer.apple.com/documentation/app_clips/configuring_the_launch_experience_of_your_app_clip).
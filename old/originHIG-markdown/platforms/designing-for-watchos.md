# **[Platforms] Designing for watchOS**

### When people glance at their Apple Watch, they know they can access essential information and perform simple, timely tasks whether they’re stationary or in motion.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/platforms/platform-watchOS-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/platforms/platform-watchOS-intro-dark_2x.png)

As you begin designing your app for Apple Watch, start by understanding the following fundamental device characteristics and patterns that distinguish the watchOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app that Apple Watch users appreciate.

**Display.** The small Apple Watch display fits on the wrist while delivering an easy-to-read, high-resolution experience.

**Ergonomics.** Because people wear Apple Watch, they’re usually no more than a foot away from the display as they raise their wrist to view it and use their opposite hand to interact with the device. In addition, the Always On display lets people view information on the watch face when they drop their wrist.

**Inputs.** Using standard [Multi-Touch gestures](https://developer.apple.com/design/human-interface-guidelines/inputs/touchscreen-gestures) like tap, swipe, and drag lets people control their experience even while they’re in motion. Turning the [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/inputs/digital-crown) imparts additional precision and feedback to scrolling interfaces, pressing the [Action button](https://developer.apple.com/design/human-interface-guidelines/inputs/action-button) initiates an essential action without looking at the screen, and using [Siri Shortcuts](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions) can help people perform their routine tasks quickly and easily. People also appreciate taking advantage of data that device features — like GPS, sensors for blood oxygen and heart function, altimeter, accelerometer, and gyroscope — can provide.

**App interactions.** People often glance at the Always On display many times throughout the day, performing focused app interactions that can last for less than a minute each. People frequently use a watchOS app’s related experiences — like complications, notifications, and Siri interactions — more than they use the app itself.

**System features.** watchOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

- [Complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications)
- [Notifications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications)
- [Always On](https://developer.apple.com/design/human-interface-guidelines/technologies/always-on)
- [Faces](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/watch-faces)

# **Best practices**

Great Apple Watch experiences integrate the platform and device capabilities that people value most. To help your experience feel at home in watchOS, prioritize the following ways to incorporate these features and capabilities.

- Enable quick, glanceable interactions that deliver critical information succinctly and help people perform targeted actions with a simple gesture or two.
- Personalize the experience by proactively anticipating people’s needs and using on-device data to provide actionable content that’s relevant in the moment or very soon.
- Use [complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications) to provide relevant, potentially dynamic data and graphics right on the watch face where people can view them on every wrist raise and tap them to dive straight into your app.
- Use [notifications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications) to deliver timely, high-value information and enable important actions people can take without opening your app.
- Support Siri to help people access shortcuts on the Siri watch face.
- Design your app to function independently, complementing your notifications and complications by providing additional details and functionality.
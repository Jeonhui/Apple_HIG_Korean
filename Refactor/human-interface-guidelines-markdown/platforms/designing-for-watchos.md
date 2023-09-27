Designing for watchOS
========================

When people glance at their Apple Watch, they know they can access essential information and perform simple, timely tasks whether they’re stationary or in motion.  
![A stylized representation of an Apple Watch frame shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4fb079e34e794b1a6b9fc03acf2c22a4/platforms-watchOS-intro@2x.png)

As you begin designing your app for Apple Watch, start by understanding the following fundamental device characteristics and patterns that distinguish the watchOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app that Apple Watch users appreciate.  


**Display.** The small Apple Watch display fits on the wrist while delivering an easy-to-read, high-resolution experience.  


**Ergonomics.** Because people wear Apple Watch, they’re usually no more than a foot away from the display as they raise their wrist to view it and use their opposite hand to interact with the device. In addition, the Always On display lets people view information on the watch face when they drop their wrist.  


**Inputs.** People can navigate vertically or inspect data by turning the   
[Digital Crown](/design/human-interface-guidelines/digital-crown)
, which offers consistent control on the watch face, the Home Screen, and within apps. They can provide input even while they’re in motion with standard   
[touchscreen gestures](/design/human-interface-guidelines/touchscreen-gestures)
 like tap, swipe, and drag. Pressing the   
[Action button](/design/human-interface-guidelines/action-button)
 initiates an essential action without looking at the screen, and using   
[shortcuts](/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)
 helps people perform their routine tasks quickly and easily. People can also take advantage of data that device features provide, such as GPS, sensors for blood oxygen and heart function, and the altimeter, accelerometer, and gyroscope.  


**App interactions.** People glance at the Always On display many times throughout the day, performing concise app interactions that can last for less than a minute each. People frequently use a watchOS app’s related experiences — like complications, notifications, and Siri interactions — more than they use the app itself.  


**System features.** watchOS provides several features that help people interact with the system and their apps in familiar, consistent ways.  


* [Complications](/design/human-interface-guidelines/complications)
* [Notifications](/design/human-interface-guidelines/notifications)
* [Always On](/design/human-interface-guidelines/always-on)
* [Watch faces](/design/human-interface-guidelines/watch-faces)

[Best practices](/design/human-interface-guidelines/designing-for-watchos#Best-practices)
-----------------------------------------------------------------------------------------

Great Apple Watch experiences are focused, specialized, and integrate the platform and device capabilities that people value most. To help your experience feel at home in watchOS, prioritize the following ways to incorporate these features and capabilities.  


* Support quick, glanceable, single-screen interactions that deliver critical information succinctly and help people perform targeted actions with a simple gesture or two.
* Minimize the depth of hierarchy in your app’s navigation, and use the   
[Digital Crown](/design/human-interface-guidelines/digital-crown)
 to provide vertical navigation for scrolling or switching between screens.
* Personalize the experience by proactively anticipating people’s needs and using on-device data to provide actionable content that’s relevant in the moment or very soon.
* Use   
[complications](/design/human-interface-guidelines/complications)
 to provide relevant, potentially dynamic data and graphics right on the watch face where people can view them on every wrist raise and tap them to dive straight into your app.
* Use   
[notifications](/design/human-interface-guidelines/notifications)
 to deliver timely, high-value information and let people perform important actions without opening your app.
* Use background content such as   
[color](/design/human-interface-guidelines/color)
 to convey useful supporting information, and use   
[materials](/design/human-interface-guidelines/materials)
 to illustrate hierarchy and a sense of place.
* Support Siri to help people access shortcuts on the Siri watch face.
* Design your app to function independently, complementing your notifications and complications by providing additional details and functionality.

[Resources](/design/human-interface-guidelines/designing-for-watchos#Resources)
-------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/designing-for-watchos#Related)

[Apple Design Resources](https://developer.apple.com/design/resources/#watchos-apps)


#### [Developer documentation](/design/human-interface-guidelines/designing-for-watchos#Developer-documentation)

[Planning your watchOS app](https://developer.apple.com/watchos/planning/)


#### [Videos](/design/human-interface-guidelines/designing-for-watchos#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/69EC76C8-B751-49E6-9B2D-ED5A7D633A9D/8195_wide_250x141_1x.jpg) Design and build apps for watchOS 10](https://developer.apple.com/videos/play/wwdc2023/10138)
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/56D03FE8-0566-429A-81D2-2F6566031498/8390_wide_250x141_1x.jpg) Design widgets for the Smart Stack on Apple Watch](https://developer.apple.com/videos/play/wwdc2023/10309)
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/0A411518-17FD-4D2E-8C52-E55D97FA61F9/8059_wide_250x141_1x.jpg) Update your app for watchOS 10](https://developer.apple.com/videos/play/wwdc2023/10031)
[Change log](/design/human-interface-guidelines/designing-for-watchos#Change-log)
---------------------------------------------------------------------------------
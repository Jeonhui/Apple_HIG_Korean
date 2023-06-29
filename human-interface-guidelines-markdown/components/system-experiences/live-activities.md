June 5, 2023

 Updated guidance to include features of iOS 17 and iPadOS 17. Live Activities
===============

A Live Activity displays up-to-date information from your app, allowing people to view the progress of events or tasks at a glance.![A stylized representation of the dynamic island, in collapsed and expanded form, displaying the score of a live sporting event. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/05e81f3cb457f179fa1343f0753499c7/components-live-activities-intro@2x.png)

Live Activities help people keep track of tasks and events they care about, offering persistent locations for displaying information that updates frequently. For example, a food delivery app could display the time remaining until a food order arrives, or a sports app could display the score for an ongoing game.

In addition to displaying a Live Activity on the Lock Screen, devices that support Live Activities can display your app information in different ways, depending on whether the device supports the Dynamic Island.

* On devices that support the Dynamic Island, the system displays Live Activities in a persistent location around the TrueDepth camera.
* On devices that don’t support the Dynamic Island, the system can display a Live Activity update in a banner that appears briefly at the top of the screen.

[Appearances](/design/human-interface-guidelines/live-activities#Appearances)
-----------------------------------------------------------------------------

Live Activities appear in highly visible locations and extend your app’s reach to the Lock Screen, in the Dynamic Island, and as an overlay at the top of the screen. To ensure a Live Activity works well on all devices that support it, in all system-determined presentations, and that it feels like a natural extension of your app, you must support the following presentation types.

For developer guidance, see [ActivityKit](/documentation/ActivityKit)
.

**Compact:** In the Dynamic Island, the system uses the compact presentation when there’s only one Live Activity that’s currently active. The compact presentation is composed of two separate presentations: one that displays on the leading side of the TrueDepth camera and one that displays on the trailing side. Although the leading and trailing presentations are separate views, they form a cohesive view in the Dynamic Island, representing a single piece of information from your app. People can tap a compact Live Activity to open the app and get more details about the event or task.

![An illustration that shows the compact leading and compact trailing views in the Dynamic Island.](https://docs-assets.developer.apple.com/published/5de0db1a358dfccca20d67ecf1e32876/type-compact@2x.png)

**Minimal:** When multiple Live Activities are active, the system uses the minimal presentation to display two of them in the Dynamic Island. One Live Activity appears attached to the Dynamic Island while the other appears detached. Depending on its content size, the detached minimal Live Activity appears circular or oval. As with a compact Live Activity, people tap a minimal Live Activity to open the app and get more details about the event or task.

![An illustration that shows the minimal view in the Dynamic Island.](https://docs-assets.developer.apple.com/published/2c38a9a60566204bec5e3c335430544f/type-minimal@2x.png)

**Expanded:** When people touch and hold a Live Activity in a compact or minimal presentation, the system displays the content in an expanded presentation.

![An illustration that shows the expanded view in the Dynamic Island.](https://docs-assets.developer.apple.com/published/267300864fe5ab09d171f4b6d1cb55d0/type-expanded@2x.png)

**Lock Screen:** On the Lock Screen, the system uses the Lock Screen presentation to display a banner at the bottom of the screen. This presentation should use a layout similar to the expanded presentation.

![A screenshot of a Live Activity on the Lock Screen of iPhone that supports the Dynamic Island.](https://docs-assets.developer.apple.com/published/7859a0d79d91b03dc6bc6581c02b2ea2/live-activity-lock-screen@2x.png)**Devices that don’t support the Dynamic Island:** On devices that don’t support the Dynamic Island, the system uses the Lock Screen presentation of your Live Activity as a banner that briefly overlays the Home Screen or another app. This happens only when an update to your Live Activity contains an alert configuration.

![A screenshot of a Live Activity that appears as a banner on the Home Screen of iPhone without Dynamic Island support.](https://docs-assets.developer.apple.com/published/d124eab5adf9b06af473c23e0d95a878/live-activity-notch@2x.png)

**iPhone in StandBy:** In StandBy, the system displays the Live Activity in the minimal detached appearance. People tap it to see the Lock Screen appearance, scaled to fill the screen.

[Best practices](/design/human-interface-guidelines/live-activities#Best-practices)
-----------------------------------------------------------------------------------

**Offer a Live Activity for tasks and live events that have a defined beginning and end.** People use Live Activities to track events with frequently updating data or to monitor the status of ongoing tasks. Don’t offer a Live Activity for a task that exceeds eight hours, and always end a Live Activity immediately after the task completes or the event ends.

**Present only the most essential content.** People appreciate getting a summary and key bits of information about an ongoing task or event; they don’t expect to receive extensive detail in a Live Activity.

**Use animations to bring attention to content updates.** Live Activities use system and custom animations with a maximum duration of two seconds. Note that the system doesn’t perform animations on Always-On displays with reduced luminance. To learn which animations are available, see [Displaying live data with Live Activities](/documentation/ActivityKit/displaying-live-data-with-live-activities)
.

**Avoid displaying sensitive information in a Live Activity.** A Live Activity is visually prominent and could be viewed by casual observers. If people might consider the information in your Live Activity to be sensitive or private, display an innocuous summary and let people tap the Live Activity to get more information in your app.

**Avoid using a Live Activity to display ads or promotions.** Live Activities help people stay informed about ongoing events and tasks, so it’s important to display only information that’s related to those events and tasks.

**Support StandBy.** When a person taps the minimal presentation in StandBy, the system scales the Lock Screen appearance by 2x to fill the screen. Make sure your assets look great in the scaled-up presentation.

### [Making Live Activities interactive](/design/human-interface-guidelines/live-activities#Making-Live-Activities-interactive)

**Make sure tapping the Live Activity opens your app at the right location.** Take people directly to details and actions related to the Live Activity — don’t require them to navigate to the relevant screen. For developer guidance on SwiftUI views that can deep link to specific screens in your app, see [`Link`](/documentation/SwiftUI/Link)
 and [`widgetURL(_:)`](/documentation/WidgetKit/DynamicIsland/widgetURL(_:))
.

**Allow people to interact with your app or respond to event or progress updates.** Starting with iOS 17 and iPadOS 17, the expanded appearance in the Dynamic Island and the Lock Screen appearance can include buttons or toggles. Use them to allow people to respond to updated data. For example, a food ordering app could show a button in its Live Activity that people tap to check in at a restaurant when they pick up a takeout order.

### [Starting, updating, and ending a Live Activity](/design/human-interface-guidelines/live-activities#Starting-updating-and-ending-a-Live-Activity)

**Give people control over beginning and ending Live Activities.** Provide buttons to stop or cancel a Live Activity in the linked view in your app. This gives people control over content on their Lock Screen and in the Dynamic Island.

**Automatically start a Live Activity when people expect it.** Although it’s a good idea to provide a button people can use to start a Live Activity from within your app, there are situations in which people are likely to expect a Live Activity to start automatically. For example, if people use your app to start a task or event — such as ordering food for delivery or making a rideshare request — it makes sense to automatically initiate a Live Activity as soon as a person places an order or makes a request. In Settings, people can turn off Live Activities for your app, so it’s important to avoid surprising people by starting a Live Activity they don’t expect.

**Update a Live Activity only when new content is available, alerting people only if it’s essential to get their attention.** It can be disruptive to alert people to a Live Activity update, and alerting them too often — or alerting them to updates that aren’t crucial — can annoy people and encourage them to stop using your app’s Live Activities.

**Consider removing a Live Activity from the Lock Screen 15 minutes after it ends.** In the Dynamic Island, the system immediately removes a Live Activity when it ends. By default, the system shows a Live Activity on the Lock Screen for up to four hours after it ends to give people time to view its final content update. In many cases, though, the outcome of a Live Activity is only relevant for a shorter time, and 15 minutes is adequate. Alternatively, you can tell the system to dismiss it at a specific time within the four-hour window or immediately after it ends.

### [Creating a consistent design](/design/human-interface-guidelines/live-activities#Creating-a-consistent-design)

**Ensure unified information and design of the compact presentations in the Dynamic Island.** The TrueDepth camera separates the compact leading and compact trailing presentations of a Live Activity, but the contents of both need to read as a single piece of information, and tapping either presentation needs to take people to the same screen in your app. Consider using color to help reinforce the relationship of content, like text and icons.

**Create consistent layouts between compact and expanded presentations.** The expanded presentation is an enlarged version of the compact presentation. Ensure that information and layouts expand predictably when the Live Activity transitions from compact to expanded presentation.

**Consider using a consistent design in both Lock Screen and expanded presentations.** A consistent design approach helps people become familiar with your content and learn how to track the progress of a Live Activity in different locations.

**Adapt to different screen sizes and Live Activity presentations.** Live Activities scale to adapt to the screen sizes of different devices. Ensure a Live Activity looks great on every device by supplying content at appropriate sizes. As you create layouts and assets for various devices and scale factors, use the values listed in [Specifications](/design/human-interface-guidelines/live-activities#Specifications)
 as guidance, but note that the actual size on screen may vary or change.

**Coordinate the corner radius of your content with the corner radius of the Live Activity.** Margins between content items and the Live Activity edge need to be consistent. To ensure that your content looks good within a Live Activity’s rounded corners, use a SwiftUI container to apply the correct corner radius. For developer guidance, see [`ContainerRelativeShape`](/documentation/SwiftUI/ContainerRelativeShape)
.

**In general, use standard margins to ensure your content is legible.** For the expanded and Lock Screen presentations, the standard margin width is 20 points. In some cases — such as for graphics and buttons — you might need to use tighter margins to avoid crowding edges or creating a cluttered appearance. For developer guidance, see [`padding(_:_:)`](/documentation/SwiftUI/View/padding(_:_:))
.

### [Choosing colors](/design/human-interface-guidelines/live-activities#Choosing-colors)

**Consider carefully before using a custom background color and opacity on the Lock Screen.** If you set a background color or image for Live Activities that appear on the Lock Screen, test colors to be sure they offer enough contrast — especially tint colors on an Always-On display with reduced luminance. Note that you can’t choose a custom background color for Live Activity presentations that appear in the Dynamic Island. However, you can apply a custom tint color for text, symbols, and a border that surrounds the Dynamic Island. For developer guidance, see [Displaying live data with Live Activities](/documentation/ActivityKit/displaying-live-data-with-live-activities)
.

**Choose colors that work well on a personalized Lock Screen.** People customize their Lock Screen with wallpaper, custom tint colors, and widgets. To make a Live Activity fit a custom Lock Screen aesthetic while remaining legible, apply custom tint colors and opacity sparingly.

**Support Dark Mode and Always On.** A Live Activity adapts its colors to look great in both the light and dark appearances and on an Always-On display with reduced luminance. For guidance, see [Dark Mode](/design/human-interface-guidelines/dark-mode)
 and [Always On](/design/human-interface-guidelines/always-on)
; for developer guidance, see [About asset catalogs](https://help.apple.com/xcode/mac/current/#/dev10510b1f7)
.

[Platform considerations](/design/human-interface-guidelines/live-activities#Platform-considerations)
-----------------------------------------------------------------------------------------------------

*Not supported in macOS, tvOS, visionOS, or watchOS.*

[Specifications](/design/human-interface-guidelines/live-activities#Specifications)
-----------------------------------------------------------------------------------

As you design your Live Activities, use the following values for guidance.

### [The Dynamic Island](/design/human-interface-guidelines/live-activities#The-Dynamic-Island)

The Dynamic Island uses a corner radius of 44 points, and its rounded corner shape matches the TrueDepth camera.



| Presentation type | Device | Dynamic Island width (points) |
| --- | --- | --- |
| Compact or minimal | iPhone 14 Pro Max | 250 |
|  | iPhone 14 Pro | 230 |
| Expanded | iPhone 14 Pro Max | 408 |
|  | iPhone 14 Pro | 371 |

### [iOS Live Activity dimensions](/design/human-interface-guidelines/live-activities#iOS-Live-Activity-dimensions)

All values listed in the table below are in points.



| Screen dimensions (portrait) | Compact leading | Compact trailing | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen (height given as a range) |
| --- | --- | --- | --- | --- | --- |
| 430x932 | 62.33x36.67 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 |
| 393x852 | 52.33x36.67 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 |

### [iPadOS Live Activity dimensions](/design/human-interface-guidelines/live-activities#iPadOS-Live-Activity-dimensions)

All values listed in the table below are in points.



| Screen dimensions (portrait) | Lock Screen (height given as a range) |
| --- | --- |
| 1366x1024 | 500x84–160 |
| 1194x834 | 425x84–160 |
| 1012x834 | 425x84–160 |
| 1080x810 | 425x84–160 |
| 1024x768 | 425x84–160 |

[Resources](/design/human-interface-guidelines/live-activities#Resources)
-------------------------------------------------------------------------

#### [Developer documentation](/design/human-interface-guidelines/live-activities#Developer-documentation)

[ActivityKit](/documentation/ActivityKit)


[SwiftUI](/documentation/SwiftUI)


[WidgetKit](/documentation/WidgetKit)


[Developing a WidgetKit strategy](/documentation/WidgetKit/Developing-a-WidgetKit-strategy)


#### [Videos](/design/human-interface-guidelines/live-activities#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/73CFB4C1-8568-43E9-AECF-D679A7355B99/8255_wide_250x141_1x.jpg) Design dynamic Live Activities](https://developer.apple.com/videos/play/wwdc2023/10194) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/B13DB71E-9E8F-4A86-88B3-306C4E772627/8244_wide_250x141_1x.jpg) Meet ActivityKit](https://developer.apple.com/videos/play/wwdc2023/10184) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/E8F2CADC-14F4-4F73-9421-705E2A99A353/8245_wide_250x141_1x.jpg) Update Live Activities with push notifications](https://developer.apple.com/videos/play/wwdc2023/10185) 
[Change log](/design/human-interface-guidelines/live-activities#Change-log)
---------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Updated guidance to include features of iOS 17 and iPadOS 17. |
| November 3, 2022 | Updated artwork and specifications. |
| September 23, 2022 | New page. |


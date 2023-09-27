# **[components-status] live-activities**

## A Live Activity displays up-to-date information from your app, allowing people to view the progress of events or tasks at a glance.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/live-activities-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/live-activities-intro-dark_2x.png)

Live Activities help people keep track of tasks and events that they care about, offering persistent locations for displaying information that updates frequently. For example, a food delivery app could display the time remaining until a food order arrives, or a sports app can display the score for an ongoing game.

In addition to displaying a Live Activity on the Lock Screen, devices that support Live Activities can display your app information in different ways, depending on whether the device also supports the Dynamic Island.

- On devices that support the Dynamic Island, the system displays Live Activities in a persistent location around the TrueDepth camera.
- On devices that don’t support the Dynamic Island, the system can display a Live Activity update in a banner that appears briefly on the top of the screen.

To display a Live Activity, the system uses the following presentations:

- **Compact.** In the Dynamic Island, the system uses the compact presentation when there’s only one Live Activity that’s currently active. The compact presentation is composed of two separate presentations: one that displays on the leading side of the TrueDepth camera, and one that displays on the trailing side. Although the leading and trailing presentations are separate views, they form a cohesive view in the Dynamic Island, representing a single piece of information from your app. People can tap a compact Live Activity to open the app and get more details about the event or task.

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-compact-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-compact-dark_2x.png)

- **Minimal.** When multiple Live Activities are active, the system uses the minimal presentation to display two of them in the Dynamic Island. One Live Activity appears attached to the Dynamic Island while the other appears detached. Depending on its content size, the detached minimal Live Activity appears circular or oval. As with a compact Live Activity, people tap a minimal Live Activity to open the app and get more details about the event or task.

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-minimal-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-minimal-dark_2x.png)

- **Expanded.** When people touch and hold a Live Activity in a compact or minimal presentation, the system displays the content in an expanded presentation.

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-expanded-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/type-expanded-dark_2x.png)

- **Lock Screen.** On the Lock Screen and on devices that don't support the Dynamic Island, the system uses the Lock Screen presentation to display a banner on the top of the screen. It appears briefly while people view the Home Screen or use another app, but only if the app determines that the update is important enough to interrupt people.

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/live-activity-notch-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities/images/live-activity-notch-dark_2x.png)

To ensure that your Live Activity works well on all devices that can support it — and in all system-determined presentations — you need to support all three presentation types for the Dynamic Island, in addition to the Lock Screen presentation.

For developer guidance, see [ActivityKit](https://developer.apple.com/documentation/activitykit).

# **Best practices**

**Offer a Live Activity for tasks and live events that have a defined beginning and end.** People use Live Activities to track events with frequently updating data or to monitor the status of ongoing tasks. Don’t offer a Live Activity for a task that exceeds eight hours, and always end a Live Activity immediately after the task completes or the event ends.

**Present only the most essential content.** People appreciate getting a summary and key bits of information about an ongoing task or event; they don’t expect to receive a lot of details or to perform actions in a Live Activity. Let people tap your Live Activity to access additional details and functionality within your app.

**Update a Live Activity only when new content is available, alerting people only if it’s essential to get their attention.** It can be disruptive to alert people to a Live Activity update, and alerting them too often — or alerting them to updates that aren’t crucial — can annoy people and encourage them to stop using your Live Activities. Note that the system alerts people to a Live Activity update in different ways, depending on the device and whether it supports the Dynamic Island.

**Avoid displaying sensitive information in a Live Activity.** A Live Activity is visually prominent and could be viewed by casual observers. If the information you need to provide refers to sensitive items, display an innocuous summary and let people tap the Live Activity to get more information in your app.

**Avoid using a Live Activity to display ads or promotions.** Live Activities help people stay informed about ongoing events and tasks, so it’s important to display only information that’s related to those events and tasks.

**Give people control over beginning and ending Live Activities.** For example, to help people end a Live Activity before the task or event ends, provide buttons to stop or cancel a Live Activity in the linked view in your app. Although it’s also a good idea to provide a button people can use to start a Live Activity from within your app, there are some situations in which people are likely to expect a Live Activity to start automatically. For example, if people use your app to start a task or event — such as ordering food for delivery or making a rideshare request — it makes sense to automatically initiate a Live Activity as soon as a person places an order or makes a request. In Settings, people can turn off Live Activities for your app, so it’s important to avoid surprising people by starting a Live Activity they don’t expect.

**Make sure tapping your Live Activity opens your app at the right location.** When people tap a Live Activity to open your app, take them directly to details and actions related to it — don’t require them to navigate to the relevant screen. For developer guidance on SwiftUI views that can deep link to specific screens in your app, see [Link](https://developer.apple.com/documentation/swiftui/link) and [widgetURL(`_:`)](https://developer.apple.com/documentation/WidgetKit/DynamicIsland/widgetURL(_:)).

**Consider removing your Live Activity from the Lock Screen after it ends.** In the Dynamic Island, the system immediately removes a Live Activity when it ends. By default, the system shows a Live Activity on the Lock Screen for up to four hours after it ends to give people time to view its final content update. If the outcome of your Live Activity is only relevant for a shorter time, tell the system to dismiss it at a specific time within the four-hour window or immediately after it ends. For example, a rideshare app might choose to display a summary of the ride in the Live Activity on the Lock Screen for 15 minutes after the ride ends so people can view the final fare.

# **Designing useful Live Activities**

**Ensure unified information and design of the compact presentations in the Dynamic Island.** The TrueDepth camera separates the compact leading and compact trailing presentations of your Live Activity, but the contents of both should read as a single piece of information, and tapping either presentation should take people to the same screen in your app. Consider using color to help reinforce the relationship of content like text and icons in the two compact presentations.

**Create consistent layouts between compact and expanded presentations.** The expanded presentation is an enlarged version of the compact presentation. Ensure that information and layouts expand predictably when the Live Activity transitions from compact to expanded presentation.

**Consider using a consistent design in both Lock Screen and expanded presentations.** When you use a consistent design approach in both presentations, you help people become familiar with your content and learn how to track an event’s or task’s progress in different locations.

**Adapt to different screen sizes and Live Activity presentations.** Live Activities scale to adapt to the screen sizes of different devices. Ensure your Live Activity looks great on every device by supplying content at appropriate sizes. As you create layouts and assets for various devices and scale factors, use the values listed in [Specifications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities#specifications) for guidance.

**Consider carefully before using a custom background color and opacity on the Lock Screen.** If you set a background color or image for Live Activities that appear on the Lock Screen, test colors to be sure they offer enough contrast — especially tint colors on Always-On display with reduced luminance. Note that you can’t choose a custom background color for Live Activity presentations that appear in the Dynamic Island. However, you can apply a custom tint color for text, symbols, and a border that surrounds the Dynamic Island. For developer guidance, see [Displaying live data with Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities).

**Coordinate the corner radius of your content with the corner radius of the Live Activity.** Margins between content items and the Live Activity edge need to be consistent. To ensure that your content looks good within a Live Activity’s rounded corners, use a SwiftUI container to apply the correct corner radius. For developer guidance, see [ContainerRelativeShape](https://developer.apple.com/documentation/swiftui/containerrelativeshape).

**In general, use standard margins to ensure your content is legible.** For the expanded and Lock Screen presentations, the standard margin width is 20 points. In some cases — such as for graphics and buttons — you might need to use tighter margins to avoid crowding edges or creating a cluttered appearance. For developer guidance, see [padding(`_:`_:)](https://developer.apple.com/documentation/swiftui/view/padding(_:_:)).

**Choose colors that work well on a personalized Lock Screen.** People customize their Lock Screen with wallpaper, custom tint colors, and widgets. To make your Live Activity fit a custom Lock Screen aesthetic while remaining legible, apply custom tint colors and opacity sparingly.

**Support Dark Mode and Always-On display.** A Live Activity adapts its colors to look great in both the light and dark appearances and on Always-On display with reduced luminance. For guidance, see [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/foundations/dark-mode) and [Always On](https://developer.apple.com/design/human-interface-guidelines/technologies/always-on); for developer guidance, see [About asset catalogs](https://help.apple.com/xcode/mac/current/#/dev10510b1f7).

**Use animations sparingly, and only to bring attention to content updates.** Live Activities use a subset of system animations, but the system doesn’t perform animations on Always-On display with reduced luminance. To learn which animations are available, see [Animate content updates](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Animate-content-updates).

# **Platform considerations**

*Not supported in iPadOS, macOS, tvOS, or watchOS.*

# **Specifications**

# **The Dynamic Island**

The Dynamic Island uses a corner radius of 44 points, and its rounded corner shape matches the TrueDepth camera.

| Presentation type | Device | Dynamic Island width (points) |
| --- | --- | --- |
| Compact or minimal | iPhone 14 Pro Max | 250 |
|  | iPhone 14 Pro | 230 |
| Expanded | iPhone 14 Pro Max | 408 |
|  | iPhone 14 Pro | 371 |

# **Live Activity sizes**

All values listed in the table below are in points.

| Screen dimensions (portrait) | Compact leading | Compact trailing | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen |
| --- | --- | --- | --- | --- | --- |
| 430x932 | 62.33x36.67 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 |
| 393x852 | 52.33x36.67 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 |
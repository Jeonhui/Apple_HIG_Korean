June 5, 2023

 Updated guidance to reflect changes in watchOS 10. Progress indicators
===================

Progress indicators let people know that your app isn’t stalled while it loads content or performs lengthy operations.![A stylized representation of a spinning indeterminate activity indicator above a progress bar. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/983ffd361839ffc1360b1542a8205a45/components-progress-indicators-intro@2x.png)

Some progress indicators also give people a way to estimate how long they have to wait for something to complete. All progress indicators are transient, appearing only while an operation is ongoing and disappearing after it completes.

Because the duration of an operation is either known or unknown, there are two types of progress indicators:

* *Determinate*, for a task with a well-defined duration, such as a file conversion.
* *Indeterminate*, for unquantifiable tasks, such as loading or synchronizing complex data.

[Best practices](/design/human-interface-guidelines/progress-indicators#Best-practices)
---------------------------------------------------------------------------------------

**When possible, use a determinate progress indicator.** An indeterminate progress indicator shows that a process is occurring, but it doesn’t help people estimate how long a task will take. A determinate progress indicator can help people decide whether to do something else while waiting for the task to complete, restart the task at a different time, or abandon the task.

**Be as accurate as possible when reporting advancement in a determinate progress indicator.** Consider evening out the pace of advancement to help people feel confident about the time needed for the task to complete. Showing 90 percent completion in five seconds and the last 10 percent in 5 minutes can make people wonder if your app is still working and can even feel deceptive.

**Keep progress indicators moving so people know something is continuing to happen.** People tend to associate a stationary indicator with a stalled process or a frozen app. If a process stalls for some reason, provide feedback that helps people understand the problem and what they can do about it.

**When possible, switch a progress bar from indeterminate to determinate.** If an indeterminate process reaches a point where you can determine its duration, switch to a determinate progress bar. People generally prefer a determinate progress indicator, because it helps them gauge what’s happening and how long it will take.

**Don’t switch from the circular style to the bar style.** Spinners and progress bars are different shapes and sizes, so transitioning between them can disrupt your interface and confuse people.

**If it’s helpful, display a description that provides additional context for the task.** Be accurate and succinct. Avoid vague terms like *loading* or *authenticating* because they seldom add value.

**Display a progress indicator in a consistent location.** Choosing a consistent location for a progress indicator helps people reliably find the status of an operation across platforms or within or between apps.

**When it’s feasible, let people halt processing.** If people can interrupt a process without causing negative side effects, include a Cancel button. If interrupting the process might cause negative side effects — such as losing the downloaded portion of a file — it can be useful to provide a Pause button in addition to a Cancel button.

**Let people know when halting a process has a negative consequence.** When canceling a process results in lost progress, it’s helpful to provide an [alert](https://developer.apple.com/design/human-interface-guidelines/alerts)
 that includes an option to confirm the cancellation or resume the process.

[Platform considerations](/design/human-interface-guidelines/progress-indicators#Platform-considerations)
---------------------------------------------------------------------------------------------------------

*No additional considerations for tvOS, visionOS, or watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/progress-indicators#iOS-iPadOS)

Progress indicators have two distinct styles.

*Progress bars* include a track that fills from the leading side to the trailing side to show the progression of a task. Progress bars are always determinate in iOS and iPadOS. For developer guidance, see [`UIProgressView`](/documentation/uikit/uiprogressview)
.

![An illustration showing a horizontal progress bar filling from left to right as a webpage loads in Safari.](https://docs-assets.developer.apple.com/published/93a913f264fa5f048c894c0462e24405/progress-bar@2x.png)

*Activity indicators* spin while a task is performed. Activity indicators are always indeterminate in iOS and iPadOS. For developer guidance, see [`UIActivityIndicatorView`](/documentation/uikit/uiactivityindicatorview)
.

![A screenshot of an activity indicator spinning while Settings checks for a software update.](https://docs-assets.developer.apple.com/published/c8ce04b843841101edde2faeab8c2a79/activity-indicator@2x.png)**Hide the unfilled portion of the track in navigation bars and toolbars.** By default, a progress bar’s track includes both filled and unfilled portions. When you use a progress bar in a navigation bar or toolbar — for example, to show a page loading — configure it to hide the unfilled portion of the track.

#### [Refresh content controls](/design/human-interface-guidelines/progress-indicators#Refresh-content-controls)

A refresh control is manually initiated to immediately reload content, typically in a table view, without waiting for the next automatic content update to occur. A refresh control is a specialized type of activity indicator, is hidden by default, and becomes visible when dragging down on the view to be reloaded. In Mail, for example, you can drag the list of Inbox messages down to check for new messages.

![A screenshot of a refresh content control spinning while Mail checks for new messages.](https://docs-assets.developer.apple.com/published/2e2d3288be3120d3c7161d381dfa5851/refresh-controls@2x.png)**Perform automatic content updates.** Although people appreciate being able to do an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.

**Supply a short title only if it adds value.** Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed. A refresh control in Podcasts, for example, uses a title to tell people when the last podcast update occurred.

For developer guidance, see [`UIRefreshControl`](/documentation/uikit/uirefreshcontrol)
.

### [macOS](/design/human-interface-guidelines/progress-indicators#macOS)

Progress indicators have two distinct styles, each with a determinate and an indeterminate type.

*Bar indicators*, also known as *progress bars*, show progress in a horizontal bar. Determinate bar indicators fill from the leading side to the trailing side, while indeterminate indicators have an animated pulse. For developer guidance, see [`NSProgressIndicatorStyleBar`](/documentation/appkit/nsprogressindicatorstyle/nsprogressindicatorstylebar)
.

![An illustration of a horizontal progress bar filled almost to the midpoint with solid color.](https://docs-assets.developer.apple.com/published/7c13b26f5bf55d96fbca8cb60aebb9d4/progress-indicator-determinate-bar@2x.png)Determinate progress bar![An illustration of a circular progress indicator filled almost to the 8 o'clock position with solid color.](https://docs-assets.developer.apple.com/published/8288f9d55f529f513e7c3bd33bc3e17a/progress-indicator-determinate-circle@2x.png)Determinate progress circle*Spinning indicators*, also known as *spinners,* show progress in a circular form. Determinate spinning indicators are circles that fill in as progress continues, while indeterminate indicators have a rotating animation. For developer guidance, see [`NSProgressIndicatorStyleSpinning`](/documentation/appkit/nsprogressindicatorstyle/nsprogressindicatorstylespinning)
.

![An illustration of a completely filled horizontal progress bar. The fill is animated to cycle through various shade changes as progress continues.](https://docs-assets.developer.apple.com/published/88592a396aa2ff5aaec9c67cb9d455e0/progress-indicator-intermediate-bar@2x.png)Indeterminate progress bar![An illustration of a circular progress indicator that animates the shading of its spokes in a clockwise direction as progress continues.](https://docs-assets.developer.apple.com/published/bd3c036177521629c04df983116f7a52/progress-indicator-intermediate-spinner@2x.png)Spinning progress indicator**Prefer a spinning progress indicator to communicate the status of a background operation or when space is constrained.** Spinners are small and unobtrusive, so they’re useful for asynchronous background tasks, like retrieving messages from a server. Spinners are also good for communicating progress within a small area, such as within a text field or next to a specific control, such as a button.

**Avoid labeling a spinning progress indicator.** Because a spinner typically appears when people initiate a process, a label is usually unnecessary.

### [watchOS](/design/human-interface-guidelines/progress-indicators#watchOS)

Progress indicators have three distinct styles.

*Progress bars* include a track that fills from the leading edge to the trailing edge to show the progression of a task. Progress bars are always determinate in watchOS.

![An illustration showing a progress bar filling from left to right.](https://docs-assets.developer.apple.com/published/33bbf8ea9d047a5933e60cb120d3556e/progress-bar-watch@2x.png)

*Progress rings* include a circular track that fills in a clockwise direction to show the progression of a task. Progress rings are always determinate in watchOS.

![An illustration showing a progress ring filling in clockwise.](https://docs-assets.developer.apple.com/published/9327014cf549f926741534698be7d5ee/progress-ring-watch@2x.png)

*Activity indicators* spin while a task performs. Activity indicators are always indeterminate in watchOS.

![An illustration that shows a spinning activity indicator.](https://docs-assets.developer.apple.com/published/02a8427a04f946d9b80d2907f84ab365/activity-indicators-watch@2x.png)

For developer guidance, see [`ProgressView`](/documentation/SwiftUI/ProgressView)
.

[Resources](/design/human-interface-guidelines/progress-indicators#Resources)
-----------------------------------------------------------------------------

#### [Developer documentation](/design/human-interface-guidelines/progress-indicators#Developer-documentation)

[`ProgressView`](/documentation/SwiftUI/ProgressView)


[`UIProgressView`](/documentation/uikit/uiprogressview)


[`UIActivityIndicatorView`](/documentation/uikit/uiactivityindicatorview)


[`UIRefreshControl`](/documentation/uikit/uirefreshcontrol)


[`NSProgressIndicator`](/documentation/appkit/nsprogressindicator)


[Change log](/design/human-interface-guidelines/progress-indicators#Change-log)
-------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |


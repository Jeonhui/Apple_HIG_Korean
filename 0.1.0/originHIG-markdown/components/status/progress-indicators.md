# **[components-status] progress-indicators**

## Progress indicators let people know that your app isn’t stalled while it loads content or performs lengthy operations.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/progress-indicators-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/progress-indicators-intro-dark_2x.png)

Some progress indicators also give people a way to estimate how long they have to wait for something to complete. All progress indicators are transient, appearing only while an operation is ongoing and disappearing after it completes.

Because the duration of an operation is either known or unknown, there are two types of progress indicators:

- *Determinate*, for a task with a well-defined duration, such as a file conversion.
- *Indeterminate*, for unquantifiable tasks, such as loading or synchronizing complex data.

# **Best practices**

**When possible, use a determinate progress indicator.** An indeterminate progress indicator shows that a process is occurring, but it doesn’t help people estimate how long a task will take. A determinate progress indicator can help people decide whether to do something else while waiting for the task to complete, restart the task at a different time, or abandon the task.

**Be as accurate as possible when reporting advancement in a determinate progress indicator.** Consider evening out the pace of advancement to help people feel confident about the time needed for the task to complete. Showing 90 percent completion in five seconds and the last 10 percent in 5 minutes can make people wonder if your app is still working and can even feel deceptive.

**Keep progress indicators moving so people know something is continuing to happen.** People tend to associate a stationary indicator with a stalled process or a frozen app. If a process stalls for some reason, provide feedback that helps people understand the problem and what they can do about it.

**When possible, switch a progress bar from indeterminate to determinate.** If an indeterminate process reaches a point where you can determine its duration, switch to a determinate progress bar. People generally prefer a determinate progress indicator, because it helps them gauge what’s happening and how long it will take.

**Don’t switch from the circular style to the bar style.** Spinners and progress bars are different shapes and sizes, so transitioning between them can disrupt your interface and confuse people.

**If it’s helpful, display a description that provides additional context for the task.** Be accurate and succinct. Avoid vague terms like *loading* or *authenticating* because they seldom add value.

**Display a progress indicator in a consistent location.** Choosing a consistent location for a progress indicator helps people reliably find the status of an operation across platforms or within or between apps.

**When it’s feasible, let people halt processing.** If people can interrupt a process without causing negative side effects, include a Cancel button. If interrupting the process might cause negative side effects — such as losing the downloaded portion of a file — it can be useful to provide a Pause button in addition to a Cancel button.

**Let people know when halting a process has a negative consequence.**When canceling a process results in lost progress, it’s helpful to provide an [alert](https://developer.apple.com/design/human-interface-guidelines/components/presentation/alerts) with an an option to confirm the cancellation or resume the process.

# **Platform considerations**

*No additional considerations for tvOS or watchOS.*

# **iOS, iPadOS**

Progress indicators have two distinct styles.

*Progress bars* include a track that fills from the leading side to the trailing side to show the progression of a task. Progress bars are always determinate in iOS and iPadOS. For developer guidance, see [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview).

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-bar_2x.png)

Play

*Activity indicators* spin while a task is performed. Activity indicators are always indeterminate in iOS and iPadOS. For developer guidance, see [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview).

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/activity-indicators_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/activity-indicators_2x.png)

Play

**Hide the unfilled portion of the track in navigation bars and toolbars.**By default, a progress bar’s track includes both filled and unfilled portions. When you use a progress bar in a navigation bar or toolbar — for example, to show a page loading — configure it to hide the unfilled portion of the track.

### **Refresh content controls**

A refresh control is manually initiated to immediately reload content, typically in a table view, without waiting for the next automatic content update to occur. A refresh control is a specialized type of activity indicator, is hidden by default, and becomes visible when dragging down on the view to be reloaded. In Mail, for example, you can drag the list of Inbox messages down to check for new messages.

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/refresh-controls_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/refresh-controls_2x.png)

Play

**Perform automatic content updates.** Although people appreciate being able to trigger an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.

**Supply a short title only if it adds value.** Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed. A refresh control in Podcasts, for example, uses a title to tell people when the last podcast update occurred.

For developer guidance, see [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol).

# **macOS**

Progress indicators have two distinct styles, each with a determinate and an indeterminate type.

*Bar indicators*, also known as *progress bars*, show progress in a horizontal bar. Determinate bar indicators fill from the leading side to the trailing side, while indeterminate indicators have an animated pulse. For developer guidance, see [NSProgressIndicatorBarStyle](https://developer.apple.com/documentation/appkit/nsprogressindicatorstylebar).

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-bar_2x.png)

Determinate progress bar

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-circle_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-circle_2x.png)

Determinate progress circle

*Spinning indicators*, also known as *spinners,* show progress in a circular form. Determinate spinning indicators are circles that fill in as progress continues, while indeterminate indicators have a rotating animation. For developer guidance, see [NSProgressIndicatorSpinningStyle](https://developer.apple.com/documentation/appkit/nsprogressindicatorspinningstyle).

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-bar_2x.png)

Indeterminate progress bar

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-spinner_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-spinner_2x.png)

Spinning progress indicator

**Prefer a spinning progress indicator to communicate the status of a background operation or when space is constrained.** Spinners are small and unobtrusive, so they’re useful for asynchronous background tasks, like retrieving messages from a server. Spinners are also good for communicating progress within a small area, such as within a text field or next to a specific control, such as a button.

**Avoid labeling a spinning progress indicator.** Because a spinner typically appears when people initiate a process, a label is usually unnecessary.
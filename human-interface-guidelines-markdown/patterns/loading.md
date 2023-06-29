Loading
=======

While content loads, avoid showing a blank view or static content that might make people think your app or game is sluggish or frozen.![A sketch of a spinning indeterminate activity indicator, suggesting data loading. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/cfdf824156ed794426ac55a2cb38ec15/patterns-loading-intro@2x.png)

[Best practices](/design/human-interface-guidelines/loading#Best-practices)
---------------------------------------------------------------------------

**Show content as soon as possible.** If you make people wait for loading to complete before displaying anything, they may interpret the lack of content as sluggishness. Instead, show placeholder text, graphics, or animations where content isn’t available yet, and replace these elements as the content loads. When possible, preload upcoming content in the background, such as while an animation is playing or people are navigating a level or menu.

**Clearly communicate that content is loading and how long it might take to complete.** Ideally, content displays instantly, but for situations where loading takes more than a moment or two, you can use system-provided components — called *progress indicators* — to show that content is loading. In general, you use a *determinate* progress indicator when you know how long loading will take, and you use an *indeterminate* progress indicator when you can’t quantify loading duration. In macOS, for example, the Finder combines a determinate progress bar with brief explanatory text to help people gauge how long a file copy will take to complete. For guidance, see [Progress indicators](/design/human-interface-guidelines/progress-indicators)
.

**If loading takes an unavoidably long time, consider giving people something to view while they wait.** For example, you might provide hints about gameplay, play a short video or animation, or display informative placeholder graphics. Gauge the remaining loading time as accurately as possible to help you avoid giving people too little time to enjoy interesting content or having so much time that you need to repeat content.

**Consider customizing loading views.** Although standard progress indicators are usually OK, they can sometimes feel out of context. Consider designing a more engaging experience by using custom animations and elements that match the style of your app or game.

[Platform considerations](/design/human-interface-guidelines/loading#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

### [watchOS](/design/human-interface-guidelines/loading#watchOS)

**As much as possible, avoid showing a loading indicator in your watchOS experience.** People expect quick interactions with their Apple Watch, so aim to display content immediately. In situations where content needs a second or two to load, it’s better to display a loading indicator than a blank screen.

[Resources](/design/human-interface-guidelines/loading#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/loading#Related)

[Launching](/design/human-interface-guidelines/launching)


[Progress indicators](/design/human-interface-guidelines/progress-indicators)



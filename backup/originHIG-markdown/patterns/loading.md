# **[patterns] loading**

# While content loads, avoid showing a blank or static screen that might make people think your app or game is sluggish or frozen.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-loading-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-loading-intro-dark_2x.png)

# **Best practices**

**Show content as soon as possible.** If you make people wait for loading to complete before displaying anything, they may interpret the lack of content as sluggishness. Instead, show placeholder text, graphics, or animations where content isn't available yet, and replace these elements as the content loads. When possible, preload upcoming content in the background, such as while an animation is playing or people are navigating a level or menu.

**Clearly communicate that content is loading and how long it might take to complete.** Ideally, content displays instantly, but for situations where loading takes more than a moment or two, you can use system-provided components — called *progress indicators* — to show that content is loading. In general, you use a *determinate* progress indicator when you know how long loading will take, and you use an *indeterminate* progress indicator when you can’t quantify loading duration. In macOS, for example, the Finder combines a determinate progress bar with brief explanatory text to help people gauge how long a file copy will take to complete. For guidance, see [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators).

**If loading takes an unavoidably long time, consider giving people something to view while they wait.** For example, you might provide hints about gameplay, show short video sequences, or display informative placeholder graphics. Gauge the remaining loading time as accurately as possible to help you avoid giving people too little time to enjoy interesting content or having so much time that you need to repeat content.

**Consider customizing loading screens.** Although standard progress indicators are usually OK, they can sometimes feel out of context. Consider designing a more immersive experience through custom animations and elements that match the style of your app or game.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*

# **watchOS**

**As much as possible, avoid showing a loading indicator in your watchOS experience.** People expect quick interactions with their Apple Watch, so aim to display content immediately. In situations where content needs a second or two to load, it’s better to display a loading indicator than a blank screen.
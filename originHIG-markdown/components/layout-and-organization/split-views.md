# **[components-layout-and-organization] split-views**

## A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/split-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/split-view-intro-dark_2x.png)

Typically, you use a split view to support navigation through a hierarchy of information. In this scenario, selecting an item in the view’s primary pane displays the item’s contents in the secondary pane. Similarly, a split view can display a tertiary pane if items in the secondary pane contain additional content.

It’s common to use a split view to create a [sidebar](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/sidebars) interface, where the leading pane lists the top-level items or collections in an app, and the secondary and optional tertiary panes can present child collections and item details. For example, Mail in iPadOS lists accounts and mailboxes in the primary pane, a selected mailbox’s messages in the secondary pane, and a selected email in the tertiary pane. Rarely, you might also use a split view to provide groups of functionality that supplement the primary view — for example, Keynote in macOS uses split view panes to present the slide navigator, the presenter notes, and the inspector pane in areas that surround the main slide canvas.

# **Best practices**

**Prefer using a split view in a regular — not a compact — environment.**A split view needs horizontal space in which to display multiple panes. In a compact environment, such as iPhone in portrait orientation, it’s difficult to display multiple panes without wrapping or truncating the content, making it less legible and harder to interact with.

**To enable navigation, persistently highlight the current selection in each pane that leads to the detail view.** The selected appearance clarifies the relationship between the content in various panes and helps people stay oriented.

**Consider letting people drag and drop content between panes.** Because a split view provides access to multiple levels of hierarchy, people can conveniently move content from one part of your app to another by dragging items to different panes.

# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in watchOS.*

# **macOS**

In macOS, you can arrange the panes of a split view horizontally, vertically, or both. A split view includes dividers between panes that can support dragging to resize them. For developer guidance, see [HSplitView](https://developer.apple.com/documentation/swiftui/hsplitview) and [VSplitView](https://developer.apple.com/documentation/swiftui/vsplitview).

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/vertical-split-view_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/vertical-split-view_2x.png)

Vertical split view

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/horizontal-split-view_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/horizontal-split-view_2x.png)

Horizontal split view

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/multiple-split-view_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views/images/multiple-split-view_2x.png)

Multiple split views

**Set reasonable defaults for minimum and maximum pane sizes.** If people can resize the panes in your app’s split view, make sure to use sizes that keep the divider visible. If a pane gets too small, the divider can seem to disappear, becoming difficult to use.

**Consider letting people hide a pane when it makes sense.** If your app includes an editing area, for example, consider letting people hide other panes to reduce distractions or allow more room for editing — in Keynote, people can hide the navigator and presenter notes panes when they want to focus on editing slide content.

**Provide multiple ways to reveal hidden panes.** For example, you might provide a toolbar button or a menu command — including a keyboard shortcut — that people can use to restore a hidden pane.

**Prefer the thin divider style.** The thin divider measures one point in width, giving you maximum space for content while remaining easy for people to use. Avoid using thicker divider styles unless you have a specific need. For example, if both sides of a divider present table rows that use strong linear elements that might make a thin divider hard to distinguish, it might work to use a thicker divider. For developer guidance, see [NSSplitView.DividerStyle](https://developer.apple.com/documentation/appkit/nssplitview/dividerstyle).

# **tvOS**

In tvOS, a split view can work well to enable content filtering. When people choose a filter category in the primary pane, your app can display the results in the secondary pane.

**Choose a split view layout that keeps the panes looking balanced.** By default, a split view devotes a third of the screen width to the primary pane and two-thirds to the secondary pane, but you can also specify a half-and-half layout.

**Display a single title above a split view, helping people understand the content as a whole.** People already know how to use a split view to navigate and filter content; they don’t need titles that describe what each pane contains.

**Choose the title’s alignment based on the type of content the secondary pane contains.** Specifically, when the secondary pane contains a content collection, consider centering the title in the window. In contrast, if the secondary pane contains a single main view of important content, consider placing the title above the primary view to give the content more room.
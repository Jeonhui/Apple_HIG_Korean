June 5, 2023

 Added guidance for split views in watchOS. Split views
===========

A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.![A stylized representation of a window consisting of three areas: a sidebar, a canvas, and an inspector. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/07bab4b89778439217ef19bbc5a7a462/components-split-view-intro@2x.png)

Typically, you use a split view to support navigation through a hierarchy of information. In this scenario, selecting an item in the view’s primary pane displays the item’s contents in the secondary pane. Similarly, a split view can display a tertiary pane if items in the secondary pane contain additional content.

It’s common to use a split view to create a [sidebar](https://developer.apple.com/design/human-interface-guidelines/sidebars)
 interface, where the leading pane lists the top-level items or collections in an app, and the secondary and optional tertiary panes can present child collections and item details. For example, Mail in iPadOS lists accounts and mailboxes in the primary pane, a selected mailbox’s messages in the secondary pane, and a selected email in the tertiary pane. Rarely, you might also use a split view to provide groups of functionality that supplement the primary view — for example, Keynote in macOS uses split view panes to present the slide navigator, the presenter notes, and the inspector pane in areas that surround the main slide canvas.

[Best practices](/design/human-interface-guidelines/split-views#Best-practices)
-------------------------------------------------------------------------------

**Prefer using a split view in a regular — not a compact — environment.** A split view needs horizontal space in which to display multiple panes. In a compact environment, such as iPhone in portrait orientation, it’s difficult to display multiple panes without wrapping or truncating the content, making it less legible and harder to interact with.

**To support navigation, persistently highlight the current selection in each pane that leads to the detail view.** The selected appearance clarifies the relationship between the content in various panes and helps people stay oriented.

**Consider letting people drag and drop content between panes.** Because a split view provides access to multiple levels of hierarchy, people can conveniently move content from one part of your app to another by dragging items to different panes.

[Platform considerations](/design/human-interface-guidelines/split-views#Platform-considerations)
-------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, or visionOS.*

### [macOS](/design/human-interface-guidelines/split-views#macOS)

In macOS, you can arrange the panes of a split view horizontally, vertically, or both. A split view includes dividers between panes that can support dragging to resize them. For developer guidance, see [`HSplitView`](/documentation/SwiftUI/HSplitView)
 and [`VSplitView`](/documentation/SwiftUI/VSplitView)
.

* [Vertical](#)
* [Horizontal](#)
* [Multiple](#)
![An illustraiton of a laptop screen with a vertical line near the left edge at about 20 percent of the screen's width.](https://docs-assets.developer.apple.com/published/60187d8541598a0c87670b116522e945/vertical-split-view@2x.png)

![An illustration of a laptop screen with a horizontal line near the bottom at about one third of the screen's height.](https://docs-assets.developer.apple.com/published/0f03142830ee1e9dbfd0b6329b30c8e0/horizontal-split-view@2x.png)

![An illustration of a laptop screen with a vertical line near the left edge and a horizontal line near the bottom, extending from the vertical line to the right edge.](https://docs-assets.developer.apple.com/published/efdcaadbb04a878194241bc67a41876b/multiple-split-view@2x.png)

**Set reasonable defaults for minimum and maximum pane sizes.** If people can resize the panes in your app’s split view, make sure to use sizes that keep the divider visible. If a pane gets too small, the divider can seem to disappear, becoming difficult to use.

**Consider letting people hide a pane when it makes sense.** If your app includes an editing area, for example, consider letting people hide other panes to reduce distractions or allow more room for editing — in Keynote, people can hide the navigator and presenter notes panes when they want to focus on editing slide content.

**Provide multiple ways to reveal hidden panes.** For example, you might provide a toolbar button or a menu command — including a keyboard shortcut — that people can use to restore a hidden pane.

**Prefer the thin divider style.** The thin divider measures one point in width, giving you maximum space for content while remaining easy for people to use. Avoid using thicker divider styles unless you have a specific need. For example, if both sides of a divider present table rows that use strong linear elements that might make a thin divider hard to distinguish, it might work to use a thicker divider. For developer guidance, see [`NSSplitView.DividerStyle`](/documentation/appkit/nssplitview/dividerstyle)
.

### [tvOS](/design/human-interface-guidelines/split-views#tvOS)

In tvOS, a split view can work well to help people filter content. When people choose a filter category in the primary pane, your app can display the results in the secondary pane.

**Choose a split view layout that keeps the panes looking balanced.** By default, a split view devotes a third of the screen width to the primary pane and two-thirds to the secondary pane, but you can also specify a half-and-half layout.

**Display a single title above a split view, helping people understand the content as a whole.** People already know how to use a split view to navigate and filter content; they don’t need titles that describe what each pane contains.

**Choose the title’s alignment based on the type of content the secondary pane contains.** Specifically, when the secondary pane contains a content collection, consider centering the title in the window. In contrast, if the secondary pane contains a single main view of important content, consider placing the title above the primary view to give the content more room.

### [watchOS](/design/human-interface-guidelines/split-views#watchOS)

In watchOS, the split view displays either the sidebar or the detail view as a full-screen view.

**Automatically display the most relevant detail view.** When your app launches, show people the most pertinent information. For example, display information relevant to their location, the time, or their recent actions.

**If your app displays multiple detail pages, place the detail views in a vertical [tab view](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views)
.** People can then use the Digital Crown to scroll between the detail view’s tabs. watchOS also displays a page indicator next to the Digital Crown, indicating the number of tabs and the currently selected tab.

![A screenshot showing a detail view with a vertical tab on Apple Watch. The page indicator next to the Digital Crown shows that the fifth tab is currently selected.](https://docs-assets.developer.apple.com/published/6648b5fa2fe8e75d4a0ffa3149c08379/split-view-watch-vertical-tab@2x.png)[Resources](/design/human-interface-guidelines/split-views#Resources)
---------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/split-views#Related)

[Sidebars](/design/human-interface-guidelines/sidebars)


[Tab bars](/design/human-interface-guidelines/tab-bars)


[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/split-views#Developer-documentation)

[`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView)


[`UISplitViewController`](/documentation/uikit/uisplitviewcontroller)


[`NSSplitViewController`](/documentation/appkit/nssplitviewcontroller)


#### [Videos](/design/human-interface-guidelines/split-views#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/5C8F0205-3AE9-4647-870B-5C10FB7EA6FF/3520_wide_250x141_1x.jpg) Designed for iPad](https://developer.apple.com/videos/play/wwdc2020/10206) 
[Change log](/design/human-interface-guidelines/split-views#Change-log)
-----------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Added guidance for split views in watchOS. |


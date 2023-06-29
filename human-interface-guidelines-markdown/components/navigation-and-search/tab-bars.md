June 21, 2023

 Updated to include guidance for visionOS. Tab bars
========

Tab bars use bar items to navigate between mutually exclusive panes of content in the same view.![A stylized representation of a tab bar containing four placeholder icons with names. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/a6228884047d7fafe87b59f2c54090aa/components-tab-bar-intro@2x.png)

Tab bars help people understand the different types of information or functionality that a view provides. They also let people quickly switch between sections of the view while preserving the current navigation state within each section.

For guidance using a similar component in macOS, see [tab views](/design/human-interface-guidelines/tab-views)
.

[Best practices](/design/human-interface-guidelines/tab-bars#Best-practices)
----------------------------------------------------------------------------

**Use a tab bar to support navigation, not to provide actions.** A tab bar lets people navigate among different areas of an app, like the Alarm, Stopwatch, and Timer tabs in the Clock app. If you need to provide controls that act on elements in the current view, use a [toolbar](/design/human-interface-guidelines/toolbars)
 instead.

**Make sure the tab bar is visible when people navigate to different areas in your app.** The exception is a tab bar within a modal view. Because a modal view provides a separate experience that people dismiss when they’re finished, hiding the view’s tab bar doesn’t affect app navigation.

**Use the minimum number of tabs required to help people navigate your app.** Each additional tab increases the complexity of your app, making it harder for people to locate information. Aim for a few tabs with short titles or icons to avoid crowding and causing labels to truncate. In general, use up to five tabs in iOS and up to six in visionOS, iPadOS, and tvOS.

**Keep tabs visible even when their content is unavailable.** If tabs are available in some cases but not in others, your app’s interface might appear unstable and unpredictable. When necessary, explain why a tab’s content is unavailable. For example, even when there is no music on an iOS device, the Listen Now tab in the Music app remains available and offers suggestions for downloading music.

**Use a succinct term for each tab title.** A useful tab title aids navigation by clearly describing the type of content or functionality the tab contains. Aim for a single word or a very short phrase, like Music, Shared, Library, or For You. Consider avoiding a generic term like Home, which lacks specificity and can mean different things in different apps.

**Use a badge to communicate unobtrusively.** You can display a badge — a red oval containing white text and either a number or an exclamation point — on a tab to indicate that new information associated with that view or mode is available. For guidance, see [Notifications](/design/human-interface-guidelines/notifications)
.

[Platform considerations](/design/human-interface-guidelines/tab-bars#Platform-considerations)
----------------------------------------------------------------------------------------------

*Not supported in macOS or watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/tab-bars#iOS-iPadOS)

By default, a tab bar is translucent: It uses a background material only when content appears behind it, removing the material when the view scrolls to the bottom. A tab bar hides when a keyboard is onscreen.

**Avoid overflow tabs whenever possible.** Depending on device size and orientation, the number of visible tabs can be smaller than the total number of tabs. If horizontal space limits the number of visible tabs, the trailing tab becomes a More tab, revealing the remaining items in a list on a separate screen. The More tab makes it harder for people to reach and notice content on tabs that are hidden, so try to limit scenarios in your app where this can happen.

**In an iPadOS app, consider using a sidebar instead of a tab bar.** Because a sidebar can display a large number of items, it can make navigating an iPad app more efficient. You can also let people customize a sidebar’s items and let them hide it to make more room for content. For guidance, see [Sidebars](/design/human-interface-guidelines/sidebars)
.

**Ensure that tabs affect the view that’s attached to the tab bar, not views elsewhere onscreen.** For example, make sure selecting a tab on the left side of a split view doesn’t cause the right side of the split view to change.

**Consider using SF Symbols to provide scalable, visually consistent tab bar items.** When you use [SF Symbols](/design/human-interface-guidelines/sf-symbols)
, tab bar items automatically adapt to different contexts. For example, the tab bar can be regular or compact, depending on the current device and orientation. Also, tab bar icons can appear above tab titles in portrait orientation, whereas in landscape, the icons and titles can appear side by side. Prefer filled symbols or icons for consistency with the platform. If your app uses a sidebar instead of a tab bar when it runs on iPad, switch the filled symbols or icons to the outlined variant in the sidebar.

![An illustration that represents two versions of the Photos app on iPhone, one in landscape and the other in portrait orientation.](https://docs-assets.developer.apple.com/published/073de700f9e4471c237135b4e5d2e2a4/tab-bar-landscape@2x.png)

If you need to create custom tab bar icons using bitmaps, create each icon in two sizes so that the tab bar looks good in both regular and compact environments. Use the following metrics when creating tab bar icons in different shapes. For guidance, see [Icons](/design/human-interface-guidelines/icons)
.

### [Target dimensions](/design/human-interface-guidelines/tab-bars#Target-dimensions)



| Icon Shape | Regular tab bars | Compact tab bars |
| --- | --- | --- |
| Circle An illustration of a solid blue circle, which represents the target, centered inside the outlines of two squares. All three shapes are contained within the outline of a rectangle. The width of the inner square is slightly smaller than the diameter of the circle. The width of the outer square is the same as the diameter of the circle. The width of the rectangle is slightly larger than its height. A vertical line, extending to the top and bottom edges of the outer square, indicates the target’s height. A horizontal line, extending to left and right edges of the outer square, represents the target’s width. | 25x25 pt | 18x18 pt |
| 50x50 px @2x | 36x36 px @2x |
| 75x75 px @3x | 54x54 px @3x |
| Square An illustration of a solid blue square, which represents the target, centered inside the outline of a slightly larger square. Both shapes are contained within the outline of a rectangle. The solid blue square is slightly smaller than the outlined square. The width of the rectangle is slightly larger than its height. A vertical line, extending to the top and bottom edges of the blue square, represents the square’s height. A horizontal line, extending to left and right edges of the blue square, indicates the target’s width. | 23x23 pt | 17x17 pt |
| 46x46 px @2x | 34x34 px @2x |
| 69x69 px @3x | 51x51 px @3x |
| Wide An illustration of a solid blue rectangle, which represents the target, vertically centered inside the outline of a larger rectangle. The height of the blue rectangle is approximately half the height of the outlined rectangle. The outlines of two squares are horizontally centered within the outlined rectangle. The width of the outlined rectangle is slightly larger than its height. A horizontal line, extending to left and right edges of the outlined rectangle, represents the target’s width. | 31 pt | 23 pt |
| 62 px @2x | 46 px @2x |
| 93 px @3x | 69 px @3x |
| Tall An illustration of a solid blue rectangle, which represents the target, horizontally centered inside the outline of a larger rectangle. The width of the blue rectangle is approximately half the width of the outlined rectangle. The outlines of two squares are horizontally centered within the outlined rectangle. The width of the outlined rectangle is slightly larger than its height. A vertical line, extending to top and bottom edges of the outlined rectangle, represents the target’s height. | 28 pt | 20 pt |
| 56 px @2x | 40 px @2x |
| 84 px @3x | 60 px @3x |

### [tvOS](/design/human-interface-guidelines/tab-bars#tvOS)

A tab bar is highly customizable. For example, you can:

* Specify a tint, color, or image for the tab bar background
* Choose a font for tab items, including a different font for the selected item
* Specify tints for selected and unselected items
* Add button icons, like settings and search

By default, a tab bar is translucent, and only the selected tab is opaque. When people use the remote to focus on the tab bar, the selected tab includes a drop shadow that emphasizes its selected state. The height of a tab bar is 68 points, and its top edge is 46 points from the top of the screen; you can’t change either of these values.

If there are more items than can fit in the tab bar, the system truncates the rightmost item by applying a fade effect that begins at the right side of the tab bar. If there are enough items to cause scrolling, the system also applies a truncating fade effect that starts from the left side.

**If you use an icon for a tab title, make sure it’s familiar.** You can use icons as tab titles to help save space, but only for universally recognized symbols like search or settings. Using an unfamiliar symbol without a descriptive title can confuse people. For guidance, see [SF Symbols](/design/human-interface-guidelines/sf-symbols)
.

**Be aware of tab bar scrolling behaviors.** By default, people can scroll the tab bar offscreen when the current tab contains a single main view. You can see examples of this behavior in the Watch Now, Movies, TV Show, Sports, and Kids tabs in the TV app. The exception is when a screen contains a split view, such as the TV app’s Library tab or an app’s Settings screen. In this case, the tab bar remains pinned at the top of the view while people scroll the content within the primary and secondary panes of the split view. Regardless of a tab’s contents, focus always returns to the tab bar at the top of the page when people press Menu on the remote.

**In a live-viewing app, organize tabs in a consistent way.** For the best experience, organize content in live-streaming apps with tabs in the following order:

* Live content
* Cloud DVR or other recorded content
* Other content

For additional guidance, see [Live-viewing apps](/design/human-interface-guidelines/live-viewing-apps)
.

**Create a branded logo image to display next to the leading or trailing end of the tab bar, if it makes sense in your app.** To ensure enough room between the branded logo image and the edge of the tab bar, place the image within the safe margin. Use the following image size values for guidance:



| Maximum width | Maximum height |
| --- | --- |
| 200 pt | 68 pt |

### [visionOS](/design/human-interface-guidelines/tab-bars#visionOS)

In visionOS, a tab bar is always vertical, floating in a position that’s fixed relative to the window’s leading side. When people look at a tab bar, it automatically expands; to open a specific tab, people focus the tab and tap. While a tab bar is expanded, it can temporarily obscure the content behind it.

 [Play](#) 
**Supply a symbol and a text title for each tab.** A tab’s symbol is always visible in the tab bar. When people look at the tab bar, the system reveals tab titles, too. Even though the tab bar expands, you need to keep tab titles short so people can read them at a glance.

![A screenshot showing a collapsed tab bar containing only symbols.](https://docs-assets.developer.apple.com/published/71541ceda25ac9006d5546e5f8db7543/visionos-tab-bar-collapsed@2x.png)Collapsed![A screenshot showing an expanded tab bar containing both symbols and titles.](https://docs-assets.developer.apple.com/published/9bd2d4bd920f88ad71d5b586bfa7ad6d/visionos-tab-bar-expanded@2x.png)Expanded**If it makes sense in your app, consider using a sidebar within a tab.** If your app’s hierarchy is deep, you might want to use a [sidebar](/design/human-interface-guidelines/sidebars)
 to support secondary navigation within a tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

[Resources](/design/human-interface-guidelines/tab-bars#Resources)
------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/tab-bars#Related)

[Tab views](/design/human-interface-guidelines/tab-views)


[Toolbars](/design/human-interface-guidelines/toolbars)


[Sidebars](/design/human-interface-guidelines/sidebars)


[Navigation bars](/design/human-interface-guidelines/navigation-bars)


#### [Developer documentation](/design/human-interface-guidelines/tab-bars#Developer-documentation)

[`UITabBar`](/documentation/uikit/uitabbar)


#### [Videos](/design/human-interface-guidelines/tab-bars#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/95386734-286A-4C41-8073-28AC9A155F44/6490_wide_250x141_1x.jpg) Explore navigation design for iOS](https://developer.apple.com/videos/play/wwdc2022/10001) 
[Change log](/design/human-interface-guidelines/tab-bars#Change-log)
--------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |


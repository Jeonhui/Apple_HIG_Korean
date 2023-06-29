June 5, 2023

 Updated guidance for using scroll views in watchOS. Scroll views
============

A scroll view lets people view content that’s larger than the view’s boundaries by moving the content horizontally or vertically.![A stylized representation of a scrollable image view. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/395072e6a9ec2890d242c1d967a7cbe4/components-scroll-view-intro@2x.png)

The scroll view itself has no appearance, but it can display a translucent scroll *bar* or *indicator* that provides additional information about the action. For example, the position of an indicator shows whether the visible portion of the content is near the beginning, middle, or end. Its height hints at the total quantity of scrollable content in the view; the shorter the indicator, the more content there is to scroll.

[Best practices](/design/human-interface-guidelines/scroll-views#Best-practices)
--------------------------------------------------------------------------------

**Support default scrolling gestures and keyboard shortcuts.** People are accustomed to the systemwide scrolling behavior and expect it to work everywhere. If you build custom scrolling for a view, make sure your scroll bars use the elastic behavior that people expect.

**Make it apparent when content is scrollable.** Because scroll bars aren’t always visible, it can be helpful to make it obvious when content extends beyond the view. For example, displaying partial content at the edge of a view indicates that there’s more content in that direction. Although most people immediately try scrolling a view to discover if additional content is available, it’s considerate to draw their attention to it.

**Avoid putting a scroll view inside another scroll view with the same orientation.** Doing so creates an unpredictable interface that’s difficult to control. It’s alright to place a horizontal scroll view inside a vertical scroll view (or vice versa), however.

**Consider supporting page-by-page scrolling if it makes sense for your content.** In some situations, people appreciate scrolling by a fixed amount of content per interaction instead of scrolling continuously. On most platforms, you can define the size of such a *page* — typically the current height or width of the view — and define an interaction that scrolls one page at a time. To help maintain context during page-by-page scrolling, you can define a unit of overlap, such as a line of text, a row of glyphs, or part of a picture, and subtract the unit from the page size.

For developer guidance, see [`isPagingEnabled`](/documentation/uikit/uiscrollview/1619432-ispagingenabled)
.

**In some cases, scroll automatically to help people find their place.** Although people initiate almost all scrolling, automatic scrolling can be helpful when relevant content is no longer in view, such as when:

* Your app performs an operation that selects content or places the insertion point in an area that’s currently hidden. For example, when your app locates text that people are searching for, scroll the content to bring the new selection into view.
* People start entering information in a location that’s not currently visible. For example, if the insertion point is on one page and people navigate to another page, scroll back to the insertion point as soon as they begin to enter data.
* The pointer moves past the edge of the view while people are making a selection. In this case, follow the pointer by scrolling in the direction it moves.
* People select something and scroll to a new location before acting on the selection. In this case, scroll until the selection is in view before performing the operation.

In all cases, automatically scroll the content only as much as necessary to help people retain context. For example, if part of a selection is visible, you don’t need to scroll the entire selection into view.

**If you support zoom, set appropriate maximum and minimum scale values.** For example, zooming in on text until a single character fills the screen doesn’t make sense in most situations.

[Platform considerations](/design/human-interface-guidelines/scroll-views#Platform-considerations)
--------------------------------------------------------------------------------------------------

*No additional considerations for visionOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/scroll-views#iOS-iPadOS)

**In general, display one scroll view per screen.** People often make large swipe gestures when scrolling, and it can be hard to avoid interacting with a neighboring scroll view on the same screen. If you need to put two scroll views on one screen, consider allowing them to scroll in different directions so one gesture is less likely to affect both views. For example, when iPhone is in portrait orientation, the Stocks app shows stock quotes that scroll vertically above company-specific information that scrolls horizontally.

**Consider showing a page control when a scroll view is in page-by-page mode.** [Page controls](/design/human-interface-guidelines/page-controls)
 show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. For example, Weather uses a page control to indicate movement between people’s saved locations. If you show a page control with a scroll view, don’t show the scrolling indicator on the same axis to avoid confusing people with redundant controls.

### [macOS](/design/human-interface-guidelines/scroll-views#macOS)

**Account for scroll bars in your layout.** By default, scroll bars appear only when people interact with views that contain them, but people can use a setting in General settings to make them appear all the time. Some input devices also cause scroll bars to display all the time. If necessary, adjust the layout of your window so important interface elements don’t appear beneath scroll bars. The scroll bar track has a thickness of 15 points (regular size) or 11 points (small or mini size).

**Avoid moving window content when transient scroll bars appear.** Constantly shifting content every time scroll bars appear can be disorienting.

**Avoid placing controls inline with a scroll bar.** Doing this can cause the bar to appear even when people set it to be transient.

**If necessary, use small or mini scroll bars in a panel.** When space is tight, you can use smaller scroll bars in panels that need to coexist with other windows. Be sure to use the same size for all controls in such a panel.

### [tvOS](/design/human-interface-guidelines/scroll-views#tvOS)

Views in tvOS can scroll, but they aren’t treated as distinct objects with scroll bars. Instead, when content exceeds the size of the screen, the system automatically scrolls the interface to keep focused items visible.

### [watchOS](/design/human-interface-guidelines/scroll-views#watchOS)

The transient scroll bar appears during active scrolling.

**Prefer vertical scrolling content.** People can use the Digital Crown to navigate to and within apps on Apple Watch. If your app contains a single list or content view, rotating the Digital Crown scrolls vertically when your app’s content is taller than the height of the display.

**Use tab views to provide page-by-page scrolling.** watchOS displays tab views as pages. If the tabs views are oriented vertically, rotating the Digital Crown moves vertically through full-screen pages of content. The system displays a page indicator next to the Digital Crown that shows people where they are in the content, both within the current page, and within a set of pages. See [tab views](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views)
.

**When using paged content, consider limiting the content of an individual page to a single screen height.** Embracing this constraint encourages each page to serve a clear and distinct purpose and results in a more glanceable design. However, if your app has longer pages, the Digital Crown lets people navigate both between pages and through a longer page’s content; the page indicator expands to a scroll indicator when scrolling through a longer page. Use variable-height pages judiciously and, if possible, place them after fixed-height pages in your app design.

[Resources](/design/human-interface-guidelines/scroll-views#Resources)
----------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/scroll-views#Related)

[Page controls](/design/human-interface-guidelines/page-controls)


[Gestures](/design/human-interface-guidelines/gestures)


[Pointing devices](/design/human-interface-guidelines/pointing-devices)


#### [Developer documentation](/design/human-interface-guidelines/scroll-views#Developer-documentation)

[`ScrollView`](/documentation/SwiftUI/ScrollView)


[`UIScrollView`](/documentation/uikit/uiscrollview)


[`NSScrollView`](/documentation/appkit/nsscrollview)


[`WKPageOrientation`](/documentation/watchkit/wkpageorientation)


[Change log](/design/human-interface-guidelines/scroll-views#Change-log)
------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Updated guidance for using scroll views in watchOS. |


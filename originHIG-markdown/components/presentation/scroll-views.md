# **[components-presentation] scroll-views**

## A scroll view lets people view content that’s larger than the view’s boundaries by moving the content horizontally or vertically.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/scroll-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/scroll-view-intro-dark_2x.png)

The scroll view itself has no appearance, but it can display a translucent scroll *bar* or *indicator* that provides additional information about the action. For example, the position of an indicator shows whether the visible portion of the content is near the beginning, middle, or end. Its height hints at the total quantity of scrollable content in the view; the shorter the indicator, the more content there is to scroll.

# **Best practices**

**Support default scrolling gestures and keyboard shortcuts.** People are accustomed to the systemwide scrolling behavior and expect it to work everywhere. If you build custom scrolling for a view, make sure your scroll bars use the elastic behavior that people expect.

**Make it apparent when content is scrollable.** Because scroll bars aren’t always visible, it can be helpful to make it obvious when content extends beyond the view. For example, displaying partial content at the edge of a view indicates that there’s more content in that direction. Although most people immediately try scrolling a view to discover if additional content is available, it’s considerate to draw their attention to it.

**Avoid putting a scroll view inside another scroll view with the same orientation.** Doing so creates an unpredictable interface that’s difficult to control. It’s alright to place a horizontal scroll view inside a vertical scroll view (or vice versa), however.

**Consider enabling page-by-page scrolling if it makes sense for your content.** In some situations, people appreciate scrolling by a fixed amount of content per interaction instead of scrolling continuously. On most platforms, you can define the size of such a *page* — typically the current height or width of the view — and enable an interaction that scrolls one page at a time. To help maintain context during page-by-page scrolling, you can define a unit of overlap, such as a line of text, a row of glyphs, or part of a picture, and subtract the unit from the page size.

For developer guidance, see [isPagingEnabled](https://developer.apple.com/documentation/uikit/uiscrollview/1619432-ispagingenabled).

**In some cases, scroll automatically to help people find their place.**Although people initiate almost all scrolling, automatic scrolling can be helpful when relevant content is no longer in view, such as when:

- Your app performs an operation that selects content or places the insertion point in an area that’s currently hidden. For example, when your app locates text that people are searching for, scroll the content to bring the new selection into view.
- People start entering information in a location that’s not currently visible. For example, if the insertion point is on one page and people navigate to another page, scroll back to the insertion point as soon as they begin to enter data.
- The pointer moves past the edge of the view while people are making a selection. In this case, follow the pointer by scrolling in the direction it moves.
- People select something and scroll to a new location before acting on the selection. In this case, scroll until the selection is in view before performing the operation.

In all cases, automatically scroll the content only as much as necessary to help people retain context. For example, if part of a selection is visible, you don’t need to scroll the entire selection into view.

**If you enable zoom, set appropriate maximum and minimum scale values.** For example, zooming in on text until a single character fills the screen doesn’t make sense in most situations.

# **Platform considerations**

# **iOS, iPadOS**

**In general, display one scroll view per screen.** People often make large swipe gestures when scrolling, and it can be hard to avoid interacting with a neighboring scroll view on the same screen. If you need to put two scroll views on one screen, consider allowing them to scroll in different directions so one gesture is less likely to affect both views. For example, when iPhone is in portrait orientation, the Stocks app shows stock quotes that scroll vertically above company-specific information that scrolls horizontally.

**Consider showing a page control when a scroll view is in page-by-page mode.** [Page controls](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls) show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. For example, Weather uses a page control to indicate movement between people’s saved locations. If you show a page control with a scroll view, disable the scrolling indicator on the same axis to avoid confusing people with redundant controls.

# **macOS**

**Account for scroll bars in your layout.** By default, scroll bars appear only when people interact with views that contain them, but people can use a setting in General settings to make them to appear all the time. Some input devices also cause scroll bars to display all the time. If necessary, adjust the layout of your window so important interface elements don't appear beneath scroll bars. The scroll bar track has a thickness of 15 points (regular size) or 11 points (small or mini size).

**Avoid moving window content when transient scroll bars appear.**Constantly shifting content every time scroll bars appear can be disorienting.

**Avoid placing controls inline with a scroll bar.** Doing this can cause the bar to appear even when people set it to be transient.

**If necessary, use small or mini scroll bars in a panel.** When space is tight, you can use smaller scroll bars in panels that need to coexist with other windows. Be sure to use the same size for all controls in such a panel.

# **tvOS**

Views in tvOS can scroll, but they aren’t treated as distinct objects with scroll bars. Instead, when content exceeds the size of the screen, the system automatically scrolls the interface to keep focused items visible.

# **watchOS**

The transient scroll bar and knob appear during active scrolling, and people can use the Digital Crown to scroll. If your interface includes multiple pages, you can set whether they scroll horizontally or vertically with [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation).
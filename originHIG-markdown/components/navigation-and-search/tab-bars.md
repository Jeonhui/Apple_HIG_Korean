# **[components-navigation-and-search] tab-bars**

## Tab bars use bar items to navigate between mutually exclusive panes of content in the same view.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-bar-intro-dark_2x.png)

Tab bars help people understand the different types of information or functionality that a view provides. They also let people quickly switch between sections of the view while preserving the current navigation state within each section.

See [Tab views](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views) for the similar component in macOS.

# **Best practices**

**Use a tab bar only to enable navigation, not to help people perform actions.** A tab bar lets people navigate among different areas of an app, like the Alarm, Stopwatch, and Timer tabs in the Clock app. If you need to provide controls that act on elements in the current view, use a [toolbar](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars) instead.

**Make sure the tab bar is visible when people navigate to different areas in your app.** The exception is a tab bar within a modal view. Because a modal view gives people a separate experience that they dismiss when they’re finished, hiding the view’s tab bar doesn’t affect app navigation.

**Use the minimum number of tabs required to help people navigate your app.** Each additional tab increases the complexity of your app, making it harder for people to locate information. Aim for a few tabs with short titles or icons to avoid crowding and causing tabs to truncate. In general, use three to five tabs in iOS; use a few more in iPadOS and tvOS if necessary.

**Keep tabs visible even when their content is unavailable.** If tabs are enabled in some cases but not in others, your app’s interface might appear unstable and unpredictable. When necessary, explain why a tab’s content is unavailable. For example, even when there is no music on an iOS device, the Listen Now tab in the Music app remains available and offers suggestions for downloading music.

**Use concrete nouns or verbs as tab titles.** A good tab title helps people navigate by clearly describing the type of content people find when they select the tab. Consider nouns for category titles like Music, Movies, TV Shows, and Sports, and verbs or short verb phrases for things related to time or peoples’ perspectives on the content (like Watch Now or For You).

**Be cautious of overcrowding tabs with functionality.** Tabs represent an app’s menu of options. Tabs titled “Home” tend to be too large in scope for an app. Aim to create focus by representing specific and descriptive categories of content or functionality on each tab.

# **Platform considerations**

*Not supported in macOS or watchOS.*

# **iOS, iPadOS**

By default, a tab bar is translucent: It uses a background material only when content appears behind it, removing the material when the view scrolls to the bottom. A tab bar hides when a keyboard is onscreen.

**Avoid overflow tabs whenever possible.** Depending on device size and orientation, the number of visible tabs can be smaller than the total number of tabs. If horizontal space limits the number of visible tabs, the trailing tab becomes a More tab, revealing the remaining items in a list on a separate screen. The More tab makes it harder for people to reach and notice content on tabs that are hidden, so try to limit scenarios in your app where this can happen.

**In an iPadOS app, consider using a sidebar instead of a tab bar.**Because a sidebar can display a large number of items, it can make navigating an iPad app more efficient. You can also let people customize a sidebar’s items and let them hide it to make more room for content. For guidance, see [Sidebars](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/sidebars).

**Ensure that tabs affect the view that’s attached to the tab bar, not views elsewhere onscreen.** For example, make sure selecting a tab on the left side of a split view doesn’t cause the right side of the split view to change.

**Use a badge to communicate unobtrusively.** You can display a badge — a red oval containing white text and either a number or an exclamation point — on a tab to indicate that new information associated with that view or mode is available. For guidance, see [Notifications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/notifications).

**Consider using SF Symbols to provide scalable, visually consistent tab bar items.** When you use [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols), tab bar items automatically adapt to different contexts. For example, the tab bar can be regular or compact, depending on the current device and orientation. Also, tab bar icons can appear above tab titles in portrait orientation, whereas in landscape, the icons and titles can appear side by side. Prefer filled symbols or icons for consistency with the platform. If your app uses a sidebar instead of a tab bar when it runs on iPad, switch the filled symbols or icons to the outlined variant in the sidebar.

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/tab-bar-landscape_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/tab-bar-landscape_2x.png)

If you need to create custom tab bar icons using bitmaps, create each icon in two sizes so that the tab bar looks good in both regular and compact environments. Use the following metrics when creating tab bar icons in different shapes. For guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/foundations/icons).

**Target width and height (circular icons)**

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/max-width-height-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/max-width-height-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 25x25 pt (75x75 px @3x) | 18x18 pt (54x54 px @3x) |
| 25x25 pt (50x50px @2x) | 18x18 pt (36x36 px @2x) |

**Target width and height (square icons)**

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 23x23 pt (69x69 px @3x) | 17x17 pt (51x51 px @3x) |
| 23x23 pt (46x46 px @2x) | 17x17 pt (34x34 px @2x) |

**Target width (wide icons)**

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-height-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-width-height-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 31pt (93px @3x) | 23pt (69px @3x) |
| 31pt (62px @2x) | 23pt (46px @2x) |

**Target height (tall icons)**

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-height-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars/images/target-height-dark_2x.png)

| Regular tab bars | Compact tab bars |
| --- | --- |
| 28pt (84px @3x) | 20pt (60px @3x) |
| 28pt (56px @2x) | 20pt (40px @2x) |

# **macOS**

Tab bars aren’t available in macOS. Instead, [tab views](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views) perform a similar function.

# **tvOS**

A tab bar is highly customizable. For example, you can:

- Specify a tint, color, or image for the tab bar background
- Choose a font for tab items, including a different font for the selected item
- Specify tints for selected and unselected items
- Add button icons, like settings and search

By default, a tab bar is translucent, and only the selected tab is opaque. When people use the remote to focus on the tab bar, the selected tab includes a drop shadow that emphasizes its selected state. The height of a tab bar is 68 points, and its top edge is 46 points from the top of the screen; you can’t change either of these values.

If there are more items than can fit in the tab bar, the system truncates the rightmost item by applying a fade effect that begins at the right side of the tab bar. If there are enough items to cause scrolling, the system also applies a truncating fade effect that starts from the left side.

**If you use an icon for a tab title, make sure it’s familiar.** You can use icons as tab titles to help save space, but only for universally recognized symbols like search or settings. Using an unfamiliar symbol without a descriptive title can confuse people. For guidance, see [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols).

**Be aware of tab bar scrolling behaviors.** By default, people can scroll the tab bar offscreen when the current tab contains a single main view. You can see examples of this behavior in the Watch Now, Movies, TV Show, Sports, and Kids tabs in the TV app. The exception is when a screen contains a split view, such as the TV app's Library tab or an app's Settings screen. In this case, the tab bar remains pinned at the top of the view while people scroll the content within the primary and secondary panes of the split view. Regardless of a tab's contents, focus always returns to the tab bar at the top of the page when people press Menu on the remote.

**In a live-viewing app, organize tabs in a consistent way.** For the best experience, organize content in live-streaming apps with tabs in the following order:

- Live content
- Cloud DVR or other recorded content
- Other content

For additional guidance, see [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/patterns/live-viewing-apps).

**Create a branded logo image to display next to the leading or trailing end of the tab bar, if it makes sense in your app.** To ensure enough room between the branded logo image and the edge of the tab bar, place the image within the safe margin. Use the following image size values for guidance:

| Maximum width | Maximum height |
| --- | --- |
| 200 pt | 68 pt |
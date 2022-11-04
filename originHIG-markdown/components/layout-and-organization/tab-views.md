# **[components-layout-and-organization] tab-views**

## A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/tab-view-intro-dark_2x.png)

# **Best practices**

**Use a tab view to present closely related areas of content.** The appearance of a tab view provides a strong visual indication of enclosure. People expect each tab to display content that is in some way similar or related to the content in the other tabs.

**Make sure the controls within a pane affect content only in the same pane.** Panes are mutually exclusive, so ensure they’re fully self-contained.

**Provide a label for each tab that describes the contents of its pane.** A good label helps people predict the contents of a pane before clicking or tapping its tab. In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts. Use title-style capitalization for tab labels.

**Avoid using a pop-up button to switch between tabs.** A tabbed control is efficient because it requires a single click or tap to make a selection, whereas a pop-up button requires two. A tabbed control also presents all choices onscreen at the same time, whereas people must click a pop-up button to see its choices. Note that a pop-up button can be a reasonable alternative in cases where there are too many panes of content to reasonably display with tabs.

**Avoid providing more than six tabs in a tab view.** Having more than six tabs can be overwhelming and create layout issues. If you have six or more tabs, consider another way to implement your app’s user interface. For example, you may find that the tabs would be better suited as view options in a pop-up button menu.

For developer guidance, see [NSTabView](https://developer.apple.com/documentation/appkit/nstabview).

# **Anatomy**

You can position the tabbed control on any side of the content area: top, bottom, left, or right. You can also hide the controls, which is appropriate when you switch the panes programmatically.

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/top_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/top_2x.png)

Top tabs

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/bottom_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/bottom_2x.png)

Bottom tabs

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/left_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/left_2x.png)

Left tabs

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/right_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views/images/right_2x.png)

Right tabs

When you hide the tabbed control, the content area can be borderless, bezeled, or bordered with a line. A borderless view can be solid or transparent.

**In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view.** This layout looks clean and leaves room for additional controls that aren’t directly related to the contents of the tab view. For example, the lock button in Date & Time settings is outside of the tab view because it applies to all tabs. You can extend a tab view to meet the window edges, but this layout is unusual.

# **Platform considerations**

*Not supported in iOS, iPadOS, watchOS, or tvOS*

# **iOS, iPadOS**

For similar functionality, consider using a [segmented control](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls) instead.
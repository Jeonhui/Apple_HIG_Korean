# **[components-navigation-and-search] sidebars**

## A sidebar enables app navigation and provides quick access to top-level collections of content in your app or game.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/sidebar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/sidebar-intro-dark_2x.png)

The term *sidebar* refers to a list of top-level app areas and collections, almost always displayed in the primary pane of a [split view](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views). When people choose an item in a sidebar, the split view displays the item’s details in a secondary pane or — if the item contains a list — the secondary pane presents the list and a tertiary pane presents the details. For example, Mail in iOS, iPadOS, and macOS uses sidebar styling and behavior to display the list of accounts and mailboxes, typically displaying the message list in a secondary pane and a message’s content in a tertiary pane.

A sidebar layout can take a lot of horizontal space, especially if you want the sidebar and its accompanying panes to be visible onscreen at the same time. In a compact environment, you might want to consider an alternative component, like a [tab bar](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars).

**DEVELOPER NOTE**When you use SwiftUI to construct a sidebar interface, you automatically get platform-appropriate appearance and behavior. For developer guidance, see [ColumnNavigationViewStyle](https://developer.apple.com/documentation/swiftui/columnnavigationviewstyle). If you don’t use SwiftUI, you can instead use [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/) or [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/).

# **Best practices**

**Use a sidebar to enable quick navigation to key areas of your app or top-level collections of content, like folders and playlists.** A sidebar can help you flatten your information hierarchy, giving people access to several peer information categories or modes at the same time.

**When possible, let people customize the contents of a sidebar.** A sidebar lets people navigate to important areas in your app, so it works well when people can decide which areas are most important and in what order they should appear.

**Consider letting people hide the sidebar.** People sometimes want to hide the sidebar to create more room for content details. When possible, let people hide and show the sidebar using the platform-specific interactions they already know. For example, in iPadOS, people expect to use the built-in edge swipe gesture; in macOS, you can include a show/hide button or add Show Sidebar and Hide Sidebar commands to your app’s View menu. Avoid hiding the sidebar by default to ensure that it remains discoverable.

**In general, show no more than two levels of hierarchy in a sidebar.**When a data hierarchy is deeper than two levels, consider using a split view interface that includes a content list between the sidebar items and detail view.

**If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group.** To help keep labels short, omit unnecessary words. For example, Mail omits the word *Messages* from the title of each mailbox, using more concise terms like *Flagged* and *Drafts*.

# **Platform considerations**

*No additional considerations for tvOS. Not supported in watchOS.*

# **iOS, iPadOS**

**In an iOS app, consider using a tab bar instead of a sidebar.** A sidebar interface can require a lot of horizontal space, which might make it too crowded on iPhone, especially in portrait orientation. In contrast, a tab bar works well to let people quickly switch between top-level sections in your app while preserving the current navigation state within each section.

**In an iPadOS app, consider using a sidebar instead of a tab bar.**Because a sidebar can display a large number of items, it can make navigating an iPad app more efficient. You can also let people customize a sidebar’s items and let them hide it to make more room for content.

**If necessary, apply the correct appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar, you can use the sidebar appearance of a collection view list layout. For developer guidance, see [UICollectionLayoutListConfiguration.Appearance](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration/appearance).

# **macOS**

In macOS, a sidebar — also known as a *source list* — extends to the full height of the window, and uses a rounded-corner appearance for the selected-item highlight.

A sidebar’s row height, text, and glyph size depend on its overall size, which can be small, medium, or large. You can set the size programmatically, but people can also change it by selecting a different sidebar icon size in General settings. The table below shows the default metrics for a sidebar in macOS.

| Sidebar size | Sidebar component | Default metrics |
| --- | --- | --- |
| Small | Row height | 24 pt |
| SF Symbol scale | Medium * |  |
| Icon size | 16x16 px @1x |  |
| Text size (style) | 11 pt (Subhead) |  |
| Medium | Row height | 28 pt |
| SF symbol scale | Medium |  |
| Icon size | 20x20 px @1x |  |
| Text size (style) | 13 pt (Body) |  |
| Large | Row height | 32 pt |
| SF Symbol scale | Medium |  |
| Icon size | 24x24 px @1x |  |
| Text size (style) | 15 pt (Title 3) |  |
| All | Horizontal spacing between cells | 17 pt |
| Vertical spacing between cells | 0 pt |  |
- In some cases, a small sidebar uses small-scale SF Symbols by default.

**Consider using familiar symbols to represent items in the sidebar.** [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/) provides a wide range of customizable symbols you can use to represent items in your app. If you need to use a bitmap image to create a custom interface icon for the sidebar, create the image in both @1x and @2x resolutions and in the small, medium, and large sizes shown in the table above.

**Avoid stylizing your app by specifying a fixed color for all sidebar icons.** By default, sidebar icons use the current [accent color](https://developer.apple.com/design/human-interface-guidelines/foundations/color/#app-accent-colors) and people expect to see their chosen accent color throughout all the apps they use. Although a fixed color can help clarify the meaning of an icon, you want to make sure that most sidebar icons display the color people choose.

**If necessary, apply the correct background appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar in your macOS app, you may need to specify an opaque background for when the window contains more than one sidebar, or when using a sidebar in a panel or settings window. In all other use cases, use a translucent background for the sidebar.

**Consider automatically hiding and revealing a sidebar when its container window resizes.** For example, reducing the size of a Mail viewer window can automatically collapse its sidebar, making more room for message content.

**In an editable sidebar, avoid placing edit buttons at the bottom edge of the view.** Consider providing buttons that add, remove, manipulate, or get information about items. Buttons at the bottom of the sidebar can hide when the bottom edge of the window is offscreen. To let people add a new sidebar group, include an Add (+) button on the trailing side of the group’s label, next to the [disclosure triangle](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/#disclosure-triangles). Enable other actions, like remove, in a context menu or in a menu bar menu. For example, in addition to providing the New Mailbox command in a context menu, Mail also lists it in the Mailbox menu.
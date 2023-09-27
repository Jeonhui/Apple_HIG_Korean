June 21, 2023

 Updated to include guidance for visionOS. Sidebars
========

A sidebar can help people navigate your app or game, providing quick access to top-level collections of content.![A stylized representation of the top portion of a window's sidebar displaying a title, a section, and some folders. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/fbab4d7b7ae7b8a2790523101585497d/components-sidebar-intro@2x.png)

The term *sidebar* refers to a list of top-level app areas and collections, almost always displayed in the primary pane of a [split view](https://developer.apple.com/design/human-interface-guidelines/split-views)
. When people choose an item in a sidebar, the split view displays the item’s details in a secondary pane or — if the item contains a list — the secondary pane presents the list and a tertiary pane presents the details. For example, Mail in iOS, iPadOS, macOS, and visionOS uses sidebar styling and behavior to display the list of accounts and mailboxes, typically displaying the message list in a secondary pane and a message’s content in a tertiary pane.

A sidebar layout can take a lot of horizontal space, especially if you want the sidebar and its accompanying panes to be visible at the same time. In a layout that’s horizontally constrained, you might want to consider an alternative component, like a [tab bar](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
.

Developer note

When you use SwiftUI to construct a sidebar interface, you automatically get platform-appropriate appearance and behavior. For developer guidance, see [`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView)
. If you don’t use SwiftUI, you can instead use [`UISplitViewController`](/documentation/uikit/uisplitviewcontroller)
 or [`NSSplitViewController`](/documentation/appkit/nssplitviewcontroller)
.

[Best practices](/design/human-interface-guidelines/sidebars#Best-practices)
----------------------------------------------------------------------------

**Use a sidebar to help people quickly navigate to key areas of your app or top-level collections of content, like folders and playlists.** A sidebar can help you flatten your information hierarchy, giving people access to several peer information categories or modes at the same time.

**When possible, let people customize the contents of a sidebar.** A sidebar lets people navigate to important areas in your app, so it works well when people can decide which areas are most important and in what order they appear.

**Consider letting people hide the sidebar.** People sometimes want to hide the sidebar to create more room for content details or to reduce distraction. When possible, let people hide and show the sidebar using the platform-specific interactions they already know. For example, in iPadOS, people expect to use the built-in edge swipe gesture; in macOS, you can include a show/hide button or add Show Sidebar and Hide Sidebar commands to your app’s View menu. In visionOS, a window typically expands to accommodate a sidebar, so people rarely need to hide it. Avoid hiding the sidebar by default to ensure that it remains discoverable.

**In general, show no more than two levels of hierarchy in a sidebar.** When a data hierarchy is deeper than two levels, consider using a split view interface that includes a content list between the sidebar items and detail view.

**If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group.** To help keep labels short, omit unnecessary words. For example, Mail omits the word *Messages* from the title of each mailbox, using more concise terms like *Flagged* and *Drafts*.

[Platform considerations](/design/human-interface-guidelines/sidebars#Platform-considerations)
----------------------------------------------------------------------------------------------

*No additional considerations for tvOS. Not supported in watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/sidebars#iOS-iPadOS)

**In an iOS app, consider using a tab bar instead of a sidebar.** A sidebar interface can require a lot of horizontal space, which might make it too crowded on iPhone, especially in portrait orientation. In contrast, a tab bar works well to let people quickly switch between top-level sections in your app while preserving the current navigation state within each section.

**In an iPadOS app, consider using a sidebar instead of a tab bar.** Because a sidebar can display a large number of items, it can make navigating an iPad app more efficient. You can also let people customize a sidebar’s items and let them hide it to make more room for content.

**If necessary, apply the correct appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar, you can use the sidebar appearance of a collection view list layout. For developer guidance, see [`UICollectionLayoutListConfiguration.Appearance`](/documentation/uikit/uicollectionlayoutlistconfiguration/appearance)
.

### [macOS](/design/human-interface-guidelines/sidebars#macOS)

In macOS, a sidebar — also known as a *source list* — extends to the full height of the window, and uses a rounded-corner appearance for the selected-item highlight.

A sidebar’s row height, text, and glyph size depend on its overall size, which can be small, medium, or large. You can set the size programmatically, but people can also change it by selecting a different sidebar icon size in General settings. The table below shows the default metrics for a sidebar in macOS.



| Sidebar size | Sidebar component | Default metrics |
| --- | --- | --- |
| Small | Row height | 24 pt |
| SF Symbol scale | Medium \* |
| Icon size | 16x16 px @1x |
| Text size (style) | 11 pt (Subhead) |
| Medium | Row height | 28 pt |
| SF symbol scale | Medium |
| Icon size | 20x20 px @1x |
| Text size (style) | 13 pt (Body) |
| Large | Row height | 32 pt |
| SF Symbol scale | Medium |
| Icon size | 24x24 px @1x |
| Text size (style) | 15 pt (Title 3) |
| All | Horizontal spacing between cells | 17 pt |
| Vertical spacing between cells | 0 pt |

In some cases, a small sidebar uses small-scale SF Symbols by default.

**Consider using familiar symbols to represent items in the sidebar.** [SF Symbols](/design/human-interface-guidelines/sf-symbols)
 provides a wide range of customizable symbols you can use to represent items in your app. If you need to use a bitmap image to create a custom interface icon for the sidebar, create the image in both @1x and @2x resolutions and in the small, medium, and large sizes shown in the table above.

**Avoid stylizing your app by specifying a fixed color for all sidebar icons.** By default, sidebar icons use the current [accent color](https://developer.apple.com/design/human-interface-guidelines/color#App-accent-colors)
 and people expect to see their chosen accent color throughout all the apps they use. Although a fixed color can help clarify the meaning of an icon, you want to make sure that most sidebar icons display the color people choose.

**If necessary, apply the correct background appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar in your macOS app, you may need to specify an opaque background for when the window contains more than one sidebar, or when using a sidebar in a panel or settings window. In all other use cases, use a translucent background for the sidebar.

**Consider automatically hiding and revealing a sidebar when its container window resizes.** For example, reducing the size of a Mail viewer window can automatically collapse its sidebar, making more room for message content.

**In an editable sidebar, avoid placing edit buttons at the bottom edge of the view.** Consider providing buttons that add, remove, manipulate, or get information about items. Buttons at the bottom of the sidebar can hide when the bottom edge of the window is offscreen. To let people add a new sidebar group, include an Add (+) button on the trailing side of the group’s label, next to the [disclosure triangle](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls#Disclosure-triangles)
. Provide other actions, like remove, in a context menu or in a menu bar menu. For example, in addition to providing the New Mailbox command in a context menu, Mail also lists it in the Mailbox menu.

### [visionOS](/design/human-interface-guidelines/sidebars#visionOS)

**If your app’s hierarchy is deep, consider using a sidebar within a tab in a tab bar.** In this situation, a sidebar can support secondary navigation within the tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

![A partial screenshot of the Music app in visionOS. The app's window includes a sidebar for navigating the music library, and the secondary pane includes a grid of playlists.](https://docs-assets.developer.apple.com/published/659dbbacdc969304721b76d56947df32/visionos-sidebar-music@2x.png)

[Resources](/design/human-interface-guidelines/sidebars#Resources)
------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/sidebars#Related)

[Split views](/design/human-interface-guidelines/split-views)


[Tab bars](/design/human-interface-guidelines/tab-bars)


[Navigation bars](/design/human-interface-guidelines/navigation-bars)


[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/sidebars#Developer-documentation)

[`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView)


[`sidebar`](/documentation/SwiftUI/ListStyle/sidebar)


[`UICollectionLayoutListConfiguration`](/documentation/uikit/uicollectionlayoutlistconfiguration)


[`NSSplitViewController`](/documentation/appkit/nssplitviewcontroller)


#### [Videos](/design/human-interface-guidelines/sidebars#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/5C8F0205-3AE9-4647-870B-5C10FB7EA6FF/3520_wide_250x141_1x.jpg) Designed for iPad](https://developer.apple.com/videos/play/wwdc2020/10206) 
[Change log](/design/human-interface-guidelines/sidebars#Change-log)
--------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |


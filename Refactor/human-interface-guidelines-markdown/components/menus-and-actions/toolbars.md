June 21, 2023

 Updated to include guidance for visionOS. Toolbars
========

A toolbar provides convenient access to frequently used commands and controls that perform actions relevant to the current view.![A stylized representation of a toolbar containing buttons for adding, sharing, composing, and moving. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/c32f9e4f2947aaf1710fa9a0056632fd/components-toolbar-intro@2x.png)

Depending on the platform, a toolbar can look and behave differently.

* In visionOS, a toolbar appears along the bottom edge of an app’s main window.
* In iOS, a toolbar appears at the bottom of a screen. iOS toolbars aren’t customizable, and they don’t support grouping.
* In iPadOS and macOS, a toolbar appears at the top of a screen or window. Both platforms support customizable toolbars and grouped toolbar items. In macOS, people can hide an app’s toolbar.
* In watchOS, the toolbar itself isn’t visible, but you can place toolbar buttons in the top corners and along the bottom of the screen. The system automatically moves the time and title to accommodate buttons in the top corners. You can also place a button in a scrolling view. By default, a scrolling toolbar button remains hidden until people reveal it by scrolling up.

For developer guidance, see [Toolbars](/documentation/SwiftUI/Toolbars)


[Best practices](/design/human-interface-guidelines/toolbars#Best-practices)
----------------------------------------------------------------------------

**Provide toolbar items that support the main tasks people perform.** In general, prioritize the commands that people are mostly likely to want. These commands are often the ones people use most frequently, but in some apps it might make sense to prioritize commands that map to the highest level or most important objects people work with. In a macOS app, consider ordering the items in the toolbar according to your prioritization scheme.

**Avoid displaying too many toolbar items.** People need to be able to distinguish and activate each item, so you don’t want to overcrowd the toolbar.

**Consider grouping toolbar items where supported.** In iPadOS, macOS, and visionOS, you can define logical groups of items to help people find commands that are related to certain subtasks or functional areas in your app. For example, Keynote includes several groups that are based on functionality, including one for presentation-level commands, one for playback commands, and one for object insertion. In iPadOS, you can also use grouping to keep items together in the Overflow menu (to learn more, see [iPadOS](/design/human-interface-guidelines/toolbars#iPadOS)
).

![An illustration that represents the toolbar in Pages, highlighted to show how toolbar buttons are grouped by related functions.](https://docs-assets.developer.apple.com/published/2e3f5504cd83837338bbe68c0ed38fbc/toolbar-layout@2x.png)

**Make sure the meaning of each toolbar item is clear.** Don’t make people guess or experiment to figure out what an item does. In all platforms except macOS, provide either a simple, recognizable symbol (or interface icon), or a short, descriptive label for each item. In a macOS app, you provide a symbol and a label so that people can view both in the toolbar if they choose. As you write labels, prefer verbs and verb phrases like *View*, *Insert*, and *Share*. Use [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)
 and no ending punctuation.

**Prefer system-provided symbols or interface icons.** System-provided symbols are familiar, automatically receive appropriate coloring, and respond consistently to user interactions and vibrancy.

**Prefer a consistent appearance for all toolbar items.** Toolbars look best and are easiest to understand when all items use a similar visual style.

**If a toolbar item toggles between two states, make sure the item clearly communicates the current state.** You might consider changing the item’s color and label to clarify its current state. In the macOS Mail toolbar, for example, the online-offline toggle button displays a filled icon and a *Go Offline* label when accounts are online; when accounts are offline, the item displays an unfilled icon and a *Go Online* label.

**In iPadOS and macOS apps, consider letting people customize the toolbar.** Toolbar customization is especially useful in apps that provide a lot of items — or that include advanced functionality that not everyone needs — and in apps that people tend to use for long periods of time. For example, it often works well to make a range of editing actions available for toolbar customization, because people often use different types of editing commands based on their work style and their current project.

**Be prepared for translucency in the toolbar when content flows beneath it.** A toolbar automatically adopts translucency when placed above a scroll view or when the window is configured as a full-size content view. In visionOS, content that can scroll behind a toolbar uses a variable blur to ensure it remains legible and [passthrough](/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough)
 remains visible. In iOS, a toolbar is translucent by default, using a background material only when content appears behind it and removing the material when the view scrolls to the bottom. For guidance, see [Materials](/design/human-interface-guidelines/materials)
.

![A screenshot of the Notes app on iPhone that shows a group of notes below the search field. The toolbar is translucent, which makes the list background visible behind it.](https://docs-assets.developer.apple.com/published/a4cee02f0f7ab800d5b42db1501eb1f9/toolbar-no-background@2x.png)When no content appears behind the toolbar, the background material doesn’t appear.![A screenshot of the Notes app on iPhone that shows a group of notes partially obscured by the toolbar. The toolbar uses a background material that differs slightly from the list background.](https://docs-assets.developer.apple.com/published/368f3a4163e784b2b71cd01044d4bf9f/toolbar-background@2x.png)When content appears behind the toolbar, the background material changes to distinguish it from the content.[Platform considerations](/design/human-interface-guidelines/toolbars#Platform-considerations)
----------------------------------------------------------------------------------------------

*No additional considerations for tvOS.*

### [iOS](/design/human-interface-guidelines/toolbars#iOS)

Although toolbars and tab bars both appear at the bottom of a screen, each has a different purpose.

* A toolbar contains buttons for performing actions related to the screen, such as creating an item, filtering items, or marking up content.
* A tab bar lets people navigate among different areas of an app, such as the Alarm, Stopwatch, and Timer tabs in the Clock app.

Toolbars and tab bars don’t appear together in the same view.

**Avoid using a segmented control in a toolbar.** Segmented controls let people switch contexts, whereas a toolbar’s actions are specific to the current screen.

**In a toolbar that contains three or fewer buttons, consider using concise text labels instead of symbols to add clarity.** For example, Calendar uses the labels Today, Calendars, and Inbox. To ensure that the labels don’t run together, you can insert fixed spaces between the buttons. For developer guidance, see [`UIBarButtonSystemItemFixedSpace`](/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace)
.

![An illustration that represents the Calendar app on iPhone. The illustration includes indicators that show the spacing between its three toolbar buttons.](https://docs-assets.developer.apple.com/published/da3de211194f8ae82a75239ea53a6c7b/toolbar-button-spacing@2x.png)

**In a toolbar that has more than three buttons, consider using symbols to conserve space.** [SF Symbols](/design/human-interface-guidelines/sf-symbols)
 provides a wide range of customizable symbols you can use to represent actions in your app. If you need to create a custom interface icon for a toolbar button, use the following sizes, adjusting as needed for balance. For guidance, see [Icons](/design/human-interface-guidelines/icons)
.



| Target size | Maximum size |
| --- | --- |
| 24x24 px @1x (48x48 px @2x, 72x72 px @3x) | 28x28 px @1x (56x56 px @2x, 84x84 px @3x) |

### [iPadOS](/design/human-interface-guidelines/toolbars#iPadOS)

In iPadOS, a toolbar offers commonly used actions that affect the current task, along with document-specific functionality, a Back button, and important actions that people might want to take at any time. In contrast, a [navigation bar](/design/human-interface-guidelines/navigation-bars)
 doesn’t typically include document-specific functionality; instead, it supports app navigation, offers actions that help people manage their content, and can include a search field.

Developer note

In iPadOS, you use [`UINavigationBar`](/documentation/uikit/uinavigationbar)
 to create a toolbar.

In iPadOS 16 and later, different areas of the toolbar can display different types of items.

* **Leading end.** Elements that let people return to the previous document and show or hide a sidebar appear at the far leading end, followed by the document title. Next to the title the toolbar can include a document menu that contains standard and app-specific commands that affect the document as a whole, such as Duplicate, Rename, Move, and Export. To ensure that these items are always available regardless of window size, items in the toolbar’s leading end aren’t customizable.
* **Center area.** Frequently used items appear in the center area, where people can add, remove, and rearrange them. Items in the center section automatically collapse into the system-managed Overflow menu when the window shrinks enough in size.
* **Trailing end.** The trailing end of a toolbar contains important items that need to remain available, buttons that open nearby inspectors, an optional search field, and the Overflow menu that reveals hidden items and supports toolbar customization. Items in the trailing end remain visible at all window sizes.

**Place a toolbar at the top edge of the screen.** iPad has a large display that provides enough room for the functionality people appreciate, while preserving access to the most important commands even at small window sizes. If you’re transitioning an iPhone app to run on iPad, be sure to move toolbar buttons at the bottom of your iOS screen to the top of your iPadOS screen.

**Use the Document menu to offer commands that affect a document as a whole.** For example, you might include commands like Duplicate, Rename, Move, and Print. Avoid listing editing commands in the Document menu — instead, consider elevating these actions to the center area of the toolbar. Also avoid offering commands that open the document in other apps, because the Share menu already lets people perform actions like using Messages to send the document to someone else, opening it in another app, or adding it to a reading list.

**Prefer the center area for task-specific commands that people are most likely to use while they’re actively engaged with the content.** The center area is always available when the window is at full size, making it a convenient location for editing commands and other actions that affect the window’s content. Also, you can let people customize the items in the center area to support their personal work style. When people make your window smaller, items in the center section of the toolbar automatically transition into the toolbar-managed Overflow menu when there’s no longer enough room to display them.

**Prefer the trailing end of the toolbar for important items that need to be visible at all window sizes.** For example, Pages offers the Share menu in this area because people often want to perform an action on the document as a whole without expanding it. The trailing end of the toolbar is also an intuitive place to put inspector buttons that reveal panels located on the trailing side of the window.

### [macOS](/design/human-interface-guidelines/toolbars#macOS)

In a macOS app, the toolbar resides in the frame at the top of a window, either below or integrated with the title bar. Note that window titles can display inline with controls, and toolbar items don’t include a bezel.

![An illustration that represents a Finder window, highlighted to show the toolbar above the content area.](https://docs-assets.developer.apple.com/published/ed9ced3e701ccc93e0d61efaa84aded0/toolbar-macos@2x.png)

When horizontal space is limited, the toolbar can display the Search button in place of the search bar. When people click the Search button, the bar expands; when they click elsewhere in the window, the search bar collapses and the toolbar displays the button again.

![An illustration that represents the top-right corner of a Finder window. A search button appears on the right side of the toolbar.](https://docs-assets.developer.apple.com/published/a2fc31feac677c857c7c5c64e96e3898/toolbar-search-collapsed-macos@2x.png)

![An illustration that represents the top-right corner of a Finder window. A search bar appears on the right side of the toolbar.](https://docs-assets.developer.apple.com/published/fd79ba61b4ee1bab855da55ee109cd1c/toolbar-search-expanded-macos@2x.png)

In a settings window, the toolbar can use [SF Symbols](/design/human-interface-guidelines/sf-symbols)
 to harmonize with the appearance of the main window, but the title position remains above the toolbar buttons. When needed for clarity, individual toolbar buttons can include color. To indicate the active pane, the window applies a system-provided selection appearance to the selected toolbar button.

![An illustration that represents an app's settings window. The window's toolbar includes buttons to view different settings screens. The first button includes a gear symbol and is labeled General.](https://docs-assets.developer.apple.com/published/d705d167b4b2381ac47d383c3a197623/toolbar-settings-macos@2x.png)

**Make every toolbar item available as a command in the menu bar.** Because people can customize the toolbar or hide it, it can’t be the only place that presents a command. In contrast, it doesn’t make sense to provide a toolbar item for every menu item because not all menu commands are important enough or used often enough to warrant space in the toolbar.

Developer note

Toolbar items automatically use the large control size. The exception is an integrated toolbar-title bar area — such as the one in a Safari window — which continues to use the regular control size. You can use constraints if you need to specify minimum or maximum sizes for a toolbar control.

**Use recommended sizes if you need to create a custom image for a toolbar item.** To create a custom interface icon, use a maximum size of 19x19 px (38x38 px @2x). To create a full-color freestanding toolbar icon, use the PNG format and provide @1x version that measures 32x32 px and a @2x version that measures 64x64 px. If you use a recognizable full-color icon from elsewhere, don’t change its appearance or perspective.

**In general, avoid giving a toolbar item a persistent selected appearance.** The system adds a rounded-rectangle background to an item only when people move the pointer over it or choose it, removing the appearance when the item performs its action or the pointer moves away. There are two exceptions to this behavior. One is a segmented control that shows a persistent selected appearance within the context of the control — such as the view controls in a Finder window toolbar — and the second is in a settings window that uses toolbar items as pane switchers.

![An illustration that represents a Finder window, highlighted to show the currently selected item in the sidebar.](https://docs-assets.developer.apple.com/published/716bfe8eed638eb97f75a1afeb224c1e/sidebar-macos@2x.png)

**Consider letting people hide the toolbar, in addition to automatically hiding it in full-screen mode.** Sometimes people appreciate being able to hide the toolbar to minimize distractions or reveal more content. If you support this action, provide commands for hiding and revealing the toolbar in the [View menu](/design/human-interface-guidelines/the-menu-bar#View-menu)
. In full-screen mode, it can work well to hide the toolbar if people don’t need it to accomplish the focused task. For example, Preview hides the toolbar in a full-screen window because people are more likely to view content than to annotate it. If you hide the toolbar in a full-screen window, reveal it (along with the menu bar) when the pointer moves to the top of the screen.

**Consider letting people click nondestructive toolbar items when a window is inactive.** Usually, clicking the toolbar of an inactive window brings the window to the front. In some cases, it may be useful to let people invoke a toolbar item without bringing the window to the front so they can stay focused on a task in a different window. The toolbar of the standard Fonts panel behaves this way.

**Consider adding spring-loading support to toolbar items.** On pressure-sensitive systems, such as systems with the Magic Trackpad, spring loading lets people activate a button or segmented control segment by dragging items over it and force clicking — that is, pressing harder — without dropping the items. People can then continue dragging the items, possibly to perform additional actions. In Calendar, for example, people can drag an event over the day, week, month, or year segments in the toolbar. Force clicking a segment switches the calendar view without releasing the event, so people can drop the event at the desired location in the new calendar view.

### [visionOS](/design/human-interface-guidelines/toolbars#visionOS)

In visionOS, the system-provided toolbar appears along the bottom edge of a window, above the window-management controls, and in a parallel plane that’s slightly in front of the window along the z-axis.

![A screenshot of a toolbar along the bottom of the Photos app window in visionOS.](https://docs-assets.developer.apple.com/published/0b3e3dc1ae1b130c48062844ed0dd84d/visionos-toolbar-photos-app@2x.png)

As with other platforms except macOS, you supply either a symbol or a text label for each item in a toolbar. When people look at a toolbar item that contains a symbol, visionOS reveals the text label, providing additional information.

**Prefer using a system-provided toolbar.** The standard toolbar has a consistent and familiar appearance and is optimized to work well with eye and hand input. In addition, the system automatically places a standard toolbar in the correct position in relation to its window.

![A screenshot of a toolbar in visionOS.](https://docs-assets.developer.apple.com/published/d702e99b18df1e1534dd11dd7ba34a81/visionos-toolbar-standard-layout@2x.png)

**Avoid creating a vertical toolbar.** In visionOS, [tab bars](/design/human-interface-guidelines/tab-bars)
 are vertical, so presenting a vertical toolbar could confuse people.

**As much as possible, keep toolbar controls consistent when people resize the window.** Unlike macOS, visionOS doesn’t include a menu bar where each app lists all its actions, so it’s important for the toolbar to provide reliable access to essential controls regardless of a window’s size.

**If your app can enter a modal state, consider offering contextually relevant toolbar controls.** For example, a photo-editing app might enter a modal state to help people perform a multistep editing task. In this scenario, the controls in the modal editing view are different from the controls in the main window. Be sure to reinstate the window’s standard toolbar controls when the app exits the modal state.

**If necessary, consider including a pull-down menu in a toolbar.** A pull-down menu lets you offer additional actions related to a toolbar item, but can be difficult for people to discover and may clutter your interface. Because a toolbar is located at the bottom edge of a window in visionOS, a pull-down menu might obscure the standard window controls that appear below the bottom edge. For guidance, see [Pull-down buttons](/design/human-interface-guidelines/pull-down-buttons)
.

### [watchOS](/design/human-interface-guidelines/toolbars#watchOS)

A toolbar button lets you offer important app functionality in a view that displays related content. Located at the top of a scrolling view, a toolbar button can stay hidden behind the navigation bar until people reveal it by scrolling up. For developer guidance, see [`primaryAction`](/documentation/SwiftUI/ToolbarItemPlacement/primaryAction)
.

**Place a toolbar button only in a scrolling view.** People frequently scroll to the top of a scrolling view, so discovering a toolbar button is almost automatic. Placing a toolbar button in a nonscrolling view makes it permanently visible, eliminating the advantage of hiding it when it’s not needed.

**Use a toolbar button for an important action that isn’t a primary app function.** A toolbar button gives you the flexibility to offer important functionality in a view whose primary purpose is related to that functionality, but may not be the same. For example, Mail provides the essential New Message action in a toolbar button at the top of the Inbox view. The primary purpose of the Inbox is to display a scrollable list of email messages, so it makes sense to offer the closely related compose action in a toolbar button at the top of the view.

**Prefer a single, full-width toolbar button.** Displaying multiple toolbar buttons — whether stacked or side by side — can complicate the view and require people to make sure they’ve discovered the full set of actions before making a choice. If you’re considering more than one toolbar button, also consider whether your app needs a separate view to offer these essential actions.

A toolbar button lets you offer important app functionality in a view that displays related content. You can place toolbar buttons in the top corners or along the bottom of the screen. If you place these buttons above scrolling content, the buttons always remain visible, as the content scrolls under them.

![A screenshot showing toolbar buttons in the top leading and trailing corners.](https://docs-assets.developer.apple.com/published/f385f267ebde030f199c154d20c64b51/toolbar-watch-top-buttons@2x.png)Top toolbar buttons.![A screenshot showing two toolbar buttons in the bottom leading and trailing corners.](https://docs-assets.developer.apple.com/published/79d7dcddd5175837c2c59d80a7f37484/toolbar-watch-bottom-buttons@2x.png)Bottom toolbar buttons.For developer guidance, see [`topBarLeading`](/documentation/SwiftUI/ToolbarItemPlacement/topBarLeading)
, [`topBarTrailing`](/documentation/SwiftUI/ToolbarItemPlacement/topBarTrailing)
, or [`bottomBar`](/documentation/SwiftUI/ToolbarItemPlacement/bottomBar)
.

You can also place a button in the scrolling view. By default, a scrolling toolbar button remains hidden until people reveal it by scrolling up. People frequently scroll to the top of a scrolling view, so discovering a toolbar button is automatic.

![A screenshot showing two toolbar buttons in the top leading and trailing corners. The toolbar also has a primary action button in the scroll view, but it's hidden.](https://docs-assets.developer.apple.com/published/8f8cc7d5660481a7e6de823e59f9ff37/toolbar-watch-primary-button-hidden@2x.png)Toolbar button hidden.![A screenshot showing two toolbar buttons in the top leading and trailing corners. The toolbar also displays a primary action button in the scroll view.](https://docs-assets.developer.apple.com/published/23abbf346c5b8c71196857c50917396f/toolbar-watch-primary-button-visible@2x.png)Toolbar button shown.For developer guidance, see [`primaryAction`](/documentation/SwiftUI/ToolbarItemPlacement/primaryAction)
.

**Use a scrolling toolbar button for an important action that isn’t a primary app function.** A toolbar button gives you the flexibility to offer important functionality in a view whose primary purpose is related to that functionality, but may not be the same. For example, Mail provides the essential New Message action in a toolbar button at the top of the Inbox view. The primary purpose of the Inbox is to display a scrollable list of email messages, so it makes sense to offer the closely related compose action in a toolbar button at the top of the view.

[Resources](/design/human-interface-guidelines/toolbars#Resources)
------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/toolbars#Related)

[Navigation bars](/design/human-interface-guidelines/navigation-bars)


[Tab bars](/design/human-interface-guidelines/tab-bars)


[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/toolbars#Developer-documentation)

[`toolbar(content:)`](/documentation/SwiftUI/View/toolbar(content:)-5w0tj)


[`UIToolbar`](/documentation/uikit/uitoolbar)


[`NSToolbar`](/documentation/appkit/nstoolbar)


#### [Videos](/design/human-interface-guidelines/toolbars#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/6E076CE0-7DDF-4471-B6F0-005ADF9C7960/6500_wide_250x141_1x.jpg) What’s new in iPad app design](https://developer.apple.com/videos/play/wwdc2022/10009) 
[Change log](/design/human-interface-guidelines/toolbars#Change-log)
--------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using toolbars in watchOS. |


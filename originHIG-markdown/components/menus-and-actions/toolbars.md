# **[components-menus-and-actions] toolbars**

## A toolbar provides convenient access to frequently used commands and controls that perform actions relevant to the current view.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toolbar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toolbar-intro-dark_2x.png)

Depending on the platform, a toolbar can look and behave differently.

- In iOS, a toolbar appears at the bottom of a screen. iOS toolbars aren’t customizable, and they don’t support grouping.
- In iPadOS and macOS, a toolbar appears at the top of a screen or window. Both platforms support customizable toolbars and grouped toolbar items. In macOS, people can hide an app’s toolbar.
- In watchOS, the toolbar itself isn’t visible, but a toolbar button can appear at the top of a scrolling view. Typically, a toolbar button remains hidden behind a navigation bar until people reveal it by scrolling up.

# **Best practices**

**Provide toolbar items that support the main tasks people perform.** In general, prioritize the commands that people are mostly likely to want. These commands are often the ones people use most frequently, but in some apps it might make sense to prioritize commands that map to the highest level or most important objects people work with. In a macOS app, consider ordering the items in the toolbar according to your prioritization scheme.

**Avoid displaying too many toolbar items.** People need to be able to distinguish and activate each item, so you don’t want to overcrowd the toolbar.

**Consider grouping toolbar items where supported.** In iPadOS and macOS, you can define logical groups of items to help people find commands that are related to certain subtasks or functional areas in your app. For example, Keynote includes several groups that are based on functionality, including one for presentation-level commands, one for playback commands, and one for object insertion. In iPadOS, you can also use grouping to keep items together in the Overflow menu (to learn more, see [iPadOS](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars#ipados)).

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/layout_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/layout_2x.png)

**Make sure the meaning of each toolbar item is clear.** People shouldn’t need to guess or experiment to figure out what an item does. For each item, provide a simple, recognizable symbol or interface icon, or a short, descriptive label. In a macOS app, provide both so that people can view the symbol and the label in the toolbar if they choose. If you provide labels, prefer verbs and verb phrases like *View*, *Insert*, and *Share*. Use title-style capitalization and no ending punctuation.

**Prefer system-provided symbols or interface icons.** System-provided symbols are familiar, automatically receive appropriate coloring, and respond consistently to user interactions and vibrancy.

**Prefer a consistent appearance for all toolbar items.** Toolbars look best and are easiest to understand when all items use a similar visual style.

**If a toolbar item toggles between two states, make sure the item clearly communicates the current state.** You might consider changing the item’s color and label to clarify its current state. In the macOS Mail toolbar, for example, the online-offline toggle button displays a blue icon and a *Go Offline*label when accounts are online; when accounts are offline, the item displays a gray icon and a *Go Online* label.

**In iPadOS and macOS apps, consider letting people customize the toolbar.** Toolbar customization is especially useful in apps that provide a lot of items — or that include advanced functionality that not everyone needs — and in apps that people tend to use for long periods of time. For example, it often works well to make a range of editing actions available for toolbar customization, because people often use different types of editing commands based on their work style and their current project.

**Be prepared for translucency in the toolbar when content flows beneath it.** A toolbar automatically adopts translucency when placed above a scroll view or when the window is configured as a full-size content view. In iOS, for example, a toolbar is translucent by default, using a background material only when content appears behind it and removing the material when the view scrolls to the bottom. For guidance, see [Materials](https://developer.apple.com/design/human-interface-guidelines/foundations/materials).

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-background_2x.png)

The Mail toolbar uses a background material to distinguish itself from the mailboxes behind it.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-no-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-no-background_2x.png)

When no mailboxes appear behind the toolbar, the background material doesn’t appear.

# **Platform considerations**

*No additional considerations for tvOS.*

# **iOS**

Although toolbars and tab bars both appear at the bottom of a screen, each has a different purpose.

- A toolbar contains buttons for performing actions related to the screen, such as creating an item, filtering items, or marking up content.
- A tab bar lets people navigate among different areas of an app, such as the Alarm, Stopwatch, and Timer tabs in the Clock app.

Toolbars and tab bars don’t appear together in the same view.

**Avoid using a segmented control in a toolbar.** Segmented controls let people switch contexts, whereas a toolbar’s actions are specific to the current screen.

**In a toolbar that contains three or fewer buttons, consider using concise text labels instead of symbols to add clarity.** For example, Calendar uses the labels Today, Calendars, and Inbox. To ensure that the labels don’t run together, you can insert fixed spaces between the buttons. For developer guidance, see [UIBarButtonSystemItemFixedSpace](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace).

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-spacing_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-spacing_2x.png)

**In a toolbar that has more than three buttons, consider using symbols to conserve space.** [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) provides a wide range of customizable symbols you can use to represent actions in your app. If you need to create a custom interface icon for a toolbar button, use the following sizes, adjusting as needed for balance. For guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/foundations/icons).

| Target size | Maximum size |
| --- | --- |
| 24x24 px @1x (48x48 px @2x, 72x72 px @3x) | 28x28 px @1x (56x56 px @2x, 84x84 px @3x) |

# **iPadOS**

In iPadOS, a toolbar offers commonly used actions that affect the current task, along with document-specific functionality, a Back button, and important actions that people might want to take at any time. In contrast, a [navigation bar](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/navigation-bars) doesn’t typically include document-specific functionality; instead, it enables navigation through an app, offers actions that help people manage their content, and can include a search field.

**DEVELOPER NOTE**In iPadOS, you use [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar) to create a toolbar.

In iPadOS 16 and later, different areas of the toolbar can display different types of items.

- **Leading end.** Elements that let people return to the previous document and show or hide a sidebar appear at the far leading end, followed by the document title. Next to the title the toolbar can include a document menu that contains standard and app-specific commands that affect the document as a whole, such as Duplicate, Rename, Move, and Export. To ensure that these items are always available regardless of window size, items in the toolbar’s leading end aren't customizable.
- **Center area.** Frequently used items appear in the center area, where people can add, remove, and rearrange them. Items in the center section automatically collapse into the system-managed Overflow menu when the window shrinks enough in size.
- **Trailing end.** The trailing end of a toolbar contains important items that need to remain available, buttons that open nearby inspectors, an optional search field, and the Overflow menu that reveals hidden items and enables toolbar customization. Items in the trailing end remain visible at all window sizes.

**Place a toolbar at the top edge of the screen.** iPad has a large display that provides enough room for the functionality people appreciate, while preserving access to the most important commands even at small window sizes. If you’re transitioning an iPhone app to run on iPad, be sure to move toolbar buttons at the bottom of your iOS screen to the top of your iPadOS screen.

**Use the Document menu to offer commands that affect a document as a whole.** For example, you might include commands like Duplicate, Rename, Move, and Print. Avoid listing editing commands in the Document menu — instead, consider elevating these actions to the center area of the toolbar. Also avoid offering commands that open the document in other apps, because the Share menu already lets people perform actions like using Messages to send the document to someone else, opening it in another app, or adding it to a reading list.

**Prefer the center area for task-specific commands that people are most likely to use while they’re actively engaged with the content.** The center area is always available when the window is at full size, making it a convenient location for editing commands and other actions that affect the window’s content. Also, you can let people customize the items in the center area to support their personal work style. When people make your window smaller, items in the center section of the toolbar automatically transition into the toolbar-managed Overflow menu when there’s no longer enough room to display them.

**Prefer the trailing end of the toolbar for important items that need to be visible at all window sizes.** For example, Pages offers the Share menu in this area because people often want to perform an action on the document as a whole without expanding it. The trailing end of the toolbar is also an intuitive place to put inspector buttons that reveal panels located on the trailing side of the window.

# **macOS**

In a macOS app, the toolbar resides in the frame at the top of a window, either below or integrated with the title bar. Starting in macOS 11, window titles can display inline with controls, and toolbar items don’t include a bezel.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-macos_2x.png)

When horizontal space is limited, the toolbar can display the Search button in place of the search bar. When people click the Search button, the bar expands; when they click elsewhere in the window, the search bar collapses and the toolbar displays the button again.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-collapsed-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-collapsed-macos_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-expanded-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-search-expanded-macos_2x.png)

In a settings window, the toolbar can use [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) to harmonize with the appearance of the main window, but the title position remains above the toolbar buttons. When needed for clarity, individual toolbar buttons can include color. To indicate the active pane, the window applies a system-provided selection appearance to the selected toolbar button.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-settings-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-settings-macos_2x.png)

**Make every toolbar item available as a command in the menu bar.**Because people can customize the toolbar or hide it, it can’t be the only place that presents a command. In contrast, it doesn’t make sense to provide a toolbar item for every menu item because not all menu commands are important enough or used often enough to warrant space in the toolbar.

**DEVELOPER NOTE**Toolbar items automatically use the large control size. The exception is an integrated toolbar-title bar area — such as the one in a Safari window — which continues to use the regular control size. You can use constraints if you need to specify minimum or maximum sizes for a toolbar control.

**Use recommended sizes if you need to create a custom image for a toolbar item.** To create a custom interface icon, use a maximum size of 19x19 px (38x38 px @2x). To create a full-color freestanding toolbar icon, use the PNG format and provide @1x version that measures 32x32 px and a @2x version that measures 64x64 px. If you use a recognizable full-color icon from elsewhere, don’t change its appearance or perspective.

**In general, avoid giving a toolbar item a persistent selected appearance.** The system adds a rounded-rectangle background to an item only when people move the pointer over it or choose it, removing the appearance when the item performs its action or the pointer moves away. There are two exceptions to this behavior. One is a segmented control that shows a persistent selected appearance within the context of the control — such as the view controls in a Finder window toolbar — and the second is in a settings window that uses toolbar items as pane switchers.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/sidebar-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/sidebar-macos_2x.png)

**Consider letting people hide the toolbar, in addition to automatically hiding it in full-screen mode.** Sometimes people appreciate being able to hide the toolbar to minimize distractions or reveal more content. If you support this action, provide commands for hiding and revealing the toolbar in the [View menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/#view-menu). In full-screen mode, it can work well to hide the toolbar if people don’t need it to accomplish the focused task. For example, Preview hides the toolbar in a full-screen window because people are more likely to view content than to annotate it. If you hide the toolbar in a full-screen window, reveal it (along with the menu bar) when the pointer moves to the top of the screen.

**Consider letting people click nondestructive toolbar items when a window is inactive.** Usually, clicking the toolbar of an inactive window brings the window to the front. In some cases, it may be useful to let people invoke a toolbar item without bringing the window to the front so they can stay focused on a task in a different window. The toolbar of the standard Fonts panel behaves this way.

**Consider adding spring-loading support to toolbar items.** On pressure-sensitive systems, such as systems with the Magic Trackpad, spring loading lets people activate a button or segmented control segment by dragging items over it and force clicking — that is, pressing harder — without dropping the items. People can then continue dragging the items, possibly to perform additional actions. In Calendar, for example, people can drag an event over the day, week, month, or year segments in the toolbar. Force clicking a segment switches the calendar view without releasing the event, so people can drop the event at the desired location in the new calendar view.

# **watchOS**

A toolbar button lets you offer important app functionality in a view that displays related content. Located at the top of a scrolling view, a toolbar button can stay hidden behind the navigation bar until people reveal it by scrolling up.

Toolbar buttons are available in watchOS 7 and later; for developer guidance, see [ToolbarItemPlacement.primaryAction.](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/primaryaction)

**Place a toolbar button only in a scrolling view.** People frequently scroll to the top of a scrolling view, so discovering a toolbar button is almost automatic. Placing a toolbar button in a nonscrolling view makes it permanently visible, eliminating the advantage of hiding it when it’s not needed.

**Use a toolbar button for an important action that isn’t a primary app function.** A toolbar button gives you the flexibility to offer important functionality in a view whose primary purpose is related to that functionality, but may not be the same. For example, Mail provides the essential New Message action in a toolbar button at the top of the Inbox view. The primary purpose of the Inbox is to display a scrollable list of email messages, so it makes sense to offer the closely related compose action in a toolbar button at the top of the view.

**Prefer a single, full-width toolbar button.** Displaying multiple toolbar buttons — whether stacked or side by side — can complicate the view and require people to make sure they’ve discovered the full set of actions before making a choice. If you’re considering more than one toolbar button, also consider whether your app needs a separate view to enable these essential actions.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-revealed_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars/images/toolbar-button-revealed_2x.png)
June 21, 2023

 Updated to include guidance for visionOS. Keyboards
=========

A physical keyboard can be an essential input device for entering text, navigating, performing actions, and more.![A sketch of a keyboard, suggesting keyboard input. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/041dcf36a378d11a3727a6ff04989365/inputs-keyboard-intro@2x.png)

People might prefer using a physical keyboard when they need to type a lot of text, and some people prefer using one all the time. VoiceOver users often require a physical keyboard. People can connect a keyboard to any device except Apple Watch.

When a physical keyboard is available, people often rely on *keyboard shortcuts*, which offer efficient ways to initiate actions without using a mouse or trackpad to navigate a menu or click a button.

[Best practices](/design/human-interface-guidelines/keyboards#Best-practices)
-----------------------------------------------------------------------------

**Support keyboard-only interaction where possible.** As the name suggests, full keyboard-access mode lets people navigate and activate windows, menus, controls, and system features using only the keyboard. visionOS supports full keyboard-access mode, as does macOS (see [Navigate your app using Full Keyboard Access](https://support.apple.com/guide/mac-help/navigate-your-mac-using-full-keyboard-access-mchlc06d1059/mac)
) and iPadOS (see [Adjust the onscreen and external keyboard settings on iPad](https://support.apple.com/guide/ipad/keyboards-ipad424a3e13/ipados)
). In iPadOS, you can also enhance the experience of using a connected keyboard with your app by customizing visual effects that help people focus on individual items as they navigate your interface. For guidance, see [iPadOS](/design/human-interface-guidelines/focus-and-selection#iPadOS)
.

[Keyboard shortcuts](/design/human-interface-guidelines/keyboards#Keyboard-shortcuts)
-------------------------------------------------------------------------------------

Most keyboard shortcuts consist of a combination of keys: a single primary key and one or more of the modifier keys (Command, Shift, Control, and Option). A rare exception is the Esc (Escape) key, which people can use as a shortcut to invoke a cancel action in various contexts.

People discover keyboard shortcuts in a couple of ways. For example, a macOS app lists its keyboard shortcuts in its menu bar menus (to learn more, see [The menu bar](/design/human-interface-guidelines/the-menu-bar)
).

![A screenshot of the Safari File menu, showing the keyboard shortcuts available for various menu item.](https://docs-assets.developer.apple.com/published/19fc18fec486adca5defdc5b4f56a9e7/menus-in-macos@2x.png)

The keyboard shortcuts in a visionOS or iPadOS app appear in the shortcut interface that displays when people hold the Command key on a connected keyboard. Similar in organization to an app’s menu bar menus on a Mac, the shortcut interface on Apple Vision Pro and iPad displays app commands in familiar system-defined menu categories such as File, Edit, and View; unlike menu bar menus, it displays all relevant categories in one view, listing within each category only available commands that also have shortcuts.

![A partial screenshot of the keyboard shortcut interface in the Maps app on iPad. The interface lists shortcuts for commands such as Drop Pin and Switch to Explore.](https://docs-assets.developer.apple.com/published/bccbaf607b1cca4f21d64646c9ac444b/keyboard-shortcut-interface@2x.png)

**Respect standard keyboard shortcuts.** People expect the standard keyboard shortcuts to work, regardless of the app they’re using. You can also help people learn your app quickly by supporting the [standard keyboard shortcuts](/design/human-interface-guidelines/keyboards#Standard-keyboard-shortcuts)
 that make sense in your app.

**In general, don’t repurpose standard keyboard shortcuts for custom actions.** People can get confused when the shortcuts they know work differently in your app. Only consider redefining a standard shortcut if its action doesn’t make sense in your app. For example, an app that doesn’t support text editing doesn’t need a text-styling command like Italic, so it might use Command–I for an action that has more relevance in the app, such as Get Info.

**Define custom keyboard shortcuts for only the most common actions in your app.** People appreciate using keyboard shortcuts for app-specific actions they perform frequently, but defining too many new shortcuts risks making your app seem difficult to learn and can clutter the shortcut interface in visionOS and iPadOS apps. Minimizing app-specific keyboard shortcuts also helps avoid potential conflicts with system-defined shortcuts that may be in place.

**Let people use modifier and other keys to adjust the behavior of some interactions.** For example, pressing Command while dragging moves items as a group, and pressing Shift while drag-resizing constrains resizing to the item’s aspect ratio. In addition, holding an arrow key moves the selected item by the smallest app-defined unit of distance until people release the key.

**Help people discover available actions in your visionOS or iPadOS app.** Because the shortcut interface displays a flat list of all items in each category, submenu titles aren’t available to provide context for their child items. For example, the item titles Name and Date Added don’t make sense without the context of the submenu title Sort Bookmarks By. You can enhance each item’s title by including the necessary context, such as Sort Bookmarks by Name and Sort Bookmarks by Date Added. For developer guidance, see [`discoverabilityTitle`](/documentation/uikit/uikeycommand/1621094-discoverabilitytitle)
.

[Custom keyboard shortcuts](/design/human-interface-guidelines/keyboards#Custom-keyboard-shortcuts)
---------------------------------------------------------------------------------------------------

It’s important for custom keyboard shortcuts to use modifier keys in ways that people expect.

Here are the modifier keys and the symbols that represent them.



| Modifier Key | Symbol |
| --- | --- |
| Control | A shallow, upside-down V shape. |
| Option | Line segments that suggest a horizontally transformed Z shape combined with a short horizontal segment aligned with the top of the Z. |
| Shift | Outline of an upward-pointing arrow. |
| Command | Outline of a stylized clover shape. |

**Prefer the Command key as the main modifier key in a custom keyboard shortcut.** Most standard keyboard shortcuts use the Command key, so people are familiar with it.

**Prefer the Shift key as a secondary modifier when the shortcut complements another shortcut.** For example, Command-P displays the Print dialog in most apps. The standard shortcut for the Page Setup dialog, which complements printing, is typically Shift-Command-P.

**Use the Option modifier sparingly.** For example, you might use Option in the shortcut for a less-common command or a convenience or power feature. For example, the Finder uses Option-Command-W for Close All Windows and Option-Command-M for Minimize All Windows.

**As much as possible, avoid using the Control key as a modifier.** The system uses Control in many systemwide features, like moving focus or capturing screenshots.

**Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command.** For example, because people are accustomed to using Command-Z for undoing an action, it would be confusing to use Shift-Command-Z as the shortcut for a command that’s unrelated to undo and redo.

**List modifier keys in the correct order.** If you use more than one modifier key in a custom shortcut, always list them in this order: Control, Option, Shift, Command.

**Identify a two-character key by its lower character unless Shift is part of the shortcut.** For example, the keyboard shortcut for Hide Status Bar is Command-Slash (/). If the Shift key is part of the keyboard shortcut, identify the key using the upper of the two characters. For example, the keyboard shortcut for Help is Command-Question Mark (?), not Shift-Command-Slash.

Tip

Some languages require modifier keys to generate certain characters. For example, on a French keyboard, Option-5 generates the “{“ character. It’s usually safe to use the Command key as a modifier, but avoid using an additional modifier with characters that aren’t available on all keyboards. If you must use a modifier other than Command, prefer using it only with the alphabetic characters.

**Let the system localize and mirror your keyboard shortcuts as needed.** For example, iPadOS automatically localizes a shortcut’s primary key and modifier keys to support the currently connected keyboard. Also, if your app switches to a right-to-left layout, the system automatically mirrors the shortcut. For guidance, see [Right to left](/design/human-interface-guidelines/right-to-left)
.

[Platform considerations](/design/human-interface-guidelines/keyboards#Platform-considerations)
-----------------------------------------------------------------------------------------------

*No additional considerations for iOS, macOS, or tvOS. Not supported in watchOS.*

### [iPadOS](/design/human-interface-guidelines/keyboards#iPadOS)

By default, iPadOS 15 and later supports keyboard navigation in text fields, text views, and sidebars, providing APIs you can use to support it in various types of collection views and other custom views in your app. For guidance, see [iPadOS](/design/human-interface-guidelines/focus-and-selection#iPadOS)
; for developer guidance, see [Focus-based navigation](/documentation/uikit/focus-based_navigation)
.

Important

Avoid supporting keyboard navigation for controls, such as buttons, segmented controls, and switches. [Full keyboard-access](https://support.apple.com/guide/ipad/keyboards-ipad424a3e13/ipados)
 already helps people activate controls, navigate to all onscreen components, and even perform gesture-based interactions like drag and drop.

### [visionOS](/design/human-interface-guidelines/keyboards#visionOS)

**Be prepared for people wanting to use a physical keyboard with your app.** People typically prefer using a connected keyboard when they need to perform tasks that require a lot of text entry, such as creating a presentation, and they often appreciate using keyboard shortcuts to navigate and initiate actions throughout the system and their apps. In addition, many people rely on physical keyboards for full keyboard-access mode or VoiceOver interactions.

 [Play](#) 
[Specifications](/design/human-interface-guidelines/keyboards#Specifications)
-----------------------------------------------------------------------------

### [Standard keyboard shortcuts](/design/human-interface-guidelines/keyboards#Standard-keyboard-shortcuts)

People expect each of the following standard keyboard shortcuts to perform the action listed in the table below.



| Primary key | Keyboard shortcut | Action |
| --- | --- | --- |
| Space | Command-Space | Show or hide the Spotlight search field. |
|  | Shift-Command-Space | Varies. |
|  | Option-Command-Space | Show the Spotlight search results window. |
|  | Control-Command-Space | Show the Special Characters window. |
| Tab | Shift-Tab | Navigate through controls in a reverse direction. |
|  | Command-Tab | Move forward to the next most recently used app in a list of open apps. |
|  | Shift-Command-Tab | Move backward through a list of open apps (sorted by recent use). |
|  | Control-Tab | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell). |
|  | Control-Shift-Tab | Move focus to the previous group of controls. |
| Esc | Option-Command-Esc | Open the Force Quit dialog. |
| Eject | Control-Command-Eject | Quit all apps (after changes have been saved to open documents) and restart the computer. |
|  | Control-Option-Command-Eject | Quit all apps (after changes have been saved to open documents) and shut the computer down. |
| F1 | Control-F1 | Toggle full keyboard access on or off. |
| F2 | Control-F2 | Move focus to the menu bar. |
| F3 | Control- F3 | Move focus to the Dock. |
| F4 | Control-F4 | Move focus to the active (or next) window. |
|  | Control-Shift-F4 | Move focus to the previously active window. |
| F5 | Control-F5 | Move focus to the toolbar. |
|  | Command-F5 | Turn VoiceOver on or off. |
| F6 | Control-F6 | Move focus to the first (or next) panel. |
|  | Control-Shift-F6 | Move focus to the previous panel. |
| F7 | Control-F7 | Temporarily override the current keyboard access mode in windows and dialogs. |
| F8 |  | Varies. |
| F9 |  | Varies. |
| F10 |  | Varies. |
| F11 |  | Show desktop. |
| F12 |  | Hide or display Dashboard. |
| Grave accent (`) | Command-Grave accent | Activate the next open window in the frontmost app. |
|  | Shift-Command-Grave accent | Activate the previous open window in the frontmost app. |
|  | Option-Command-Grave accent | Move focus to the window drawer. |
| Hyphen (-) | Command-Hyphen | Decrease the size of the selection. |
|  | Option-Command-Hyphen | Zoom out when screen zooming is on. |
| Left bracket ({) | Command-Left bracket | Left-align a selection. |
| Right bracket (}) | Command-Right bracket | Right-align a selection. |
| Pipe (|) | Command-Pipe | Center-align a selection. |
| Colon (:) | Command-Colon | Display the Spelling window. |
| Semicolon (;) | Command-Semicolon | Find misspelled words in the document. |
| Comma (,) | Command-Comma | Open the app’s settings window. |
|  | Control-Option-Command-Comma | Decrease screen contrast. |
| Period (.) | Control-Option-Command-Period | Increase screen contrast. |
| Question mark (?) | Command-Question mark | Open the app’s Help menu. |
| Forward slash (/) | Option-Command-Forward slash | Turn font smoothing on or off. |
| Equal sign (=) | Shift-Command-Equal sign | Increase the size of the selection. |
|  | Option-Command-Equal sign | Zoom in when screen zooming is on. |
| 3 | Shift-Command-3 | Capture the screen to a file. |
|  | Control-Shift-Command-3 | Capture the screen to the Clipboard. |
| 4 | Shift-Command-4 | Capture a selection to a file. |
|  | Control-Shift-Command-4 | Capture a selection to the Clipboard. |
| 8 | Option-Command-8 | Turn screen zooming on or off. |
|  | Control-Option-Command-8 | Invert the screen colors. |
| A | Command-A | Select every item in a document or window, or all characters in a text field. |
|  | Shift-Command-A | Deselect all selections or characters. |
| B | Command-B | Boldface the selected text or toggle boldfaced text on and off. |
| C | Command-C | Copy the selection to the Clipboard. |
|  | Shift-Command-C | Display the Colors window. |
|  | Option-Command-C | Copy the style of the selected text. |
|  | Control-Command-C | Copy the formatting settings of the selection and store on the Clipboard. |
| D | Option-Command-D | Show or hide the Dock. |
|  | Control-Command-D | Display the definition of the selected word in the Dictionary app. |
| E | Command-E | Use the selection for a find operation. |
| F | Command-F | Open a Find window. |
|  | Option-Command-F | Jump to the search field control. |
|  | Control-Command-F | Enter full screen. |
| G | Command-G | Find the next occurrence of the selection. |
|  | Shift-Command-G | Find the previous occurrence of the selection. |
| H | Command-H | Hide the windows of the currently running app. |
|  | Option-Command-H | Hide the windows of all other running apps. |
| I | Command-I | Italicize the selected text or toggle italic text on or off. |
|  | Command-I | Display an Info window. |
|  | Option-Command-I | Display an inspector window. |
| J | Command-J | Scroll to a selection. |
| M | Command-M | Minimize the active window to the Dock. |
|  | Option-Command-M | Minimize all windows of the active app to the Dock. |
| N | Command-N | Open a new document. |
| O | Command-O | Display a dialog for choosing a document to open. |
| P | Command-P | Display the Print dialog. |
|  | Shift-Command-P | Display the Page Setup dialog. |
| Q | Command-Q | Quit the app. |
|  | Shift-Command-Q | Log out the person currently logged in. |
|  | Option-Shift-Command-Q | Log out the person currently logged in without confirmation. |
| S | Command-S | Save a new document or save a version of a document. |
|  | Shift-Command-S | Duplicate the active document or initiate a Save As. |
| T | Command-T | Display the Fonts window. |
|  | Option-Command-T | Show or hide a toolbar. |
| U | Command-U | Underline the selected text or turn underlining on or off. |
| V | Command-V | Paste the Clipboard contents at the insertion point. |
|  | Shift-Command-V | Paste as (Paste as Quotation, for example). |
|  | Option-Command-V | Apply the style of one object to the selection. |
|  | Option-Shift-Command-V | Paste the Clipboard contents at the insertion point and apply the style of the surrounding text to the inserted object. |
|  | Control-Command-V | Apply formatting settings to the selection. |
| W | Command-W | Close the active window. |
|  | Shift-Command-W | Close a file and its associated windows. |
|  | Option-Command-W | Close all windows in the app. |
| X | Command-X | Remove the selection and store on the Clipboard. |
| Z | Command-Z | Undo the previous operation. |
|  | Shift-Command-Z | Redo (when Undo and Redo are separate commands rather than toggled using Command-Z). |
| Right arrow | Command-Right arrow | Change the keyboard layout to current layout of Roman script. |
|  | Shift-Command-Right arrow | Extend selection to the next semantic unit, typically the end of the current line. |
|  | Shift-Right arrow | Extend selection one character to the right. |
|  | Option-Shift-Right arrow | Extend selection to the end of the current word, then to the end of the next word. |
|  | Control-Right arrow | Move focus to another value or cell within a view, such as a table. |
| Left arrow | Command-Left arrow | Change the keyboard layout to current layout of system script. |
|  | Shift-Command-Left arrow | Extend selection to the previous semantic unit, typically the beginning of the current line. |
|  | Shift-Left arrow | Extend selection one character to the left. |
|  | Option-Shift-Left arrow | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
|  | Control-Left arrow | Move focus to another value or cell within a view, such as a table. |
| Up arrow | Shift-Command-Up arrow | Extend selection upward in the next semantic unit, typically the beginning of the document. |
|  | Shift-Up arrow | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Up arrow | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
|  | Control-Up arrow | Move focus to another value or cell within a view, such as a table. |
| Down arrow | Shift-Command-Down arrow | Extend selection downward in the next semantic unit, typically the end of the document. |
|  | Shift-Down arrow | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Down arrow | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
|  | Control-Down arrow | Move focus to another value or cell within a view, such as a table. |

### [Standard international keyboard shortcuts](/design/human-interface-guidelines/keyboards#Standard-international-keyboard-shortcuts)

The system defines several key combinations for use with localized versions of the system, localized keyboard, keyboard layouts, and input methods. These shortcuts don’t correspond directly to menu commands.



| Keyboard shortcut | Action |
| --- | --- |
| Control-Space | Toggle between the current and last input source. |
| Control-Option-Space | Switch to the next input source in the list. |
| [Modifier key]-Command-Space | Varies. |
| Command-Right arrow | Change keyboard layout to current layout of Roman script. |
| Command-Left arrow | Change keyboard layout to current layout of system script. |

[Resources](/design/human-interface-guidelines/keyboards#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/keyboards#Related)

[Virtual keyboards](/design/human-interface-guidelines/virtual-keyboards)


[Entering data](/design/human-interface-guidelines/entering-data)


[Pointing devices](/design/human-interface-guidelines/pointing-devices)


#### [Developer documentation](/design/human-interface-guidelines/keyboards#Developer-documentation)

[`KeyboardShortcut`](/documentation/SwiftUI/KeyboardShortcut)


[Input events](/documentation/SwiftUI/Input-events)


[Handling key presses made on a physical keyboard](/documentation/uikit/mac_catalyst/handling_key_presses_made_on_a_physical_keyboard)


[Mouse, Keyboard, and Trackpad](/documentation/appkit/mouse_keyboard_and_trackpad)


#### [Videos](/design/human-interface-guidelines/keyboards#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/9CCE8A5D-A751-441C-B88F-FB91E2D1958E/4949_wide_250x141_1x.jpg) What's new in UIKit](https://developer.apple.com/videos/play/wwdc2021/10059) 
[Change log](/design/human-interface-guidelines/keyboards#Change-log)
---------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |


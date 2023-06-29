# **[inputs] keyboards**

## A physical keyboard can be an essential input device for entering text, navigating, performing actions, and more.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-keyboard-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-keyboard-intro_2x.png)

On a Mac, some people prefer using a keyboard instead of a mouse or a trackpad, and VoiceOver users require it. People can also connect an external keyboard to their iPhone, iPad, or TV.

When a physical keyboard is available, people often rely on *keyboard shortcuts*, which offer efficient ways to initiate actions without using a mouse or trackpad to navigate a menu or click a button.

# **Best practices**

**Support keyboard-only interaction where possible.** As the name suggests, full keyboard-access mode lets people navigate and activate windows, menus, controls, and system features using only the keyboard. To learn more, see [Navigate your app using Full Keyboard Access](https://support.apple.com/guide/mac-help/navigate-your-mac-using-full-keyboard-access-mchlc06d1059/mac) and [Adjust the onscreen and external keyboard settings on iPad](https://support.apple.com/guide/ipad/keyboards-ipad424a3e13/ipados). In iPadOS, you can enhance the experience of using a connected keyboard with your app by customizing visual effects that help people focus on individual items as they navigate your interface. For guidance, see [Keyboard navigation on iPad](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#keyboard-navigation-on-ipad).

# **Keyboard shortcuts**

Most keyboard shortcuts consist of a combination of keys: a single primary key and one or more of the modifier keys (Command, Shift, Control, and Option). A rare exception is the Esc (Escape) key, which people can use as a shortcut to invoke a cancel action in various contexts.

People discover keyboard shortcuts in a couple of ways. For example, a macOS app lists its keyboard shortcuts in its menu bar menus (to learn more, see [The menu bar](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar)).

![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/menus-in-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/menus-in-macos_2x.png)

The keyboard shortcuts in an iPadOS app appear in the shortcut interface that displays when people hold the Command key on a connected keyboard. Similar in organization to an app’s menu bar menus on a Mac, the shortcut interface on iPad displays app commands in familiar system-defined menu categories such as File, Edit, and View. Unlike menu bar menus, the iPad interface displays all relevant categories in one view, listing within each category only available commands that also have shortcuts.

![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/keyboard-shortcut-interface_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/keyboard-shortcut-interface_2x.png)

**Respect standard keyboard shortcuts.** People expect the standard keyboard shortcuts to work, regardless of the app they’re using. You can also help people learn your app quickly by supporting the [system-defined keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#reserved-keyboard-shortcuts) that make sense in your app.

**In general, don’t repurpose standard keyboard shortcuts for custom actions.** People can get confused when the shortcuts they know work differently in your app. Only consider redefining a standard shortcut if its action doesn’t make sense in your app. For example, an app that doesn’t support text editing doesn’t need a text-styling command like Italic, so it might use Command–I for an action that has more relevance in the app, such as Get Info.

**Define custom keyboard shortcuts for only the most common actions in your app.** People appreciate using keyboard shortcuts for app-specific actions they perform frequently, but defining too many new shortcuts risks making your app seem difficult to learn and can clutter the shortcut interface in an iPadOS app. Minimizing app-specific keyboard shortcuts also helps avoid potential conflicts with system-defined shortcuts that may be in place.

**Let people use modifier and other keys to adjust the behavior of some interactions.** For example, pressing Command while dragging moves items as a group, and pressing Shift while drag-resizing constrains resizing to the item’s aspect ratio. In addition, holding an arrow key moves the selected item by the smallest app-defined unit of distance until people release the key.

# **Custom keyboard shortcuts**

It’s important for custom keyboard shortcuts to use modifier keys in ways that people expect.

Here are the modifier keys and the symbols that represent them.

[제목 없음](https://www.notion.so/f4f77f527d9e44ae9000234f5b840435)

**Prefer the Command key as the main modifier key in a custom keyboard shortcut.** Most standard keyboard shortcuts use the Command key, so people are familiar with it.

**Prefer the Shift key as a secondary modifier when the shortcut complements another shortcut.** For example, Command-P displays the Print dialog in most apps. The standard shortcut for the Page Setup dialog, which complements printing, is typically Shift-Command-P.

**Use the Option modifier sparingly.** For example, you might use Option in the shortcut for a less-common command or a convenience or power feature. For example, the Finder uses Option-Command-W for Close All Windows and Option-Command-M for Minimize All Windows.

**As much as possible, avoid using the Control key as a modifier.** The system uses Control in many systemwide features, like moving focus or capturing screenshots.

**Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command.** For example, because people are accustomed to using Command-Z for undoing an action, it would be confusing to use Shift-Command-Z as the shortcut for a command that’s unrelated to undo and redo.

**List modifier keys in the correct order.** If you use more than one modifier key in a custom shortcut, always list them in this order: Control, Option, Shift, Command.

**Identify a two-character key by its lower character unless Shift is part of the shortcut.** For example, the keyboard shortcut for Hide Status Bar is Command-Slash (/). If the Shift key is part of the keyboard shortcut, identify the key using the upper of the two characters. For example, the keyboard shortcut for Help is Command-Question Mark (?), not Shift-Command-Slash.

**TIP**Some languages require modifier keys to generate certain characters. For example, on a French keyboard, Option-5 generates the “{“ character. It’s usually safe to use the Command key as a modifier, but avoid using an additional modifier with characters that aren’t available on all keyboards. If you must use a modifier other than Command, prefer using it only with the alphabetic characters.

**Let the system localize and mirror your keyboard shortcuts as needed.**For example, iPadOS automatically localizes a shortcut’s primary key and modifier keys to support the currently connected keyboard. Also, if your app switches to a right-to-left layout, the system automatically mirrors the shortcut. For guidance, see [Right to left](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left).

# **Platform considerations**

*No additional considerations for iOS, macOS, or tvOS. Not supported in watchOS.*

# **iPadOS**

**Help people discover available actions in your iPadOS app.** Because the iPad shortcut interface displays a flat list of all items in each category, submenu titles aren’t available to provide context for their child items. For example, the item titles Name and Date Added don’t make sense without the context of the submenu title Sort Bookmarks By. You can enhance each item’s title by including the necessary context, such as Sort Bookmarks by Name and Sort Bookmarks by Date Added. For developer guidance, see [discoverabilityTitle](https://developer.apple.com/documentation/uikit/uikeycommand/1621094-discoverabilitytitle).

### **Keyboard navigation on iPad**

By default, iPadOS 15 and later enables keyboard navigation in text fields, text views, and sidebars, providing APIs you can use to enable it in various types of collection views and other custom views in your app. For developer guidance, see [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based_navigation).

**IMPORTANT**Avoid enabling keyboard navigation for controls, such as buttons, segmented controls, and switches. Full keyboard-access mode already helps people activate controls, navigate to all onscreen components, and even perform gesture-based interactions like drag and drop.

The iPadOS and tvOS focus systems are similar. People perform actions by moving a focus indicator to an item and then selecting it (for guidance, see [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/inputs/focus-and-selection)). Although the underlying system is the same, the user experiences are a little different. tvOS uses *directional focus*, which means that people can use the same interaction — that is, swiping the Siri Remote or using only the arrow keys on a connected keyboard — to navigate to every onscreen component. In contrast, iPadOS defines *focus groups*, which represent specific areas within an app, like a sidebar, grid, or list. Using focus groups, iPadOS can support two different keyboard interactions.

- Pressing the Tab key moves focus among focus groups, letting people navigate to sidebars, grids, and other app areas.
- Pressing an arrow key enables a directional focus interaction that’s similar to tvOS, but limited to navigation among items in the same focus group. For example, people can use an arrow key to move through the items in a list or a sidebar.

Onscreen components can indicate focus by using the halo effect or the highlighted appearance.

The *halo* focus effect — also known as the *focus ring* — displays a customizable outline around the component. You can apply the halo effect to custom views and to fully opaque content within a collection or list cell, such as an image.

![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/halo-focus-effect_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/halo-focus-effect_2x.png)

Photos uses the halo effect to indicate the focused photo in a collection.

**Customize the halo focus effect when necessary.** By default, the system uses an item’s shape to infer the shape of its halo. If the system-provided halo doesn’t give you the appearance you want, you can refine it to match contours like rounded corners or shapes defined by Bézier paths. You can also adjust a halo’s position if another component occludes or clips it. For example, you might need to ensure that a badge appears above the halo or that a parent view doesn’t clip it. For developer guidance, see [UIFocusHaloEffect](https://developer.apple.com/documentation/uikit/uifocushaloeffect).

![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/customized-halo_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/customized-halo_2x.png)

Photos uses a rounded-corner halo to match the corners of the focused album’s thumbnail.

The *highlighted* appearance — in which the component’s background uses the app’s accent color — also indicates focus, but it’s not a focus effect. The highlight appearance occurs automatically when people select a collection view cell on which you’ve set background and content configurations (for developer guidance, see [UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewcell)).

![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/highlighted-appearance_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/highlighted-appearance_2x.png)

Photos uses the highlighted appearance to indicate the selected item in the sidebar.

**Ensure that focus moves through your custom views in ways that make sense.** As people continue pressing the Tab key, focus moves through focus groups in reading order: leading to trailing, and top to bottom. Although focus moves through system-provided views in ways that people expect, you might need to adjust the order in which the focus system visits your custom views. For example, if you want focus to move down through a vertical stack of custom views before it moves in the trailing direction to the next view, you need to identify the stack container as a single focus group. For developer guidance, see [focusGroupIdentifier](https://developer.apple.com/documentation/uikit/uifocusenvironment/3601224-focusgroupidentifier).

**Adjust the priority of an item to reflect its importance within a focus group.** When a group receives focus, its *primary item* automatically receives focus too, making it easy for people to select the item they’re most likely to want. You can make an item primary by increasing its priority. For developer guidance, see [UIFocusGroupPriority](https://developer.apple.com/documentation/uikit/uifocusgrouppriority/).

# **Specifications**

# **Reserved keyboard shortcuts**

The following keyboard shortcuts are either reserved by the system or well-known to people.

| Primary Key | Keyboard Shortcut | Used by the System | Action |
| --- | --- | --- | --- |
| Space | Command-Space | ● | Show or hide the Spotlight search field. |
|  | Shift-Command-Space | ● | Varies. Apple reserved. |
|  | Option-Command-Space | ● | Show the Spotlight search results window. |
|  | Control-Command-Space | ● | Show the Special Characters window. |
| Tab | Shift-Tab | ● | Navigate through controls in a reverse direction. |
|  | Command-Tab | ● | Move forward to the next most recently used app in a list of open apps. |
|  | Shift-Command-Tab | ● | Move backward through a list of open apps (sorted by recent use). |
|  | Control-Tab | ● | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell). |
|  | Control-Shift-Tab | ● | Move focus to the previous group of controls. |
| Esc | Option-Command-Esc | ● | Open the Force Quit dialog. |
| Eject | Control-Command-Eject | ● | Quit all apps (after changes have been saved to open documents) and restart the computer. |
|  | Control-Option-Command-Eject | ● | Quit all apps (after changes have been saved to open documents) and shut the computer down. |
| F1 | Control-F1 | ● | Toggle full keyboard access on or off. |
| F2 | Control-F2 | ● | Move focus to the menu bar. |
| F3 | Control- F3 | ● | Move focus to the Dock. |
| F4 | Control-F4 | ● | Move focus to the active (or next) window. |
|  | Control-Shift-F4 | ● | Move focus to the previously active window. |
| F5 | Control-F5 | ● | Move focus to the toolbar. |
|  | Command-F5 | ● | Turn VoiceOver on or off. |
| F6 | Control-F6 | ● | Move focus to the first (or next) panel. |
|  | Control-Shift-F6 | ● | Move focus to the previous panel. |
| F7 | Control-F7 | ● | Temporarily override the current keyboard access mode in windows and dialogs. |
| F8 |  | ● | Varies. Apple reserved. |
| F9 |  | ● | Varies. Apple reserved. |
| F10 |  | ● | Varies. Apple reserved. |
| F11 |  | ● | Show desktop. |
| F12 |  | ● | Hide or display Dashboard. |
| Grave accent (`) | Command-Grave accent | ● | Activate the next open window in the frontmost app. |
|  | Shift-Command-Grave accent | ● | Activate the previous open window in the frontmost app. |
|  | Option-Command-Grave accent | ● | Move focus to the window drawer. |
| Hyphen (-) | Command-Hyphen | ● | Decrease the size of the selection. |
|  | Option-Command-Hyphen | ● | Zoom out when screen zooming is on. |
| Left bracket ({) | Command-Left bracket |  | Left-align a selection. |
| Right bracket (}) | Command-Right bracket |  | Right-align a selection. |
| Pipe (|) | Command-Pipe |  | Center-align a selection. |
| Colon (:) | Command-Colon |  | Display the Spelling window. |
| Semicolon (;) | Command-Semicolon |  | Find misspelled words in the document. |
| Comma (,) | Command-Comma |  | Open the app’s settings window. |
|  | Control-Option-Command-Comma | ● | Decrease screen contrast. |
| Period (.) | Control-Option-Command-Period | ● | Increase screen contrast. |
| Question mark (?) | Command-Question mark |  | Open the app’s Help menu. |
| Forward slash (/) | Option-Command-Forward slash | ● | Turn font smoothing on or off. |
| Equal sign (=) | Shift-Command-Equal sign | ● | Increase the size of the selection. |
|  | Option-Command-Equal sign | ● | Zoom in when screen zooming is on. |
| 3 | Shift-Command-3 | ● | Capture the screen to a file. |
|  | Control-Shift-Command-3 | ● | Capture the screen to the Clipboard. |
| 4 | Shift-Command-4 | ● | Capture a selection to a file. |
|  | Control-Shift-Command-4 | ● | Capture a selection to the Clipboard. |
| 8 | Option-Command-8 | ● | Turn screen zooming on or off. |
|  | Control-Option-Command-8 | ● | Invert the screen colors. |
| A | Command-A |  | Selects every item in a document or window, or all characters in a text field. |
|  | Shift-Command-A |  | Deselects all selections or characters. |
| B | Command-B |  | Boldface the selected text or toggle boldfaced text on and off. |
| C | Command-C |  | Copy the selection to the Clipboard. |
|  | Shift-Command-C |  | Display the Colors window. |
|  | Option-Command-C |  | Copy the style of the selected text. |
|  | Control-Command-C |  | Copy the formatting settings of the selection and store on the Clipboard. |
| D | Option-Command-D | ● | Show or hide the Dock. |
|  | Control-Command-D |  | Display the definition of the selected word in the Dictionary app. |
| E | Command-E |  | Use the selection for a find operation. |
| F | Command-F |  | Open a Find window. |
|  | Option-Command-F |  | Jump to the search field control. |
|  | Control-Command-F |  | Enter full screen. |
| G | Command-G |  | Find the next occurrence of the selection. |
|  | Shift-Command-G |  | Find the previous occurrence of the selection. |
| H | Command-H |  | Hide the windows of the currently running app. |
|  | Option-Command-H |  | Hide the windows of all other running apps. |
| I | Command-I |  | Italicize the selected text or toggle italic text on or off. |
|  | Command-I |  | Display an Info window. |
|  | Option-Command-I |  | Display an inspector window. |
| J | Command-J |  | Scroll to a selection. |
| M | Command-M |  | Minimize the active window to the Dock. |
|  | Option-Command-M |  | Minimize all windows of the active app to the Dock. |
| N | Command-N |  | Open a new document. |
| O | Command-O |  | Display a dialog for choosing a document to open. |
| P | Command-P |  | Display the Print dialog. |
|  | Shift-Command-P |  | Display the Page Setup dialog. |
| Q | Command-Q |  | Quit the app. |
|  | Shift-Command-Q | ● | Log out the current user. |
|  | Option-Shift-Command-Q | ● | Log out the current user without confirmation. |
| S | Command-S |  | Save a new document or save a version of a document. |
|  | Shift-Command-S |  | Duplicate the active document or initiate a Save As. |
| T | Command-T |  | Display the Fonts window. |
|  | Option-Command-T |  | Show or hide a toolbar. |
| U | Command-U |  | Underline the selected text or turn underlining on or off. |
| V | Command-V |  | Paste the Clipboard contents at the insertion point. |
|  | Shift-Command-V |  | Paste as (Paste as Quotation, for example). |
|  | Option-Command-V |  | Apply the style of one object to the selection. |
|  | Option-Shift-Command-V |  | Paste the Clipboard contents at the insertion point and apply the style of the surrounding text to the inserted object. |
|  | Control-Command-V |  | Apply formatting settings to the selection. |
| W | Command-W |  | Close the active window. |
|  | Shift-Command-W |  | Close a file and its associated windows. |
|  | Option-Command-W |  | Close all windows in the app. |
| X | Command-X |  | Remove the selection and store on the Clipboard. |
| Z | Command-Z |  | Undo the previous operation. |
|  | Shift-Command-Z |  | Redo (when Undo and Redo are separate commands rather than toggled using Command-Z). |
| Right arrow | Command-Right arrow | ● | Change the keyboard layout to current layout of Roman script. |
|  | Shift-Command-Right arrow | ● | Extend selection to the next semantic unit, typically the end of the current line. |
|  | Shift-Right arrow | ● | Extend selection one character to the right. |
|  | Option-Shift-Right arrow | ● | Extend selection to the end of the current word, then to the end of the next word. |
|  | Control-Right arrow | ● | Move focus to another value or cell within a view, such as a table. |
| Left arrow | Command-Left arrow | ● | Change the keyboard layout to current layout of system script. |
|  | Shift-Command-Left arrow | ● | Extend selection to the previous semantic unit, typically the beginning of the current line. |
|  | Shift-Left arrow | ● | Extend selection one character to the left. |
|  | Option-Shift-Left arrow | ● | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
|  | Control-Left arrow | ● | Move focus to another value or cell within a view, such as a table. |
| Up arrow | Shift-Command-Up arrow | ● | Extend selection upward in the next semantic unit, typically the beginning of the document. |
|  | Shift-Up arrow | ● | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Up arrow | ● | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
|  | Control-Up arrow | ● | Move focus to another value or cell within a view, such as a table. |
| Down arrow | Shift-Command-Down arrow | ● | Extend selection downward in the next semantic unit, typically the end of the document. |
|  | Shift-Down arrow | ● | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Down arrow | ● | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
|  | Control-Down arrow | ● | Move focus to another value or cell within a view, such as a table. |

# **Reserved international keyboard shortcuts**

The system reserves several key combinations for use with localized versions of the system, localized keyboard, keyboard layouts, and input methods. These shortcuts don’t correspond directly to menu commands.

| Keyboard shortcut | Action |
| --- | --- |
| Control-Space | Toggle between the current and last input source. |
| Control-Option-Space | Switch to the next input source in the list. |
| [Modifier key]-Command-Space | Varies. Apple reserved. |
| Command-Right arrow | Change keyboard layout to current layout of Roman script. |
| Command-Left arrow | Change keyboard layout to current layout of system script. |
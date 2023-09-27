# **[components-status] the-menu-bar**

## On a Mac, the menu bar at the top of the screen displays the top-level menus in your app or game, which typically include both system-provided menus and custom ones.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/the-menu-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/the-menu-bar-intro-dark_2x.png)

Mac users are very familiar with the macOS menu bar, and they rely on it to help them learn what an app does and find the commands they need. To help your app or game feel at home in macOS, it’s essential to provide a consistent menu bar experience.

**NOTE**In iPadOS, an app’s keyboard shortcuts can appear in the shortcut interface that displays when people hold the Command key on an attached hardware keyboard. The shortcut interface is similar in appearance and organization to the menu bar in macOS — and it can contain familiar menu items like New Window and Copy — but unlike the menu bar, it doesn’t contain every command an app supports. For guidance, see [Keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/#keyboard-shortcuts).

Menus in the menu bar share most of the appearance and behavior characteristics that all menu types have. To learn about menus in general — and how organize and label menu items — see [Menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus).

# **Anatomy**

The Apple menu, which is always the first item on the leading side of the menu bar, includes system-defined menu items that are always available. You can’t modify or remove the Apple menu.

When present in the menu bar, the following menus appear after the Apple menu in the order listed below.

- *AppName* (you supply a short version of your app’s name for this menu’s title)
- File
- Edit
- Format
- View
- App-specific menus, if any
- Window
- Help

Space permitting, the system can display menu bar extras in the trailing end of the menu bar. A *menu bar extra* provides a menu of app- or system-defined items that people can access in most contexts. With the exception of essential menu bar extras, like Clock, people choose the menu bar extras they want to keep in the menu bar. For example, people might want to include the system-provided Bluetooth menu bar extra to help them manage Bluetooth connections at any time. For guidance, see [Menu bar extras](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#menu-bar-extras).

When menu bar space is constrained, the system prioritizes the display of menus and essential menu bar extras. To ensure that menus remain readable, the system may decrease the space between the titles, truncating them if necessary.

When people enter full-screen mode, the menu bar typically hides until they reveal it by moving the pointer to the top of the screen. For guidance, see [Going full screen](https://developer.apple.com/design/human-interface-guidelines/patterns/going-full-screen).

# **Best practices**

**Enable the system-defined menus and menu items that are relevant in your app.** People generally expect to find familiar menus and menu items in the apps and games they use. In many cases, the system implements the functionality of standard menu items so you don’t have to. For example, when people select text in a standard text field, the system enables the Edit > Copy menu item.

**Prefer using the default ordering of menu bar menus and the default ordering of menu items within each menu.** It’s easier for people to find what they're looking for when your menus and menu items use the ordering they expect.

**Enable the keyboard shortcuts defined for the standard menu items you include.** People expect to use the keyboard shortcuts they already know for standard menu items, like Copy, Cut, Paste, Save, and Print. Define custom keyboard shortcuts only when necessary.

**Prefer short, one-word menu titles.** Various factors — like different display sizes and the presence of menu bar extras — can affect the spacing and appearance of your menus. One-word menu titles work especially well in the menu bar because they take little space and are easy for people to scan. Consider the following guidance as you write a menu title.

- Aim for a title that helps people predict the items within the menu. For example, a menu labeled “Font” implies that it lists items for adjusting text attributes, not for performing edit actions like copy and paste.
- Avoid mixing text with symbols or interface icons in a menu title. Only a menu bar extra uses a symbol or icon as a title.
- Use title-style capitalization if you need to use more than one word in the menu title.

# **App menu**

The app menu lists items that apply to your app or game as a whole, rather than to a specific task, document, or window. To help people quickly identify the active app, the menu bar displays your app name in bold.

The app menu typically contains the following menu items — along with their standard keyboard shortcuts — listed in the following order.

| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| About YourAppName |  | Displays the About window for your app, which includes copyright and version information | Prefer a short name of 16 characters or fewer. Don't include a version number. |
| Settings… | Command-Comma (,) | Opens your Settings window. | Use only for app-level settings. If you also offer document-specific settings, put them in the File menu. |
| Optional app-specific items |  | Performs custom app-level setting or configuration actions | List custom app-configuration items after the Settings item and within the same group. |
| Services |  | Displays a submenu of services from the system and other apps that apply to the current context |  |
| Hide YourAppName | Command-H | Hides your app and all of its windows, and then activates the most recently used app | Use the same short app name you supply for the About item. |
| Hide Others | Option-Command-H | Hides all other open apps and their windows |  |
| Show All |  | Shows all other open apps and their windows behind your app’s windows |  |
| Quit YourAppName | Command-Q | Quits your app. Pressing Option changes Quit YourAppName to Quit and Keep Windows. | Use the same short app name you supply for the About item. |

**Display the About menu item first.** Include a separator after the About menu item so that it appears by itself in a group.

# **File menu**

The File menu contains commands that help people manage the files or documents an app supports. If your app doesn’t handle any types of files, you can rename or eliminate this menu. For example, System Settings doesn’t include a File menu.

The File menu typically contains the following menu items — along with their standard keyboard shortcuts — listed in the following order.

| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| New Item | Command-N | Creates a new document, file, or window | For Item, use a term that names the type of item your app creates. For example, Calendar uses "Event" and "Calendar." |
| Open | Command-O | Can open the selected item or present an interface in which people select an item to open | If people need to select an item in a separate interface, an ellipsis follows the command to indicate that more input is required. |
| Open Recent |  | Displays a submenu that lists recently opened documents and files that people can select, and typically includes a Clear Menuitem | List document and filenames that people recognize in the submenu; don't display file paths. List the documents in the order people last opened them, with the most recently opened document first. |
| Close | Command-W | Closes the current window or document. Pressing Option changes Close to Close All. For a tab-based window, Close Tab replaces Close. | In a tab-based window, consider adding a Close Window item to let people close the entire window with one click or tap. |
| Close Tab | Command-W | Closes the current tab in a tab-based window. Pressing Option changes Close Tab to Close Other Tabs. |  |
| Close File | Shift-Command-W | Closes the current file and all its associated windows | Consider enabling this menu item if your app can open multiple views of the same file. |
| Save | Command-S | Saves the current document or file | Automatically save changes periodically as people work so they don’t need to keep choosing File > Save. For a new document, prompt people for a name and location. If you need to let people save a file in multiple formats, prefer a pop-up menu that lets people choose a format in the Save sheet. |
| Save All |  | Saves all open documents |  |
| Duplicate | Shift-Command-S | Duplicates the current document, leaving both documents open. Pressing Option changes Duplicate to Save As. | Prefer Duplicate to menu items like Save As, Export, Copy To, and Save To because these items don't clarify the relationship between the original file and the new one. |
| Rename… |  | Lets people change the name of the current document |  |
| Move To… |  | Prompts people to choose a new location for the document |  |
| Export As... |  | Prompts people for a name, output location, and export file format. After exporting the file, the current document remains open; the exported file doesn’t open. | Reserve the Export As item for when you need to let people export content in a format your app doesn’t typically handle. |
| Revert to |  | When people enable autosaving, displays a submenu that lists recent document versions and an option to display the version browser. After people choose a version to restore, it replaces the current document. |  |
| Page Setup... | Shift-Command-P | Opens a panel for specifying printing parameters like paper size and printing orientation. A document can save the printing parameters that people specify. | Include the Page Setup item if you need to support printing parameters that apply to a specific document. Parameters that are global in nature, like a printer's name, or that people change frequently, like the number of copies to print, belong in the Print panel. |
| Print... | Command-P | Opens the standard Print panel, which lets people print to a printer, send a fax, or save as a PDF |  |

# **Edit menu**

The Edit menu lets people make changes to content in the current document or text container, and provides commands for interacting with the Clipboard. Because many editing commands apply to any editable content, the Edit menu is useful even in apps that aren’t document-based.

**Determine whether Find menu items belong in the Edit menu.** For example, if your app lets people search for files or other types of objects, Find menu items might be more appropriate in the File menu.

The Edit menu typically contains the following top-level menu items, listed in the following order.

| Menu item             | Keyboard shortcut | Action                                                                                                                                                                          | Guidance                                                                                                                                                                                                                                             |
|-----------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Undo                  | Command-Z         | Reverses the effect of the previous user operation                                                                                                                              | Clarify the target of the undo. For example, if people just selected a menu item, you can append the item's title, such as Undo Paste and Match Style. For a text entry operation, you might append the word *Typing* to give Undo Typing.           |
| Redo                  | Shift–Command-Z   | Reverses the effect of the previous Undo operation                                                                                                                              | Clarify the target of the redo. For example, if people just reversed a menu item selection, you can append the item's title, such as Redo Paste and Match Style. For a text entry operation, you might append the word _Typing_ to give Redo Typing. |
| Cut                   | Command-X         | Removes the selected data and stores it on the Clipboard, replacing the previous contents of the Clipboard                                                                      |                                                                                                                                                                                                                                                      |
| Copy                  | Command-C         | Duplicates the selected data and stores it on the Clipboard                                                                                                                     |                                                                                                                                                                                                                                                      |
| Paste                 | Command-P         | Inserts the contents of the Clipboard at the current insertion point. The Clipboard contents remain unchanged, permitting people to choose Paste multiple times.                |                                                                                                                                                                                                                                                      |
| Paste and Match Style | Command-P         | Inserts the contents of the Clipboard at the current insertion point, matching the style of the inserted text to the surrounding text                                           |                                                                                                                                                                                                                                                      |
| Delete                | Delete            | Removes the selected data, but doesn’t place it on the Clipboard                                                                                                                | Provide a Delete menu item instead of an Erase or Clear menu item. Choosing Delete is the equivalent of pressing the Delete key, so it’s important for the naming to be consistent.                                                                  |
| Select All            | Command-A         | Highlights all selectable content in the current document or text container                                                                                                     |                                                                                                                                                                                                                                                      |
| Find                  | Command-F         | Displays a submenu containing menu items for performing search operations in the current document or text container. Standard submenus (and their keyboard shortcuts) include:  |                                                                                                                                                                                                                                                      |

• Find
• Find and Replace… (Option-Command-F)
• Find Next (Command-G)
• Find Previous (Shift-Command-G)
• Use Selection for Find (Command-E)
• Jump to Selection (Command-J) |  |
| Spelling and Grammar |  | Displays a submenu containing menu items for checking for and correcting spelling and grammar in the current document or text container. Standard submenus (and their keyboard shortcuts) include:
• Show Spelling and Grammar (Command-Colon (:))
• Check Document Now (Command-Semicolon (;))
• Check Spelling While Typing
• Check Grammar With Spelling
• Correct Spelling Automatically |  |
| Substitutions |  | Displays a submenu containing items that let people toggle automatic substitutions while they type in a document or text container. Standard submenus include:
• Show Substitutions
• Smart Copy/Paste
• Smart Quotes
• Smart Dashes
• Smart Links
• Data Detectors
• Text Replacement |  |
| Transformations |  | Displays a submenu containing items that transform selected text. Standard submenus include:
• Make Uppercase
• Make Lowercase
• Capitalize |  |
| Speech |  | Displays a submenu containing Start Speaking and Stop Speaking items, which control when the system audibly reads selected text. |  |
| Start Dictation… | Function Function | Opens the dictation window and converts spoken words into text that’s added at the current insertion point. The system automatically adds the Start Dictation menu item at the bottom of the Edit menu. |  |
| Emoji & Symbols | Control-Command-Space | Displays a Character Viewer, which includes emoji, symbols, and other characters people can insert at the current insertion point. The system automatically adds the Emoji & Symbols menu item at the bottom of the Edit menu. |  |

# **Format menu**

The Format menu lets people adjust text formatting attributes in the current document or text container. You can exclude this menu if your app doesn’t support formatted text editing.

The Format menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Keyboard shortcut | Action                                                                                                                                             | Guidance |
|-----------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Font      |                   | Displays a submenu containing items for adjusting font attributes of the selected text. Standard submenus (and their keyboard shortcuts) include:  |          |

• Show Fonts (Command-T)
• Bold (Command-B)
• Italic (Command-I)
• Underline (Command-U)
• Bigger (Command-Plus sign (+))
• Smaller (Command-Hyphen (-))
• Show Colors (Shift–Command-C)
• Copy Style (Option–Command-C)
• Paste Style (Option–Command-V) |  |
| Text |  | Displays a submenu containing items for adjusting text attributes of the selected text. Standard submenus (and their keyboard shortcuts) include:
• Align Left (Command-Left Brace ({))
• Align Center (Command-Pipe (|))
• Justify
• Align Right (Command-Right Brace (}))
• Writing Direction
• Show Ruler
• Copy Ruler (Control–Command-C)
• Paste Ruler (Control–Command-V) |  |

# **View menu**

The View menu lets people customize the appearance of all an app’s windows, regardless of type.

**IMPORTANT**The View menu doesn’t include items for navigating between or managing specific windows; the [Window menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#window-menu) provides these commands.

**Provide a View menu even if your app supports only a subset of the standard view functions.** For example, if your app doesn’t include a tab bar, toolbar, or sidebar, but does support full-screen mode, provide a View menu that includes only the Enter/Exit Full Screen menu item.

**Ensure that each show/hide item title reflects the current state of the corresponding view.** For example, when the toolbar is hidden, provide a Show Toolbar menu item; when the toolbar is visible, provide a Hide Toolbar menu item.

The View menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| Show/Hide Tab Bar |  | Toggles the visibility of the tab bar above the body area in a tab-based window |  |
| Show All Tabs/Exit Tab Overview |  | Enters and exits a view (similar to Mission Control) that provides an overview of all open tabs in a tab-based window |  |
| Show/Hide Toolbar | Option-Command-T | In a window that includes a toolbar, toggles the toolbar’s visibility. |  |
| Customize Toolbar… |  | In a window that includes a toolbar, opens a view that lets people customize toolbar items |  |
| Show/Hide Sidebar | Control-Command-S | In a window that includes a sidebar, toggles the sidebar’s visibility. |  |
| Enter/Exit Full Screen | Function-F | In an app that supports a full-screen experience, opens the window at full-screen size in a new space |  |

# **App-specific menus**

Your app’s custom menus appear in the menu bar between the View menu and the Window menu. For example, Safari’s menu bar includes app-specific History and Bookmarks menus.

**Provide app-specific menus for custom commands.** People look in the menu bar when searching for app-specific commands, especially when using an app for the first time. Even when commands are available elsewhere in your app, it’s important to list them in the menu bar. Putting commands in the menu bar makes them easier for people to find, lets you assign keyboard shortcuts to them, and makes them more accessible to people using Full Keyboard Access. Excluding commands from the menu bar — even infrequently used or advanced commands — risks making them difficult for everyone to find.

**As much as possible, reflect your app’s hierarchy in app-specific menus.** For example, Mail lists the Mailbox, Message, and Format menus in an order that mirrors the relationships of these items: mailboxes contain messages, and messages contain formatting.

**In general, list universally applicable menus first and more focused menus last.** Place universal menus closer to the Apple menu; place focused menus closer to the Help menu.

# **Window menu**

The Window menu lets people navigate, organize, and manage an app’s windows.

**IMPORTANT**The Window menu doesn’t help people customize the appearance of windows or close them. To customize a window, people use commands in the [View menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#view-menu); to close a window, people choose Close in the [File menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#file-menu).

**Provide a Window menu even if your app has only one window.** Include the Minimize and Zoom menu items so people using Full Keyboard Access can use the keyboard to invoke these functions.

**Consider including menu items for showing and hiding panels.** A [panel](https://developer.apple.com/design/human-interface-guidelines/macos/windows-and-views/panels/)provides information, configuration options, or tools for interacting with content in a primary window, and typically appears only when people need it. There’s no need to provide access to the font panel or text color panel because the Format menu lists these panels.

The Window menu typically contains the following top-level menu items, listed in the following order.

| Menu item                             | Keyboard shortcut | Action                                                                                                                                                                                                                                                                                                          | Guidance                                                                                                                                                     |
|---------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimize                              | Command-M         | Minimizes the active window to the Dock. Pressing the Option key changes this item to Minimize All.                                                                                                                                                                                                             |                                                                                                                                                              |
| Zoom                                  |                   | Toggles between a predefined size appropriate to the window’s content and the window size people set. Pressing the Option key changes this item to Zoom All.                                                                                                                                                    | Avoid using Zoom to enter or exit full-screen mode. The View menuenables these functions.                                                                    |
| Show Previous Tab                     | Control-Shift-Tab | Shows the tab before the current tab in a tab-based window                                                                                                                                                                                                                                                      |                                                                                                                                                              |
| Show Next Tab                         | Control-Tab       | Shows the tab after the current tab in a tab-based window                                                                                                                                                                                                                                                       |                                                                                                                                                              |
| Move Tab to New Window                |                   | Opens the current tab in a new window                                                                                                                                                                                                                                                                           |                                                                                                                                                              |
| Merge All Windows                     |                   | Combines all open windows into a single tabbed window                                                                                                                                                                                                                                                           |                                                                                                                                                              |
| Enter/Exit Full Screen                | Control-Command-F | In an app that supports a full-screen experience, opens the window at full-screen size in a new space                                                                                                                                                                                                           | Include this item in the Window menu only if your app doesn't have a View menu. In this scenario, continue to provide separate Minimize and Zoom menu items. |
| Bring All to Front                    |                   | Brings all an app's open windows to the front, maintaining their onscreen location, size, and layering order. (Clicking the app icon in the Dock has the same effect.) Pressing the Option key changes this item to Arrange in Front, which brings an app's windows to the front in a neatly tiled arrangement. |                                                                                                                                                              |
| *Name of an open app-specific window* |                   | Brings the selected window to the front.                                                                                                                                                                                                                                                                        | List the currently open windows in alphabetical order for easy scanning. Avoid listing panels or other modal views.                                          |

# **Help menu**

The Help menu — located at the trailing end of the menu bar — provides access to an app’s help documentation. When you use the Help Book format for this documentation, macOS automatically includes a search field at the top of the Help menu.

| Menu item | Keyboard shortcut | Action | Guidance |
| --- | --- | --- | --- |
| Send YourAppNameFeedback to Apple |  | Opens the Feedback Assistant, in which people can provide feedback. |  |
| YourAppNameHelp |  | When the content uses the Help Book format, opens the content in the built-in Help Viewer. |  |
| Additional Item |  |  | Use a separator between your primary help documentation and additional items, which might include registration information or release notes. Keep the total the number of items you list in the Help menu small to avoid overwhelming people with too many choices when they need help. Alternatively, consider linking to additional items from within your help documentation. |

For guidance, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/patterns/offering-help); for developer guidance, see [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager).

# **Dynamic menu items**

In rare cases, it can make sense to present a *dynamic menu item*, which is a menu item that changes its behavior when people choose it while pressing a modifier key (Control, Option, Shift, or Command). For example, the *Minimize*item in the Window menu changes to *Minimize All* when people press the Option key.

**Avoid making a dynamic menu item the only way to accomplish a task.**Dynamic menu items are hidden by default, so they’re best suited to offer shortcuts to advanced actions that people can accomplish in other ways. For example, if someone hasn’t discovered the *Minimize All* dynamic menu item in the Window menu, they can still minimize each open window.

**Use dynamic menu items primarily in menu bar menus.** Adding a dynamic menu item to contextual or Dock menus can make the item even harder for people to discover.

**Require only a single modifier key to reveal a dynamic menu item.** It can be physically awkward to press more than one key while simultaneously opening a menu and choosing a menu item, in addition to reducing the discoverability of the dynamic behavior. For developer guidance, see the [isAlternate](https://developer.apple.com/documentation/appkit/nsmenuitem/1514823-isalternate) property of [NSMenuItem](https://developer.apple.com/documentation/appkit/nsmenuitem).

**TIP**macOS automatically sets the width of a menu to hold the widest item, including dynamic menu items.

# **Menu bar extras**

A menu bar extra exposes app-specific functionality using an icon that appears in the menu bar when your app is running, even when it’s not the frontmost app. Menu bar extras are on the opposite side of the menu bar from your app's menus.

When necessary, the system hides menu bar extras to make room for app menus. Similarly, if there are too many menu bar extras, the system may hide some to avoid crowding app menus.

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/images/menu-bar-extras_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/images/menu-bar-extras_2x.png)

**Consider using a symbol to represent your menu bar extra.** You can create an [interface icon](https://developer.apple.com/design/human-interface-guidelines/foundations/icons) or you can choose a [symbol](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) from the SF Symbols app, using it as-is or customizing it to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image so it looks good on both dark and light menu bars, and when your menu bar extra is selected.

**Display a menu — not a popover — when people click your menu bar extra.** Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [popover](https://developer.apple.com/design/human-interface-guidelines/components/presentation/popovers).

**Let people — not your app — decide whether to enable your menu bar extra.** Typically, people add a menu bar extra to the menu bar by changing a setting in an app’s settings window. To ensure discoverability, however, consider giving people the option of enabling the menu bar extra during setup.

**Avoid relying on the presence of menu bar extras.** The system hides and shows menu bar extras regularly, and you can’t be sure which other menu bar extras people have chosen to display or predict the location of your menu bar extra.

**Consider exposing app-specific functionality in other ways, too.** For example, you can provide a [Dock menu](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/dock-menus) that appears when people Control-click your app’s Dock icon. People can hide or choose not to use your menu bar extra, but a Dock menu is aways available when your app is running.

# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*
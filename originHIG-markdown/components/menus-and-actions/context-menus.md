# **[components-menus-and-actions] context-menus**

## A context menu provides access to functionality that’s directly related to an onscreen item, without cluttering the interface.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/context-menu-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/context-menu-intro-dark_2x.png)

Although a context menu provides convenient access to frequently used items, it’s hidden by default, so people might not know it’s there. To reveal a context menu, people generally choose a view or select some content and then perform an action, using the input modes their current configuration supports. For example:

- The system-defined long press gesture in iOS and iPadOS
- Pressing the Control key while clicking a pointing device in macOS and iPadOS
- Using a secondary click on a Magic Trackpad in macOS or iPadOS

# **Best practices**

**Prioritize relevancy when choosing items to include in a context menu.**A context menu isn’t for providing advanced or rarely used items; instead, it helps people quickly access the commands they’re most likely to need in their current context. For example, the context menu for a Mail message in the inbox includes commands for replying and moving the message, but not commands for editing message content, managing mailboxes, or filtering messages.

**Aim for a small number of menu items.** A context menu that’s too long can be difficult to scan and scroll.

**Enable context menus consistently throughout your app.** If you provide context menus for items in some places but not in others, people won’t know where they can use the feature and may think there’s a problem.

**Always make context menu items available in the main interface, too.**For example, in Mail in iOS and iPadOS, the context menu items that are available for a message in the inbox are also available in the toolbar of the message view. In macOS, an app’s menu bar menus list all the app’s commands, including those in various context menus.

**If you need to use submenus to manage a menu’s complexity, keep them to one level.** A submenu is a menu item that reveals a secondary menu of logically related commands. Although submenus can shorten a context menu and clarify its commands, more than one level of submenu complicates the experience and can be difficult for people to navigate. If you need to include a submenu, give it an intuitive title that helps people predict its contents without opening it.

**Aim to place the most frequently used menu items where people are likely to focus first.** When a context menu opens, people often read it starting from the part that’s closest to where their finger or pointer revealed it. Depending on the onscreen location of the selected content, a context menu might open above or below that area of the screen, so you might also need to reverse the order of items to match the position of the menu.

**Show keyboard shortcuts in you app’s main menus, not in context menus.** Context menus already provide a shortcut to task-specific commands, so it's redundant to display keyboard shortcuts too.

**Follow best practices for using separators.** As with other types of menus, you can use separators to group items in a context menu and help people scan the menu more quickly. In general, you don’t want more than about three groups in a context menu. For guidance, see [Menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus).

# **Content**

In most cases, a context menu doesn’t display a title, but as with all other menus, each item in a context menu displays a short label that describes what it does. For guidance, see [Menus > Labels](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus/#labels).

# **Platform considerations**

*Not supported in tvOS or watchOS.*

# **iOS, iPadOS**

**In general, avoid adding a title to a context menu.** The exception is if a context menu targets content that might not be clear. For example, when people select multiple Mail messages and tap the Mark toolbar button, the resulting context menu displays a title that states the number of selected messages, reminding people that the command they choose affects all the messages they selected.

**Include a symbol or interface icon with each command in a context menu.** A symbol or icon reinforces the meaning of a command, helping people instantly understand its function. In cases where there are multiple commands that need to use the same symbol, consider omitting all symbols to avoid repeating them.

**Provide either a context menu or an edit menu for an item, but not both.** If you enable both features for the same item, it can be confusing to people — and difficult for the system to detect their intent. See [Edit menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/edit-menus).

**Warn people about context menu items that can destroy data.** If you need to include potentially destructive items in your context menu — such as Delete or Remove — list them at the end of the menu and identify them as destructive (for developer guidance, see [destructive](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/3335200-destructive)). The system can display a destructive menu item using a red text color.

**In iPadOS, consider using a context menu to let people create a new object in your app.** iPadOS lets you reveal a context menu when people perform a long press on the touchscreen or use a secondary click with an attached trackpad or keyboard. For example, Files lets people create a new folder by revealing a context menu in an area between existing files and folders.

In iOS and iPadOS, a context menu can display a preview of the current content near the list of commands. People can choose a command in the menu or — in some cases — they can tap the preview to open it or drag it to another area.

**Prefer a graphical preview that clarifies the target of a context menu’s commands.** For example, when people reveal a context menu on a list item in Notes or Mail, the preview shows a condensed version of the actual content to help people confirm that they're working with the item they intend.

**Ensure that your preview looks good as it animates.** As people reveal a context menu on an onscreen object, the system animates the preview image as it emerges from the content, dimming the screen behind the preview and the menu. It’s important to adjust the preview’s clipping path to match the shape of the preview image so that its contours, such as the rounded corners, don’t appear to change during animation. For developer guidance, see [UIContextMenuInteractionDelegate](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate).

# **macOS**

On a Mac, a context menu is sometimes called a *contextual* menu.

# **watchOS**

In versions of watchOS before watchOS 7, people could press firmly on the display to open a hidden menu of actions relevant to the current screen. In watchOS 7 and later, watchOS apps elevate important items out of such menus and into the relevant screen or a settings screen.
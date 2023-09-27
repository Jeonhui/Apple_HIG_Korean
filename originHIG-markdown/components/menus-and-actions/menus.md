# **[components-menus-and-actions] menus**

## A menu reveals its options when people interact with it, making it a space-efficient way to present commands in your app or game.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/menus-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/menus-intro-dark_2x.png)

Menus are ubiquitous throughout the interface, so most people already know how to use them. When you use menus consistently in your app or game, it can help make your experience feel familiar and easy to learn.

The system provides several types of menus that support different use cases, such as:

- A button — like a [pop-up button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pop-up-buttons) or [pull-down button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pull-down-buttons) — that reveals a menu of options directly relating to its action
- A hidden [context menu](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/context-menus) that people can reveal to access to a small number of frequently used actions relevant to their current view or task
- A macOS app’s [menu bar](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar) menus that contain all the commands people can perform in the app

Regardless of type, all menus list one or more *menu items*, each of which represents a command, option, or state that affects the current selection or context. When people choose a menu item, the action occurs and the menu typically closes.

# **Labels**

Each menu item displays text to describe its action and may include a symbol or interface icon to clarify meaning. In addition to text and symbols, a menu item can also display the characters people type to perform the associated keyboard shortcut, if there is one. Unlike most other types of menus, a context menu doesn’t display keyboard shortcuts because it already provides a quick way to get task-specific actions.

**NOTE**Depending on menu layout, an iOS or iPadOS app can display a few unlabeled menu items that use only symbols or icons to identify them. For guidance, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus#ios-ipados).

**To help people understand what a menu item does, write a label that clearly and succinctly describes it.** Depending on the item you’re describing, consider the following guidance:

- To label a menu item that initiates an action, use a verb or verb phrase that describes the action, such as *Copy*, *Share App*, or *Close*.
- When describing the status of a menu item that toggles between attributes or states, indicate its current state. For example, you might use a pair of labels for a menu item that shows or hides something, like *Show Completed* and *Hide Completed*, or you might display a checkmark next to the label to show that the state or attribute is in effect, such as *Organize by Conversation*.

**For consistent labels, adopt a condensed style that doesn't include articles, and use title-style capitalization.** In English, the articles *a*, *an*, and *the* always lengthen labels, but rarely enhance understanding. For example, when people want to open a message in Mail, they understand that the *Open Message* menu item refers to the currently selected message, so adding an article to the label — such as *Open the Message* — doesn't help clarify the item's action.

**Append an ellipsis to a menu item’s label when people need to provide additional information before the action can complete.** The ellipsis character (…) signals that another view will open in which people can input information or make choices.

**Show people when a menu item is unavailable.** An unavailable menu item often appears dimmed and doesn’t respond to interactions. If all of a menu’s items are unavailable, ensure that the menu itself remains enabled so people can open it and learn about the commands it contains.

# **Toggled items**

When you need to help people switch an item or attribute between two states, you can support toggling in one of the following three ways:

- A single menu item that displays a label that can change depending on the current state, such as *Show Ruler* and *Hide Ruler*. The parent menu never lists more than one label at a time.
- A single menu item that has a checkmark next to it when it’s turned on; for example, a text attribute like *Bold*. The parent menu always lists the item, displaying or removing the checkmark according to the current state.
- A pair of menu items, each of which has a label that describes one of two opposing actions or states; for example, *Grid On* and *Grid Off*. The parent menu always lists both menu items, but only the menu item that’s currently in effect displays a checkmark or appears selected (usually dimmed).

**Consider using changeable titles to shorten a long list of items that show and hide features.** For example, the View menu in Mail uses changeable titles to Show or Hide the Tab Bar, Mailbox List, Toolbar, or Favorites Bar.

**Use a changeable label when there isn't enough room to list a pair of menu items.** When necessary to make sure both titles are unambiguous, consider using two verbs that clearly express opposite actions, like *Turn Grid On* and *Turn Grid Off*.

**Consider using a checkmark when a toggled item represents an attribute that’s currently in effect.** It’s easy for people to scan for checkmarks in a list of attributes to find the ones that are in effect. For example, in the standard Format > Font menu, checkmarks can make it easy for people notice the styles that apply to selected text.

**Consider offering a menu item that makes it easy to remove multiple toggled attributes.** For example, if you let people apply several styles to selected text, it can work well to provide a menu item — such as *Plain* — that removes all applied formatting attributes at one time.

**Consider displaying a pair of menu items instead of one toggled menu item if it adds clarity.** Sometimes, it helps people to view both actions or states at the same time. The Mailbox menu in Mail, for example, includes both the *Take All Accounts Online* and *Take All Accounts Offline* items, so when someone's accounts are online, only the *Take All Accounts Offline* menu item appears enabled.

# **Organization**

To help people find the item they’re looking for, you can organize menu items according to frequency of use, object importance, functional categories, or another prioritization scheme that fits the way people use your app.

Sometimes, it makes sense to group logically related items within a menu, such as the editing commands *Copy*, *Cut*, and *Paste*. To help people visually distinguish groups, you use a separator. Depending on the platform and type of menu, a *separator* appears between groups as a horizontal line or a short gap in the menu’s background appearance.

**List menu items according to your prioritization scheme.** People tend to start scanning a menu from the top, so listing high-priority items and groups first often means that people can find what they want without scanning the entire menu.

**Avoid letting your prioritization scheme separate a group of commands that are logically related, even if the commands don’t all have the same priority.** For example, people generally use Paste and Match Style much less often than they use Paste, but they expect to find both commands in the same group that contains other related editing actions like Copy and Cut.

**Be mindful of menu length.** People need more time and attention to read a long menu, which means they may miss the command they want. If a menu is long, you might need to break it into separate menus. In some cases, you can use a submenu to shorten the list. The exception is a menu that contains user-defined or dynamically generated content, such as the History and Bookmarks menus in Safari. In this situation, people expect the menu to accommodate the items they add to it, so a long menu is fine, and scrolling is acceptable.

# **Submenus**

Sometimes, a menu item can reveal a set of closely related items in a subordinate list called a *submenu*. In this case, a menu item indicates the presence of a submenu by displaying a symbol — like a chevron — after its label.

**Use submenus sparingly.** Each submenu adds complexity to the interface and hides the items it contains. You might consider creating a submenu when a term appears in more than two menu items in the same group. For example, instead of offering separate menu items for *Sort by Date*, *Sort by Subject*, and *Sort by Unread*, the View menu in Mail includes a Sort By submenu that contains items like *Date*, *Subject*, and *Unread*. In a case like this, it generally works well to use the repeated term in the submenu label to help people predict what it contains.

**Limit the depth and length of submenus.** It can be difficult for people to reveal multiple levels of hierarchical submenus, so it’s generally best to restrict them to a single level. Also, if a submenu contains more than about five items, consider creating a new menu.

**Keep a submenu enabled even when its nested menu items are unavailable.** A submenu item — like all menu items — needs to let people open it and learn about the commands it contains.

**Prefer using a submenu to indenting menu items.** Using indentation is inconsistent with the system and doesn’t clearly express the relationships between the menu items.

# **Platform considerations**

*No additional considerations for macOS, tvOS, or watchOS.*

# **iOS, iPadOS**

Beginning in iOS 16 and iPadOS 16, a menu can display items in one of the following three layouts.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus/images/small-medium-large-menu-layouts-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus/images/small-medium-large-menu-layouts-dark_2x.png)

- **Small.** A row of four items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon, but no label.
- **Medium.** A row of three items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon above a short label.
- **Large (the default).** The menu displays all items in a list.

For developer guidance, see [preferredElementSize](https://developer.apple.com/documentation/uikit/uimenu/4013313-preferredelementsize?language=objc).

**Choose a small or medium menu layout when it can help streamline people’s choices.** Consider using the medium layout if your app has three important actions that people often want to perform. For example, Notes uses the medium layout to give people a quick way to perform the Scan, Lock, and Pin actions. Use the small layout only for closely related actions that typically appear as a group, such as Bold, Italic, Underline, and Strikethrough. For each action, use a recognizable symbol that helps people identify the action without a label.
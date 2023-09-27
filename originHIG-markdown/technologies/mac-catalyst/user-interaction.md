# **[technologies-mac-catalyst] user-interaction**

Both iPad and Mac accept user input from a range of devices — such as the Multi-Touch display, keyboard, mouse, and trackpad. Typically, touch interactions inform iOS conventions, whereas keyboard and mouse interactions inform macOS conventions. When you create your Mac app with Mac Catalyst, first review differences between user interactions on iPad and Mac. Then, think about how users interact with your Mac app and make changes to follow macOS conventions.

For example, Mac users typically use a two-step process to interact with content and controls: they first select an object and then perform an action on it. Because time passes between these steps, the object’s selected state must persist until people finish choosing the action. Mac users expect this behavior — referred to as *selection persistence* — regardless of the input device they use.

On the other hand, iPad users can perform actions either through gestures — which rarely depend on selection persistence — or by using a keyboard, mouse, or trackpad.

Here are some other examples that show how per-platform conventions can affect the user experience:

- Mac users appreciate Next and Previous buttons in place of iPad or trackpad gestures such as swiping among pages, especially if they use a mouse.
- Mac users expect to use the Delete key or choose a Delete command in a menu, so displaying a Delete button in the UI is usually unnecessary.
- Mac users expect a menu command or a button in a toolbar to load new content, while iPad users are accustomed to pulling down on a view to refresh its contents.

As you translate iOS user interactions to Mac interactions, focus on letting people manipulate objects in ways that adhere to platform conventions. Take advantage of the fact that Mac users can easily use the keyboard and the mouse or trackpad at the same time. For example, let people select multiple cells in a collection view, change a persistent selection by using arrow keys or by pressing letter and number keys, or use keyboard shortcuts.

# **App menus**

On a Mac, the menu bar at the top of the screen gives people a consistent location for commands that control both apps and the system. The menu bar contains the current app’s standard and custom menus, in addition to the Apple menu, which lists system-level commands that are always available. Mac users expect every Mac app to make most commands available in the menu bar. Because iOS apps use controls to display commands in the main UI, finding a logical and intuitive menu bar location for every app command is a key part of the adaptation process.

![https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/mac-catalyst-app-menu_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/mac-catalyst-app-menu_2x.png)

To design the menu bar menus for the Mac version of your app, start by listing all actions that people can perform and grouping them into the categories defined by the standard menu bar menus.

**NOTE**Most Mac apps include a View menu and a Window menu. Although these menus may seem similar, they have different purposes. People use the View menu to customize the appearance of app windows and to move among different functional areas, whereas they use the Window menu to navigate, organize, and manage the collection of windows in an app. For guidance, see [The menu bar](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/).

If some actions on your list don’t make sense in the standard menu bar menus, you might need to add a custom menu. Mac apps often add a custom menu bar menu for commands that are associated with either a core app object or a core app workflow. For example, Mail in macOS uses the Message and Mailbox menus to list commands that operate on these fundamental app objects. In contrast, Keynote uses the Arrange menu to list commands associated with the core workflow of arranging objects in a slide deck.

After you group your app’s actions into menus, order the items in each menu in a way that makes sense. Each standard menu defines a recommended order for items, so it’s important to follow this order for the items that you support. For example, Mac users expect the File menu to present items in this order:

- New...
- Open...
- Open Recent
- Close

In a custom menu bar menu, order the items according to importance, frequency of use, or another scheme that makes sense in your app. Menu bar menus can also contain submenus and separators that help group items in logical ways. For guidance, see [Menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus).

**DEVELOPER NOTE**To add and remove custom menus, use [UIMenuBuilder](https://developer.apple.com/documentation/uikit/uimenubuilder) and add menu items that represent your iOS app’s commands as menu items with [UICommand](https://developer.apple.com/documentation/uikit/uicommand).

# **Keyboard input**

Mac users expect apps to support macOS keyboard conventions like keyboard shortcuts for common commands, and each key command usually comes with a corresponding men item in the menu bar.

**Allow users to navigate your Mac app using the keyboard.** For example, map each major view area, such as each tab, to the keyboard shortcuts ⌘1, ⌘2, and so on. Then, add the key commands the View menu.

**DEVELOPER NOTE**To add menu items that support keyboard shortcuts for commands, use [UIKeyCommand](https://developer.apple.com/documentation/uikit/uikeycommand). For developer guidance, see [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/uicommand/adding_menus_and_shortcuts_to_the_menu_bar_and_user_interface).

**Support keyboard shortcuts for all common commands in your menus.** Both Mac users and iPad users who use keyboards can benefit from this change; for example:

- Allow users who use keyboards to undo a previous action with a keyboard shortcut and a corresponding menu item instead of displaying an Undo button in the UI of your Mac app.
- Remove the Delete button from the macOS version of your app and let people use the Delete key or the app’s Edit > Delete menu command instead.

For guidance, see [Custom keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#custom-keyboard-shortcuts).

For developer guidance, see [Accessing actions using menu elements](https://developer.apple.com/tutorials/mac-catalyst/accessing-actions-using-menu-elements) and [Take advantage of the delete menu element](https://developer.apple.com/tutorials/mac-catalyst/accessing-actions-using-menu-elements#Take-Advantage-of-the-Delete-Menu-Element).

# **Help**

iOS apps usually offer help by directing users to an information section in the app or a website, whereas Mac users expect apps to offer onscreen help documentation through the Help menu bar menu. For guidance, see [Help menu](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#custom-keyboard-shortcuts) and [Offering help](https://developer.apple.com/design/human-interface-guidelines/patterns/offering-help).

# **Contextual menus**

Contextual menus help people discover actions they can perform on an object without opening a menu bar menu. If you support [context menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/context-menus) in your iOS app, the system automatically converts them to contextual menus in the macOS version of your app.

To give Mac users the best experience, look for additional places to support contextual menus. For example, if there are common actions that people can perform on an object in your app, add a contextual menu that lists these actions. You can also add a contextual menu to a view that represents an object — for example, folder objects in the Finder support contextual menus that offer actions like Open in New Tab, Rename, and Duplicate.

In iOS 14 and later, a button can display a pull-down menu, or simply *menu*, that lists items or actions people can choose. When you create a Mac app with Mac Catalyst, a menu automatically becomes a macOS menu. For guidance, see [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pull-down-buttons).

# **Gestures**

Most iOS gestures convert automatically when you create your Mac app with Mac Catalyst; for example:

| iOS gesture... | Translates to mouse interaction |
| --- | --- |
| Tap | Left or right click |
| Touch and hold | Click and hold |
| Pan | Left click and drag |

| iOS gesture... | Translates to trackpad gesture |
| --- | --- |
| Tap | Click |
| Touch and hold | Click and hold |
| Pan | Click and drag |
| Pinch | Pinch |
| Rotate | Rotate |

As a concrete example, consider an iOS app that allows people to tap an object and drag it around. In macOS, people might click and hold the object and then drag it around. As a general rule, try to use standard controls and views in your Mac app, because they automatically respond to most standard clicks and gestures. Avoid redefining systemwide inter-app gestures, and define custom gestures cautiously. Additionally, don’t rely on the availability of specific devices and gestures, because not everyone has a mouse or trackpad. People may also disable and redefine gestures without your knowledge. For guidance, see [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices).

**DEVELOPER NOTE**The two touches in the pinch and rotate gestures get sent to the view under the pointer, not the view under each touch.
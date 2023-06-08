# **[components-menus-and-actions] dock-menus**

## On a Mac, people can secondary click an app’s or game’s icon in the Dock to reveal a Dock menu, which presents both system-provided and custom items.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/dock-menu-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/dock-menu-intro-dark_2x.png)

The system-provided Dock menu items can vary depending on whether the app is open. For example, the Dock menu for Safari includes menu items for actions like viewing a current window or creating a new window.

# **Best practices**

As with all menus, you need to label Dock menu items succinctly and organize them logically. For guidance, see [Menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus).

**Make custom Dock menu items available elsewhere too.** Because the Dock menu is hidden by default, people might not know it’s there. Be sure to list the same commands in your menu bar menus or within your interface.

**Prefer high-value custom items for your Dock menu.** For example, a Dock menu can list all currently or recently open windows, making it a convenient way to jump to the window people want. Also consider listing a few of the actions that are most likely to be useful when your app isn’t frontmost or when there are no open windows. For example, Mail includes items for getting new mail and composing a new message in addition to listing all open windows.

**Place custom menu items above the system-provided ones.** People expect to find the system-provided items at the bottom of the Dock menu.

# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*

# **iOS, iPadOS**

Although iOS and iPadOS don’t support a Dock menu, people can reveal a similar menu of system-provided and custom items — called Home Screen quick actions — when they long press an app icon on the Home Screen or in the Dock. For guidance, see [Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions).
# **[patterns] settings**

# People expect apps and games to just work, but they also appreciate having ways to customize the experience to fit their needs.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-settings-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-settings-intro-dark_2x.png)

When it makes sense, you can offer context-specific settings within your app or game so people don’t have to leave their current task to make adjustments. If you also offer settings that affect the overall app or game, you can provide a custom settings area. In iOS, iPadOS, macOS, and tvOS, the system provides a Settings app that can include some app-specific options.

# **Best practices**

**As much as possible, let people modify task-specific options without going to a settings area.** For example, if your app lets people adjust things like showing or hiding parts of the interface, reordering a collection of items, or filtering a list, make these options available in the screens they affect, where they’re discoverable and convenient. Putting this type of option in a separate settings area disconnects it from its context, requiring people to suspend their task to make adjustments, and often hiding the results until people resume the task.

**When necessary, put app-level options in a separate settings area.** People don’t tend to visit an app’s settings area very often, so it’s important to include only rarely-changed options that affect the experience as a whole, such as overall interface style or alternative app icons.

**Minimize the number of settings you offer.** Although people appreciate having control over an app, they also appreciate being able to benefit from the experience without first doing a lot of setup. Too many settings can make an app feel less approachable, while also making it hard to find a particular setting.

**Respect people’s systemwide settings and avoid including redundant versions of them in your app-specific settings area.** People expect to use the system-provided settings apps to manage global options like accessibility accommodations, scrolling behavior, and authentication methods, and they expect all apps to adhere to their choices. Offering app-specific settings that include custom versions of global options is inconsistent and confusing in at least two ways: First, it implies that systemwide settings may not apply to the current app and second, that changing one of the app’s custom settings can affect other apps too.

**Avoid using in-app settings to ask for setup information you can get in other ways.** For example, instead of asking someone to enter a zip code so you can present local options, ask permission to use their current location. For guidance, see [Accessing private data](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data).

**Add only the most rarely changed options to the system-provided settings apps.** On each platform, the system includes an app that lets people adjust things like the overall appearance of the system, network connections, account details, accessibility requirements, and language and region settings. Although both the Settings app (in iOS, iPadOS, and tvOS) and the System Settings app (in macOS) can also contain app-specific settings, people must switch away from their current context to adjust those settings. If you must offer app-specific settings in the system settings apps, consider providing a button that opens them directly from your app.

**Make your in-app settings easy to find, but not too prominent.** For example, consider making settings available within a profile or account view. In a watchOS app, you could make a very small number of essential options available at the bottom of the main view.

**In macOS and iPadOS apps, make settings available in ways people expect.** For example, people appreciate being able to use the standard Command-Comma (,) keyboard shortcut to open app-level settings. In an app that runs on a Mac, include an app-level settings item in the [App menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#app-menu) and, if you provide document-level options, add this item to the [File menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#file-menu). Avoid adding settings buttons to a macOS app’s toolbar, because doing so decreases the space available for essential commands that people use frequently.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, or tvOS.*

# **macOS**

An app-specific window opens when people choose the Settings item in the App menu. Typically, an app-specific settings window contains a toolbar that includes buttons for switching between views — called *panes* — that each contain a group of related settings.

**Disable a settings window’s minimize and maximize buttons.** It’s quick to open a settings window using the standard Command–Comma (,) keyboard shortcut, so there’s no need to keep the window in the Dock, and because a settings window accommodates the size of the current pane, people don’t need to expand the window to see more.

**Provide a noncustomizable toolbar that remains visible and always indicates the active toolbar button.** A settings window’s toolbar identifies the areas people can customize and enables navigation among those areas. People rely on a stable settings interface to help them find what they need.

**Update the window's title to reflect the currently visible pane.** If your settings window doesn’t have multiple panes, use the title *App Name* Settings.

**Restore the most recently viewed pane.** People often adjust related settings more than once, so it can be convenient when a settings window opens to the last pane people used.

# **watchOS**

Avoid supplying app-specific settings to include in the watchOS Settings app.
# **[technologies-mac-catalyst] visual-design**

To help the Mac version of your app look great, address platform differences in the following areas of visual design.

# **Layout**

Mac users expect to resize app windows to just about any size, from full screen to as small as the app permits. To support this type of infinite resizability — and to take advantage of the wider Mac display — use the regular-width and regular-height size classes and consider reflowing elements in your window’s content area to a side-by-side arrangement when necessary.

**As much as possible, adopt a top-down user flow.** Mac apps place the most important actions and content near the top of the window. If your iOS app provides controls in a toolbar or navigation bar, put these controls in the window toolbar of the macOS version of your app.

**Consider moving controls from the main UI of your iPad app to your Mac app’s toolbar.**Additionally, list the commands associated with these controls in the menus of your macOS app’s menu bar.

**NOTE**In macOS, a toolbar button is always visible, but the current context might make it unavailable; in iOS, a toolbar button is always available, but the current context might remove it from the toolbar. For example, if your iOS app includes a toolbar button that works in only one tab, the macOS version displays the button as unavailable in all other tabs.

**Relocate buttons from the left or right edge of the screen.** On iPad, placing buttons on the middle-left or middle-right screen edges can help people reach them, but on a Mac, this ergonomic consideration doesn’t apply. You may want to relocate controls to the top or bottom edge of the content area or put them in the toolbar of your macOS window.

# **Color**

**Use the system’s accent color on both platforms.** iOS apps define the colors used to tint buttons and to indicate selection. In contrast, Mac users expect apps to use the accent color they chose in System Settings.

The [dynamic system colors](https://developer.apple.com/design/human-interface-guidelines/foundations/color#ios-ipados) designed for iOS backgrounds automatically map to appropriate macOS equivalents, as shown below.

| iOS color | Equivalent macOS color |
| --- | --- |
| https://developer.apple.com/documentation/uikit/uicolor/3173140-systembackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173137-secondarysystembackground | https://developer.apple.com/documentation/appkit/nscolor/1528630-windowbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173154-tertiarysystembackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor (overlaid with https://developer.apple.com/documentation/appkit/nscolor/1534635-quaternarylabelcolor) |
| https://developer.apple.com/documentation/uikit/uicolor/3173145-systemgroupedbackground | https://developer.apple.com/documentation/appkit/nscolor/1528630-windowbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173138-secondarysystemgroupedbackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173155-tertiarysystemgroupedbackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor (overlaid with https://developer.apple.com/documentation/appkit/nscolor/1534635-quaternarylabelcolor) |

Other semantically defined iOS colors — such as the and the label and separator colors — map to similarly named macOS colors. For guidance, see [macOS](https://developer.apple.com/design/human-interface-guidelines/foundations/color#macos).

**Don’t tint buttons in table rows.** In your iOS app, you use a tint to show that buttons in table rows are active, but in macOS, tinted buttons in table rows look out of place.

# **Typography**

With the iPad idiom, the system automatically scales text to achieve good results without requiring you to specify different font values on each platform. However, you might not get the best results in every situation.

**Make sure small type is legible on the Mac.** Be prepared to increase some of the smallest font sizes you use in your iOS app so that all text remains legible in the macOS version. Also, note that macOS doesn’t support Dynamic Type.

**If you adopt the Mac idiom, adjust your text’s font size.** With the iPad idiom, the system scales text to 77% of its size. For example, the system scales text that uses the iOS baseline font size of 17pt down to 13pt in macOS. With the Mac idiom, text renders at 100% of its configured size, which can appear too large without adjustment. When possible, use text styles and avoid fixed font sizes. For guidance, see [Adopting the Mac idiom](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/mac-idiom).

# **Custom icons and glyphs**

**Create a macOS version of your app icon.** Great macOS app icons showcase the lifelike rendering style that people expect in macOS while presenting a harmonious user experience across all platforms. For guidance, see [App icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

**Prefer using symbols offered by SF symbols.** SF Symbols provides a set of consistent, highly configurable symbols you can use to offer consistent iconography across platforms. You can also create your own custom symbol images to use in your iOS and macOS apps. In addition, macOS 11 and later automatically maps AppKit shared images — such as control icons for Action, Add, and Bookmarks — to specific symbols. As a result, your app may already display symbol images offered by SF Symbols in interface elements like the toolbar on Macs that run macOS 11 or later. Using SF symbols ensures that your app’s iconography aligns with the general iconography of macOS.

For guidance, see [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols).

**Create platform-specific glyphs, if necessary.** If your iOS app uses custom glyphs that reference the platform in some way, create new glyphs that feel at home on the Mac. Xcode provides a separate asset catalog you can use in your iOS app for macOS-specific glyphs.

# **Settings**

If you supply app settings that appear in the iOS Settings app, your macOS app automatically displays a Settings menu item and a Settings window. If your iOS app uses child panes to hierarchically organize settings, macOS automatically adds a toolbar to the Settings window with a tab for each child pane. Each tab uses the standard system settings icon and the child pane’s title. When a user clicks the tab, they see the child pane’s settings items.

As Mac users expect, your settings window appears when they choose the Settings menu item in your app menu. However, there are a few ways you can refine the display of your child panes and settings items and make your app’s settings experience feel more at home on the Mac.

**Customize the icon for each tab.** Because macOS automatically uses the standard system-settings icon for your settings items, people will have to read each toolbar button’s title to distinguish among multiple items. To improve this experience, supply a custom icon for each settings item so that each tab displays a different icon.

**Make switch controls easier for macOS users to understand.** A switch in iOS Settings can include a small amount of text that provides more information about how the switch affects the user experience. Additionally, Mac apps, unlike iOS apps, often display a confirmation alert when the user uses a switch to make changes to a setting. To follow macOS platform conventions for app settings, provide a brief description to accompany a switch and specify content to display in a confirmation alert when people change a setting. For developer guidance, see [Displaying a Settings window](https://developer.apple.com/documentation/uikit/creating_a_mac_version_of_your_ipad_app/displaying_a_preferences_window).
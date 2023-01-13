# **[technologies-mac-catalyst] introduction**

# When you use Mac Catalyst to create a Mac version of your iOS app, you make your app available to a new audience and give existing users the opportunity to enjoy it in a new environment.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Mac-Catalyst-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Mac-Catalyst-intro_2x.png)

# **Before you start**

Many iOS apps are great candidates for creating a Mac app with Mac Catalyst. This is especially true for iOS apps that already work well on iPad and support key iPad features; for example:

**Drag and drop.** When you support drag and drop in your iOS app, you also get support for drag and drop in the Mac version.

**Keyboard shortcuts.** Even though a physical keyboard may not always be available on iPad, iPad users appreciate using keyboard shortcuts to streamline their interaction with your app. On the Mac, users always expect apps to offer keyboard shortcuts. By supporting keyboard shortcuts in your iOS app, you make it easy to add support for common macOS shortcuts to your Mac app.

**Multitasking.** Apps that do a good job scaling the interface to support Split View, Slide Over, and Picture in Picture lay the necessary groundwork to support the extensive window resizability that Mac users expect.

**Support for multiple windows.** By supporting multiple scenes on iPad, you also get support for multiple windows in the macOS version.

An iOS app that works well on iPad is a solid foundation for creating a Mac App with Mac Catalyst. However, some apps rely on frameworks or features that don’t exist on a Mac. For example, if your app’s essential features require capabilities like gyroscope, accelerometer, or rear camera, frameworks like HealthKit or ARKit, or if the app’s main function is something like navigation, it might not be suitable for the Mac.

For developer guidance, see [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac_catalyst). For Mac app–design guidance, see [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/platforms/designing-for-macos).

# **Planning enhancements for your Mac app**

Creating a Mac version of your iOS app with Mac Catalyst gives the app automatic support for fundamental macOS features such as:

- Keyboard, trackpad, mouse, and Touch Bar input, including key focus and keyboard navigation
- Window management
- Toolbar support
- Rich text interaction, including copy and paste as well as contextual menus for editing
- File management
- Pull-down menus
- App-specific settings in the system-provided Settings app

System-provided UI elements take on a more Mac-like appearance, too, for example:

- Split view
- File browser
- Activity view
- Form sheet
- Contextual actions
- Color picker

**DEVELOPER NOTE**To get an overview of how views and controls change when you create a Mac app with Mac Catalyst, download [UIKit Catalog: creating and customizing views and controls](https://developer.apple.com/documentation/uikit/mac_catalyst/uikit_catalog_creating_and_customizing_views_and_controls) and build the macOS target.

When you first create a Mac app with Mac Catalyst, Xcode defaults to the "Scale Interface to Match iPad" setting, or *iPad idiom*. This setting allows you to create a Mac app without making big changes to your app’s layout. By choosing the iPad idiom, standard iOS interface elements retain their appearance in the Mac version of your iOS app; for example, the switch control retains its iOS appearance. In addition, the system scales the app’s interface to ensure that text and interface elements are consistent with the macOS display environment without requiring you to update your app’s layout.

As an alternative to choosing the iPad idiom, you can choose the "Optimize Interface for Mac" setting, or *Mac idiom*, in Xcode. With the Mac idiom, your app takes on an even more Mac-like appearance and the system doesn’t scale your app’s layout. As a result, text and graphics appear sharper, making your app look its best on the Mac. However, adopting the Mac idiom often requires you to do additional work on your app’s layout.

When you create a Mac version of your iOS app, initially choose the iPad idiom and make the app feel at home on the Mac by adopting macOS app structure, navigation conventions, and design patterns. After you complete this work, consider switching to the Mac idiom, especially if your app displays a lot of text, detailed artwork, or uses animations.

For guidance, see [Mac idiom](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/mac-idiom).

# **Reviewing platform conventions and design patterns**

When you create a Mac version of your iOS app with Mac Catalyst, you need to ensure that your Mac app gives people a rich Mac experience. No matter whether you adopt the iPad idiom or the Mac idiom, it’s essential to go beyond simply displaying your iOS layout in a macOS window. iOS and macOS each define design patterns and conventions for user interaction that are rooted in the different ways people use their devices. Before you dive in and update specific views and controls, become familiar with the main differences between the platforms so you can create a great Mac app.

Differences in conventions and design patterns with the biggest impact on the Mac version of your iOS app exist in the following key areas:

**Navigation.** Many iOS and macOS apps organize data in similar ways, but they use different controls and visual indicators to help people understand and navigate through the data. For guidance, see [App structure and navigation](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/app-structure).

**User input and interactions.** Although both iPad and Mac accept user input from a range of devices — such as the Multi-Touch display, keyboard, mouse, and trackpad — touch interactions are the basis for iOS conventions. In contrast, keyboard and mouse interactions are key for macOS conventions. For guidance, see [User interaction](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst/overview/user-interaction).

**Menus.** Mac users are familiar with the persistent menu bar and expect to find all app commands in menu-bar menus. iOS, on the other hand, doesn’t have a persistent menu bar, and iOS users expect to find app commands in the app’s UI. For guidance, see [App menus](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/user-interaction#app-menus).

**Visual design and layout.** To take advantage of the wider Mac screen in ways that give Mac users a great experience, update your app’s visual design and layout; for example:

- Divide a single column of content and actions into multiple columns.
- Present an inspector UI next to the main content instead of using a popover.
- Simultaneously show two or more levels of an app’s hierarchy.
- Adopt the Mac idiom to make your app’s appearance even more Mac-like.

For guidance, see [Visual design](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/visual-design).

Viewing your iPad app from the perspective of macOS design conventions can also suggest ways to also improve the iPad version, especially if your iPad app originate on iPhone. As you reassess the ways you lay out views and controls in your Mac app, consider this as an opportunity to see if there are places where you can improve your iOS app to make better use of the large iPad screen.
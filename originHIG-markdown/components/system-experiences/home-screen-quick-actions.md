# **[components-status] home-screen-quick-actions**

## Home Screen quick actions give people a way to perform app-specific actions from the Home Screen.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/home-screen-quick-actions-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/home-screen-quick-actions-intro-dark_2x.png)

People can get a menu of available quick actions when they touch and hold an app icon (on a 3D Touch device, people can press on the icon with increased pressure to see the menu). For example, Mail includes quick actions that open the Inbox or the VIP mailbox, initiate a search, and create a new message. In addition to app-specific actions, a Home Screen quick action menu also lists items for removing the app and editing the Home Screen.

Each Home Screen quick action includes a title, an interface icon on the left or right (depending on your app’s position on the Home Screen), and an optional subtitle. The title and subtitle are always left-aligned in left-to-right languages. Your app can even dynamically update its quick actions when new information is available. For example, Messages provides quick actions for opening your most recent conversations.

# **Best practices**

**Create quick actions for compelling, high-value tasks.** For example, Maps lets people search near their current location or get directions home without first opening the Maps app. Every app should enable at least one useful quick action; you can provide a total of four.

**Avoid making unpredictable changes to quick actions.** Dynamic quick actions are a great way to keep actions relevant. For example, it may make sense to update quick actions based on the current location or recent activities in your app, time of day, or changes in settings. However, actions shouldn’t change in ways that are unpredictable or confusing.

**Provide a succinct title for each quick action.** An action’s title should instantly communicate the results of the action; for example, “Directions Home,” “Create New Contact,” and “New Message.” If you need to give more context, provide a subtitle too. Mail uses subtitles to indicate whether there are unread messages in the Inbox and VIP folder. Don’t include your app name or any extraneous information in the title or subtitle, keep the text short to avoid truncation, and take localization into account as you write the text.

**Provide a recognizable interface icon for each quick action.** Consider using an [SF Symbol](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) to represent an action. If you design your own interface [icons](https://developer.apple.com/design/human-interface-guidelines/foundations/icons), use the Quick Action Icon Template that’s included with [Apple Design Resources for iOS and iPadOS](https://developer.apple.com/design/resources/#ios-apps) and use the following sizes for guidance.

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/max-width-height.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/max-width-height.svg)

Maximum width and height

---

34.67x34.67 pt (104x104 px @3x)

---

35x35 pt (70x70 px @2x)

---

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width-height.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width-height.svg)

Target width and height

---

26.67x26.67 pt (80x80 px @3x)

---

27x27 pt (54x54 px @2x)

---

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width.svg)

Target width (wide glyphs)

---

29.33pt (88px @3x)

---

30pt (60px @2x)

---

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-height.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-height.svg)

Target height (tall glyphs)

---

29.33pt (88px @3x)

---

30pt (60px @2x)

---

**Don’t use an emoji in place of a symbol or interface icon.** Emojis are full color, whereas quick action symbols are monochromatic and change appearance in Dark Mode to maintain contrast.

# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in macOS, watchOS, or tvOS.*
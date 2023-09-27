Home Screen quick actions
=========================

Home Screen quick actions give people a way to perform app-specific actions from the Home Screen.![A stylized representation of a set of menu items extending up from an app icon. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/35e4b815806479aa344da29de3133afb/components-home-screen-quick-actions-intro@2x.png)

People can get a menu of available quick actions when they touch and hold an app icon (on a 3D Touch device, people can press on the icon with increased pressure to see the menu). For example, Mail includes quick actions that open the Inbox or the VIP mailbox, initiate a search, and create a new message. In addition to app-specific actions, a Home Screen quick action menu also lists items for removing the app and editing the Home Screen.

Each Home Screen quick action includes a title, an interface icon on the left or right (depending on your app’s position on the Home Screen), and an optional subtitle. The title and subtitle are always left-aligned in left-to-right languages. Your app can even dynamically update its quick actions when new information is available. For example, Messages provides quick actions for opening your most recent conversations.

[Best practices](/design/human-interface-guidelines/home-screen-quick-actions#Best-practices)
---------------------------------------------------------------------------------------------

**Create quick actions for compelling, high-value tasks.** For example, Maps lets people search near their current location or get directions home without first opening the Maps app. People tend to expect every app to provide at least one useful quick action; you can provide a total of four.

**Avoid making unpredictable changes to quick actions.** Dynamic quick actions are a great way to keep actions relevant. For example, it may make sense to update quick actions based on the current location or recent activities in your app, time of day, or changes in settings. Make sure that actions change in ways that people can predict.

**For each quick action, provide a succinct title that instantly communicates the results of the action.** For example, titles like “Directions Home,” “Create New Contact,” and “New Message” can help people understand what happens when they choose the action. If you need to give more context, provide a subtitle too. Mail uses subtitles to indicate whether there are unread messages in the Inbox and VIP folder. Don’t include your app name or any extraneous information in the title or subtitle, keep the text short to avoid truncation, and take localization into account as you write the text.

**Provide a recognizable interface icon for each quick action.** Consider using [SF Symbols](/design/human-interface-guidelines/sf-symbols)
 to represent actions. If you design your own interface [icon](https://developer.apple.com/design/human-interface-guidelines/icons)
, use the Quick Action Icon Template that’s included with [Apple Design Resources for iOS and iPadOS](https://developer.apple.com/design/resources/#ios-apps)
 and use the following sizes for guidance.

![An illustration of a filled square, which represents the maximum size, with the outline of a smaller square centered inside it. A vertical line, extending to the top and bottom edges of the outer square, represents the maximum height. A horizontal line, extending to the left and right edges of the outer square, represents the maximum width.](https://docs-assets.developer.apple.com/published/1ec1ffc04eedb78e420d7664b663b739/home-screen-max-width-height@2x.png)



| Maximum width and height |
| --- |
| 34.67x34.67 pt (104x104 px @3x) |
| 35x35 pt (70x70 px @2x) |

![An illustration of a filled square, which represents the target, centered inside a larger, outlined square. A vertical line, extending to the top and bottom edges of the inner square, represents the target’s height. A horizontal line, extending to left and right edges of the inner square, represents the target’s width.](https://docs-assets.developer.apple.com/published/c00cf5c89adb35da0baabe3b3a445b7e/home-screen-target-width-height@2x.png)



| Target width and height |
| --- |
| 26.67x26.67 pt (80x80 px @3x) |
| 27x27 pt (54x54 px @2x) |

![An illustration of a filled rectangle, which represents the target, inside the outline of a larger square. The width of the rectangle is slightly larger than its height. A horizontal line, extending to the left and right edges of the rectangle, indicates the target’s width.](https://docs-assets.developer.apple.com/published/c55cfb0ffe717c613e7fc7ea0ece11e0/home-screen-target-width@2x.png)



| Target width (wide glyphs) |
| --- |
| 29.33pt (88px @3x) |
| 30pt (60px @2x) |

![An illustration of a filled rectangle, which represents the target, inside the outline of a larger square. The height of the rectangle is slightly larger than its width. A vertical line, extending to the top and bottom edges of the rectangle, indicates the target’s height.](https://docs-assets.developer.apple.com/published/7f8368ed42dd4bf8359aa57e3763ad7b/home-screen-target-height@2x.png)



| Target height (tall glyphs) |
| --- |
| 29.33pt (88px @3x) |
| 30pt (60px @2x) |

**Don’t use an emoji in place of a symbol or interface icon.** Emojis are full color, whereas quick action symbols are monochromatic and change appearance in Dark Mode to maintain contrast.

[Platform considerations](/design/human-interface-guidelines/home-screen-quick-actions#Platform-considerations)
---------------------------------------------------------------------------------------------------------------

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/home-screen-quick-actions#Resources)
-----------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/home-screen-quick-actions#Related)

[Menus](/design/human-interface-guidelines/menus)


#### [Developer documentation](/design/human-interface-guidelines/home-screen-quick-actions#Developer-documentation)

[Add Home Screen Quick Actions](/documentation/uikit/menus_and_shortcuts/add_home_screen_quick_actions)



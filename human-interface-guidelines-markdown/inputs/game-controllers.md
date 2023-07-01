Game controllers
================

Game controllers can enhance gameplay and increase a player’s immersion in a game.![A sketch of a game controller, suggesting gameplay. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4186aa8fd4fb94811a5752cdcdeeb036/inputs-game-controller-intro@2x.png)

Supporting as many types of game controllers as possible gives people additional ways to enjoy interacting with your game.

[Best practices](/design/human-interface-guidelines/game-controllers#Best-practices)
------------------------------------------------------------------------------------

**Support the platform’s default input method.** A game controller is an optional purchase, but every iPhone and iPad has a touchscreen, every Mac has a keyboard and a touchpad or mouse, and every Apple TV has a remote. If you support game controllers, consider letting people use the platform’s default input method to controls games, too.

**Determine game controller requirements.** If your game has advanced game mechanics that a platform’s default input method can’t support, you can require the use of a game controller. The App Store displays a “Game Controller Required” badge to help people identify such apps and may warn people if they haven’t paired a compatible game controller with their device.

**Confirm required game controller connections.** People can open your game any time, even without a connected controller. If your app requires a game controller, check for its presence and gracefully prompt people to connect one if necessary.

**Help people understand the advantages of using a game controller with your app.** If your game is playable without a game controller, but using a game controller is recommended, look for ways to inform players that using a game controller will make playing easier and more enjoyable.

**Avoid requiring people to switch input devices.** For example, make sure players can use a game controller to navigate all game menus and interact with all essential functions without needing to switch to the platform’s default input method.

![An illustration of a game controller with callouts that indicate the locations of the controller’s triggers, shoulder buttons, directional pad, and thumbsticks.](https://docs-assets.developer.apple.com/published/eb11b2fd68cf6b6415990ad147ea4c0d/game-controller@2x.png)

**Support clickable thumbsticks when present.** Some controllers include thumbsticks that people can click or hold down as well as rotate. These buttons — also known as L3 and R3 — typically let people modify the current action by rotating the thumbstick. For example, clicking or holding a left thumbstick that causes motion might let people move at a different speed; clicking or holding a right thumbstick that controls camera orientation might let people zoom in or “crouch.” As you consider ways to support clickable thumbsticks, be guided by the behaviors that people expect in various game genres.

**In general, prefer using the left thumbstick or directional pad (D-pad) button to move focus in the current screen.** Typically, people don’t expect to use the right thumbstick to perform focus navigation while in a game.

**Customize onscreen instructions to help people use the connected game controller.** Different controllers can use different colors or symbols to represent similar buttons, so it’s a good idea to avoid using color alone to refer to a button or explain what it does. Instead, refer to a button using the connected controller’s labeling scheme, such as “A” or the image of a triangle or square. In some cases, you might consider also showing an image of the interaction instead of using only a button label. For example, you might display an image of a D-pad, highlighted to indicate the up direction. Using images in addition to labels can be especially helpful for people who aren’t experienced with controllers because it doesn’t require them to hunt for a specific button label during gameplay.

[Buttons](/design/human-interface-guidelines/game-controllers#Buttons)
----------------------------------------------------------------------

In addition to playing games, people can use a game controller to navigate system and app interfaces, eliminating the need to switch input devices.



| Button | Expected behavior in iOS and iPadOS | Expected behavior in macOS | Expected behavior in tvOS |
| --- | --- | --- | --- |
| D-pad | Moves focus | Moves focus | Moves focus |
| A | Activates a control or selects an item | Activates a control or selects an item | Activates a control or selects an item |
| B | – | – | Returns to previous screen. Exits to Apple TV Home Screen from an app’s root-level screen. |
| X | Activates media playback. Pauses/resumes media playback. | Activates media playback. Pauses/resumes media playback. | Activates media playback. Pauses/resumes media playback. |
| Y | – | – | N/A |
| Left shoulder/trigger | Navigates left or moves focus | Navigates left or moves focus | Navigates left or moves focus |
| Right shoulder/trigger | Navigates right or moves focus | Navigates right or moves focus | Navigates right or moves focus |
| Left thumbstick | Navigates. Moves focus. | Navigates. Moves focus. | Navigates. Moves focus. |
| Right thumbstick | – | – | N/A |

A controller with a single auxiliary button needs to support the following behaviors:



| Interaction with auxiliary button | Expected behavior in iOS and iPadOS | Expected behavior in macOS | Expected behavior in tvOS |
| --- | --- | --- | --- |
| Press | Returns to previous screen or pauses game | Returns to previous screen or pauses game | Returns to previous screen or pauses game |
| Long press | N/A | N/A | Exits to Apple TV Home Screen |
| Double press | Reveals multitasking user interface | Reveals multitasking user interface | Reveals multitasking user interface |

A controller with multiple auxiliary buttons includes a logo button in addition to the Menu button. Such a controller needs to support the following behaviors when people interact with the logo and Menu buttons:



| Button | Interaction | Expected behavior in iOS and iPadOS | Expected behavior in macOS | Expected behavior in tvOS |
| --- | --- | --- | --- | --- |
| Logo | Press | Reveals Control Center | Reveals Control Center | Reveals Control Center |
|  | Long press | N/A | N/A | Exists to Apple TV Home Screen |
|  | Double press | Reveals multitasking user interface | Reveals multitasking user interface | Reveals multitasking user interface |
| Menu | Press | Pauses game | Pauses game | Pauses game |

[Platform considerations](/design/human-interface-guidelines/game-controllers#Platform-considerations)
------------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS. Not supported in watchOS.*

[Resources](/design/human-interface-guidelines/game-controllers#Resources)
--------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/game-controllers#Related)

[Feedback](/design/human-interface-guidelines/feedback)


#### [Developer documentation](/design/human-interface-guidelines/game-controllers#Developer-documentation)

[Game Controller](/documentation/gamecontroller)


#### [Videos](/design/human-interface-guidelines/game-controllers#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/48/919F0864-4C46-496C-AF1A-48B0CBA92170/2914_wide_250x141_1x.jpg) Supporting New Game Controllers](https://developer.apple.com/videos/play/wwdc2019/616) 

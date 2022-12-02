# **[inputs] touchscreen-gestures**

## Gestures are a key way for people to interact with their touchscreen devices, eliciting a close personal connection with content and enhancing the sense of directly manipulating onscreen objects.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-gestures-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-gestures-intro_2x.png)

In addition to using a touchscreen, people can also gesture using devices such as a trackpad, mouse, remote, or game controller. For example, people can use a trackpad to interact with their iPad or Mac, and they can use a game controller to interact with iPhone, iPad, Mac, and Apple TV. For guidance incorporating input from these devices, see [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices), [Remotes](https://developer.apple.com/design/human-interface-guidelines/inputs/remotes), and [Game controllers](https://developer.apple.com/design/human-interface-guidelines/inputs/game-controllers).

Touchscreen devices all use basic gestures like tap, swipe, and drag. Some platforms define additional gestures; for example, iOS and iPadOS support pinch and rotate. As you incorporate touchscreen gestures into your interface, you need to understand the behaviors of each platform’s [standard gestures](https://developer.apple.com/design/human-interface-guidelines/inputs/touchscreen-gestures#standard-gestures) so that you can provide a familiar and consistent experience.

# **Best practices**

**In general, respond to gestures in ways that are consistent with other apps.** People expect most gestures to work the same regardless of their current context. For example, people expect the pinch gesture to adjust a view’s zoom level or scale a selected object. Avoid using a familiar gesture to perform an action that’s unique to your app; similarly, avoid creating a unique gesture to perform a standard action like choosing a button or scrolling a long view.

**Define custom gestures only when necessary.** People might find it difficult to discover and remember a custom gesture, and if it's awkward to perform, people may not want — or be able — to use it. Prefer custom gestures for situations where your app offers an immersive experience that requires context-specific interactions, like in a game or a drawing app, or when the system doesn’t handle a standard gesture, such as pinch in watchOS, or a gesture in a SpriteKit or SceneKit scene. If you decide to define a custom gesture, make sure it’s:

- Easy to discover and perform
- Not too similar to gestures people already know
- Not the only way to perform an important action in your app

**Make sure gestures apply to the appropriate content.** In general, gestures should apply to the content with which people are currently interacting, such as a selected element, an active view in a window, or an area on top of an item, like a photo. Start by using finger positions to help you identify the most specific content people are likely to be manipulating, and make that content the gesture’s target. If the content doesn’t respond to the gesture, consider targeting higher content levels and containers.

**Handle gestures as responsively as possible.** Gestures enhance the experience of direct manipulation and provide immediate live feedback. As people perform a gesture in your app, provide feedback that helps them predict its results and, if necessary, communicates the extent and type of movement required to complete the action.

**Enable shortcut gestures to supplement standard gestures, not to replace them.** People need simple, familiar ways to navigate and perform actions, even if it means an extra tap or two. For example, in an app that supports navigation through a hierarchy of screens, people expect to find a back button in a navigation bar that lets them return to the previous screen with a single tap. To help accelerate this action, many apps also offer a shortcut gesture — such as swiping from the side of the display or window — while continuing to provide the back button.

**Avoid interfering with systemwide screen-edge gestures.** Depending on the device, screen-edge gestures can provide access to the Home Screen, App Switcher, Notification Center, Control Center, and Dock. People rely on these gestures to work in every app. In rare cases, an immersive app like a game might require custom screen-edge gestures that take priority over the system's gestures. In this rare scenario, the game can use a behavior called *edge protect* in which the first swipe invokes the app-specific gesture and a second swipe invokes the system gesture. If you must enable custom screen-edge gestures, use edge protect sparingly, because people must perform a second gesture before they can access the system-level actions. For developer guidance, see the [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/uikit/uiviewcontroller/2887512-preferredscreenedgesdeferringsys)property of [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller).

# **Standard gestures**

| Gesture | iOS | iPadOS | watchOS | Standard action |
| --- | --- | --- | --- | --- |
| Tap | ● | ● | ● | Activate a control.Select an item. |
| Swipe | ● | ● | ● | Reveal actions and controls.Dismiss views.Scroll. |
| Pan (UIKit) / Drag (SwiftUI) | ● | ● | ● | Move a UI element. |
| Pinch (UIKit) / Magnification (SwiftUI) | ● | ● | – | Zoom a view.Magnify content. |
| Long press | ● | ● | ● | Reveal additional controls or functionality |
| Rotation | ● | ● | – | Rotate a selected item. |
| Edge swipe | ● | ● | ● | Navigate.Reveal controls, information, or system experiences. |
| Double tap | ● | ● | – | Zoom in.Zoom out if already zoomed in. |
| Three-finger swipe | ● | ● | – | Initiate undo (left swipe).Initiate redo (right swipe). |
| Four-finger swipe | – | ● | – | Switch between apps. |
| Three-finger pinch | ● | ● | – | Copy selected text (pinch in).Paste copied text (pinch out). |

# **Platform considerations**

*Not supported in macOS or tvOS.*

# **iOS, iPadOS**

**Consider enabling simultaneous recognition of multiple gestures if it enhances the experience.** Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating touchscreen input with Apple Pencil input in your iPadOS app, see [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble).

# **watchOS**

**Consider alternatives to the long press gesture.** In versions of watchOS earlier than watchOS 7, people could press firmly on the display to do things like change the watch face or reveal a hidden menu called a Force Touch menu. In watchOS 7 and later, system apps make previously hidden menu items accessible in a related screen or a settings screen. If you formerly supported a long-press gesture to open a hidden menu, consider relocating the menu items elsewhere. For guidance, see [Menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus).
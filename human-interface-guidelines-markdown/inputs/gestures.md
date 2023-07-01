June 21, 2023

 Changed page title from Touchscreen gestures and updated to include guidance for visionOS. Gestures
========

Gestures are a key way for people to interact with their devices, eliciting a close personal connection with content and enhancing the sense of directly manipulating app objects.![A sketch of a pointing hand swiping in a curved motion toward the right, suggesting touch interaction with a device. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/21ef165b3e1da4255ee2a9a55796afc0/inputs-gestures-intro@2x.png)

Depending on the device they’re using, people can make gestures on a touchscreen, in the air, or on a range of input devices such as a trackpad, mouse, remote, or game controller.

Every platform supports basic gestures like tap, swipe, and drag. Although the precise movements that make up basic gestures can vary per platform and input device, people are familiar with the underlying functionality of these gestures and expect to use them everywhere. For a list of these gestures, see [Standard gestures](/design/human-interface-guidelines/gestures#Standard-gestures)
.

[Best practices](/design/human-interface-guidelines/gestures#Best-practices)
----------------------------------------------------------------------------

**Always be sure to give people multiple ways to interact with your app.** Design your app to support the accessibility features people use to personalize the ways they interact with their devices. For guidance, see [Accessibility](/design/human-interface-guidelines/accessibility)
.

**In general, respond to gestures in ways that are consistent with other apps on the device.** People expect most gestures to work the same regardless of their current context. For example, people expect tap to activate or select an object. Avoid using a familiar gesture to perform an action that’s unique to your app; similarly, avoid creating a unique gesture to perform a standard action like activating a button or scrolling a long view.

**Define custom gestures only when necessary.** People might find it difficult to discover and remember a custom gesture, and if it’s awkward to perform, people may not want — or be able — to use it. Prefer custom gestures for situations where your app offers an in-depth experience that requires context-specific interactions, like in a game or a drawing app, or when the system doesn’t handle a standard gesture, such as pinch in watchOS. If you decide to define a custom gesture, make sure it’s:

* Easy to discover and perform
* Not too similar to gestures people already know
* Not the only way to perform an important action in your app

**Handle gestures as responsively as possible.** Gestures enhance the experience of direct manipulation and provide immediate feedback. As people perform a gesture in your app, provide feedback that helps them predict its results and, if necessary, communicates the extent and type of movement required to complete the action.

**Offer shortcut gestures to supplement standard gestures, not to replace them.** People need simple, familiar ways to navigate and perform actions, even if it means an extra tap or two. For example, in an app that supports navigation through a hierarchy of views, people expect to find a Back button in a navigation bar that lets them return to the previous view with a single tap. To help accelerate this action, many apps also offer a shortcut gesture — such as swiping from the side of a window or touchscreen — while continuing to provide the Back button.

**In iOS, iPadOS, and watchOS, avoid interfering with system-defined screen-edge gestures.** Screen-edge gestures like edge swipe can provide access to the Home Screen, App Switcher, Notification Center, Control Center, and Dock, and people rely on such gestures to work in every app. In rare cases, a game might require custom screen-edge gestures that take priority over the system’s gestures. In this rare scenario, the game can use a behavior called *edge protect* in which the first swipe invokes the app-specific gesture and a second swipe invokes the system gesture. If you must define custom screen-edge gestures, use edge protect sparingly, because people must perform a second gesture before they can access the system-level actions. For developer guidance, see the [`preferredScreenEdgesDeferringSystemGestures`](/documentation/uikit/uiviewcontroller/2887512-preferredscreenedgesdeferringsys)
 property of [`UIViewController`](/documentation/uikit/uiviewcontroller)
.

[Platform considerations](/design/human-interface-guidelines/gestures#Platform-considerations)
----------------------------------------------------------------------------------------------

### [iOS, iPadOS](/design/human-interface-guidelines/gestures#iOS-iPadOS)

In addition to the [standard gestures](/design/human-interface-guidelines/gestures#Standard-gestures)
 supported in all platforms, iOS and iPadOS support a few other gestures that people expect.



| Gesture | Common action |
| --- | --- |
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |

**Consider allowing simultaneous recognition of multiple gestures if it enhances the experience.** Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating touchscreen input with Apple Pencil input in your iPadOS app, see [Apple Pencil and Scribble](/design/human-interface-guidelines/apple-pencil-and-scribble)
.

### [macOS](/design/human-interface-guidelines/gestures#macOS)

Although most people tend to use a [keyboard](/design/human-interface-guidelines/keyboards)
 to interact with a Mac, they can also make [standard gestures](/design/human-interface-guidelines/gestures#Standard-gestures)
 on a Magic Trackpad, Magic Mouse, or a [game controller](/design/human-interface-guidelines/game-controllers)
 that includes a touch surface.

### [tvOS](/design/human-interface-guidelines/gestures#tvOS)

People expect to use [standard gestures](/design/human-interface-guidelines/gestures#Standard-gestures)
 with the Siri Remote to navigate tvOS apps, browse channels and content, play and pause media, and make selections (for guidance, see [Remotes](/design/human-interface-guidelines/remotes)
). People also expect to use standard gestures with a compatible remote or [game controller](/design/human-interface-guidelines/game-controllers)
 that includes a touch surface.

### [visionOS](/design/human-interface-guidelines/gestures#visionOS)

visionOS defines two types of gestures: indirect and direct.

An *indirect* gesture affects the currently focused object. For example, after people bring [focus](/design/human-interface-guidelines/focus-and-selection)
 to a control, they can activate or select it by quickly tapping a finger to their thumb to make the indirect tap gesture. visionOS supports indirect gestures by default, and people use them to perform the [standard gestures](/design/human-interface-guidelines/gestures#Standard-gestures)
 they already know.

 [Play](#) 
Indirect gestures tend to be fast — because people can look in different directions quickly — and comfortable, because device cameras can capture hand movements while people’s hands rest in their laps or at their sides. In addition, indirect gestures let people interact with any object they can focus, regardless of its location in space, because they don’t have to be able to reach it with their hands.

A *direct* gesture affects the object that people are touching (in visionOS, people *touch* a virtual object by bringing a finger close to the object). For example, one way people can use the system-provided keyboard is to touch the keys. Direct gestures require objects to be near enough for people to reach them. Also, because people have to move their hand, instead of their eyes, to the object, direct gestures tend to be better suited to situations where quick, precise interactions aren’t critical.

 [Play](#) 
Here are the common direct gestures people use in visionOS.



| Direct gesture | Common use |
| --- | --- |
| Touch | Directly select or activate an object. |
| Touch and hold | Open a contextual menu. |
| Touch and drag | Move an object to a new location. |
| Double touch | Preview an object or file; select a word in an editing context. |
| Swipe | Reveal actions and controls; dismiss views; scroll. |
| With two hands, pinch and drag together or apart | Zoom in or out. |
| With two hands, pinch and drag in a circular motion | Rotate an object. |

**Support tap everywhere you can.** As soon as people focus an object in your app or game, tap is the first gesture they’re likely to make when they want to select or activate it. Even if you also support custom gestures, supporting tap throughout your experience can help people get comfortable with your app or game quickly.

**Prefer indirect gestures.** An indirect gesture tends to be easy for people to make because they don’t have to move their hands to a specific location. Reserve direct gestures for when you want to invite people to manipulate a nearby virtual object.

**If direct gestures are a feature of your app, make sure people can get the same functionality using indirect gestures.** As much as possible, you want people to have the flexibility to choose the interaction method that works best for them.

**Avoid requiring specific body movements or positions for input.** Provide alternatives to input that requires people to move.

#### [Designing custom gestures in visionOS](/design/human-interface-guidelines/gestures#Designing-custom-gestures-in-visionOS)

To create a custom gesture, you rely on ARKit for information like hand positioning and joint orientation. Before you can offer custom gestures in your app, your app must be running in a Full Space and you must request people’s permission to access information about their hands. For developer guidance, see [Setting up access to ARKit data](/documentation/visionOS/setting-up-access-to-arkit-data)
.

![A screenshot of a person's hands performing a custom gesture, placing the two hands together to form a heart, while playing a visionOS game.](https://docs-assets.developer.apple.com/published/363ecbc8eeb441809f62ae935e13fbdc/visionos-custom-spatial-gesture-happy-beam@2x.png)

**Prioritize comfort in custom gestures.** Continually test the ergonomics of all interactions that require custom gestures. A custom interaction that requires people to keep their arms raised for even a little while can be physically tiring, and repeating very similar movements many times in succession can stress people’s muscles and joints.

**Consider carefully before defining custom gestures that involve multiple fingers or both hands.** It can be challenging for people to perform custom gestures, and requiring them to position multiple fingers or use both hands at the same time can be even more difficult.

**Avoid creating a custom gesture that requires people to use a specific hand.** Expecting people to remember which hand to use for a custom gesture increases their cognitive load while also making your experience less welcoming to people with strong hand-dominance or limb differences.

If you decide to create a custom gesture, make sure it’s:

* **Inclusive.** Gestures can mean different things to different people, so be sure your custom gestures don’t send messages you don’t intend.
* **Comfortable.** Great custom gestures are physically easy for people to perform, especially over time.
* **Distinctive.** Custom gestures that harmonize with your app or game can be easier for people to discover and remember, while enhancing their enjoyment of the experience.
* **Easy to describe.** If you can’t use simple language and simple graphics to describe your custom gesture, it may mean that the gesture will be difficult for people to learn and perform.

### [watchOS](/design/human-interface-guidelines/gestures#watchOS)

**Consider alternatives to the long-press gesture.** In versions of watchOS earlier than watchOS 7, people could press firmly on the display to do things like change the watch face or reveal a hidden menu called a Force Touch menu. In watchOS 7 and later, system apps make previously hidden menu items accessible in a related screen or a settings screen. If you formerly supported a long-press gesture to open a hidden menu, consider relocating the menu items elsewhere. For guidance, see [Menus](/design/human-interface-guidelines/menus)
.

[Specifications](/design/human-interface-guidelines/gestures#Specifications)
----------------------------------------------------------------------------

### [Standard gestures](/design/human-interface-guidelines/gestures#Standard-gestures)

The system provides APIs that support the familiar gestures people use with their devices, whether they use a touchscreen, an indirect gesture in visionOS, or an input device like a trackpad, mouse, remote, or game controller. For developer guidance, see [Gestures](/documentation/SwiftUI/Gestures)
.



| Gesture | Supported in | Common action |
| --- | --- | --- |
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control; select an item. |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions and controls; dismiss views; scroll. |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element. |
| Touch (or pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality. |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS | Zoom in; zoom out if already zoomed in. |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view; magnify content. |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate a selected item. |

For guidance on supporting additional gestures and button presses on specific input devices, see [Pointing devices](/design/human-interface-guidelines/pointing-devices)
, [Remotes](/design/human-interface-guidelines/remotes)
, and [Game controllers](/design/human-interface-guidelines/game-controllers)
.

[Resources](/design/human-interface-guidelines/gestures#Resources)
------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/gestures#Related)

[Feedback](/design/human-interface-guidelines/feedback)


[Eyes](/design/human-interface-guidelines/eyes)


#### [Developer documentation](/design/human-interface-guidelines/gestures#Developer-documentation)

[`UITouch`](/documentation/uikit/uitouch)


#### [Videos](/design/human-interface-guidelines/gestures#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_1x.jpg) Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 
[Change log](/design/human-interface-guidelines/gestures#Change-log)
--------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Changed page title from Touchscreen gestures and updated to include guidance for visionOS. |


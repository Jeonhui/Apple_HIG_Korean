# **[inputs] focus-and-selection**

## Focus visually identifies the onscreen object that will respond to interactions like a mouse click, a keyboard command, or a button press on a remote.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-focus-and-selection-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-focus-and-selection-intro_2x.png)

Focus enables a simplified, element-based navigation experience tailored to situations where the current input device doesn’t necessarily enable access to every part of the screen. For example, when people use their finger, a pointing device, or Apple Pencil, they can target any onscreen area, often with pixel-level precision. In contrast, when people use an input device like a keyboard, remote, or game controller, they target specific interface elements, not pixels.

It’s important to understand that focusing an item is not always the same as selecting it. In tvOS, for example, people generally use one gesture to focus an interface component and another gesture to select it. In iPadOS, bringing focus to an item can also select it, as long as selection doesn’t produce behavior that might be distracting, like switching to a new view or showing an alert.

Different platforms communicate focus using different visual indicators. For example, iPadOS and macOS can call attention to a focused item by drawing a ring around it or highlighting it; tvOS generally uses the [parallax effect](https://developer.apple.com/design/human-interface-guidelines/foundations/images#parallax-effect) to give the focused item an appearance of depth and liveliness. The system’s implementation of focus effects and interactions is sometimes called a *focus system* or *focus model*.

# **Best practices**

**Rely on system-provided focus effects.** System-defined focus effects can provide experiences that feel tactile, responsive, and fluid. In tvOS, for example, when people swipe quickly to move focus from one side of the screen to the other, the system communicates a natural sense of inertia as focus subtly accelerates and then decelerates through onscreen items. Consider creating a custom focus system only if it’s absolutely necessary.

**Let people control focus movement as much as possible.** People rely on the focus system to help them know where they are in your app, so it’s important to avoid moving focus to a different item without their interaction. An exception is when a previously focused item no longer exists; in this scenario, it’s less confusing to move focus to a new item than it is to hide the visual focus indication.

# **Platform considerations**

*Not supported in iOS or watchOS.*

# **iPadOS, macOS**

**Let people bring focus to content elements — such as list items, text fields, and search fields — but not to controls like buttons, sliders, and toggles.** In iPadOS and macOS, people use [Full Keyboard Access](https://support.apple.com/en-mn/guide/mac-help/mchlc06d1059/mac) to reach every control through keyboard interactions, so you need only enable focus for key content features in your app. To learn more about supporting focus behavior in your iPadOS app, see [Keyboard navigation on iPad](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/#keyboard-navigation-on-ipad).

**Use consistent visual appearances for focused items.** For example, give a focused list item an inverted highlight that uses your app’s accent color, and give an unfocused list item a light gray highlight when it’s selected (for developer guidance, see [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview/) and [NSTableView](https://developer.apple.com/documentation/appkit/nstableview/)).

**In general, use a focus ring for a text or search field, but use a highlight in a list or collection.** Although you can use a focus ring to draw attention to an item that fills a cell, like a photo, it’s easier for people to view lists and collections when an entire row is highlighted.

# **tvOS**

**Make sure people can bring focus to every element in your app.** People rely on using directional gestures on a remote or game controller (or pressing the arrow keys on an attached keyboard) to reach every onscreen element.

**In a full-screen experience, let people use gestures to interact with the content, not to move focus.** When an item displays in full screen, it doesn’t show focus, so people naturally assume that their gestures will affect the object, and not its focus state.

**Avoid displaying a pointer.** People expect to navigate a fixed number of items by changing focus, not by trying to drag a tiny pointer around a huge screen. While free-form movement might make sense during gameplay, such as when looking for a hidden object or flying a plane, use the focus model when people navigate menus and other interface elements. If your app requires a pointer, make sure it’s highly visible and feels integrated with your experience.

**Design your interface to accommodate components in various focus states.** In tvOS, focusable items can have up to five different states, each of which is visually distinct. Because focusing an item often increases its scale, you need to supply assets for the larger, focused size to ensure they always look sharp, and you need to make sure the larger item doesn’t crowd the surrounding interface.

[제목 없음](https://www.notion.so/d25c90a1a9c04fe89fe42b1eefc88408)

For developer guidance, see [Adding user-focusable elements to a tvOS app](https://developer.apple.com/documentation/uikit/focus-based_navigation/adding_user-focusable_elements_to_a_tvos_app).
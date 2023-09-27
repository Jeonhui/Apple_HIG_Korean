June 21, 2023

 Updated to include guidance for visionOS. Buttons
=======

A button initiates an instantaneous action.![A stylized representation of two horizontally aligned buttons. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/1e58c07540f30e0b4c3342770e6270af/components-buttons-intro@2x.png)

Versatile and highly customizable, buttons give people simple, familiar ways to do tasks in your app. In general, a button combines three attributes to clearly communicate its function:

* **Style.** A visual style based on size, color, and shape.
* **Content.** The symbol (or interface icon), text label, or both that a button displays to convey its purpose.
* **Role.** A system-defined role that identifies a button’s semantic meaning and can affect its appearance.

In addition to all-purpose buttons, many common button styles — like Info, Close, and Contact Add — perform familiar tasks throughout the system. There are also many button-like components that have distinct appearances and behaviors for specific use cases, like [toggles](/design/human-interface-guidelines/toggles)
, [pop-up buttons](/design/human-interface-guidelines/pop-up-buttons)
, and [segmented controls](/design/human-interface-guidelines/segmented-controls)
.

[Best practices](/design/human-interface-guidelines/buttons#Best-practices)
---------------------------------------------------------------------------

When buttons are instantly recognizable and easy to understand, an app tends to feel intuitive and well designed.

**Make buttons easy for people to use.** It’s essential to include enough space around a button so that people can visually distinguish it from surrounding components and content. Giving a button enough space is also critical for helping people select or activate it, regardless of the method of input they use. As a general rule, a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt — to ensure that people can select it easily, whether they use a fingertip, a pointer, their eyes, or a remote.

**Ensure that each button clearly communicates it purpose.** A button always includes a text label or a symbol (or interface icon) — and sometimes a combination of both — to help people predict what it does.

[Style](/design/human-interface-guidelines/buttons#Style)
---------------------------------------------------------

System buttons offer a range of styles that support extensive customization while providing built-in interaction states, accessibility support, and appearance adaptation. Different platforms define different styles that help you communicate hierarchies of actions in your app.

You can configure a system button to use any combination of style and size. By default, a system button uses a size-specific corner radius and your app’s accent color. If necessary, you can change these attributes, in addition to attributes that control content layout and the presence of an activity indicator.

**In general, use a button that has a visible background for the most likely action in a view.** Buttons that have a fill or background shape tend to be the most visually prominent, helping people quickly identify the action they’re most likely to want.

**Consider keeping the number of visually prominent buttons to one or two per view.** Giving people too many prominent buttons increases their cognitive load, requiring them to spend more time considering options before making a choice.

**Use style — not size — to visually distinguish the preferred choice among multiple options.** When you use buttons of the same size to offer two or more options, you signal that the options form a coherent set of choices. If you want to highlight the preferred or most likely option in a set, use a more prominent button style for that option and a less prominent style for the remaining ones.

[Content](/design/human-interface-guidelines/buttons#Content)
-------------------------------------------------------------

**Create button content that helps people instantly understand what the button does.** Depending on the platform, a button can contain an icon, text, or both.

Note

In macOS and visionOS, the system displays a tooltip after people hover over a button for a moment. A tooltip displays a brief phrase that explains what a button does; for guidance, see [Offering help](/design/human-interface-guidelines/offering-help)
.

**Consider using an icon when a button performs a familiar action that people associate with the icon.** For example, people can predict that a button containing the `square.and.arrow.up` symbol will help them perform share-related activities. If it makes sense to use an icon in your button, consider using an existing or customized [symbol](/design/human-interface-guidelines/sf-symbols)
.

**Consider using text when a short label communicates more clearly than an icon.** To use text, write a few words that succinctly describe what the button does. Using [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64)
, consider starting the label with a verb to help convey the button’s action — for example, a button that lets people add items to their shopping cart might use the label “Add to Cart.”

[Role](/design/human-interface-guidelines/buttons#Role)
-------------------------------------------------------

A system button can have one of the following roles:

* **Normal.** No specific meaning.
* **Primary.** The button is the default button — the button people are most likely to choose.
* **Cancel.** The button cancels the current action.
* **Destructive.** The button performs an action that can result in data destruction.

A button’s role can have additional effects on the appearance you configure. For example, the system can use bold text for the label in a primary button, whereas a destructive button uses a red color.

**Assign the primary role to the button people are most likely to choose.** When a primary button responds to the Return key, it makes it easy for people to quickly confirm their choice. In addition, when the button is in a temporary view — like a [sheet](/design/human-interface-guidelines/sheets)
, an editable view, or an [alert](/design/human-interface-guidelines/alerts)
 — assigning it the primary role means that the view can automatically close when people press Return.

**Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice.** Because of its visual prominence, people sometimes choose a primary button without reading it first. Help people avoid losing content by assigning the primary role to nondestructive buttons.

[Platform considerations](/design/human-interface-guidelines/buttons#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for tvOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/buttons#iOS-iPadOS)

iOS and iPadOS have four button styles, each available in three sizes. Each combination of size and style has a different level of visual prominence.

![An illustration showing a matrix of the 12 possible size and style combinations of a system button that contains a right-pointing triangle and the word Play. The rows of the matrix represent the sizes small, medium, and large; the columns represent the styles plain, gray, tinted, and filled.](https://docs-assets.developer.apple.com/published/f12460d1f751463c7588623e011e13ef/button-sizes-styles@2x.png)

**Include additional text below the label only if it provides useful details.** Additional text uses a smaller text size than the label, showing that the information is secondary to the button’s action. For example, you might add text to update an Add to Cart button with the number of items in the cart. Avoid writing a subtitle that explains more about what the button does; make sure a button’s containing view, label or image, style, and role provide all the information people need to understand its action.

**Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.** Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different label alongside the activity indicator. For example, the label “Checkout” could change to “Checking out…” while the activity indicator is visible. When a delay occurs after people click or tap your configured button, the system displays the activity indicator next to the original or alternative label, hiding the button image, if there is one.

![An illustration that represents the People tab in the Find My app. The People sheet uses two same-size buttons to provide the option to share their location with another person or cancel.](https://docs-assets.developer.apple.com/published/451d5391eb190cd4059edb2ce6bbb432/button-activity-indicator-hidden@2x.png)

![An illustration that represents the People tab in the Find My app, showing that after someone taps the Share button a spinning activity indicator appears inside the leading edge of the button.](https://docs-assets.developer.apple.com/published/8c1f6f94ea9360484d2a23c744617a7b/button-activity-indicator-visible@2x.png)

### [macOS](/design/human-interface-guidelines/buttons#macOS)

Several specific button types are unique to macOS.

#### [Push buttons](/design/human-interface-guidelines/buttons#Push-buttons)

The standard button type in macOS is known as a *push button*. You can configure a push button to display text, a symbol, an interface icon, or an image, or a combination of text and image content. Push buttons can act as the default button in a view and you can tint them.

**Use a flexible-height push button only when you need to display tall or variable height content.** Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button that contains two lines of text or a tall icon, use a flexible-height button; otherwise, use a standard push button. For developer guidance, see [`NSBezelStyleRegularSquare`](/documentation/appkit/nsbezelstyle/nsbezelstyleregularsquare)
.

**Append a trailing ellipsis to the title when a push button opens another window, view, or app.** Throughout the system, an ellipsis in a control title signals that people can provide additional input. For example, the Edit buttons in the AutoFill pane of Safari Settings include ellipses because they open other views that let people modify autofill values.

**Consider supporting spring loading.** On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can continue dragging the items, possibly to perform additional actions.

#### [Gradient buttons](/design/human-interface-guidelines/buttons#Gradient-buttons)

A gradient button initiates an action related to a view, like adding or removing rows in a table.

![A screenshot of gradient buttons for add (with a plus symbol) and remove (with a minus symbol), appearing in the Login Items settings pane.](https://docs-assets.developer.apple.com/published/f2606e47b757034508eafaa1390d2923/gradient-buttons-macos@2x.png)

Gradient buttons contain symbols or interface icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear in close proximity to their associated view — usually within or beneath it — so people know which view the buttons affect.

**Use gradient buttons in a view, not in the window frame.** Gradient buttons aren’t intended for use in toolbars or status bars. If you need a button in a [toolbar](https://developer.apple.com/design/human-interface-guidelines/toolbars)
, use a toolbar item.

**Prefer using a symbol in a gradient button.** [SF Symbols](/design/human-interface-guidelines/sf-symbols)
 provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.

**Avoid using labels to introduce gradient buttons.** Because gradient buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.

For developer guidance, see [`NSBezelStyleSmallSquare`](/documentation/appkit/nsbezelstyle/nsbezelstylesmallsquare)
.

#### [Help buttons](/design/human-interface-guidelines/buttons#Help-buttons)

A help button appears within a view and opens app-specific help documentation.

![A screenshot of the help button highlighted in the lower-right corner of a VoiceOver settings pane.](https://docs-assets.developer.apple.com/published/8758db366f196180da7cfda317b49cde/help-buttons-macos@2x.png)

Help buttons are circular, consistently sized buttons that contain a question mark. For guidance on creating help documentation, see [Offering help](/design/human-interface-guidelines/offering-help)
.

**Use the system-provided help button to display your help documentation.** People are familiar with the appearance of the standard help button and know that choosing it opens help content.

**When possible, open the help topic that’s related to the current context.** For example, the help button in the Rules pane of Mail settings opens the Mail User Guide to a help topic that explains how to change these settings. If no specific help topic applies directly to the current context, open the top level of your app’s help documentation when people choose a help button.

**Include no more than one help button per window.** Multiple help buttons in the same context make it hard for people to predict the result of clicking one.

**Position help buttons where people expect to find them.** Use the following locations for guidance.



| View style | Help button location |
| --- | --- |
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

**Use a help button within a view, not in the window frame.** For example, avoid placing a help button in a toolbar or status bar.

**Avoid displaying text that introduces a help button.** People know what a help button does, so they don’t need additional descriptive text.

#### [Image buttons](/design/human-interface-guidelines/buttons#Image-buttons)

An image button appears in a view and displays an image, symbol, or interface icon. You can configure an image button to behave like a push button, toggle, or pop-up button.

![A screenshot of an image button as used in Pages to show how an image will appear when applying styles.](https://docs-assets.developer.apple.com/published/799bc8a8022ff1325319b50e2bc24231/image-buttons-macos@2x.png)

**Use an image button in a view, not in the window frame.** For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See [Toolbars](/design/human-interface-guidelines/toolbars)
.

**Include about 10 pixels of padding between the edges of the image and the button edges.** An image button’s edges define its clickable area even when they aren’t visible. Including padding ensures that a click registers correctly even if it’s not precisely within the image. In general, avoid including a system-provided border in an image button; for developer guidance, see [`isBordered`](/documentation/appkit/nsbutton/1525565-isbordered)
.

**If you need to include a label, position it below the image button.** For related guidance, see [Labels](/design/human-interface-guidelines/labels)
.

### [visionOS](/design/human-interface-guidelines/buttons#visionOS)

An visionOS button typically includes a visible background that can help people see it, and the button plays sound to provide feedback when people interact with it.

 [Play](#) 
visionOS defines three standard button shapes, each of which supports the following types of labels.



| Shape | Icon only | Text only | Icon and text |
| --- | --- | --- | --- |
| Circular | A checkmark denoting availability. |  |  |
| Pill |  | A checkmark denoting availability. | A checkmark denoting availability. |
| Rounded rectangle |  | A checkmark denoting availability. |  |

visionOS buttons use a different visual style to communicate each of the following interaction states:

* Idle
* Hover
* Selected
* Selected toggle
* Unavailable

In addition to the five states listed above, circular buttons can also reveal a tooltip when people look at the button for a brief time. In contrast, buttons that contain text don’t display a tooltip because the button’s descriptive label communicates what it does.

 [Play](#) 
visionOS provides buttons in several sizes, depending on shape and contents.



| Shape | Mini (28 pt) | Small (32 pt) | Standard (44 pt) | Large (52 pt) | XL (64 pt) |
| --- | --- | --- | --- | --- | --- |
| Circular | A checkmark denoting availability. | A checkmark denoting availability. | A checkmark denoting availability. | A checkmark denoting availability. | A checkmark denoting availability. |
| Pill (text only) |  | A checkmark denoting availability. | A checkmark denoting availability. | A checkmark denoting availability. |  |
| Pill (text and icon) |  |  | A checkmark denoting availability. | A checkmark denoting availability. |  |
| Rounded rectangle |  | A checkmark denoting availability. | A checkmark denoting availability. | A checkmark denoting availability. |  |

**Prefer buttons that have a discernible background shape and fill.** It tends to be easier for people to see a button when it’s enclosed in a shape that uses a contrasting background fill. The exception is a button in a toolbar, context menu, alert, or [ornament](/design/human-interface-guidelines/ornaments)
 where the shape and material of the larger component make the button comfortably visible. The following guidelines can help you ensure that a button looks good in different contexts:

* When a button appears on top of a glass [window](/design/human-interface-guidelines/windows#visionOS)
, use a light material in the button’s background.
* When a button appears floating in space, use the [glass material](/design/human-interface-guidelines/materials#visionOS)
 for its background.

**Avoid creating a custom button that uses a white background fill and black text or icons.** The system reserves this visual style to convey the selected toggle state.

**In general, prefer circular or pill-shape buttons.** People’s eyes tend to be drawn toward the corners in a shape, making it difficult to keep looking at the shape’s center. The more rounded a button’s shape, the easier it is for people to bring focus to it. When you need to display a button by itself, prefer a pill-shape button.

**Provide enough space around a button to make it easy for people to bring focus to it.** To help make focusing comfortable, place buttons so their centers are always at least 60 points apart. If your buttons are 60 points or larger, add four points of padding around them to keep the hover effect from overlapping. Also, it’s usually best to avoid displaying small or mini buttons in a vertical stack or horizontal row.

**Choose the right shape if you need to display text-labeled buttons in a stack or row.** Specifically, prefer the rounded-rectangle shape in a vertical stack of buttons and prefer the pill shape in a horizontal row of buttons.

**Design feedback sounds for custom buttons.** visionOS doesn’t play haptics, so it’s important to provide audible feedback for interactions with custom buttons.

### [watchOS](/design/human-interface-guidelines/buttons#watchOS)

watchOS displays all buttons using the [`capsule`](/documentation/SwiftUI/ButtonBorderShape/capsule)
 button shape. In watchOS 10, the buttons are larger and have material backgrounds that adapt to underlying content to ensure legibility.

![An illustration that represents a screen on Apple Watch, which includes capsule-shaped Primary and Secondary buttons.](https://docs-assets.developer.apple.com/published/8bf040bdd7aefb683943471f12ca3f26/button-watch@2x.png)

**Use the [toolbar](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars)
 to place buttons in the corners.** The system automatically moves the time and title to accommodate toolbar buttons.

![An illustration showing toolbar buttons in the top leading and trailing corners, as well as three toolbar buttons across the bottom of the screen.](https://docs-assets.developer.apple.com/published/5107ebed76f98c154a803845ad4c7a60/button-watch-corners@2x.png)

Toolbar buttons automatically inherit the app’s tint color. Only change the tint color when you need to convey important information, such as when a button performs a destructive action.

**Prefer buttons that span the width of the screen for primary actions in your app.** Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button’s content.

**Use toolbar buttons to provide either navigation to related areas or contextual actions for the view’s content.** These buttons provide access to additional information or secondary actions for the view’s content.

**Use the same height for vertical stacks of one- and two-line text buttons.** As much as possible, use identical button heights for visual consistency.

[Resources](/design/human-interface-guidelines/buttons#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/buttons#Related)

[Pop-up buttons](/design/human-interface-guidelines/pop-up-buttons)


[Pull-down buttons](/design/human-interface-guidelines/pull-down-buttons)


[Toggles](/design/human-interface-guidelines/toggles)


[Segmented controls](/design/human-interface-guidelines/segmented-controls)


[Location button](/design/human-interface-guidelines/privacy#Location-button)


#### [Developer documentation](/design/human-interface-guidelines/buttons#Developer-documentation)

[`Button`](/documentation/SwiftUI/Button)


[`UIButton`](/documentation/uikit/uibutton)


[`NSButton`](/documentation/appkit/nsbutton)


#### [Videos](/design/human-interface-guidelines/buttons#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/4445FCE4-AF6C-435D-BEF8-7A5A73D51270/4954_wide_250x141_1x.jpg) Meet the UIKit button system](https://developer.apple.com/videos/play/wwdc2021/10064) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/9CCE8A5D-A751-441C-B88F-FB91E2D1958E/4949_wide_250x141_1x.jpg) What's new in UIKit](https://developer.apple.com/videos/play/wwdc2021/10059) 
[Change log](/design/human-interface-guidelines/buttons#Change-log)
-------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using buttons in watchOS. |


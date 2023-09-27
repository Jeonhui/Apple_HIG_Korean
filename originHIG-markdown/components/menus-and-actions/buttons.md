# **[components-menus-and-actions] buttons**

## A button initiates an instantaneous action.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/buttons-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/buttons-intro-dark_2x.png)

Versatile and highly customizable, buttons give people simple, familiar ways to do tasks in your app. In general, a button combines three attributes to clearly communicate its function:

- **Style.** A visual style based on size, color, and shape.
- **Content.** The symbol (or interface icon), text label, or both that a button displays to convey its purpose.
- **Role.** A system-defined role that identifies a button’s semantic meaning and can affect its appearance.

In addition to all-purpose buttons, many common button styles — like Info, Close, and Contact Add — enable familiar behaviors throughout the system. There are also many button-like components that have distinct appearances and behaviors for specific use cases, like [toggles](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles), [pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pop-up-buttons), and [segmented controls](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls).

# **Best practices**

When buttons are instantly recognizable and easy to understand, an app tends to feel intuitive and well designed.

**Make buttons easy for people to choose.** On a touchscreen, buttons need a hit target of at least 44x44 points to accommodate a fingertip. On all screens, it’s essential to include enough space around a button so that people can visually distinguish it from surrounding components and content, whether people use touch, a pointer, or a system that expands a button when it’s in focus.

**Ensure that each button clearly communicates it purpose.** A button always includes a text label or a symbol (or interface icon) — and sometimes a combination of both — to help people predict what it does.

# **Style**

System buttons offer a range of styles that support extensive customization while providing built-in interaction states, accessibility support, and appearance adaptation.

iOS and iPadOS have four button styles, each available in three sizes. Each combination of size and style has a different level of visual prominence, helping you present hierarchies of actions within your app.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-sizes-styles-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-sizes-styles-dark_2x.png)

You can configure a system button to use any combination of style and size. By default, a system button uses a size-specific corner radius and your app’s accent color. If necessary, you can change these attributes — in addition to attributes that control content layout and the presence of an activity indicator — in your button configuration.

**Use a filled button for the most likely action in a view.** The filled style is the most visually prominent, so it helps people quickly identify the action they’re most likely to want. At the same time, avoid using too many filled buttons in a view. Too many filled buttons can increase cognitive load because people must spend time comparing multiple likely options before making a choice.

**Use style — not size — to visually distinguish the preferred choice among multiple options.** When you use buttons of the same size to offer two or more options, you signal that the options form a coherent set of choices. If you want to highlight the preferred or most likely option in a set, use a more prominent button style for that option and a less prominent style for the remaining ones.

# **Content**

**Create button content that helps people instantly understand what the button does.** If an interface icon makes sense in your button, consider using an existing or customized [SF Symbol](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/). To use text, create a short label that succinctly describes what the button does. Using [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64), consider starting the label with a verb to help convey the button’s action — for example, a button that lets people add items to their shopping cart might use the label “Add to Cart.”

**Include additional text below the label only if it provides useful details.**Additional text uses a smaller text size than the label, showing that the information is secondary to the button’s action. For example, you might add text to update an Add to Cart button with the number of items in the cart. Avoid writing a subtitle that explains more about what the button does; make sure a button’s containing view, label or image, style, and role provide all the information people need to understand its action.

**Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.**Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different label alongside the activity indicator. For example, the label “Checkout” could change to “Checking out...” while the activity indicator is visible. When a delay occurs after people click or tap your configured button, the system displays the activity indicator next to the original or alternative label, hiding the button image, if there is one.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-visible_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-visible_2x.png)

# **Role**

A system button can have one of the following roles:

- **Normal.** No specific meaning.
- **Primary.** The button is the default button — the button people are most likely to choose.
- **Cancel.** The button cancels the current action.
- **Destructive.** The button performs an action that can result in data destruction.

A button’s role can have additional effects on the appearance you configure. For example, the system uses bold text for the label in a primary button, whereas a destructive button uses a red color.

**Assign the primary role to the button people are most likely to choose.**When a primary button responds to the Return key, it makes it easy for people to quickly confirm their choice. In addition, when the button is in a temporary view — like a [sheet](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets), an editable view, or an [alert](https://developer.apple.com/design/human-interface-guidelines/components/presentation/alerts) — assigning it the primary role means that the view can automatically close when people press Return.

**Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice.** Because of its visual prominence, people sometimes choose a primary button without reading it first. Help people avoid losing content by assigning the primary role to nondestructive buttons.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, or tvOS.*

# **macOS**

Several specific button types are unique to macOS.

### **Push buttons**

The standard button type in macOS is known as a *push button*. You can configure a push button to display text, a symbol, an interface icon, or an image, or a combination of text and image content. Push buttons can act as the default button in a view and you can tint them.

**Use a flexible-height push button only when you need to display tall or variable height content.** Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button that contains two lines of text or a tall icon, use a flexible-height button; otherwise, use a standard push button. For developer guidance, see [NSBezelStyleRegularSquare](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyleregularsquare/).

**Append a trailing ellipsis to the title when a push button opens another window, view, or app.** Throughout the system, an ellipsis in a control title signals that people can provide additional input. For example, the Edit buttons in the AutoFill pane of Safari Settings include ellipses because they open other views that let people modify autofill values.

**Consider enabling spring loading.** On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can continue dragging the items, possibly to perform additional actions.

### **Gradient buttons**

A gradient button initiates an action related to a view, like adding or removing rows in a table.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/gradient-buttons-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/gradient-buttons-macos_2x.png)

Gradient buttons contain symbols or interface icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear in close proximity to their associated view — usually within or beneath it — so people know which view the buttons affect.

**Use gradient buttons in a view, not in the window frame.** Gradient buttons aren’t intended for use in toolbars or status bars. If you need a button in a [toolbar](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars), use a toolbar item.

**Prefer using a symbol in a gradient button.** [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.

**Avoid using labels to introduce gradient buttons.** Because gradient buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.

For developer guidance, see [NSBezelStyleSmallSquare](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstylesmallsquare/).

### **Help buttons**

A help button appears within a view and opens app-specific help documentation.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/help-buttons-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/help-buttons-macos_2x.png)

Help buttons are circular, consistently sized buttons that contain a question mark. For guidance on creating help documentation, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/patterns/offering-help).

**Use the system-provided help button to display your help documentation.** People are familiar with the appearance of the standard help button and know that choosing it opens help content.

**When possible, open the help topic that’s related to the current context.** For example, the help button in the Rules pane of Mail settings opens the Mail User Guide to a help topic that explains how to change these settings. If no specific help topic applies directly to the current context, open the top level of your app’s help documentation when people choose a help button.

**Include no more than one help button per window.** Multiple help buttons in the same context make it hard for people to predict the result of clicking one.

**Position help buttons where people expect to find them.** Use the following locations for guidance.

| View style | Help button location |
| --- | --- |
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

**Use a help button within a view, not in the window frame.** For example, avoid placing a help button in a toolbar or status bar.

**Avoid displaying text that introduces a help button.** People know what a help button does, so they don’t need additional descriptive text.

### **Image buttons**

An image button appears in a view and displays an image, symbol, or interface icon. You can configure an image button to behave like a push button, toggle, or pop-up button.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/image-buttons-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/image-buttons-macos_2x.png)

**Use an image button in a view, not in the window frame.** For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See [Toolbars](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars).

**Include about 10 pixels of padding between the edges of the image and the button edges.** An image button’s edges define its clickable area even when they aren’t visible. Including padding ensures that a click registers correctly even if it’s not precisely within the image. In general, avoid including a system-provided border in an image button; for developer guidance, see [isBordered](https://developer.apple.com/documentation/appkit/nsbutton/1525565-isbordered/).

**If you need to include a label, position it below the image button.** For related guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels).

# **watchOS**

**Prefer buttons that span the width of the screen.** Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button’s content.

**Use the same height for vertical stacks of one- and two-line text buttons.** As much as possible, use identical button heights for visual consistency.

**Use the system-defined corner radius.** The system defines corner radius values that provide a consistent visual style across apps and reinforce the interactivity of buttons. In Apple Watch Series 4 and later, corner radius values differ depending on whether the button is in a scrolling or nonscrolling view.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-pinned-watchos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-pinned-watchos_2x.png)

In nonscrolling views, buttons use a 22-point corner radius.

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-scroll-view-watchos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-scroll-view-watchos_2x.png)

In scrolling views, buttons use a 9-point corner radius.
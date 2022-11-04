# **[components-layout-and-organization] labels**

## A label is a static piece of text that people can read and often copy, but not edit.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/label-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/label-intro-dark_2x.png)

Labels display text throughout the interface, in buttons, menu items, and views, helping people understand the current context and what they can do next.

The term *label* refers to uneditable text that can appear in various places. For example:

- Within a button, a label generally conveys what the button does, such as Edit, Cancel, or Send.
- Within many lists, a label can describe each item, often accompanied by a symbol or an image.
- Within a view, a label might provide additional context by introducing a control or describing a common action or task that people can perform in the view.

**DEVELOPER NOTE**To display uneditable text, SwiftUI defines two components: [Label](https://developer.apple.com/documentation/swiftui/label) and [Text](https://developer.apple.com/documentation/swiftui/text).

The guidance below can help you use a label to display text. In some cases, guidance for specific components — such as [buttons](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons), [menus](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus), and [lists](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lists-and-tables) — includes additional recommendations for using text.

# **Best practices**

**Use a label to display a small amount of text that people don’t need to edit.** If you need to let people edit a small amount of text, use a [text field](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields). If you need to display a large amount of text, and optionally let people edit it, use a [text view](https://developer.apple.com/design/human-interface-guidelines/components/content/text-views).

**Prefer system fonts.** A label can display plain or styled text, and it supports Dynamic Type (where available) by default. If you adjust the style of a label or use custom fonts, make sure the text remains legible.

**Use system-provided label colors to communicate relative importance.**The system defines four label colors that vary in appearance to help you give text different levels of visual importance. For additional guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/foundations/color).

| System color | Example usage | iOS, iPadOS, tvOS | macOS |
| --- | --- | --- | --- |
| Label | Primary information | labelColor | labelColor |
| Secondary label | A subheading or supplemental text | secondaryLabelColor | secondaryLabelColor |
| Tertiary label | Text that describes an unavailable item or behavior | tertiaryLabelColor | tertiaryLabelColor |
| Quaternary label | Watermark text | quaternaryLabelColor | quaternaryLabelColor |

**Make useful label text selectable.** If a label contains useful information — like an error message, a location, or an IP address — consider letting people select and copy it for pasting elsewhere.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, or tvOS.*

# **macOS**

**DEVELOPER NOTE**To display uneditable text in a label, use the [isEditable](https://developer.apple.com/documentation/appkit/nstextfield/1399407-iseditable) property of [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield).

# **watchOS**

In addition to using SwiftUI [Label](https://developer.apple.com/documentation/swiftui/label) and [Text](https://developer.apple.com/documentation/swiftui/text) components in your watchOS app, you can use WatchKit date and timer labels to display real-time values.

A [date label](https://developer.apple.com/documentation/watchkit/wkinterfacedate) (shown below on the left) displays the current date, the current time, or a combination of both. You can configure a date label to use a variety of formats, calendars, and time zones. After configuration, a date label updates its value without further input from your app. A [timer label](https://developer.apple.com/documentation/watchkit/wkinterfacetimer) (shown below on the right) displays a precise countdown or count-up timer. You can configure a timer label to display its count value in a variety of formats. After configuration, a timer label counts down or up without further input from your app.

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-mail_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-mail_2x.png)

Date label

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-stopwatch_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels/images/dates-timers-stopwatch_2x.png)

Timer label

**Consider using date and timer labels in complications.** When you use the system-provided date and timer labels, watchOS automatically adjusts the presentation of the label content to fit the available space. For guidance, see [Complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications); for developer guidance, see [CLKRelativeDateTextProvider](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider).
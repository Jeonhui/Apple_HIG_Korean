June 5, 2023

 Updated guidance to reflect changes in watchOS 10. Labels
======

A label is a static piece of text that people can read and often copy, but not edit.![A stylized representation of a text label. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/b428963465f223dd1fdd01779043810c/components-label-intro@2x.png)

Labels display text throughout the interface, in buttons, menu items, and views, helping people understand the current context and what they can do next.

The term *label* refers to uneditable text that can appear in various places. For example:

* Within a button, a label generally conveys what the button does, such as Edit, Cancel, or Send.
* Within many lists, a label can describe each item, often accompanied by a symbol or an image.
* Within a view, a label might provide additional context by introducing a control or describing a common action or task that people can perform in the view.

Developer note

To display uneditable text, SwiftUI defines two components: [`Label`](/documentation/SwiftUI/Label)
 and [`Text`](/documentation/SwiftUI/Text)
.

The guidance below can help you use a label to display text. In some cases, guidance for specific components — such as [action buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
, [menus](https://developer.apple.com/design/human-interface-guidelines/menus)
, and [lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)
 — includes additional recommendations for using text.

[Best practices](/design/human-interface-guidelines/labels#Best-practices)
--------------------------------------------------------------------------

**Use a label to display a small amount of text that people don’t need to edit.** If you need to let people edit a small amount of text, use a [text field](https://developer.apple.com/design/human-interface-guidelines/text-fields)
. If you need to display a large amount of text, and optionally let people edit it, use a [text view](https://developer.apple.com/design/human-interface-guidelines/text-views)
.

**Prefer system fonts.** A label can display plain or styled text, and it supports Dynamic Type (where available) by default. If you adjust the style of a label or use custom fonts, make sure the text remains legible.

**Use system-provided label colors to communicate relative importance.** The system defines four label colors that vary in appearance to help you give text different levels of visual importance. For additional guidance, see [Color](/design/human-interface-guidelines/color)
.



| System color | Example usage | iOS, iPadOS, tvOS | macOS |
| --- | --- | --- | --- |
| Label | Primary information | [`labelColor`](/documentation/uikit/uicolor/3173131-labelcolor)
 | [`labelColor`](/documentation/appkit/nscolor/1534657-labelcolor)
 |
| Secondary label | A subheading or supplemental text | [`secondaryLabelColor`](/documentation/uikit/uicolor/3173136-secondarylabelcolor)
 | [`secondaryLabelColor`](/documentation/appkit/nscolor/1533254-secondarylabelcolor)
 |
| Tertiary label | Text that describes an unavailable item or behavior | [`tertiaryLabelColor`](/documentation/uikit/uicolor/3173153-tertiarylabelcolor)
 | [`tertiaryLabelColor`](/documentation/appkit/nscolor/1532376-tertiarylabelcolor)
 |
| Quaternary label | Watermark text | [`quaternaryLabelColor`](/documentation/uikit/uicolor/3173135-quaternarylabelcolor)
 | [`quaternaryLabelColor`](/documentation/appkit/nscolor/1534635-quaternarylabelcolor)
 |

**Make useful label text selectable.** If a label contains useful information — like an error message, a location, or an IP address — consider letting people select and copy it for pasting elsewhere.

[Platform considerations](/design/human-interface-guidelines/labels#Platform-considerations)
--------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, tvOS, or visionOS.*

### [macOS](/design/human-interface-guidelines/labels#macOS)

Developer note

To display uneditable text in a label, use the [`isEditable`](/documentation/appkit/nstextfield/1399407-iseditable)
 property of [`NSTextField`](/documentation/appkit/nstextfield)
.

### [watchOS](/design/human-interface-guidelines/labels#watchOS)

Date and time text components (shown below on the left) display the current date, the current time, or a combination of both. You can configure a date text component to use a variety of formats, calendars, and time zones. A countdown timer text component (shown below on the right) displays a precise countdown or count-up timer. You can configure a timer text component to display its count value in a variety of formats.

![An illustration that represents a Mail message on Apple Watch, highlighted to show a date aligned to the leading edge of the screen and a time aligned to the trailing edge.](https://docs-assets.developer.apple.com/published/6b38ed52f948cf00b56ad92ebfc065f5/dates-timers-mail@2x.png)Date label![An illustration that represents the Stopwatch app's Digital screen on Apple Watch, highlighted to show the current time value centered at the top of the screen, just below the status bar.](https://docs-assets.developer.apple.com/published/c460013d30240d5e4ce7ca5826f7a901/dates-timers-stopwatch@2x.png)Timer labelWhen you use the system-provided date and timer text components, watchOS automatically adjusts the label’s presentation to fit the available space. The system also updates the content without further input from your app.

Consider using date and timer components in complications. For design guidance, see [Complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications)
; for developer guidance, see [`Text`](/documentation/SwiftUI/Text)
.

[Resources](/design/human-interface-guidelines/labels#Resources)
----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/labels#Related)

[Text fields](/design/human-interface-guidelines/text-fields)


[Text views](/design/human-interface-guidelines/text-views)


#### [Developer documentation](/design/human-interface-guidelines/labels#Developer-documentation)

[`Label`](/documentation/SwiftUI/Label)


[`Text`](/documentation/SwiftUI/Text)


[`UILabel`](/documentation/uikit/uilabel)


[`NSTextField`](/documentation/appkit/nstextfield)


[Change log](/design/human-interface-guidelines/labels#Change-log)
------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |


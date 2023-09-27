# **[content] text-views**

## A text view displays multiline, styled text content, which can optionally be editable.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/text-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/text-view-intro-dark_2x.png)

Text views can be any height and enable scrolling when the content extends outside of the view. By default, content within a text view is aligned to the leading edge and uses the system label color. In iOS or iPadOS, if a text view is editable, a keyboard appears when people select the view.

# **Best practices**

**Use a text view when you need to display text that’s long, editable, or in a special format.** Text views differ from [text fields](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields) and [labels](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels) in that they provide the most options for displaying specialized text and receiving text input. If you need to display a small amount of text, it’s simpler to use a label instead or a text field if the text is editable.

**Keep text legible.** Although you can use multiple fonts, colors, and alignments in creative ways, it’s essential to maintain the readability of your content. It’s a good idea to adopt Dynamic Type so your text still looks good if people change text size on their device. You should also test your content with accessibility options enabled, such as bold text. For guidance, see [Accessibility](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility) and [Typography](https://developer.apple.com/design/human-interface-guidelines/foundations/typography).

**Make useful text selectable.** If a text view contains useful information such as an error message, a serial number, or an IP address, consider letting people select and copy it for pasting elsewhere.

# **Platform considerations**

*No additional considerations for macOS.*

# **iOS, iPadOS**

**Show the appropriate keyboard type.** Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view should be appropriate for the type of content. For guidance, see [Onscreen keyboards](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards).

# **tvOS**

You can display text in tvOS using a text view. Because text input in tvOS is minimal by design, tvOS uses [text fields](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields) for editable text instead.

# **watchOS**

You can display text in watchOS either as a label in WatchKit or with a text view in SwiftUI. For guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels).
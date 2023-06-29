# **[components-selection-and-input] pickers**

## A picker displays one or more scrollable lists of distinct values that people can choose from.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/pickers-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/pickers-intro-dark_2x.png)

The system provides several styles of pickers, each of which offers different types of selectable values and has a different appearance. The exact values shown in a picker, and their order, depend on the device language.

Pickers help people enter information by letting them choose single or multipart values. Date pickers specifically offer additional ways to choose values, like selecting a day in a calendar view or entering dates and times using a numeric keypad.

# **Best practices**

**Consider using a picker to offer medium-to-long lists of items.** If you need to display a fairly short list of choices, consider using a [pull-down button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pull-down-buttons) instead of a picker. Although a picker makes it easy to scroll quickly through many items, it may add too much visual weight to a short list of items. On the other hand, if you need to present a very large set of items, consider using a [list or table](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lists-and-tables). Lists and tables can adjust in height, and tables can include an index, which makes it much faster to target a section of the list.

**Use predictable and logically ordered values.** Many values in a picker may be hidden before people interact with it. It’s best when people can predict what the hidden values are, such as with an alphabetized list of countries, so they can move through the items quickly.

**Avoid switching screens to show a picker.** A picker works well when displayed in context, below or in proximity to the field being edited. A picker typically appears at the bottom of the screen or in a popover.

**Consider providing less granularity when specifying minutes in a date picker.** By default, a minute list includes 60 values (0 to 59). You can optionally increase the minute interval as long as it divides evenly into 60. For example, you might want quarter-hour intervals (0, 15, 30, and 45).

# **Platform considerations**

# **iOS, iPadOS**

A date picker is an efficient interface for selecting a specific date, time, or both, using touch, a keyboard, or a pointing device. You can display a date picker in one of the following styles:

- Compact — A button that displays editable date and time content in a modal view.
- Inline — For time only, a button that displays wheels of values; for dates and times, an inline calendar view.
- Wheels — A set of scrolling wheels that also supports data entry through built-in or external keyboards.
- Automatic — A system-determined style based on the current platform and date picker mode.

A date picker has four modes, each of which presents a different set of selectable values.

- Date — Displays months, days of the month, and years.
- Time — Displays hours, minutes, and (optionally) an AM/PM designation.
- Date and time — Displays dates, hours, minutes, and (optionally) an AM/PM designation.
- Countdown timer — Displays hours and minutes, up to a maximum of 23 hours and 59 minutes. This mode isn’t available in the inline or compact styles.

The exact values shown in a date picker, and their order, depend on the device location.

Here are several examples of date pickers showing different combinations of style and mode.

• [Compact](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers#)
• [Inline](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers#)
• [Wheels](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-closed_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-closed_2x.png)

Scheduled summary settings uses a compact date picker in time mode.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-open_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-open_2x.png)

When people tap the date picker, it reveals time values within a modal view.


**Use a compact date picker when space is constrained.** The compact style displays a button that shows the current value in your app’s accent color. When people tap the button, the date picker opens a modal view, providing access to a familiar calendar-style editor and time picker. Within the modal view, people can make multiple edits to dates and times before tapping outside the view to confirm their choices.

# **macOS**

**Choose a date picker style that suits your app.** There are two styles of date pickers in macOS: textual and graphical. The textual style is useful when you’re working with limited space and you expect people to make specific date and time selections. The graphical style is useful when you want to give people the option of browsing through days in a calendar or selecting a range of dates, or when the look of a clock face is appropriate for your app.

For developer guidance, see [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker).

# **tvOS**

Pickers are available in tvOS with SwiftUI. For developer guidance, see [Picker](https://developer.apple.com/documentation/swiftui/picker).

# **watchOS**

Pickers display lists of items that people navigate using the Digital Crown, which enables a precise and engaging way to manage selections.

Pickers present their items in the following styles.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-list_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-list_2x.png)

**List picker.** Displays text and images in a scrolling list. In addition to the selected item, a list picker shows the previous and next items when they're available.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-stack_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-stack_2x.png)

**Stack picker.**Displays images in a card stack interface. As people scroll, images animate into position with the selected image on top.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-sequence_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-sequence_2x.png)

**Sequence picker.**Displays one image from a sequence of images. As people turn the Digital Crown, the picker displays the previous or next image in the sequence without animations.

You can configure a picker to display an outline, caption, and scrolling indicator. These elements help identify the picker onscreen and help people navigate its contents.

**Use captions to clarify the meaning of items or of the picker itself.** You can assign unique captions to an item if it helps to clarify its meaning. Alternatively, you can assign the same caption to all items to clarify the purpose of the picker itself.

**Display a scroll indicator when the total number of items might not be obvious.** A scroll indicator reflects the total number of items in a picker and indicates the current position within the list. A scroll indicator is unnecessary when the sequence and number of items is obvious, such as when specifying the number of seconds for a timer.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-scroller_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-scroller_2x.png)
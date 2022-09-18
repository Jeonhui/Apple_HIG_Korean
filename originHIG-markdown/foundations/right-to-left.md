# **[foundations] right-to-left**

### Support right-to-left languages like Arabic and Hebrew by reversing your interface as needed to match the reading direction of the related scripts.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-rtl-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-rtl-intro-dark_2x.png)

When people choose a language for their device — or just your app or game — they expect the interface to adapt in various ways (to learn more, see [Localization](https://developer.apple.com/localization/)).

System-provided UI frameworks support right-to-left (RTL) by default, enabling system-provided UI components to flip automatically in the RTL context. If you use system-provided elements and standard layouts, you might not need to make any changes to your app’s automatically reversed interface.

If you want to fine-tune your layout or enhance specific localizations to adapt to different currencies, numerals, or mathematical symbols that can occur in various locales in countries that use RTL languages, follow these guidelines.

# **Text alignment**

**Adjust text alignment to match the interface direction, if the system doesn’t do so automatically.** For example, if you left-align text with content in the left-to-right (LTR) context, right-align the text to match the content’s mirrored position in the RTL context.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-ltr-screen-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-ltr-screen-dark_2x.png)

Left-aligned text in the LTR context

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-rtl-screen-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/text-alignment-rtl-screen-dark_2x.png)

Right-aligned content in the RTL context

**Align a paragraph based on its language, not on the current context.** When the alignment of a paragraph — defined as three or more lines of text — doesn’t match its language, it can be difficult to read. For example, right-aligning a paragraph that consists of LTR text can make the beginning of each line difficult to see. To improve readability, continue aligning one- and two-line text blocks to match the reading direction of the current context, but align a paragraph to match its language.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-correct-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-correct-dark_2x.png)

A left-aligned paragraph in the RTL context

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-wrong-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/paragraph-alignment-wrong-dark_2x.png)

A right-aligned paragraph in the RTL context

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Use a consistent alignment for all text items in a list.** To ensure a comfortable reading and scanning experience, reverse the alignment of all items in a list, including items that are displayed in a different script.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-correct_2x.png)

Right-aligned content in the RTL context

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-wrong_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mixed-script-list-alignment-wrong_2x.png)

Mixed alignment in the RTL content

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

# **Numbers and characters**

Different RTL languages can use different number systems. For example, Hebrew text uses Western Arabic numerals, whereas Arabic text might use either Western or Eastern Arabic numerals. The use of Western and Eastern Arabic numerals varies among countries and regions and even among areas within the same country or region.

If your app focuses on mathematical concepts or other number-centric topics, it’s a good idea to identify the appropriate way to display such information in each locale you support. In contrast, apps that don’t focus on number-related topics can generally rely on system-provided number representations.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123_2x.png)

Western Arabic numerals

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123-ar_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/textformat-123-ar_2x.png)

Eastern Arabic numerals

**Don’t reverse the order of numerals in a specific number.** Regardless of the current language or the surrounding content, the digits in a specific number — such as “541,” a phone number, or a credit card number — always appear in the same order.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/latin-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/latin-numerals-dark_2x.png)

Latin

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/hebrew-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/hebrew-numerals-dark_2x.png)

Hebrew

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/western-arabic-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/western-arabic-numerals-dark_2x.png)

Arabic (Western Arabic numerals)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/eastern-arabic-numerals-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/eastern-arabic-numerals-dark_2x.png)

Arabic (Eastern Arabic numerals)

**Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves.** Controls like progress bars, sliders, and rating controls often include numerals to clarify their meaning. If you use numerals in this way, be sure to reverse the order of the numerals to match the direction of the flipped control. Also reverse a sequence of numerals if you use the sequence to communicate a specific order.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-latin-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-latin-dark_2x.png)

Latin

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-eastern-arabic-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-eastern-arabic-dark_2x.png)

Arabic (Eastern Arabic numerals)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-hebrew-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-hebrew-dark_2x.png)

Hebrew

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-western-arabic-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/match-numeral-order-to-directional-controls-western-arabic-dark_2x.png)

Arabic (Western Arabic numerals)

# **Controls**

**Flip controls that show progress from one value to another.** Because people tend to view forward progress as moving in the same direction as the language they read, it makes sense to flip controls like sliders and progress indicators in the RTL context. When you do this, also be sure to reverse the positions of the accompanying glyphs or images that depict the beginning and ending values of the control.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-ltr_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-ltr_2x.png)

Directional controls in the LTR context

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-rtl_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/flipped-directional-control-rtl_2x.png)

Directional controls in the RTL context

**Flip controls that help people navigate or access items in a fixed order.** For example, in the RTL context, a back button must point to the right so the flow of screens matches the reading order of the RTL language. Similarly, next or previous buttons that let people access items in an ordered list need to flip in the RTL context to match the reading order.

**Preserve the direction of a control that refers to an actual direction or points to an onscreen area.** For example, if you provide a control that means “to the right,” it must always point right, regardless of the current context.

**Visually balance adjacent Latin and RTL scripts when necessary.** In buttons, labels, and titles, Arabic or Hebrew text can appear too small when next to uppercased Latin text, because Arabic and Hebrew don’t include uppercase letters. To visually balance Arabic or Hebrew text with Latin text that uses all capitals, it often works well to increase the RTL font size by about 2 points.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-uneven-vertical-height_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-uneven-vertical-height_2x.png)

Arabic and Hebrew text can look too small next to uppercased Latin text of the same font size.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-even-vertical-height_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/download-even-vertical-height_2x.png)

You can slightly increase the font size of Arabic and Hebrew text to visually balance uppercased Latin text.

# **Images**

**Avoid flipping images like photographs, illustrations, and general artwork.** Flipping an image often changes the image’s meaning; flipping a copyrighted image could be a violation. If an image’s content is strongly connected to reading direction, consider creating a new version of the image instead of flipping the original.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-right_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-right_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-wrong_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-displayed-wrong_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Reverse the positions of images when their order is meaningful.** For example, if you display multiple images in a specific order like chronological, alphabetical, or favorite, reverse their positions to preserve the order’s meaning in the RTL context.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-ltr_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-ltr_2x.png)

Items with meaningful positions in the LTR context

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-rtl_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/image-positions-rtl_2x.png)

Items with meaningful positions in the RTL context

# **Interface icons**

When you use [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) to supply interface icons for your app, you get variants for the RTL context and localized symbols for Arabic and Hebrew, among other languages. If you create custom symbols, you can specify their directionality. For developer guidance, see [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/uiimage/creating_custom_symbol_images_for_your_app).

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-dark.svg)

LTR variants of directional symbols

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/list-bullet-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/book-closed-fill-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/rectangle-and-pencil-and-ellipsis-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/macwindow-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/battery-25-rtl-dark.svg)

RTL variants of directional symbols

**Flip interface icons that represent text or reading direction.** For example, if an interface icon uses left-aligned bars to represent text in the LTR context, right-align the bars in the RTL context.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-dark.svg)

LTR variant of a symbol that represents text

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-plaintext-rtl-dark.svg)

RTL variant of a symbol that represents text

**Consider creating a localized version of an interface icon that displays text.** Some interface icons include letters or words to help communicate a script-related concept, like font-size choice or a signature. If you have a custom interface icon that needs to display actual text, consider creating a localized version. For example, SF Symbols offers different versions of the signature, rich-text, and I-beam pointer symbols for use with Latin, Hebrew, and Arabic text, among others.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-dark.svg)

Latin

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-he-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-he-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-he-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-he-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-he-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-he-dark.svg)

Hebrew

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-ar-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/signature-ar-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-ar-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/doc-richtext-ar-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-ar-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/character-cursor-ibeam-ar-dark.svg)

Arabic

If you have a custom interface icon that uses letters or words to communicate a concept unrelated to reading or writing, consider designing an alternative image that doesn’t use text.

**Flip an interface icon that shows forward or backward motion.** When something moves in the same direction that people read, they typically interpret that direction as forward; when something moves in the opposite direction, people tend to interpret the direction as backward. An interface icon that depicts an object moving forward or backward needs to flip in the RTL context to preserve the meaning of the motion. For example, an icon that represents a speaker typically shows sound waves emanating forward from the speaker. In the LTR context, the sound waves come from the left, so in the RTL context, the icon needs to flip to show the waves coming from the right.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-wave-3.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-wave-3.svg)

LTR variant of a symbol that depicts forward motion

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-wave-3-rtl.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-wave-3-rtl.svg)

RTL variant of a symbol that depicts forward motion

**Don’t flip logos or universal signs and marks.** Displaying a flipped logo confuses people and can have legal repercussions. Always display a logo in its original form, even if it includes text. People expect universal symbols and marks like the checkmark to have a consistent appearance, so avoid flipping them.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/appletv-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/appletv-dark.svg)

A logo

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/checkmark-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/checkmark-dark.svg)

A universal symbol or mark

**In general, avoid flipping interface icons that depict real-world objects.** Unless you use the object to indicate directionality, it’s best to avoid flipping an icon that represents a familiar item. For example, clocks work the same everywhere, so a traditional clock interface icon needs to look the same regardless of language direction. Some interface icons might seem to reference language or reading direction because they represent items that are slanted for right-handed use. However, most people are right-handed, so flipping an icon that shows a right-handed tool isn’t necessary and might be confusing.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/clock-fill-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/clock-fill-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/pencil-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/pencil-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/gamecontroller-fill-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/gamecontroller-fill-dark.svg)

Glyphs that represent physical objects don’t generally need to flip.

**Before merely flipping a complex custom interface icon, consider its individual components and the overall visual balance.** In some cases, a component — like a badge, slash, or magnifying glass — needs to adhere to a visual design language regardless of localization. For example, SF Symbols maintains visual consistency by using the same backslash to represent the prohibition or negation of a symbol’s meaning in both LTR and RTL versions.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-slash-fill-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-slash-fill-dark.svg)

LTR variant of a symbol that includes a backslash

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-slash-fill-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/speaker-slash-fill-rtl-dark.svg)

RTL variant of a symbol that includes a backslash

In other cases, you might need to flip a component (or its position) to ensure the localized version of the icon still makes sense. For example, if a badge represents the actual UI that people see in your app, it needs to flip if your UI flips. Alternatively, if a badge modifies the meaning of an interface icon, consider whether flipping the badge preserves both the modified meaning and the overall visual balance of the icon.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/cart-fill-badge-plus-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/cart-fill-badge-plus-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/cart-fill-badge-rtl-unbalanced-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/cart-fill-badge-rtl-unbalanced-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/cart-fill-badge-plus-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/cart-fill-badge-plus-rtl-dark.svg)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

The badge doesn’t depict an object in the UI, but keeping it in the top-right corner visually unbalances the cart.

If your custom interface icon includes a component that can imply handedness, like a tool, consider preserving the orientation of the tool while flipping the base image if necessary.

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mail-and-text-magnifyingglass-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mail-and-text-magnifyingglass-dark.svg)

LTR variant of a symbol that depicts a tool

![https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mail-and-text-magnifyingglass-rtl-dark.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/images/mail-and-text-magnifyingglass-rtl-dark.svg)

RTL variant of a symbol that depicts a tool

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*
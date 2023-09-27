# **[components-selection-and-input] onscreen-keyboards**

## In iOS, iPadOS, and tvOS, the system provides various types of onscreen keyboards people can use to enter data.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/keyboard-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/keyboard-intro-dark_2x.png)

An onscreen keyboard can provide a specific set of keys that are optimized for the current task; for example, a keyboard that supports entering email addresses can include the “@” character and a period or even “.com”. An onscreen keyboard doesn’t enable keyboard shortcuts.

When it makes sense in your app, you can replace the system-provided keyboard with a custom view that enables app-specific data entry. You can also create an app extension that offers a custom keyboard people can install and use in place of the standard keyboard.

# **Best practices**

**Match the onscreen keyboard to the type of content people are editing.**For example, you can help people enter numeric data by providing the numbers and punctuation keyboard. When you specify a semantic meaning for a text input area, the system can automatically provide a keyboard that matches the type of input you expect, potentially using this information to refine the keyboard corrections it offers. For developer guidance, see [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) and [UITextContentType](https://developer.apple.com/documentation/uikit/uitextcontenttype).

- **Alphabet**

  ![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/alphabet_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/alphabet_2x.png)

- [Alphabet](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [ASCII Capable](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [ASCII Capable Number Pad](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Decimal Pad](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Default](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Email Address](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Name Phone Pad](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Number Pad](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Numbers and Punctuation](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Phone Pad](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Twitter](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [URL](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)
- [Web Search](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#)

**Consider customizing the Return key label if it helps clarify the text-entry experience.** For example, it might make sense to use “Join” or “Done” instead of “Return.” For developer guidance, see [UIReturnKeyType](https://developer.apple.com/documentation/uikit/uireturnkeytype).

# **Custom input views**

You can create an input view if you want to provide custom functionality that enhances data-entry tasks in your app. For example, Numbers provides a custom input view for entering numeric values while editing a spreadsheet. A custom input view replaces the system-provided keyboard while people are in your app. For developer guidance, see [inputViewController](https://developer.apple.com/documentation/uikit/uiresponder/1621117-inputviewcontroller). If you want to create a [custom keyboard](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#custom-keyboards) that people can use in other apps as well as yours, you need to create an app extension that people can install.

**Make sure your custom input view makes sense in the context of your app.** In addition to making data entry simple and intuitive, you want people to understand the benefits of using your custom input view. Otherwise, they may wonder why they can’t regain the system keyboard while in your app.

**Play the standard keyboard sound while people type.** The keyboard sound provides familiar feedback when people tap a key on the system keyboard, so they’re likely to expect the same sound when they tap keys in your custom input view. People can turn keyboard clicks off for all keyboard interactions in Settings > Sounds. For developer guidance, see [playInputClick](https://developer.apple.com/documentation/uikit/uidevice/1620050-playinputclick).

**Consider providing a custom input accessory view.** An input accessory view can appear above an onscreen keyboard — whether standard or custom — providing app-specific functionality related to the data people are working with. For example, Numbers displays an input accessory view that helps people enter standard or custom calculations to apply to spreadsheet data. Avoid using an accessory view to display content that isn’t relevant to the current task. For developer guidance, see [inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/1621119-inputaccessoryview).

# **Custom keyboards**

You can provide a custom keyboard that replaces the system keyboard by creating an app extension. An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/).

After people enable your custom keyboard in Settings, they can use it for text entry within any app, except when editing secure text fields and phone number fields. People can enable multiple custom keyboards and switch between them at any time. For developer guidance, see [Creating a custom keyboard](https://developer.apple.com/documentation/uikit/keyboards_and_input/creating_a_custom_keyboard).

Custom keyboards make sense when you want to expose unique keyboard functionality systemwide, such as a novel way of inputting text or the ability to type in a language the system doesn’t support. If you want to provide a custom keyboard for people to use only while they're in your app, consider creating a [custom input view](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#custom-input-views) instead.

**Provide an obvious and easy way to switch between keyboards.** People know that the Globe key on the standard keyboard — which replaces the Emoji key when multiple keyboards are enabled — quickly switches to other keyboards, and they expect a similarly intuitive experience in your keyboard.

**Avoid duplicating system-provided keyboard features.** On some devices, the Emoji/Globe key and Dictation key automatically appear beneath the keyboard, even when people are using custom keyboards. Your app can't affect these keys, and it's likely to be confusing if you repeat them in your keyboard.

**Consider providing a keyboard tutorial in your app.** People are used to the standard keyboard, and learning how to use a new keyboard can take time. You can help make the process easier by providing usage instructions in your app — for example, you might tell people how to enable your keyboard, activate it during text entry, use it, and switch back to the standard keyboard. Avoid displaying help content within the keyboard itself.

# **Platform considerations**

*Not supported in macOS or watchOS.*

# **iOS, iPadOS**

**Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.** Using the layout guide also helps you keep important parts of your interface visible while the keyboard is onscreen. For guidance, see [iOS keyboard layout guide](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/#ios-keyboard-layout-guide).

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/ui-fully-visible_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/ui-fully-visible_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

When you use the keyboard layout guide, app UI and the keyboard work well together.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/text-field-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/text-field-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

If you don’t use the keyboard layout guide, the keyboard might obscure UI, such as a text field...

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/button-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/button-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

...or a button.

# **watchOS**

On Apple Watch, people can launch the Apple Continuity Keyboard, entering text from a nearby iOS device signed in to the same iCloud account.

# **tvOS**

tvOS displays a linear onscreen keyboard when people select a text field using the Siri Remote.

**NOTE**A grid keyboard screen appears when people use devices other than the Siri Remote, and the layout of content automatically adapts to the keyboard.

When people activate a digit entry view, tvOS displays a digit-specific keyboard. For guidance, see [Digit entry views](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/digit-entry-views).
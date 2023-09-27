June 21, 2023

 Changed page title from Onscreen keyboards and updated to include guidance for visionOS. Virtual keyboards
=================

In iOS, iPadOS, tvOS, and visionOS, the system provides various types of virtual keyboards people can use to enter data.![A stylized representation of a numeric keypad shown on top of a grid that suggests the canvas of a design tool. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/cbfe3793eff04e91313c24eb211e5cf9/components-virtual-keyboard-intro@2x.png)

A virtual keyboard can provide a specific set of keys that are optimized for the current task; for example, a keyboard that supports entering email addresses can include the “@” character and a period or even “.com”. A virtual keyboard doesn’t support keyboard shortcuts.

When it makes sense in your app, you can replace the system-provided keyboard with a custom view that supports app-specific data entry. In iOS, iPadOS, and tvOS, you can also create an app extension that offers a custom keyboard people can install and use in place of the standard keyboard.

[Best practices](/design/human-interface-guidelines/virtual-keyboards#Best-practices)
-------------------------------------------------------------------------------------

**Choose a keyboard that matches the type of content people are editing.** For example, you can help people enter numeric data by providing the numbers and punctuation keyboard. When you specify a semantic meaning for a text input area, the system can automatically provide a keyboard that matches the type of input you expect, potentially using this information to refine the keyboard corrections it offers. For developer guidance, see [`UIKeyboardType`](/documentation/uikit/uikeyboardtype)
 and [`UITextContentType`](/documentation/uikit/uitextcontenttype)
.

* [Alphabet](#)
* [ASCII capable](#)
* [ASCII capable number pad](#)
* [Decimal pad](#)
* [Default](#)
* [Email address](#)
* [Name phone pad](#)
* [Number pad](#)
* [Numbers and punctuation](#)
* [Phone pad](#)
* [Twitter](#)
* [URL](#)
* [Web search](#)
![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, Space, and Return keys. Typing suggestions appear above the keyboard and the Dictation button appears below it.](https://docs-assets.developer.apple.com/published/ed54b8ef6680b6185f4f2f5bbb45388d/alphabet@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, Space, and Return keys. Typing suggestions appear above the keyboard and the Dictation button appears below it.](https://docs-assets.developer.apple.com/published/69ce2451c45c55f5da8654f29efcf74a/ascii-capable@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 10 number keys in addition to the Delete key. Keys for the numbers 2 through 9 each include the 3 or 4 letters associated with the number on a phone.](https://docs-assets.developer.apple.com/published/7e2dacab57f3cafef65654114f76060c/ascii-capable-number-pad@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 10 number keys in addition to the Delete and period keys. Keys for the numbers 2 through 9 each include the 3 or 4 letters associated with the number on a phone.](https://docs-assets.developer.apple.com/published/027140c4a08f5990e73e31e882baa9d5/decimal-pad@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, Space, and Return keys. Typing suggestions appear above the keyboard and the  Emoji and Dictation buttons appear below it.](https://docs-assets.developer.apple.com/published/94e607265b9dba19e346b11aec6cc8d5/default@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, Space, period, at symbol, and Return keys. Typing suggestions appear above the keyboard and the Emoji button appears below it.](https://docs-assets.developer.apple.com/published/a8c3fa7689f4fcf39a79effc1f5269de/email-address@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, Space, and Return keys. Typing suggestions appear above the keyboard and the Emoji and Dictation buttons appear below it.](https://docs-assets.developer.apple.com/published/3bd3c5a0c73b6ba3d0983466ab52b102/name-phone-pad@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 10 number keys in addition to the Delete key. Keys for the numbers 2 through 9 each include the 3 or 4 letters associated with the number on a phone.](https://docs-assets.developer.apple.com/published/6325e27cbae3ae710f779a96286a0367/number-pad@2x.png)![A partial screenshot of a keyboard on iPhone that displays 10 number and 15 punctuation keys in addition to the secondary punctuation key and the Delete, Letters, Space, and Return keys. Typing suggestions appear above the keyboard and the Dictation button appears below it.](https://docs-assets.developer.apple.com/published/51f3258d5460cff13f16d867510a1b51/numbers-and-punctuation@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 10 number keys in addition to the Delete key and a key for plus, star, and hash. Keys for the numbers 2 through 9 each include the 3 or 4 letters associated with the number on a phone.](https://docs-assets.developer.apple.com/published/532836f8d0351d296b5c013f57771e5c/phone-pad@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, Space, at symbol, and hash keys. Typing suggestions appear above the keyboard and the Emoji and Dictation buttons appear below it.](https://docs-assets.developer.apple.com/published/c4ac1982404f0be78774ab560ffee1b2/twitter@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, period, slash, dot com, and Return keys. Typing suggestions appear above the keyboard and the Emoji button appears below it.](https://docs-assets.developer.apple.com/published/7390bbfaa3dc40cae7b7da99004a7ff8/url@2x.png)![A partial screenshot of a keyboard on iPhone that displays all 26 letter keys in addition to the Shift, Delete, Numbers, Space, period, and Go keys. Typing suggestions appear above the keyboard and the Emoji and Dictation buttons appear below it.](https://docs-assets.developer.apple.com/published/0a7081d7294ad6764e839c31c56954fc/web-search@2x.png)**Consider customizing the Return key label if it helps clarify the text-entry experience.** For example, it might make sense to use “Join” or “Done” instead of “Return.” For developer guidance, see [`UIReturnKeyType`](/documentation/uikit/uireturnkeytype)
.

[Custom input views](/design/human-interface-guidelines/virtual-keyboards#Custom-input-views)
---------------------------------------------------------------------------------------------

In some cases, you can create an *input view* if you want to provide custom functionality that enhances data-entry tasks in your app. For example, Numbers provides a custom input view for entering numeric values while editing a spreadsheet. A custom input view replaces the system-provided keyboard while people are in your app. For developer guidance, see [`inputViewController`](/documentation/uikit/uiresponder/1621117-inputviewcontroller)
. If you want to create a [custom keyboard](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards#Custom-keyboards)
 that people can use in other apps as well as yours, you need to create an app extension that people can install.

**Make sure your custom input view makes sense in the context of your app.** In addition to making data entry simple and intuitive, you want people to understand the benefits of using your custom input view. Otherwise, they may wonder why they can’t regain the system keyboard while in your app.

**Play the standard keyboard sound while people type.** The keyboard sound provides familiar feedback when people tap a key on the system keyboard, so they’re likely to expect the same sound when they tap keys in your custom input view. People can turn keyboard sounds off for all keyboard interactions in Settings > Sounds. For developer guidance, see [`playInputClick()`](/documentation/uikit/uidevice/1620050-playinputclick)
.

**Consider providing a custom input accessory view.** An *input accessory view* can appear above a virtual keyboard — whether standard or custom — providing app-specific functionality related to the data people are working with. For example, Numbers displays an input accessory view that helps people enter standard or custom calculations to apply to spreadsheet data. Avoid using an accessory view to display content that isn’t relevant to the current task. For developer guidance, see [`inputAccessoryView`](/documentation/uikit/uiresponder/1621119-inputaccessoryview)
.

[Custom keyboards](/design/human-interface-guidelines/virtual-keyboards#Custom-keyboards)
-----------------------------------------------------------------------------------------

In iOS, iPadOS, and tvOS, you can provide a custom keyboard that replaces the system keyboard by creating an app extension. An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/)
.

After people choose your custom keyboard in Settings, they can use it for text entry within any app, except when editing secure text fields and phone number fields. People can choose multiple custom keyboards and switch between them at any time. For developer guidance, see [Creating a custom keyboard](/documentation/uikit/keyboards_and_input/creating_a_custom_keyboard)
.

Custom keyboards make sense when you want to expose unique keyboard functionality systemwide, such as a novel way of inputting text or the ability to type in a language the system doesn’t support. If you want to provide a custom keyboard for people to use only while they’re in your app, consider creating a [custom input view](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards#Custom-input-views)
 instead.

**Provide an obvious and easy way to switch between keyboards.** People know that the Globe key on the standard keyboard — which replaces the Emoji key when multiple keyboards are available — quickly switches to other keyboards, and they expect a similarly intuitive experience in your keyboard.

**Avoid duplicating system-provided keyboard features.** On some devices, the Emoji/Globe key and Dictation key automatically appear beneath the keyboard, even when people are using custom keyboards. Your app can’t affect these keys, and it’s likely to be confusing if you repeat them in your keyboard.

**Consider providing a keyboard tutorial in your app.** People are used to the standard keyboard, and learning how to use a new keyboard can take time. You can help make the process easier by providing usage instructions in your app — for example, you might tell people how to choose your keyboard, activate it during text entry, use it, and switch back to the standard keyboard. Avoid displaying help content within the keyboard itself.

[Platform considerations](/design/human-interface-guidelines/virtual-keyboards#Platform-considerations)
-------------------------------------------------------------------------------------------------------

*Not supported in macOS or watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/virtual-keyboards#iOS-iPadOS)

**Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.** Using the layout guide also helps you keep important parts of your interface visible while the virtual keyboard is onscreen. For guidance, see [iOS keyboard layout guide](/design/human-interface-guidelines/layout#iOS-keyboard-layout-guide)
.

![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard.](https://docs-assets.developer.apple.com/published/f51b04a89c12a3a3fc4b106b0a7dca49/ui-fully-visible@2x.png)

![A checkmark in a circle to indicate a correct example.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)The keyboard layout guide helps ensure that app UI and the keyboard work well together.![An illustration of an app layout on iPhone, showing two stacked text fields. The keyboard covers part of the bottom text field.](https://docs-assets.developer.apple.com/published/1d03dce9daac0d7bba163dea6109583c/text-field-hidden@2x.png)

![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)Without the layout guide, the keyboard could make entering text more difficult.![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard. The keyboard covers part of the button.](https://docs-assets.developer.apple.com/published/796daa3daefc5adafa23f1b0348b6107/button-hidden@2x.png)

![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)Without the layout guide, the keyboard could make tapping a button more difficult.### [tvOS](/design/human-interface-guidelines/virtual-keyboards#tvOS)

tvOS displays a linear virtual keyboard when people select a text field using the Siri Remote.

Note

A grid keyboard screen appears when people use devices other than the Siri Remote, and the layout of content automatically adapts to the keyboard.

When people activate a digit entry view, tvOS displays a digit-specific keyboard. For guidance, see [Digit entry views](/design/human-interface-guidelines/digit-entry-views)
.

### [visionOS](/design/human-interface-guidelines/virtual-keyboards#visionOS)

In visionOS, the system-provided virtual keyboard appears in a separate window that people can move where they want. You don’t need to account for the location of the keyboard in your layouts.

### [watchOS](/design/human-interface-guidelines/virtual-keyboards#watchOS)

On Apple Watch, people can launch the Apple Continuity Keyboard, entering text from a nearby iOS device signed in to the same iCloud account.

[Resources](/design/human-interface-guidelines/virtual-keyboards#Resources)
---------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/virtual-keyboards#Related)

[Entering data](/design/human-interface-guidelines/entering-data)


[Keyboards](/design/human-interface-guidelines/keyboards)


[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/virtual-keyboards#Developer-documentation)

[`UIKeyboardType`](/documentation/uikit/uikeyboardtype)


#### [Videos](/design/human-interface-guidelines/virtual-keyboards#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_1x.jpg) Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 
[Change log](/design/human-interface-guidelines/virtual-keyboards#Change-log)
-----------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Changed page title from Onscreen keyboards and updated to include guidance for visionOS. |


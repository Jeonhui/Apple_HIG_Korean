# **[components-selection-and-input] onscreen-keyboards**

## In iOS, iPadOS, and tvOS, the system provides various types of onscreen keyboards people can use to enter data.
> iOS, 아이패드 OS, TV OS에서 이 시스템은 사람들이 데이터를 입력하는 데 사용할 수 있는 다양한 종류의 온스크린 키보드를 제공한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/keyboard-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/keyboard-intro-dark_2x.png)

An onscreen keyboard can provide a specific set of keys that are optimized for the current task; for example, a keyboard that supports entering email addresses can include the “@” character and a period or even “.com”. An onscreen keyboard doesn’t enable keyboard shortcuts.
> 화면 키보드는 현재 작업에 최적화된 특정 키 집합을 제공할 수 있습니다. 예를 들어 전자 메일 주소 입력을 지원하는 키보드에는 "@" 문자와 마침표 또는 .com이 포함될 수 있습니다. 화면 키보드에서는 바로 가기 키를 사용할 수 없습니다.
>




When it makes sense in your app, you can replace the system-provided keyboard with a custom view that enables app-specific data entry. You can also create an app extension that offers a custom keyboard people can install and use in place of the standard keyboard.
> 앱에서 사용할 수 있으면 시스템에서 제공하는 키보드를 앱별 데이터 입력을 가능하게 하는 사용자 지정 보기로 바꿀 수 있습니다. 표준 키보드 대신 사용자가 설치하고 사용할 수 있는 사용자 지정 키보드를 제공하는 앱 확장을 만들 수도 있습니다.
>




# **Best practices**

**Match the onscreen keyboard to the type of content people are editing.**For example, you can help people enter numeric data by providing the numbers and punctuation keyboard. When you specify a semantic meaning for a text input area, the system can automatically provide a keyboard that matches the type of input you expect, potentially using this information to refine the keyboard corrections it offers. For developer guidance, see [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) and [UITextContentType](https://developer.apple.com/documentation/uikit/uitextcontenttype).
> 사용자가 편집 중인 내용 유형에 화면 키보드를 일치시킵니다.예를 들어, 숫자와 구두점 키보드를 제공하여 사람들이 숫자 데이터를 입력하는 것을 도울 수 있습니다. 텍스트 입력 영역에 의미적 의미를 지정하면 시스템이 자동으로 예상되는 입력 유형과 일치하는 키보드를 제공할 수 있으며, 이 정보를 사용하여 제공하는 키보드 수정을 구체화할 수 있습니다. 개발자 지침은 UIKeyboardType 및 UITextContentType을 참조하십시오.
>




- **Alphabet**

![../components/selection-and-input/onscreen-keyboards/images/alphabet_2x.png](../components/selection-and-input/onscreen-keyboards/images/alphabet_2x.png)

- [Alphabet](../components/selection-and-input/onscreen-keyboards#)
- [ASCII Capable](../components/selection-and-input/onscreen-keyboards#)
- [ASCII Capable Number Pad](../components/selection-and-input/onscreen-keyboards#)
- [Decimal Pad](../components/selection-and-input/onscreen-keyboards#)
- [Default](../components/selection-and-input/onscreen-keyboards#)
- [Email Address](../components/selection-and-input/onscreen-keyboards#)
- [Name Phone Pad](../components/selection-and-input/onscreen-keyboards#)
- [Number Pad](../components/selection-and-input/onscreen-keyboards#)
- [Numbers and Punctuation](../components/selection-and-input/onscreen-keyboards#)
- [Phone Pad](../components/selection-and-input/onscreen-keyboards#)
- [Twitter](../components/selection-and-input/onscreen-keyboards#)
- [URL](../components/selection-and-input/onscreen-keyboards#)
- [Web Search](../components/selection-and-input/onscreen-keyboards#)

**Consider customizing the Return key label if it helps clarify the text-entry experience.** For example, it might make sense to use “Join” or “Done” instead of “Return.” For developer guidance, see [UIReturnKeyType](https://developer.apple.com/documentation/uikit/uireturnkeytype).
> 텍스트 입력 환경을 명확히 하는 데 도움이 되는 경우 Return 키 레이블을 사용자 정의하는 것이 좋습니다. 예를 들어, "Return" 대신 "Join" 또는 "Done"을 사용하는 것이 적절할 수 있습니다. 개발자 지침은 UIRurnKeyType을 참조하십시오.
>




# **Custom input views**

You can create an input view if you want to provide custom functionality that enhances data-entry tasks in your app. For example, Numbers provides a custom input view for entering numeric values while editing a spreadsheet. A custom input view replaces the system-provided keyboard while people are in your app. For developer guidance, see [inputViewController](https://developer.apple.com/documentation/uikit/uiresponder/1621117-inputviewcontroller). If you want to create a [custom keyboard](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#custom-keyboards) that people can use in other apps as well as yours, you need to create an app extension that people can install.
> 앱에서 데이터 입력 작업을 향상시키는 사용자 지정 기능을 제공하려면 입력 보기를 만들 수 있습니다. 예를 들어, 숫자는 스프레드시트를 편집하는 동안 숫자 값을 입력하기 위한 사용자 지정 입력 보기를 제공합니다. 사용자 지정 입력 보기는 사용자가 앱에 있는 동안 시스템에서 제공한 키보드를 대체합니다. 개발자 지침은 입력ViewController를 참조하십시오. 사용자의 앱뿐만 아니라 다른 앱에서도 사용할 수 있는 사용자 지정 키보드를 만들려면 사용자가 설치할 수 있는 앱 확장을 만들어야 합니다.
>




**Make sure your custom input view makes sense in the context of your app.** In addition to making data entry simple and intuitive, you want people to understand the benefits of using your custom input view. Otherwise, they may wonder why they can’t regain the system keyboard while in your app.
> 사용자 지정 입력 보기가 앱의 맥락에서 의미가 있는지 확인하십시오. 데이터 입력을 단순하고 직관적으로 만드는 것 외에도 사용자 지정 입력 보기를 사용할 때의 이점을 사람들이 이해하기를 원할 수 있습니다. 그렇지 않으면 앱에 있는 동안 시스템 키보드를 되찾을 수 없는 이유를 궁금해할 수 있습니다.
>




**Play the standard keyboard sound while people type.** The keyboard sound provides familiar feedback when people tap a key on the system keyboard, so they’re likely to expect the same sound when they tap keys in your custom input view. People can turn keyboard clicks off for all keyboard interactions in Settings > Sounds. For developer guidance, see [playInputClick](https://developer.apple.com/documentation/uikit/uidevice/1620050-playinputclick).
> 키보드 소리는 사용자가 시스템 키보드에서 키를 누를 때 익숙한 피드백을 제공하므로 사용자 지정 입력 보기에서 키를 누를 때도 같은 소리가 날 수 있습니다. 설정 > 소리에서 모든 키보드 상호 작용에 대한 키보드 클릭을 끌 수 있습니다. 개발자 지침은 playInputClick을 참조하십시오.
>




**Consider providing a custom input accessory view.** An input accessory view can appear above an onscreen keyboard — whether standard or custom — providing app-specific functionality related to the data people are working with. For example, Numbers displays an input accessory view that helps people enter standard or custom calculations to apply to spreadsheet data. Avoid using an accessory view to display content that isn’t relevant to the current task. For developer guidance, see [inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/1621119-inputaccessoryview).
> 사용자 지정 입력 액세서리 보기를 제공하는 것을 고려해 보십시오. 입력 액세서리 보기는 표준 또는 사용자 지정 키보드 위에 나타나 사용자가 작업 중인 데이터와 관련된 앱별 기능을 제공할 수 있습니다. 예를 들어, 숫자는 사용자가 스프레드시트 데이터에 적용할 표준 또는 사용자 정의 계산을 입력하는 데 도움이 되는 입력 보조프로그램 보기를 표시합니다. 보조 보기를 사용하여 현재 작업과 관련 없는 내용을 표시하지 않도록 합니다. 개발자 지침은 입력 보조프로그램 보기를 참조하십시오.
>




# **Custom keyboards**

You can provide a custom keyboard that replaces the system keyboard by creating an app extension. An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/).
> 앱 확장을 만들어 시스템 키보드를 대체하는 사용자 지정 키보드를 제공할 수 있습니다. 앱 확장은 사용자가 시스템의 특정 영역의 기능을 확장하기 위해 설치하고 사용할 수 있는 코드입니다. 자세한 내용은 앱 확장을 참조하십시오.
>




After people enable your custom keyboard in Settings, they can use it for text entry within any app, except when editing secure text fields and phone number fields. People can enable multiple custom keyboards and switch between them at any time. For developer guidance, see [Creating a custom keyboard](https://developer.apple.com/documentation/uikit/keyboards_and_input/creating_a_custom_keyboard).
> 설정에서 사용자 지정 키보드를 활성화한 후 보안 텍스트 필드 및 전화 번호 필드를 편집하는 경우를 제외하고는 앱 내의 텍스트 입력에 사용할 수 있습니다. 사용자는 여러 개의 사용자 지정 키보드를 사용할 수 있으며 언제든지 키보드 간에 전환할 수 있습니다. 개발자 지침은 사용자 지정 키보드 만들기를 참조하십시오.
>




Custom keyboards make sense when you want to expose unique keyboard functionality systemwide, such as a novel way of inputting text or the ability to type in a language the system doesn’t support. If you want to provide a custom keyboard for people to use only while they're in your app, consider creating a [custom input view](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards#custom-input-views) instead.
> 사용자 지정 키보드는 텍스트를 입력하는 새로운 방법이나 시스템에서 지원하지 않는 언어를 입력하는 기능과 같은 고유한 키보드 기능을 시스템 전체에 노출하려는 경우에 적합합니다. 사용자가 앱에 있는 동안에만 사용할 수 있는 사용자 지정 키보드를 제공하려면 대신 사용자 지정 입력 보기를 만드는 것을 고려해 보십시오.
>




**Provide an obvious and easy way to switch between keyboards.** People know that the Globe key on the standard keyboard — which replaces the Emoji key when multiple keyboards are enabled — quickly switches to other keyboards, and they expect a similarly intuitive experience in your keyboard.
> 표준 키보드의 Globe 키(여러 키보드가 활성화된 경우 Emoji 키를 대체함)가 다른 키보드로 빠르게 전환되고 키보드에서도 이와 유사한 직관적인 경험을 기대할 수 있습니다.
>




**Avoid duplicating system-provided keyboard features.** On some devices, the Emoji/Globe key and Dictation key automatically appear beneath the keyboard, even when people are using custom keyboards. Your app can't affect these keys, and it's likely to be confusing if you repeat them in your keyboard.
> 일부 장치에서는 사용자 지정 키보드를 사용하는 경우에도 Emoji/Globe 키와 Dictation 키가 키보드 아래에 자동으로 나타납니다. 앱은 이러한 키에 영향을 줄 수 없으며 키보드에서 이를 반복하면 혼동될 수 있습니다.
>




**Consider providing a keyboard tutorial in your app.** People are used to the standard keyboard, and learning how to use a new keyboard can take time. You can help make the process easier by providing usage instructions in your app — for example, you might tell people how to enable your keyboard, activate it during text entry, use it, and switch back to the standard keyboard. Avoid displaying help content within the keyboard itself.
> 앱에서 키보드 튜토리얼을 제공하는 것을 고려해 보십시오. 사람들은 표준 키보드에 익숙하며 새로운 키보드 사용 방법을 배우는 데 시간이 걸릴 수 있습니다. 예를 들어 키보드를 활성화하고, 텍스트 입력 중에 활성화하고, 사용하고, 표준 키보드로 다시 전환하는 방법을 다른 사람에게 알려주는 등의 사용 지침을 앱에 제공하여 프로세스를 더 쉽게 만들 수 있습니다. 키보드 자체 내에 도움말 내용이 표시되지 않도록 합니다.
>




# **Platform considerations**

*Not supported in macOS or watchOS.*
> macOS 또는 watch에서 지원되지 않음운영 체제
>




# **iOS, iPadOS**

**Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.** Using the layout guide also helps you keep important parts of your interface visible while the keyboard is onscreen. For guidance, see [iOS keyboard layout guide](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/#ios-keyboard-layout-guide).
> 키보드 레이아웃 가이드를 사용하면 키보드가 인터페이스의 통합된 부분처럼 느껴집니다. 레이아웃 가이드를 사용하면 키보드가 화면에 표시되는 동안 인터페이스의 중요한 부분을 계속 볼 수 있습니다. 자세한 내용은 iOS 키보드 레이아웃 가이드를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/ui-fully-visible_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/ui-fully-visible_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

When you use the keyboard layout guide, app UI and the keyboard work well together.
> 키보드 레이아웃 가이드를 사용하면 앱 UI와 키보드가 잘 연동된다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/text-field-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/text-field-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

If you don’t use the keyboard layout guide, the keyboard might obscure UI, such as a text field...
> 키보드 레이아웃 가이드를 사용하지 않으면 키보드가 텍스트 필드와 같은 UI를 흐리게 할 수 있습니다...
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/button-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards/images/button-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

...or a button.

# **watchOS**

On Apple Watch, people can launch the Apple Continuity Keyboard, entering text from a nearby iOS device signed in to the same iCloud account.
> 애플 워치에서 사람들은 애플 컨티뉴이티 키보드를 시작할 수 있으며, 가까운 iOS 기기의 텍스트를 동일한 아이클라우드 계정에 입력할 수 있다.
>




# **tvOS**

tvOS displays a linear onscreen keyboard when people select a text field using the Siri Remote.
> TVOS는 사람들이 Siri 리모컨을 사용하여 텍스트 필드를 선택할 때 화면에 선형 키보드를 표시합니다.
>




**NOTE**A grid keyboard screen appears when people use devices other than the Siri Remote, and the layout of content automatically adapts to the keyboard.
> 참고 사람들이 Siri Remote 이외의 장치를 사용할 때 그리드 키보드 화면이 나타나고 콘텐츠 레이아웃이 키보드에 자동으로 적용됩니다.
>




When people activate a digit entry view, tvOS displays a digit-specific keyboard. For guidance, see [Digit entry views](../components/selection-and-input/digit-entry-views).
> 사람들이 숫자 입력 보기를 활성화하면 TVOS는 숫자별 키보드를 표시합니다. 자세한 내용은 숫자 입력 보기를 참조하십시오.
>




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





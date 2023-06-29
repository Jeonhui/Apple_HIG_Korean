# **[patterns] entering-data**

# When you need information from people, design ways that make it easy for them to provide it without making mistakes.
> 사람들의 정보가 필요할 때, 그들이 실수하지 않고 쉽게 제공할 수 있는 방법을 설계하세요.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-entering-data-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-entering-data-intro-dark_2x.png)

Entering information can be a tedious process regardless of the interaction methods people use. Improve the experience by pre-gathering as much information as possible to minimize the amount of data people need to supply and by supporting all available input methods so people can choose the method that works for them.
> 정보를 입력하는 것은 사람들이 사용하는 상호 작용 방법에 관계없이 지루한 과정이 될 수 있다. 사용자가 제공해야 할 데이터 양을 최소화하기 위해 가능한 많은 정보를 미리 수집하고 사용 가능한 모든 입력 방법을 지원하여 사용자가 자신에게 맞는 방법을 선택할 수 있도록 경험을 개선합니다.
>




# **Best practices**

**Get information from the system whenever possible.** Don’t ask people to provide information that you can gather automatically — such as from settings — or with their permission, such as their location or calendar information.
> 가능할 때마다 시스템에서 정보를 가져옵니다. 설정 등 자동으로 수집할 수 있는 정보나 사용자의 권한(예: 위치 또는 일정관리 정보)을 다른 사람에게 제공하지 마십시오.
>




**Be clear about the data you need.** For example, you might display a prompt in a text field — like “username@company.com” — or provide an introductory label that describes the information, like “Email.” You can also prefill fields with reasonable default values, which can minimize decision making and speed data entry.
> 필요한 데이터에 대해 명확히 합니다. 예를 들어, "username@company.com"과 같은 텍스트 필드에 프롬프트를 표시하거나 "전자 메일"과 같은 정보를 설명하는 소개 레이블을 제공할 수 있습니다. 적절한 기본값을 사용하여 필드를 미리 채울 수도 있으므로 의사 결정을 최소화하고 데이터 입력 속도를 높일 수 있습니다.
>




**Use a secure text-entry field when appropriate.** If your app or game needs sensitive data, use a field that obscures people’s input as they enter it, typically by displaying a small filled circle symbol for each character. For developer guidance, see [SecureField](https://developer.apple.com/documentation/swiftui/securefield). In tvOS, you can also configure a [digit entry view](../components/selection-and-input/digit-entry-views) to obscure the numerals people enter (for developer guidance, see [isSecureDigitEntry](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller/2967056-issecuredigitentry)).
> 적절한 경우 보안 텍스트 입력 필드를 사용합니다. 앱이나 게임에 중요한 데이터가 필요한 경우 일반적으로 각 캐릭터에 대해 채워진 작은 원 기호를 표시하여 입력 시 사용자의 입력을 흐리게 하는 필드를 사용하십시오. 개발자 지침은 SecureField를 참조하십시오. tvOS에서 숫자 입력 보기를 구성하여 사용자가 입력하는 숫자를 숨길 수도 있습니다(개발자 지침은 isSecureDigitEntry 참조).
>




**Never prepopulate a password field.** Always ask people to enter their password or use biometric or keychain authentication. For guidance, see [Managing accounts](../patterns/managing-accounts).
> 암호 필드를 미리 입력하지 마십시오. 항상 사람들에게 암호를 입력하거나 생체 인식 또는 키 체인 인증을 사용하도록 요청하십시오. 자세한 내용은 계정 관리를 참조하십시오.
>




**Dynamically validate field values.** People can get frustrated when they have to go back and correct mistakes after filling out a lengthy form. When you verify values as soon as people enter them — and provide feedback as soon as you detect a problem — you give them the opportunity to correct errors right away. For numeric data in particular, consider using a number formatter, which automatically configures a text field to accept only numeric values. You can also configure a formatter to display the value in a specific way, such as with a certain number of decimal places, as a percentage, or as currency.
> 필드 값을 동적으로 검증합니다. 사람들은 긴 양식을 작성한 후 돌아가서 실수를 바로잡아야 할 때 좌절할 수 있다. 사용자가 값을 입력하는 즉시 값을 확인하고 문제를 발견하는 즉시 피드백을 제공하는 경우 오류를 즉시 수정할 수 있는 기회를 제공합니다. 특히 숫자 데이터의 경우 텍스트 필드를 숫자 값만 허용하도록 자동으로 구성하는 숫자 형식을 사용하는 것을 고려해 보십시오. 특정 소수 자릿수, 백분율 또는 통화와 같은 특정 방법으로 값을 표시하도록 형식 지정자를 구성할 수도 있습니다.
>




**When possible, offer choices instead of requiring text entry.** It’s usually easier and more efficient to choose from lists of options than to type information, even when a keyboard is conveniently available. When it makes sense, consider using a picker, menu, or other selection component to give people an easy way to provide the information you need.
> 가능한 경우 텍스트 입력을 요구하는 대신 선택 사항을 제공합니다. 일반적으로 키보드를 사용할 수 있는 경우에도 정보를 입력하는 것보다 옵션 목록에서 선택하는 것이 더 쉽고 효율적입니다. 이 경우 선택 도구, 메뉴 또는 기타 선택 구성 요소를 사용하여 사용자에게 필요한 정보를 쉽게 제공할 수 있습니다.
>




**As much as possible, let people provide data by dragging and dropping it or by pasting it.** Supporting these interactions can ease data entry and make your experience feel more integrated with the rest of the system.
> 가능한 한 사람들이 데이터를 끌어다 놓거나 붙여넣기를 통해 데이터를 제공하도록 합니다. 이러한 상호 작용을 지원하면 데이터를 쉽게 입력할 수 있고 시스템의 나머지 부분과 더욱 통합되는 느낌을 받을 수 있습니다.
>




**When data is truly required, enable advancement only after collecting it.** Before enabling a Next or Continue button, make sure all required fields have values. When the button becomes enabled, people know that it’s time to proceed.
> 데이터가 정말로 필요한 경우 데이터를 수집한 후에만 고급을 사용하도록 설정합니다. [다음] 또는 [계속] 단추를 활성화하기 전에 모든 필수 필드에 값이 있는지 확인하십시오. 이 버튼이 활성화되면, 사람들은 이 버튼을 계속 진행해야 할 때라는 것을 알게 됩니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, tvOS, or watchOS.*
> iOS, iPadOS, tvOS 또는 시청에 대한 추가 고려 사항 없음OS.
>




# **macOS**

**Consider using an expansion tooltip to show the full version of clipped or truncated text in a field.** An *expansion tooltip* behaves like a *help tag*, appearing when the pointer rests on top of a field. Apps running in macOS — including iOS and iPadOS apps running on a Mac — can use an expansion tooltip to help people view the complete data they entered when a text field is too small to display it. For guidance, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/patterns/offering-help/#macos).
> 필드에 잘라내거나 잘린 텍스트의 전체 버전을 표시하려면 확장 도구 설명을 사용하십시오. 확장 도구 설명은 도움말 태그와 같이 작동하며 포인터가 필드 위에 있을 때 나타납니다. Mac OS에서 실행되는 iOS 및 iPadOS 앱을 포함하여 Mac OS에서 실행되는 앱은 확장 도구 팁을 사용하여 텍스트 필드가 너무 작아서 표시할 수 없을 때 입력한 전체 데이터를 볼 수 있습니다. 자세한 내용은 도움말 제공을 참조하십시오.
>




# **[components-selection-and-input] text-fields**

## A text field is a rectangular area in which people enter or edit small, specific pieces of text.
> 텍스트 필드는 사용자가 특정한 작은 텍스트 조각을 입력하거나 편집하는 직사각형 영역입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/text-field-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/text-field-intro-dark_2x.png)

# **Best practices**

**Use a text field to request a small amount of information, such as a name or an email address.** To let people input larger amounts of text, use a [text view](../components/content/text-views) instead.
> 이름이나 전자 메일 주소와 같은 소량의 정보를 요청하려면 텍스트 필드를 사용하고, 더 많은 양의 텍스트를 입력하려면 텍스트 보기를 사용하십시오.
>




**Show a hint in a text field to help communicate its purpose.** A text field can contain placeholder text — such as "Email" or "Password" — when there’s no other text in the field. Because placeholder text disappears when people start typing, it can also be useful to include a separate label describing the field to remind people of its purpose.
> 텍스트 필드에 다른 텍스트가 없는 경우 텍스트 필드에는 "전자 메일" 또는 "암호"와 같은 자리 표시자 텍스트가 포함될 수 있습니다. 사용자가 입력을 시작하면 자리 표시자 텍스트가 사라지므로 필드를 설명하는 별도의 레이블을 포함하여 사용자에게 해당 용도를 알려주는 것도 유용합니다.
>




**Use secure text fields to hide private data.** Always use a secure text field when your app asks for sensitive data, such as a password. For developer guidance, see [SecureField](https://developer.apple.com/documentation/SwiftUI/SecureField).
> 보안 텍스트 필드를 사용하여 개인 데이터를 숨깁니다. 앱에서 암호와 같은 중요한 데이터를 요청할 때는 항상 보안 텍스트 필드를 사용하십시오. 개발자 지침은 보안 필드를 참조하십시오.
>




**To the extent possible, match the size of a text field to the quantity of anticipated text.** The size of a text field helps people gauge the amount of information to provide.
> 텍스트 필드의 크기를 예상되는 텍스트의 양과 일치시키십시오. 텍스트 필드의 크기는 사람들이 제공할 정보의 양을 측정하는 데 도움이 됩니다.
>




**Evenly space multiple text fields.** If your layout includes multiple text fields, leave enough space between them so people can easily see which input field belongs with each introductory label. Stack multiple text fields vertically when possible, and use consistent widths to create a more organized layout. For instance, the first and last name fields on an address form might be one width, while the address and city fields might be a different width.
> 레이아웃에 여러 텍스트 필드가 포함된 경우, 사용자가 각 소개 레이블에 속한 입력 필드를 쉽게 볼 수 있도록 충분한 간격을 두십시오. 가능한 경우 여러 개의 텍스트 필드를 수직으로 쌓고 일정한 너비를 사용하여 보다 체계적인 레이아웃을 작성합니다. 예를 들어, 주소 양식의 이름 필드와 성 필드는 하나의 너비이지만 주소 필드와 도시 필드는 서로 다른 너비일 수 있습니다.
>




**Ensure that tabbing between multiple fields flows as people expect.**When tabbing between fields, focus should move in a logical sequence. The system attempts to achieve this result automatically, so you won’t need to customize this too often.
> 여러 필드 사이의 탭이 사용자의 예상대로 흐르는지 확인합니다.필드 사이를 탭할 때 포커스는 논리적 순서로 이동해야 합니다. 시스템은 자동으로 이 결과를 얻으려고 하므로 자주 사용자 지정할 필요가 없습니다.
>




**Validate fields when it makes sense.** For example, if the only legitimate value for a field is a string of digits, your app should alert people if they’ve entered characters other than digits. The appropriate time to check the data depends on the context: when entering an email address, it’s best to validate when people change focus; when creating a username or password, validation should happen before the focus switches to another field.
> 필드의 유효성을 확인합니다. 예를 들어, 필드의 합법적인 값이 숫자 문자열뿐인 경우, 앱은 사용자에게 숫자 이외의 문자를 입력했는지 알려주어야 합니다. 데이터를 확인하는 적절한 시간은 상황에 따라 다릅니다. 전자 메일 주소를 입력할 때 사람이 포커스를 변경할 때 확인하는 것이 가장 좋습니다. 사용자 이름 또는 암호를 만들 때는 포커스가 다른 필드로 전환되기 전에 확인이 수행되어야 합니다.
>




**Use a number formatter to help with numeric data.** A number formatter automatically configures the text field to accept only numeric values. It can also display the value in a specific way, such as with a certain number of decimal places, as a percentage, or as currency. Don't assume the actual presentation of data, however, as formatting can vary significantly based on people's locale.
> 숫자 데이터에 도움이 되도록 숫자 형식 지정기를 사용하십시오. 숫자 형식 지정기는 숫자 값만 허용하도록 텍스트 필드를 자동으로 구성합니다. 또한 특정 소수 자릿수, 백분율 또는 통화와 같은 특정 방법으로 값을 표시할 수 있습니다. 그러나 사용자의 로케일에 따라 형식이 크게 달라질 수 있으므로 데이터의 실제 표시는 가정하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-formatted-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-formatted-text_2x.png)

Formatted text

**Adjust line breaks according to the needs of the field.** By default, the system clips any text extending beyond the bounds of a text field. Alternatively, you can set up a text field to wrap text to a new line at the character or word level, or to truncate (indicated by an ellipsis) at the beginning, middle, or end.
> 필드의 필요에 따라 줄 바꿈을 조정합니다. 기본적으로 시스템은 텍스트 필드의 범위를 벗어나는 텍스트를 클리핑합니다. 또는 텍스트 필드를 설정하여 텍스트를 문자 또는 단어 수준의 새 줄로 묶거나 시작, 중간 또는 끝에서 줄임표로 표시되도록 할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-clipped-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-clipped-text_2x.png)

Clipped text

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-wrapped-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-wrapped-text_2x.png)

Wrapped text

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-truncated-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/text-fields/images/text-fields-truncated-text_2x.png)

Truncated text

**Consider using an expansion tooltip to show the full version of clipped or truncated text.** An expansion tooltip behaves like a help tag and appears when the user places the pointer over the field.
> 확장 도구 설명을 사용하여 잘리거나 잘린 텍스트의 전체 버전을 표시하는 것을 고려해 보십시오. 확장 도구 설명은 도움말 태그처럼 작동하며 사용자가 필드 위에 포인터를 놓으면 나타납니다.
>




**In iOS, iPadOS, and tvOS apps, show the appropriate keyboard type.**Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view should be appropriate for the type of content. For guidance, see [Onscreen keyboards](../components/selection-and-input/onscreen-keyboards).
> iOS, iPadOS 및 TVOS 앱에서 적절한 키보드 유형을 표시합니다.여러 키보드 유형을 사용할 수 있으며, 각각 다른 유형의 입력을 용이하게 하도록 설계되었습니다. 데이터 입력을 간소화하려면 텍스트 보기를 편집할 때 표시하는 키보드가 내용 유형에 적합해야 합니다. 자세한 내용은 화면 키보드를 참조하십시오.
>




**Minimize text entry in your tvOS and watchOS apps.** Entering long passages of text or filling out numerous text fields is time-consuming on Apple TV and Apple Watch. Minimize text input and consider gathering information more efficiently, such as with buttons.
> TVOS에서 텍스트 입력 최소화 및 시청OS 앱. 애플 TV와 애플 워치에서 긴 텍스트 구절을 입력하거나 수많은 텍스트 필드를 작성하는 것은 시간이 많이 걸린다. 텍스트 입력을 최소화하고 단추를 사용하는 등 보다 효율적으로 정보를 수집할 수 있습니다.
>




# **Platform considerations**

*No additional considerations for tvOS.*

# **iOS, iPadOS**

**Display a Clear button in the trailing end of a text field to help people erase their input.** When this element is present, people can tap it to clear the text field’s contents, without having to keep tapping the Delete key.
> 입력 내용을 지우는 데 도움이 되도록 텍스트 필드의 끝에 지우기 단추를 표시합니다. 이 요소가 있으면 삭제 키를 계속 누를 필요 없이 텍스트 필드의 내용을 지울 수 있습니다.
>




**Use images and buttons to provide clarity and functionality in text fields.** You can display custom images in both ends of a text field, or you can add a system-provided button, such as the Bookmarks button. In general, use the leading end of a text field to indicate a field’s purpose and the trailing end to offer additional features, such as bookmarking.
> 이미지와 단추를 사용하여 텍스트 필드에서 명확한 정보와 기능을 제공합니다. 텍스트 필드의 양쪽 끝에 사용자 정의 이미지를 표시하거나 책갈피 단추와 같은 시스템 제공 단추를 추가할 수 있습니다. 일반적으로 텍스트 필드의 맨 앞 끝은 필드의 목적을 나타내고 맨 뒤의 끝은 책갈피와 같은 추가 기능을 제공하는 데 사용합니다.
>




# **macOS**

**Consider using a combo box if you need to pair text input with a list of choices.** For related guidance, see [Combo boxes](../components/selection-and-input/combo-boxes).
> 텍스트 입력과 선택 목록을 쌍으로 구성해야 하는 경우 콤보 상자 사용을 고려하십시오. 관련 지침은 콤보 상자를 참조하십시오.
>




# **watchOS**

**Present a text field only when necessary.** As much as possible, prefer letting people enter data by selecting an option from a list, using dictation, or using Scribble. People can also use the Apple Continuity Keyboard to enter text on another nearby device.
> 필요한 경우에만 텍스트 필드를 표시합니다. 목록에서 옵션을 선택하거나 받아쓰기 또는 스크라이브를 사용하여 사용자가 데이터를 입력할 수 있도록 허용하는 것이 좋습니다. 또한 Apple Continuity 키보드를 사용하여 근처에 있는 다른 장치에 텍스트를 입력할 수 있습니다.
>




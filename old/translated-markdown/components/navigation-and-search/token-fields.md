# **[components-navigation-and-search] token-fields**

## A token field is a type of text field that includes *tokens* — blocks of text that people can easily select and manipulate.
> 토큰 필드는 사용자가 쉽게 선택하고 조작할 수 있는 텍스트 블록인 토큰을 포함하는 텍스트 필드의 유형입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/token-field-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/token-field-intro-dark_2x.png)

When composing a new message in Mail, for example, the address fields are token fields. As people enter recipients, the recipients are converted from text into token form. People can select these recipient tokens and drag them to reorder or otherwise work with them individually.
> 예를 들어, 메일에서 새 메시지를 작성할 때 주소 필드는 토큰 필드입니다. 수신인을 입력하면 수신인은 텍스트에서 토큰 형식으로 변환됩니다. 사용자는 이러한 수신인 토큰을 선택하고 끌어서 순서를 변경하거나 개별적으로 작업할 수 있습니다.
>




You can configure a token field to present people with a list of suggested tokens as they enter text into the field. For example, Mail suggests recipients as people type into an address field. If they select a suggested recipient, it’s inserted into the field as a token.
> 사용자가 필드에 텍스트를 입력할 때 제안된 토큰 목록을 사용자에게 표시하도록 토큰 필드를 구성할 수 있습니다. 예를 들어, 메일은 사용자가 주소 필드에 입력할 때 수신인을 제안합니다. 제안된 수신인을 선택하면 해당 수신인은 토큰으로 필드에 삽입됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-suggestion_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-suggestion_2x.png)

An individual token can also include a contextual menu that’s denoted by a downward chevron character. This contextual menu can include information about the token or editing options. In Mail, a recipient token includes a contextual menu with commands for editing the recipient, marking the recipient as a VIP, and viewing the recipient’s contact card, among others.
> 개별 토큰에는 아래쪽 쉐브론 문자로 표시되는 상황별 메뉴도 포함될 수 있습니다. 이 상황에 맞는 메뉴에는 토큰 또는 편집 옵션에 대한 정보가 포함될 수 있습니다. 메일에서 수신인 토큰에는 수신인을 편집하고, 수신인을 VIP로 표시하고, 수신인의 연락처 카드를 보는 등의 명령이 포함된 상황별 메뉴가 포함되어 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-contextual_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-contextual_2x.png)

Some token fields are accompanied by a separate list of available tokens, which people can select and drag into the field. The Language & Region settings pane uses this approach for its date and time format fields, for example. It offers individual date and time tokens that can be dragged into token fields, which people can format using the tokens’ contextual menus.
> 일부 토큰 필드는 사용 가능한 토큰의 별도 목록과 함께 제공되며, 사용자는 이 목록을 선택하여 필드로 끌 수 있습니다. 예를 들어, [언어 및 지역 설정] 영역은 날짜 및 시간 형식 필드에 이 접근방식을 사용합니다. 토큰 필드로 끌어다 놓을 수 있는 개별 날짜 및 시간 토큰을 제공하며, 토큰의 상황에 맞는 메뉴를 사용하여 포맷할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-dates_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-dates_2x.png)

Tokens can also represent search terms in some situations; see [Search fields](../components/navigation-and-search/search-fields).
> 토큰은 경우에 따라 검색어를 나타낼 수도 있습니다. 필드 검색을 참조하십시오.
>




# **Best practices**

**Add value with a context menu.** People often benefit from a [context menu](../components/menus-and-actions/context-menus)with additional options or information about a token.
> 상황에 맞는 메뉴로 가치를 더하세요. 사람들은 종종 토큰에 대한 추가 옵션이나 정보가 있는 상황에 맞는 메뉴로부터 이익을 얻습니다.
>




**Consider providing additional ways to convert text into tokens.** By default, text people enter turns into a token whenever they type a comma. You can specify additional shortcuts, such as return, that should also invoke this action.
> 텍스트를 토큰으로 변환하는 추가 방법을 제공하는 것을 고려하십시오. 기본적으로 사용자가 입력한 텍스트는 쉼표를 입력할 때마다 토큰으로 바뀝니다. 이 작업을 호출할 추가 바로 가기(예: 반환)를 지정할 수 있습니다.
>




**Customize the delay before showing tokens that the system suggests.**Suggestions appear immediately by default. However, suggestions appearing too quickly can be a distraction while typing. If your app suggests tokens, consider adjusting the delay to a comfortable level.
> 시스템에서 제안하는 토큰을 표시하기 전에 지연을 사용자 지정합니다.제안은 기본적으로 즉시 나타납니다. 그러나 제안이 너무 빨리 나타나는 것은 타자를 치는 동안 방해가 될 수 있습니다. 만약 당신의 앱이 토큰을 제안한다면, 편안한 수준으로 지연을 조정하는 것을 고려하세요.
>




# **Platform considerations**

*Not available in iOS, iPadOS, tvOS, and watchOS.*
> iOS, iPadOS, tvOS 및 watch에서는 사용할 수 없습니다.운영 체제
>




# **[components-navigation-and-search] token-fields**

## A token field is a type of text field that includes *tokens* — blocks of text that people can easily select and manipulate.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/token-field-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/token-field-intro-dark_2x.png)

When composing a new message in Mail, for example, the address fields are token fields. As people enter recipients, the recipients are converted from text into token form. People can select these recipient tokens and drag them to reorder or otherwise work with them individually.

You can configure a token field to present people with a list of suggested tokens as they enter text into the field. For example, Mail suggests recipients as people type into an address field. If they select a suggested recipient, it’s inserted into the field as a token.

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-suggestion_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-suggestion_2x.png)

An individual token can also include a contextual menu that’s denoted by a downward chevron character. This contextual menu can include information about the token or editing options. In Mail, a recipient token includes a contextual menu with commands for editing the recipient, marking the recipient as a VIP, and viewing the recipient’s contact card, among others.

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-contextual_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-contextual_2x.png)

Some token fields are accompanied by a separate list of available tokens, which people can select and drag into the field. The Language & Region settings pane uses this approach for its date and time format fields, for example. It offers individual date and time tokens that can be dragged into token fields, which people can format using the tokens’ contextual menus.

![https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-dates_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/token-fields/images/token-fields-dates_2x.png)

Tokens can also represent search terms in some situations; see [Search fields](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields).

# **Best practices**

**Add value with a context menu.** People often benefit from a [context menu](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/context-menus)with additional options or information about a token.

**Consider providing additional ways to convert text into tokens.** By default, text people enter turns into a token whenever they type a comma. You can specify additional shortcuts, such as return, that should also invoke this action.

**Customize the delay before showing tokens that the system suggests.**Suggestions appear immediately by default. However, suggestions appearing too quickly can be a distraction while typing. If your app suggests tokens, consider adjusting the delay to a comfortable level.

# **Platform considerations**

*Not available in iOS, iPadOS, tvOS, and watchOS.*
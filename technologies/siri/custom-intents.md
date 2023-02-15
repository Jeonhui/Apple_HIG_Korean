# **[technologies-siri] custom-intents**

If your app lets people perform an everyday task that doesn’t fit into any of the SiriKit domains, you can create a custom intent to represent it (see [System intents](../technologies/siri/system-intents) for a list of domains). You can also use a custom or system intent to support a shortcut, which gives people a quick way to initiate frequently performed actions by speaking a simple phrase or accepting a suggestion from Siri. To learn how to integrate your intents with the system so that people can discover them and add them to Siri, see [Shortcuts and suggestions](../siri/overview/shortcuts-and-suggestions/).
> 앱에서 사용자가 SiriKit 도메인에 맞지 않는 일상적인 작업을 수행할 수 있는 경우 이를 나타내는 사용자 정의 의도를 만들 수 있습니다(도메인 목록은 시스템 의도 참조). 또한 사용자 정의 또는 시스템 의도를 사용하여 단축키를 지원할 수 있으며, 이를 통해 사용자는 간단한 구문을 말하거나 시리의 제안을 수락하여 자주 수행되는 작업을 빠르게 시작할 수 있습니다. 사용자의 의도를 시스템과 통합하여 사용자가 의도를 검색하고 Siri에 추가하는 방법에 대해서는 바로 가기 및 제안을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/hey-siri-confirmation-not-required-success_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/hey-siri-confirmation-not-required-success_2x.png)

# **Custom intent categories and responses**
> 사용자 정의 의도 범주 및 응답
>




Although your custom intent won’t belong to a SiriKit domain, you’ll need to model it on a system-defined *intent category* that’s related to your action. SiriKit defines several categories that represent generic tasks, such as create, order, share, and search. Because these definitions are in the system, Siri knows how to communicate with people about common actions that are associated with each category — such as placing an order or sharing content — in ways that feel natural.
> 사용자 지정 의도가 SiriKit 도메인에 속하지 않더라도 작업과 관련된 시스템 정의 의도 범주를 기반으로 모델링해야 합니다. SiriKit는 생성, 순서, 공유 및 검색과 같은 일반적인 작업을 나타내는 여러 범주를 정의합니다. 이러한 정의가 시스템에 있기 때문에, 시리는 주문을 하거나 콘텐츠를 공유하는 것과 같은 각 범주와 관련된 일반적인 행동에 대해 사람들과 자연스럽게 소통하는 방법을 알고 있다.
>




It’s important to choose the category that best represents your action because the category influences the ways Siri speaks about it and the controls people might see in the interface. For example, a coffee app would likely choose the order category to represent its custom *order coffee*intent, and as a result, Siri can speak default responses that make sense in the context of this action, such as “Ready to order?” and “OK. Ordering.” Category choice can have other effects, too: Because the order category includes actions that have financial impact, using this category for the *order coffee* intent means that people will be asked to authenticate before completing the action.
> 사용자의 행동을 가장 잘 나타내는 범주를 선택하는 것이 중요합니다. 범주는 Siri가 행동에 대해 말하는 방식과 사용자가 인터페이스에서 볼 수 있는 컨트롤에 영향을 미치기 때문입니다. 예를 들어, 커피 앱은 주문 카테고리를 선택하여 사용자 지정 주문 커피 의도를 나타낼 수 있으며, 결과적으로 시리는 "주문 준비 완료" 및 "주문 완료"와 같은 이 작업의 맥락에서 의미 있는 기본 응답을 말할 수 있습니다 범주 선택은 다른 효과도 가질 수 있다: 주문 범주에는 재정적인 영향을 미치는 행동이 포함되기 때문에, 커피 주문 의도에 이 범주를 사용하는 것은 사람들이 그 행동을 완료하기 전에 인증을 요청받는다는 것을 의미한다.
>




For several categories, the system defines additional verbs that are related to the category’s default action. You can use these alternative verbs to help ensure that the Siri dialogue and the button titles displayed in the interface align with the way you present your app’s actions. For example, in addition to the default verb *order*, the order category includes the verbs *buy* and *book*.
> 여러 범주에 대해 시스템은 범주의 기본 동작과 관련된 추가 동사를 정의합니다. 이러한 대체 동사를 사용하여 인터페이스에 표시되는 Siri 대화상자와 버튼 제목이 앱의 동작을 표시하는 방식과 일치하도록 할 수 있습니다. 예를 들어, 기본 동사 순서 외에도 순서 범주에는 동사 buy와 book이 포함됩니다.
>




SiriKit defines the following custom intent categories and associated verbs.
> SiriKit는 다음과 같은 사용자 정의 의도 범주와 관련 동사를 정의한다.
>




| Category | Default verb | Additional verbs |
| --- | --- | --- |
| Generic | Do | Run, go |
| Information | View | Open |
| Order | Order | Book, buy |
| Start | Start | Navigate |
| Share | Share | Post, send |
| Create | Create | Add |
| Search | Search | Find, filter |
| Download | Download | Get |
| Other | Set | Request, toggle, check in |

SiriKit also defines three response types:
> SiriKit는 또한 세 가지 응답 유형을 정의합니다:
>




- Confirmation. Confirms that people still want to perform the action.
- >  확인. 작업을 계속 수행하려는 사용자를 확인합니다.

- Success. Indicates that the action has been initiated.
- >  성공. 작업이 시작되었음을 나타냅니다.

- Error. Tells people that the action can’t be completed.
- >  오류. 작업을 완료할 수 없음을 사용자에게 알립니다.


In several custom intent categories, SiriKit defines default dialogue for each response type. For example, the default confirmation dialogue for the order category is, “Ready to order?” and the default success dialogue for the share category is, “OK. Shared.”
> 여러 사용자 정의 의도 범주에서 SiriKit는 각 응답 유형에 대한 기본 대화 상자를 정의합니다. 예를 들어, 주문 카테고리의 기본 확인 대화상자는 "주문 준비 완료"이고 공유 카테고리의 기본 성공 대화상자는 "확인. 공유"입니다
>




To customize a response, you create a template that combines dialogue you write with placeholders for relevant information your app can supply while it’s working on the intent. For example, a coffee app might enhance the default order confirmation dialogue by providing custom content that includes a placeholder for the total cost of the order.
> 응답을 사용자 지정하려면 앱이 의도적으로 작동하는 동안 제공할 수 있는 관련 정보에 대한 플레이스홀더와 작성한 대화를 결합한 템플릿을 만듭니다. 예를 들어, 커피 앱은 총 주문 비용에 대한 자리 표시자를 포함하는 사용자 지정 콘텐츠를 제공하여 기본 주문 확인 대화상자를 향상시킬 수 있다.
>




Depending on the response type, your custom dialogue is presented before or after the default dialogue. For example, confirmation responses present the default dialogue after any custom dialogue. In the coffee app example, the customized confirmation dialogue would begin with something like, “Your large coffee with cream comes to $2.50.” and end with the default dialogue, “Ready to order?”
> 응답 유형에 따라 사용자 정의 대화 상자가 기본 대화 상자 앞이나 뒤에 표시됩니다. 예를 들어, 확인 응답은 사용자 정의 대화 뒤에 기본 대화 상자를 표시합니다. 커피 앱 예제에서 사용자 정의된 확인 대화상자는 "크림을 넣은 큰 커피는 $2.50입니다."와 같은 것으로 시작하여 기본 대화상자인 "주문 준비 완료?"로 끝납니다
>




# **Design a custom intent**

If a built-in SiriKit intent represents your action’s purpose, adopt that intent instead of defining a custom intent. For example, if you’d like to offer a shortcut for sending a message, adopt [INSendMessageIntent](https://developer.apple.com/documentation/sirikit/insendmessageintent); if you’d like to offer a shortcut for playing media, adopt [INPlayMediaIntent](https://developer.apple.com/documentation/sirikit/inplaymediaintent). For guidance, see [System intents](../technologies/siri/system-intents/).
> 기본 제공 SiriKit 의도가 작업의 목적을 나타내는 경우 사용자 정의 의도를 정의하는 대신 해당 의도를 채택하십시오. 예를 들어, 메시지를 보내는 바로 가기를 제공하려면 INSendMessage를 사용합니다의도: 미디어 재생에 대한 바로 가기를 제공하려면 INPlayMedia를 사용하십시오의도. 자세한 내용은 시스템 의도를 참조하십시오.
>




**If your app’s action requires a custom intent, pick the category that most closely matches the action.** A category informs the system about the general function of an intent or shortcut — like order, download, or search — and affects the text and spoken dialogue presented to people when a shortcut is offered by the system or used with Siri. You design the flow of conversation for the custom intents you offer, so it’s essential that you choose a category that corresponds to the meaning of each intent.
> 앱의 작업에 사용자 지정 의도가 필요한 경우 해당 작업과 가장 가까운 범주를 선택하십시오. 범주는 시스템에 주문, 다운로드 또는 검색과 같은 의도 또는 바로 가기의 일반적인 기능에 대해 알려주고 시스템에서 바로 가기를 제공하거나 Siri와 함께 사용할 때 사용자에게 제공되는 텍스트 및 음성 대화에 영향을 줍니다. 사용자가 제공하는 사용자 정의 의도에 따라 대화의 흐름을 설계하기 때문에 각 의도의 의미에 해당하는 범주를 선택하는 것이 중요합니다.
>




**TIP**If your action’s primary purpose is to retrieve information or show something to people — like displaying a sports score or the weather — use the information category. Using a different category requires people to make additional taps to get the information.
> 팁당신의 행동의 주요 목적이 정보를 검색하거나 사람들에게 스포츠 점수나 날씨를 표시하는 것과 같은 것을 보여주는 것이라면 정보 범주를 사용하세요. 다른 범주를 사용하려면 사람들이 정보를 얻기 위해 추가 탭을 작성해야 합니다.
>




**Design custom intents that accelerate common, useful tasks.** Take advantage of the familiarity people have with your app and focus on tasks that people are already doing often.
> 일반적이고 유용한 작업을 가속화하는 사용자 지정 의도를 설계합니다. 사용자가 앱에 익숙해진 이점을 활용하고 이미 자주 수행하고 있는 작업에 집중하십시오.
>




**Ensure that your intent works well in every scenario.** Make it easy for people to run your intent as a shortcut, regardless of how they initiate it. For example, be prepared for people to run it using their voice on devices with and without a screen, from suggestions on the lock screen or the Siri face on Apple Watch, from search, and within a multistep shortcut.
> 당신의 의도가 모든 시나리오에서 잘 작동하는지 확인하십시오. 사람들이 당신의 의도를 어떻게 시작하든 간에 바로 가기로 쉽게 실행할 수 있도록 하십시오. 예를 들어, 사람들이 화면이 있든 없든 간에, 잠금 화면이나 애플 워치의 시리 페이스에 대한 제안, 검색, 다단계 바로 가기 내에서 음성을 사용하여 실행할 수 있도록 준비하십시오.
>




**In general, design custom intents for tasks that aren’t overly complex.** People benefit the most from intents that reduce the number of actions required to complete a task. Don’t counteract that simplicity by requiring people to engage in a lengthy conversation with your app. You can also reduce the likelihood of user errors by limiting custom intents to clearly defined tasks.
> 일반적으로 지나치게 복잡하지 않은 작업에 대해 사용자 정의 의도를 설계합니다. 사람들은 작업을 완료하는 데 필요한 작업 수를 줄이는 의도에서 가장 큰 이점을 얻습니다. 사람들이 당신의 앱과 긴 대화를 하도록 요구함으로써 그 단순함에 대응하지 마세요. 또한 사용자 정의 의도를 명확하게 정의된 태스크로 제한하여 사용자 오류 가능성을 줄일 수 있습니다.
>




**Design your intents to be long-lived.** Avoid offering intents that are date-specific or associated with temporary data. For example, it’s not a good idea if a travel app offers a custom intent for each specific itinerary. A better intent might use follow-up questions to let people get the itinerary for one of their upcoming trips.
> 사용자의 의도가 오래 지속되도록 설계하십시오. 날짜별이거나 임시 데이터와 관련된 의도는 제공하지 마십시오. 예를 들어, 여행 앱이 각 특정 여행 일정에 대한 사용자 지정 의도를 제공하는 것은 좋은 생각이 아닙니다. 더 나은 의도는 후속 질문을 사용하여 사람들이 다가오는 여행 중 하나의 여행 일정을 얻을 수 있도록 할 수 있다.
>




**Don’t request permission to use Siri.** If your app supports only custom intents — and not system intents — you don’t need to get permission to use Siri before letting people create and use voice shortcuts for your intents. Asking for permission can slow people down and could discourage them from using your app’s custom intents.
> Siri 사용 권한을 요청하지 마십시오. 앱이 시스템 의도가 아닌 사용자 지정 의도만 지원하는 경우 사용자가 원하는 대로 음성 바로 가기를 만들고 사용하도록 허용하기 전에 Siri 사용 권한을 얻을 필요가 없습니다. 허가를 요청하는 것은 사람들의 속도를 늦출 수 있고 그들이 당신의 앱의 사용자 정의 의도를 사용하는 것을 막을 수 있다.
>




**Support background operation.** The best intents enable shortcuts that run quickly and don’t pull people out of their current context. Strive to support custom intents that can run in the background without bringing your app to the front. Supporting background operation also ensures that people can complete the task in hands-free and voice-only scenarios.
> 백그라운드 작업을 지원합니다. 최상의 의도는 빠르게 실행되고 현재 컨텍스트에서 사용자를 끌어내지 않는 바로 가기를 가능하게 합니다. 앱을 전면에 내세우지 않고 백그라운드에서 실행할 수 있는 사용자 지정 의도를 지원하도록 노력하십시오. 또한 백그라운드 작업을 지원하면 핸즈프리 및 음성 전용 시나리오에서 작업을 완료할 수 있습니다.
>




# **Help people customize their requests**
> 사용자가 요청을 사용자 정의할 수 있도록 지원
>




Custom intents can offer follow-up questions that let people do more with a single intent by refining its results on the fly. For example, if you offer an *order coffee* intent, you can help people get exactly what they want by asking them questions such as, “What size?”, “What flavor?”, and “Which location?” Details like size, flavor, and location are *parameters* your app can define to help people personalize their request.
> 사용자 정의 의도는 결과를 신속하게 세분화하여 단일 의도로 더 많은 작업을 수행할 수 있는 후속 질문을 제공할 수 있습니다. 예를 들어, 만약 당신이 커피 주문 의도를 제공한다면, 당신은 사람들에게 "어떤 크기?", "어떤 맛?", "어느 위치?"와 같은 질문을 함으로써 그들이 원하는 것을 얻도록 도울 수 있다 크기, 맛 및 위치와 같은 세부 정보는 사용자가 요청을 개인화하는 데 도움이 되도록 앱이 정의할 수 있는 매개 변수입니다.
>




People supply parameter values to personalize an intent by responding to your follow-up questions or by editing existing values in the Shortcuts app or the Add to Siri sheet within your app. For example, if you offer an *order ground coffee* intent that includes a parameter for the grind size, you might supply a follow-up question like, “Which grind?” For people who typically order the coarse grind, you could simplify the interaction by using the value *coarse* as the default parameter value in a dialogue like, “Do you want coarse-ground coffee?” If people choose a different grind, you can follow up by presenting the full list of options. In voice-only scenarios, Siri speaks your follow-up questions and sends you the responses. When people use the Shortcuts app or your Add to Siri sheet to edit a parameter value, you receive the new value when they use the associated shortcut. For developer guidance, see [Adding user interactivity with Siri Shortcuts and the Shortcuts app](https://developer.apple.com/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app).
> 사용자는 후속 질문에 응답하거나 앱 내 바로 가기 앱 또는 시리에 추가 시트에서 기존 값을 편집하여 의도를 개인화하기 위한 매개 변수 값을 제공합니다. 예를 들어, 분쇄 크기에 대한 매개 변수가 포함된 분쇄된 커피 주문 의도를 제공하는 경우, "어느 분쇄입니까?"와 같은 후속 질문을 제공할 수 있습니다 일반적으로 거친 분쇄를 주문하는 사용자의 경우, "굵은 분쇄 커피를 원하십니까?"와 같은 대화 상자에서 거친 값을 기본 매개 변수 값으로 사용하여 상호 작용을 단순화할 수 있습니다 사람들이 다른 방법을 선택하는 경우 전체 옵션 목록을 제시하여 후속 조치를 취할 수 있습니다. 음성 전용 시나리오에서는 Siri가 후속 질문을 말하고 응답을 보냅니다. 사람들이 바로 가기 앱이나 당신의 Siri 시트에 추가를 사용하여 매개 변수 값을 편집할 때, 당신은 그들이 연관된 바로 가기를 사용할 때 새로운 값을 받는다. 개발자 지침은 Siri 바로 가기 및 바로 가기 앱으로 사용자 상호 작용 추가를 참조하십시오.
>




**Design intents that require as few follow-up questions as possible.** Often, an intent can fulfill a request without asking any follow-up questions. Although follow-up questions make intents more flexible, you don’t want to force people into a long interaction. In most cases, it’s best to offer just one or two follow-up questions.
> 가능한 적은 수의 후속 질문이 필요한 의도를 설계합니다. 종종 의도는 후속 질문을 묻지 않고 요청을 수행할 수 있습니다. 후속 질문이 의도를 더 유연하게 만들지만, 사람들에게 긴 상호 작용을 강요하고 싶지는 않습니다. 대부분의 경우, 한 두 개의 후속 질문만 제공하는 것이 가장 좋습니다.
>




**List the smallest number of options possible, and sort the items in a way that makes sense.**As with too many follow-up questions, giving people too many options can make completing the task feel onerous. As you determine whether to include an item, consider its complexity as well as its utility. In a food-ordering app, for example, it might be easier for people to parse a list of individual menu items than a list of orders, each of which contains multiple items. After you identify a small number of useful items, consider sorting them by recency, frequency, or popularity.
> 가능한 최소 수의 옵션을 나열하고 항목을 의미 있는 방식으로 정렬합니다.너무 많은 후속 질문과 마찬가지로, 사람들에게 너무 많은 옵션을 주는 것은 과제를 완료하는 것을 부담스럽게 할 수 있다. 항목을 포함할지 여부를 결정할 때 항목의 복잡성과 유용성을 고려하십시오. 예를 들어, 음식 주문 앱에서 사람들은 각각이 여러 항목을 포함하는 주문 목록보다 개별 메뉴 항목 목록을 분석하는 것이 더 쉬울 수 있다. 소수의 유용한 항목을 식별한 후에는 최근, 빈도 또는 인기별로 정렬하는 것을 고려해 보십시오.
>




**Make sure each follow-up question is meaningful.** Ideally, each follow-up question helps people make an important choice. If options or questions you present are too granular or too similar, the conversation can become repetitive, and people may feel like using your intent is too much work.
> 각각의 후속 질문이 의미가 있는지 확인하십시오. 이상적으로는, 각 후속 질문은 사람들이 중요한 선택을 하는 데 도움이 됩니다. 사용자가 제시하는 옵션이나 질문이 너무 세분화되거나 유사한 경우 대화가 반복될 수 있으며, 사용자의 의도를 사용하는 것이 너무 많은 작업이라고 느낄 수 있습니다.
>




**Design parameters that are easy for people to understand and use.** Aim for parameters that represent simple values or attributes and name them using simple, straightforward terms. For example, a soup-ordering app might define parameters for the type of soup, the serving size, and a delivery location, using names like *soup*, *size*, and *location*. For guidance, see [Shortcuts and suggestions](../technologies/siri/shortcuts-and-suggestions/).
> 사람들이 이해하고 사용하기 쉬운 매개변수를 설계합니다. 단순한 값이나 속성을 나타내는 매개변수를 목표로 하고 단순하고 간단한 용어를 사용하여 이름을 지정합니다. 예를 들어 수프 주문 앱은 수프, 크기 및 위치와 같은 이름을 사용하여 수프 종류, 제공 크기 및 배달 위치에 대한 매개 변수를 정의할 수 있습니다. 자세한 내용은 바로 가기 및 제안을 참조하십시오.
>




**Ask for confirmation only when necessary.** An intent can ask people for confirmation before completing the task or when interpreting an answer to a follow-up question. Apps that support tasks that have financial impact, such as an app that enables ordering, must ask for confirmation before completing an order. For tasks that don’t have financial impact, asking for confirmation can feel like too much extra work and can sometimes discourage people from completing their request. In all cases, avoid asking for confirmation more than once.
> 필요한 경우에만 확인을 요청하십시오. 의도는 작업을 완료하기 전에 또는 후속 질문에 대한 답변을 해석할 때 사람들에게 확인을 요청할 수 있습니다. 주문이 가능한 앱처럼 금전적인 영향을 미치는 작업을 지원하는 앱은 주문을 완료하기 전에 확인을 요청해야 한다. 재정적인 영향을 미치지 않는 작업의 경우, 확인을 요청하는 것은 너무 많은 추가 작업처럼 느껴질 수 있고 때때로 사람들이 요청을 완료하는 것을 방해할 수 있습니다. 모든 경우 두 번 이상 확인을 요청하지 마십시오.
>




**Support chaining of follow-up questions when it makes sense.** For example, an app that helps people order food might offer options for pickup or delivery, but ask for a specific location only after people choose the delivery option.
> 예를 들어, 사람들이 음식을 주문할 수 있도록 도와주는 앱은 픽업 또는 배달 옵션을 제공하지만, 사람들이 배달 옵션을 선택한 후에만 특정 위치를 요청할 수 있습니다.
>




**Provide useful default parameter values in your Add to Siri sheet.** You can make it easier for people to create a shortcut for your intent by setting default values that are based on a person’s current context. For example, a soup-ordering app might offer a *Reorder soup* intent with a follow-up question that asks people to specify a past order. When people add this shortcut to Siri from a particular order’s detail view, the app could preconfigure the shortcut to include the values from that order in its parameters. Bear in mind that some people may never configure your intent in the Shortcuts app or your Add to Siri sheet, so always provide shortcuts that don’t rely on additional configuration.
> [시리에 추가] 시트에 유용한 기본 매개변수 값을 입력하십시오. 사용자의 현재 컨텍스트를 기반으로 기본값을 설정하여 사용자가 원하는 바로 가기를 쉽게 만들 수 있습니다. 예를 들어 수프 주문 앱은 사람들에게 과거 주문을 지정하도록 요청하는 후속 질문과 함께 수프 주문 의도를 제공할 수 있다. 사람들이 특정 주문의 세부 보기에서 이 바로 가기를 Siri에 추가할 때, 앱은 해당 주문의 값을 매개 변수에 포함하도록 바로 가기를 미리 구성할 수 있습니다. 일부 사용자는 바로 가기 앱이나 시리에 추가 시트에서 사용자의 의도를 구성하지 않을 수 있으므로 항상 추가 구성에 의존하지 않는 바로 가기를 제공합니다.
>




**Prioritize the options you offer based on the context in which people run your shortcut.** For example, if people use your shortcut to order an item for pickup, offer pickup locations that are currently close by. Offering options that adapt to the context in which your shortcut is run can help people avoid creating separate shortcuts for specific options.
> 사용자가 바로 가기를 실행하는 상황에 따라 제공하는 옵션의 우선 순위를 지정합니다. 예를 들어, 사용자가 바로 가기를 사용하여 픽업할 항목을 주문하는 경우 현재 가까운 픽업 위치를 제공합니다. 바로 가기가 실행되는 상황에 맞는 선택사항을 제공하면 사용자가 특정 선택사항에 대한 별도의 바로 가기를 작성하는 것을 방지할 수 있습니다.
>




**Consider adjusting the parameter values you offer when people set up your shortcut.** When you indicate that a parameter has dynamic options, you can enhance the shortcut setup experience in two ways.
> 사용자가 바로 가기를 설정할 때 제공하는 매개 변수 값을 조정하는 것을 고려하십시오. 매개 변수에 동적 옵션이 있음을 나타낼 때 두 가지 방법으로 바로 가기 설정 환경을 향상시킬 수 있습니다.
>




- You can find and present parameter values that are relevant to the context people are in while they’re setting up the shortcut. For example, if people use the Shortcuts app to choose a value for a store-location parameter, the parameter can dynamically generate a list of stores that are currently closest to the device.
- >  바로 가기를 설정하는 동안 사용자가 있는 컨텍스트와 관련된 매개 변수 값을 찾아 표시할 수 있습니다. 예를 들어, 사람들이 바로 가기 앱을 사용하여 저장 위치 매개 변수의 값을 선택하는 경우 매개 변수는 현재 장치에 가장 가까운 저장소 목록을 동적으로 생성할 수 있습니다.

- You can present a comprehensive list of parameter values. When people set up a shortcut, having an extensive list of parameter values can help them create the shortcut they want. In contrast, when people use a shortcut to accelerate an action, they generally prefer the convenience of having a shorter list of choices.
- >  매개 변수 값의 포괄적인 목록을 표시할 수 있습니다. 바로 가기를 설정할 때 매개 변수 값의 광범위한 목록을 사용하면 원하는 바로 가기를 만들 수 있습니다. 대조적으로, 사람들이 행동을 가속화하기 위해 바로 가기를 사용할 때, 그들은 일반적으로 짧은 선택 목록을 갖는 편리함을 선호한다.


For developer guidance, see the storeLocation parameter in the intent definition file of the [SoupChef sample code project](https://developer.apple.com/documentation/sirikit/soup_chef_accelerating_app_interactions_with_shortcuts).
> 개발자 지침은 SoupChef 샘플 코드 프로젝트의 의도 정의 파일에서 storeLocation 매개 변수를 참조하십시오.
>




# **Enhance the voice experience for custom intents**
> 사용자 정의 의도를 위한 음성 환경 개선
>




**Aim to create conversational interactions.** You can customize what Siri says throughout the voice experience, including the handling of follow-up questions. Try writing a script and acting it out with another person to see how well your dialogue works in a face-to-face exchange. Experiencing custom dialogue in this way can help you find places where the interaction doesn’t feel natural.
> 대화형 상호작용을 만드는 것을 목표로 합니다. 후속 질문의 처리를 포함하여 음성 경험 전반에 걸쳐 시리가 말하는 것을 사용자 정의할 수 있습니다. 직접 대화를 주고받을 때 여러분의 대화가 얼마나 효과적인지 보기 위해 대본을 쓰고 다른 사람과 연기해 보세요. 이러한 방식으로 사용자 지정 대화를 경험하면 상호 작용이 자연스럽게 느껴지지 않는 장소를 찾는 데 도움이 될 수 있습니다.
>




**Help people understand errors and failures.** The system provides some default error descriptions, but it’s best to enhance error responses so that they’re specific to the current situation. For example, if chicken noodle soup is sold out, a soup app can respond with a custom error like, “Sorry, we’re out of chicken noodle soup” instead of “Sorry, we can’t complete your order.”
> 이 시스템은 기본 오류 설명을 제공하지만 현재 상황에 맞게 오류 응답을 개선하는 것이 가장 좋습니다. 예를 들어, 닭국수가 품절된 경우 수프 앱은 "죄송합니다, 주문을 완료할 수 없습니다" 대신 "죄송합니다, 닭국수가 없습니다"와 같은 사용자 지정 오류로 응답할 수 있습니다
>




**Strive for engaging voice responses.** Remember that people may perform your app’s tasks from their HomePod, using “Hey Siri” with their AirPods, or through CarPlay without looking at a screen. In these cases, the voice response should convey the same essential information that the visual elements display to ensure that people can get what they need no matter how they interact with Siri.
> 매력적인 음성 응답을 위해 노력하십시오. 사람들은 홈팟에서, 에어팟과 함께 "헤이 시리"를 사용하거나 화면을 보지 않고 CarPlay를 통해 앱의 작업을 수행할 수 있습니다. 이러한 경우 음성 응답은 사람들이 시리와 어떻게 상호 작용하든 필요한 것을 얻을 수 있도록 시각적 요소가 표시하는 것과 동일한 필수 정보를 전달해야 한다.
>




**Create voice responses that are concise, descriptive, and work well in voice-driven scenarios.** As with a shortcut title, an effective custom spoken response clearly conveys what’s happening as the shortcut runs. If you ask follow-up questions, be sure to customize the default dialogue for clarity. For example, “Which soup?” is clearer than “Which one?”
> 간결하고 서술적이며 음성 중심의 시나리오에서 잘 작동하는 음성 응답을 만듭니다. 바로 가기 제목과 마찬가지로 효과적인 사용자 지정 음성 응답은 바로 가기가 실행됨에 따라 발생하는 일을 명확하게 전달합니다. 후속 질문을 할 경우 명확하게 하기 위해 기본 대화 상자를 사용자 지정해야 합니다. 예를 들어, "어떤 수프?"는 "어떤 수프?"보다 더 명확하다
>




**Avoid unnecessary repetition.** People tend to run voice shortcuts frequently, so they may hear the same prompt multiple times when answering follow-up questions or dealing with errors. Use the context of the current conversation to remove as many details from the prompts as possible. Avoid including unnecessary words or attempts at humor because both can become irritating over time.
> 사람들은 음성 바로 가기를 자주 실행하기 때문에 후속 질문에 답하거나 오류를 처리할 때 동일한 프롬프트를 여러 번 들을 수 있습니다. 현재 대화의 컨텍스트를 사용하여 프롬프트에서 가능한 한 많은 세부 정보를 제거합니다. 불필요한 말이나 유머 시도를 포함하는 것을 피하세요. 왜냐하면 둘 다 시간이 지남에 따라 짜증이 날 수 있기 때문입니다.
>




**Help conversations with Siri feel natural.** People interact with Siri in a variety of ways, such as choosing a list item by saying “the second one,” or, in the case of a soup-ordering app, saying “large” or “small” instead of “bowl” or “cup.” You can make people’s Siri interactions feel more natural when you give the system alternative terms and phrases that work as app-specific synonyms (like using “bowl” as a synonym for “large”). Also consider enhancing clarity by providing alternative dialogue options for Siri to speak. For example, the soup app might present a list of onscreen menu options like “1 clam chowder,” “1 clam chowder and 1 tomato,” but speak these options as “Which order? The one with clam chowder only or the one that includes tomato?”
> 시리와의 대화가 자연스럽게 느껴지도록 도와준다. 사람들은 '두 번째'라고 말하며 목록 항목을 선택하거나, 수프 주문 앱의 경우 '그릇'이나 '컵' 대신 '크다' 또는 '작다'고 말하는 등 다양한 방식으로 시리와 상호작용한다 앱별 동의어(예: "bowl"을 "large"의 동의어로 사용)로 작동하는 시스템 대체 용어와 구문을 제공할 때 사람들의 시리 상호 작용을 보다 자연스럽게 느낄 수 있습니다. 또한 Siri가 말할 수 있는 대체 대화 옵션을 제공하여 명확성을 높이는 것을 고려하십시오. 예를 들어, 수프 앱은 "1 clam chowder", "1 clam chowder and 1 tomato"와 같은 화면 메뉴 옵션 목록을 표시할 수 있지만 이러한 옵션은 "어떤 순서?"로 말합니다? 조개 차우더만 있는 것과 토마토가 들어간 것 중 어느 것이 더 좋습니까?"
>




**Exclude your app name.** The system provides verbal and visual attribution for your app when responding to people. Including your appʼs name in a verbal response is redundant and may make the experience of interacting with Siri feel less natural. Siri speaks your app’s name less frequently when people have used a shortcut several times, because it isn’t necessary to keep reminding them which app is responding.
> 앱 이름을 제외합니다. 이 시스템은 사용자에게 응답할 때 앱에 대한 언어 및 시각적 속성을 제공합니다. 당신의 앱 이름을 구두 답변에 포함시키는 것은 불필요하며 시리와 상호 작용하는 경험을 덜 자연스럽게 느끼게 할 수 있다. Siri는 어떤 앱이 응답하는지 계속해서 상기시킬 필요가 없기 때문에 사람들이 여러 번 바로 가기를 사용했을 때 당신의 앱 이름을 덜 말한다.
>




**Don’t attempt to mimic or manipulate Siri.** Your app should never impersonate Siri, attempt to reproduce the functionality that Siri provides, or provide a response that appears to come from Apple.
> Siri를 흉내 내거나 조작하지 마십시오. 앱은 Siri를 가장하거나 Siri가 제공하는 기능을 재현하려고 하거나 Apple에서 제공하는 것으로 보이는 응답을 제공해서는 안 됩니다.
>




**Be appropriate and respect parental controls.** Never present offensive or demeaning content. Keep in mind that many families use parental controls to restrict explicit content and content that’s based on specific rating levels.
> 적절하고 부모의 통제를 존중해야 한다. 모욕적이거나 모욕적인 내용을 제시해서는 안 된다. 많은 가정에서 보호자 통제를 사용하여 특정 등급 수준에 따라 명시적인 내용과 내용을 제한합니다.
>




**Avoid using personal pronouns.** Create content that’s inclusive of all people.
> 인칭 대명사를 사용하는 것을 피하세요. 모든 사람을 포함하는 내용을 만드십시오.
>




**Consider letting people view more options in your app.** If the list of options doesn’t include the items people need, you might want to include an item that lets people open your app to see more. In the list, you could use copy like, “See more in *App Name*” and in spoken dialogue, you might encourage people to say “More options.”
> 사용자가 앱에서 더 많은 옵션을 볼 수 있도록 허용하는 것이 좋습니다. 옵션 목록에 필요한 항목이 없으면 사용자가 앱을 열어서 더 많은 항목을 볼 수 있도록 허용하는 항목을 포함할 수 있습니다. 목록에서 "앱 이름에서 더 보기"와 같은 복사본을 사용할 수 있으며, 음성 대화에서 사람들이 "더 많은 옵션"을 말하도록 권장할 수 있습니다
>




**Keep responses device-independent.** People may use Siri to interact with your app on Apple Watch, HomePod, iPad, iPhone, or through CarPlay. If you must provide device-specific wording, make sure it accurately reflects the user’s current device.
> 응답을 장치 독립적으로 유지합니다. 사용자는 Siri를 사용하여 Apple Watch, HomePod, iPad, iPhone 또는 CarPlay를 통해 앱과 상호 작용할 수 있습니다. 장치별 표현을 제공해야 하는 경우 사용자의 현재 장치를 정확하게 반영해야 합니다.
>




**Don’t advertise.** Don’t include advertisements, marketing, or in-app purchase sales pitches in your intent content.
> 광고하지 마십시오. 광고, 마케팅 또는 앱 내 구매 판매 광고를 의도한 내용에 포함시키지 마십시오.
>




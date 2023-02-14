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





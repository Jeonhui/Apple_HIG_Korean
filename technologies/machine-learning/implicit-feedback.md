# **[technologies-machine-learning] implicit-feedback**

Implicit feedback is information that arises as people interact with your app’s features. Unlike the specific responses you get from [explicit feedback](../technologies/machine-learning/explicit-feedback), implicit feedback gives you a wide range of information about user behavior and preferences. Although incorporating implicit feedback isn’t required for a great machine learning app, the feedback can help you improve your app’s user experience without asking people to do any extra work.
> 암시적 피드백은 사용자가 앱의 기능과 상호 작용할 때 발생하는 정보입니다. 명시적 피드백에서 얻는 특정 응답과 달리, 암시적 피드백은 사용자 행동 및 선호도에 대한 광범위한 정보를 제공합니다. 훌륭한 기계 학습 앱에 암묵적 피드백을 통합할 필요는 없지만, 피드백은 사람들에게 추가 작업을 요청하지 않고도 앱의 사용자 경험을 향상시키는 데 도움이 될 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/implicit-feedback_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/implicit-feedback_2x.png)

**Always secure people’s information.** Implicit feedback can gather potentially sensitive user information, so you must be particularly careful to maintain strict controls on user privacy.
> 항상 사람들의 정보를 보호하십시오. 암묵적인 피드백은 잠재적으로 민감한 사용자 정보를 수집할 수 있으므로 사용자 개인 정보에 대한 엄격한 통제를 유지하도록 특히 주의해야 합니다.
>




**Help people control their information.** As an app developer, you know that the more you understand about the behavior of your users — both within your app and in other apps — the more you can improve the experience your app provides. Although most people understand the benefits of making their information available to multiple apps, they may still be surprised when things they do in one app affect experiences they have in a different app. Worse, people may assume that apps are sharing their private information, which can cause them to lose trust in the apps. It’s important to tell people how your app gets and shares their information and to give people ways to restrict the flow of their information.
> 사람들이 자신의 정보를 제어할 수 있도록 도와줍니다. 앱 개발자로서, 앱 내와 다른 앱 모두에서 사용자의 행동에 대해 더 많이 이해할수록 앱이 제공하는 경험을 더 향상시킬 수 있다는 것을 알고 있습니다. 대부분의 사람들은 자신의 정보를 여러 앱에서 사용할 수 있게 하는 것의 이점을 이해하지만, 한 앱에서 하는 일이 다른 앱에서 경험하는 것에 영향을 미칠 때 여전히 놀랄 수 있다. 설상가상으로, 사람들은 앱이 그들의 개인 정보를 공유하고 있다고 가정할 수 있으며, 이것은 앱에 대한 신뢰를 잃게 할 수 있다. 앱이 어떻게 정보를 얻고 공유하는지 알려주고 사람들에게 정보의 흐름을 제한할 수 있는 방법을 제공하는 것이 중요합니다.
>




**Don’t let implicit feedback decrease people’s opportunities to explore.** Implicit feedback tends to reinforce people’s behavior, which can improve the user experience in the short term, but may worsen it in the long term. For example, it might seem like a good idea to give people a set of suggestions that matches all the things they’re interested in now, but doing so doesn’t encourage them to explore new things.
> 암묵적 피드백이 사람들의 탐색 기회를 감소시키지 않도록 한다. 암묵적 피드백은 사람들의 행동을 강화시키는 경향이 있어 단기적으로는 사용자 경험을 향상시킬 수 있지만 장기적으로는 악화시킬 수 있다. 예를 들어, 사람들에게 그들이 지금 관심 있는 모든 것들과 일치하는 일련의 제안들을 주는 것이 좋은 생각처럼 보일 수 있지만, 그렇게 하는 것이 그들이 새로운 것들을 탐구하도록 격려하지는 않는다.
>




**When possible, use multiple feedback signals to improve suggestions and mitigate mistakes.** Implicit feedback is indirect, so it can be difficult to discern the user’s actual intent in the information you gather. For example, if someone views a photo, shares it in a message, and adds it to a shared album, it doesn’t necessarily mean they have positive feelings about the photo. Incorporate implicit feedback from multiple sources and interactions to help you avoid misinterpreting people’s intentions.
> 가능하면 여러 피드백 신호를 사용하여 제안을 개선하고 실수를 완화하십시오. 암묵적 피드백은 간접적이기 때문에 수집한 정보에서 사용자의 실제 의도를 식별하기 어려울 수 있습니다. 예를 들어, 누군가가 사진을 보고 메시지로 공유한 다음 공유 앨범에 추가한다고 해서 반드시 사진에 대해 긍정적인 감정을 갖는 것은 아닙니다. 여러 출처 및 상호 작용의 암시적 피드백을 통합하여 사용자의 의도를 잘못 해석하지 않도록 합니다.
>




**Consider withholding private or sensitive suggestions.** People often share their accounts and devices with others, or switch from using a personal device to a communal one. If your app receives implicit feedback related to private or sensitive topics, avoid offering recommendations based on that feedback.
> 개인적이거나 민감한 제안을 보류하는 것을 고려하십시오. 사람들은 종종 자신의 계정과 장치를 다른 사람들과 공유하거나 개인용 장치를 사용하는 것에서 공용 장치로 전환합니다. 앱이 비공개 또는 민감한 주제와 관련된 암묵적인 피드백을 받는 경우 해당 피드백을 기반으로 한 권장 사항을 제공하지 마십시오.
>




**Prioritize recent feedback.** People’s tastes change frequently, so base your recommendations on recent implicit feedback. For example, Face ID prioritizes recent facial input because it’s most likely to represent what the user looks like now. If recent feedback isn’t available, you can fall back to historical feedback.
> 최근 피드백의 우선순위를 정하세요. 사람들의 취향은 자주 바뀌기 때문에 최근의 암묵적인 피드백을 바탕으로 추천을 하세요. 예를 들어, Face ID는 현재 사용자의 모습을 나타낼 가능성이 가장 높기 때문에 최근의 얼굴 입력을 우선시합니다. 최근 피드백을 사용할 수 없는 경우 과거 피드백으로 돌아갈 수 있습니다.
>




**Use feedback to update predictions on a cadence that matches the user’s mental model of the feature.** For example, people expect typing suggestions to update immediately as they’re typing. On the other hand, giving people continuously updated song recommendations makes it hard to consider individual songs and could make them feel rushed or overwhelmed.
> 예를 들어, 사람들은 입력 제안이 입력할 때 즉시 업데이트되기를 기대합니다. 반면에, 사람들에게 지속적으로 업데이트된 노래 추천을 주는 것은 개별적인 노래를 고려하기 어렵게 만들고 그들이 서두르거나 벅차게 느끼게 할 수 있다.
>




**Be prepared for changes in implicit feedback when you make changes to your app’s UI.** Even small UI changes can lead to noticeable changes in the amount and types of implicit feedback. For example, changing the location of a button can affect how people use it, even if there’s no change in the benefit they get from the button’s action. Take such changes into account when interpreting the implicit feedback you receive from interactions in your app.
> 앱의 UI를 변경할 때 암시적 피드백의 변경에 대비하십시오. 작은 UI 변경으로도 암시적 피드백의 양과 유형이 눈에 띄게 변경될 수 있습니다. 예를 들어 단추의 위치를 변경하면 단추의 동작으로 얻는 이점이 변경되지 않더라도 사용자가 단추를 사용하는 방법에 영향을 줄 수 있습니다. 앱의 상호 작용에서 받은 암시적 피드백을 해석할 때 이러한 변경 사항을 고려하십시오.
>




**Beware of confirmation bias.** Implicit feedback is constrained by what users can actually see and do in your app and other apps — it rarely gives you insight into new things people might like to do. Avoid relying solely on implicit feedback to inform your results.
> 확인 편향에 주의하라. 암묵적 피드백은 사용자가 당신의 앱과 다른 앱에서 실제로 보고 할 수 있는 것에 의해 제한된다. 그것은 사람들이 하고 싶어할 수 있는 새로운 것들에 대한 통찰력을 거의 제공하지 않는다. 결과를 알리기 위해 암묵적인 피드백에만 의존하지 마십시오.
>




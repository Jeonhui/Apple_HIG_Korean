# **[technologies-machine-learning] confidence**

Confidence indicates the measure of certainty for a result. Not all models produce confidence values by default, so you might consider generating them if you can use them to improve the user experience of your app.
> 신뢰는 결과에 대한 확실성의 척도를 나타냅니다. 모든 모델이 기본적으로 신뢰 값을 생성하는 것은 아니므로 앱의 사용자 환경을 개선하기 위해 신뢰 값을 사용할 수 있는 경우 신뢰 값을 생성하는 것을 고려할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/confidence_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/confidence_2x.png)

Although it might seem like higher confidence produces a higher quality result — and therefore a better user experience — it doesn’t necessarily work that way. You need to verify that your confidence values correspond to the quality of your results. For example, you might review values for multiple confidence thresholds or compare values across multiple versions of your app. If you’re not sure how your confidence values correlate with the quality of your results, it’s not a good idea to convey confidence to people.
> 신뢰도가 높아지면 더 높은 품질의 결과가 나오고 따라서 더 나은 사용자 환경이 생성되는 것처럼 보일 수 있지만 반드시 그렇게 작동하는 것은 아닙니다. 신뢰 값이 결과의 품질과 일치하는지 확인해야 합니다. 예를 들어 여러 신뢰 임계값에 대한 값을 검토하거나 여러 버전의 앱에서 값을 비교할 수 있습니다. 자신의 신뢰 가치가 결과의 질과 어떻게 상관관계가 있는지 확실하지 않다면, 사람들에게 자신감을 전달하는 것은 좋은 생각이 아니다.
>




**Know what your confidence values mean before you decide how to present them.** For example, people may forgive low-quality results from [complementary](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/roles#critical-or-complementary) features — especially when results are accompanied by [attributions](../technologies/machine-learning/attribution) or other contextual information — but presenting low-quality results in a prominent way is likely to erode trust in your app.
> 예를 들어, 사람들은 특히 결과에 속성이나 기타 상황에 맞는 정보가 수반되는 경우 보완 기능의 낮은 품질의 결과를 용서할 수 있지만, 낮은 품질의 결과를 눈에 띄는 방식으로 제시하면 앱에 대한 신뢰를 약화시킬 수 있습니다.
>




**In general, translate confidence values into concepts that people already understand.** Simply displaying a confidence value doesn’t necessarily help people understand how it relates to a result. For example, a feature that suggests new music based on the user’s listening habits might calculate that there’s a 97% match between a new song and the songs to which the user listens. However, displaying “97% match” next to the new song as an attribution doesn’t communicate enough information to help the user make a choice. In contrast, providing an attribution that’s clearly based on the user’s behavior — such as “Because you listen to pop music" — can be more actionable.
> 일반적으로 신뢰 값을 사람들이 이미 이해하고 있는 개념으로 변환해야 합니다. 단순히 신뢰 값을 표시한다고 해서 결과와 어떤 관계가 있는지 이해하는 데 반드시 도움이 되는 것은 아닙니다. 예를 들어, 사용자의 청취 습관에 따라 새 음악을 제안하는 기능은 새 노래와 사용자가 듣는 노래 사이에 97%의 일치가 있다고 계산할 수 있습니다. 그러나 신곡 옆에 "97% 일치"를 속성으로 표시하는 것은 사용자가 선택하는 데 도움이 될 만큼 충분한 정보를 전달하지 못한다. 반대로 "팝 음악을 듣기 때문에"와 같이 사용자의 행동에 명확하게 기반을 둔 속성을 제공하는 것이 더 실행 가능할 수 있습니다.
>




**In situations where attributions aren’t helpful, consider ranking or ordering the results in a way that implies confidence levels.** If you must display confidence directly, consider expressing it in terms of semantic categories. For example, a feature that predicts travel prices might replace ranges of confidence numbers with categories like “high chance” and “low chance” to give context to the values and help people understand and compare the results.
> 속성이 도움이 되지 않는 상황에서는 신뢰 수준을 암시하는 방식으로 결과의 순위를 매기거나 순서를 정하는 것을 고려하고, 자신감을 직접 표시해야 할 경우 의미론적 범주로 표현하는 것을 고려한다. 예를 들어, 여행 가격을 예측하는 기능은 신뢰할 수 있는 숫자의 범위를 "높은 가능성"과 "낮은 가능성"과 같은 범주로 대체하여 값에 맥락을 제공하고 사람들이 결과를 이해하고 비교하도록 도울 수 있다.
>




**In scenarios where people expect statistical or numerical information, display confidence values that help them interpret the results.** For example, weather predictions, sports statistics, and polling numbers are often accompanied by specific values that express the accuracy of the data as an interval or a percentage.
> 사람들이 통계적 또는 수치적 정보를 기대하는 시나리오에서는 결과를 해석하는 데 도움이 되는 신뢰 값을 표시한다. 예를 들어, 날씨 예측, 스포츠 통계, 여론조사 번호는 종종 데이터의 정확성을 간격 또는 백분율로 표현하는 특정 값을 동반한다.
>




**Whenever possible, help people make decisions by conveying confidence in terms of actionable suggestions.** Understanding people’s goals is key to expressing confidence in ways that help them make decisions. For example, if your feature predicts when an item will be at its lowest price, you know that people want to optimize how they spend their time and money. For a feature like this, displaying percentages or other numerical confidence values would be less valuable than providing actionable suggestions like “This is a good time to buy,” or “Consider waiting for a better price.”
> 가능할 때마다 실행 가능한 제안의 관점에서 자신감을 전달함으로써 사람들이 결정을 내릴 수 있도록 도와준다. 사람들의 목표를 이해하는 것은 그들이 결정을 내리는 데 도움이 되는 방법에 대한 자신감을 표현하는 열쇠이다. 예를 들어, 기능이 항목의 최저 가격을 예측하는 경우 사람들은 시간과 돈을 소비하는 방법을 최적화하려고 합니다. 이러한 기능의 경우, 백분율 또는 기타 수치 신뢰 값을 표시하는 것은 "지금이 구매하기에 좋은 시기" 또는 "더 나은 가격을 기다리는 것을 고려해 보십시오"와 같은 실행 가능한 제안을 제공하는 것보다 덜 가치가 있습니다
>




**Consider changing how you present results based on different confidence thresholds.** If high or low levels of confidence have a meaningful impact on the ways people can experience the results, it’s a good idea to adapt your presentation accordingly. For example, when confidence is high, the face recognition feature in Photos simply displays the photos that contain a specific person, but when confidence is lower, the feature asks people to confirm whether the photos contain the person before showing more.
> 서로 다른 신뢰 임계값을 기반으로 결과를 제시하는 방법을 변경하는 것을 고려하십시오. 신뢰 수준이 높거나 낮으면 사람들이 결과를 경험할 수 있는 방법에 의미 있는 영향을 미친다면, 그에 따라 프레젠테이션을 조정하는 것이 좋습니다. 예를 들어, 신뢰도가 높으면 사진의 얼굴 인식 기능은 특정 인물이 포함된 사진만 표시하지만 신뢰도가 낮을 경우에는 더 많은 정보를 표시하기 전에 사진에 해당 인물이 포함되어 있는지 확인하도록 요청합니다.
>




**When you know that confidence values correspond to result quality, you generally want to avoid showing results when confidence is low.** Especially when a feature is proactive and can make unbidden suggestions, poor results can cause people to be annoyed and even lose trust in the feature. For suggestions and proactive features, it’s a good idea to set a confidence threshold below which you don’t offer results.
> 신뢰도 값이 결과 품질에 해당한다는 것을 알게 되면 일반적으로 신뢰도가 낮을 때 결과를 표시하는 것을 피하고 싶어합니다. 특히 기능이 사전 예방적이고 거부할 수 없는 제안을 할 수 있는 경우, 좋지 않은 결과는 사람들을 짜증나게 하고 기능에 대한 신뢰를 잃게 할 수 있습니다. 제안 및 사전 예방적 기능의 경우 결과를 제공하지 않는 신뢰 임계값을 설정하는 것이 좋습니다.
>




# **[technologies-machine-learning] multiple-optinos**

Depending on the design of your feature, it might work best to present a single result or multiple results from which people can choose. Providing multiple options can give people a greater sense of control and can help bridge the gap between your model’s predictions and what people actually want. Multiple options can also encourage people to have realistic expectations about the types of results your app generates.
> 형상의 설계에 따라 사용자가 선택할 수 있는 단일 결과 또는 여러 결과를 제공하는 것이 가장 효과적일 수 있다. 여러 옵션을 제공하면 사람들에게 더 큰 통제력을 제공할 수 있으며 모형의 예측과 사람들이 실제로 원하는 것 사이의 차이를 메우는 데 도움이 될 수 있습니다. 또한 여러 옵션을 사용하면 앱이 생성하는 결과 유형에 대해 현실적인 기대를 가질 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/multiple-options_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/multiple-options_2x.png)

You might present multiple options to people in the following contexts:
> 다음 상황에서 사용자에게 여러 가지 선택사항을 제시할 수 있습니다:
>




- Suggested options, a proactive feature that suggests content to people based on the their past interactions. For example, For You recommendations from Apple Music.
- >  제안된 옵션, 사용자의 과거 상호 작용을 기반으로 사용자에게 콘텐츠를 제안하는 사전 예방적 기능. 예를 들어 Apple Music의 For You 권장 사항을 참조하십시오.

- Requested options, a reactive feature that suggests potential next steps to people based on their recent actions. For example, Quick Type suggestions.
- >  요청된 옵션, 즉 최근의 행동을 기반으로 사람들에게 잠재적인 다음 단계를 제안하는 반응형 기능입니다. 예를 들어 빠른 유형 제안이 있습니다.

- Corrections, which are actions people take to fix mistakes your app has made when it’s acting on their behalf. For example, the Photos Auto-Crop feature.
- >  수정: 앱이 자신을 대신하여 작동할 때 사람들이 저지른 실수를 수정하기 위해 취하는 조치입니다. 예를 들어, 사진 자동 자르기 기능이 있습니다.


**Prefer diverse options.** When possible, balance the accuracy of a response with the diversity of multiple options. For example, Apple Maps generally suggests more than one route to a destination, such as a route without tolls, a scenic route, or a route that uses highways. Providing different types of options helps people choose the one that they prefer and can also suggest new items that might interest them.
> 다양한 옵션을 선호합니다. 가능하면 반응의 정확성과 여러 옵션의 다양성의 균형을 맞추십시오. 예를 들어, Apple Maps는 일반적으로 통행료가 없는 경로, 경치 좋은 경로 또는 고속도로를 사용하는 경로와 같이 목적지로 가는 두 개 이상의 경로를 제안합니다. 다양한 유형의 옵션을 제공하면 사람들이 선호하는 항목을 선택하는 데 도움이 되고 관심을 가질 수 있는 새로운 항목을 제안할 수도 있습니다.
>




**In general, avoid providing too many options.** People must evaluate each option before making a choice, so more options increases cognitive load. When possible, list options on one screen so people don’t have to scroll to find the right one.
> 일반적으로 너무 많은 옵션을 제공하는 것을 피하라. 사람들은 선택을 하기 전에 각 옵션을 평가해야 한다. 그래서 더 많은 옵션이 인지 부하를 증가시킨다. 가능하면 한 화면에 옵션을 나열하여 사용자가 올바른 옵션을 찾기 위해 스크롤할 필요가 없도록 합니다.
>




**List the most likely option first.** When you know how your [confidence](../technologies/machine-learning/confidence) values correlate with the quality of your results, you might use them to rank the options. You might also consider using contextual information, such as the time of day or the current location, to help you determine the most likely option. If it makes sense in your app, select the first option by default so people can quickly achieve their goals without reading through every option.
> 가장 가능성이 높은 옵션을 먼저 나열하십시오. 신뢰 값이 결과의 품질과 어떤 상관 관계가 있는지 알게 되면 이 값을 사용하여 옵션의 순위를 매길 수 있습니다. 가장 가능성이 높은 옵션을 결정하는 데 도움이 되도록 시간 또는 현재 위치와 같은 상황별 정보를 사용하는 것을 고려할 수도 있습니다. 만약 당신의 앱에서 그것이 타당하다면, 사람들이 모든 옵션을 읽지 않고도 빠르게 목표를 달성할 수 있도록 기본적으로 첫 번째 옵션을 선택하세요.
>




**Make options easy to distinguish and choose.** For example, in a routing app, people often need to make route choices quickly to avoid going the wrong way. When options look similar, help people distinguish between them by providing a brief description of each one and taking particular care to highlight the differences. In cases where there are too many options to display in a single view, such as with content recommendations, consider grouping options in categories that people can scan rapidly.
> 예를 들어 라우팅 앱에서 사람들은 종종 잘못된 길로 가는 것을 피하기 위해 빠르게 경로를 선택해야 한다. 옵션이 비슷하게 보일 때 각 옵션에 대한 간단한 설명을 제공하고 차이점을 강조하기 위해 특히 주의를 기울임으로써 사람들이 옵션을 구별할 수 있도록 도와줍니다. 콘텐츠 권장사항과 같이 단일 보기에 표시할 수 있는 옵션이 너무 많은 경우 사용자가 빠르게 검색할 수 있는 범주의 그룹화 옵션을 고려하십시오.
>




**Learn from selections when it makes sense.** People give you [implicit feedback](../technologies/machine-learning/implicit-feedback) every time they make a selection. When it doesn’t adversely affect the user experience, use this feedback to refine the options you provide and increase the chance that you’ll present the most likely option first. In general, continuing to offer incorrect results is likely to decrease people’s trust in the quality of your app’s predictions.
> 적절한 선택을 통해 학습하십시오. 사람들은 선택을 할 때마다 암묵적인 피드백을 제공합니다. 사용자 환경에 부정적인 영향을 미치지 않는 경우 이 피드백을 사용하여 제공하는 옵션을 세분화하고 가장 가능성이 높은 옵션을 먼저 제시할 가능성을 높입니다. 일반적으로 잘못된 결과를 계속 제공하면 앱의 예측 품질에 대한 사람들의 신뢰가 떨어질 수 있습니다.
>




# **[technologies-machine-learning] limitations**

Every feature — whether it’s based on machine learning or not — has certain limitations to what it can deliver. In general, there are two types of limitations: things a feature can’t do well and things a feature can’t do at all. When there’s a mismatch between people’s expectations about a feature and what the feature can actually accomplish, a limitation can seem like a defect. For example, people might expect:
> 기계 학습을 기반으로 하든 아니든 모든 기능은 제공할 수 있는 것에 일정한 한계가 있다. 일반적으로 기능이 제대로 수행할 수 없는 것과 기능이 전혀 수행할 수 없는 것의 두 가지 유형의 제한이 있습니다. 기능에 대한 사람들의 기대와 기능이 실제로 달성할 수 있는 것 사이에 불일치가 있을 때, 제한은 결함처럼 보일 수 있습니다. 예를 들어, 사람들은 다음을 기대할 수 있다:
>




- Photos to perform a search that covers every category they can imagine
- >  상상할 수 있는 모든 범주를 포함하는 검색을 수행할 사진

- Siri to respond to queries that aren’t well defined, like "What is the meaning of life?"
- >  시리는 "삶의 의미가 무엇인가?"와 같이 잘 정의되지 않은 질문에 응답한다

- FaceID to work from every angle
- >  모든 각도에서 작동하는 Face ID


An important part of the design process is to identify the scenarios where limitations impact the user experience and design ways to help people work with them. For example:
> 설계 프로세스의 중요한 부분은 한계가 사용자 경험에 영향을 미치는 시나리오를 식별하고 사람들이 한계를 가지고 작업할 수 있도록 방법을 설계하는 것이다. 예:
>




- Set people’s expectations before they use the feature
- >  기능을 사용하기 전에 사용자의 기대치 설정

- Show people how to get the best results while they’re using the feature
- >  기능을 사용하는 동안 최상의 결과를 얻는 방법을 사람들

- When inferior results occur, explain why so that people can understand the feature better
- >  열등한 결과가 발생했을 때, 사람들이 그 특징을 더 잘 이해할 수 있도록 그 이유를 설명한다


![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/limitations_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/limitations_2x.png)

**Help people establish realistic expectations.** When a limitation may have a serious effect on user experience but happens rarely, consider making people aware of the limitation before they use your app or feature. You might describe the limitation in marketing materials or within the feature’s context so that people can decide how they want to rely on the feature. If the effects of a limitation aren’t serious, you can help set people’s expectations by providing [attributions](../technologies/machine-learning/attribution).
> 제한이 사용자 경험에 심각한 영향을 미칠 수 있지만 드물게 발생하는 경우 앱이나 기능을 사용하기 전에 사용자에게 제한을 알리는 것을 고려하십시오. 마케팅 자료 또는 기능의 컨텍스트 내에서 제한 사항을 설명하여 사용자가 기능에 어떻게 의존할지 결정할 수 있습니다. 제한의 영향이 심각하지 않은 경우 속성을 제공하여 사람들의 기대치를 설정하는 데 도움이 될 수 있습니다.
>




**Demonstrate how to get the best results.** If you don’t provide guidance for using a feature, people may assume it will do everything they want. When you proactively show people how to get good results, you help them benefit from the feature and establish a more accurate mental model of the feature’s capabilities. There are many ways to show people the best ways to use a feature, such as:
> 최상의 결과를 얻는 방법을 시연하십시오. 기능 사용에 대한 지침을 제공하지 않으면 사람들은 기능이 원하는 모든 것을 수행할 것이라고 생각할 수 있습니다. 사람들에게 좋은 결과를 얻는 방법을 적극적으로 보여주면, 사람들이 기능을 통해 이익을 얻을 수 있도록 돕고 기능의 기능에 대한 보다 정확한 정신적 모델을 확립할 수 있습니다. 사람들에게 기능을 사용하는 가장 좋은 방법을 보여주는 방법은 다음과 같습니다:
>




- Use placeholder text to suggest input. In Photos, the search bar displays the text “Photos, People, Places...” to help people understand what they can search for before they begin typing. Photos also displays a description of how it scans the photo library to offer search suggestions.
- >  자리 표시자 텍스트를 사용하여 입력을 제안합니다. 사진에서 검색 표시줄에는 "사진, 사람, 장소..."라는 텍스트가 표시되어 입력을 시작하기 전에 검색할 수 있는 항목을 쉽게 이해할 수 있습니다. 사진은 또한 검색 제안을 제공하기 위해 사진 라이브러리를 검색하는 방법에 대한 설명을 표시합니다.

- As people interact with the feature, provide feedback on their actions to guide them towards a result without overwhelming them. For example, while people are interacting with Animoji, the feature responds to current conditions and suggests how people can improve their results by adjusting the lighting or moving closer to the camera.
- >  사람들이 기능과 상호 작용할 때, 그들을 압도하지 않고 결과로 안내하기 위해 그들의 행동에 대한 피드백을 제공합니다. 예를 들어, 사람들이 Animoji와 상호 작용하는 동안, 이 기능은 현재 상태에 반응하고 사람들이 조명을 조정하거나 카메라에 더 가까이 이동함으로써 결과를 개선할 수 있는 방법을 제안한다.

- Suggest alternative ways to accomplish the user’s goal instead of showing no results. To do this successfully, you need to understand the goal well enough to suggest alternatives that make sense. For example, if people ask Siri to set a timer on a Mac, Siri suggests setting a reminder instead, because timers aren’t available in macOS. This suggestion makes sense because Siri understands that the goal is to receive an alert at a certain time.
- >  결과를 보여주지 않고 사용자의 목표를 달성할 수 있는 대안을 제시합니다. 이것을 성공적으로 하기 위해서는, 당신은 타당한 대안을 제시할 수 있을 정도로 목표를 잘 이해해야 한다. 예를 들어, 사람들이 시리에게 맥에서 타이머를 설정하라고 하면, 시리는 대신 미리 알림을 설정할 것을 제안한다. 이 제안은 시리가 특정 시간에 경보를 수신하는 것이 목표라는 것을 이해하기 때문에 타당하다.


**Explain how limitations can cause unsatisfactory results.** People can get frustrated when it seems that your feature works intermittently. Ideally, your feature can recognize and describe the reasons for poor results to make people aware of the limitations and help them to adjust their expectations. For example, Animoji tells people that it doesn’t work well in the dark.
> 제한이 어떻게 불만족스러운 결과를 초래할 수 있는지 설명하십시오. 사람들은 당신의 기능이 간헐적으로 작동하는 것처럼 보일 때 좌절할 수 있습니다. 이상적인 기능은 좋지 않은 결과의 원인을 인식하고 설명하여 사람들에게 한계를 인식시키고 기대를 조정하는 데 도움이 될 수 있습니다. 예를 들어, Animoji는 사람들에게 어둠 속에서는 잘 작동하지 않는다고 말합니다.
>




**Consider telling people when limitations are resolved.** When people use a feature frequently, they learn to avoid the interactions that fail because of the feature’s limitations. When you update your app to remove a limitation, you might want to notify people so that they can adjust their mental model of your feature and return to interactions they’d previously avoided.
> 사용자가 기능을 자주 사용할 때 기능의 제한으로 인해 실패하는 상호 작용을 피하는 방법을 배울 수 있습니다. 제한을 제거하기 위해 앱을 업데이트할 때 사용자의 기능에 대한 마인드 모델을 조정하고 이전에 피했던 상호 작용으로 돌아갈 수 있도록 사람들에게 알릴 수 있습니다.
>




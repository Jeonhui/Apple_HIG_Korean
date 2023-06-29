# **[technologies-machine-learning] machine-learning-roles**

# **Defining the role of machine learning in your app**
> 앱에서 기계 학습의 역할 정의
>




Machine learning systems vary widely, and the ways an app can use machine learning vary widely, too. As you approach the design of your app, think about how its features use machine learning in each of the following areas.
> 머신 러닝 시스템은 매우 다양하며, 앱이 머신 러닝을 사용할 수 있는 방법도 매우 다양하다. 당신이 앱의 디자인에 접근하면서, 그것의 기능이 다음 각 영역에서 머신러닝을 어떻게 사용하는지 생각해보라.
>




# **Critical or complementary**

If an app can still work without the feature that machine learning enables, machine learning is complementary to the app; otherwise, it’s a critical dependency. For example:
> 만약 앱이 기계 학습이 가능하게 하는 기능 없이도 작동할 수 있다면, 기계 학습은 앱을 보완하는 것이다. 그렇지 않으면, 그것은 중요한 의존성이다. 예:
>




- The keyboard uses machine learning to provide QuickType suggestions. Because the keyboard still works without these suggestions, machine learning plays a complementary role in the app.
- >  키보드는 기계 학습을 사용하여 QuickType 제안을 제공합니다. 키보드는 여전히 이러한 제안 없이 작동하기 때문에, 기계 학습은 앱에서 보완적인 역할을 한다.

- Face ID relies on machine learning to enable accurate face recognition. Without machine learning, Face ID would not work.
- >  얼굴 ID는 기계 학습에 의존하여 정확한 얼굴 인식을 가능하게 한다. 기계 학습이 없다면 페이스 ID는 작동하지 않을 것이다.


In general, the more critical an app feature is, the more people need accurate and reliable results. On the other hand, if a complementary feature delivers results that aren’t always of the highest quality, people may be more forgiving.
> 일반적으로 앱 기능이 중요할수록 사람들은 더 정확하고 신뢰할 수 있는 결과를 필요로 한다. 반면에, 보완적인 특징이 항상 최고의 품질이 아닌 결과를 제공한다면, 사람들은 더 관대해질 수 있다.
>




# **Private or public**

Machine learning results depend on data. To make good design decisions, you need to know as much as possible about the types of data your app feature needs. In general, the more sensitive the data, the more serious the consequences of inaccurate or unreliable results. For example:
> 머신러닝 결과는 데이터에 따라 달라진다. 올바른 설계 결정을 내리기 위해서는 앱 기능에 필요한 데이터 유형에 대해 가능한 한 많이 알아야 합니다. 일반적으로 민감한 데이터일수록 부정확하거나 신뢰할 수 없는 결과의 결과가 더 심각합니다. 예:
>




- If a health app misinterprets data and incorrectly recommends a visit to the doctor, people are likely to experience anxiety and may lose trust in the app.
- >  건강 앱이 데이터를 잘못 해석해 진료를 잘못 추천하면 사람들이 불안감을 느낄 가능성이 높고 앱에 대한 신뢰를 잃을 수도 있다.

- If a music app misinterprets data and recommends an artist that people don’t like, they’re likely to view the result as an inconsequential mistake.
- >  만약 음악 앱이 데이터를 잘못 해석하고 사람들이 좋아하지 않는 아티스트를 추천한다면, 그들은 그 결과를 중요하지 않은 실수로 볼 가능성이 높다.


As with critical app features, features that use sensitive data should prioritize accuracy and reliability. Regardless of the sensitivity of the data, all apps must protect user privacy at all times.
> 중요한 앱 기능과 마찬가지로 중요한 데이터를 사용하는 기능은 정확성과 신뢰성을 우선시해야 한다. 데이터의 민감도와 상관없이 모든 앱은 항상 사용자의 개인 정보를 보호해야 한다.
>




# **Proactive or reactive**

A *proactive* app feature provides results without people requesting it to do so. Proactive features can prompt new tasks and interactions by providing unexpected, sometimes serendipitous results. In contrast, a *reactive* app feature provides results when people ask for them or when they take certain actions. Reactive features typically help people as they perform their current task. For example:
> 사전 예방적 앱 기능은 사용자가 요청하지 않고 결과를 제공합니다. 사전 예방적 기능은 예상치 못한, 때로는 우연한 결과를 제공함으로써 새로운 작업과 상호 작용을 촉진할 수 있습니다. 대조적으로, 반응형 앱 기능은 사람들이 요청하거나 특정 조치를 취할 때 결과를 제공한다. 반응형 기능은 일반적으로 사람들이 현재 작업을 수행할 때 도움이 됩니다. 예:
>




- QuickType suggests words in reaction to what people type.
- >  QuickType은 사람들이 입력하는 것에 대한 반응으로 단어를 제안합니다.

- Siri Suggestions can proactively suggest a shortcut based on people’s recent routines.
- >  시리 제안은 사람들의 최근 일상을 바탕으로 바로 가기를 능동적으로 제안할 수 있다.


Because people don’t ask for the results that a proactive feature provides, they may have less tolerance for low-quality information. To reduce the possibility that people will find proactive results intrusive or irrelevant, you may need to use additional data for the feature.
> 사람들은 사전 예방적 기능이 제공하는 결과를 요구하지 않기 때문에 낮은 품질의 정보에 대한 관용이 적을 수 있습니다. 사용자가 사전 예방적 결과가 방해가 되거나 관련이 없다고 생각할 가능성을 줄이기 위해 기능에 추가 데이터를 사용해야 할 수도 있습니다.
>




# **Visible or invisible**

Apps may use machine learning to support visible or invisible features. People are usually aware of visible app features because such features tend to offer suggestions or choices that people view and interact with. For example, a visible keyboard feature tries to guess the word that people are typing and presents the most likely words in a list from which people choose.
> 앱은 기계 학습을 사용하여 눈에 보이거나 보이지 않는 기능을 지원할 수 있다. 사람들은 일반적으로 눈에 보이는 앱 기능을 알고 있는데, 이는 이러한 기능이 사람들이 보고 상호 작용하는 제안이나 선택을 제공하는 경향이 있기 때문이다. 예를 들어, 보이는 키보드 기능은 사용자가 입력하는 단어를 추측하고 사용자가 선택한 목록에 가장 가능성이 높은 단어를 표시합니다.
>




As the name suggests, an invisible feature provides results that aren’t obvious to people. For example, the keyboard learns how people type over time so it can optimize the tap area for each key and help them make fewer typing mistakes. Because this app feature improves the typing experience without requiring people to make choices, many people aren’t aware that the feature exists.
> 이름에서 알 수 있듯이 보이지 않는 기능은 사람들에게 명확하지 않은 결과를 제공합니다. 예를 들어 키보드는 시간이 지남에 따라 사람들이 입력하는 방법을 학습하므로 각 키에 대한 탭 영역을 최적화하고 입력 오류를 줄일 수 있습니다. 이 앱 기능은 사람들이 선택할 필요 없이 타이핑 경험을 향상시키기 때문에, 많은 사람들은 그 기능이 존재한다는 것을 알지 못한다.
>




People’s impression of the reliability of results can differ depending on whether a feature is visible or invisible. With a visible feature, people form an opinion about the feature’s reliability as they choose from among its results. It’s harder for an invisible feature to communicate its reliability — and potentially receive feedback — because people may not be aware of the feature at all.
> 결과의 신뢰성에 대한 사람들의 인상은 특징이 보이느냐 보이지 않느냐에 따라 달라질 수 있다. 가시적인 기능을 통해 사람들은 결과 중에서 선택할 때 기능의 신뢰성에 대한 의견을 형성한다. 보이지 않는 기능은 사람들이 그 기능을 전혀 인식하지 못할 수 있기 때문에 신뢰성을 전달하고 잠재적으로 피드백을 받는 것이 더 어렵습니다.
>




# **Dynamic or static**

All machine learning models can improve, but some improve dynamically, as people interact with the app feature, and others improve offline and affect the feature only when the app updates. For example:
> 모든 기계 학습 모델은 개선될 수 있지만, 사람들이 앱 기능과 상호 작용하면서 동적으로 개선되는 것도 있고, 오프라인에서 개선되어 앱이 업데이트되어야만 기능에 영향을 미치는 것도 있다. 예:
>




- Face ID improves dynamically as people’s faces gradually change over time.
- >  얼굴 ID는 시간이 지남에 따라 사람들의 얼굴이 점차 변화함에 따라 역동적으로 개선된다.

- Photos improves its object recognition capabilities with every new iOS release.
- >  사진은 iOS가 새로 출시될 때마다 객체 인식 기능을 향상시킵니다.


In addition to the frequency of app updates, static or dynamic improvements can affect other parts of the user experience, too. For example, dynamic features often incorporate forms of [calibration](../technologies/machine-learning/calibration)and feedback (either [implicit](../technologies/machine-learning/implicit-feedback) or [explicit](../technologies/machine-learning/explicit-feedback)), whereas static features may not.
> 앱 업데이트 빈도 외에도 정적 또는 동적 개선은 사용자 경험의 다른 부분에도 영향을 미칠 수 있습니다. 예를 들어 동적 특징은 종종 (암묵적이거나 명시적인) 교정과 피드백의 형태를 포함하는 반면 정적 특징은 그렇지 않을 수 있다.
>




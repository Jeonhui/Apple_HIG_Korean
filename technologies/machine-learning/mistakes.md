# **[technologies-machine-learning] mistakes**

It’s inevitable that your app will make mistakes. Although people may not expect perfection, mistakes can damage their experience and decrease their trust in your app. To help you avoid negative consequences, it’s crucial to:
> 당신의 앱이 실수하는 것은 불가피하다. 비록 사람들이 완벽을 기대하지 않을 수도 있지만, 실수는 그들의 경험을 손상시키고 당신의 앱에 대한 신뢰를 떨어뜨릴 수 있다. 부정적인 결과를 방지하려면 다음을 수행해야 합니다:
>




- Anticipate mistakes. As much as possible, design ways to avoid mistakes and mitigate them when they happen.
- >  실수를 예상하다. 가능한 한 실수를 방지하고 실수가 발생했을 때 이를 완화할 수 있는 방법을 설계하십시오.

- Help people handle mistakes. Mistakes can have a wide range of consequences, so the tools you provide to handle a mistake must be able to address those consequences.
- >  사람들이 실수를 처리할 수 있도록 도와줍니다. 실수는 광범위한 결과를 초래할 수 있으므로 실수를 처리하기 위해 제공하는 도구는 그러한 결과를 해결할 수 있어야 합니다.

- Learn from mistakes when doing so improves your app. In some cases, learning from a mistake might have undesirable effects, such as causing unpredictability in the user experience. When it makes sense, use each mistake as a data point that can refine your machine learning models and improve your app.
- >  실수를 통해 학습하면 앱이 향상됩니다. 어떤 경우에는 실수로부터 학습하는 것이 사용자 경험에 예측 불가능성을 야기하는 것과 같은 바람직하지 않은 영향을 미칠 수 있다. 타당하다면, 각각의 실수를 당신의 머신 러닝 모델을 개선하고 당신의 앱을 개선할 수 있는 데이터 포인트로 사용하세요.


There are several machine learning patterns that can help you address mistakes:
> 실수를 해결하는 데 도움이 될 수 있는 몇 가지 기계 학습 패턴이 있습니다:
>




- [Limitations](../technologies/machine-learning/limitations) help you set people’s expectations about the accuracy of your suggestions.
- >  제한은 제안의 정확성에 대한 사람들의 기대치를 설정하는 데 도움이 됩니다.

- [Corrections](../technologies/machine-learning/corrections) give people a way to be successful even when your results are wrong.
- >  교정은 여러분의 결과가 틀렸을 때도 사람들이 성공할 수 있는 방법을 제공합니다.

- [Attributions](../technologies/machine-learning/attribution) give people insight into where suggestions come from, which can help them understand mistakes.
- >  귀인은 사람들에게 제안이 어디서 왔는지에 대한 통찰력을 주고, 이것은 그들이 실수를 이해하는 것을 도울 수 있다.

- [Confidence](../technologies/machine-learning/confidence) helps you gauge the quality of your results, which can impact how you present them.
- >  자신감은 결과의 품질을 측정하는 데 도움이 되며 결과를 제시하는 방식에 영향을 미칠 수 있습니다.

- Feedback — both [explicit](../technologies/machine-learning/explicit-feedback) and [implicit](../technologies/machine-learning/implicit-feedback) — lets people tell you about mistakes that you might not be aware of.
- >  명시적이든 암시적이든 피드백을 통해 사람들은 사용자가 인식하지 못할 수 있는 실수에 대해 말할 수 있습니다.


**Understand the significance of a mistake’s consequences.** For example, incorrect keyboard suggestions might annoy people, but suggesting a travel route that results in a missed flight is a serious inconvenience. Show empathy by providing corrective actions or tools that match the seriousness of the mistake.
> 예를 들어, 잘못된 키보드 제안은 사람들을 짜증나게 할 수 있지만, 비행기를 놓칠 수 있는 여행 경로를 제안하는 것은 심각한 불편을 초래한다. 실수의 심각성에 맞는 시정 조치나 도구를 제공함으로써 공감을 보여줍니다.
>




**Make it easy for people to correct frequent or predictable mistakes.** If you don’t give people an easy way to correct mistakes, they can lose trust in your app.
> 사람들이 자주 또는 예측 가능한 실수를 쉽게 수정할 수 있도록 하십시오. 실수를 쉽게 수정할 수 있는 방법을 사람들에게 제공하지 않으면 앱에 대한 신뢰를 잃을 수 있습니다.
>




**Continuously update your feature to reflect people’s evolving interests and preferences.** One way to help you improve your understanding of users and avoid mistakes is to use implicit feedback to discover changes in their tastes and habits. You should also update your feature with domain-specific information, such as current trends in popular entertainment. Ideally, people don’t have to do any work to benefit from improvements in your app.
> 사람들의 진화하는 관심사와 선호도를 반영하기 위해 기능을 지속적으로 업데이트하십시오. 사용자에 대한 이해를 높이고 실수를 방지하는 한 가지 방법은 암묵적 피드백을 사용하여 사용자의 취향과 습관의 변화를 발견하는 것입니다. 또한 인기 있는 엔터테인먼트의 현재 추세와 같은 도메인별 정보로 기능을 업데이트해야 합니다. 이상적으로, 사람들은 당신의 앱의 개선으로부터 이익을 얻기 위해 어떤 일도 할 필요가 없다.
>




**When possible, address mistakes without complicating the UI.** Some patterns, such as corrections and limitations, tend to integrate seamlessly with an app’s UI, whereas others, like attributions, can be harder to integrate. Balance a pattern’s effect on the UI with its potential for compounding the mistake. For example, if you update the UI with an attribution that turns out to be wrong, the effect of the original mistake is magnified.
> 가능하면 UI를 복잡하게 만들지 않고 실수를 해결하십시오. 수정 및 제한과 같은 일부 패턴은 앱의 UI와 완벽하게 통합되는 경향이 있는 반면, 속성과 같은 다른 패턴은 통합하기가 더 어려울 수 있습니다. 패턴이 UI에 미치는 영향과 오류를 악화시킬 수 있는 가능성의 균형을 맞춥니다. 예를 들어 잘못된 속성으로 UI를 업데이트하면 원래 실수의 효과가 확대됩니다.
>




**Be especially careful to avoid mistakes in proactive features.** A proactive feature — like a suggestion based on user behaviors — promises valuable results without asking people to do anything to get them. However, because people don’t request a proactive feature, they often have less patience with its mistakes. Mistakes made by proactive features can also cause people to feel that they have less control.
> 사전 예방적 기능의 실수를 방지하기 위해 특히 주의해야 합니다. 사전 예방적 기능은 사용자 행동에 기반한 제안과 같이 사람들에게 어떤 것도 요구하지 않고 귀중한 결과를 약속합니다. 그러나 사람들은 사전 예방적 기능을 요청하지 않기 때문에 종종 실수에 대한 인내심이 떨어진다. 사전 예방적 기능으로 인한 실수는 사람들로 하여금 자신이 통제력이 떨어진다고 느끼게 할 수도 있다.
>




**As you work on reducing mistakes in one area, always consider the effect your work has on other areas and overall accuracy.** For example, optimizing an image recognition app to improve how it recognizes dogs might result in a decreased ability to recognize cats. As your models evolve, be prepared for mistakes to evolve, too. Use what you know about people’s preferences to help you determine the areas to focus on.
> 한 영역에서 실수를 줄이는 작업을 할 때는 항상 다른 영역과 전체적인 정확도에 미치는 영향을 고려해야 합니다. 예를 들어, 이미지 인식 앱을 최적화하여 개를 인식하는 방법을 개선하면 고양이를 인식하는 능력이 저하될 수 있습니다. 모델이 발전함에 따라, 실수도 발전할 수 있도록 준비하십시오. 사용자의 환경설정에 대해 알고 있는 내용을 사용하여 집중할 영역을 결정할 수 있습니다.
>




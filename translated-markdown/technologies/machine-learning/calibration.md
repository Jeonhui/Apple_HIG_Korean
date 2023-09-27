# **[technologies-machine-learning] calibration**

Calibration is a process during which people provide information that an app feature needs before it can function. To use Face ID, for example, you must first scan your face.
> 보정은 사용자가 앱 기능이 작동하기 전에 필요한 정보를 제공하는 프로세스입니다. 예를 들어, 얼굴 ID를 사용하려면 먼저 얼굴을 스캔해야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/calibration_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/calibration_2x.png)

In general, only use calibration when your feature can’t function without that initial information. If your feature can work without calibration, consider using other ways to gather information about people, such as [implicit feedback](../technologies/machine-learning/implicit-feedback) or possibly [explicit feedback](../technologies/machine-learning/explicit-feedback).
> 일반적으로 초기 정보 없이 기능이 작동할 수 없는 경우에만 보정을 사용하십시오. 기능이 보정 없이 작동할 수 있는 경우 암시적 피드백 또는 명시적 피드백과 같은 다른 방법을 사용하여 사용자에 대한 정보를 수집하는 것을 고려해 보십시오.
>




**Always secure people’s information.** During calibration, people may provide sensitive information and you must make sure it remains secure.
> 항상 사용자의 정보를 보호하십시오. 교정하는 동안 사용자가 중요한 정보를 제공할 수 있으므로 사용자는 이 정보를 안전하게 유지해야 합니다.
>




**Be clear about why you need people’s information.** Typically, calibration is required before people can use a feature, so it’s essential that they understand the value of providing their information. As you briefly describe how people can benefit from your feature, focus on what it does rather than on how it works.
> 사람들의 정보가 필요한 이유를 명확히 하라. 일반적으로 사람들이 기능을 사용하기 전에 보정이 필요하므로 정보를 제공하는 것의 가치를 이해하는 것이 필수적이다. 사람들이 당신의 기능에서 어떻게 이익을 얻을 수 있는지 간략하게 설명할 때, 그것이 어떻게 작동하는지보다는 그것이 무엇을 하는지에 초점을 맞추어라.
>




**Collect only the most essential information.** Designing a unique experience that has a tight focus on getting a small amount of information can make people more comfortable participating in the process and increase their trust in your app.
> 가장 중요한 정보만 수집하십시오. 적은 양의 정보를 얻는 데 집중하는 독특한 경험을 설계하면 사람들이 프로세스에 더 편안하게 참여하고 앱에 대한 신뢰를 높일 수 있습니다.
>




**Avoid asking people to participate in calibration more than once.** Also, it’s best when calibration occurs early in the user experience. As people continue using your app or feature, you can use implicit or explicit feedback to evolve your information about them without asking them to participate again. An exception is a feature that needs calibration with an object instead of a person. For example, an app that helps people improve their baseball swing might need to calibrate with each new baseball field.
> 보정 작업에 두 번 이상 참여하도록 요청하지 마십시오. 또한 사용자 경험 초기에 보정 작업이 수행되는 경우가 가장 좋습니다. 사람들이 계속해서 당신의 앱이나 기능을 사용할 때, 당신은 암묵적이거나 명시적인 피드백을 사용하여 그들에게 다시 참여하도록 요청하지 않고 그들에 대한 당신의 정보를 발전시킬 수 있다. 예외는 사람 대신 개체로 보정해야 하는 기능입니다. 예를 들어, 사람들이 그들의 야구 스윙을 향상시키는 것을 돕는 앱은 각각의 새로운 야구장에 맞춰 조정할 필요가 있을 수 있다.
>




**Make calibration quick and easy.** Even a brief calibration experience takes time and requires effort from people. An ideal calibration experience makes it easy for people to respond, without compromising the quality of the information they provide. The following guidelines can help you create a streamlined calibration experience.
> 빠르고 쉽게 교정할 수 있습니다. 짧은 교정 경험에도 시간이 걸리고 사람들의 노력이 필요합니다. 이상적인 교정 환경은 사람들이 제공하는 정보의 품질을 손상시키지 않고 쉽게 응답할 수 있도록 합니다. 다음 지침은 간소화된 교정 환경을 만드는 데 도움이 될 수 있습니다.
>




- Focus on getting a few pieces of important information and infer the rest from other sources or getting people’s feedback.
- >  몇 가지 중요한 정보를 얻는 데 집중하고 나머지는 다른 출처에서 추론하거나 사람들의 피드백을 얻으세요.

- Avoid asking for information that most people would have to look up.
- >  대부분의 사람들이 찾아봐야 할 정보를 묻는 것을 피하세요.

- Avoid asking people to perform actions that might be difficult.
- >  사용자에게 어려울 수 있는 작업을 수행하도록 요청하지 마십시오.


**Make sure people know how to perform calibration successfully.** After people decide to participate in calibration, give them an explicit goal and show their progress towards it. For example, Face ID calibration briefly describes what people need to do and changes the appearance of the tick marks encircling the face as people progress through scanning.
> 사람들이 교정을 성공적으로 수행하는 방법을 알고 있는지 확인하십시오. 사람들이 교정에 참여하기로 결정한 후, 그들에게 명확한 목표를 제시하고 그 목표를 향한 그들의 진전을 보여줍니다. 예를 들어, 얼굴 ID 보정은 사람들이 무엇을 해야 하는지 간략하게 설명하고 사람들이 스캔을 통해 진행함에 따라 얼굴 주위의 눈금 모양을 변경합니다.
>




**Immediately provide assistance if progress stalls.** When progress stalls, people can feel stuck or powerless, and they may lose trust in your app. In this situation, it’s crucial to give people actionable recommendations that quickly get them back on track. As you provide this guidance, never imply that something’s wrong or that people are at fault, and never leave people without a clear next step.
> 진행이 정지되면 즉시 지원을 제공합니다. 진행이 정지되면 사람들은 정체되거나 무력감을 느낄 수 있으며, 앱에 대한 신뢰를 잃을 수 있습니다. 이러한 상황에서, 사람들이 빠르게 정상 궤도에 오를 수 있도록 실행 가능한 권장 사항을 제공하는 것이 중요하다. 여러분이 이 지침을 제공할 때, 어떤 것이 잘못되었거나 사람들에게 잘못이 있다는 것을 절대 암시하지 말고, 명확한 다음 단계 없이 사람들을 떠나지 마세요.
>




**Confirm success.** The moment people successfully complete calibration, reward their time and effort by giving them a clear path towards using the feature. Providing an explicit completion to the calibration experience reinforces the unique nature of the experience and helps people switch their focus to your feature.
> 성공을 확인합니다. 사람들이 성공적으로 교정을 완료하는 순간, 그들에게 기능을 사용할 수 있는 명확한 경로를 제공함으로써 그들의 시간과 노력에 보답합니다. 보정 경험을 명시적으로 완료하면 경험의 고유한 특성이 강화되고 사람들이 사용자의 기능으로 초점을 전환하는 데 도움이 됩니다.
>




**Let people cancel calibration at any time.** Make sure you give people an easy way to cancel the experience at any point and avoid implying any judgement about their choice. There’s no need to provide any messaging that mentions the canceled calibration, because the next time people attempt to use the feature, they’ll have another chance to participate.
> 사람들이 언제든지 교정을 취소할 수 있도록 합니다. 사람들에게 언제든지 경험을 취소할 수 있는 쉬운 방법을 제공하고 선택에 대한 판단을 암시하지 않도록 하십시오. 다음에 사람들이 이 기능을 사용하려고 할 때, 그들은 또 다른 참여 기회를 갖게 될 것이기 때문에, 취소된 보정을 언급하는 메시지를 제공할 필요가 없다.
>




**Give people a way to update or remove information they provided during calibration.** Letting people edit their information gives them more control and can lead them to have greater trust in your app. Although the calibration experience can help people edit their responses, it’s a good idea to let people edit their information outside of the calibration experience so that they feel free to make changes at any time.
> 보정 중에 제공한 정보를 업데이트하거나 제거할 수 있는 방법을 사용자에게 제공합니다. 사용자가 정보를 편집하도록 허용하면 사용자가 더 많은 제어 권한을 갖게 되고 사용자의 앱을 더 신뢰할 수 있습니다. 보정 경험은 사용자의 반응을 편집하는 데 도움이 될 수 있지만, 사용자가 언제든지 자유롭게 변경할 수 있도록 보정 경험 외의 정보를 편집하도록 하는 것이 좋습니다.
>




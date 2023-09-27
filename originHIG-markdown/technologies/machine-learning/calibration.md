# **[technologies-machine-learning] Calibration**

Calibration is a process during which people provide information that an app feature needs before it can function. To use Face ID, for example, you must first scan your face.

![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/calibration_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/calibration_2x.png)

In general, only use calibration when your feature can’t function without that initial information. If your feature can work without calibration, consider using other ways to gather information about people, such as [implicit feedback](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/implicit-feedback) or possibly [explicit feedback](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/explicit-feedback).

**Always secure people’s information.** During calibration, people may provide sensitive information and you must make sure it remains secure.

**Be clear about why you need people’s information.** Typically, calibration is required before people can use a feature, so it’s essential that they understand the value of providing their information. As you briefly describe how people can benefit from your feature, focus on what it does rather than on how it works.

**Collect only the most essential information.** Designing a unique experience that has a tight focus on getting a small amount of information can make people more comfortable participating in the process and increase their trust in your app.

**Avoid asking people to participate in calibration more than once.** Also, it’s best when calibration occurs early in the user experience. As people continue using your app or feature, you can use implicit or explicit feedback to evolve your information about them without asking them to participate again. An exception is a feature that needs calibration with an object instead of a person. For example, an app that helps people improve their baseball swing might need to calibrate with each new baseball field.

**Make calibration quick and easy.** Even a brief calibration experience takes time and requires effort from people. An ideal calibration experience makes it easy for people to respond, without compromising the quality of the information they provide. The following guidelines can help you create a streamlined calibration experience.

- Focus on getting a few pieces of important information and infer the rest from other sources or getting people’s feedback.
- Avoid asking for information that most people would have to look up.
- Avoid asking people to perform actions that might be difficult.

**Make sure people know how to perform calibration successfully.** After people decide to participate in calibration, give them an explicit goal and show their progress towards it. For example, Face ID calibration briefly describes what people need to do and changes the appearance of the tick marks encircling the face as people progress through scanning.

**Immediately provide assistance if progress stalls.** When progress stalls, people can feel stuck or powerless, and they may lose trust in your app. In this situation, it’s crucial to give people actionable recommendations that quickly get them back on track. As you provide this guidance, never imply that something’s wrong or that people are at fault, and never leave people without a clear next step.

**Confirm success.** The moment people successfully complete calibration, reward their time and effort by giving them a clear path towards using the feature. Providing an explicit completion to the calibration experience reinforces the unique nature of the experience and helps people switch their focus to your feature.

**Let people cancel calibration at any time.** Make sure you give people an easy way to cancel the experience at any point and avoid implying any judgement about their choice. There’s no need to provide any messaging that mentions the canceled calibration, because the next time people attempt to use the feature, they’ll have another chance to participate.

**Give people a way to update or remove information they provided during calibration.** Letting people edit their information gives them more control and can lead them to have greater trust in your app. Although the calibration experience can help people edit their responses, it’s a good idea to let people edit their information outside of the calibration experience so that they feel free to make changes at any time.
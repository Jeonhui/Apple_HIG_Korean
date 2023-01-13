# **[technologies-machine-learning] limitations**

Every feature — whether it’s based on machine learning or not — has certain limitations to what it can deliver. In general, there are two types of limitations: things a feature can’t do well and things a feature can’t do at all. When there’s a mismatch between people’s expectations about a feature and what the feature can actually accomplish, a limitation can seem like a defect. For example, people might expect:

- Photos to perform a search that covers every category they can imagine
- Siri to respond to queries that aren’t well defined, like "What is the meaning of life?"
- FaceID to work from every angle

An important part of the design process is to identify the scenarios where limitations impact the user experience and design ways to help people work with them. For example:

- Set people’s expectations before they use the feature
- Show people how to get the best results while they’re using the feature
- When inferior results occur, explain why so that people can understand the feature better

![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/limitations_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/limitations_2x.png)

**Help people establish realistic expectations.** When a limitation may have a serious effect on user experience but happens rarely, consider making people aware of the limitation before they use your app or feature. You might describe the limitation in marketing materials or within the feature’s context so that people can decide how they want to rely on the feature. If the effects of a limitation aren’t serious, you can help set people’s expectations by providing [attributions](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/attribution).

**Demonstrate how to get the best results.** If you don’t provide guidance for using a feature, people may assume it will do everything they want. When you proactively show people how to get good results, you help them benefit from the feature and establish a more accurate mental model of the feature’s capabilities. There are many ways to show people the best ways to use a feature, such as:

- Use placeholder text to suggest input. In Photos, the search bar displays the text “Photos, People, Places...” to help people understand what they can search for before they begin typing. Photos also displays a description of how it scans the photo library to offer search suggestions.
- As people interact with the feature, provide feedback on their actions to guide them towards a result without overwhelming them. For example, while people are interacting with Animoji, the feature responds to current conditions and suggests how people can improve their results by adjusting the lighting or moving closer to the camera.
- Suggest alternative ways to accomplish the user’s goal instead of showing no results. To do this successfully, you need to understand the goal well enough to suggest alternatives that make sense. For example, if people ask Siri to set a timer on a Mac, Siri suggests setting a reminder instead, because timers aren’t available in macOS. This suggestion makes sense because Siri understands that the goal is to receive an alert at a certain time.

**Explain how limitations can cause unsatisfactory results.** People can get frustrated when it seems that your feature works intermittently. Ideally, your feature can recognize and describe the reasons for poor results to make people aware of the limitations and help them to adjust their expectations. For example, Animoji tells people that it doesn’t work well in the dark.

**Consider telling people when limitations are resolved.** When people use a feature frequently, they learn to avoid the interactions that fail because of the feature’s limitations. When you update your app to remove a limitation, you might want to notify people so that they can adjust their mental model of your feature and return to interactions they’d previously avoided.
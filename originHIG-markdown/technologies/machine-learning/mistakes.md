# **[technologies-machine-learning] mistakes**

It’s inevitable that your app will make mistakes. Although people may not expect perfection, mistakes can damage their experience and decrease their trust in your app. To help you avoid negative consequences, it’s crucial to:

- Anticipate mistakes. As much as possible, design ways to avoid mistakes and mitigate them when they happen.
- Help people handle mistakes. Mistakes can have a wide range of consequences, so the tools you provide to handle a mistake must be able to address those consequences.
- Learn from mistakes when doing so improves your app. In some cases, learning from a mistake might have undesirable effects, such as causing unpredictability in the user experience. When it makes sense, use each mistake as a data point that can refine your machine learning models and improve your app.

There are several machine learning patterns that can help you address mistakes:

- [Limitations](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/limitations) help you set people’s expectations about the accuracy of your suggestions.
- [Corrections](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/corrections) give people a way to be successful even when your results are wrong.
- [Attributions](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/attribution) give people insight into where suggestions come from, which can help them understand mistakes.
- [Confidence](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/confidence) helps you gauge the quality of your results, which can impact how you present them.
- Feedback — both [explicit](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/explicit-feedback) and [implicit](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/implicit-feedback) — lets people tell you about mistakes that you might not be aware of.

**Understand the significance of a mistake’s consequences.** For example, incorrect keyboard suggestions might annoy people, but suggesting a travel route that results in a missed flight is a serious inconvenience. Show empathy by providing corrective actions or tools that match the seriousness of the mistake.

**Make it easy for people to correct frequent or predictable mistakes.** If you don’t give people an easy way to correct mistakes, they can lose trust in your app.

**Continuously update your feature to reflect people’s evolving interests and preferences.** One way to help you improve your understanding of users and avoid mistakes is to use implicit feedback to discover changes in their tastes and habits. You should also update your feature with domain-specific information, such as current trends in popular entertainment. Ideally, people don’t have to do any work to benefit from improvements in your app.

**When possible, address mistakes without complicating the UI.** Some patterns, such as corrections and limitations, tend to integrate seamlessly with an app’s UI, whereas others, like attributions, can be harder to integrate. Balance a pattern’s effect on the UI with its potential for compounding the mistake. For example, if you update the UI with an attribution that turns out to be wrong, the effect of the original mistake is magnified.

**Be especially careful to avoid mistakes in proactive features.** A proactive feature — like a suggestion based on user behaviors — promises valuable results without asking people to do anything to get them. However, because people don’t request a proactive feature, they often have less patience with its mistakes. Mistakes made by proactive features can also cause people to feel that they have less control.

**As you work on reducing mistakes in one area, always consider the effect your work has on other areas and overall accuracy.** For example, optimizing an image recognition app to improve how it recognizes dogs might result in a decreased ability to recognize cats. As your models evolve, be prepared for mistakes to evolve, too. Use what you know about people’s preferences to help you determine the areas to focus on.
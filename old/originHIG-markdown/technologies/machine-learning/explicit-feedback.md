# **[technologies-machine-learning] explicit-feedback**

Explicit feedback provides actionable information your app can use to improve the content and experience it presents to people. Unlike [implicit feedback](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/implicit-feedback) — which is information an app gleans from user actions — explicit feedback is information people provide in response to a specific request from the app.

![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/explicit-feedback_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/explicit-feedback_2x.png)

*Favoriting* — marking an item for quick access in the future — and *social feedback* — expressing emotions towards others — are common user interactions that seem like mechanisms that supply explicit feedback. However, these tools actually provide implicit feedback because they don’t support app-specific requests. People use favoriting and social feedback to accomplish their own goals and apps can gather implicit feedback from these interactions.

**Request explicit feedback only when necessary.** People must take action to provide explicit feedback, so it’s best to avoid requesting it if possible. Instead, consider using implicit feedback to learn how people interact with your app without asking them to do extra work.

**Always make providing explicit feedback a voluntary task.** You want to communicate that explicit feedback can help improve the experience without making people feel that providing it is mandatory.

**Don’t ask for both positive and negative feedback.** Good suggestions don’t require any feedback, so you don’t want to imply that people should give positive feedback on all the results they like. Instead, give people the opportunity to provide negative feedback on results they don’t like so that you can improve the experience.

**Use simple, direct language to describe each explicit feedback option and its consequences.** Avoid using imprecise terms such as *dislike* because such terms don’t convey consequences and can be hard to translate. Instead, describe each option in a way that helps people understand what will happen when they choose the option, such as:

- Suggest less pop music
- Suggest more thrillers
- Mute politics for a week

**Add iconography to an option description if it helps people understand it.** Icons can help clarify or emphasize part of an option description. Avoid using an icon by itself, because iconography alone isn’t always clear enough to communicate granularity or consequences.

**Consider offering multiple options when requesting explicit feedback.** Providing [multiple options](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/multiple-options) can give people a sense of control and help them identify unwanted suggestions and remove them from your app. To help people provide feedback, consider offering options that become progressively more specific so that it’s easy for people to clarify their response.

**Act immediately when you receive explicit feedback and persist the resulting changes.** For example, if people identify content they don’t want to see, that content should instantly disappear from their view and not appear elsewhere in your app. When you react immediately to feedback and show that your app remembers it, you build people’s trust in the value of providing it.

**Consider using explicit feedback to help improve when and where you show results.** For example, people might like a result, but they may not want to see it at certain times or in certain contexts. Explicit feedback on when and where to show results can help you fine-tune the experience people have in your app.
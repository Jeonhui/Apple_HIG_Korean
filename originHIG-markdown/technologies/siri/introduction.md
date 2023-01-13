# **[technologies-siri] introduction**

# Siri makes it easy for people to accomplish everyday tasks quickly using voice, touch, or automation.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Siri-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Siri-intro_2x.png)

When you use [SiriKit](https://developer.apple.com/documentation/sirikit) to define the tasks and actions that your app supports, people can use Siri to perform them even when your app isn’t running. If you’re an accessory maker, you can also help people use Siri to control your accessories by integrating them with [HomeKit](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/introduction/) or [AirPlay 2](https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/introduction/). Here are some of the ways people can use Siri to interact with your app or accessory:

- Ask Siri to perform a system-defined task that your app supports, like send a message, play a song, or start a workout.
- Add a *shortcut*, which is a way to accelerate actions your app defines through onscreen interactions or by voice.
- Use the Shortcuts app to adjust what a shortcut does, including combining several actions to perform one multistep shortcut.
- Tap a *suggestion* to perform a shortcut with your app (Siri can *suggest* shortcuts that people might want to perform, based on their current context and the information you provide).
- Use Siri to control an accessory that integrates with your app.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png)

Siri works with your products on iPhone, iPad, Mac, Apple Watch, HomePod, and AirPods, so people can use it almost everywhere.

When you make your app’s tasks available through Siri, you have several opportunities to customize the user experience. At a fundamental level, you customize the flow and functionality of the everyday tasks and actions you support to implement your business requirements. To reinforce this functionality throughout the user experience, you can write dialogue that reflects the style and tone of your company’s communications and design custom UI that incorporates your app’s visual style into the Siri interface.

As you approach the job of integrating your app with Siri, assess the actions your app enables and learn how people use your app without voice interaction. Then consider the following steps:

- Identify key tasks in your app that people might want to perform on a regular basis.
- Drive engagement by telling the system about your app’s key tasks and by supporting suggestions.
- For actions that people can perform through voice interaction, design functional conversational flows that feel natural.
- Explore the various ways people might perform your app’s tasks — such as in a hands-free situation — and the devices they might be using, such as Apple Watch or iPad.

# **Identify your app’s key tasks**

Tasks are at the core of your app’s integration with Siri. SiriKit builds on the idea of a person’s intention to perform a task by using the term *intent* to represent a task an app supports. The communication between your app and Siri is based on the intents — that is, the tasks — your app helps people perform.

SiriKit defines *system intents* that represent common tasks — such as sending a message, calling a friend, and starting a workout — and groups related intents into domains. A *domain* is a category of tasks that Siri knows how to talk about, like messaging, calling, and workouts. For a complete list of domains and the actions in each domain that iOS and watchOS support, see [System intents](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/system-intents/).

When possible, take advantage of the intents that SiriKit defines. Using system-provided intents can make your job easier, while still giving you opportunities to customize the experience. However, if your app offers tasks that aren’t represented by system-defined intents — like ordering a meal or shopping for groceries — you can create a *custom intent* (for guidance, see [Custom intents](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/custom-intents/)).

### **A closer look at intents**

When people use Siri to ask questions and perform actions, Siri does the language processing and semantic analysis needed to turn their requests into intents for your app to handle. The exception is the personal phrase that people create to trigger a shortcut: When people speak the exact phrase, Siri recognizes it without doing additional processing or analysis.

As a designer, your main job is to present clear, actionable content that helps clarify and streamline the interactions people have with Siri to get things done in your app. Some of these interactions happen while your app and SiriKit communicate about handling the intent, so it’s helpful to be familiar with the related SiriKit terminology. At a high level, your app processes an intent in three phases: resolve, confirm, and handle.

First, your app and SiriKit must agree on what the request means in the *resolve* phase. You can think of this phase as the time to ask people for everything your app needs and, if necessary, ask for additional information or clarification. For example, if people ask to send a message to Amy, and they have multiple contacts named Amy, a messaging app can have Siri ask which Amy they mean. Details related to an intent, like a message recipient’s name, are known as *parameters*. In the resolve phase, you can indicate the parameters that are required to complete an action and those that are optional. For developer guidance, see [Resolving the parameters of an intent](https://developer.apple.com/documentation/sirikit/resolving_and_handling_intents/resolving_the_parameters_of_an_intent).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/resolve-phase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/resolve-phase_2x.png)

The second phase — called the *confirm* phase — happens when you have all the information you need to handle the intent. This phase can give people a chance to make sure they want to complete the task. For example, tasks that have financial impact require confirmation. In addition to asking for the user’s consent, you can present an error during this phase if something will prevent your app from completing the action. For example, if people use an app to order an item for pickup when the pickup location is closed, the app can describe why it can’t complete the action right now. Presenting this error during the confirm phase avoids making people wait until they’re paying for the item to find out that their request has failed. For developer guidance, see [Confirming the details of an intent](https://developer.apple.com/documentation/sirikit/resolving_and_handling_intents/confirming_the_details_of_an_intent).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/confirm-phase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/confirm-phase_2x.png)

Third, your app performs the task and tells SiriKit what it actually did in the *handle* phase. You can provide both visual and textual information that tells people what your app did to handle their request. For example, an app that lets people order coffee might present a receipt that describes the order. Siri can speak or display the information your app provides. For developer guidance, see [Handling an intent](https://developer.apple.com/documentation/sirikit/resolving_and_handling_intents/handling_an_intent).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/handle-phase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/handle-phase_2x.png)

# **Provide information about actions and support suggestions**

Most apps enable large numbers of actions, but people tend to perform only a handful of them on a regular basis. When you tell the system about people’s regular actions and describe new ones you think they’ll want to perform in the future, Siri can *suggest* shortcuts for both types of actions when people are likely to be interested in them.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/suggested-action_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/suggested-action_2x.png)

For example, in an app that’s all about coffee, the most frequent action might be to order a cup of coffee, while less frequent actions might include buying coffee beans or locating a new coffee shop. In this example, the coffee app would share information about the *order coffee* action so that Siri can suggest a shortcut for this action when people usually want to do it, like weekday mornings. The app could also tell Siri about an action that people haven’t performed yet, but might be interested in — like ordering a new seasonal variation of their favorite coffee — so that Siri might suggest a shortcut for this action.

Siri can use signals like location, time of day, and type of motion (such as walking, running, or driving), to intelligently predict just the right time and place to suggest actions from your app. Depending on the information your app shares and people’s current context, Siri can offer shortcut *suggestions* on the lock screen, in search results, or on the [Siri watch face](https://support.apple.com/guide/watch/faces-and-features-apde9218b440/watchos#apdcc88df92c). Siri can also use some types of information to suggest actions that system apps support, such as using Calendar to add an event shared by your app. Here are some example scenarios.

- Shortly before 7:30 a.m., Siri might suggest the *order coffee* action to people who use the coffee app every morning.
- After people use a box office–type app to buy tickets to a movie, Siri might remind them to turn on Do Not Disturb shortly before showtime.
- Siri might suggest an automation that starts a workout in the user’s favorite workout app and plays their favorite workout playlist as they enter their usual gym.
- When people enter the airport after a home-bound flight, Siri might suggest they request a ride home from their favorite ride-sharing app.

When you provide information about your actions to the system, people can also use the Shortcuts app to create shortcuts for the system and custom intents you support. For guidance, see [Shortcuts and suggestions](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions/).

# **Design a great voice experience**

A great voice interface helps people feel confident they’ll get the results they want, even when they’re not sure what they can say. Siri supports different voice experiences for system-provided intents and custom intents. With a system intent, Siri does the natural language processing for you, letting people interact with your app in various conversational ways. With a custom intent, your app helps people perform a task that Siri doesn’t know about yet, which results in a different type of support for the voice experience. Custom intents give you additional opportunities to customize conversational dialogue, but also require people to create and speak a precise phrase to trigger the interaction.

As a designer, you have several ways to enhance both types of conversational experiences and help people specify what they want without engaging in lengthy exchanges.

For system-provided intents, you help Siri communicate with people about the action they want to accomplish by providing essential information and defining any app-specific terminology that might come up during the conversation. You don’t have to write additional dialogue for Siri to speak because Siri already knows about the actions in the system-defined domains and understands many ways that people may talk about them. For example, if you need to confirm the recipient’s name during the resolve phase of a messaging intent, you simply indicate that the required parameter value is missing and Siri says to the sender "Who do you want to send it to?"

Even though you don’t write custom dialogue for system-provided intents, you can enhance the voice experience in other ways. For example, if people ask Siri to "play *Your Music App*" as they enter their gym, you could respond by playing their workout playlist.

When you support a custom intent, people initiate the action by using their personal invocation phrase; if people don’t speak their phrase precisely, Siri doesn’t trigger the intent. Although you can suggest a memorable phrase for people to use, your principal job is to write clear, direct dialogue, often in the form of follow-up questions, to help people accomplish the action in as few steps as possible.

For example, a coffee app might suggest *Order coffee* as a phrase people could use to reorder a favorite cup of coffee. In a scenario where people usually use *Order coffee* to order a cappuccino in various sizes, the coffee app could follow up with custom dialogue that builds on this knowledge, like "What size of cappuccino?" For other types of actions, more open-ended questions can be better at helping people accomplish the task efficiently. For example, if people trigger a grocery shopping action by saying *Add to cart*, the grocery shopping app could follow up with "OK, what do you want?"

# **Recognize that people use Siri in different contexts**

People can use Siri to get things done while they’re in a car, working out, using apps on a device, or interacting with HomePod. You don’t always know the context in which people are using Siri to perform your app’s actions, so flexibility is key in order to help people have a great experience no matter what they’re doing.

To communicate with people regardless of their current context, you should supply information that Siri can provide both vocally and visually. Supporting both voice and screen-based content lets Siri decide which communication method works best for people in their current situation. For example, Siri speaks to people through their AirPods if they say "Hey Siri" while using them.

In voice-only situations, Siri verbally describes information that would have been presented onscreen in other situations. Consider a food-delivery app that requires people to confirm a transaction before completing the order. In a voice-only scenario, Siri may say "Your total is fifteen dollars, and your order will take thirty minutes to arrive at your door. Ready to order?" In contrast, when people can view the cost and delivery information onscreen, Siri might simply say "Ready to order?" When you support custom intents, you’re responsible for supplying the voice-only dialogue that describes these types of onscreen information.’
June 5, 2023

 Removed Add to Siri guidance. Added references to the new App Shortcuts page. Siri
====

Siri makes it easy for people to accomplish everyday tasks quickly, using voice, touch, or automation.![A sketch of the Siri icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4198addd86e0d7d3c38660dd8b20fca0/technologies-Siri-intro@2x.png)

When you use [SiriKit](/documentation/sirikit)
 to define the tasks and actions that your app supports, people can use Siri to perform them even when your app isn’t running. If you’re an accessory maker, you can also help people use Siri to control your accessories by integrating them with [HomeKit](/design/human-interface-guidelines/homekit)
 or [AirPlay](/design/human-interface-guidelines/airplay)
. Here are some of the ways people can use Siri to interact with your app or accessory:

* Ask Siri to perform a system-defined task that your app supports, like send a message, play a song, or start a workout.
* Run a *shortcut*, which is a way to accelerate actions your app defines through onscreen interactions or by voice.
* Use the Shortcuts app to adjust what a shortcut does, including combining several actions to perform one multistep shortcut.
* Tap a *suggestion* to perform a shortcut with your app (Siri can *suggest* shortcuts that people might want to perform, based on their current context and the information you provide).
* Use Siri to control an accessory that integrates with your app.

![A screenshot of a custom Siri interface on iPhone that shows a person used their voice to compose a message that reads 'Do you want to grab lunch?' with an app named My Message App. The interface includes 'No' and 'Yes' buttons to cancel or send the message.](https://docs-assets.developer.apple.com/published/ea7493babaa5ef9e5e2fbc73152304f8/sirikit-intent-hero@2x.png)Siri works with your products on iPhone, iPad, Mac, Apple Watch, HomePod, and AirPods, so people can use it almost everywhere.

When you make your app’s tasks available through Siri, you have several opportunities to customize the user experience. At a fundamental level, you customize the flow and functionality of the everyday tasks and actions you support to implement your business requirements. To reinforce this functionality throughout the user experience, you can write dialogue that reflects the style and tone of your company’s communications and design custom UI that incorporates your app’s visual style into the Siri interface.

As you approach the job of integrating your app with Siri, assess the actions your app performs and learn how people use your app without voice interaction. Then consider the following steps:

* Identify key tasks in your app that people might want to perform on a regular basis.
* Drive engagement by telling the system about your app’s key tasks and by supporting suggestions.
* For actions that people can perform through voice interaction, design functional conversational flows that feel natural.
* Explore the various ways people might perform your app’s tasks — such as in a hands-free situation — and the devices they might be using, such as Apple Watch or iPad.

[Integrating your app with Siri](/design/human-interface-guidelines/siri#Integrating-your-app-with-Siri)
--------------------------------------------------------------------------------------------------------

Tasks are at the core of your app’s integration with Siri. SiriKit builds on the idea of a person’s intention to perform a task by using the term *intent* to represent a task an app supports. The communication between your app and Siri is based on the intents — that is, the tasks — your app helps people perform.

SiriKit defines *system intents* that represent common tasks — such as sending a message, calling a friend, and starting a workout — and groups related intents into domains. A *domain* is a category of tasks that Siri knows how to talk about, like messaging, calling, and workouts. For a complete list of domains and the actions in each domain that iOS and watchOS support, see [System intents](/design/human-interface-guidelines/siri#System-intents)
.

When possible, take advantage of the intents that SiriKit defines. Using system-provided intents can make your job easier, while still giving you opportunities to customize the experience. However, if your app offers tasks that aren’t represented by system-defined intents — like ordering a meal or shopping for groceries — you can create a *custom intent* (for guidance, see [Custom intents](/design/human-interface-guidelines/siri#Custom-intents)
).

### [A closer look at intents](/design/human-interface-guidelines/siri#A-closer-look-at-intents)

When people use Siri to ask questions and perform actions, Siri does the language processing and semantic analysis needed to turn their requests into intents for your app to handle. The exception is the personal phrase that people create to run a shortcut: When people speak the exact phrase, Siri recognizes it without doing additional processing or analysis.

As a designer, your main job is to present clear, actionable content that helps clarify and streamline the interactions people have with Siri to get things done in your app. Some of these interactions happen while your app and SiriKit communicate about handling the intent, so it’s helpful to be familiar with the related SiriKit terminology. At a high level, your app processes an intent in three phases: resolve, confirm, and handle.

First, your app and SiriKit must agree on what the request means in the *resolve* phase. You can think of this phase as the time to ask people for everything your app needs and, if necessary, ask for additional information or clarification. For example, if people ask to send a message to Amy, and they have multiple contacts named Amy, a messaging app can have Siri ask which Amy they mean. Details related to an intent, like a message recipient’s name, are known as *parameters*. In the resolve phase, you can indicate the parameters that are required to complete an action and those that are optional. For developer guidance, see [Resolving the Parameters of an Intent](/documentation/sirikit/resolving_and_handling_intents/resolving_the_parameters_of_an_intent)
.

![A screenshot of a custom Siri interface on iPhone that asks someone what kind of coffee to order with an app named My Coffee App. The interface includes a list of options: Light Roast with Cream, Vanilla Latte, Small Espresso and Donut, and Something Else.](https://docs-assets.developer.apple.com/published/c3afeeb60191c12c6edeed1999c5e473/resolve-phase@2x.png)The second phase — called the *confirm* phase — happens when you have all the information you need to handle the intent. This phase can give people a chance to make sure they want to complete the task. For example, tasks that have financial impact require confirmation. In addition to asking for a person’s consent, you can present an error during this phase if something will prevent your app from completing the action. For example, if people use an app to order an item for pickup when the pickup location is closed, the app can describe why it can’t complete the action right now. Presenting this error during the confirm phase avoids making people wait until they’re paying for the item to find out that their request has failed. For developer guidance, see [Confirming the Details of an Intent](/documentation/sirikit/resolving_and_handling_intents/confirming_the_details_of_an_intent)
.

![A screenshot of a custom Siri interface on iPhone that lets someone confirm their pick-up order with an app named My Coffee App. The interface shows the items ordered, their prices, taxes and fees, and a total. The interface also includes 'Cancel' and 'Order' buttons.](https://docs-assets.developer.apple.com/published/ec17de8af4af42101171c0793e766272/confirm-phase@2x.png)Third, your app performs the task and tells SiriKit what it actually did in the *handle* phase. You can provide both visual and textual information that tells people what your app did to handle their request. For example, an app that lets people order coffee might present a receipt that describes the order. Siri can speak or display the information your app provides. For developer guidance, see [Handling an Intent](/documentation/sirikit/resolving_and_handling_intents/handling_an_intent)
.

![A screenshot of a custom Siri interface on iPhone that confirms a coffee order is complete. The interface includes an order number and instructs the person to pick up their order in 10 minutes.](https://docs-assets.developer.apple.com/published/a5a1ec9624803a6771fa107d621fd9ac/handle-phase@2x.png)### [Provide information about actions and support suggestions](/design/human-interface-guidelines/siri#Provide-information-about-actions-and-support-suggestions)

Most apps support large numbers of actions, but people tend to perform only a handful of them on a regular basis. When you tell the system about people’s regular actions and describe new ones you think they’ll want to perform in the future, Siri can *suggest* shortcuts for both types of actions when people are likely to be interested in them.

![A screenshot of Siri suggestions on the search screen on iPhone. The screen shows four suggested apps: My Run App, Weather, Messages, and Music. The screen also includes a suggested shortcut for My Run App that reads 'Start a run'.](https://docs-assets.developer.apple.com/published/dfe8a7024898a77c65f800f644cb85a4/suggested-action@2x.png)For example, in an app that’s all about coffee, the most frequent action might be to order a cup of coffee, while less frequent actions might include buying coffee beans or locating a new coffee shop. In this example, the coffee app would share information about the *order coffee* action so that Siri can suggest a shortcut for this action when people usually want to do it, like weekday mornings. The app could also tell Siri about an action that people haven’t performed yet, but might be interested in — like ordering a new seasonal variation of their favorite coffee — so that Siri might suggest a shortcut for this action.

Siri can use signals like location, time of day, and type of motion (such as walking, running, or driving), to intelligently predict just the right time and place to suggest actions from your app. Depending on the information your app shares and people’s current context, Siri can offer shortcut *suggestions* on the lock screen, in search results, or on the [Siri watch face](https://support.apple.com/guide/watch/faces-and-features-apde9218b440/watchos#apdcc88df92c)
. Siri can also use some types of information to suggest actions that system apps support, such as using Calendar to add an event shared by your app. Here are some example scenarios.

* Shortly before 7:30 a.m., Siri might suggest the *order coffee* action to people who use the coffee app every morning.
* After people use a box office–type app to buy tickets to a movie, Siri might remind them to turn on Do Not Disturb shortly before showtime.
* Siri might suggest an automation that starts a workout in a person’s favorite workout app and plays their favorite workout playlist as they enter their usual gym.
* When people enter the airport after a home-bound flight, Siri might suggest they request a ride home from their favorite ride-sharing app.

When you provide information about your actions to the system, people can also use the Shortcuts app to create shortcuts for the system and custom intents you support. For guidance, see [Shortcuts and suggestions](/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)
.

### [Design a great voice experience](/design/human-interface-guidelines/siri#Design-a-great-voice-experience)

A great voice interface helps people feel confident they’ll get the results they want, even when they’re not sure what they can say. Siri supports different voice experiences for system-provided intents and custom intents. With a system intent, Siri does the natural language processing for you, letting people interact with your app in various conversational ways. With a custom intent, your app helps people perform a task that Siri doesn’t know about yet, which results in a different type of support for the voice experience. Custom intents give you additional opportunities to customize conversational dialogue, but also require people to create and speak a precise phrase to start the interaction.

As a designer, you have several ways to enhance both types of conversational experiences and help people specify what they want without engaging in lengthy exchanges.

For system-provided intents, you help Siri communicate with people about the action they want to accomplish by providing essential information and defining any app-specific terminology that might come up during the conversation. You don’t have to write additional dialogue for Siri to speak because Siri already knows about the actions in the system-defined domains and understands many ways that people may talk about them. For example, if you need to confirm the recipient’s name during the resolve phase of a messaging intent, you simply indicate that the required parameter value is missing and Siri says to the sender “Who do you want to send it to?”

Even though you don’t write custom dialogue for system-provided intents, you can enhance the voice experience in other ways. For example, if people ask Siri to “play *MyMusicApp*” as they enter their gym, you could respond by playing their workout playlist.

When you support a custom intent, people start the action by using their personal invocation phrase; if people don’t speak their phrase precisely, Siri doesn’t initiate the intent. Although you can suggest a memorable phrase for people to use, your principal job is to write clear, direct dialogue, often in the form of follow-up questions, to help people accomplish the action in as few steps as possible.

For example, a coffee app might suggest *Order coffee* as a phrase people could use to reorder a favorite cup of coffee. In a scenario where people usually use *Order coffee* to order a cappuccino in various sizes, the coffee app could follow up with custom dialogue that builds on this knowledge, like “What size of cappuccino?” For other types of actions, more open-ended questions can be better at helping people accomplish the task efficiently. For example, if people start a grocery shopping action by saying *Add to cart*, the grocery shopping app could follow up with “OK, what do you want?”

### [Recognize that people use Siri in different contexts](/design/human-interface-guidelines/siri#Recognize-that-people-use-Siri-in-different-contexts)

People can use Siri to get things done while they’re in a car, working out, using apps on a device, or interacting with HomePod. You don’t always know the context in which people are using Siri to perform your app’s actions, so flexibility is key to help people have a great experience no matter what they’re doing.

To communicate with people regardless of their current context, supply information that Siri can provide both vocally and visually. Supporting both voice and screen-based content lets Siri decide which communication method works best for people in their current situation. For example, Siri speaks to people through their AirPods if they say “Hey Siri” while using them.

In voice-only situations, Siri verbally describes information that would have been presented onscreen in other situations. Consider a food-delivery app that requires people to confirm a transaction before completing the order. In a voice-only scenario, Siri may say “Your total is fifteen dollars, and your order will take thirty minutes to arrive at your door. Ready to order?” In contrast, when people can view the cost and delivery information onscreen, Siri might simply say “Ready to order?” When you support custom intents, you’re responsible for supplying the voice-only dialogue that describes these types of onscreen information.

[System intents](/design/human-interface-guidelines/siri#System-intents)
------------------------------------------------------------------------

SiriKit defines a large number of system intents that represent common tasks people do, such as playing music, sending messages to friends, and managing notes. For system intents, Siri defines the conversational flow, while your app provides the data to complete the interaction.

![A screenshot of a custom Siri interface on iPhone that shows a person used their voice to compose a message that reads 'Do you want to grab lunch?' with an app named My Message App. The interface includes 'No' and 'Yes' buttons to cancel or send the message.](https://docs-assets.developer.apple.com/published/ea7493babaa5ef9e5e2fbc73152304f8/sirikit-intent-hero@2x.png)SiriKit provides the following intents.



| Domain (link to developer guidance) | Intents |
| --- | --- |
| [VoIP Calling](/documentation/sirikit/voip_calling)
 | Initiate calls. |
| [Workouts](/documentation/sirikit/workouts)
 | Start, pause, resume, end, and cancel workouts. |
| [Lists and Notes](/documentation/sirikit/lists_and_notes)
 | Create notes. |
| Search for notes. |
| Create reminders based on a date, time, or location. |
| [Media](/documentation/sirikit/media)
 | Search for and play media content, such as video, music, audiobooks, and podcasts. |
| Like or dislike items. |
| Add items to a library or playlist. |
| [Messaging](/documentation/sirikit/messaging)
 | Send messages. |
| Search for messages. |
| Read received messages. |
| [Payments](/documentation/sirikit/payments)
 | Send payments. |
| Request payments. |
| [Car Commands](/documentation/sirikit/car_commands)
 | Activate hazard lights or honk the horn. |
| Lock and unlock the doors. |
| Check the current fuel or power level. |

### [Design responses to system intents](/design/human-interface-guidelines/siri#Design-responses-to-system-intents)

People use Siri for convenience, and they expect a fast response. Your app needs to perform the system intents it supports quickly and accurately so that people have a great experience when they choose your app to get things done.

**Whenever possible, complete requests without leaving Siri.** If a request must be finished in your app, take people directly to the expected destination. Don’t show intermediary screens or messages that slow down the experience.

**When a request has a financial impact, default to the safest and least expensive option.** Never deceive people or misrepresent information. For a purchase with multiple pricing levels, don’t default to the most expensive. When people make a payment, don’t charge extra fees without informing them.

**When people request media playback from your app, consider providing alternative results if the request is ambiguous.** When you display alternative results within the Siri UI, people can easily choose a different piece of content if your first offering isn’t what they want.

**On Apple Watch, design a streamlined workflow that requires minimal interaction.** Whenever possible, use intelligent defaults instead of asking for input. For example, a music app could respond to a nonspecific request — like “Play music with MyMusicApp” — by playing a favorite playlist. If you must present options to people, offer a small number of focused choices that reduce the need for additional prompting.

### [Enhance the voice experience for system intents](/design/human-interface-guidelines/siri#Enhance-the-voice-experience-for-system-intents)

Help people learn how to use Siri to get things done in your app, and make conversation with Siri feel natural in the context of your brand, by defining app-specific terms and alternative ways people might refer to your app.

**Create example requests.** When people tap the Help button in the Siri interface, they view a guide that can include example phrases that you supply. Write phrases that demonstrate the easiest and most efficient ways to use Siri with your app. For developer guidance, see [Intent Phrases](/documentation/sirikit/registering_custom_vocabulary_with_sirikit/global_vocabulary_reference/intent_phrases)
.

**Define custom vocabulary that people use with your app.** Help Siri learn more about the actions your app performs by defining specific terms people might actually use in requests, like account names, contact names, photo tags, photo album names, ride options, and workout names. Make sure these terms are nongeneric and unique to your app. Never include other app names, terms that are obviously connected with other apps, inappropriate language, or reserved phrases, like *Hey Siri*. Note that Siri uses the terms you define to help resolve requests, but there’s no guarantee that Siri will recognize them.

**Consider defining alternative app names.** If people might refer to your app in different ways, it’s a good idea to provide a list of alternative names to help Siri understand what people mean. For example, a UnicornChat app might define the term *Unicorn* as an alternative app name. Never impersonate other apps by listing their names as alternative names for your app.

### [Design a custom interface for a system intent](/design/human-interface-guidelines/siri#Design-a-custom-interface-for-a-system-intent)

If it makes sense in your iOS app, you can supply custom interface elements or a completely custom UI for Siri or Maps to display along with your intent response. A watchOS app can’t provide a custom UI for Siri to display on Apple Watch.

![A screenshot of a custom Siri interface on iPhone that shows a person used their voice to compose a payment of $20 to Juan Chavez with an app named My Payment App. The interface includes 'Cancel' and 'Send' buttons.](https://docs-assets.developer.apple.com/published/f435a1e1d1b30c0d9462042f94d628ab/custom-ui-in-siri-interface@2x.png)**Avoid including extraneous or redundant information.** A custom interface lets you bring elements from your app into the Siri interface, but displaying information that isn’t related to the action can distract people. You also want to avoid duplicating information that the system can display in the Siri or Maps interface. For developer guidance, see [`INParameter`](/documentation/sirikit/inparameter)
.

**Make sure people can still perform the action without viewing your custom interface.** People can switch to voice-only interaction with Siri at any time, so it’s crucial to help Siri speak the same information that you display in your custom interface.

**Use ample margins and padding in your custom interface.** Avoid extending content to the edges of your interface unless it’s content that appears to flow naturally offscreen, like a map. In general, provide a margin of 20 points between each edge of your interface and the content. Use the app icon that appears above your interface to guide alignment: content tends to look best when it’s lined up with the center of this icon.

![An illustration of the upper-left corner of a custom Siri interface. A vertical line runs from the left side of the interface to the center of an app icon that contains a coffee cup. A label along the line indicates the distance is 20 points.](https://docs-assets.developer.apple.com/published/f25467882f266266281adaab25849e3b/custom-ui-insets@2x.png)

**Minimize the height of your interface.** The system displays other elements above and below your custom interface, such as the text prompt, the spoken response, and the Siri waveform. Aim for a custom interface height that’s no taller than half the height of the screen, so people can see all your content without scrolling.

**Refrain from displaying your app name or icon.** The system automatically shows this information, so it’s redundant to include it in your custom interface.

For developer guidance, see [Creating an Intents UI Extension](/documentation/sirikit/creating_an_intents_ui_extension)
.

[Custom intents](/design/human-interface-guidelines/siri#Custom-intents)
------------------------------------------------------------------------

If your app lets people perform an everyday task that doesn’t fit into any of the SiriKit domains, you can create a custom intent to represent it (see [System intents](/design/human-interface-guidelines/siri#System-intents)
 for a list of domains). You can also use a custom or system intent to support a shortcut, which gives people a quick way to initiate frequently performed actions by speaking a simple phrase or accepting a suggestion from Siri. To learn how to integrate your intents with the system so that people can discover them and add them to Siri, see [Shortcuts and suggestions](/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)
.

![A screenshot of a custom Siri interface on iPhone that shows a response to a person's inquiry about high tide from an app named Tides. The interface includes text that reads 'Tides says: High tide will be 6.4ft at 8:00 tonight.', along with additional descriptive text and a graph that shows tide height at different times of the day.](https://docs-assets.developer.apple.com/published/4736846fafbda35f7421b7eb9386730d/hey-siri-confirmation-not-required-success@2x.png)### [Custom intent categories and responses](/design/human-interface-guidelines/siri#Custom-intent-categories-and-responses)

Although your custom intent won’t belong to a SiriKit domain, you’ll need to model it on a system-defined *intent category* that’s related to your action. SiriKit defines several categories that represent generic tasks, like create, order, share, and search. Because these definitions are in the system, Siri knows how to communicate with people about common actions that are associated with each category — like placing an order or sharing content — in ways that feel natural.

It’s important to choose the category that best represents your action because the category influences the ways Siri speaks about it and the controls people might see in the interface. For example, a coffee app would likely choose the order category to represent its custom *order coffee* intent, and as a result, Siri can speak default responses that make sense in the context of this action, like “Ready to order?” and “OK. Ordering.” Category choice can have other effects, too: Because the order category includes actions that have financial impact, using this category for the *order coffee* intent means that people will be asked to authenticate before completing the action.

For several categories, the system defines additional verbs that are related to the category’s default action. You can use these alternative verbs to help ensure that the Siri dialogue and the button titles displayed in the interface align with the way you present your app’s actions. For example, in addition to the default verb *order*, the order category includes the verbs *buy* and *book*.

SiriKit defines the following custom intent categories and associated verbs.



| Category | Default verb | Additional verbs |
| --- | --- | --- |
| Generic | Do | Run, go |
| Information | View | Open |
| Order | Order | Book, buy |
| Start | Start | Navigate |
| Share | Share | Post, send |
| Create | Create | Add |
| Search | Search | Find, filter |
| Download | Download | Get |
| Other | Set | Request, toggle, check in |

SiriKit also defines three response types:

* Confirmation. Confirms that people still want to perform the action.
* Success. Indicates that the action has been initiated.
* Error. Tells people that the action can’t be completed.

In several custom intent categories, SiriKit defines default dialogue for each response type. For example, the default confirmation dialogue for the order category is, “Ready to order?” and the default success dialogue for the share category is, “OK. Shared.”

To customize a response, you create a template that combines dialogue you write with placeholders for relevant information your app can supply while it’s working on the intent. For example, a coffee app might enhance the default order confirmation dialogue by providing custom content that includes a placeholder for the total cost of the order.

Depending on the response type, your custom dialogue is presented before or after the default dialogue. For example, confirmation responses present the default dialogue after any custom dialogue. In the coffee app example, the customized confirmation dialogue would begin with something like, “Your large coffee with cream comes to $2.50” and end with the default dialogue, “Ready to order?”

### [Design a custom intent](/design/human-interface-guidelines/siri#Design-a-custom-intent)

If a built-in SiriKit intent represents your action’s purpose, adopt that intent instead of defining a custom intent. For example, if you’d like to offer a shortcut for sending a message, adopt [`INSendMessageIntent`](/documentation/sirikit/insendmessageintent)
; if you’d like to offer a shortcut for playing media, adopt [`INPlayMediaIntent`](/documentation/sirikit/inplaymediaintent)
. For guidance, see [System intents](/design/human-interface-guidelines/siri#System-intents)
.

**If your app’s action requires a custom intent, pick the category that most closely matches the action.** A category informs the system about the general function of an intent or shortcut — like order, download, or search — and affects the text and spoken dialogue presented to people when a shortcut is offered by the system or used with Siri. You design the flow of conversation for the custom intents you offer, so it’s essential that you choose a category that corresponds to the meaning of each intent.

Tip

If your action’s primary purpose is to retrieve information or show something to people — like displaying a sports score or the weather — use the information category. Using a different category requires people to make additional taps to get the information.

**Design custom intents that accelerate common, useful tasks.** Take advantage of the familiarity people have with your app and focus on tasks that people are already doing often.

**Ensure that your intent works well in every scenario.** Make it easy for people to run your intent as a shortcut, regardless of how they initiate it. For example, be prepared for people to run it using their voice on devices with and without a screen, from suggestions on the lock screen or the Siri face on Apple Watch, from search, and within a multistep shortcut.

**In general, design custom intents for tasks that aren’t overly complex.** People benefit the most from intents that reduce the number of actions required to complete a task. Don’t counteract that simplicity by requiring people to engage in a lengthy conversation with your app. You can also reduce the likelihood of user errors by limiting custom intents to clearly defined tasks.

**Design your intents to be long-lived.** Avoid offering intents that are date-specific or associated with temporary data. For example, it’s not a good idea for a travel app to offer a custom intent for each specific itinerary. A better intent might use follow-up questions to let people get the itinerary for one of their upcoming trips.

**Don’t request permission to use Siri.** If your app supports only custom intents — and not system intents — you don’t need to get permission to use Siri before letting people create and use voice shortcuts for your intents. Asking for permission can slow people down and could discourage them from using your app’s custom intents.

**Support background operation.** The best intents support shortcuts that run quickly and don’t pull people out of their current context. Strive to support custom intents that can run in the background without bringing your app to the front. Supporting background operation also ensures that people can complete the task in hands-free and voice-only scenarios.

### [Help people customize their requests](/design/human-interface-guidelines/siri#Help-people-customize-their-requests)

Custom intents can offer follow-up questions that let people do more with a single intent by refining its results on the fly. For example, if you offer an *order coffee* intent, you can help people get exactly what they want by asking them questions like, “What size?”, “What flavor?”, and “Which location?” Details like size, flavor, and location are *parameters* your app can define to help people personalize their request.

People supply parameter values to personalize an intent by responding to your follow-up questions or by editing existing values in the Shortcuts app. For example, if you offer an *order ground coffee* intent that includes a parameter for the grind size, you might supply a follow-up question like, “Which grind?” For people who typically order the coarse grind, you could simplify the interaction by using the value *coarse* as the default parameter value in a dialogue like, “Do you want coarse-ground coffee?” If people choose a different grind, you can follow up by presenting the full list of options. In voice-only scenarios, Siri speaks your follow-up questions and sends you the responses. When people use the Shortcuts app to edit a parameter value, you receive the new value when they use the associated shortcut. For developer guidance, see [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app)
.

**Design intents that require as few follow-up questions as possible.** Often, an intent can fulfill a request without asking any follow-up questions. Although follow-up questions make intents more flexible, you don’t want to force people into a long interaction. In most cases, it’s best to offer just one or two follow-up questions.

**List the smallest number of options possible, and sort the items in a way that makes sense.** As with too many follow-up questions, giving people too many options can make completing the task feel onerous. As you determine whether to include an item, consider its complexity as well as its utility. In a food-ordering app, for example, it might be easier for people to parse a list of individual menu items than a list of orders, each of which contains multiple items. After you identify a small number of useful items, consider sorting them by recency, frequency, or popularity.

**Make sure each follow-up question is meaningful.** Ideally, each follow-up question helps people make an important choice. If options or questions you present are too granular or too similar, the conversation can become repetitive, and people may feel like using your intent is too much work.

**Design parameters that are easy for people to understand and use.** Aim for parameters that represent simple values or attributes and name them using simple, straightforward terms. For example, a soup-ordering app might define parameters for the type of soup, the serving size, and a delivery location, using names like *soup*, *size*, and *location*. For guidance, see [Shortcuts and suggestions](/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)
.

**Ask for confirmation only when necessary.** An intent can ask people for confirmation before completing the task or when interpreting an answer to a follow-up question. Apps that support tasks that have financial impact, like an app that helps people place orders, must ask for confirmation before completing an order. For tasks that don’t have financial impact, asking for confirmation can feel like too much extra work and can sometimes discourage people from completing their request. In all cases, avoid asking for confirmation more than once.

**Support follow-up questions when it makes sense.** For example, an app that helps people order food might offer options for pickup or delivery, but ask for a specific location only after people choose the delivery option.

**Prioritize the options you offer based on the context in which people run your shortcut.** For example, if people use your shortcut to order an item for pickup, offer pickup locations that are currently close by. Offering options that adapt to the context in which your shortcut is run can help people avoid creating separate shortcuts for specific options.

**Consider adjusting the parameter values you offer when people set up your shortcut.** When you indicate that a parameter has dynamic options, you can enhance the shortcut setup experience in two ways:

* You can find and present parameter values that are relevant to the context people are in while they’re setting up the shortcut. For example, if people use the Shortcuts app to choose a value for a store-location parameter, the parameter can dynamically generate a list of stores that are currently closest to the device.
* You can present a comprehensive list of parameter values. When people set up a shortcut, having an extensive list of parameter values can help them create the shortcut they want. In contrast, when people use a shortcut to accelerate an action, they generally prefer the convenience of having a shorter list of choices.

For developer guidance, see the `storeLocation` parameter in the intent definition file of the [Soup Chef: Accelerating App Interactions with Shortcuts](/documentation/sirikit/soup_chef_accelerating_app_interactions_with_shortcuts)
 sample code project.

### [Enhance the voice experience for custom intents](/design/human-interface-guidelines/siri#Enhance-the-voice-experience-for-custom-intents)

**Aim to create conversational interactions.** You can customize what Siri says throughout the voice experience, including the handling of follow-up questions. Try writing a script and acting it out with another person to see how well your dialogue works in a face-to-face exchange. Experiencing custom dialogue in this way can help you find places where the interaction doesn’t feel natural.

**Help people understand errors and failures.** The system provides some default error descriptions, but it’s best to enhance error responses so that they’re specific to the current situation. For example, if chicken noodle soup is sold out, a soup app can respond with a custom error like, “Sorry, we’re out of chicken noodle soup” instead of “Sorry, we can’t complete your order.”

**Strive for engaging voice responses.** Remember that people may perform your app’s tasks from their HomePod, using “Hey Siri” with their AirPods, or through CarPlay without looking at a screen. In these cases, the voice response needs to convey the same essential information that the visual elements display to ensure that people can get what they need no matter how they interact with Siri.

**Create voice responses that are concise, descriptive, and effective in voice-driven scenarios.** As with a shortcut title, an effective custom spoken response clearly conveys what’s happening as the shortcut runs. If you ask follow-up questions, be sure to customize the default dialogue for clarity. For example, “Which soup?” is clearer than “Which one?”

**Avoid unnecessary repetition.** People tend to run voice shortcuts frequently, so they may hear the same prompt multiple times when answering follow-up questions or dealing with errors. Use the context of the current conversation to remove as many details from the prompts as possible. Avoid including unnecessary words or attempts at humor, because both can become irritating over time.

**Help conversations with Siri feel natural.** People interact with Siri in a variety of ways, like choosing a list item by saying “the second one,” or, in the case of a soup-ordering app, saying “large” or “small” instead of “bowl” or “cup.” You can make people’s Siri interactions feel more natural when you give the system alternative terms and phrases that work as app-specific synonyms (like using “bowl” as a synonym for “large”). Also consider enhancing clarity by providing alternative dialogue options for Siri to speak. For example, the soup app might present a list of onscreen menu options like “1 clam chowder,” or “1 clam chowder and 1 tomato,” but speak these options as “Which order? The one with clam chowder only or the one that includes tomato?”

**Exclude your app name.** The system provides verbal and visual attribution for your app when responding to people. Including your appʼs name in a verbal response is redundant and may make the experience of interacting with Siri feel less natural. Siri speaks your app’s name less frequently when people have used a shortcut several times, because it isn’t necessary to keep reminding them which app is responding.

**Don’t attempt to mimic or manipulate Siri.** Never impersonate Siri, attempt to reproduce the functionality that Siri provides, or provide a response that appears to come from Apple.

**Be appropriate and respect parental controls.** Never present offensive or demeaning content. Keep in mind that many families use parental controls to restrict explicit content and content that’s based on specific rating levels.

**Avoid using personal pronouns.** Create content that’s inclusive of all people.

**Consider letting people view more options in your app.** If the list of options doesn’t include the items people need, you might want to include an item that lets people open your app to see more. In the list, you could use copy like, “See more in *App Name*,” and in spoken dialogue, you might encourage people to say, “More options.”

**Keep responses device-independent.** People may use Siri to interact with your app via Apple Watch, HomePod, iPad, iPhone, or CarPlay. If you must provide device-specific wording, make sure it accurately reflects the person’s current device.

**Don’t advertise.** Don’t include advertisements, marketing, or in-app purchase sales pitches in your intent content.

[Shortcuts and suggestions](/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)
----------------------------------------------------------------------------------------------

When you support shortcuts, people have a variety of ways to discover and interact with the custom and system intents your app provides. For example:

* Siri can suggest a shortcut for an action people have performed at least once by offering it in search results, on the lock screen, and in the Shortcuts app.
* Your app can supply a shortcut for an action that people haven’t done yet but might want to do in the future, so that the Shortcuts app can suggest it or it can appear on the [Siri watch face](https://support.apple.com/guide/watch/faces-and-features-apde9218b440/watchos#apdcc88df92c)
.
* People can use the Shortcuts app to view all their shortcuts and even combine actions from different apps into multistep shortcuts.
* People can also use the Shortcuts app to automate a shortcut by defining the conditions that can run it, like time of day or current location.

The Shortcuts app is also available in macOS 12 and later and in watchOS 7 and later. For developer guidance, see [SiriKit](/documentation/sirikit)
.

Developer note

The Add to Siri method for adding shortcuts is no longer supported. See [App Shortcuts](/design/human-interface-guidelines/app-shortcuts)
 for ways to integrate your app with Siri and the system.

### [Make app actions widely available](/design/human-interface-guidelines/siri#Make-app-actions-widely-available)

*Donating* information about the actions your app supports helps the system offer them to people in various ways, such as:

* In search results
* Throughout the Shortcuts app
* On the lock screen as a Siri Suggestion
* Within the Now Playing view (for recently played media content)
* During Wind Down

Donations also power Automation Suggestions in the Shortcut app’s Gallery, making it easy for people to set up automations for hands-free interactions with your app.

You can also tell the system about shortcuts for actions people haven’t taken yet or make a shortcut available on the Siri watch face (for guidance, see [Suggest Shortcuts people might want to add to Siri](/design/human-interface-guidelines/siri#Suggest-Shortcuts-people-might-want-to-add-to-Siri)
 and [Display shortcuts on the Siri watch face](/design/human-interface-guidelines/siri#Display-shortcuts-on-the-Siri-watch-face)
). For developer guidance, see [Donating Shortcuts](/documentation/sirikit/donating_shortcuts)
.

**Make a donation every time people perform the action.** When you donate a shortcut each time people perform the associated action, you help the system more accurately predict the best time and place to offer the shortcut.

**Only donate actions that people actually perform.** For example, a coffee-ordering app donates the *Order coffee* shortcut every time people order coffee, but not when people do something else, like browse the menu. Similarly, a media app donates information about a song — like its title and album — only when people are actually listening to it. (For developer guidance, see [Improving Siri Media Interactions and App Selection](/documentation/sirikit/media/improving_siri_media_interactions_and_app_selection)
.)

**Remove donations for actions that require corresponding data.** If information required by a donated action no longer exists, your app needs to delete the donation so the shortcut isn’t suggested anymore. For example, if people delete a contact in a messaging app, the app needs to delete donations for messaging that contact. When people create a shortcut themselves, only they can delete it. For developer guidance, see [Deleting Donated Shortcuts](/documentation/sirikit/deleting_donated_shortcuts)
.

**If your app handles reservations, consider donating them to the system.** These items — like ticketed events, travel itineraries, or reservations for restaurants, flights, or movies — automatically appear as suggestions in Calendar or Maps. When you donate a reservation, it can appear on the lock screen with a suggestion to check in with your app or as a reminder that uses current traffic conditions to recommend when people should leave. For developer guidance, see [Donating Reservations](/documentation/sirikit/siri_event_suggestions/donating_reservations)
.

#### [Suggest Shortcuts people might want to add to Siri](/design/human-interface-guidelines/siri#Suggest-Shortcuts-people-might-want-to-add-to-Siri)

If your app supports an action that people haven’t performed yet but might find useful, you can provide a *suggested* shortcut to the system so that people can discover it. For example, if people use a coffee-ordering app to order their daily coffee but not to order a holiday special, the app might still want to give them a way to do this with an *Order holiday coffee* shortcut.

Suggested shortcuts appear in both the Gallery and the shortcut editor in the Shortcuts app. For developer guidance, see [Offering Actions in the Shortcuts App](/documentation/sirikit/offering_actions_in_the_shortcuts_app)
.

#### [Display shortcuts on the Siri watch face](/design/human-interface-guidelines/siri#Display-shortcuts-on-the-Siri-watch-face)

On Apple Watch, people can run shortcuts in several ways. For example, people can ask Siri, tap a shortcut [complication](/design/human-interface-guidelines/complications)
 on a watch face, or use the Shortcuts app available in watchOS 7 and later. You can also make shortcuts available on the Siri watch face.

To have a shortcut appear on the Siri watch face, you define a *relevant* shortcut by including information like the time of day at which your shortcut is relevant and how the shortcut can display on the Siri watch face. The information you supply lets the Siri watch face intelligently display your shortcut to people when they’re in the appropriate context.

For developer guidance, see [Defining Relevant Shortcuts for the Siri Watch Face](/documentation/sirikit/watch_and_widget_support/defining_relevant_shortcuts_for_the_siri_watch_face)
.

### [Create shortcut titles and subtitles](/design/human-interface-guidelines/siri#Create-shortcut-titles-and-subtitles)

Shortcut titles and subtitles appear when the system suggests them. In Siri Suggestions on iPhone and Apple Watch, a shortcut can also display an image.

**Be concise but descriptive.** An effective title conveys what happens when the shortcut runs. A subtitle can provide additional detail that supplements — but doesn’t duplicate — the title.

**Start titles with a verb and use sentence-style capitalization without punctuation.** Think of a shortcut title as a brief instruction.



|  | Example title |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | *Order my favorite coffee* |
| An X in a circle to indicate incorrect usage. | *Large latte* |
| A checkmark in a circle to indicate correct usage. | *Show today’s forecast* |
| An X in a circle to indicate incorrect usage. | *Weather forecast* |

**Lead with important information.** Long titles and subtitles may be truncated in certain contexts, depending on the device’s screen size.

**Exclude your app name.** The system already identifies the app associated with a shortcut.

**Localize titles and subtitles.** Providing content in multiple languages ensures an equally great experience for people everywhere.

**Consider providing a custom image for a more engaging suggestion.** For example, the shortcut for *Order my favorite coffee* could show a cup of the customer’s favorite coffee. Create an image that measures:

* 60x60 pt (180x180 px @ 3x) to display in an iOS app
* 34x34 pt (68x68 px @2x) to display on the Siri watch face on the 44mm Apple Watch (watchOS scales down the image for smaller watches)

### [Provide default phrases for shortcuts](/design/human-interface-guidelines/siri#Provide-default-phrases-for-shortcuts)

Your app provides default phrases for shortcuts during setup. People can personalize these phrases when adding your shortcuts to Siri.

**Keep phrases short and memorable.** Bear in mind that people must speak your phrase verbatim, so long or confusing phrases may result in mistakes and frustration. Two- and three-word phrases tend to work best. More words can be harder for people to remember, and phrases that are too long will get truncated.

**Make sure the phrases you suggest are accurate and specific.** Phrases like *Reorder coffee* or *Order my usual coffee* clearly describe what the shortcut does, which makes it easier for people to remember the phrase later. Also make sure that your suggested phrases are specific to each shortcut’s scope. For example, *Watch baseball* is clearer and more memorable than *Watch sports*. It’s also important to avoid implying that people can vary a shortcut’s invocation phrase to get a different result. For example, people might interpret a phrase like *Order a large clam chowder* to mean that your shortcut will give them what they want if they substitute “small” for “large” and “lobster bisque” for “clam chowder.”

**Don’t commandeer core Siri commands.** For example, never suggest a phrase like *Call 911* or include the text *Hey Siri*.

### [Make shortcuts customizable](/design/human-interface-guidelines/siri#Make-shortcuts-customizable)

When you define a parameter for each detail your app needs to perform an intent, people can customize the shortcut by editing these details in the Shortcuts app.

To show people which details they can edit and how their edits affect the action, you provide a *parameter summary*. A parameter summary succinctly describes the action by using the parameters in a sentence that begins with a verb. For example, a customizable *Order coffee* shortcut could display a parameter summary like “Order *quantity* *coffee*” where *quantity* and *coffee* are the parameters that people can edit. Here’s an example of how the *Order coffee* shortcut might look after people supply values for the *quantity* and *coffee* parameters.

![A screenshot of an Order Coffee shortcut’s parameters screen in the Shortcuts editor. The screen includes a field to specify how many cups to order and the type of coffee. The screen also includes a Done button and button for suggesting actions to perform next.](https://docs-assets.developer.apple.com/published/38ec9847858f9b38c9da07b973de0b9d/edited-parameter-summary@2x.png)**Provide a parameter summary for each custom intent you support.** At minimum, include in your parameter summary all parameters your intent requires and any parameters that receive values from other apps or actions. The summary doesn’t have to include optional parameters or parameters that people aren’t likely to edit; if you omit parameters like these from the summary, people can still access them in the Show More section.

**Craft a short parameter summary that’s clearly related to your intent’s title.** When the intent title and the parameter summary are similar, it’s easy for people to recognize the action regardless of where they view it. Aim to use the same words in the summary and the title — in particular, it’s helpful to begin both phrases with the same verb. For example, if your intent title is “Search encyclopedia,” a good parameter summary could be “Search encyclopedia for *search term*.”

**Aim for a parameter summary that reads like a sentence.** Use sentence-style capitalization, but don’t include ending punctuation. When possible, avoid punctuation entirely. Punctuation within a summary — especially colons, semicolons, and parentheses — can make the summary hard to read and understand.

**Provide multiple parameter summaries when necessary.** If your action includes a parameter that has a parent-child relationship with other parameters, you can provide multiple variants of the summary based on the current value of the parent parameter. For example, if your *order coffee* shortcut lets people specify whether they want to pick up their order or have it delivered, your parameter summary can reflect the current choice. In this scenario, create one parameter summary that helps people pick a store location and another summary that helps them pick a delivery address. Be sure to use a consistent grammatical structure and parameter order in all variants of the summary that you create.

![A screenshot of an Order Coffee shortcut’s parameters screen in the Shortcuts editor. The screen includes a field that's configured to order one double espresso for pickup at a store. The screen also includes a Done button and button for suggesting actions to perform next.](https://docs-assets.developer.apple.com/published/0ef7d5b55d30b47f82cc5e1babcced53/parent-parameter-choice@2x.png)Delivery or pickup![A screenshot of an Order Coffee shortcut’s parameters screen in the Shortcuts editor. The screen includes a field that's configured to order one double espresso for delivery to a location. The screen also includes a Done button and button for suggesting actions to perform next.](https://docs-assets.developer.apple.com/published/d04025126178429495a28de0f83945cf/child-parameter-choice@2x.png)Delivery location**Provide output parameters for information that people can use in a multistep shortcut.** For example, an *order coffee* action might provide output that includes the estimated delivery time and the cost of the order. With this information, people could create a multistep shortcut that messages a friend about the delivery time and logs the transaction in their favorite budgeting app.

**Consider defining an input parameter.** When you define an input parameter for an action, the action can automatically receive output from a preceding action in a multistep shortcut. For example, if your action applies a filter to the image it receives in an *image* parameter, you might designate *image* as the input parameter so that it automatically accepts images from other actions. You configure an input parameter in your intent definition file (shown in [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app#3239040)
).

![A screenshot of a Start My Run shortcut’s parameters screen in the Shortcuts editor. The screen includes three actions: Start a run, Play Running Playlist, and Turn Do Not Disturb On until Turned Off. The screen also includes a Done button and button for suggesting actions to perform next.](https://docs-assets.developer.apple.com/published/ca0a8ecbfc43df602848910683ffb886/input-output-parameters@2x.png)**Help people distinguish among different variations of the same action.** For example, an app that offers a *send message* action might use a contact photo to help people visually distinguish the various messages they send. To do this, choose the parameter that’s most identifiable to people and designate it as the key parameter (shown in [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app#3239040)
). Be sure to provide an image for the key parameter every time you donate the action (for developer guidance, see [`INImage`](/documentation/sirikit/inimage)
).

![A screenshot that shows the search for apps and actions view that appears when someone creates a new shortcut in the Shortcuts app. An Order Coffee action appears in a Suggestions area, and includes options for ordering an espresso and a latte. A Create Alarm action appears below the Order Coffee action, and includes options for adding alarms at 5:10PM and 10:10AM.](https://docs-assets.developer.apple.com/published/26ede1b5f6f0f1c7e6cea52dfa2d7b4c/multiple-intent-configurations@2x.png)**Avoid providing multiple actions that perform the same basic task.** For example, instead of providing an action that adds text to a note and a different action that adds an image, consider providing a single action that lets people add both types of content. Providing a few high-level actions can make it easier for people to understand what the actions do when they’re combined in a multistep shortcut.

For developer guidance, see [Shortcut-Related UI](/documentation/sirikit/shortcut-related_ui)
.

[Editorial guidelines](/design/human-interface-guidelines/siri#Editorial-guidelines)
------------------------------------------------------------------------------------

**Don’t refer to Siri using pronouns like “she,” “him,” or “her.”** Ideally, just use the word *Siri*. For example, *After you add a shortcut to Siri, you can run the shortcut anytime by asking Siri*.

**Use correct capitalization and punctuation when using the term *Hey Siri*.** *Hey Siri* is two words, italicized or in quotes, with an uppercase *H* and uppercase *S*. Do not follow the term with an ellipsis.



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | *Say Hey Siri to activate Siri.* |
| A checkmark in a circle to indicate correct usage. | *Say “Hey Siri” to activate Siri.* |
| An X in a circle to indicate incorrect usage. | *Say Hey Siri… to activate Siri.* |
| An X in a circle to indicate incorrect usage. | *Say “hey Siri” to activate Siri.* |

**In a localized context, translate only the word *Hey* in the phrase *Hey Siri*.** As an Apple trademark, *Siri* is never translated. Here is a list of acceptable translations for the phrase *Hey Siri*:



| Locale code | *Hey Siri* translation | Locale code | *Hey Siri* translation |
| --- | --- | --- | --- |
| ar\_AE | يا Siri | fr\_CA | Dis Siri |
| ar\_SA | يا Siri | fr\_CH | Dis Siri |
| da\_DK | Hej Siri | fr\_FR | Dis Siri |
| de\_AT | Hey Siri | it\_CH | Ehi Siri |
| de\_CH | Hey Siri | it\_IT | Ehi Siri |
| de\_DE | Hey Siri | ja\_JP | Hey Siri |
| en\_AU | Hey Siri | ko\_KR | Siri야 |
| en\_CA | Hey Siri | ms\_MY | Hai Siri |
| en\_GB | Hey Siri | nb\_NO | Hei Siri |
| en\_IE | Hey Siri | nl\_BE | Hé, Siri |
| en\_IN | Hey Siri | nl\_NL | Hé Siri |
| en\_NZ | Hey Siri | no\_NO | Hei Siri |
| en\_SG | Hey Siri | pt\_BR | E aí Siri |
| en\_US | Hey Siri | ru\_RU | привет Siri |
| en\_ZA | Hey Siri | sv\_SE | Hej Siri |
| es\_CL | Oye Siri | th\_TH | หวัดดี Siri |
| es\_ES | Oye Siri | tr\_TR | Hey Siri |
| es\_MX | Oye Siri | zh\_CN | 嘿Siri |
| es\_US | Oye Siri | zh\_HK | 喂 Siri |
| fi\_FI | Hei Siri | zh\_TW | 嘿 Siri |
| fr\_BE | Dis Siri |  |  |

### [Referring to Shortcuts](/design/human-interface-guidelines/siri#Referring-to-Shortcuts)

**When referring to the Shortcuts feature or app, always typeset with a capital S and make sure that *Shortcuts* is plural.** For example, *MyApp integrates with Shortcuts to provide a quick way to get things with just a tap or by asking Siri.*

**When referring to individual shortcuts (that is, not the feature or the Shortcuts app), use lowercase.** For example, *Run a shortcut by asking Siri or tapping a suggestion on the Lock Screen*.

**Use the right terminology when describing how people can use Shortcuts in your app.** People run shortcuts by asking Siri, so your wording needs to be very similar to phrases like *Run a shortcut by asking Siri* or *Run the shortcut by asking Siri with your personalized phrase* (localized as appropriate). Avoid using phrases like *add voice shortcuts*, *make a voice command*, *create a voice prompt*, or any other variation. Instead, consider a phrase like *Add a shortcut to Siri to run with your voice* (localized as appropriate).

To encourage people to create or use shortcuts in ways other than voice — like automations, Home Screen shortcuts, and other methods — use a phrase that doesn’t specify a particular method, like *For quick access, add to Shortcuts*.

Note

Use translations of your app name and the word *Shortcuts* — but not *Siri* — when referring to them in a localized context.

### [Referring to Apple products](/design/human-interface-guidelines/siri#Referring-to-Apple-products)

**Adhere to Apple’s trademark guidelines.** Apple trademarks can’t appear in your app name or images. In text, use Apple product names exactly as shown on the [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)
.

* Use Apple product names in singular form only; don’t make Apple product names possessive.
* Don’t translate Apple, Siri, or any other Apple trademark.
* Don’t use category descriptors. For example, say iPad, not tablet.
* Don’t indicate any kind of sponsorship, partnership, or endorsement from Apple.
* Attribute Apple, Siri, and all other Apple trademarks with the correct credit lines wherever legal information appears within your app.
* Refer to Apple devices and operating systems only in technical specifications or compatibility descriptions.

See [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)
.

[Platform considerations](/design/human-interface-guidelines/siri#Platform-considerations)
------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/siri#Resources)
--------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/siri#Related)

[App Shortcuts](/design/human-interface-guidelines/app-shortcuts)


[Design for intelligence](https://developer.apple.com/news/?id=mb3c4r4r)


[Guidelines for using Apple trademarks and copyrights](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)


#### [Developer documentation](/design/human-interface-guidelines/siri#Developer-documentation)

[SiriKit](/documentation/sirikit)


#### [Videos](/design/human-interface-guidelines/siri#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/D3281878-D461-48C4-85E9-FCB66D09A038/6670_wide_250x141_1x.jpg) Design App Shortcuts](https://developer.apple.com/videos/play/wwdc2022/10169) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/1F7BB4BF-73DB-4EB4-A65E-5540D89DD861/5146_wide_250x141_1x.jpg) Donate intents and expand your app’s presence](https://developer.apple.com/videos/play/wwdc2021/10231) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/F9CCA013-491E-48BD-A0FF-D21B24F1D5E9/5220_wide_250x141_1x.jpg) Design great actions for Shortcuts, Siri, and Suggestions](https://developer.apple.com/videos/play/wwdc2021/10283) 
[Change log](/design/human-interface-guidelines/siri#Change-log)
----------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Removed Add to Siri guidance. Added references to the new [App Shortcuts](/design/human-interface-guidelines/app-shortcuts)
 page. |
| May 2, 2023 | Consolidated guidance into one page. |


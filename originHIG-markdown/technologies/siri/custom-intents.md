# **[technologies-siri] custom-intents**

If your app lets people perform an everyday task that doesn’t fit into any of the SiriKit domains, you can create a custom intent to represent it (see [System intents](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/system-intents) for a list of domains). You can also use a custom or system intent to support a shortcut, which gives people a quick way to initiate frequently performed actions by speaking a simple phrase or accepting a suggestion from Siri. To learn how to integrate your intents with the system so that people can discover them and add them to Siri, see [Shortcuts and suggestions](https://developer.apple.com/design/human-interface-guidelines/siri/overview/shortcuts-and-suggestions/).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/hey-siri-confirmation-not-required-success_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/hey-siri-confirmation-not-required-success_2x.png)

# **Custom intent categories and responses**

Although your custom intent won’t belong to a SiriKit domain, you’ll need to model it on a system-defined *intent category* that’s related to your action. SiriKit defines several categories that represent generic tasks, such as create, order, share, and search. Because these definitions are in the system, Siri knows how to communicate with people about common actions that are associated with each category — such as placing an order or sharing content — in ways that feel natural.

It’s important to choose the category that best represents your action because the category influences the ways Siri speaks about it and the controls people might see in the interface. For example, a coffee app would likely choose the order category to represent its custom *order coffee*intent, and as a result, Siri can speak default responses that make sense in the context of this action, such as “Ready to order?” and “OK. Ordering.” Category choice can have other effects, too: Because the order category includes actions that have financial impact, using this category for the *order coffee* intent means that people will be asked to authenticate before completing the action.

For several categories, the system defines additional verbs that are related to the category’s default action. You can use these alternative verbs to help ensure that the Siri dialogue and the button titles displayed in the interface align with the way you present your app’s actions. For example, in addition to the default verb *order*, the order category includes the verbs *buy* and *book*.

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

- Confirmation. Confirms that people still want to perform the action.
- Success. Indicates that the action has been initiated.
- Error. Tells people that the action can’t be completed.

In several custom intent categories, SiriKit defines default dialogue for each response type. For example, the default confirmation dialogue for the order category is, “Ready to order?” and the default success dialogue for the share category is, “OK. Shared.”

To customize a response, you create a template that combines dialogue you write with placeholders for relevant information your app can supply while it’s working on the intent. For example, a coffee app might enhance the default order confirmation dialogue by providing custom content that includes a placeholder for the total cost of the order.

Depending on the response type, your custom dialogue is presented before or after the default dialogue. For example, confirmation responses present the default dialogue after any custom dialogue. In the coffee app example, the customized confirmation dialogue would begin with something like, “Your large coffee with cream comes to $2.50.” and end with the default dialogue, “Ready to order?”

# **Design a custom intent**

If a built-in SiriKit intent represents your action’s purpose, adopt that intent instead of defining a custom intent. For example, if you’d like to offer a shortcut for sending a message, adopt [INSendMessageIntent](https://developer.apple.com/documentation/sirikit/insendmessageintent); if you’d like to offer a shortcut for playing media, adopt [INPlayMediaIntent](https://developer.apple.com/documentation/sirikit/inplaymediaintent). For guidance, see [System intents](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/system-intents/).

**If your app’s action requires a custom intent, pick the category that most closely matches the action.** A category informs the system about the general function of an intent or shortcut — like order, download, or search — and affects the text and spoken dialogue presented to people when a shortcut is offered by the system or used with Siri. You design the flow of conversation for the custom intents you offer, so it’s essential that you choose a category that corresponds to the meaning of each intent.

**TIP**If your action’s primary purpose is to retrieve information or show something to people — like displaying a sports score or the weather — use the information category. Using a different category requires people to make additional taps to get the information.

**Design custom intents that accelerate common, useful tasks.** Take advantage of the familiarity people have with your app and focus on tasks that people are already doing often.

**Ensure that your intent works well in every scenario.** Make it easy for people to run your intent as a shortcut, regardless of how they initiate it. For example, be prepared for people to run it using their voice on devices with and without a screen, from suggestions on the lock screen or the Siri face on Apple Watch, from search, and within a multistep shortcut.

**In general, design custom intents for tasks that aren’t overly complex.** People benefit the most from intents that reduce the number of actions required to complete a task. Don’t counteract that simplicity by requiring people to engage in a lengthy conversation with your app. You can also reduce the likelihood of user errors by limiting custom intents to clearly defined tasks.

**Design your intents to be long-lived.** Avoid offering intents that are date-specific or associated with temporary data. For example, it’s not a good idea if a travel app offers a custom intent for each specific itinerary. A better intent might use follow-up questions to let people get the itinerary for one of their upcoming trips.

**Don’t request permission to use Siri.** If your app supports only custom intents — and not system intents — you don’t need to get permission to use Siri before letting people create and use voice shortcuts for your intents. Asking for permission can slow people down and could discourage them from using your app’s custom intents.

**Support background operation.** The best intents enable shortcuts that run quickly and don’t pull people out of their current context. Strive to support custom intents that can run in the background without bringing your app to the front. Supporting background operation also ensures that people can complete the task in hands-free and voice-only scenarios.

# **Help people customize their requests**

Custom intents can offer follow-up questions that let people do more with a single intent by refining its results on the fly. For example, if you offer an *order coffee* intent, you can help people get exactly what they want by asking them questions such as, “What size?”, “What flavor?”, and “Which location?” Details like size, flavor, and location are *parameters* your app can define to help people personalize their request.

People supply parameter values to personalize an intent by responding to your follow-up questions or by editing existing values in the Shortcuts app or the Add to Siri sheet within your app. For example, if you offer an *order ground coffee* intent that includes a parameter for the grind size, you might supply a follow-up question like, “Which grind?” For people who typically order the coarse grind, you could simplify the interaction by using the value *coarse* as the default parameter value in a dialogue like, “Do you want coarse-ground coffee?” If people choose a different grind, you can follow up by presenting the full list of options. In voice-only scenarios, Siri speaks your follow-up questions and sends you the responses. When people use the Shortcuts app or your Add to Siri sheet to edit a parameter value, you receive the new value when they use the associated shortcut. For developer guidance, see [Adding user interactivity with Siri Shortcuts and the Shortcuts app](https://developer.apple.com/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app).

**Design intents that require as few follow-up questions as possible.** Often, an intent can fulfill a request without asking any follow-up questions. Although follow-up questions make intents more flexible, you don’t want to force people into a long interaction. In most cases, it’s best to offer just one or two follow-up questions.

**List the smallest number of options possible, and sort the items in a way that makes sense.**As with too many follow-up questions, giving people too many options can make completing the task feel onerous. As you determine whether to include an item, consider its complexity as well as its utility. In a food-ordering app, for example, it might be easier for people to parse a list of individual menu items than a list of orders, each of which contains multiple items. After you identify a small number of useful items, consider sorting them by recency, frequency, or popularity.

**Make sure each follow-up question is meaningful.** Ideally, each follow-up question helps people make an important choice. If options or questions you present are too granular or too similar, the conversation can become repetitive, and people may feel like using your intent is too much work.

**Design parameters that are easy for people to understand and use.** Aim for parameters that represent simple values or attributes and name them using simple, straightforward terms. For example, a soup-ordering app might define parameters for the type of soup, the serving size, and a delivery location, using names like *soup*, *size*, and *location*. For guidance, see [Shortcuts and suggestions](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions/).

**Ask for confirmation only when necessary.** An intent can ask people for confirmation before completing the task or when interpreting an answer to a follow-up question. Apps that support tasks that have financial impact, such as an app that enables ordering, must ask for confirmation before completing an order. For tasks that don’t have financial impact, asking for confirmation can feel like too much extra work and can sometimes discourage people from completing their request. In all cases, avoid asking for confirmation more than once.

**Support chaining of follow-up questions when it makes sense.** For example, an app that helps people order food might offer options for pickup or delivery, but ask for a specific location only after people choose the delivery option.

**Provide useful default parameter values in your Add to Siri sheet.** You can make it easier for people to create a shortcut for your intent by setting default values that are based on a person’s current context. For example, a soup-ordering app might offer a *Reorder soup* intent with a follow-up question that asks people to specify a past order. When people add this shortcut to Siri from a particular order’s detail view, the app could preconfigure the shortcut to include the values from that order in its parameters. Bear in mind that some people may never configure your intent in the Shortcuts app or your Add to Siri sheet, so always provide shortcuts that don’t rely on additional configuration.

**Prioritize the options you offer based on the context in which people run your shortcut.** For example, if people use your shortcut to order an item for pickup, offer pickup locations that are currently close by. Offering options that adapt to the context in which your shortcut is run can help people avoid creating separate shortcuts for specific options.

**Consider adjusting the parameter values you offer when people set up your shortcut.** When you indicate that a parameter has dynamic options, you can enhance the shortcut setup experience in two ways.

- You can find and present parameter values that are relevant to the context people are in while they’re setting up the shortcut. For example, if people use the Shortcuts app to choose a value for a store-location parameter, the parameter can dynamically generate a list of stores that are currently closest to the device.
- You can present a comprehensive list of parameter values. When people set up a shortcut, having an extensive list of parameter values can help them create the shortcut they want. In contrast, when people use a shortcut to accelerate an action, they generally prefer the convenience of having a shorter list of choices.

For developer guidance, see the storeLocation parameter in the intent definition file of the [SoupChef sample code project](https://developer.apple.com/documentation/sirikit/soup_chef_accelerating_app_interactions_with_shortcuts).

# **Enhance the voice experience for custom intents**

**Aim to create conversational interactions.** You can customize what Siri says throughout the voice experience, including the handling of follow-up questions. Try writing a script and acting it out with another person to see how well your dialogue works in a face-to-face exchange. Experiencing custom dialogue in this way can help you find places where the interaction doesn’t feel natural.

**Help people understand errors and failures.** The system provides some default error descriptions, but it’s best to enhance error responses so that they’re specific to the current situation. For example, if chicken noodle soup is sold out, a soup app can respond with a custom error like, “Sorry, we’re out of chicken noodle soup” instead of “Sorry, we can’t complete your order.”

**Strive for engaging voice responses.** Remember that people may perform your app’s tasks from their HomePod, using “Hey Siri” with their AirPods, or through CarPlay without looking at a screen. In these cases, the voice response should convey the same essential information that the visual elements display to ensure that people can get what they need no matter how they interact with Siri.

**Create voice responses that are concise, descriptive, and work well in voice-driven scenarios.** As with a shortcut title, an effective custom spoken response clearly conveys what’s happening as the shortcut runs. If you ask follow-up questions, be sure to customize the default dialogue for clarity. For example, “Which soup?” is clearer than “Which one?”

**Avoid unnecessary repetition.** People tend to run voice shortcuts frequently, so they may hear the same prompt multiple times when answering follow-up questions or dealing with errors. Use the context of the current conversation to remove as many details from the prompts as possible. Avoid including unnecessary words or attempts at humor because both can become irritating over time.

**Help conversations with Siri feel natural.** People interact with Siri in a variety of ways, such as choosing a list item by saying “the second one,” or, in the case of a soup-ordering app, saying “large” or “small” instead of “bowl” or “cup.” You can make people’s Siri interactions feel more natural when you give the system alternative terms and phrases that work as app-specific synonyms (like using “bowl” as a synonym for “large”). Also consider enhancing clarity by providing alternative dialogue options for Siri to speak. For example, the soup app might present a list of onscreen menu options like “1 clam chowder,” “1 clam chowder and 1 tomato,” but speak these options as “Which order? The one with clam chowder only or the one that includes tomato?”

**Exclude your app name.** The system provides verbal and visual attribution for your app when responding to people. Including your appʼs name in a verbal response is redundant and may make the experience of interacting with Siri feel less natural. Siri speaks your app’s name less frequently when people have used a shortcut several times, because it isn’t necessary to keep reminding them which app is responding.

**Don’t attempt to mimic or manipulate Siri.** Your app should never impersonate Siri, attempt to reproduce the functionality that Siri provides, or provide a response that appears to come from Apple.

**Be appropriate and respect parental controls.** Never present offensive or demeaning content. Keep in mind that many families use parental controls to restrict explicit content and content that’s based on specific rating levels.

**Avoid using personal pronouns.** Create content that’s inclusive of all people.

**Consider letting people view more options in your app.** If the list of options doesn’t include the items people need, you might want to include an item that lets people open your app to see more. In the list, you could use copy like, “See more in *App Name*” and in spoken dialogue, you might encourage people to say “More options.”

**Keep responses device-independent.** People may use Siri to interact with your app on Apple Watch, HomePod, iPad, iPhone, or through CarPlay. If you must provide device-specific wording, make sure it accurately reflects the user’s current device.

**Don’t advertise.** Don’t include advertisements, marketing, or in-app purchase sales pitches in your intent content.
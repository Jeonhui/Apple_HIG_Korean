June 5, 2023

 New page. App Shortcuts
=============

An App Shortcut is an easily understood, frequently used task or piece of content from your app or game that you provide to the system for people to use in a variety of contexts.![A stylized representation of the Notes app appearing as the result in the Top Hit area of Spotlight, along with App Shortcuts for creating a new note and opening two other recent notes. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/183dda77d62e2ab7dae5994f2e754a26/components-app-shortcuts-intro@2x.png)

App Shortcuts work on iPhone, iPad, Apple Watch, HomePod, and AirPods, so people can use them almost everywhere, as soon as they install your app or game. The system presents App Shortcuts in a variety of ways to help people use them quickly and conveniently, including with Siri, in Spotlight search, Suggestions, and the Shortcuts app.

App Shortcuts exist within the broader context of *custom shortcuts*, which people define using the Shortcuts app, and *actions*, the set of all functions from your app or game that you make available to the system.

Actions are the building blocks of both App Shortcuts and custom shortcuts. For guidance on designing actions with custom shortcuts in mind, see [Actions](/design/human-interface-guidelines/app-shortcuts#Actions)
.

For developer guidance, see [App Intents](/documentation/AppIntents)
. For guidance specific to Siri, see [Siri](/design/human-interface-guidelines/siri)
.

Developer note

The [SiriKit](/documentation/sirikit)
 framework supports a variety of [common use cases](/design/human-interface-guidelines/siri#System-intents)
 without the need to build custom intents. Before you start building an App Shortcut with the App Intents framework, it’s a good idea to determine whether you can take advantage of the predefined system intents available in SiriKit.

[Best practices](/design/human-interface-guidelines/app-shortcuts#Best-practices)
---------------------------------------------------------------------------------

**Identify the subset of things your app can do that make the most sense as App Shortcuts.** You can create up to 10 App Shortcuts, so prioritize the ones you think will be most helpful.

**Choose self-contained, straightforward features.** Self-contained tasks can be completed via Siri or search in their entirety. They don’t require your app to be open at all. Straightforward tasks are uncomplicated ones that people can succeed at quickly. Tasks that require many steps or a lot of input are less helpful as App Shortcuts.

**Write brief, memorable shortcut names.** Because the shortcut name is what people see in the UI and what they say to run it with Siri, it’s important to clearly communicate its function and make it easy to remember. You’ll have to include your app name (or a related synonym that you define), but you can be creative with it. For example, the Voice Memos app uses the shortcut “Record Voice Memo” rather than “Start recording a Voice Memo”.

**Consider including a dynamic parameter.** You can set a parameter in your shortcut that people can change depending on what they’d like to do. For example, a meditation app could use a dynamic parameter to let someone start a specific type of meditation, by saying “Start [Morning, Daily, Sleep] Meditation.” You can supply one dynamic parameter per App Shortcut, and its value comes from a finite list that you specify. Choose predictable and familiar parameter values, since people won’t have the list in front of them for reference. For developer guidance, see [App entities](/documentation/AppIntents/app-entities)
.

**In the case of an ambiguous request, ask for more information.** When possible, try to make a reasonable assumption and present it as an option for people to consider. If they don’t want the first option, direct them to a list of alternatives. It’s important for this list to be short (roughly five items or fewer), since Siri reads the entire list aloud in voice-only scenarios.

**Use custom snippets and Live Activities to present information and request further action.** Live Activities offer people continuous access to information, which is great for timers and countdowns that appear until an event is complete. Custom snippets are noninteractive custom views you can create with SiriKit or the App Intents framework, and are great for self-contained pieces of information (showing the weather at a person’s current location, for example). Live Activities and custom snippets are great ways to add visual elements that are unique to your app. See [Live Activities](/design/human-interface-guidelines/live-activities)
.

**Consider how your App Shortcuts will appear in Spotlight.** Your App Shortcuts can appear in Spotlight along with suggestions and searches for your app, so for each of your shortcuts, choose an SF Symbol from the SF Symbols library that accurately reflects its intent.

### [Language](/design/human-interface-guidelines/app-shortcuts#Language)

**Favor simple phrases with a single, obvious parameter.** Avoid complex phrases with multiple potential variables that people could mistake for the single dynamic parameter available in your shortcut. For example, “Start [Sleep] Meditation with nature sounds” appears to have two possible parameters. If your phrase feels too complicated when you say it aloud, it’s probably too complicated for people to use consistently. If the additional information is absolutely required, you can ask for it in a subsequent step.

**Include thoughtful natural language variations.** People might try a similar phrase to run your shortcut if they don’t remember the exact words. Be sure to include as many of these as you can: “Start Voice Memo” and “New Voice Memo” as variations, for example. Be thorough, but use your judgement to determine the boundaries of the shortcut’s function; “Save a Voice Memo” might not be appropriate when the intent is to create one. Include natural language variations for all of the languages that your app is localized in.

**Omit supporting dialogue when a custom visual presentation makes it redundant.** By default, the system displays the dialogue that Siri reads to people alongside any custom visual elements that you provide with a custom snippet. If the visual you provide contains the same information as the dialogue, suppress the dialogue so it won’t be shown.

**Write snippet dialogues for all platforms, not just visual ones.** Because your snippets can appear when people run App Shortcuts on audio-only platforms such as AirPods and HomePod, be sure to include all of the critical information in the snippet in the dialogue as well as any custom visual elements. Make sure your custom snippets look and sound great on all of the platforms where they’ll appear.

### [Presentation](/design/human-interface-guidelines/app-shortcuts#Presentation)

**Arrange your shortcuts in the order that you want them to appear in Spotlight.** This is the same order that they appear in the Shortcuts app. You can manually change the order with an app update, and you can also let peoples’ parameter choice reorder your shortcuts dynamically. As people use your app more and the number of their custom parameters increases, sorting shortcuts dynamically becomes more important. Consider using a heuristic such as recency or frequency to drive the order.

**Use a Siri tip view to highlight App Shortcuts in your app.** Pick key places to surface these tips, where people are most likely to benefit as they’re exploring — immediately before or after completing an action that they may want to repeat, for example. Be sure to make these tips dismissible; it’s always good to respect a person’s desire to remove unwanted information from their workflow. For developer guidance, see [`SiriTipUIView`](/documentation/AppIntents/SiriTipUIView)
.

### [Information collection](/design/human-interface-guidelines/app-shortcuts#Information-collection)

**Use an open-ended request to collect information with a wide range of possible values.** This is particularly useful for collecting values like numbers, place names, or times. Since people can say anything in response, make it clear what type of information you expect. To benefit from built-in dialogue and visual patterns, as well as Siri’s natural language understanding, use one of the open-ended requests provided by the App Intents framework if it fits the needs of your shortcut task.

**Use an intent confirmation before collecting an important response.** Intent confirmations are meant for particularly consequential actions, such as financial transactions, destructive actions like deleting content, or actions that feel high-risk (like sending a Calendar invitation to a big group). Be deliberate about when you use confirmations, since people appreciate being able to get through shortcuts quickly, and confirmations add an extra step.

**When confirming an intent, use a verb that reiterates the specific action.** Specific verbs (like “order”) communicate more clearly than ambiguous ones (like “confirm”). The App Intents framework provides a list of useful default verbs and their synonyms that you can use as-is, or you can use a custom verb that specifically matches the needs of your shortcut; if you use a custom verb, be sure to provide all of its relevant synonyms so Siri understands the intent in as many situations as possible.

[Actions](/design/human-interface-guidelines/app-shortcuts#Actions)
-------------------------------------------------------------------

Actions are specific tasks or functions that you want to make accessible through Siri, Spotlight, and the Shortcuts app. When you designate a function in your app as an action, people can use it in custom shortcuts they create, and the action can appear as a suggestion as people establish use patterns with your app.

Note

The most useful, concise, and self-contained actions are great candidates for App Shortcuts.

**Prioritize building actions for features that people use the most.** Starting with your app’s most widely used features helps people get the most out of each action. In the Calendar app, for example, people often add new events, get existing events, and edit their events, so these are great candidates for actions.

**Split complex tasks into smaller, more concise actions when possible.** This can make for a more powerful and configurable automation experience, and helps people understand exactly what each action will do.

**Make your actions platform agnostic.** People appreciate when actions are available on all of the devices they use. Support as many devices as you can in the context of your app. For AirPods and HomePod, this means creating a straightforward, complete experience interacting with voice alone.

**Consider the experience that people will have when customizing your actions.** People can use your actions as part of larger custom shortcuts that they create in the Shortcuts app. Be sure to present parameters that flow clearly, according to natural language, to help people understand what the action does and how it can relate to other actions in the context of a larger workflow.

**Write an action title that matches the action’s parameter summary.** An action is represented by its *title*, which is a brief representation that appears throughout the system, and by its *parameter summary*, which is a phrase that includes the action’s important parameters and appears in the editor of the Shortcuts app. Both the action’s title and its parameter summary start with the same verb, and they share as many words as possible between them. For example, Messages pairs the “Send Message” action title with the parameter summary “Send `“Message”` to `Recipients`.” For developer guidance, see [Providing your app’s capabilities to system services](/documentation/AppIntents/Providing-your-app-s-capabilities-to-system-services)
.

[Parameters](/design/human-interface-guidelines/app-shortcuts#Parameters)
-------------------------------------------------------------------------

Parameters are elements within an action that provide additional information to the system to resolve the action. For example, an action that sends a message might include a parameter for the recipient, and one for the message string. An action can have any number of parameters, though actions you designate as App Shortcuts can have only one.

For developer guidance, see [Parameter resolution](/documentation/AppIntents/parameter-resolution)
.

**Include parameters where they would naturally occur in an action.** Any place an action can make use of a variety of possible input values, or present a variety of possible results, is a great opportunity to add a parameter.

**Keep in mind that people can use parameters in shortcuts they configure.** People interact with your actions when they provide follow-up responses to resolve them, and when they configure custom shortcuts in the Shortcuts app. Be sure that the parameter’s position in the action and its possible response values make sense in both contexts. For example, when setting up an action for archiving tasks, be sure to include similar values for the “archive” parameter when editing it in the Shortcuts app (*configuration*) and when running the action with Siri (*resolution*).

**Define custom parameter entities as necessary.** The system provides useful built-in parameters that you can query as part of an action, but if you need to describe a parameter that isn’t included by default, you can configure a custom one. Use dynamic enumerations to define custom UIs for custom parameters in your actions. For developer guidance, see [`DynamicOptionsProvider`](/documentation/AppIntents/DynamicOptionsProvider)
.

**Consider providing a default value for each required parameter of your action.** If you have a strong opinion about a good starting place for a certain parameter, consider providing it as a default so people don’t have to go through multiple steps when using your action. Whether you provide a default or not, make sure that the action prompts people to provide their own value for the parameter — either through a question, or from a list — since people can always configure a parameter to “Ask Each Time” using the Shortcuts app.

**Place all of your optional parameters in the Options UI.** This way people can disclose them when they need to see them, and you don’t need to include them as part of the action summary.

[Platform considerations](/design/human-interface-guidelines/app-shortcuts#Platform-considerations)
---------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, visionOS, or watchOS. Not supported in tvOS.*

### [macOS](/design/human-interface-guidelines/app-shortcuts#macOS)

App Shortcuts aren’t supported in macOS. However, actions you create for your app using App Intents and SiriKit are supported, and people can build shortcuts using them with the Shortcuts app on Mac.

[Resources](/design/human-interface-guidelines/app-shortcuts#Resources)
-----------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/app-shortcuts#Related)

[Siri](/design/human-interface-guidelines/siri)


[Siri Style Guide](https://developer.apple.com/siri/style-guide/)


[Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)


#### [Developer documentation](/design/human-interface-guidelines/app-shortcuts#Developer-documentation)

[App Intents](/documentation/AppIntents)


[SiriKit](/documentation/sirikit)


[Providing your app’s capabilities to system services](/documentation/AppIntents/Providing-your-app-s-capabilities-to-system-services)


[Integrating custom data types into your intents](/documentation/AppIntents/Integrating-custom-types-into-your-intents)


#### [Videos](/design/human-interface-guidelines/app-shortcuts#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/B9AAA7B6-3671-44CB-B195-C1D7929E616E/8254_wide_250x141_1x.jpg) Design Shortcuts for Spotlight](https://developer.apple.com/videos/play/wwdc2023/10193) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/D3281878-D461-48C4-85E9-FCB66D09A038/6670_wide_250x141_1x.jpg) Design App Shortcuts](https://developer.apple.com/videos/play/wwdc2022/10169) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/8ED05354-3C9C-4F3C-A4A1-FED3C33D359B/6671_wide_250x141_1x.jpg) Implement App Shortcuts with App Intents](https://developer.apple.com/videos/play/wwdc2022/10170) 
[Change log](/design/human-interface-guidelines/app-shortcuts#Change-log)
-------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | New page. |


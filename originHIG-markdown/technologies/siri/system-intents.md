# **[technologies-siri] system-intents**

SiriKit defines a large number of system intents that represent common tasks people do, such as playing music, sending messages to friends, and managing notes. For system intents, Siri defines the conversational flow, while your app provides the data to complete the interaction.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png)

SiriKit provides the following intents.

| Domain(link to developer guidance) | Intents |
| --- | --- |
| https://developer.apple.com/documentation/sirikit/voip_calling | Initiate calls. |
| https://developer.apple.com/documentation/sirikit/workouts | Start, pause, resume, end, and cancel workouts. |
| https://developer.apple.com/documentation/sirikit/lists_and_notes | Create notes.Search for notes.Create reminders based on a date, time, or location. |
| https://developer.apple.com/documentation/sirikit/media | Search for and play media content, such as video, music, audiobooks, and podcasts.Like or dislike items.Add items to a library or playlist. |
| https://developer.apple.com/documentation/sirikit/messaging | Send messages.Search for messages.Read received messages. |
| https://developer.apple.com/documentation/sirikit/payments | Send payments.Request payments. |
| https://developer.apple.com/documentation/sirikit/car_commands | Activate hazard lights or honk the horn.Lock and unlock the doors.Check the current fuel or power level. |

# **Design responses to system intents**

People use Siri for convenience and they expect a fast response. Your app should perform the system intents it supports quickly and accurately so that people have a great experience when they choose your app to get things done.

**Complete requests without leaving Siri whenever possible.** If a request must be finished in your app, take people directly to the expected destination. Don’t show intermediary screens or messages that slow down the experience.

**When a request has a financial impact, default to the safest and least expensive option.**Never deceive people or misrepresent information. For a purchase with multiple pricing levels, don’t default to the most expensive. When people make a payment, don’t charge extra fees without informing them.

**When people request media playback from your app, consider providing alternative results if the request is ambiguous.** When you display alternative results within the Siri UI, people can easily choose a different piece of content if your first offering isn’t what they want.

**On Apple Watch, design a streamlined workflow that requires minimal interaction.** Use intelligent defaults instead of asking for input whenever possible. For example, a music app could respond to a nonspecific request — such as "Play music with MyMusicApp" — by playing a favorite playlist. If you must present options to people, offer a small number of focused choices that reduce the need for additional prompting.

# **Enhance the voice experience for system intents**

Help people learn how to use Siri to get things done in your app and make conversation with Siri feel natural in the context of your brand by defining app-specific terms and alternative ways people might refer to your app.

**Create example requests.** When people tap the Help button in the Siri interface, they view a guide that can include example phrases that you supply. Write phrases that demonstrate the easiest and most efficient ways to use Siri with your app. For developer guidance, see [Intent phrases](https://developer.apple.com/documentation/sirikit/registering_custom_vocabulary_with_sirikit/global_vocabulary_reference/intent_phrases).

**Define custom vocabulary that people use with your app.** Help Siri learn more about the actions your app performs by defining specific terms people might actually use in requests, like account names, contact names, photo tags, photo album names, ride options, and workout names. Make sure these terms are nongeneric and unique to your app. Never include other app names, terms that are obviously connected with other apps, inappropriate language, or reserved phrases, such as *Hey Siri*. Note that Siri uses the terms you define to help resolve requests, but there’s no guarantee that Siri will recognize them.

**Consider defining alternative app names.** If people might refer to your app in different ways, it’s a good idea to provide a list of alternative names to help Siri understand what people mean. For example, a UnicornChat app might define the term *Unicorn* as an alternative app name. Never impersonate other apps by listing their names as alternative names for your app.

# **Design a custom interface for a system intent**

If it makes sense in your iOS app, you can supply custom interface elements or a completely custom UI for Siri or Maps to display along with your intent response. A watchOS app can’t provide a custom UI for Siri to display on Apple Watch.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-in-siri-interface_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-in-siri-interface_2x.png)

**Avoid including extraneous or redundant information.** A custom interface lets you bring elements from your app into the Siri interface, but displaying information that isn’t related to the action can distract people. You also want to avoid duplicating information that the system can display in the Siri or Maps interface. For developer guidance, see [INParameter](https://developer.apple.com/documentation/sirikit/inparameter).

**Make sure people can still perform the action without viewing your custom interface.** People can switch to voice-only interaction with Siri at any time, so it’s crucial to help Siri speak the same information that you display in your custom interface.

**Use ample margins and padding in your custom interface.** Avoid extending content to the edges of your interface unless it’s content that appears to flow naturally offscreen, like a map. In general, provide a margin of 20 points between each edge of your interface and the content. Use the app icon that appears above your interface to guide alignment: content tends to look best when it’s lined up with the center of this icon.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-insets_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-insets_2x.png)

**Minimize the height of your interface.** The system displays other elements above and below your custom interface, such as the text prompt, the spoken response, and the Siri waveform. Aim for a custom interface height that’s no taller than half the height of the screen, so people can see all your content without scrolling.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-height_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-height_2x.png)

**Refrain from displaying your app name or icon.** The system automatically shows this information, so it’s redundant to include it in your custom interface.

For developer guidance, see [Creating an intents UI extension](https://developer.apple.com/documentation/sirikit/creating_an_intents_ui_extension).
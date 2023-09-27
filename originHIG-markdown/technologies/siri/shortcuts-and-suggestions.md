# **[technologies-siri] shortcuts-and-suggestions**

When you support shortcuts, people have a variety of ways to discover and interact with the custom and system intents your app provides. For example:

- Siri can suggest a shortcut for an action people have performed at least once by offering it in search results, on the lock screen, and in the Shortcuts app.
- Your app can supply a shortcut for an action that people haven’t done yet, but might want to do in the future, so that the Shortcuts app can suggest it or it can appear on the [Siri watch face](https://support.apple.com/guide/watch/faces-and-features-apde9218b440/watchos#apdcc88df92c).
- People can use the Shortcuts app to view all their shortcuts and even combine actions from different apps into multistep shortcuts.
- People can also use the Shortcuts app to automate a shortcut by defining the conditions that should run it, like time of day or current location.
- When you provide an Add to Siri button for your custom intent, people can create a shortcut they can run with their voice (for guidance, see [Help people add shortcuts](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#help-people-add-shortcuts)).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-initial-recording_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-initial-recording_2x.png)

The Shortcuts app is also available in macOS 12 and later and in watchOS 7 and later. For developer guidance, see [SiriKit > Shortcuts](https://developer.apple.com/documentation/sirikit#2979425).

# **Make app actions widely available**

*Donating* information about the actions your app supports helps the system offer them to people in various ways, such as:

- In search results
- Throughout the Shortcuts app
- On the lock screen as a Siri Suggestion
- Within the Now Playing view (for recently played media content)
- During Wind Down

Donations also power Automation Suggestions in the Shortcut app’s Gallery, making it easy for people to set up automations for hands-free interactions with your app.

You can also tell the system about shortcuts for actions people haven’t taken yet or make a shortcut available on the Siri watch face (for guidance, see [Suggest shortcuts people might want to add to Siri](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#suggest-shortcuts-people-might-want-to-add-to-siri) and [Display Shortcuts on the Siri Watch face](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#display-shortcuts-on-the-siri-watch-face)). For developer guidance, see [Donating shortcuts](https://developer.apple.com/documentation/sirikit/donating_shortcuts).

**Make a donation every time people perform the action.** When you donate a shortcut each time people perform the associated action, you help the system more accurately predict the best time and place to offer the shortcut.

**Only donate actions that people actually perform.** For example, a coffee-ordering app should donate the *Order coffee* shortcut every time people order coffee, but it shouldn’t make this donation when people do something else, like browse the menu. Similarly, a media app should donate information about a song — like its title and album — only when people are actually listening to it. (For developer guidance, see [Improving Siri media interactions and app selection](https://developer.apple.com/documentation/sirikit/media/improving_siri_media_interactions_and_app_selection).)

**Remove donations for actions that require corresponding data.** If information required by a donated action no longer exists, your app should delete the donation so the shortcut isn’t suggested anymore. For example, if people delete a contact in a messaging app, the app should delete donations for messaging that contact. When people create a shortcut themselves, only they can delete it. For developer guidance, see [Deleting Donated Shortcuts](https://developer.apple.com/documentation/sirikit/deleting_donated_shortcuts).

**If your app handles reservations, consider donating them to the system.** These items — like ticketed events, travel itineraries, or reservations for restaurants, flights, or movies — automatically appear as suggestions in Calendar or Maps. When you donate a reservation, it can appear on the lock screen with a suggestion to check in with your app or as a reminder that uses current traffic conditions to recommend when people should leave. For developer guidance, see [Donating reservations](https://developer.apple.com/documentation/sirikit/siri_event_suggestions/donating_reservations).

### **Suggest Shortcuts people might want to add to Siri**

If your app supports an action that people haven’t performed yet but might find useful, you can provide a *suggested* shortcut to the system so that people can discover it. For example, if people use a coffee-ordering app to order their daily coffee but not to order a holiday special, the app might still want to give them a way to do this with an *Order holiday coffee* shortcut.

Suggested shortcuts appear in both the Gallery and the shortcut editor in the Shortcuts app. Also, your app can display an Add to Siri button that people can use to enable a suggested shortcut while they’re in your app. For developer guidance, see [Suggesting shortcuts to users](https://developer.apple.com/documentation/sirikit/shortcut_management/suggesting_shortcuts_to_users).

### **Display shortcuts on the Siri watch face**

On Apple Watch, people can run shortcuts in several ways. For example, people can ask Siri, tap a shortcut [complication](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/) on a watch face, or use the Shortcuts app available in watchOS 7 and later. You can also make shortcuts available on the Siri watch face.

To have a shortcut appear on the Siri watch face, you define a *relevant* shortcut by including information like the time of day at which your shortcut is relevant and how the shortcut should be displayed on the Siri watch face. The information you supply lets the Siri watch face intelligently display your shortcut to people when they’re in the appropriate context.

For developer guidance, see [Defining relevant shortcuts for your app](https://developer.apple.com/documentation/sirikit/relevant_shortcuts/defining_relevant_shortcuts_for_your_app).

# **Create shortcut titles and subtitles**

Shortcut titles and subtitles appear when the system suggests them or when people add shortcuts to Siri or edit them. In Siri Suggestions on iPhone and Apple Watch, a shortcut can also display an image.

**Be concise but descriptive.** An effective title conveys what happens when the shortcut runs. A subtitle can provide additional detail that supplements — but doesn’t duplicate — the title.

**Start titles with a verb and use sentence-style capitalization without punctuation.** Think of a shortcut title as a brief instruction.

[제목 없음](https://www.notion.so/554292f08526485aaf9b81a21a8f4fe0)

**Lead with important information.** Long titles and subtitles may be truncated in certain contexts, depending on the device’s screen size.

**Exclude your app name.** The system already identifies the app associated with a shortcut.

**Localize titles and subtitles.** Providing content in multiple languages ensures an equally great experience for people everywhere.

**Consider providing a custom image for a more engaging suggestion.** For example, the shortcut for *Order my favorite coffee* could show a cup of the customer’s favorite coffee. Create an image that measures:

- 60x60 pt (180x180 px @ 3x) to display in an iOS app
- 34x34 pt (68x68 px @2x) to display on the Siri watch face on the 44mm Apple Watch (watchOS scales down the image for smaller watches)

# **Help people add shortcuts**

People can add shortcuts from within your app or in the Shortcuts app.

**Offer an Add to Siri button to let people add a shortcut for a common action.** In the Add to Siri sheet that appears when people tap the button, they can type or record a custom voice command (or accept the app’s suggested phrase) and add the shortcut. After the shortcut is added, the button’s text automatically changes to *Added to Siri* and it displays the invocation phrase. These changes show people that they successfully added the shortcut and, crucially, remind them what to say when asking Siri to run it. For guidance on using the Add to Siri button, see [Add to Siri button styles](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#add-to-siri-button-styles).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-not-added_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-not-added_2x.png)

**If you create a custom button to add a shortcut, provide an experience that mirrors the system-provided one.** Display the phrase *Add to Siri* in your custom button. Don’t display alternative phrases — like *add voice command*, *create voice shortcut*, or *make voice prompt* — or display the Siri icon in your custom button. Also, don’t use the Siri icon as a button, or display it anywhere else in your interface. (See [Display multiple shortcuts in one place](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#display-multiple-shortcuts-in-one-place) for guidance on offering several shortcuts in one screen.)

After people use your custom button to add a shortcut, it’s important to display their trigger phrase to help them remember it. If you created a custom Add to Siri button, you can mirror the system-provided experience and update the button to display *Added to Siri* followed by the phrase.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-added_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-added_2x.png)

**Let people edit and remove the shortcuts they added.** When people tap the trigger phrase displayed in your app after adding a shortcut, show the shortcut editing view again so they can update the phrase or delete the shortcut.

**Update the shortcuts your app displays.** People can add, remove, and update your app’s shortcuts in the Shortcuts app. However, the Shortcuts app doesn’t notify your app when these changes occur. It’s your app’s responsibility to keep its interface up to date with the latest shortcut changes.

# **Provide default phrases for shortcuts**

Your app provides default phrases for shortcuts during setup. People can personalize these phrases when adding your shortcuts to Siri.

**Keep phrases short and memorable.** Bear in mind that people must speak your phrase verbatim, so long or confusing phrases may result in mistakes and frustration. Two- and three-word phrases tend to work best. More words can be harder for people to remember, and phrases that are too long will get truncated.

**Make sure the phrases you suggest are accurate and specific.** Phrases like *Reorder coffee* or *Order my usual coffee* clearly describe what the shortcut does, which makes it easier for people to remember the phrase later. Also make sure that your suggested phrases are specific to each shortcut’s scope. For example, *Watch baseball* is clearer and more memorable than *Watch sports*. It’s also important to avoid implying that people can vary a shortcut’s invocation phrase to get a different result. For example, people might interpret a phrase like *Order a large clam chowder* to mean that your shortcut will give them what they want if they substitute “small” for “large” and “lobster bisque” for “clam chowder.”

**Don’t commandeer core Siri commands.** For example, your app should never suggest a phrase like *Call 911* or include the text *Hey Siri*.

# **Make shortcuts customizable**

When you define a parameter for each detail your app needs to perform an intent, people can customize the shortcut by editing these details in the Shortcuts app or your Add to Siri sheet.

To show people which details they can edit and how their edits affect the action, you provide a *parameter summary*. A parameter summary succinctly describes the action by using the parameters in a sentence that begins with a verb. For example, a customizable *Order coffee* shortcut could display a parameter summary like “Order *quantity* *coffee*” where *quantity* and *coffee* are the parameters that people can edit. Here’s an example of how the *Order coffee* shortcut might look after people supply values for the *quantity* and *coffee* parameters.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/edited-parameter-summary_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/edited-parameter-summary_2x.png)

**Provide a parameter summary for each custom intent you support.** At minimum, your parameter summary should include all parameters your intent requires and any parameters that receive values from other apps or actions. The summary doesn’t have to include optional parameters or parameters that people aren’t likely to edit; if you omit parameters like these from the summary, people can still access them in the Show More section.

**Craft a short parameter summary that’s clearly related to your intent’s title.** When the intent title and the parameter summary are similar, it’s easy for people to recognize the action regardless of where they view it. Aim to use the same words in the summary and the title — in particular, it’s helpful to begin both phrases with the same verb. For example, if your intent title is “Search encyclopedia”, a good parameter summary could be “Search encyclopedia for *search term*”.

**Aim for a parameter summary that reads like a sentence.** Use sentence-style capitalization, but don’t include ending punctuation. When possible, avoid punctuation entirely. Punctuation within a summary — especially colons, semicolons, and parentheses — can make the summary hard to read and understand.

**Provide multiple parameter summaries when necessary.** If your action includes a parameter that has a parent-child relationship with other parameters, you can provide multiple variants of the summary based on the current value of the parent parameter. For example, if your *order coffee*shortcut lets people specify whether they want to pick up their order or have it delivered, your parameter summary should reflect the current choice. In this scenario, you should create one parameter summary that helps people pick a store location and another summary that helps them pick a delivery address. Be sure to use a consistent grammatical structure and parameter order in all variants of the summary that you create.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/parent-parameter-choice_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/parent-parameter-choice_2x.png)

Delivery or pickup

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/child-parameter-choice_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/child-parameter-choice_2x.png)

Delivery location

**Provide output parameters for information that people can use in a multistep shortcut.** For example, an *order coffee* action might provide output that includes the estimated delivery time and the cost of the order. With this information, people could create a multistep shortcut that messages a friend about the delivery time and logs the transaction in their favorite budgeting app.

**Consider defining an input parameter.** When you define an input parameter for an action, the action can automatically receive output from a preceding action in a multistep shortcut. For example, if your action applies a filter to the image it receives in an *image* parameter, you might designate *image* as the input parameter so that it automatically accepts images from other actions. You configure an input parameter in your intent definition file (shown in “Define User-Configurable Shortcuts” in [Adding user interactivity with Siri shortcuts and the Shortcuts app](https://developer.apple.com/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app)).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/input-output-parameters_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/input-output-parameters_2x.png)

**Help people distinguish among different variations of the same action.** For example, an app that offers a *send message* action might use a contact photo to help people visually distinguish the various messages they send. To do this, choose the parameter that’s most identifiable to people and designate it as the key parameter (shown in “Define User-Configurable Shortcuts” in [Adding user interactivity with Siri shortcuts and the Shortcuts app](https://developer.apple.com/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app)). Be sure to provide an image for the key parameter every time you donate the action (for developer guidance, see [INImage](https://developer.apple.com/documentation/sirikit/inimage)).

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/multiple-intent-configurations_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/multiple-intent-configurations_2x.png)

**Avoid providing multiple actions that perform the same basic task.** For example, instead of providing an action that adds text to a note and a different action that adds an image, consider providing a single action that lets people add both types of content. Providing a few high-level actions can make it easier for people to understand what the actions do when they’re combined in a multistep shortcut.

For developer guidance, see [Shortcut management](https://developer.apple.com/documentation/sirikit/shortcut_management).

# **Add to Siri button styles**

The Add to Siri button is available in several visual styles. You can also customize the corner radius of the buttons to match your app’s interface.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black_2x.png)

**Black.** Use on white or light-color backgrounds that provide sufficient contrast. Don’t use on black or dark backgrounds.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black-Outlined_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black-Outlined_2x.png)

**Black with outline.** Use on dark backgrounds that provide sufficient contrast. Don’t use on white or light-color backgrounds.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White_2x.png)

**White.** Use on dark backgrounds that provide sufficient contrast. Don’t use on white or light-color backgrounds.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White-Outlined_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White-Outlined_2x.png)

**White with outline.** Use on white or light-color backgrounds that don’t provide sufficient contrast. Don’t use on dark or saturated backgrounds.

**Accommodate the variable width of the Add to Siri button.** The width of the button varies in different locales and when updated to display the user’s invocation phrase.

**Maintain clear space around the Add to Siri button.** At minimum, leave padding of 1/10 the button’s height on all sides of the button.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-ClearSpace_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-ClearSpace_2x.png)

# **Display multiple shortcuts in one place**

If your app contains more than a few shortcuts, consider creating a dedicated area of the app to display them. A dedicated screen makes it easy for people to see all of your app’s shortcuts at a glance and to add the shortcuts they want to use. Alternatively, consider offering follow-up questions to support additional options for a single shortcut.

**Use an unambiguous title for your list of shortcuts.** For example, using “Siri Shortcuts” for the navigation bar title clearly communicates the purpose of the screen.

**Consider creating a custom Add button for a list of shortcuts.** The system-provided Add to Siri button can add too much visual weight when it’s used several times in one view. If the screen makes it clear that all the items in the list are Siri Shortcuts, you can display a simpler button that uses “Add” or “+” for each shortcut in the list.

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-list-shortcuts-added_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-list-shortcuts-added_2x.png)

**Provide feedback when a shortcut has been added.** Show people that they’ve successfully added a shortcut by replacing the Add button with an Edit button and displaying the phrase they recorded. Alternatively, you can remove the Add button and let people tap the phrase they recorded to open an editing view.
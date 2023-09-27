Writing
=======

The words you choose within your app are an essential part of its user experience.![A sketch of a document and pencil, suggesting written content. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/5bd05331c62b850b25ac62f8581b97b6/foundations-writing-intro@2x.png)

Whether you’re building an onboarding experience, writing an alert, or describing an image for accessibility, designing through the lens of language will help people get the most from your app or game.

[Getting started](/design/human-interface-guidelines/writing#Getting-started)
-----------------------------------------------------------------------------

**Determine your app’s voice.** Think about who you’re talking to, so you can figure out the type of vocabulary you’ll use. What types of words are familiar to people using your app? How do you want people to feel? The words for a banking app might convey trust and stability, for example, while the words in a game might convey excitement and fun. Create a list of common terms, and reference that list to keep your language consistent. Consistent language, along with a voice that reflects your app’s values, helps everything feel more cohesive.

**Match your tone to the context.** Once you’ve established your app’s voice, vary your tone based on the situation. Consider what people are doing while they’re using your app — both in the physical world and within the app itself. Are they exercising and reached a goal? Or are they trying to make a payment and received an error? Situational factors affect both what you say and how you display the text on the screen.

Compare the tone of these two examples from Apple Watch. In the first, the tone is straightforward and direct, reflecting the seriousness of the situation. In the second, the tone is light and congratulatory.

![A screenshot of a Fall Detection message that reads: it looks like you've taken a hard fall.](https://docs-assets.developer.apple.com/published/58f94ca509ec5b915b6c3b8ea21aaf9f/fall-detection-message@2x.png)![A screenshot of an Activity message that reads: you set a personal record for your longest daily Move streak, 35 days!](https://docs-assets.developer.apple.com/published/54d5ea9ec7d50374459f8ab01ee6b9ea/move-streak-message@2x.png)**Be clear.** Choose words that are easily understood and convey the right thing. Check each word to be sure it needs to be there. If you can use fewer words, do so. When in doubt, read your writing out loud.

**Write for everyone.** For your app to be useful for as many people as possible, it needs to speak to as many people as possible. Choose simple, plain language and write with accessibility and localization in mind, avoiding jargon and gendered terminology. For guidance, see [Writing inclusively](https://help.apple.com/applestyleguide/#/apdcb2a65d68)
 and [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/accessibility#VoiceOver)
; for developer guidance, see [Localization](https://developer.apple.com/documentation/xcode/localization)
.

[Best practices](/design/human-interface-guidelines/writing#Best-practices)
---------------------------------------------------------------------------

**Consider each screen’s purpose**. Pay attention to the order of elements on a screen, and put the most important information first. Format your text to make it easy to read. If you’re trying to convey more than one idea, consider breaking up the text onto multiple screens, and think about the flow of information across those screens.

**Be action oriented.** Active voice and clear labels help people navigate through your app from one step to the next, or from one screen to another. When labeling buttons and links, it’s almost always best to use a verb. Prioritize clarity and avoid the temptation to be too cute or clever with your labels. For example, just saying “Next” often works better than “Let’s do this!” For links, avoid using “Click here” in favor of more descriptive words or phrases, such as “Learn more about UX Writing.” This is especially important for people using screen readers to access your app.

**Build language patterns.** Consistency builds familiarity, helping your app feel cohesive, intuitive, and thoughtfully designed. It also makes writing for your app easier, as you can return to these patterns again and again. Here are a few language patterns to consider establishing:

* **Title or sentence case.** Decide whether you want to use title case or sentence case for alerts, page titles, headlines, button labels, and links. Throughout the HIG, you’ll find guidelines for specific components, but how you format your text is a reflection of your app’s voice. Title case is more formal, while sentence case is more casual. Choose a style that fits your app.
* **First or second person.** If your app allows people to save favorites or bookmark items, for example, those items could be found in “My Favorites” or “Your Saved Items,” but don’t use both. Choose first or second person and stick with it.
* **Continue or Next.** If your app has a flow that spans multiple screens, decide how you want to label the button or link that takes you from one step to the next. “Continue” or “Next” works well, but choose one and be consistent with how you use it. Make sure you indicate a difference at the end of the flow, like a button labeled “Done.”

**Write for how people use each device.** People may use your app on several types of devices. While your language needs to be consistent across them, think about where it would be helpful to adjust your text to make it suitable for different devices. Make sure you describe gestures correctly on each device — for example, not saying “click” for a touch device like iPhone or iPad where you mean “tap.”

Where and how people use a device, its screen size, and its location all affect how you write for your app. iPhone and Apple Watch, for example, offer opportunities for personalization, but their small screens require brevity. TVs, on the other hand, are often in common living spaces, and several people are likely to see anything on the screen, so consider who you’re addressing. Bigger screens also require brevity, as the text must be large for people to see it from a distance.

**Provide clear next steps on any blank screens.** An empty state, like a completed to-do list or bookmarks folder with nothing in it, can provide a good opportunity to make people feel welcome and educate them about your app. Empty states can also showcase your app’s voice, but make sure that the content is useful and fits the context. An empty screen can be daunting if it isn’t obvious what to do next, so guide people on actions they can take, and give them a button or link to do so if possible. Remember that empty states are usually temporary, so don’t show crucial information that could then disappear.

**Write clear error messages.** It’s always best to help people avoid errors. When an error message is necessary, display it as close to the problem as possible, avoid blame, and be clear about what someone can do to fix it. For example, “That password is too short” isn’t as helpful as “Choose a password with at least 8 characters.” Remember that errors can be frustrating. Interjections like “oops!” or “uh-oh” are typically unnecessary and can sound insincere. If you find that language alone can’t address an error that’s likely to affect many people, use that as an opportunity to rethink the interaction.

**Choose the right delivery method.** There are many ways to get people’s attention, whether or not they are actively using your app. When there’s something you want to communicate, consider the urgency and importance of the message. Think about the context in which someone might see the message, whether it requires immediate action, and how much supporting information someone might need. Choose the correct delivery method, and use a tone appropriate for the situation. For guidance, see [Notifications](/design/human-interface-guidelines/notifications)
, [Alerts](/design/human-interface-guidelines/alerts)
, and [Action sheets](/design/human-interface-guidelines/action-sheets)
.

**Keep settings labels clear and simple.** Help people easily find the settings they need by labeling them as practically as possible. If the setting label isn’t enough, add an explanation. Describe what it does when turned on, and people can infer the opposite. In the Handwashing Timer setting for Apple Watch, for example, the description explains that a timer can start when you’re washing your hands. It isn’t necessary to tell you that a timer won’t start when this setting is off.

![A partial screenshot showing the Handwashing Timer description, which reads: Apple Watch can detect when you're washing your hands and start a 20-second timer.](https://docs-assets.developer.apple.com/published/d313580ca52395f9227953797ce98537/handwashing-settings@2x.png)If you need to direct someone to a setting, provide a direct link or button, rather than trying to describe its location. For guidance, see [Settings](/design/human-interface-guidelines/settings)
.

**Show hints in text fields.** If your app allows people to enter their own text, like account or contact information, label all fields clearly, and use hint or placeholder text so people know how to format the information. You can give an example in hint text, like “name@example.com,” or describe the information, such as “Your name.” Show errors right next to the field, and instruct people how to enter the information correctly, rather than scolding them for not following the rules. “Use only letters for your name” is better than “Don’t use numbers or symbols.” Avoid robotic error messages with no helpful information, like “Invalid name.” For guidance, see [Text fields](/design/human-interface-guidelines/text-fields)
.

[Platform considerations](/design/human-interface-guidelines/writing#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/writing#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/writing#Related)

[Apple Style Guide](https://help.apple.com/applestyleguide/#/)


[Writing inclusively](https://help.apple.com/applestyleguide/#/apdcb2a65d68)


[Inclusion](/design/human-interface-guidelines/inclusion)


[Accessibility](/design/human-interface-guidelines/accessibility)


[Color](/design/human-interface-guidelines/color)


#### [Videos](/design/human-interface-guidelines/writing#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/E58B8A59-15C1-4FB4-B61A-23DBA2AF6D28/6530_wide_250x141_1x.jpg) Writing for interfaces](https://developer.apple.com/videos/play/wwdc2022/10037) 
[Change log](/design/human-interface-guidelines/writing#Change-log)
-------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| February 27, 2023 | New page. |


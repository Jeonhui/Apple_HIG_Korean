Action button
=============

The Action button can offer specific actions in workout apps running in watchOS 9 and later on Apple Watch Ultra.![A sketch of an arrow pointing toward the action button on the side of an Apple Watch, suggesting initiating an action. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/e9f0fbe50cec4b4b3ac0ef5daa14e321/inputs-action-button-intro@2x.png)

When wearing Apple Watch Ultra, people can use the Action button to easily start or progress through functions in apps that support Workout, Shortcuts, and Dive actions. The Action button can also give people quick access to system-provided functionality, like turning Flashlight on and off or marking a Compass Waypoint. People choose an initial function for the Action button when they set up their device; later, they can adjust this choice in Settings.

Depending on the actions you support, people can choose the function that occurs when they press the Action button for the first time and — in some cases — they can choose the actions that occur on subsequent presses. For example, when an app supports Shortcuts, people simply choose the Shortcut they want the Action button to initiate, making additional button presses unnecessary. In contrast, a Workout app might let people start a triathlon with the first button press and switch to another segment with a subsequent press.

Important

Apps don’t respond when people press and hold the Action button because watchOS reserves this interaction for the emergency SOS feature.

[Best practices](/design/human-interface-guidelines/action-button#Best-practices)
---------------------------------------------------------------------------------

**Offer a set of essential actions from which people can choose the one they want to initiate with the first button press.** For example, if your app helps people track their progress during a triathlon, the “Start Race” action might be the one most people want to initiate when they first press the Action button. Avoid offering an Action button action that merely opens your app; your app icon and complications already give people quick ways to open your app.

**Consider offering a secondary function that supports or advances the primary action people choose.** People often use the Action button without looking at the screen, so a subsequent button press needs to flow logically from the first press, while also making sense in the current context. If your app supports Workout or Dive actions, consider designing a simple, intuitive secondary function that people can easily learn and remember. Consider carefully before you offer more than one secondary function, because doing so can increase people’s cognitive load and make your app seem harder to use.

**For each action you support, write a short label that succinctly describes it.** People view your labels when they visit Settings to choose the action they want the Action button to initiate. Using [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)
, create a label that begins with a verb, uses present tense, and avoids including articles and prepositions. For example, use “Start Race” instead of “Started Race” or “Start the Race.”

**Pause the current function when people press the Action and side buttons together.** The exception is in a diving app where pausing a dive could be dangerous to the diver, causing them to lose track of their depth or not understand how long they’ve been underwater. Unless pausing the current function would result in a negative experience, be sure to meet people’s expectations by letting them pause their current activity when they press both buttons at the same time.

**Prefer using subsequent button presses to support additional functionality; avoid offering a “stop” or “conclude” function.** If you need to let people stop their main task — as opposed to pausing the current function — offer this option within your interface instead.

**Prefer letting the system show people how to use the Action button with your app.** When you support the Action button, the system automatically helps people configure it to initiate one of your app’s actions. If necessary, you can provide content that teaches people how to use the Action button with your app, but be sure to avoid creating content that repeats or conflicts with the system-provided flow.

[Platform considerations](/design/human-interface-guidelines/action-button#Platform-considerations)
---------------------------------------------------------------------------------------------------

*Not supported in iOS, iPadOS, macOS, tvOS, or visionOS.*

[Resources](/design/human-interface-guidelines/action-button#Resources)
-----------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/action-button#Related)

[Workouts](/design/human-interface-guidelines/workouts)


[Digital Crown](/design/human-interface-guidelines/digital-crown)


[Change log](/design/human-interface-guidelines/action-button#Change-log)
-------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| September 14, 2022 | New page. |


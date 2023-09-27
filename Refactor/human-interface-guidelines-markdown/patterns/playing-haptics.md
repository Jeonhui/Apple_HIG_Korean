June 21, 2023

 Updated to include guidance for visionOS. Playing haptics
===============

Playing haptics can engage people’s sense of touch and bring their familiarity with the physical world into your app or game.![A sketch of a horizontal line of three slightly overlapping circles, suggesting vibration. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/367115f42d7b6235a3087fd140366955/patterns-playing-haptics-intro@2x.png)

The system can play haptics in addition to visual and auditory feedback to communicate things like the confirmation of an Apple Pay transaction or the arrival of a notification in iOS and watchOS. On a Mac that’s equipped with a Force Touch trackpad, apps can play haptics while people are dragging content or respond to different strengths of a force click to cause different levels of change in an onscreen element. In a tvOS or iPadOS app, game controllers can provide haptic feedback.

Depending on the platform, the system may provide haptic feedback for standard components by default. For example, components like switches, sliders, and pickers automatically play haptic feedback on supported iPhone models; on Apple Watch, the Taptic Engine generates haptics and watchOS combines an audible tone with some of them. In addition, the system may provide built-in haptic patterns you can use in your app or game or even let you design custom ones.

[Best practices](/design/human-interface-guidelines/playing-haptics#Best-practices)
-----------------------------------------------------------------------------------

**Use system-provided haptic patterns according to their documented meanings.** People recognize standard haptics because the system plays them consistently on interactions with standard controls. If the documented use case for a pattern doesn’t make sense in your app, use a generic pattern or create your own, where supported. For guidance, see [Custom haptics](/design/human-interface-guidelines/playing-haptics#Custom-haptics)
.

**Use haptics consistently.** It’s important to build a clear, causal relationship between each haptic and the action that causes it so people learn to associate certain haptic patterns with certain experiences. If a haptic doesn’t reinforce a cause-and-effect relationship, it can be confusing and seem gratuitous. For example, if your app plays a specific haptic pattern when a game character fails to finish a mission, people associate that pattern with a negative outcome. If you use the same haptic pattern for a positive outcome like a level completion, people will be confused.

**Use haptics in ways that complement other feedback in your app.** When visual, auditory, and tactile feedback are in harmony — as they generally are in the physical world — the user experience is more coherent and can seem more natural. For example, match the intensity and sharpness of a haptic with the animation you use to accompany it. You can also synchronize sound with haptics; for developer guidance, see [Delivering Rich App Experiences with Haptics](/documentation/corehaptics/delivering_rich_app_experiences_with_haptics)
.

**Avoid overusing haptics.** Sometimes a haptic can feel just right when it happens occasionally, but become tiresome when it plays frequently. It’s important to do user testing that can help you discover a balance that most people appreciate. Often, the best haptic experience is one that people may not be conscious of, but miss when it’s turned off.

**Make haptics optional.** Let people turn off or mute haptics if they wish, and make sure people can still enjoy your app without them.

**Be aware that playing haptics might impact other user experiences.** By design, haptics produce enough physical force for people to feel the vibration. Ensure that haptic vibrations don’t disrupt user experiences involving the camera, gyroscope, or microphone.

[Custom haptics](/design/human-interface-guidelines/playing-haptics#Custom-haptics)
-----------------------------------------------------------------------------------

Games often use custom haptics to enhance gameplay. Although it’s less common, nongame apps might also use custom haptics to provide a richer, more delightful experience.

You can design custom haptic patterns that vary dynamically, based on user input or context. For example, the impact players feel when a game character jumps from a tree can be stronger than when the character jumps in place, and substantial experiences — like a collision or a hit — can feel very different from subtle experiences like the approach of footsteps or a looming danger.

There are two basic building blocks you can use to generate custom haptic patterns.

* *Transient* events are brief and compact, often feeling like taps or impulses. The experience of tapping the Flashlight button on the Home Screen is an example of a transient event.
* *Continuous* events feel like sustained vibrations, such as the experience of the lasers effect in a message.

Regardless of the type of haptic event you use to generate a custom haptic, you can also control its *sharpness* and *intensity*. You can think of sharpness as a way to abstract a haptic experience into the waveform that produces the corresponding physical sensations. Specifying sharpness lets you relay to the system your intent for the experience. For example, you might use sharpness values to convey an experience that’s soft, rounded, or organic, or one that’s crisp, precise, or mechanical. As the term implies, intensity means the strength of the haptic.

By combining transient and continuous events, varying sharpness and intensity, and including optional audio content, you can create a wide range of different haptic experiences. For developer guidance, see [Core Haptics](/documentation/corehaptics)
.

[Platform considerations](/design/human-interface-guidelines/playing-haptics#Platform-considerations)
-----------------------------------------------------------------------------------------------------

### [iPadOS, tvOS, visionOS](/design/human-interface-guidelines/playing-haptics#iPadOS-tvOS-visionOS)

Game controllers can play haptics and you can support game controller input in your apps. For developer guidance, see [Playing Haptics on Game Controllers](/documentation/corehaptics/playing_haptics_on_game_controllers)
.

### [iOS](/design/human-interface-guidelines/playing-haptics#iOS)

On supported iPhone models, you can add haptics to your experience in the following ways:

* Use standard UI components — like [toggles](https://developer.apple.com/design/human-interface-guidelines/toggles)
, [sliders](https://developer.apple.com/design/human-interface-guidelines/sliders)
, and [pickers](https://developer.apple.com/design/human-interface-guidelines/pickers)
 — that play Apple-designed system haptics by default.
* When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of [notification](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Notification)
, [impact](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Impact)
, and [selection](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Selection)
 (for developer guidance, see [`UIFeedbackGenerator`](/documentation/uikit/uifeedbackgenerator)
).

#### [Notification](/design/human-interface-guidelines/playing-haptics#Notification)

Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.

 [Play](#) 
**Success.** Indicates that a task or action has completed. [Play](#) 
**Warning.** Indicates that a task or action has produced a warning of some kind. [Play](#) 
**Error.** Indicates that an error has occurred.#### [Impact](/design/human-interface-guidelines/playing-haptics#Impact)

Impact haptics provide a physical metaphor you can use to complement a visual experience. For example, people might feel a tap when a view snaps into place or a thud when two heavy objects collide.

 [Play](#) 
**Light.** Indicates a collision between small or lightweight UI objects. [Play](#) 
**Medium.** Indicates a collision between medium-sized or medium-weight UI objects. [Play](#) 
**Heavy.** Indicates a collision between large or heavyweight UI objects. [Play](#) 
**Rigid.** Indicates a collision between hard or inflexible UI objects. [Play](#) 
**Soft.** Indicates a collision between soft or flexible UI objects.#### [Selection](/design/human-interface-guidelines/playing-haptics#Selection)

Selection haptics provide feedback while the values of a UI element are changing.

 [Play](#) 
**Selection.** Indicates that a UI element’s values are changing.### [macOS](/design/human-interface-guidelines/playing-haptics#macOS)

When a Magic Trackpad is available, your app can provide one of the three following haptic patterns in response to a drag operation or force click.



| Haptic feedback pattern | Description |
| --- | --- |
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don’t apply. |

For developer guidance, see [`NSHapticFeedbackPerformer`](/documentation/appkit/nshapticfeedbackperformer)
.

### [watchOS](/design/human-interface-guidelines/playing-haptics#watchOS)

Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content. By default, the system provides linear haptic detents that people can feel as they rotate the Digital Crown. Some system controls, like table views, provide detents as new items scroll onto the screen. For developer guidance, see [`WKHapticType`](/documentation/watchkit/wkhaptictype)
.

watchOS defines the following set of haptics, each of which conveys a specific meaning to people.

* [Notification](#)
* [Up](#)
* [Down](#)
* [Success](#)
* [Failure](#)
* [Retry](#)
* [Start](#)
* [Stop](#)
* [Click](#)
 [Play](#) 
**Notification.** Tells the person that something significant or out of the ordinary has happened and requires their attention. The system plays this same haptic when a local or remote notification arrives.

 [Play](#) 
**Up.** Tells the person that an important value increased above a significant threshold.

 [Play](#) 
**Down.** Tells the person that an important value decreased below a significant threshold.

 [Play](#) 
**Success.** Tells the person that an action completed successfully.

 [Play](#) 
**Failure.** Tells the person that an action failed.

 [Play](#) 
**Retry.** Tells the person that an action failed but they can retry it.

 [Play](#) 
**Start.** Tells the person that an activity started. Use this haptic when starting a timer or any other activity that a person can explicitly start and stop. The stop haptic usually follows this haptic.

 [Play](#) 
**Stop.** Tells the person that an activity stopped. Use this haptic when stopping a timer or other activity that the person previously started.

 [Play](#) 
**Click.** Provides the sensation of a dial clicking, helping you communicate progress at predefined increments or intervals. Overusing the click haptic tends to diminish its utility and can even be confusing when clicks overlap each other.

[Resources](/design/human-interface-guidelines/playing-haptics#Resources)
-------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/playing-haptics#Related)

[Feedback](/design/human-interface-guidelines/feedback)


[Gestures](/design/human-interface-guidelines/gestures)


#### [Developer documentation](/design/human-interface-guidelines/playing-haptics#Developer-documentation)

[Core Haptics](/documentation/corehaptics)


#### [Videos](/design/human-interface-guidelines/playing-haptics#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/100FA6DD-1A48-485A-AFC2-47FDB92376D3/5210_wide_250x141_1x.jpg) Practice audio haptic design](https://developer.apple.com/videos/play/wwdc2021/10278) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/48/9EEAE751-B5EE-4934-8F3A-38361FBA05DE/3277_wide_250x141_1x.jpg) Introducing Core Haptics](https://developer.apple.com/videos/play/wwdc2019/520) 
[Change log](/design/human-interface-guidelines/playing-haptics#Change-log)
---------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |


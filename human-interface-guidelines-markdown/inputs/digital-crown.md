June 21, 2023

 Updated to include guidance for visionOS. Digital Crown
=============

The Digital Crown is an important hardware input for Apple Vision Pro and Apple Watch.![A sketch of a curved arrow beside a Digital Crown, that suggests turning the Digital Crown. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/3b12fdaf898877ad12d62535cea6d032/inputs-digital-crown-intro@2x.png)

On both Apple Vision Pro and Apple Watch, people can use the Digital Crown to interact with the system; on Apple Watch, people can also use the Digital Crown to interact with apps.

[Apple Vision Pro](/design/human-interface-guidelines/digital-crown#Apple-Vision-Pro)
-------------------------------------------------------------------------------------

On Vision Pro, people use the Digital Crown to:

* Adjust volume
* Adjust the level of immersion in a portal or an Environment
* Recenter content so it’s in front of them
* Open Accessibility settings
* Exit an app and return to the Home View

Note that in a fully immersive app (that is, an app that uses [`FullImmersionStyle`](/documentation/SwiftUI/FullImmersionStyle)
), people can use the Digital Crown to exit the app, but not to affect the level of immersion. To learn more, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

Important

Although the system can notify your app when people recenter your content, you don’t receive direct information from the Digital Crown, no matter how a person uses it.

[Apple Watch](/design/human-interface-guidelines/digital-crown#Apple-Watch)
---------------------------------------------------------------------------

As people turn the Digital Crown, it generates information you can use to enhance or facilitate interactions with your app, like scrolling or operating standard or custom controls.

Starting with watchOS 10, the Digital Crown takes on an elevated role as the primary input for navigation. On the watch face, people turn the Digital Crown to view widgets in the Smart Stack, and on the Home Screen, people use it to move vertically through their collection of apps. Within apps, people turn the Digital Crown to switch between vertically paginated tabs, and to scroll through list views and variable height pages.

Beyond its use for navigation, turning the Digital Crown generates information you can use to enhance or facilitate interactions with your app, such as inspecting data or operating standard or custom controls.

Note

Apps don’t respond to presses on the Digital Crown because watchOS reserves these interactions for system-provided functionality like revealing the Home Screen.

Most Apple Watch models provide haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content. By default, the system provides linear haptic *detents* — or taps — as people turn the Digital Crown a specific distance. Some system controls, like table views, provide detents as new items scroll onto the screen.

**Anchor your app’s navigation to the Digital Crown.** Starting with watchOS 10, turning the Digital Crown is the main way people navigate within and between apps. List, tab, and scroll views are vertically oriented, allowing people to use the Digital Crown to easily move between the important elements of your app’s interface. When anchoring interactions to the Digital Crown, also be sure to back them up with corresponding touch screen interactions.

**Consider using the Digital Crown to inspect data in contexts where navigation isn’t necessary.** In contexts where the Digital Crown doesn’t need to navigate through lists or between pages, it’s a great tool to inspect data in your app. For example, in World Clock, turning the Digital Crown advances the time of day at a selected location, allowing people to compare various times of day to their current time.

**Provide visual feedback in response to Digital Crown interactions.** For example, pickers change the currently displayed value as people use the Digital Crown. If you track turns directly, use this data to update your interface programmatically. If you don’t provide visual feedback, people are likely to assume that turning the Digital Crown has no effect in your app.

**Update your interface to match the speed with which people turn the Digital Crown.** People expect turning the Digital Crown to give them precise control over an interface, so it works well to use this speed to determine the speed at which you make changes. Avoid updating content at a rate that makes it difficult for people to select values.

**Use the default haptic feedback when it makes sense in your app.** If haptic feedback doesn’t feel right in the context of your app — for example, if the default detents don’t match your app’s animation — turn off the detents. You can also adjust the haptic feedback behavior for tables, letting them use linear detents instead of row-based detents. For example, if your table has rows with significantly different heights, linear detents may give people a more consistent experience.

[Platform considerations](/design/human-interface-guidelines/digital-crown#Platform-considerations)
---------------------------------------------------------------------------------------------------

*Not supported in iOS, iPadOS, macOS, or tvOS.*

[Resources](/design/human-interface-guidelines/digital-crown#Resources)
-----------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/digital-crown#Related)

[Feedback](/design/human-interface-guidelines/feedback)


[Action button](/design/human-interface-guidelines/action-button)


[Immersive experiences](/design/human-interface-guidelines/immersive-experiences)


#### [Developer documentation](/design/human-interface-guidelines/digital-crown#Developer-documentation)

[`WKCrownDelegate`](/documentation/watchkit/wkcrowndelegate)


#### [Videos](/design/human-interface-guidelines/digital-crown#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/2C47B638-090D-4CBB-9E9E-EBE8114536D9/8132_wide_250x141_1x.jpg) Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_1x.jpg) Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/B1446E95-6CAF-4E43-BAE7-0C7041B44B94/8054_wide_250x141_1x.jpg) Meet watchOS 10](https://developer.apple.com/videos/play/wwdc2023/10026) 
[Change log](/design/human-interface-guidelines/digital-crown#Change-log)
-------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Added guidelines emphasizing the central role of the Digital Crown for navigation. |


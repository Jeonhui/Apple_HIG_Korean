June 21, 2023

 New page. Eyes
====

In visionOS, people look at a virtual object to bring focus to it, identifying it as a target they can interact with.![A sketch of a human eye. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/126393ded1c486236fc7a9feabea30ea/inputs-eyes-intro@2x.png)

When people look at an interactive object, visionOS highlights it, providing visual feedback that helps them confirm the object is one they want. The visual feedback, or *hover effect*, shows that the object is focused, which means that people can use an [indirect gesture](/design/human-interface-guidelines/gestures#visionOS)
 like tap to interact with it. For example, people can return to the previous webpage in Safari by looking at the back button to focus it and then tapping. Similarly, people can look at an individual photo in their Photos library and tap to open it.

In rare cases, the system can automatically display an expanded view of a component after it’s focused. For example, when people look at a tab bar, the entire bar resizes to reveal text labels next to each tab. In this scenario, an individual tab also highlights before the tab bar expansion to let people select it before revealing the labels. A system-provided button can also reveal a tooltip when people look at it.

Important

To help preserve people’s privacy, visionOS doesn’t provide direct information about where people are looking before they tap. When you use system-provided components, visionOS automatically tells you when people tap the component. For developer guidance, see [Adopting best practices for privacy and user preferences](/documentation/visionOS/adopting-best-practices-for-privacy)
.

For general guidance on focus, see [Focus and selection](/design/human-interface-guidelines/focus-and-selection)
.

[Best practices](/design/human-interface-guidelines/eyes#Best-practices)
------------------------------------------------------------------------

**Always give people multiple ways to interact with your app.** Design your app to support the accessibility features people use to personalize the ways they interact with their devices. For guidance, see [Accessibility](/design/human-interface-guidelines/accessibility)
.

**Design for visual comfort.** Help people accomplish their primary task by making sure that the objects they need to use are within their [field of view](/design/human-interface-guidelines/spatial-layout#Field-of-view)
. When your app is running in the Shared Space, the system automatically places windows and volumes in convenient locations; if your app is running in a Full Space, you may need to request access to information about a person’s head pose to help you place app content appropriately. You can also improve the visual comfort of your experience when you avoid requiring people to make multiple quick eye adjustments, either over a large area or through multiple levels of depth. For guidance, see [Depth](/design/human-interface-guidelines/spatial-layout#Depth)
.

**Place content at a comfortable viewing distance.** For example, to help people remain comfortable while they read or engage with content over time, aim to place it at least one meter away. In general, you don’t want to place content very close to people unless they’ll view or interact with it for only a little while.

**Make it easy for people to focus an item by providing enough space around it.** Because eyes naturally tend to make small, quick adjustments in direction even while people are looking at one place, crowding UI objects together can make it difficult for people to look at one of them without jumping to another. You can help ensure that there’s enough space between interactive items by using a margin of at least 16 points around the bounds of each item or by placing items so that their centers are always at least 60 points apart. For additional layout guidance, see [Layout](/design/human-interface-guidelines/layout)
 and [Spatial layout](/design/human-interface-guidelines/spatial-layout)
.

**Consider using subtle visual cues to encourage people to look at the item they’re most likely to want.** For example, it often works well to place the item near the center of the field of view or use techniques like gentle motion, increased contrast, or variations in color or scale to draw people’s attention. In general, prefer cues that are noticeable without being flashy or harsh.

**Minimize visual distractions.** When there’s a lot of visual noise, it can be difficult for people to find the object they’re looking for. Visual movement can be even more distracting: When people sense movement — especially in their peripheral vision — they tend to respond automatically by looking at it, making it hard to maintain focus on the object they’re interested in.

**Avoid using a repeating pattern or texture that fills the field of view.** In some cases, people’s eyes can lock onto different elements in a pattern or texture, making the elements appear to have different depths. To avoid this effect, consider using the pattern in a smaller area.

**Prefer using standard UI components.** System-provided components provide consistent visual feedback when people look at them and behave consistently when focused. If your custom components use different visual cues to provide visual feedback, it can be difficult for people to learn and remember how these components work in your app.

**In general, give an interactive item a rounded shape.** People’s eyes tend to be drawn toward the corners in a shape, making it difficult to maintain focus on the shape’s center. The more rounded an item’s shape, the easier it is for people to focus it.

[Platform considerations](/design/human-interface-guidelines/eyes#Platform-considerations)
------------------------------------------------------------------------------------------

*Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

[Resources](/design/human-interface-guidelines/eyes#Resources)
--------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/eyes#Related)

[Focus and selection](/design/human-interface-guidelines/focus-and-selection)


[Immersive experiences](/design/human-interface-guidelines/immersive-experiences)


[Gestures](/design/human-interface-guidelines/gestures)


[Spatial layout](/design/human-interface-guidelines/spatial-layout)


#### [Developer documentation](/design/human-interface-guidelines/eyes#Developer-documentation)

[Adopting best practices for privacy and user preferences](/documentation/visionOS/adopting-best-practices-for-privacy)


#### [Videos](/design/human-interface-guidelines/eyes#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_1x.jpg) Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/2C47B638-090D-4CBB-9E9E-EBE8114536D9/8132_wide_250x141_1x.jpg) Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) 
[Change log](/design/human-interface-guidelines/eyes#Change-log)
----------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | New page. |


June 21, 2023

 Updated to include guidance for visionOS. Motion
======

In all platforms, beautiful, fluid motions bring the interface to life, conveying status, providing feedback and instruction, and enriching the visual experience.![A sketch of three overlapping diamonds, suggesting the movement of an element from left to right. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/1a0efd7807cfcba7a5821be86b20bafc/foundations-motion-intro@2x.png)

Many system components automatically include motion, letting you offer familiar and consistent experiences throughout your app or game. If you design custom motion, prefer intentional animations that keep people oriented and comfortable, provide clear feedback in response to their actions, and help them learn your interface without getting overwhelmed.

[Best practices](/design/human-interface-guidelines/motion#Best-practices)
--------------------------------------------------------------------------

**Use subtle motion to communicate.** Motion can be a great way to enhance feedback and understanding by showing how things change, what will happen when people perform an action, and what they can do next. For example, when people minimize a window in macOS, it moves smoothly from the desktop to the Dock so they know exactly where it went; when people set up Face ID, the system briefly describes what they need to do and helps them during scanning by visually changing the tick marks encircling their face; in visionOS, window controls expand gently when people bring focus to them.

**Add motion purposefully, supporting the experience without overshadowing it.** Don’t add motion for the sake of adding motion. Gratuitous or excessive animation can distract people and may make them feel disconnected or physically uncomfortable.

**Make motion optional.** There are several reasons why people might not experience movement in your app, so it’s essential to avoid using it as the only way to communicate important information. For example, people can turn on the Reduce Motion accessibility setting to minimize or eliminate animations. For guidance, see [Motion](/design/human-interface-guidelines/accessibility#Motion)
.

**Strive for realism and credibility.** In non game apps, accurate, realistic motion can help people understand how something works, but motion that doesn’t make sense — or appears to defy physical laws — can make them feel disoriented. For example, if someone reveals a view by sliding it down from the top, they don’t expect to dismiss the view by sliding it to the side.

**Prefer brief, precise animations.** Animations that combine brevity and precision tend to feel more lightweight and less intrusive, and often convey information more effectively. For example, when people tap the list button in Weather on iPhone, the fullscreen view of the current city quickly transitions to the list view, pinpointing the city’s location in the list. In visionOS, when people tap a panorama in Photos, the view smoothly expands to fill the space in front of them, helping them visually track the transition.

**In general, avoid adding motion to interactions that occur frequently.** The system already provides subtle animations for interactions with standard interface elements. Avoid making people spend extra time paying attention to unnecessary motion every time they interact with your content.

**Consider using animated symbols where it makes sense.** When you use SF Symbols 5 or later, you can apply animations to SF Symbols or custom symbols. For guidance, see [Animations](/design/human-interface-guidelines/sf-symbols#Animations)
.

[Platform considerations](/design/human-interface-guidelines/motion#Platform-considerations)
--------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*

### [visionOS](/design/human-interface-guidelines/motion#visionOS)

In visionOS, motion can subtly communicate context, draw attention to information, and enrich immersive experiences. Combined with [depth](/design/human-interface-guidelines/spatial-layout#Depth)
, motion also provides essential feedback when people bring [focus](/design/human-interface-guidelines/focus-and-selection)
 to elements. It’s crucial to use motion in ways that people appreciate without causing distraction, confusion, or discomfort.

While wearing Apple Vision Pro, people use [passthrough](/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough)
 to view their physical surroundings while they interact with virtual content. Because both the surroundings and app content can be visible at the same time, people can be uncomfortable if the movement of virtual content makes them feel like they or their surroundings are moving instead. In general, the larger a moving virtual object is, the harder it can be to maintain the feeling of stability.

**Help people remain comfortable when showing the movement of large virtual objects.** If an object is large enough to fill a lot of the [field of view](/design/human-interface-guidelines/spatial-layout#Field-of-view)
, occluding most or all of passthrough, people can naturally perceive it as being part of their surroundings. To help people perceive the object’s movement without making them think that they or their surroundings are moving, you can increase the object’s translucency, helping people see through it, or lower its contrast to make its motion less noticeable. If you need to show a transition between large objects, consider using a fade or an effect that brings content in and out of focus to minimize potential disorientation.

Note

People can experience discomfort even when they’re the ones moving a large virtual object, such as a window. Although adjusting translucency and contrast can help in this scenario, too, consider keeping a window’s size fairly small.

**Be mindful of displaying moving content that occupies most of a window.** In this scenario, people can sometimes perceive the window’s content as being the world around them and the movement as being their own. If you need to display moving content in a window, consider restricting the size of the window or the content area so people can continue to see their surroundings. If you create the motion shown in the window, prefer maintaining a horizontal horizon, keeping the speed low, and avoiding sudden or unexpected camera movements. You might also want to use low-contrast textures, which can make motion less perceptible.

**Be gentle with rotational motions.** When you rotate the virtual world, either by rotating the camera, or by rotating large virtual objects around someone, the rotation can upset the person’s sense of stability, especially when the rotation is fast or lasts too long. Instead, consider using instantaneous directional changes during a quick fade-out.

**Avoid showing objects that oscillate in a sustained way.** In particular, you want to avoid showing an oscillation that has a frequency of around 0.2Hz because people can be very sensitive to this frequency. If you need to show objects oscillating, aim to keep the amplitude low and consider making the content translucent.

**Eliminate unnecessary motion.** Because people look at the object they want to interact with, displaying motion where it might cause them to look away can be frustrating. Prefer using motion only when you need to encourage people to look at something important.

**As much as possible, avoid displaying motion at the edges of a person’s field of view.** People can be particularly sensitive to motion that occurs in their peripheral vision. In addition to being distracting, peripheral motion can even cause discomfort because it can make people feel like they or their surroundings are moving.

**Consider giving people a stationary frame of reference.** It can be easier for people to handle visual movement when it’s contained within an area that doesn’t move. In contrast, people can feel unwell when it appears that everything around them is moving.

**Avoid encouraging people to move their head while they’re experiencing visual rotation.** When virtual objects appear to rotate around them, people typically need to keep their eyes in a consistent direction to avoid feeling unwell.

**Consider using fades when you need to relocate an object.** When an object moves from one location to another, people naturally watch the movement. If such movement doesn’t communicate anything useful to people, you can fade the object out before moving it and fade it back in after it’s in the new location.

### [watchOS](/design/human-interface-guidelines/motion#watchOS)

SwiftUI provides a powerful and streamlined way to add motion to your app. If you need to use WatchKit to animate layout and appearance changes — or create animated image sequences — see [`WKInterfaceImage`](/documentation/watchkit/wkinterfaceimage#1652345)
.

Note

All layout- and appearance-based animations automatically include built-in easing that plays at the start and end of the animation. You can’t turn off or customize easing.

[Resources](/design/human-interface-guidelines/motion#Resources)
----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/motion#Related)

[Feedback](/design/human-interface-guidelines/feedback)


[Accessibility](https://www.apple.com/accessibility/)


[Spatial layout](/design/human-interface-guidelines/spatial-layout)


[Immersive experiences](/design/human-interface-guidelines/immersive-experiences)


#### [Developer documentation](/design/human-interface-guidelines/motion#Developer-documentation)

[Animating Views and Transitions](/tutorials/SwiftUI/animating-views-and-transitions)


#### [Videos](/design/human-interface-guidelines/motion#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/2C47B638-090D-4CBB-9E9E-EBE8114536D9/8132_wide_250x141_1x.jpg) Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/42/E55D60D2-C7D7-4F96-9A9D-8AF4C7D6BB49/2247_wide_250x141_1x.jpg) Designing Fluid Interfaces](https://developer.apple.com/videos/play/wwdc2018/803) 
[Change log](/design/human-interface-guidelines/motion#Change-log)
------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |


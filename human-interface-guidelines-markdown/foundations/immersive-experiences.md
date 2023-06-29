New page. Immersive experiences
=====================

In visionOS, you can design apps and games that extend beyond windows and volumes, and let people immerse themselves in your content.![A sketch that suggests Apple Vision Pro. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/9f31df1cc933713456a4fc39a37ea68a/foundations-immersive-experiences-intro@2x.png)

In visionOS, people can run multiple apps at the same time in the *Shared Space* or concentrate on a single app at a time in a *Full Space*. By default, your app launches in the Shared Space, where people can switch between multiple running apps much as they do on a Mac. When they want a more immersive experience, people can transition your app to a Full Space, where other apps hide and your app can display content anywhere.

[Immersion and passthrough](/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough)
---------------------------------------------------------------------------------------------------------------

visionOS supports a spectrum of immersion that helps you give people several ways to experience your app or game. Throughout this spectrum, the visibility of people’s physical surroundings plays a key role in the immersiveness of the experience.

 [Play](#) 
While wearing Apple Vision Pro, people can see their physical surroundings using *passthrough*, which provides real-time video from the device’s external cameras.

To change how much of their surroundings they see, people use the [Digital Crown](/design/human-interface-guidelines/digital-crown)
 to adjust the amount of passthrough. For example, people might increase passthrough when they want to interact with a nearby physical object or read text on another device, or they might decrease passthrough when they want to bring up an Environment.

 [Play](#) 
Important

Your app doesn’t receive direct information about the current level of passthrough or when it changes, which means that you don’t know how well a person can see their surroundings.

Consider the following techniques for immersing people in your experience and helping them engage with your content.

* **Dim passthrough while in the Shared Space.** You can ask the system to subtly dim passthrough and other visible content to minimize distractions and highlight a specific window or volume, without hiding other apps. For developer guidance, see [`SurroundingsEffect`](/documentation/SwiftUI/SurroundingsEffect)
.
* **Display 3D content in a Full Space.** When your app transitions to a Full Space, you can display 3D content that isn’t bound by a window, in addition to content in standard windows and volumes. For developer guidance, see [`automatic`](/documentation/SwiftUI/ImmersionStyle/automatic)
.
* **Integrate with someone’s surroundings.** When running in a Full Space, your app can also request access to information about nearby physical objects and room layout, helping you display virtual content that blends with people’s surroundings. For developer guidance, see [`mixed`](/documentation/SwiftUI/ImmersionStyle/mixed)
 and [ARKit](/documentation/arkit)
.
* **Create a portal.** An app running in a Full Space can use a portal to offer a more immersive experience that doesn’t completely remove people from their surroundings. When a portal opens, people get a roughly 180-degree view into your immersive content, and they can use the Digital Crown to adjust the size of the portal. For developer guidance, see [`progressive`](/documentation/SwiftUI/ImmersionStyle/progressive)
.
* **Create a fully immersive experience.** To provide a fully immersive experience, an app running in a Full Space can ask the system to hide passthrough while it displays content that completely surrounds people, transporting them to a new place. For developer guidance, see [`full`](/documentation/SwiftUI/ImmersionStyle/full)
.

visionOS implements the following behaviors while people use apps.

* If a person moves more than about a meter, the system automatically makes all displayed content translucent to help them navigate their surroundings.
* When a fully immersive experience starts, the system defines an invisible zone that extends 1.5 meters from the initial position of the wearer’s head. If their head moves outside of that zone, the experience automatically stops and passthrough returns to help people avoid colliding with objects in their physical surroundings.
* The system can stop an immersive experience when people get too close to a physical object or when they move too quickly.

[Best practices](/design/human-interface-guidelines/immersive-experiences#Best-practices)
-----------------------------------------------------------------------------------------

**Offer multiple ways to use your app.** In addition to giving people the freedom to choose their experiences, it’s essential to design your app to support the accessibility features people use to personalize the ways they interact with their devices. For guidance, see [Accessibility](/design/human-interface-guidelines/accessibility)
.

**Reserve immersion for meaningful moments and content.** Not every task benefits from immersion, and not every immersive task needs to be fully immersive. Although people sometimes want to enter a different world, they often want to stay grounded in their surroundings while they’re using your app, and they can appreciate being able to use other apps and system features at the same time. Instead of assuming that your app needs to be fully immersive most of the time, design ways for people to immerse themselves in the individual tasks and content that make your app unique. For example, people can browse their albums in Photos using a familiar app window in the Shared Space, but when they want to examine a single photo, they can temporarily transition to a more immersive experience in a Full Space where they can expand the photo and appreciate its details.

**Help people engage with key moments in your app, regardless of the level of immersion.** Cues like dimming, [motion](/design/human-interface-guidelines/motion)
, [scale](/design/human-interface-guidelines/spatial-layout#Scale)
, and [Spatial Audio](/design/human-interface-guidelines/playing-audio#visionOS)
 can help draw people’s attention to a specific area of content, whether it’s in a window in the Shared Space or a completely immersive experience in a Full Space. Start with subtle cues that gently guide people’s attention, strengthening the cues only if it makes sense in your app.

**Prefer letting people choose when to enter a more immersive experience.** You don’t want to move people into a more immersive experience without their consent, and you don’t want to overwhelm them by unexpectedly displaying large windows or objects. Instead, provide clear entry and exit controls so people can decide when to be more immersed in your content.

**Design smooth, predictable transitions between experiences.** Help people prepare for different experiences by providing gentle transitions that let people visually track changes. Avoid sudden, jarring transitions that might be disorienting or uncomfortable.

**Make it easy for people to exit an immersive experience.** For example, Keynote provides a prominent Exit button to help people leave the Theater experience and return to the slide-viewing window. Make sure your button clarifies whether it returns people to a previous, less immersive context or quits an experience like a game. If exiting your immersive experience also quits your app, consider providing controls that let people pause or return to a place where they can save their progress before quitting.

**Avoid encouraging people to move while they’re in a fully immersive experience.** In a completely immersive experience, the system hides passthrough, and people might lose track of their surroundings while they’re engaged with your content. It’s critical to encourage people to remain safe and comfortable while they use your app. One way to help people stay in one place is to bring your content to them instead of expecting them to move toward the content.

**Adopt ARKit if you want to blend app content with someone’s surroundings.** For example, you might want to integrate virtual content into someone’s surroundings or use the wearer’s hand positions to inform your experience. If you need access to these types of sensitive data, you must request people’s permission. For guidance, see [Privacy](/design/human-interface-guidelines/privacy)
; for developer guidance, see [`SceneReconstructionProvider`](/documentation/arkit/scenereconstructionprovider)
.

**In an app that lets people blend virtual objects with their surroundings, help them avoid completely obscuring passthrough.** People often use the presence of passthrough to decide whether to move carefully in their surroundings. If people can place virtual objects in ways that prevent them from seeing nearby physical objects, they might not realize that moving in their surroundings could be difficult. To help people avoid this situation, you need to use the correct APIs to implement your immersive experience, so the system can respond appropriately if people move. For developer guidance, see [`ImmersionStyle`](/documentation/SwiftUI/ImmersionStyle)
.

**Be mindful of people’s visual comfort.** For example, although you can place 3D content anywhere while your app is running in a Full Space, prefer placing it within people’s [field of view](/design/human-interface-guidelines/spatial-layout#Field-of-view)
. Also make sure you display motion in comfortable ways while your app runs in a Full Space because people may not have the same frame of reference they’re used to. For guidance, see [Motion](/design/human-interface-guidelines/motion)
.

[Platform considerations](/design/human-interface-guidelines/immersive-experiences#Platform-considerations)
-----------------------------------------------------------------------------------------------------------

*Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

[Resources](/design/human-interface-guidelines/immersive-experiences#Resources)
-------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/immersive-experiences#Related)

[Spatial layout](/design/human-interface-guidelines/spatial-layout)


[Motion](/design/human-interface-guidelines/motion)


#### [Developer documentation](/design/human-interface-guidelines/immersive-experiences#Developer-documentation)

[Creating fully immersive experiences in your app](/documentation/visionOS/creating-fully-immersive-experiences)


[Incorporating real-world surroundings in an immersive experience](/documentation/visionOS/incorporating-surroundings-in-an-immersive-experience)


[Immersive spaces](/documentation/SwiftUI/Immersive-spaces)


#### [Videos](/design/human-interface-guidelines/immersive-experiences#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/FAD92809-C8B7-4968-802C-C662B1AF6C94/8340_wide_250x141_1x.jpg) Explore immersive sound design](https://developer.apple.com/videos/play/wwdc2023/10271) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/942191E7-9B98-487D-AE81-400D58285B31/8129_wide_250x141_1x.jpg) Design spatial SharePlay experiences](https://developer.apple.com/videos/play/wwdc2023/10075) 
[Change log](/design/human-interface-guidelines/immersive-experiences#Change-log)
---------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | New page. |


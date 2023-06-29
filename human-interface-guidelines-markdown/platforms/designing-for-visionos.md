Designing for visionOS
=========================

When people wear Apple Vision Pro, they enter an infinite 3D space where they can engage with your app or game while staying connected to their surroundings.  
![A stylized representation of Apple Vision Pro shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/df20c2f5927e27ce269d973c6adb3b43/platforms-visionOS-intro@2x.png)

As you begin designing your app or game for visionOS, start by understanding the fundamental device characteristics and patterns that distinguish the platform. Use these characteristics and patterns to inform your design decisions and help you create immersive and engaging experiences.  


**Space.** Apple Vision Pro offers a limitless canvas where people can view virtual content like   
[windows](/design/human-interface-guidelines/windows)
,   
[volumes](/design/human-interface-guidelines/windows#Volumes)
, and 3D objects, and choose to enter deeply immersive experiences that can transport them to different places.  


**Immersion.** In a visionOS app, people can fluidly transition between different levels of   
[immersion](/design/human-interface-guidelines/immersive-experiences)
. By default, an app launches in the   
*Shared Space* where multiple apps can run side-by-side and people can open, close, and relocate windows. People can also choose to transition an app to a   
*Full Space*, where it’s the only app running. While in a Full Space app, people can view 3D content blended with their surroundings, open a portal to view another place, or enter a different world.  


**Passthrough.**   
[Passthrough](/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough)
 provides live video from the device’s external cameras, and helps people interact with virtual content while also seeing their actual surroundings. When people want to see more or less of their surroundings, they use the   
[Digital Crown](/design/human-interface-guidelines/digital-crown)
 to control the amount of passthrough.  


**Spatial Audio.** Vision Pro combines acoustic and visual-sensing technologies to model the sonic characteristics of a person’s surroundings, automatically making audio sound natural in their space. When an app receives a person’s permission to access information about their surroundings, it can fine-tune   
[Spatial Audio](/design/human-interface-guidelines/playing-audio#visionOS)
 to bring custom experiences to life.  


**Focus and gestures.** In general, people interact with Vision Pro using their   
[eyes](/design/human-interface-guidelines/eyes)
 and   
[hands](/design/human-interface-guidelines/gestures#visionOS)
. People perform most actions by looking at a virtual object to bring   
[focus](/design/human-interface-guidelines/focus-and-selection)
 to it and making an   
*indirect gesture*, like a tap, to activate it. People can also use a   
*direct gesture* to interact with a virtual object by touching it with a finger.  


**Ergonomics.** While wearing Vision Pro, people rely entirely on the device’s cameras for everything they see, both real and virtual, so maintaining visual comfort is paramount. The system helps maintain comfort by automatically placing content so it’s relative to the wearer’s head, regardless of the person’s height or whether they’re sitting, standing, or lying down. Because visionOS brings content to people — instead of making people move to reach the content — people can remain at rest while engaging with apps and games.  


**Accessibility.** Apple Vision Pro supports   
[accessibility](/design/human-interface-guidelines/accessibility)
 technologies like VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer, and many more, so people can use the interactions that work for them. In visionOS, as in all platforms, system-provided UI components build in accessibility support by default, while system frameworks give you ways to enhance the accessibility of your app or game.  


[Best practices](/design/human-interface-guidelines/designing-for-visionos#Best-practices)
------------------------------------------------------------------------------------------

Great visionOS apps and games are approachable and familiar, while offering extraordinary experiences that can surround people with beautiful content, expanded capabilities, and captivating adventures.  


**Embrace the unique features of Apple Vision Pro.** Take advantage of space, Spatial Audio, and immersion to bring life to your experiences, while integrating passthrough, focus, and gestures in ways that feel at home on the device.  


**Consider the entire spectrum of immersion as you design ways to present your app’s most distinctive moments.** You can present experiences in a windowed, UI-centric context, a fully immersive context, or something in between. For each key moment in your app, find the minimum level of immersion that suits it best — don’t assume that every moment needs to be fully immersive.  


**Use windows for contained, UI-centric experiences.** To help people perform standard tasks, prefer standard   
[windows](/design/human-interface-guidelines/windows#visionOS)
 that appear as planes in space and contain familiar controls. In visionOS, people can relocate windows anywhere they want, and the system’s   
[dynamic scaling](/design/human-interface-guidelines/spatial-layout#Scale)
 helps keep window content legible whether it’s near or far.  


**Prioritize comfort.** To help people stay comfortable and physically relaxed as they interact with your app or game, keep the following fundamentals in mind.  


* Display content within a person’s   
[field of view](/design/human-interface-guidelines/spatial-layout#Field-of-view)
, positioning it relative to their head. Avoid placing content in places where people have to turn their head or change their position to interact with it.
* Avoid displaying   
[motion](/design/human-interface-guidelines/motion#visionOS)
 that’s overwhelming, jarring, too fast, or missing a stationary frame of reference.
* Support   
[indirect gestures](/design/human-interface-guidelines/gestures#visionOS)
 that let people interact with apps while their hands rest in their lap or at their sides.
* If you support direct gestures, make sure the interactive content isn’t too far away and that people don’t need to interact with it for extended periods.
* Avoid encouraging people to move too much while they’re in a fully   
[immersive experience](/design/human-interface-guidelines/immersive-experiences)
.

**Help people share activities with others.** When you use   
[SharePlay](/design/human-interface-guidelines/shareplay#visionOS)
 to support shared activities, people can view the   
*Spatial Personas* of other participants, making it feel like everyone is together in the same space.  


[Resources](/design/human-interface-guidelines/designing-for-visionos#Resources)
--------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/designing-for-visionos#Related)

[Apple Design Resources](https://developer.apple.com/design/resources/#visionOS-apps)


#### [Developer documentation](/design/human-interface-guidelines/designing-for-visionos#Developer-documentation)

[Creating your first visionOS app](/documentation/visionOS/creating-your-first-visionos-app)


#### [Videos](/design/human-interface-guidelines/designing-for-visionos#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072)
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_1x.jpg) Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073)
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076)
[Change log](/design/human-interface-guidelines/designing-for-visionos#Change-log)
----------------------------------------------------------------------------------
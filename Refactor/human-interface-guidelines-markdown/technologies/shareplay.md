June 21, 2023

 Updated to include guidance for visionOS. SharePlay
=========

SharePlay helps multiple people share activities — like viewing a movie, listening to music, playing a game, or sketching ideas on a whiteboard — while they’re in a FaceTime call or Messages conversation.![A sketch of the SharePlay icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/cd055a691d877485d819f837a6eb15a7/technologies-Share-Play-intro@2x.png)

The system synchronizes app playback on all participating devices to support seamless media and content sharing that lets everyone enjoy the experience simultaneously. In visionOS, SharePlay helps people enjoy these experiences while they’re together in the same virtual space.

When someone shares content during a FaceTime call, the system asks each participant to launch the app to begin the experience. If people don’t have the app installed, the SharePlay alert encourages them to download it from the App Store. If you make the platform-specific versions of your app available as a [Universal Purchase](https://developer.apple.com/support/universal-purchase/)
, people can make one purchase and use your app and their in-app purchases across all the platforms you support.

[Best practices](/design/human-interface-guidelines/shareplay#Best-practices)
-----------------------------------------------------------------------------

**Let people know that you support SharePlay.** People often expect media playback experiences to be shareable, so indicate this capability in your interface. For example, you can use the `shareplay` SF Symbol to identify the content or experiences in your app that support SharePlay.

**If part of your app requires a subscription, consider ways to help nonsubscriber participants quickly join a group activity.** For example, you might offer temporary or provisional access to nonsubscribers or let an existing subscriber send a one-time pass to a friend. To make it easy for family members to share your content in a SharePlay experience, you can support [Family Sharing](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase#Supporting-Family-Sharing)
. If people can start a subscription during a SharePlay experience, present a streamlined version of your sign-up flow so they can join the activity without making others wait. For guidance, see [Autorenewable subscriptions](/design/human-interface-guidelines/in-app-purchase#Autorenewable-subscriptions)
.

**Support Picture in Picture (PiP) when possible.** On iPhone and iPad, people can open a shared video in a PiP window. On a Mac, a shared video opens in a background window that people can move into the foreground when they want to watch.

**Use the term *SharePlay* correctly.** You can use *SharePlay* as a noun — as in “Join SharePlay” — and also as a verb when describing a direct action in your interface. For example, in a button or sheet that lets people share a movie-viewing activity, you can use a phrase like “SharePlay Movie.” Avoid using an adjective with SharePlay; for example, in your visionOS app, don’t add terms like *virtual* or *spatial*. Avoid changing the term *SharePlay* in any way; for example, don’t use variations like *SharePlayed*, *SharePlays*, or *SharePlaying*.

[Sharing activities](/design/human-interface-guidelines/shareplay#Sharing-activities)
-------------------------------------------------------------------------------------

An *activity* is an app-defined type of shareable experience. For example, an app that lets people view videos might define a separate activity for viewing each type of content — like movies, TV shows, and uploaded videos — and display a different description for each activity. You can define as many different activities as make sense in your app. For developer guidance, see [Inviting Participants to Share an Activity](/documentation/GroupActivities/inviting-participants-to-share-an-activity)
.

**Briefly describe each activity.** When people receive an invitation to participate in an activity, your description helps them understand the experience they’re about to share. For example, a video-viewing app might associate its descriptive movie view with a movie-viewing activity. In this case, the descriptive view might display a movie’s title, a plot summary, and a poster image. Write a simple, meaningful description that’s short enough to avoid truncation.

**Make it easy to start sharing an activity.** If there’s no session available when people start a shareable activity, you can present UI that lets them start a group activity. In response, the system asks people if they want to share or continue the experience solo.

![An illustration that represents the TV app on iPhone. The screen shows a video above text. The SharePlay icon appears inline with some of the text. The top of the screen includes a 'Back' button, a banner that reads 'Choose Content to Use SharePlay', and a 'Share' button.](https://docs-assets.developer.apple.com/published/fc9ea8247d44a000c4740b41e345666d/shareplay-1@2x.png)

![An illustration that represents the TV app on iPhone. The screen shows an alert overlaid on a video and text. The alert includes buttons titled 'SharePlay', 'Start Only for Me', and 'Cancel'.](https://docs-assets.developer.apple.com/published/8303dab81c8408c4e582f230a3128923/shareplay-2@2x.png)

**Help people prepare to join a session before displaying the activity.** For example, if people must log in, download content, or make a payment before they can participate, display views that help them perform these tasks before showing the activity UI. Make these tasks as simple and effortless as possible so people can join the group activity quickly.

**When possible, defer app tasks that might delay a shared activity.** For example, if your app needs to know a participant’s profile, consider asking for this information at a convenient time, like when playback pauses or finishes.

[Platform considerations](/design/human-interface-guidelines/shareplay#Platform-considerations)
-----------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.*

### [visionOS](/design/human-interface-guidelines/shareplay#visionOS)

People expect most visionOS apps to support SharePlay. While wearing Apple Vision Pro, people choose the Spatial option in FaceTime to share content and activities with others.

In a shared activity, FaceTime can show representations of other participants — called Spatial Personas — within each wearer’s space, making everyone feel like they’re sharing the same experience in the same place. During a shared experience in FaceTime, people can interact with each other in natural ways through their Spatial Personas. For example, people can speak or gesture directly to others, tell when someone is paying attention to them, and know which person is using a shared tool or resource.

visionOS uses the concept of *shared context* to describe the characteristics of a shared activity that help people feel physically present with others while connecting over the same content. A shared context helps give people confidence that they’re experiencing the same thing as everyone else.

When people feel that they’re truly sharing an experience, social dynamics can encourage authentic, intuitive interactions. For example, people can communicate verbally and nonverbally to make plans, take turns, and share resources.

Note

During a shared activity, the system helps preserve people’s privacy by obscuring some visual details about wearers. In addition, a person can adjust their Spatial Persona if they want. Although the system can place Spatial Personas shoulder to shoulder and it supports shared gestures like a handshake or “high five,” Spatial Personas remain apart.

**Choose the Spatial Persona template that suits your shared activity.** When you design a shared activity, you can use a Spatial Persona template to specify a layout for arranging Spatial Personas in the shared activity space. The system provides three Spatial Persona templates: side-by-side, surround, and conversational.

The side-by-side template places participants next to each other along a curved line segment, all facing the shared content. The side-by-side template gives everyone a great view of the content, making it a good choice for helping people watch media together. Because people aren’t facing each other in this arrangement, the side-by-side template can encourage less nonverbal interaction than other Spatial Persona templates.

![An illustration representing a side-by-side shared activity in visionOS. Participants are positioned next to one another and facing a shared screen.](https://docs-assets.developer.apple.com/published/72343469eb001f3e3e55af56c7a87f2e/visionos-shareplay-side-by-side@2x.png)

The system-applied surround template arranges participants all the way around the shared content in the center. This Spatial Persona template works especially well when the content is 3D, because each participant views it from a different angle. In the surround template, participants face each other as if they were grouped around a table, promoting both verbal and nonverbal interactions.

![An illustration representing a surround shared activity in visionOS. Participants are gathered in a circle around shared content.](https://docs-assets.developer.apple.com/published/ec3334ce0617ce3a41cdb53ea14527a8/visionos-shareplay-surround@2x.png)

The conversational template also groups participants around a center point, but places your content along the circle, not at its center. Because of this position, not everyone has the same view of your content, and it might not be convenient for everyone to interact with it. Consider using the conversational arrangement if your experience is more about people being together while your app performs a task in the background like playing music.

![An illustration representing a conversational shared activity in visionOS. Participants are positioned in a semi-circle formation around shared content.](https://docs-assets.developer.apple.com/published/6c5ce8c1e229e1cda5b90cc024ede5d6/visionos-shareplay-conversational@2x.png)

For developer guidance, see [`SystemCoordinator`](/documentation/GroupActivities/SystemCoordinator)
 and [`SpatialTemplatePreference`](/documentation/GroupActivities/SpatialTemplatePreference)
.

**Be prepared to launch directly into your shared activity.** When one person shares your activity with others on a FaceTime call, the system minimizes friction by automatically launching your app for everyone. In this scenario, you want to avoid displaying any windows that aren’t related to the shared activity. For example, if people need to sign in before joining the activity, be sure to present this task in an autodismissible window that disappears as soon as people finish providing the required input.

**Help people enter a shared activity together, but don’t force them.** When one participant changes their level of immersion, the system tells you so you can synchronize the experience for everyone. Before synchronizing, check whether changing a person’s level of immersion would disrupt their current task; if it would, offer them the choice to join the updated experience. For example, if someone is editing content in an unshared window, you might present an alert that lets them choose to transition. For guidance, see [Immersive experiences](/design/human-interface-guidelines/immersive-experiences)
.

**Smoothly update a shared activity when new participants join.** When someone joins an in-progress activity, you need to integrate them without disrupting the experience for everyone else. For example, it’s important to update shared immersive content to keep all participants synchronized. Also, consider designing ways to accommodate up to five participants in your arrangement, updating their positions as necessary.

#### [Maintaining a shared context](/design/human-interface-guidelines/shareplay#Maintaining-a-shared-context)

When your shared activity runs in a Full Space, the system helps your app maintain a shared context by using a single coordinate system to arrange your content and all participants, automatically synchronizing the size, position, and orientation of your app for each person. You’re responsible for displaying objects, playing sounds, and supporting interactions in ways that enhance the feeling of sharing the experience.

**Make sure everyone views the same state of your app.** If your app has more than one state — such as a media app that provides both minimal and theater-like viewing modes — you need to avoid letting different participants view different states, because doing so can diminish people’s sense of being together in a shared space. The exception to this is when someone needs to temporarily exit a shared activity; for guidance, see [Adjusting a shared context](/design/human-interface-guidelines/shareplay#Adjusting-a-shared-context)
.

**Use Spatial Audio to enrich your shared activity.** Playing Spatial Audio can help you strengthen the realism of the shared experience. For guidance, see [Playing audio](/design/human-interface-guidelines/playing-audio)
.

**When possible, let people discover natural, social solutions to confusions or conflicts that might arise during a shared experience.** For example, if only one participant at a time can use a virtual tool, avoid displaying UI, like tool-use controls or notifications, and instead let people speak or gesture to the group when they want to use the tool. If conflicts can arise during your shared activity — for example, if multiple people try to change the same content at the same time — consider implementing a simple rule, like last change wins, and letting people use the rule to define behavior that’s acceptable to the group.

**Help people keep their private and shared content separate.** By default, the system clearly differentiates a shared window from windows that aren’t shared. For example, when people use Music to listen together, the shared Music window appears as a new window for everyone, while any individual’s open library window remains separate and unshared. If your app can open multiple windows, help people share the one they want and make it easy for them to distinguish shared from unshared windows. If possible, also let people drag content they want to share from a private window to a shared one.

#### [Adjusting a shared context](/design/human-interface-guidelines/shareplay#Adjusting-a-shared-context)

Sometimes, it makes sense to adjust the shared context of a shared activity so each participant can customize their experience, such as for comfort or accessibility. In other situations, strictly maintaining a shared context might decrease people’s enjoyment of the experience. For example, when content has only one ideal viewing angle, each participant might need their own.

**Let people personalize their experience without changing the experience for others.** For example, people might need to adjust various settings, like volume or subtitles, to make views and interactions accessible or make themselves more comfortable.

**Consider when to give each participant a unique view of the shared content.** Some content looks best when people view it from a specific perspective. For example, people can share a Spatial Capture in a standard window with other people’s Spatial Personas visible around it. However, to perceive the depth in a Spatial Capture, each person needs to view it from the right angle. In this scenario, a person could temporarily transition to a Full Space that hides other participants and ensures the right viewing angle for them, even while everyone else continues to view the standard window and each other. If it makes sense to provide per-person versions of your shared content, be sure to continue synchronizing people’s positions and your app context to maintain the shared experience.

**Make it easy for people to exit and rejoin a shared activity.** Sometimes, people need to perform an unrelated task in your app or a different one, or engage with their physical surroundings. When this happens, you need to present a control or other component that lets people quickly rejoin the shared activity. In addition, you might want to continue displaying the shared content so people can stay informed about the ongoing shared experience while they’re hiding their Spatial Persona.

[Resources](/design/human-interface-guidelines/shareplay#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/shareplay#Related)

[Autorenewable subscriptions](/design/human-interface-guidelines/in-app-purchase#Autorenewable-subscriptions)


#### [Developer documentation](/design/human-interface-guidelines/shareplay#Developer-documentation)

[GroupActivities](/documentation/GroupActivities)


#### [Videos](/design/human-interface-guidelines/shareplay#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/942191E7-9B98-487D-AE81-400D58285B31/8129_wide_250x141_1x.jpg) Design spatial SharePlay experiences](https://developer.apple.com/videos/play/wwdc2023/10075) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/C2B0FC1B-CEFF-44CE-8689-F987ED3779F7/5095_wide_250x141_1x.jpg) Design for Group Activities](https://developer.apple.com/videos/play/wwdc2021/10184) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/C1BB30E0-B95E-4B6F-90E7-DD9447FC8923/5098_wide_250x141_1x.jpg) Build custom experiences with Group Activities](https://developer.apple.com/videos/play/wwdc2021/10187) 
[Change log](/design/human-interface-guidelines/shareplay#Change-log)
---------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| December 19, 2022 | Clarified guidance for helping nonsubscribers join a group activity. |


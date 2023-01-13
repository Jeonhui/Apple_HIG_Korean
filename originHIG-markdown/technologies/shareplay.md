# **[technologies] shareplay**

# SharePlay helps multiple people share activities — like viewing movies and listening to music — while they’re in a FaceTime call or Messages conversation.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Share-Play-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Share-Play-intro_2x.png)

The system synchronizes app playback on all participating devices to enable seamless media sharing so everyone can enjoy the experience simultaneously.

**Let people know that you support SharePlay.** People often expect media playback experiences to be shareable, so indicate this capability in your UI. For example, you can use the `shareplay` SF Symbol to identify the content or experiences in your app that support SharePlay.

Offer [Universal Purchase](https://developer.apple.com/support/universal-purchase/) to support SharePlay experiences among people running your app on different platforms. While sharing media during a FaceTime call, each participant views the content within your app running on their device. If a participant doesn’t have your app installed, SharePlay can help them download it from the App Store.

# **Sharing activities**

An *activity* is an app-defined type of shareable experience. For example, an app that lets people view videos might define a separate activity for viewing each type of content — like movies, TV shows, and uploaded videos — and display a different description for each activity. You can define as many different activities as make sense in your app. For developer guidance, see [Inviting participants to share an activity](https://developer.apple.com/documentation/groupactivities/inviting-participants-to-share-an-activity).

**Briefly describe each activity.** When people receive an invitation to participate in an activity, your description helps them understand the experience they’re about to share. For example, a video-viewing app might associate its descriptive movie view with a movie-viewing activity. In this case, the descriptive view might display a movie’s title, a plot summary, and a poster image. Write a simple, meaningful description that’s short enough to avoid truncation.

**Make it easy to start sharing an activity.** If there’s no session available when people start a shareable activity, you can present UI that lets them start a group activity. In response, the system asks people if they want to share or continue the experience solo.

![https://developer.apple.com/design/human-interface-guidelines/technologies/shareplay/images/shareplay_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/shareplay/images/shareplay_2x.png)

**Help people prepare to join a session before displaying the activity.** For example, if people must log in, download content, or make a payment before they can participate, display views that help them perform these tasks before showing the activity UI. Make these tasks as simple and effortless as possible so people can join the group activity quickly.

**If part of your app requires a subscription, consider ways to help nonsubscriber participants quickly join a group activity.** For example, you might offer temporary or provisional access to nonsubscribers or let an existing subscriber send a one-time pass to a friend. To make it easy for family members to share your content in a SharePlay experience, you can support [Family Sharing](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#enabling-family-sharing). If people can start a subscription during a SharePlay experience, present a streamlined version of your sign-up flow so they can join the activity without making others wait. For guidance, see [Auto-renewable subscriptions](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#auto-renewable-subscriptions).

**When possible, defer app tasks that might delay a shared activity.** For example, if your app needs to know a participant’s profile, consider asking for this information at a convenient time, like when playback pauses or finishes.

**Use the term *SharePlay* correctly.** You can use *SharePlay* as a noun — as in "Join SharePlay" — and also as a verb when describing a direct action in your UI. For example, in a button or sheet that lets people share a movie-viewing activity, you can use a phrase like "SharePlay Movie." Avoid changing the term *SharePlay* in any way; for example, don’t use variations like *SharePlayed*, *SharePlays*, or *SharePlaying*.

**Support Picture in Picture (PiP) when possible.** On iPhone and iPad, people can open a shared video in a PiP window. On a Mac, a shared video opens in a background window that people can move into the foreground when they want to watch.
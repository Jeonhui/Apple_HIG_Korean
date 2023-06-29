# **[technologies-homekit] custom-functionality**

Your app is a great place to help people appreciate the unique functionality of your accessory. For example, an app for a light that displays different colors could help people create HomeKit scenes using colors imported from their photos.

**Be clear about what users can do in your app and when they should use the Home app.** For example, if your app supports only lights, you should consider encouraging people to create a "Movie Time" scene that not only dims the lights, but also closes the shades, and turns on the TV to a specific input. To do this, first guide people to set up a scene that includes only your accessory's actions—in this scenario, dimming the lights. Then, your app can suggest that people open the Home app to add their HomeKit-enabled shades and TV to the scene you helped them create. For guidance on how to refer to the Home app, see [Home app icon](https://developer.apple.com/design/human-interface-guidelines/homekit/overview/icons/#apple-home-app-icon) and [Editorial guidelines](https://developer.apple.com/design/human-interface-guidelines/homekit/overview/editorial/).

**Defer to HomeKit if your database differs from the HomeKit database.** Give people a seamless experience by automatically reflecting changes made in the Home app or in other third-party HomeKit apps. If you must ask people to manage conflicts in your app, present the conflict visually so that they have a clear picture of the choice they need to confirm. For example, if the user changes an accessory's service name in the Home app, your app can detect this change and could show both names side by side to confirm that the user wants to use the new name in your app, too.

**Ask permission to update the HomeKit database when users make changes in your app.**People should never be surprised by something that changes in the Home app, so it’s essential to get permission or an indication of intent before you write to the database. In particular, never overwrite HomeKit database settings without explicit direction from the user.

# **Cameras**

Your app can display still images or streaming video from a connected HomeKit IP camera.

**Don't block camera imagery.** It's fine to supplement the camera's content with useful features, such as an alert calling attention to potentially interesting activity. However, you should avoid covering portions of the camera's imagery with other content.

**Show a microphone button only if the camera supports bidirectional audio.** A non-functioning microphone button takes up valuable display space in your app and risks confusing people.
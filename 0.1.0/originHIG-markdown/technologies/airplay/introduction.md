# **[technologies-airplay] introduction**

## AirPlay lets people stream media content wirelessly from iOS, macOS, and tvOS devices to Apple TV, HomePod, and AirPlay-enabled TVs and speakers.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-AirPlay-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-AirPlay-intro_2x.png)

If your app provides media playback, support AirPlay streaming — not just mirroring — for the best user experience.

To support media playback and AirPlay, adopt the following frameworks:

- [AVFoundation](https://developer.apple.com/documentation/avfoundation), for media playback
- [AVKit](https://developer.apple.com/documentation/avkit), for the built-in media player, which offers a standard set of user controls and supports features like chapter navigation, subtitles, closed captioning, and AirPlay streaming

**Use the system-provided media player.** The built-in media player accommodates the needs of most media apps and provides a consistent playback experience across the system. It's familiar, easy to implement, and adopts new features and improvements automatically. Custom players with unfamiliar interfaces can be confusing and frustrating to people. Design a custom video player only if your app’s needs aren't met by the system-provided player. For developer guidance, see [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller).

![https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_VideoScreen_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_VideoScreen_2x.png)

**Provide content in the highest possible resolution.** Your [HLS](https://developer.apple.com/documentation/http_live_streaming) (HTTP Live Streaming) playlist should include the full range of available resolutions so that people can experience your content in the resolution that's appropriate for the device they're using (AVFoundation automatically selects the resolution based on the device). If you don't include a range of resolutions, your content will look low quality when people stream it to a device that can play at higher resolutions. For example, content that looks great on iPhone at 720p will look low quality when people use AirPlay to stream it to a 4K TV.

# **Entering AirPlay**

**Provide an intuitive way to enter AirPlay.** Clearly display the control for entering AirPlay within your custom player UI.

**Use Apple-provided icons on controls that initiate AirPlay.** When you use the system-provided media player, the correct AirPlay icon displays automatically. If necessary, you can adjust the size and tint of the icon to match the appearance of your app. For developer guidance, see [AVRoutePickerView](https://developer.apple.com/documentation/avkit/avroutepickerview) and [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview).

![https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Video_Transparent.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Video_Transparent.svg)

AirPlay video

![https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Black_Transparent.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/airplay/images/AirPlay_Black_Transparent.svg)

AirPlay audio

**Position the AirPlay icon correctly.** In a custom player, match the icon positions used in the system-provided media player. Specifically, display the AirPlay icon in the lower left corner when the device is in portrait orientation and in the lower right corner when the device is in landscape orientation.

**Don't hide the AirPlay icon in a submenu or require people to use a control to see it.** If your app includes a control for initiating AirPlay, the system-provided icon should be visible on the control. Also, make sure the AirPlay icon is visible within the player UI.

**Ensure that custom controls for entering AirPlay are intuitive and behave as people expect.**Strive to match the appearance and behavior of the system-provided buttons, including distinct visual states that indicate when playback has been initiated, is occurring, or is unavailable.

# **During Playback**

**Support remote control events.** When you support remote control events, people can choose actions like play, pause, and fast forward on the lock screen, and through interaction with Siri or HomePod. For developer guidance, see [Remote Command Center Events](https://developer.apple.com/documentation/mediaplayer/remote_command_center_events).

**Don't stop playback when your app enters the background or when the device locks.** For example, people expect the TV show they started streaming from your app to continue while they check their mail or put their device to sleep. In this type of scenario, it's also crucial to avoid mirroring, because people don't want to stream other types of content without explicitly choosing to do so.

**Don't interrupt another app's playback unless your app is starting to play immersive media.**Although people can choose to play all new content, your app should not interrupt current playback by default. For example, if your app plays a video when it launches or auto-plays inline videos, you should play this content on only the local device, while allowing current playback to continue. For developer guidance, see [AVAudioSessionCategoryAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryambient?language=objc).

**Provide an interface for controlling media playback.** Your app should give people controls for performing common tasks during playback, like pause, play, skip, scrub, and exit. By default, the system-provided media player displays a screen that includes standard controls, and indicates playback is occurring on another device.

**Let people use other parts of your app during playback.** When AirPlay is active, your app should still be functional. If the user navigates away from the playback screen, make sure other in-app videos don't begin playing and interrupt the streaming content.

**Stream only expected content.** Disable streaming of content like background loops and short video experiences that make sense only within the context of the app itself. For developer guidance, see [usesExternalPlaybackWhileExternalScreenIsActive](https://developer.apple.com/documentation/avfoundation/avplayer/1624255-usesexternalplaybackwhileexterna).
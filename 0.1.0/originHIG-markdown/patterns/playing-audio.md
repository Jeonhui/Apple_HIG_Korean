# **[patterns] playing-audio**

# People expect rich audio experiences that automatically adjust when the context changes on the device.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-audio-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-playing-audio-intro-dark_2x.png)

Devices can play audio in a variety of ways, such as through internal or external speakers, headphones, and wirelessly through Bluetooth or AirPlay-enabled devices. To manipulate sound on their devices people use several types of controls, including volume buttons, the Ring/Silent switch on iPhone, headphone controls, the Control Center volume slider, and sound controls in third-party accessories. Whether sound is a primary part of your experience or an embellishment, you need to make sure it behaves as people expect as they make changes to volume and output.

**Silence.** People switch their device to silent when they want to avoid being interrupted by unexpected sounds like ringtones and incoming message tones. In this scenario, they also want to silence nonessential sounds, such as keyboard clicks, sound effects, game soundtracks, and other audible feedback. When a device is in silent mode, it should play only the audio that people explicitly initiate, like media playback, alarms, and audio/video messaging.

**Volume.** People expect their volume settings to affect all sound in the system — including music and in-app sound effects — regardless of the method they use to adjust the volume. An exception is the ringer volume on iPhone, which people can adjust separately in Settings.

**Headphones.** People use headphones to keep their listening private and to free their hands. When plugging in headphones, users expect sound to reroute automatically without interruption; when unplugging headphones, they expect playback to pause immediately.

# **Best practices**

**Adjust levels automatically when necessary — don’t adjust the overall volume.** Your app can adjust relative, independent volume levels to achieve a great mix of audio, but the system volume should always govern the final output.

**Permit rerouting of audio when possible.** People often want to select a different audio output device. For example, they may want to listen to music through their living room stereo, car radio, or Apple TV. Support this capability unless there’s a compelling reason not to.

**Use the system-provided volume view to let people make audio adjustments.** The volume view includes a volume-level slider and a control for rerouting audio output. You can customize the appearance of the slider. For developer guidance, see [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview).

**Choose an audio category that fits the way your app or game uses sound.** Depending on the audio category you choose, your app’s sounds can mix with other audio, play while your app is in the background, or stop when people set the Ring/Silent switch to silent. As much as possible, pick a category that helps your app meet people’s expectations. For example, don’t make people stop listening to music from another app if you don’t need to. For developer guidance, see [AVAudioSession.Category](https://developer.apple.com/documentation/avfaudio/avaudiosession/category).

**Respond to audio controls only when it makes sense.** People can control audio playback from outside your app’s interface — such as in Control Center or with controls on their headphones — regardless of whether your app is in the foreground or background. If your app is actively playing audio, in a clear audio-related context, or connected to a Bluetooth or AirPlay-enabled device, it’s fine to respond to audio controls. Otherwise, when people activate a control, avoid halting currently playing from another app.

**Avoid repurposing audio controls.** People expect audio controls to behave consistently in all apps, so it’s essential to avoid redefining the meaning of an audio control in your app. If your app doesn’t support certain controls, don’t respond to them.

**Consider creating custom audio player controls only if you need to offer commands that the system doesn’t support.** For example, you might want to define custom increments for skipping forward or backward, or present content that's related to the playing audio, such as a sports score.

**Let other apps know when your app finishes playing temporary audio.** If your app can temporarily interrupt the audio of other apps, be sure to flag your audio session in a way that lets other apps know when they can resume. For developer guidance, see [notifyOthersOnDeactivation](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactiveoptions/1616603-notifyothersondeactivation).

# **Handling interruptions**

Although most apps and games rely on the system’s default interruption behavior, you can customize this behavior to better accommodate your needs.

**Determine how to respond to audio-session interruptions.** For example, if your app enables recording or other audio-related tasks that people don’t want interrupted, you can tell the system to avoid interrupting the currently playing audio for an incoming call unless people choose to accept it. Another example is a VoIP app, which must end a call when people close the Smart Folio of their iPad while they’re using the built-in microphone. Closing the Smart Folio automatically mutes the iPad microphone and by default interrupts the audio session associated with it. If a VoIP app restarts the audio session when people reopen their Smart Folio, it risks invading people’s privacy by reenabling the microphone without their knowledge. You can inspect an audio-session interruption to help determine the right way to respond; for developer guidance, see [Responding to audio session interruptions](https://developer.apple.com/documentation/avfaudio/avaudiosession/responding_to_audio_session_interruptions).

**When an interruption ends, determine whether to resume audio playback automatically.** Sometimes, audio from a different app can interrupt the audio your app is playing. An interruption can be *resumable*, like an incoming phone call, or *nonresumable*, like when people start a new music playlist. Use the interruption type and your app’s type to decide whether to resume playback automatically. For example, a media playback app that’s actively playing audio when an interruption occurs can check to be sure the type is resumable before continuing playback when the interruption ends. On the other hand, a game doesn’t need to check the interruption type before automatically resuming playback, because a game plays audio without an explicit user choice. For developer guidance, see [shouldResume](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions/1616528-shouldresume).

# **Platform considerations**

# **iOS, iPadOS**

**Use the system’s sound services to play short sounds and vibrations.** For developer guidance, see [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio_services).

# **macOS**

In macOS, notification sounds mix with other audio by default.

# **tvOS**

In tvOS, the system plays audio only when people initiate it, through interactions within apps and games or when performing device calibrations. For example, tvOS doesn’t play sounds to accompany components like alerts or notifications.

# **watchOS**

In watchOS, the system manages audio playback. An app can play short audio clips while it’s active and running in the foreground, or it can play longer audio that continues even when people lower their wrist or switch to another app. For developer guidance, see [Playing background audio](https://developer.apple.com/documentation/watchkit/storyboard_support/playing_background_audio).

**Use the recommended encoding values for media assets.** Specifically, use the 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding) format to produce good-quality audio with lower data requirements.

**Consider** **presenting a Now Playing view so people can control current or recently played audio without leaving your app.** The system-provided Now Playing view also displays information about the current audio source — which might be another app on a person's Apple Watch or iPhone — and automatically selects the current or most recently used source. For developer guidance, see [Adding a Now Playing view](https://developer.apple.com/documentation/watchkit/storyboard_elements/adding_a_now_playing_view).

| Category | Meaning | Behavior |
| --- | --- | --- |
| Solo ambient | Sound isn’t essential, but it silences other audio. For example, a game with a soundtrack. | Responds to the silence switch.Doesn’t mix with other sounds.Doesn’t play in the background. |
| Ambient | Sound isn’t essential, and it doesn’t silence other audio. For example, a game that lets people play music from another app during gameplay in place of the game’s soundtrack. | Responds to the silence switch.Mixes with other sounds.Doesn’t play in the background. |
| Playback | Sound is essential and might mix with other audio. For example, an audiobook or educational app that teaches a foreign language, which people might want to listen to after leaving the app. | Doesn’t respond to the silence switch.May or may not mix with other sounds.Can play in the background. |
| Record | Sound is recorded. For example, a note-taking app that offers an audio recording mode. An app of this nature might switch its category to playback if it lets people play the recorded notes. | Doesn’t respond to the silence switch.Doesn’t mix with other sounds.Can record in the background. |
| Play and record | Sound is recorded and played, potentially simultaneously. For example, an audio messaging or video calling app. | Doesn’t respond to the silence switch.May or may not mix with other sounds.Can record and play in the background. |
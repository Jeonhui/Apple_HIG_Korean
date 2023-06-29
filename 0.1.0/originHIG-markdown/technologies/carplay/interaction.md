# **[technologies-carplay] interaction**

# **Audio**

Regardless of whether audio is a primary aspect of your app’s experience, you need to know how people expect audio to behave and meet those expectations.

**Transition to the Now Playing screen only when content is ready to play.** Due to buffering and network conditions, it may take several seconds for audio to begin playing after a user selects it. The user’s selection remains highlighted, and a spinning activity indicator is displayed until your app informs the system that the audio is ready to play.

**Start playback as soon as audio has sufficiently loaded, even if descriptive information is still loading.** Continue loading descriptive information in the background, and show it once it's available.

**Avoid beginning playback automatically.** Unless your app’s purpose is to play a single source of audio, or your app is resuming previously interrupted audio, it shouldn’t begin playback until the user initiates it.

**Resume audio playback after an interruption only when it's appropriate.** Temporary interruptions such as incoming phone calls are resumable. Permanent interruptions, such as a music playlist initiated by Siri, are nonresumable. When a resumable interruption occurs, your app should resume playback when the interruption ends if audio was actively playing when the interruption started.

**Adjust levels automatically when necessary, but not the overall volume.** Your app can adjust relative, independent volume levels to achieve a great mix of audio. However, the final output volume should always be controlled by the user.

**Use the system’s sound services for short sounds, such as a sound accompanying an alert.**For developer guidance, see [System Sound Services](https://developer.apple.com/documentation/audiotoolbox/system_sound_services).

If your app is an audio app, see [Audio apps](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/introduction#audio-apps) for related design guidance.

# **Car data**

Automaker apps that implement a custom data interface can integrate with a vehicle to retrieve and respond to data such as climate, radio information, speed, and GPS location. An app might offer a dashboard screen, for example, that presents climate and speed information in a highly visual manner.

**Respond gracefully when data is unavailable.** Data can become unavailable in the car for a variety of reasons, such as losing the GPS connection while driving through a tunnel. Make sure your app handles connection problems nonintrusively.

For guidance regarding the development of a custom data interface, see [ExternalAccessory](https://developer.apple.com/documentation/externalaccessory).

# **iPhone**

CarPlay shows compatible apps from the user’s connected iPhone on the car’s built-in display, applying simplified interfaces that are optimized for use while driving.

**Eliminate app interactions on iPhone when CarPlay is active.** CarPlay is the best and safest way to interact with apps while driving, and interactions should occur using the car’s built-in controls and display. Any required setup on iPhone should occur before the vehicle is in motion.

**Never lock the user out of CarPlay because the connected iPhone requires input.** Assume that the iPhone is inaccessible when CarPlay is active. If a problem must be resolved on the connected iPhone, let the user do so once the vehicle is stopped.

**Make sure your app works when the iPhone is locked or in the trunk.** When CarPlay is active, the user’s phone may be locked or otherwise inaccessible. Your app should function regardless.

# **Knobs and controls**

Vehicles that support CarPlay have physical controls (buttons, knobs, and touchpads, for example) that supplement the touchscreen and, in some cases, serve as the primary means of user input. At minimum, a Siri button, navigation controls, selection controls, and back controls are always present when physical controls provide the primary means of user input.

**Respond to media controls as expected.** If your app offers audio playback features, it should respond when the user presses a physical play, pause, next track, previous track, fast forward, and rewind button in the car. For developer guidance, see [MPRemoteCommandCenter](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter).

### **Focus-based navigation**

CarPlay has a focus model that helps people move through onscreen interface elements using a knob or touchpad when the built-in display doesn’t support touch interactions. By rotating a knob or swiping a touchpad, focus moves from element to element, stopping on a specific one. The user can then press the knob, tap the touchpad, or press a button to activate or interact with the element.

Play

**Position onscreen elements so the user can navigate logically from item to item.** Changes in focus should be predictable.

For developer guidance, see [UIFocusEnvironment](https://developer.apple.com/documentation/uikit/uifocusenvironment).

# **Touchscreen**

Users can interact with a CarPlay app by performing gestures on the car’s built-in touchscreen display. CarPlay supports both low-fidelity and high-fidelity touchscreen displays. High-fidelity screens have lower finger-tracking latency than low-fidelity screens, and therefore support more gestures. Depending on the display, CarPlay apps can respond single-finger gestures, as follows.

| Gesture | Usage | Low-fidelity screen | High-fidelity screen |
| --- | --- | --- | --- |
| Tap | Activates a control or selects an item. | ● | ● |
| Double-tap | Zooms in and centers content. | ● | ● |
| Touch and hold | Activates a control for a period of time. For example, touching and holding the Next Track button in the Music app fast-forwards the currently playing track. | ● | ● |
| Flick | Scrolls or pans quickly. |  | ● |
| Drag | Moves an element from side-to-side or drags an element across the screen. |  | ● |

**Minimize touchscreen interactions.** Don’t expect people to keep reaching out to touch the screen, especially while the car is in motion. Require as few manual interactions as possible to reach content and initiate functions.

# **Siri**

Siri is an essential feature of CarPlay that facilitates distraction-free, voice-driven app interactions. Certain types of apps can integrate with Siri to perform tasks in response to spoken commands and questions from users.

| Type of app | Supported Siri interactions |
| --- | --- |
| Automaker apps | Change the audio source.Change the climate.Change the defroster settings.Change seat settings.Change the radio station.Save and load driver profiles. |
| Messaging apps | Send messages.Read received messages. |
| Voice over Internet Protocol (VoIP) apps | Start audio calls. |

A voice command button on the steering wheel activates Siri, even when CarPlay isn’t visible on the car’s built-in display. Once activated, Siri handles the language processing and semantic analysis needed to turn spoken requests into actionable instructions your app can handle. You’re responsible for defining the tasks your app handles. Your app must validate the information it receives, provide information for Siri to present, and take action. While validating information, if something is missing or unclear, your app can instruct Siri to request confirmation or more information.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Siri_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Siri_2x.png)

**Respond quickly and minimize interaction.** People use Siri for convenience, so don't make them wait for a response. Your app should validate information and take action as quickly as possible after receiving a request. When clarification or additional information is needed, present efficient, focused choices that reduce the possibility of additional prompting.

**Increase accuracy with custom vocabulary.** Help Siri learn more about the actions your app performs by defining specific terms people might use in requests. These terms should be nongeneric and unique to your app. Never include other app names, terms that are obviously connected with other apps, inappropriate language, or reserved phrases, such as “Hey Siri.” Note that any terms you define are used by Siri to help resolve requests, but aren’t guaranteed to be recognized.
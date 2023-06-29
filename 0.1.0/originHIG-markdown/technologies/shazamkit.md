# **[technologies] shazamkit**

# ShazamKit enables audio recognition by matching an audio sample against the ShazamKit catalog or a custom audio catalog.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ShazamKit-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ShazamKit-intro_2x.png)

You can use ShazamKit to enable features like:

- Enhancing experiences with graphics that correspond with the genre of currently playing music
- Making media content accessible to people with hearing disabilities by providing closed captions or sign language that syncs with the audio
- Synchronizing in-app experiences with virtual content in contexts like online learning and retail

If you need the device microphone to get audio samples for your app to recognize, you must request access to it. As with all types of permission requests, it’s important to help people understand why you’re asking for access. For guidance, see [Accessing private data](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data).

![https://developer.apple.com/design/human-interface-guidelines/technologies/shazamkit/images/mic-permission_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/shazamkit/images/mic-permission_2x.png)

# **Best practices**

After you receive permission to access the microphone for features that have ShazamKit enabled, follow these guidelines.

**Stop recording as soon as possible.** When people allow your app to record audio for recognition, they don’t expect the microphone to stay on. To help preserve privacy, only record for as long as it takes to get the sample you need.

**Let people opt in to storing your app’s recognized songs to their iCloud library.** If your app can store recognized songs to iCloud, give people a way to first approve this action. Even though both the Music Recognition control and the Shazam app show your app as the source of the recognized song, people appreciate having control over which apps can store content in their library.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*
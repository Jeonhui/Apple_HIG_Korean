# **[foundations] motion**

### On all platforms, beautiful, fluid motions bring the interface to life, conveying status, providing feedback and instruction, and enriching the visual experience.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-motion-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-motion-intro-dark_2x.png)

System components automatically include motion, letting you offer of familiar and consistent experiences throughout your app or game. As you design custom motion, focus on intentional animations that keep people oriented, provide clear feedback in response to their actions, and help them learn your interface without getting overwhelmed.

# **Best practices**

**Use motion to communicate.** Motion can be a great way to enhance feedback and understanding by showing how things change, what will happen when people perform an action, and what they can do next. For example, when people minimize a window in macOS, it moves smoothly from the desktop to the Dock so they know exactly where it went; when people set up Face ID, the system briefly describes what they need to do and helps them during scanning by visually changing the tick marks encircling their face.

**Add motion purposefully, supporting the experience without overshadowing it.** Don’t add motion for the sake of adding motion. Gratuitous or excessive animation can distract people or make them feel disconnected, especially in an app that doesn’t provide an immersive experience.

**Make motion optional.** There are several reasons why people might not see onscreen animations, so it’s essential to avoid using it as the only way to communicate important information. For example, when the Reduce Motion accessibility setting is on, be sure to minimize or eliminate animations. For guidance, see [Color and effects](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/#color-and-effects).

**Strive for realism and credibility.** Accurate, realistic motion can help people understand how something works, but motion that doesn’t make sense — or appears to defy physical laws — can make them feel disoriented. For example, if someone reveals a view by sliding it down from the top of the screen, they don’t expect to dismiss the view by sliding it to the side.

**Prefer quick, precise animations.** Animations that combine brevity and precision tend to feel more lightweight and less intrusive, and often convey information more effectively. For example, when people tap the list button in Weather on iPhone, the fullscreen view of the current city quickly transitions to the list view, pinpointing the city’s location in the list.

**In general, avoid adding motion to interactions that occur frequently.** The system already provides subtle animations for interactions with standard interface elements. Avoid making people spend extra time watching unnecessary motion every time they interact with something.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*

# **watchOS**

SwiftUI provides a powerful and streamlined way to add motion to your app. If you need to use WatchKit to animate layout and appearance changes — or create animated image sequences — follow these guidelines.

**NOTE**All layout- and appearance-based animations automatically include built-in easing that plays at the start and end of the animation. You can’t turn off or customize easing.

Using WatchKit, you can animate changes to the following attributes of your app's UI elements:

- Alignment
- Background color
- Group insets
- Height
- Opacity
- Accent color
- Width

WatchKit also lets you create an animated image sequence, which consists of two or more individual images displayed sequentially over time. Each image in the sequence constitutes a single frame of the animation, and the whole animation runs in a loop unless you modify the playback behavior at runtime. You install animated image sequences primarily in image, group, and button elements of your interface.

You can programmatically control the playback speed, direction, and frame rate of animated sequences for image and group elements. Other interface elements display the full animation in an endless loop.

**Store images in your watchOS app bundle when possible.** Storing images in your watchOS app bundle minimizes the delay in loading those images and showing the animation at runtime. Use this technique for animations that are part of your app’s design.

**Optimize all images in your image sequences.** Optimized images take less space on disk and load more quickly in some situations.

**Use the same image sequence for forward and reverse animations.** At runtime, you can animate image sequences in reverse, eliminating the need to provide a set of duplicate images in reverse order. Using this technique reduces the size of your app.
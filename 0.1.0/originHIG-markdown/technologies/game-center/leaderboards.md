# **[technologies-game-center] leaderboards**

Leaderboards can be a great way to encourage competition within your game. When you adopt Game Center and provide the relevant data, players can easily check their ranking against friends or global players.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboards_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboards_2x.png)

You can take advantage of the system-designed UI or present leaderboard information within custom UI. If necessary, you can also provide a custom link that takes players directly to the leaderboards area in the dashboard. For guidance, see [Custom dashboard links](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/custom-dashboard-links).

**Choose a leaderboard type that aligns with the core mechanics of your game.** Game Center supports a classic leaderboard that tracks all-time scores and a recurring leaderboard that resets based on an interval you define. For example, you might want your leaderboard to reset every other week, every day, or even every 5 minutes. Recurring leaderboards can increase engagement by giving players more chances to take the lead. For developer guidance, see [GKLeaderboard](https://developer.apple.com/documentation/gamekit/gkleaderboard).

# **Creating leaderboard images (optional)**

Although you don’t have to supply leaderboard images, doing so gives you another opportunity to offer beautiful artwork and reinforce your game’s visual aesthetic.

**Design high-quality artwork that echoes the in-game experience.** Players should be able to recognize your leaderboards at a glance.

**Aim to create a unique image for each leaderboard.** People often use these images to help them distinguish among leaderboards, so it’s a good idea to avoid reusing an image in multiple leaderboards. As you design individual images, keep in mind that players often see several leaderboards at the same time, so prefer complimentary images that work well as a set.

**Create leaderboard images in the appropriate size and format.** For games that run in iOS, iPadOS, and macOS, the system displays an individual leaderboard at its actual size, except for rounding both top corners. For leaderboards that are part of a set, the system crops the top and bottom of each image, leaving a rectangular area in the middle. To ensure that your primary content remains visible, make sure it stays within the cropped rectangle.

Use the following specifications to create leaderboard artwork for a game that runs in iOS, iPadOS, and macOS.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboard-image-layout-general_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboard-image-layout-general_2x.png)

| Attribute | Value |
| --- | --- |
| Format | PNG or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x320 pt (1024x640 px @2x) |

For games that run in tvOS, provide between one and three multilayer images for each leaderboard or leaderboard set in your game. The back layer of the art must be opaque. At runtime, a dark gradient may overlay your image from bottom to top, and you can place text above the bottom-right corner. Unlike achievement images, leaderboard images are focusable.

Because they’re focusable, you need to design leaderboards that remain easy to view while the focus effect moves and scales the images (to learn more about focus effects, see [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/inputs/focus-and-selection)). In addition, focusing may crop your leaderboard content at the edges of some layers. To ensure that your primary content stays comfortably visible while in focus, avoid placing it too close to the edges.

Use the following specifications to create leaderboard images for a game that runs in tvOS. You can also download a template from [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps) that can help you position content.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-multi-layered-leaderboard-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-multi-layered-leaderboard-image_2x.png)

| Attribute | Value |
| --- | --- |
| Aspect ratio | 16:9 |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 659x371 pt (1318x742 px @2x) |
| Focused size | 618x348 pt (1236x696 px @2x) |
| Unfocused size | 548x309 pt (1096x618 px @2x) |

# **Writing text that describes your leaderboards**

A leaderboard includes a title you can use to describe the area of competition.

**Be succinct and use correct capitalization.** A leaderboard truncates the title after two lines of text. Use title-style capitalization for the title and avoid capitalizing all letters.
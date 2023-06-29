# **[technologies-game-center] dashboard**

After players have signed into Game Center, they can launch the in-game dashboard by selecting the access point within your game. The dashboard is a full-screen view that appears on top of your game and gives players access to their Game Center profile and information.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/game-center-dashboard_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/game-center-dashboard_2x.png)

The dashboard — like the access point and other Game Center UI — uses a background material that adapts to the appearance of your game. The translucency of this material provides a sense of depth and helps remind players that they haven’t left your game.

**Pause your game while the dashboard is present.** Pausing your game helps you avoid potential performance impacts, but it also helps players focus on their Game Center information without feeling that the game is continuing without them.

If necessary, your game can include custom links that open the dashboard or take players directly to their Game Center profile. For guidance, see [Custom dashboard links](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/custom-dashboard-links).

# **Creating a dashboard image (tvOS)**

Games that run in tvOS can display an optional image at the top of the in-game dashboard.

**Use a simple, easily recognizable image that looks great at a distance.** Although you should avoid using your app icon for this image, you could use your game’s logo or word mark. To ensure that your image contrasts well with the dashboard appearance, consider using transparency to let the dashboard background to show through.

Use the following specifications to create a dashboard image.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-dashboard-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-dashboard-image_2x.png)

| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 600x180 pt (1200x360 px @2x) |

Custom dashboard artwork is not focusable.
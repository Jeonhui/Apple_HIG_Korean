# **[technologies-game-center] achievements**

Achievements can give players added incentive to stay engaged with your game. In iOS 14 and later, Game Center achievements appear in a collectible card format that highlights the player’s progress and showcases your artwork. Achievements are a prominent feature in Game Center UI, so it’s essential to design beautiful, high-quality assets that catch the eye and encourage players to return to your game.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievements-grouped_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievements-grouped_2x.png)

If necessary, your game can include a custom link that takes players directly to the achievements area in the dashboard. For guidance, see [Custom dashboard links](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/custom-dashboard-links).

# **Integrating your achievements into Game Center**

Game Center defines four achievement states: locked, in-progress, hidden, and completed. The system groups achievements by completion status, displaying completed achievements in the Completed group and all other achievements in the Locked group.

**Align your achievement types with Game Center achievement states.** The system displays achievements differently, depending on state. For example, an in-progress achievement includes a percentage value that shows how close players are to completion, whereas a locked achievement displays a padlock glyph. When you map your achievements to the four Game Center achievement states, you give players a consistent experience and you help them see at a glance the types of achievements your game offers.

**Determine a display order for your achievements.** The order in which you upload achievements is the order in which they’re displayed. For example, you might want your achievements to appear in an order that corresponds to the most common path through your game.

# **Creating great achievement images**

When players complete an achievement, the system moves the card that represents it into the Completed group, fills the card’s circular frame with your artwork, and adds a badge that displays the completion date. Achievement artwork is required when you adopt Game Center achievements.

**Design rich, high-quality images that complement your game and make players feel rewarded.** Providing beautiful achievements that reward a variety of gameplay styles and skill levels can encourage players to stay engaged with your game and earn more achievements. Because players appreciate earning unique achievements that remind them of each accomplishment, avoid reusing the same asset to represent more than one achievement. If you don’t provide an asset for an achievement, the card shows a placeholder image instead.

**Design a centered image for each achievement.** The system applies a circular mask to your achievement image, so be sure to keep primary content centered.

**Create achievement images in the appropriate size and format.** Use the following specifications to create opaque images for games that run in iOS, iPadOS, and macOS.

| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |

Use the following specifications to create an achievement image.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-achievement-image-layout_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-achievement-image-layout_2x.png)

| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 320x320 pt (640x640 px @2x) |
| Mask diameter | 200 pt (400 px @2x) |

In tvOS, achievement images aren’t focusable.

# **Writing text that describes your achievements**

Regardless of an achievement’s state, the card displays your title and description below the circular frame.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievement_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievement_2x.png)

**Be succinct.** The achievement card limits the title and description to two lines each. If your title or description wraps beyond two lines, the card truncates the text.

**Use correct capitalization styles.** In particular, avoid using all capital letters in your title and description. The achievement title should use title-style capitalization and the description should use sentence-style.

**Be creative with an achievement’s title, but straightforward with its description.** Although most players appreciate entertaining titles, they expect an achievement’s description to specify how to earn it.
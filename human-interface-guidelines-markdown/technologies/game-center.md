Game Center
===========

The GameKit framework supports Game Center, a social gaming network available for games running in iOS, iPadOS, macOS, tvOS, visionOS, and watchOS.![A sketch of the Game Center icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4df10f335123d3744626913e7fc71a02/technologies-Game-Center-intro@2x.png)

Players can use Game Center’s centralized service to connect to each other and to access their profile and game-related information across all Game Center games on their devices.

When you integrate Game Center into your game, you can take advantage of its social and multiplayer features without having to develop your own support for them. For example, you can use Game Center functionality to deliver:

* Your unique achievements
* Leaderboards that promote competition and comparison
* Rich multiplayer experiences

GameKit provides a full-featured UI that makes it easy to present Game Center highlights and experiences in consistent ways within your game. Alternatively, you can use GameKit APIs and Game Center data to present this functionality within your custom UI. For developer guidance, see [GameKit](/documentation/gamekit)
.

[Access point](/design/human-interface-guidelines/game-center#Access-point)
---------------------------------------------------------------------------

The Game Center *access point* is an Apple-designed UI element that lets players view their Game Center profile and information without leaving your game. After signing into Game Center on a device, players can use the access point within your game to launch the in-game [Dashboard](/design/human-interface-guidelines/game-center#Dashboard)
, where they can view and manage their profile and other game-related content.

To make sure that players can engage with their Game Center information without leaving your game, you need to include the access point in your interface and incorporate its behaviors into your game. The following guidelines can help you give players a consistent experience. For developer guidance, see [Adding an access point to your game](/documentation/gamekit/adding_an_access_point_to_your_game)
.

Note

If necessary, your game can include a custom link that opens the dashboard. For guidance, see [Custom dashboard links](/design/human-interface-guidelines/game-center#Custom-dashboard-links)
.

**Choose the information to present when the access point appears.** When it first appears, the access point can briefly display highlights that are relevant in your game, like players’ overall achievement progress or their standing among friends in the default leaderboard.

![A screenshot of the main menu screen of the game called The Coast, shown in landscape orientation on iPhone. The menu screen shows an expanded access point in the upper-left corner, the title in the middle of the screen, and the words Single and Multiplayer below the title. The access point shows a player avatar and includes the text 21 out of 50 achievements complete.](https://docs-assets.developer.apple.com/published/d48507c9229434ea7577ad67139f08cd/access-point-expanded-greeting@2x.png)After displaying your relevant Game Center updates, the access point shrinks to display only the player’s profile avatar. Because players frequently view their avatar in the collapsed access point, they learn to associate it with Game Center highlights. Players can always launch the in-game dashboard by choosing the access point, regardless of its current appearance.

**Display the access point in your main menu.** Players typically view your main menu every time they start your game, so using this location for the access point can help them remember where to find it. Avoid displaying the access point in splash screens, cinematic flows, tutorials, or other content that might precede your game’s main menu screen. If you can’t add the access point to your game menu, you can add it to your settings area instead.

![A screenshot of the main menu screen of the game called The Coast, shown in landscape orientation on iPhone. The menu screen shows a collapsed access point in the upper-left corner, the title in the middle of the screen, and the words Single and Multiplayer below the title. The access point shows only the player avatar.](https://docs-assets.developer.apple.com/published/04a3be5e50fe3432b32c71d1cbd5c15c/access-point-corner-placement@2x.png)**Hide the access point when players leave your menu.** When players leave the main menu to play your game, they’re focused on gameplay, not Game Center. Players know that they can always view their progress and open the dashboard by revisiting your menu, so there’s no need to include the access point elsewhere.

**Place the access point in a corner of your game menu window or view.** You can choose the corner that works best with your menu interface.

**Avoid placing game controls near the access point.** To help you prevent game controls from encroaching on the access point, consider defining a *safe area*. A safe area helps you ensure that there’s enough room for both the collapsed and expanded versions of the access point, in addition to Game Center achievement notifications that you might want to appear during gameplay.

On iPhone, the width of the expanded access point is 335 points and the height is 62 points, in both landscape and portrait orientations. In general, it’s a good idea to avoid the area at the top of the screen that has a height of 91 points in landscape and 114 points in portrait.

* [Portrait](#)
* [Landscape](#)
![An illustration that shows the safe area on iPhone in portrait orientation. An area at the top of the screen, above the safe area, includes an expanded access point. Callouts specify the height and width of the access point, and the distance between the safe area and the top of the screen.](https://docs-assets.developer.apple.com/published/837ad9bb00f6250feae453a67d8feb05/access-point-portrait-safe-areas@2x.png)

![An illustration that shows the safe area on iPhone in landscape orientation. An area at the top of the screen, above the safe area, includes an expanded access point. Callouts specify the height and width of the access point, and the distance between the safe area and the top of the screen.](https://docs-assets.developer.apple.com/published/df2b91a65b98966c7fb49c3c89da79ca/access-point-landscape-safe-areas@2x.png)

[Dashboard](/design/human-interface-guidelines/game-center#Dashboard)
---------------------------------------------------------------------

After players sign in to Game Center, they can launch the in-game dashboard by selecting the access point within your game. The dashboard is a full-screen view that appears on top of your game and gives players access to their Game Center profile and information. For developer guidance, see [Displaying the Game Center dashboard](/documentation/gamekit/displaying_the_game_center_dashboard)
.

![A screenshot of an in-game dashboard in a game called The Coast, shown in landscape orientation on iPhone. The dashboard includes an avatar, player name, achievements, friends, and recent activity.](https://docs-assets.developer.apple.com/published/fbcc74c2d6df759f5a2ac4c4110e75da/game-center-dashboard@2x.png)The dashboard — like the access point and other Game Center UI — uses a background material that adapts to the appearance of your game. The translucency of this material provides a sense of depth and helps remind players that they haven’t left your game.

**Pause your game while the dashboard is present.** Pausing your game helps you avoid potential performance impacts, but it also helps players focus on their Game Center information without feeling that the game is continuing without them.

If necessary, your game can include custom links that open the dashboard or take players directly to their Game Center profile. For guidance, see [Custom dashboard links](/design/human-interface-guidelines/game-center#Custom-dashboard-links)
.

### [Creating a dashboard image (tvOS)](/design/human-interface-guidelines/game-center#Creating-a-dashboard-image-tvOS)

Games that run in tvOS can display an optional image at the top of the in-game dashboard.

**Use a simple, easily recognizable image that looks great at a distance.** Although you want to avoid using your app icon for this image, you could use your game’s logo or word mark. To ensure that your image contrasts well with the dashboard appearance, consider using transparency to let the dashboard background show through.

Use the following specifications to create a dashboard image.

![An illustration of a rectangle representing dashboard artwork on Apple TV. The rectangle includes text that denotes it's 600 points wide and 180 points tall.](https://docs-assets.developer.apple.com/published/438f3caaa842926ba5a0f54470c64373/tvos-dashboard-image@2x.png)



| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 600x180 pt (1200x360 px @2x) |

Custom dashboard artwork isn’t focusable.

[Achievements](/design/human-interface-guidelines/game-center#Achievements)
---------------------------------------------------------------------------

Achievements can give players added incentive to stay engaged with your game. Game Center achievements appear in a collectible card format that highlights the player’s progress and showcases your artwork. Achievements are a prominent feature in Game Center UI, so it’s essential to design high-quality assets that catch the eye and encourage players to return to your game. For developer guidance, see [Rewarding players with achievements](/documentation/gamekit/rewarding_players_with_achievements)
.

![A screenshot of an in-game dashboard in a game called The Coast, shown in landscape orientation on iPhone. The dashboard displays an achievements area that shows a row of individual achievements marked as completed or locked. Each achievement is displayed on a rounded-rectangular card. Completed achievements include a circular image in a frame in the top half of the card. Locked achievements include a lock glyph within a  circular frame. Text in the dashboard tells that player that one of 13 achievements are complete and provides encouraging text indicating that they're off to a great start.](https://docs-assets.developer.apple.com/published/c5ac64ad15f869906dcbc61ef1526085/achievements-grouped@2x.png)If necessary, your game can include a custom link that takes players directly to the achievements area in the dashboard. For guidance, see [Custom dashboard links](/design/human-interface-guidelines/game-center#Custom-dashboard-links)
.

### [Integrating your achievements into Game Center](/design/human-interface-guidelines/game-center#Integrating-your-achievements-into-Game-Center)

Game Center defines four achievement states: locked, in-progress, hidden, and completed. The system groups achievements by completion status, displaying completed achievements in the Completed group and all other achievements in the Locked group.

**Align your achievement types with Game Center achievement states.** The system displays achievements differently, depending on state. For example, an in-progress achievement includes a percentage value that shows how close players are to completion, whereas a locked achievement displays a padlock glyph. When you map your achievements to the four Game Center achievement states, you give players a consistent experience and you help them see at a glance the types of achievements your game offers.

**Determine a display order for your achievements.** The order in which you upload achievements is the order in which they’re displayed. For example, you might want your achievements to appear in an order that corresponds to the most common path through your game.

### [Creating great achievement images](/design/human-interface-guidelines/game-center#Creating-great-achievement-images)

When players complete an achievement, the system moves the card that represents it into the Completed group, fills the card’s circular frame with your artwork, and adds a badge that displays the completion date. Achievement artwork is required when you adopt Game Center achievements.

**Design rich, high-quality images that complement your game and make players feel rewarded.** Providing beautiful achievements that reward a variety of gameplay styles and skill levels can encourage players to stay engaged with your game and earn more achievements. Because players appreciate earning unique achievements that remind them of each accomplishment, avoid reusing the same asset to represent more than one achievement. If you don’t provide an asset for an achievement, the card shows a placeholder image instead.

**Design a centered image for each achievement.** The system applies a circular mask to your achievement image, so be sure to keep primary content centered.

**Create achievement images in the appropriate size and format.** Use the following specifications to create opaque images for games that run in iOS, iPadOS, and macOS.



| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |

Use the following specifications to create an achievement image for a game that runs in tvOS.

![An illustration of an achievement image layout that consists of a square with an outlined circle centered within it. The square represents the actual size of the image, which is 320 points square. The circle, which measures 200 points in diameter, represents the mask that’s applied to the image.](https://docs-assets.developer.apple.com/published/5c87f87262313d88e3f18db73c05e5e2/tvos-achievement-image-layout@2x.png)



| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 320x320 pt (640x640 px @2x) |
| Mask diameter | 200 pt (400 px @2x) |

In tvOS, achievement images aren’t focusable.

### [Writing text that describes your achievements](/design/human-interface-guidelines/game-center#Writing-text-that-describes-your-achievements)

Regardless of an achievement’s state, the card displays your title and description below the circular frame.

![An illustration of a single completed achievement card that shows a lighthouse in the circular frame, the title Passage Lighthouse, and the description Complete Level 1. Callouts indicate the positions of the title and description, which appear below the image.](https://docs-assets.developer.apple.com/published/bc539c143dd5294957ee4d0d9b75b718/achievement@2x.png)

**Be succinct.** The achievement card limits the title and description to two lines each. If your title or description wraps beyond two lines, the card truncates the text.

**Use correct capitalization styles.** In particular, avoid using all capital letters in your title and description. Use [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)
 for the achievement title and use sentence-style capitalization for the description.

**Be creative with an achievement’s title but straightforward with its description.** Although most players appreciate entertaining titles, they expect an achievement’s description to specify how to earn it.

[Leaderboards](/design/human-interface-guidelines/game-center#Leaderboards)
---------------------------------------------------------------------------

Leaderboards can be a great way to encourage competition within your game. When you adopt Game Center and provide the relevant data, players can easily check their ranking against friends or global players.

![A screenshot of an in-game dashboard in a game called The Coast, shown in landscape orientation on iPhone. The dashboard displays a leaderboards area, which shows four leaderboards and one partial leaderboard. Each leaderboard is displayed in a rounded-rectangular card and includes an image in the top half and text in the bottom half. In each card, the text provides the leaderboard title and describes the player’s standing in that competition.](https://docs-assets.developer.apple.com/published/c327c831a96fcf6c4b00fbdd2bb27bfc/leaderboards@2x.png)You can take advantage of the system-designed UI or present leaderboard information within custom UI. If necessary, you can also provide a custom link that takes players directly to the leaderboards area in the dashboard. For guidance, see [Custom dashboard links](/design/human-interface-guidelines/game-center#Custom-dashboard-links)
.

**Choose a leaderboard type that aligns with the core mechanics of your game.** Game Center supports a classic leaderboard that tracks all-time scores and a recurring leaderboard that resets based on an interval you define. For example, you might want your leaderboard to reset every other week, every day, or even every 5 minutes. Recurring leaderboards can increase engagement by giving players more chances to take the lead. For developer guidance, see [`GKLeaderboard`](/documentation/gamekit/gkleaderboard)
.

### [Creating leaderboard images (optional)](/design/human-interface-guidelines/game-center#Creating-leaderboard-images-optional)

Although you don’t have to supply leaderboard images, doing so gives you another opportunity to offer beautiful artwork and reinforce your game’s visual aesthetic.

**Design high-quality artwork that echoes the in-game experience.** You want players to be able to recognize your leaderboards at a glance.

**Aim to create a unique image for each leaderboard.** People often use these images to help them distinguish among leaderboards, so it’s a good idea to avoid reusing an image in multiple leaderboards. As you design individual images, keep in mind that players often see several leaderboards at the same time, so prefer complementary images that work well as a set.

**Create leaderboard images in the appropriate size and format.** For games that run in iOS, iPadOS, and macOS, the system displays an individual leaderboard at its actual size, rounding both top corners. For leaderboards that are part of a set, the system adjusts each image’s actual size by cropping its top and bottom, leaving a rectangular area in the middle. To ensure that your primary content remains visible, make sure it stays within the cropped rectangle.

Use the following specifications to create leaderboard artwork for a game that runs in iOS, iPadOS, and macOS.

![An illustration of the leaderboard artwork layout for games that run in iOS, iPadOS, and macOS. The illustration consists of a square that contains a smaller, centered rectangle. The square measures 512 points per side and represents the actual size of the image. The rectangle represents the area visible after cropping, which is 512 points wide and 320 points tall.](https://docs-assets.developer.apple.com/published/128c801fe9906251a2d35964d8f3972c/leaderboard-image-layout-general@2x.png)



| Attribute | Value |
| --- | --- |
| Format | PNG or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x320 pt (1024x640 px @2x) |

For games that run in tvOS, provide between one and three multilayer images for each leaderboard or leaderboard set in your game. The back layer of the art must be opaque. At runtime, a dark gradient may overlay your image from bottom to top, and you can place text above the bottom-right corner. Unlike achievement images, leaderboard images are focusable.

Because they’re focusable, you need to design leaderboards that remain easy to view while the focus effect moves and scales the images (to learn more about focus effects, see [Focus and selection](/design/human-interface-guidelines/focus-and-selection)
). In addition, focusing may crop your leaderboard content at the edges of some layers. To ensure that your primary content stays comfortably visible while in focus, avoid placing it too close to the edges.

Use the following specifications to create leaderboard images for a game that runs in tvOS. You can also download a template from [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps)
 that can help you position content.

![An illustration of the leaderboard artwork layout for games that run in tvOS. The diagram consists of a rectangle that contains a slightly smaller rectangle. The larger rectangle represents the actual size of the image, measuring 659 points wide and 371 points tall. The smaller rectangle represents the focused size, which is 618 points wide and 348 points tall. Within the smaller rectangle, dashes outline a slightly smaller rectangle that measures 548 points wide and 309 points tall, representing the unfocused size.](https://docs-assets.developer.apple.com/published/d1582495749fcc1221a4545851cb08d8/tvos-multi-layered-leaderboard-image@2x.png)



| Attribute | Value |
| --- | --- |
| Aspect ratio | 16:9 |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 659x371 pt (1318x742 px @2x) |
| Focused size | 618x348 pt (1236x696 px @2x) |
| Unfocused size | 548x309 pt (1096x618 px @2x) |

### [Writing text that describes your leaderboards](/design/human-interface-guidelines/game-center#Writing-text-that-describes-your-leaderboards)

A leaderboard includes a title you can use to describe the area of competition.

**Be succinct and use correct capitalization.** A leaderboard truncates the title after two lines of text. Use [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)
 for the title and avoid capitalizing all letters.

[Multiplayer](/design/human-interface-guidelines/game-center#Multiplayer)
-------------------------------------------------------------------------

Game Center supports real-time and turn-based multiplayer functionality. For developer guidance, see [Finding multiple players for a game](/documentation/gamekit/finding_multiple_players_for_a_game)
.

When you adopt Game Center’s full-featured UI, you can provide a familiar and consistent matchmaking experience. In particular, you can offer the built-in player picker view, which helps players find people for a match without leaving your game. The built-in picker view can list system-suggested contacts, Game Center friends, and players who recently participated in non-auto-matched games.

When you add support for SharePlay, players can automatically join a game with friends from a Messages conversation or during a group FaceTime call (for developer guidance, see [GroupActivities](/documentation/GroupActivities)
).

![A screenshot of a Game Center multiplayer lobby screen in a game titled The Coast, running in landscape orientation on iPhone. The screen shows four player slots, each represented by a rounded-rectangular card. The leftmost card represents the current player. The middle two cards represent other players. The rightmost card represents a player set to be auto-matched. There are buttons at the bottom of the screen for inviting friends and starting the game.](https://docs-assets.developer.apple.com/published/b368874f73e68f7c15f86a2fb8c891f4/multiplayer-lobby@2x.png)When you adopt Game Center multiplayer functionality, you can use the system-designed multiplayer UI or present the information within your custom UI. Although the Game Center multiplayer UI supports the ability to send invitations to a player’s contacts, GameKit doesn’t provide API that lets you offer this functionality in a custom multiplayer UI.

**Provide an unambiguous button that lets players access the multiplayer lobby.** If your game supports a multiplayer experience, clearly display this option in your game’s main menu screen. For best results, use the term *Multiplayer*.

**Provide a rich preview image to customize a Messages-based invitation experience.** If players can use Messages to invite other people to a match, supply an image that represents your game to help customize the experience. Create an image that measures 480x480 pt (960x960 px @2x), name it `GKMessageImage.png`, and add it to your game’s [asset catalog](https://help.apple.com/xcode/mac/current/#/dev10510b1f7)
.

![An illustration representing a preview image for a game. The image features a red lighthouse and an attached red and white building. A rocky coast and some water are visible at the bottom of the image and a blue sky, the sun, and a cloud appear behind and above the buildings.](https://docs-assets.developer.apple.com/published/da695cb1486788149d4ee1bc0ff7511c/message-image-invitation@2x.png)

[Custom dashboard links](/design/human-interface-guidelines/game-center#Custom-dashboard-links)
-----------------------------------------------------------------------------------------------

Players can always use the access point to launch the dashboard without leaving your game, but you might need to provide custom UI that opens the dashboard or deep-links to an area within it, like leaderboards. If custom links are necessary in your game, it’s important to provide a familiar user experience that doesn’t confuse players. To ensure consistency, use the artwork that Game Center provides and use the correct terms to refer to each Game Center area.

**Use only Game Center–provided artwork in custom UI that opens the dashboard.** [Apple Design Resources](https://developer.apple.com/design/resources/)
 provides downloadable Game Center artwork you can use in your custom UI. For example, you can download artwork for custom UI that links to achievements, leaderboards, the player’s Game Center profile, and the dashboard itself. Be sure to use each art file for the appropriate area; for example, don’t use the dashboard art file in a button that opens the leaderboards section. In particular, don’t use the player’s Game Center avatar in a custom button that opens the player’s profile. Reusing the avatar can cause players to confuse your button with the access point, which creates an inconsistent user experience.

**Respect the appearance of Game Center artwork.** Don’t adjust the width, corner radius, or aspect ratio of the artwork; don’t add a trademark symbol or any other content; don’t add visual effects to the artwork, such as shadows, glows, or reflections; and don’t flip, rotate, or animate the artwork.

### [Referencing Game Center and dashboard areas](/design/human-interface-guidelines/game-center#Referencing-Game-Center-and-dashboard-areas)

The following guidelines describe how to use Game Center terminology correctly so that you can avoid confusing players.

**Don’t use the term *GameKit* in game UI.** GameKit is a developer-facing term that refers to the framework your game uses to integrate with Game Center. If you need to describe how your game works with the features GameKit provides, use the term *Game Center*. For example, you might say that your game “displays achievements in Game Center.”

**Use correct capitalization when using the term *Game Center*.** *Game Center* is two words, with an uppercase *G* and uppercase *C*, followed by lowercase letters. You can display *Game Center* entirely in uppercase only when you need to conform to an established typographic interface style, such as in a game that capitalizes all text.

**Use the system-provided translation of *Game Center*.** Avoid confusing players by referring to Game Center using the translation that they view on their device.

**Use correct terminology to refer to dashboard areas.** If you use different terms in your custom links to dashboard areas, players won’t be certain where the links will take them.



| Correct term | Examples of incorrect terms |
| --- | --- |
| Achievements | Awards, Trophies, Medals |
| Leaderboards | Rankings, Scores, Leaders |
| Game Center Profile | Profile, Account, Player Info |
| Game Center | Game Zone, Game Space, Play Center |
| Add Friends | Add, Add Profile, Add Buddies, Include Friends |

**Localize the correct terms.** When a term includes *Game Center*, use the system-provided translation of *Game Center* and localize the remaining terms, such as *Profile*.

[Platform considerations](/design/human-interface-guidelines/game-center#Platform-considerations)
-------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/game-center#Resources)
---------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/game-center#Related)

[Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps)


#### [Developer documentation](/design/human-interface-guidelines/game-center#Developer-documentation)

[GameKit](/documentation/gamekit)


[Create asset catalogs and sets](https://help.apple.com/xcode/mac/current/#/dev10510b1f7)


#### [Videos](/design/human-interface-guidelines/game-center#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/1A1DBC1F-F678-4E94-8B98-E5476E51B2EB/3659_wide_250x141_1x.jpg) Design for Game Center](https://developer.apple.com/videos/play/wwdc2020/10145) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/49/A3FBC918-45BC-4328-8140-928B1C64B7CD/3412_wide_250x141_1x.jpg) Tap into Game Center: Dashboard, Access Point, and Profile](https://developer.apple.com/videos/play/wwdc2020/10618) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/49/8F74DAC7-BC6B-4BD0-8697-7BF173C7E360/3792_wide_250x141_1x.jpg) Tap into Game Center: Leaderboards, Achievements, and Multiplayer](https://developer.apple.com/videos/play/wwdc2020/10619) 
[Change log](/design/human-interface-guidelines/game-center#Change-log)
-----------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| May 2, 2023 | Consolidated guidance into one page. |


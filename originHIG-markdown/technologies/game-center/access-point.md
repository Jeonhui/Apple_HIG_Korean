# **[technologies-game-center] access-point**

The Game Center *access point* is an Apple-designed UI element that lets players view their Game Center profile and information without leaving your game. After signing into Game Center on a device, players can use the access point within your game to launch the in-game [dashboard](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/dashboard), where they can view and manage their profile and other game-related content.

To make sure that players can engage with their Game Center information without leaving your game, you need to include the access point in your interface and incorporate its behaviors into your game. The following guidelines can help you give players a consistent experience. For developer guidance, see [GKAccessPoint](https://developer.apple.com/documentation/gamekit/gkaccesspoint).

**NOTE**If necessary, your game can include a custom link that opens the dashboard. For guidance, see [Custom dashboard links](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/custom-dashboard-links).

**Choose the information to present when the access point appears.** When it first appears, the access point can briefly display highlights that are relevant in your game, like players’ overall achievement progress or their standing among friends in the default leaderboard.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-expanded-greeting_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-expanded-greeting_2x.png)

After displaying your relevant Game Center updates, the access point shrinks to display only the player’s profile avatar. Because players frequently view their avatar in the collapsed access point, they learn to associate it with Game Center highlights. Players can always launch the in-game dashboard by choosing the access point, regardless of its current appearance.

**Display the access point in your main menu screen.** Players typically view your main menu every time they start your game, so using this location for the access point can help them remember where to find it. Avoid displaying the access point in splash screens, cinematic flows, tutorials, or other content that might precede your game’s main menu screen. If you can’t add the access point to your game menu, you can add it to your settings screen instead.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-corner-placement_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-corner-placement_2x.png)

**Hide the access point when players leave your menu screen.** When players leave the main menu to play your game, they’re focused on gameplay, not Game Center. Players know that they can always view their progress and open the dashboard by revisiting your menu screen, so there’s no need to include the access point elsewhere.

**Place the access point in a corner of the screen.** You can choose the corner that works best with the UI of your game menu screen.

**Avoid placing game controls near the access point.** To help you prevent game controls from encroaching on the access point, consider defining a *safe area*. A safe area helps you ensure that there’s enough room for both the collapsed and expanded versions of the access point, in addition to Game Center achievement notifications that you might want to appear during gameplay.

On iPhone, the width of the expanded access point is 335 points in landscape and 280 points in portrait. In general, it’s a good idea to avoid the area at the top of the screen that has a height of 91 points in landscape and 114 points in portrait.

• [Portrait](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/access-point#)
• [Landscape](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/access-point#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-portrait-safe-areas_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-portrait-safe-areas_2x.png)
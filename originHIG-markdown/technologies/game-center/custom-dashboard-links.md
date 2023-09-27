# **[technologies-game-center] custom-dashboard-links**

Players can always use the access point to launch the dashboard without leaving your game, but you might need to provide custom UI that opens the dashboard or deep-links to an area within it, like leaderboards. If custom links are necessary in your game, it’s important to provide a familiar user experience that doesn’t confuse players. To ensure consistency, use the artwork that Game Center provides and use the correct terms to refer to each Game Center area.

**Use only Game Center–provided artwork in custom UI that opens the dashboard.** [Apple Design Resources](https://developer.apple.com/design/resources/) provides downloadable Game Center artwork you can use in your custom UI. For example, you can download artwork for custom UI that links to achievements, leaderboards, the player’s Game Center profile, and the dashboard itself. Be sure to use each art file for the appropriate area; for example, don’t use the dashboard art file in a button that opens the leaderboards section. In particular, don’t use the player’s Game Center avatar in a custom button that opens the player’s profile. Reusing the avatar can cause players to confuse your button with the access point, which creates an inconsistent user experience.

**Respect the appearance of Game Center artwork.** Don’t adjust the width, corner radius, or aspect ratio of the artwork; don’t add a trademark symbol or any other content; don’t add visual effects to the artwork, such as shadows, glows, or reflections; and don’t flip, rotate, or animate the artwork.

# **Referencing Game Center and dashboard areas**

The following guidelines describe how to use Game Center terminology correctly so that you can avoid confusing players.

**Don’t use the term *GameKit* in game UI.** GameKit is a developer-facing term that refers to the framework your game uses to integrate with Game Center. If you need to describe how your game works with the features GameKit provides, use the term *Game Center*. For example, you might say that your game “displays achievements in Game Center.”

**Use correct capitalization when using the term *Game Center*.** *Game Center* is two words, with an uppercase G and uppercase C, followed by lowercase letters. You can display *Game Center*entirely in uppercase only when you need to conform to an established typographic interface style, such as in a game that capitalizes all text.

**Use the system-provided translation of *Game Center*.** Avoid confusing players by referring to Game Center using the translation that they view on their device.

**Use correct terminology to refer to dashboard areas.** If you use different terms in your custom links to dashboard areas, players won’t be certain where the links will take them.

| Correct term | Examples of incorrect terms |
| --- | --- |
| Achievements | Awards, Trophies, Medals |
| Leaderboards | Rankings, Scores, Leaders |
| Game Center Profile | Profile, Account, Player Info |
| Game Center | Game Zone, Game Space, Play Center |
| Add Friends | Add, Add Profile, Add Buddies, Include Friends |

**Localize the correct terms.** When a term includes *Game Center*, use the system-provided translation of *Game Center* and localize the remaining terms, such as *Profile*.
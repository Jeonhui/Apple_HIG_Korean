# **[technologies-game-center] multiplayer**

Game Center supports real-time and turn-based multiplayer functionality. When you adopt Game Center’s full-featured UI, you can provide a familiar and consistent matchmaking experience. In particular, you can offer the built-in player picker view, which helps players find people for a match without leaving your game. The built-in picker view can list system-suggested contacts, Game Center friends, and players who have recently participated in non-auto-matched games.

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/multiplayer-lobby_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/multiplayer-lobby_2x.png)

When you adopt Game Center multiplayer functionality, you can use the system-designed multiplayer UI or present the information within your custom UI. Although the Game Center multiplayer UI supports the ability to send invitations to a player’s contacts, GameKit doesn’t provide API that lets you offer this functionality in a custom multiplayer UI.

**Provide an unambiguous button that lets players access the multiplayer lobby.** If your game supports a multiplayer experience, clearly display this option in your game’s main menu screen. For best results, use the term “Multiplayer.”

**Provide a rich preview image to customize a Messages-based invitation experience.** If players can use Messages to invite other people to a match, supply an image that represents your game to help customize the experience. Create an image that measures 480x480 pt (960x960 px @2x), name it `GKMessageImage.png`, and add it to your game’s [asset catalog](https://help.apple.com/xcode/mac/current/#/dev10510b1f7).

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/message-image-invitation_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/message-image-invitation_2x.png)
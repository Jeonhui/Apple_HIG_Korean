# **[technologies-game-center] multiplayer**

Game Center supports real-time and turn-based multiplayer functionality. When you adopt Game Center’s full-featured UI, you can provide a familiar and consistent matchmaking experience. In particular, you can offer the built-in player picker view, which helps players find people for a match without leaving your game. The built-in picker view can list system-suggested contacts, Game Center friends, and players who have recently participated in non-auto-matched games.
> 게임 센터는 실시간 및 턴 기반 멀티플레이어 기능을 지원한다. 게임 센터의 모든 기능을 갖춘 UI를 채택하면 친숙하고 일관된 중매 경험을 제공할 수 있습니다. 특히 플레이어가 게임을 떠나지 않고도 경기할 사람을 찾을 수 있도록 도와주는 기본 제공 플레이어 선택 보기를 제공할 수 있습니다. 기본 제공된 선택 도구 보기에는 시스템에서 제안한 연락처, 게임 센터 친구 및 최근에 자동으로 일치하지 않는 게임에 참여한 플레이어를 나열할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/multiplayer-lobby_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/multiplayer-lobby_2x.png)

When you adopt Game Center multiplayer functionality, you can use the system-designed multiplayer UI or present the information within your custom UI. Although the Game Center multiplayer UI supports the ability to send invitations to a player’s contacts, GameKit doesn’t provide API that lets you offer this functionality in a custom multiplayer UI.
> 게임 센터 멀티 플레이어 기능을 채택하면 시스템 설계 멀티 플레이어 UI를 사용하거나 사용자 지정 UI 내에 정보를 표시할 수 있습니다. 게임 센터 멀티플레이어 UI는 플레이어의 연락처로 초대장을 보내는 기능을 지원하지만 게임킷은 사용자 지정 멀티플레이어 UI에서 이 기능을 제공할 수 있는 API를 제공하지 않습니다.
>




**Provide an unambiguous button that lets players access the multiplayer lobby.** If your game supports a multiplayer experience, clearly display this option in your game’s main menu screen. For best results, use the term “Multiplayer.”
> 플레이어가 멀티플레이어 로비에 액세스할 수 있는 명확한 단추를 제공하십시오. 게임에서 멀티플레이어 환경을 지원하는 경우 게임의 기본 메뉴 화면에 이 옵션을 명확히 표시하십시오. 최상의 결과를 얻으려면 "멀티 플레이어"라는 용어를 사용하십시오
>




**Provide a rich preview image to customize a Messages-based invitation experience.** If players can use Messages to invite other people to a match, supply an image that represents your game to help customize the experience. Create an image that measures 480x480 pt (960x960 px @2x), name it `GKMessageImage.png`, and add it to your game’s [asset catalog](https://help.apple.com/xcode/mac/current/#/dev10510b1f7).
> 메시지 기반 초대 환경을 사용자 지정할 수 있는 풍부한 미리 보기 이미지를 제공합니다. 플레이어가 메시지를 사용하여 다른 사람을 경기에 초대할 수 있는 경우 사용자 지정에 도움이 되도록 게임을 나타내는 이미지를 제공하십시오. 480x480pt(960x960px@2x) 크기의 이미지를 만들고 GKMessageImage.png으로 이름을 지정한 후 게임의 자산 카탈로그에 추가합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/message-image-invitation_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/message-image-invitation_2x.png)

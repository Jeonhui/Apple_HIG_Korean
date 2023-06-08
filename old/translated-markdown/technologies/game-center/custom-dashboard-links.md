# **[technologies-game-center] custom-dashboard-links**

Players can always use the access point to launch the dashboard without leaving your game, but you might need to provide custom UI that opens the dashboard or deep-links to an area within it, like leaderboards. If custom links are necessary in your game, it’s important to provide a familiar user experience that doesn’t confuse players. To ensure consistency, use the artwork that Game Center provides and use the correct terms to refer to each Game Center area.
> 플레이어는 게임을 종료하지 않고 액세스 지점을 사용하여 대시보드를 시작할 수 있지만 대시보드를 열거나 리더보드와 같은 대시보드 내 영역에 대한 심층 링크를 제공하는 사용자 지정 UI를 제공해야 할 수도 있습니다. 게임에서 사용자 지정 링크가 필요한 경우 플레이어를 혼란스럽게 하지 않는 친숙한 사용자 환경을 제공하는 것이 중요합니다. 일관성을 유지하려면 게임 센터에서 제공하는 아트워크를 사용하고 올바른 용어를 사용하여 각 게임 센터 영역을 참조하십시오.
>




**Use only Game Center–provided artwork in custom UI that opens the dashboard.** [Apple Design Resources](https://developer.apple.com/design/resources/) provides downloadable Game Center artwork you can use in your custom UI. For example, you can download artwork for custom UI that links to achievements, leaderboards, the player’s Game Center profile, and the dashboard itself. Be sure to use each art file for the appropriate area; for example, don’t use the dashboard art file in a button that opens the leaderboards section. In particular, don’t use the player’s Game Center avatar in a custom button that opens the player’s profile. Reusing the avatar can cause players to confuse your button with the access point, which creates an inconsistent user experience.
> 대시보드를 여는 사용자 지정 UI에서 게임 센터에서 제공하는 아트워크만 사용하십시오. Apple Design Resources는 다운로드 가능한 게임 센터 아트워크를 사용자 지정 UI에서 사용할 수 있습니다. 예를 들어 성과, 리더보드, 플레이어의 게임 센터 프로필 및 대시보드 자체에 연결되는 사용자 지정 UI에 대한 아트워크를 다운로드할 수 있습니다. 각 아트 파일을 해당 영역에 사용해야 합니다. 예를 들어, 리더보드 섹션을 여는 단추에서 대시보드 아트 파일을 사용하지 마십시오. 특히 플레이어의 프로필을 여는 사용자 지정 단추에서 플레이어의 게임 센터 아바타를 사용하지 마십시오. 아바타를 재사용하면 플레이어가 사용자의 버튼을 액세스 포인트와 혼동하여 일관성 없는 사용자 환경을 만들 수 있습니다.
>




**Respect the appearance of Game Center artwork.** Don’t adjust the width, corner radius, or aspect ratio of the artwork; don’t add a trademark symbol or any other content; don’t add visual effects to the artwork, such as shadows, glows, or reflections; and don’t flip, rotate, or animate the artwork.
> 게임 센터 아트워크의 모양을 존중합니다. 아트워크의 너비, 모서리 반지름 또는 가로 세로 비율을 조정하지 마십시오. 상표 기호나 다른 내용을 추가하지 마십시오. 그림자, 빛 또는 반사와 같은 시각적 효과를 아트워크에 추가하지 마십시오. 아트워크를 뒤집거나 회전하거나 애니메이션 작업하지 마십시오.
>




# **Referencing Game Center and dashboard areas**
> 게임 센터 및 대시보드 영역 참조
>




The following guidelines describe how to use Game Center terminology correctly so that you can avoid confusing players.
> 다음 지침에서는 플레이어를 혼동하지 않도록 게임 센터 용어를 올바르게 사용하는 방법에 대해 설명합니다.
>




**Don’t use the term *GameKit* in game UI.** GameKit is a developer-facing term that refers to the framework your game uses to integrate with Game Center. If you need to describe how your game works with the features GameKit provides, use the term *Game Center*. For example, you might say that your game “displays achievements in Game Center.”
> 게임 UI에서 GameKit라는 용어를 사용하지 마십시오. GameKit은 게임이 게임 센터와 통합하기 위해 사용하는 프레임워크를 가리키는 개발자 대면 용어입니다. 게임 키트가 제공하는 기능과 함께 게임이 작동하는 방식을 설명하려면 게임 센터라는 용어를 사용하십시오. 예를 들어, 게임이 "게임 센터에 성과를 표시"한다고 말할 수 있습니다
>




**Use correct capitalization when using the term *Game Center*.** *Game Center* is two words, with an uppercase G and uppercase C, followed by lowercase letters. You can display *Game Center*entirely in uppercase only when you need to conform to an established typographic interface style, such as in a game that capitalizes all text.
> Game Center라는 용어를 사용할 때는 올바른 대문자를 사용하십시오. Game Center는 대문자 G와 대문자 C 다음에 소문자를 사용합니다. 모든 텍스트를 대문자로 표시하는 게임과 같이 설정된 타이포그래피 인터페이스 스타일을 준수해야 하는 경우에만 Game Center를 대문자로 표시할 수 있습니다.
>




**Use the system-provided translation of *Game Center*.** Avoid confusing players by referring to Game Center using the translation that they view on their device.
> 게임 센터의 시스템 제공 번역을 사용하십시오. 플레이어가 단말기에서 보는 번역을 사용하여 게임 센터를 참조하여 플레이어를 혼란스럽게 하지 마십시오.
>




**Use correct terminology to refer to dashboard areas.** If you use different terms in your custom links to dashboard areas, players won’t be certain where the links will take them.
> 대시보드 영역을 참조하려면 올바른 용어를 사용하십시오. 대시보드 영역에 대한 사용자 지정 링크에서 다른 용어를 사용하면 링크가 어디로 이동할지 플레이어가 확신할 수 없습니다.
>




| Correct term | Examples of incorrect terms |
| --- | --- |
| Achievements | Awards, Trophies, Medals |
| Leaderboards | Rankings, Scores, Leaders |
| Game Center Profile | Profile, Account, Player Info |
| Game Center | Game Zone, Game Space, Play Center |
| Add Friends | Add, Add Profile, Add Buddies, Include Friends |

**Localize the correct terms.** When a term includes *Game Center*, use the system-provided translation of *Game Center* and localize the remaining terms, such as *Profile*.
> 올바른 용어를 현지화하십시오. 용어에 게임 센터가 포함된 경우 시스템에서 제공하는 게임 센터 번역을 사용하고 프로필과 같은 나머지 용어를 현지화하십시오.
>




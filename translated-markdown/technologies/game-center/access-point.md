# **[technologies-game-center] access-point**

The Game Center *access point* is an Apple-designed UI element that lets players view their Game Center profile and information without leaving your game. After signing into Game Center on a device, players can use the access point within your game to launch the in-game [dashboard](../technologies/game-center/dashboard), where they can view and manage their profile and other game-related content.
> 게임 센터 액세스 포인트는 플레이어가 게임을 떠나지 않고 게임 센터 프로필과 정보를 볼 수 있도록 하는 Apple이 설계한 UI 요소입니다. 장치에서 게임 센터에 로그인한 후 플레이어는 게임 내 액세스 지점을 사용하여 자신의 프로필 및 기타 게임 관련 콘텐츠를 보고 관리할 수 있는 게임 내 대시보드를 시작할 수 있습니다.
>




To make sure that players can engage with their Game Center information without leaving your game, you need to include the access point in your interface and incorporate its behaviors into your game. The following guidelines can help you give players a consistent experience. For developer guidance, see [GKAccessPoint](https://developer.apple.com/documentation/gamekit/gkaccesspoint).
> 플레이어가 게임을 떠나지 않고 게임 센터 정보에 참여할 수 있도록 하려면 인터페이스에 액세스 지점을 포함하고 해당 동작을 게임에 통합해야 합니다. 다음 지침은 플레이어에게 일관된 경험을 제공하는 데 도움이 될 수 있습니다. 개발자 지침은 GKAccessPoint를 참조하십시오.
>




**NOTE**If necessary, your game can include a custom link that opens the dashboard. For guidance, see [Custom dashboard links](../technologies/game-center/custom-dashboard-links).
> 참고필요한 경우 게임에 대시보드를 여는 사용자 지정 링크가 포함될 수 있습니다. 자세한 내용은 사용자 지정 대시보드 링크를 참조하십시오.
>




**Choose the information to present when the access point appears.** When it first appears, the access point can briefly display highlights that are relevant in your game, like players’ overall achievement progress or their standing among friends in the default leaderboard.
> 액세스 지점이 나타날 때 표시할 정보를 선택하십시오. 처음 나타날 때 액세스 지점은 플레이어의 전반적인 성취 진행 상황이나 기본 리더 보드에서 친구들 사이의 순위와 같은 게임과 관련된 강조 표시를 잠시 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-expanded-greeting_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-expanded-greeting_2x.png)

After displaying your relevant Game Center updates, the access point shrinks to display only the player’s profile avatar. Because players frequently view their avatar in the collapsed access point, they learn to associate it with Game Center highlights. Players can always launch the in-game dashboard by choosing the access point, regardless of its current appearance.
> 관련 게임 센터 업데이트를 표시한 후 액세스 지점이 축소되어 플레이어의 프로필 아바타만 표시됩니다. 플레이어는 붕괴된 액세스 포인트에서 아바타를 자주 보기 때문에 게임 센터 하이라이트와 연관시키는 법을 배웁니다. 플레이어는 현재 모습에 관계없이 언제든지 액세스 포인트를 선택하여 게임 내 대시보드를 실행할 수 있습니다.
>




**Display the access point in your main menu screen.** Players typically view your main menu every time they start your game, so using this location for the access point can help them remember where to find it. Avoid displaying the access point in splash screens, cinematic flows, tutorials, or other content that might precede your game’s main menu screen. If you can’t add the access point to your game menu, you can add it to your settings screen instead.
> 플레이어는 일반적으로 게임을 시작할 때마다 기본 메뉴를 표시하므로 이 위치를 액세스 지점으로 사용하면 액세스 지점을 찾을 수 있습니다. 게임의 기본 메뉴 화면 앞에 액세스 지점이 스플래시 화면, 영화 흐름, 자습서 또는 기타 콘텐츠에 표시되지 않도록 합니다. 게임 메뉴에 액세스 지점을 추가할 수 없는 경우 대신 설정 화면에 추가할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-corner-placement_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-corner-placement_2x.png)

**Hide the access point when players leave your menu screen.** When players leave the main menu to play your game, they’re focused on gameplay, not Game Center. Players know that they can always view their progress and open the dashboard by revisiting your menu screen, so there’s no need to include the access point elsewhere.
> 플레이어가 메뉴 화면에서 나갈 때 액세스 지점을 숨깁니다. 플레이어가 기본 메뉴에서 나와 게임을 실행하면 게임 센터가 아닌 게임플레이에 집중됩니다. 플레이어는 항상 메뉴 화면을 다시 방문하여 진행 상황을 보고 대시보드를 열 수 있으므로 다른 곳에 액세스 지점을 포함할 필요가 없습니다.
>




**Place the access point in a corner of the screen.** You can choose the corner that works best with the UI of your game menu screen.
> 화면 구석에 액세스 포인트를 배치합니다. 게임 메뉴 화면의 UI에 가장 잘 맞는 코너를 선택할 수 있습니다.
>




**Avoid placing game controls near the access point.** To help you prevent game controls from encroaching on the access point, consider defining a *safe area*. A safe area helps you ensure that there’s enough room for both the collapsed and expanded versions of the access point, in addition to Game Center achievement notifications that you might want to appear during gameplay.
> 게임 컨트롤을 액세스 지점 근처에 배치하지 마십시오. 게임 컨트롤이 액세스 지점을 침해하는 것을 방지하려면 안전 영역을 정의하는 것을 고려하십시오. 안전 영역을 사용하면 게임 플레이 중에 표시할 수 있는 게임 센터 달성 알림뿐만 아니라 축소 버전과 확장 버전의 액세스 포인트를 모두 저장할 수 있는 충분한 공간을 확보할 수 있습니다.
>




On iPhone, the width of the expanded access point is 335 points in landscape and 280 points in portrait. In general, it’s a good idea to avoid the area at the top of the screen that has a height of 91 points in landscape and 114 points in portrait.
> 아이폰에서 확장된 접속점의 폭은 가로 335점, 세로 280점이다. 일반적으로 화면 상단의 높이가 가로 91점, 세로 114점인 영역은 피하는 것이 좋다.
>




• [Portrait](../technologies/game-center/access-point#)
• [Landscape](../technologies/game-center/access-point#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-portrait-safe-areas_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/access-point-portrait-safe-areas_2x.png)
